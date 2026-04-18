# A Guide to vim.pack (Neovim Built-in Plugin Manager)

**Source:** https://echasnovski.com/blog/2026-03-13-a-guide-to-vim-pack
**Author:** Evgeni Chasnovski
**Published:** 2026-03-13
**License:** CC BY-SA 4.0

---

## Overview

`vim.pack` is Neovim 0.12's built-in plugin manager, implemented in Lua as the `vim.pack` module. It combines installation, loading, and updates into a unified system.

## Core Concepts

### Lua Foundation
Requires basic Lua knowledge (tables, functions, `init.lua`). See `:h lua-concepts` and `:h lua-guide`.

### Runtime Files
Neovim discovers plugins via `'runtimepath'`, which includes:
- Lua modules (`lua/` subdirectories)
- Plugin scripts (`plugin/`)
- Filetype plugins (`ftplugin/`)

Key paths: user config (`~/.config/nvim`), data directory's `site/`, and `after/` for config overrides.

### Plugin Packages Structure
Plugins follow the Vim package standard under `pack/` with `start/` and `opt/` subdirs:
- **Start plugins**: load automatically at startup
- **Opt plugins**: load only via `:packadd`

`vim.pack` installs all plugins as "opt" plugins within a dedicated `core` package, so config comments can control loading.

## Installation and Loading

### Basic Usage
`vim.pack.add()` is a "smart `:packadd`"—installs missing plugins and loads them immediately:

```lua
vim.pack.add({
  'https://github.com/nvim-mini/mini.nvim',
  'https://github.com/neovim/nvim-lspconfig',
  'https://github.com/nvim-treesitter/nvim-treesitter',
})
```

Confirmation dialog: `y` to confirm, `n` to skip, `a` to allow all.

### Plugin Specifications

```lua
vim.pack.add({
  { src = 'https://github.com/nvim-mini/mini.nvim', version = 'stable' },
  { src = 'https://github.com/neovim/nvim-lspconfig', name = 'lspconfig' },
  'https://github.com/nvim-treesitter/nvim-treesitter',
})
```

`version` supports branches, tags, commits, or `vim.version.range('2.x')`.

### Lockfile
`nvim-pack-lock.json` records plugin state. Version-control it; never edit manually. Enables bootstrapping new machines, reverting updates, storing version targets.

## Configuration Organization

### Single `vim.pack.add()` Approach
One call with all plugins plus hooks defined beforehand.
- **Pros:** Robust, works with lazy-loaded plugins via lockfile, simplest setup.
- **Cons:** Not modular; loads all plugins at startup.

### Many `vim.pack.add()` Calls
Spread calls across `plugin/` directory files (sourced alphabetically).
Multiple calls for the same plugin are safe—only the first executes.

### Lazy Loading
Two strategies:

**Load after startup** (simpler):
```lua
vim.schedule(function()
  vim.pack.add({ 'https://github.com/nvim-mini/mini.cmdline' })
end)
```

**Load before needed** (event-based):
```lua
vim.api.nvim_create_autocmd('CmdlineEnter', {
  once = true,
  callback = function()
    vim.pack.add({ 'https://github.com/nvim-mini/mini.cmdline' })
    require('mini.cmdline').setup()
  end
})
```

Author recommends "moderate" lazy loading.

## Plugin Hooks

Actions triggered by `PackChangedPre` and `PackChanged` autocmds. Event data: plugin name/spec, active state, change kind (`install`/`update`/`delete`).

Example—update Treesitter parsers on plugin update:

```lua
vim.api.nvim_create_autocmd('PackChanged', { callback = function(ev)
  local name, kind = ev.data.spec.name, ev.data.kind
  if name == 'nvim-treesitter' and kind == 'update' then
    if not ev.data.active then vim.cmd.packadd('nvim-treesitter') end
    vim.cmd('TSUpdate')
  end
end })
```

**Critical:** Autocmds must be created **before** `vim.pack.add()` for install hooks to fire.

## Updates and Management

### Updating Plugins
```lua
:lua vim.pack.update()                       -- All plugins
:lua vim.pack.update({ 'mini.nvim' })        -- Specific
:lua vim.pack.update(nil, { force = true })  -- Skip confirmation
:lua vim.pack.update(nil, { offline = true })-- Current state only
:lua vim.pack.update(nil, { target = 'lockfile' }) -- Revert
```

Confirmation buffer shows change summaries, `]]`/`[[` navigation, built-in LSP (symbols, hover, code actions). Updates logged to `nvim-pack.log`.

### Deleting Plugins
1. Remove from config
2. `vim.pack.del({ 'plugin-name' })`

Never delete directories manually—leaves lockfile entries, causing reinstalls.

### Contributing to Installed Plugins
1. Create separate local plugin directory
2. Clone the plugin repo there
3. Comment out the `vim.pack.add()` call
4. Load via `vim.cmd.packadd('local-copy-name')`

## Troubleshooting

`:checkhealth vim.pack` detects:
- Missing/problematic lockfile entries
- Lockfile misalignment with disk
- Inactive (installed but unloaded) plugins

## Migration

### From mini.deps

| mini.deps | vim.pack |
|-----------|----------|
| `MiniDeps.add('user/repo')` | `vim.pack.add({ 'https://github.com/user/repo' })` |
| `source` | `src` |
| `checkout` | `version` |
| Hook functions | Autocommand-based hooks |
| `MiniDeps.now/later()` | `MiniMisc.safely()` |

### From lazy.nvim

| lazy.nvim feature | vim.pack alternative |
|---|---|
| `cmd`, `event`, `ft`, `keys` lazy triggers | Manual event-based loading |
| `opts` field | Post-`vim.pack.add()` setup calls |
| `dependencies` | List all plugins in single call |

**Performance note:** lazy.nvim usually wins on startup via aggressive lazy loading. `vim.pack` can match via `vim.loader.enable()` (20-30% improvement) plus strategic lazy loading.

## Limitations and Design Choices

1. **Git-only**: Only Git repos; other formats require manual installation.
2. **All plugins as "opt"**: Prevents config comments from breaking dependent functionality.
3. **Manual dependency resolution**: Dependencies must be listed first in `vim.pack.add()`.
4. **No declarative lazy loading**: Users must create autocmds.
5. **Future**: `packspec` standardization for plugin-defined hooks and dependency declarations.

## Key Takeaways

- **Simplicity first**: Start with single `vim.pack.add()`; modularize only if needed.
- **Config-driven**: The config file is the source of truth.
- **Reliable updates**: Lockfile ensures reproducibility across machines.
- **Moderate lazy loading**: Gains must balance configuration complexity.
- **Hook management**: Install hooks require autocmds defined before `vim.pack.add()`.
- **Native integration**: Built-in status means stability guarantees match Neovim core.
