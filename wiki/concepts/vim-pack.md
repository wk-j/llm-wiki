---
title: vim.pack
type: concept
tags: [neovim, plugin-manager, lua, tooling]
created: 2026-04-17
updated: 2026-04-17
sources: [vim-pack-guide.md]
---

# vim.pack

`vim.pack` is the built-in [[plugin-manager]] shipped with [[neovim|Neovim]] 0.12, implemented as a Lua module. It combines install, load, and update into one API deliberately smaller than third-party managers like `lazy.nvim` or `packer.nvim`.

## Public API

Three functions cover everything:

| Function | Purpose |
|---|---|
| `vim.pack.add(specs)` | Install any missing plugins and `packadd` them. Idempotent — safe to call multiple times for the same plugin. |
| `vim.pack.update(names?, opts?)` | Fetch and apply updates. Opts: `force`, `offline`, `target = 'lockfile'`. |
| `vim.pack.del(names)` | Remove installed plugins (after removing from config). |

A spec is either a Git URL string or a table: `{ src = '...', version = 'stable' \| 'v2.0' \| vim.version.range('2.x'), name = '...' }`.

## Architecture

- **All plugins installed as "opt"** under a single `core` package directory. This means commenting out a `vim.pack.add()` call cleanly disables the plugin — nothing auto-loads from `pack/start/`.
- **Lockfile** (`nvim-pack-lock.json`) in the config dir records exact versions. Commit it; never hand-edit.
- **Hooks** fire through `PackChangedPre` / `PackChanged` autocmds carrying `spec.name`, `active`, `kind` ∈ {`install`, `update`, `delete`}.
- **Health check** via `:checkhealth vim.pack` flags lockfile drift and inactive plugins.

## Design trade-offs

What `vim.pack` deliberately omits vs. `lazy.nvim`:

| Omitted feature | Rationale / workaround |
|---|---|
| Declarative lazy-loading (`cmd`/`event`/`ft`/`keys`) | Hand-write autocmds with `once = true`. Keeps behavior transparent. |
| `opts` field for setup | Call `require('plugin').setup({...})` yourself after `vim.pack.add()`. |
| `dependencies` graph | List dependencies first in the same `vim.pack.add()` call. |
| Non-Git sources | Git only; other sources require manual `pack/*/opt/` install. |
| Plugin-declared hooks | Planned as `packspec`; not yet shipped. |

The trade is **mechanical transparency over declarative convenience** — the config file shows exactly what runs and when.

## Lazy-loading patterns

Because there's no DSL, lazy loading is just Lua:

```lua
-- Defer past startup
vim.schedule(function()
  vim.pack.add({ 'https://github.com/nvim-mini/mini.cmdline' })
end)

-- Event-gated (one-shot)
vim.api.nvim_create_autocmd('CmdlineEnter', {
  once = true,
  callback = function()
    vim.pack.add({ 'https://github.com/nvim-mini/mini.cmdline' })
    require('mini.cmdline').setup()
  end,
})
```

Author [[evgeni-chasnovski|Chasnovski]]'s guidance: lazy-load *moderately*. Startup wins rarely justify heavy configuration complexity; `vim.loader.enable()` alone recovers 20-30%.

## Hook ordering gotcha

Install hooks only fire if the `PackChanged` autocmd exists **before** `vim.pack.add()` runs. The single-call config pattern (define all autocmds → call `vim.pack.add()` once) makes this trivial; scattered `plugin/*.lua` files require more care.

## Relationship to other managers

- **mini.deps** — predecessor by same author. `vim.pack` is a conceptual successor built into core. Migration is mostly renames (`source`→`src`, `checkout`→`version`) plus converting hook functions to autocmds.
- **lazy.nvim** — the dominant third-party manager. Faster startup via aggressive declarative lazy loading; richer spec DSL. `vim.pack` matches performance with care but never matches declarative power.
- **packer.nvim** — archived; `vim.pack` fills its niche for users who want a simple built-in option.

## Positioning

`vim.pack` is for users who treat plugin management as plumbing, want native stability guarantees, and prefer explicit Lua over declarative specs. It does not try to replace `lazy.nvim` for users who want its ergonomics.

## See also

- [[vim-pack-guide]]
- [[neovim]]
- [[evgeni-chasnovski]]
- [[plugin-manager]]
