---
title: Plugin Manager
type: concept
tags: [tooling, editors, package-management]
created: 2026-04-17
updated: 2026-04-17
sources: [vim-pack-guide.md]
---

# Plugin Manager

A plugin manager installs, loads, updates, and removes user-authored extensions for a host program — typically a text editor. In the Vim/Neovim world, it also decides *when* plugins load (startup vs. lazy) and manages lockfiles for reproducibility.

## Core responsibilities

1. **Fetch** — clone a repository (usually Git) into a known location.
2. **Load** — make the plugin visible on `runtimepath` so the editor finds its `plugin/`, `lua/`, `ftplugin/` files.
3. **Update** — fetch new commits, show a diff, let the user accept or reject.
4. **Pin** — record the installed version (lockfile) so a fresh machine produces an identical environment.
5. **Hook** — run user code before/after install/update/delete (e.g. `TSUpdate` after installing `nvim-treesitter`).

Advanced managers add:
- **Lazy loading** — defer plugin load until an event, command, filetype, or keypress fires.
- **Dependency resolution** — ensure plugin A loads before plugin B if B requires A.
- **Declarative specs** — DSL for lazy triggers and setup in a single table.

## The Neovim landscape

| Manager | Style | Notes |
|---|---|---|
| [[vim-pack]] | Minimal, built-in (Neovim 0.12+) | Three functions, lockfile, autocmd-based hooks. No declarative lazy DSL. |
| lazy.nvim | Rich declarative | Dominant third-party. `cmd`/`event`/`ft`/`keys` lazy triggers, `opts`, `dependencies`. |
| mini.deps | Minimal, Lua | [[evgeni-chasnovski\|Chasnovski]]'s precursor to vim.pack. |
| packer.nvim | Legacy | Archived in 2023; users migrate to lazy.nvim or vim.pack. |
| pathogen / vim-plug | Pre-Lua era | Vimscript; still widely used in plain Vim. |

## The central trade-off

Plugin managers span a spectrum from **mechanically transparent** (you write Lua that imperatively loads plugins) to **declaratively convenient** (you write a spec table, the manager figures out when and how).

- Transparent wins: config is the source of truth, hook ordering is obvious, no magic.
- Declarative wins: startup speed via aggressive lazy loading, less boilerplate, consistent shape.

[[vim-pack]] sits at the transparent end by design. `lazy.nvim` at the declarative end. Both are legitimate.

## Lockfiles

A lockfile records the exact commit of each installed plugin. It:
- Lets a new machine reproduce the current environment.
- Enables "revert latest update" workflows.
- Should be checked into version control.
- Should never be hand-edited.

[[vim-pack]] writes `nvim-pack-lock.json`; lazy.nvim writes `lazy-lock.json`.

## See also

- [[vim-pack]]
- [[neovim]]
- [[helix]] — alternative: a batteries-included editor that ships features as built-ins rather than plugins
