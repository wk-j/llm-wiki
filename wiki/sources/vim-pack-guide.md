---
title: "A Guide to vim.pack"
type: source
tags: [neovim, vim, plugin-manager, lua, tooling]
created: 2026-04-17
updated: 2026-04-17
url: https://echasnovski.com/blog/2026-03-13-a-guide-to-vim-pack
date_published: 2026-03-13
sources: [A Guide to vim pack.md]
---

# A Guide to vim.pack

Blog post by [[evgeni-chasnovski|Evgeni Chasnovski]] (creator of mini.nvim) walking through [[vim-pack]], [[neovim|Neovim]] 0.12's built-in [[plugin-manager]]. Published 2026-03-13.

## What is vim.pack

A Lua module (`vim.pack`) shipped with Neovim 0.12 that handles plugin install, load, and update in one unified system. It is a *minimal* manager by design — no declarative lazy-loading DSL, no non-Git sources, no dependency resolution. It is "a smart `:packadd`" plus a lockfile plus an update UI.

## Design philosophy

- **Config is the source of truth.** The `init.lua` lists the plugins; the lockfile records versions.
- **All plugins installed as "opt"** under a single `core` package — lets users comment out a `vim.pack.add()` entry without accidentally breaking dependents that still load at startup.
- **Native integration** — stability guarantees match Neovim core.
- **Moderate lazy loading** — author warns against over-engineering; gains must beat cognitive cost.

## The API (very small)

```lua
vim.pack.add({ 'https://github.com/user/repo', ... })      -- install + load
vim.pack.update({ 'name' }, { force = ..., offline = ..., target = 'lockfile' })
vim.pack.del({ 'name' })
```

Plugin spec can be a Git URL string or a table with `src`, `version`, `name`. `version` supports refs (branch/tag/commit) or `vim.version.range('2.x')`.

Lockfile: `nvim-pack-lock.json` in config dir. Commit it; never edit by hand. Enables machine bootstrap, revert-to-lockfile, pinned versions.

## Hooks: autocmd-based

Two events: `PackChangedPre`, `PackChanged`. Event data carries `spec.name`, `active`, `kind` (`install`/`update`/`delete`).

Canonical example — rebuild Treesitter parsers after update:

```lua
vim.api.nvim_create_autocmd('PackChanged', { callback = function(ev)
  if ev.data.spec.name == 'nvim-treesitter' and ev.data.kind == 'update' then
    if not ev.data.active then vim.cmd.packadd('nvim-treesitter') end
    vim.cmd('TSUpdate')
  end
end })
```

**Critical ordering:** the autocmd must be registered *before* `vim.pack.add()` for install hooks to fire on first run.

## Configuration patterns

- **Single call**: one `vim.pack.add()` listing every plugin. Most robust; least modular.
- **Many calls**: one per file under `plugin/`, sourced alphabetically. Modular. Duplicate calls for the same plugin are safe (first one wins).
- **Lazy loading**: either `vim.schedule()` to defer off startup, or `nvim_create_autocmd` with `once = true` on an event (`CmdlineEnter`, `InsertEnter`, etc.).

## Update UX

`:lua vim.pack.update()` opens a buffer with per-plugin change summaries, `]]`/`[[` navigation, and a built-in LSP server providing symbols, hover, and code actions. Logs land in `nvim-pack.log`. Flags: `force`, `offline` (show state without fetching), `target = 'lockfile'` (revert).

`:checkhealth vim.pack` surfaces lockfile drift and inactive plugins.

## Migration notes

### From mini.deps (same author)
Syntax shifts: `MiniDeps.add('user/repo')` → `vim.pack.add({ 'https://github.com/user/repo' })`; `source`→`src`, `checkout`→`version`; hook functions → autocmd-based hooks; `MiniDeps.now/later()` → `MiniMisc.safely()`. Delete old `site/pack/deps` plugins before migration.

### From lazy.nvim
Features with no direct equivalent: `cmd`/`event`/`ft`/`keys` lazy triggers (→ manual autocmds), `opts` (→ explicit `setup()` calls), `dependencies` (→ list all plugins in one call, dependencies first).

**Performance:** lazy.nvim typically wins startup via aggressive lazy loading. `vim.pack` can close the gap with `vim.loader.enable()` (20-30% improvement) plus strategic manual lazy loading.

## Limitations

1. Git-only — no local paths, tarballs, LuaRocks.
2. All plugins are "opt" (by design).
3. Manual dependency ordering (dependencies listed first).
4. No declarative lazy-loading DSL.
5. `packspec` standardization (plugin-declared hooks/deps) is planned, not shipped.

## Key takeaways

- Ships with Neovim 0.12 — no bootstrapping needed.
- Designed for users who want the plugin manager to stay out of the way.
- Lockfile + `vim.pack.update()` UX rival dedicated managers.
- Trades declarative convenience (lazy.nvim) for mechanical transparency.

## See also

- [[vim-pack]]
- [[neovim]]
- [[evgeni-chasnovski]]
- [[plugin-manager]]
- [[helix]] — contrast: batteries-included editor with no plugin manager at all
