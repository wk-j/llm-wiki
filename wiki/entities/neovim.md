---
title: Neovim
type: entity
tags: [editors, vim, neovim, tooling]
created: 2026-04-17
updated: 2026-04-17
sources: [vim-pack-guide.md]
---

# Neovim

Neovim is a hyperextensible, Lua-embedded fork of Vim, originally forked in 2014 to refactor Vim's C codebase and add an embedded scripting runtime. It is the de facto modern Vim for most users who want async, Lua configuration, built-in LSP, and tree-sitter.

## What makes it distinct from Vim

- **Embedded Lua runtime** — `init.lua` replaces `.vimrc` as the idiomatic config.
- **Built-in LSP client** — `vim.lsp` ships in core; servers configured via `vim.lsp.enable()` and `nvim-lspconfig`.
- **Built-in [[tree-sitter]]** — parsers, highlights, text objects.
- **`vim.loader`** — bytecode cache; `vim.loader.enable()` yields 20-30% startup improvement.
- **`runtimepath` conventions** — `lua/`, `plugin/`, `ftplugin/`, `after/` layout for discovering modules.

## Plugin ecosystem

Plugins are Git repositories laid out under `pack/<package>/{start,opt}/<plugin>/`. Historically managed by third-party tools (pathogen → vim-plug → packer.nvim → lazy.nvim). As of Neovim 0.12, the built-in [[vim-pack]] module provides install/load/update natively.

## Version 0.12

Shipped [[vim-pack]] as core. This is the first release where a capable plugin manager is part of Neovim itself — earlier versions had `:packadd` and the package standard, but no install/update UX.

## Position relative to other editors

- **Vim** — Neovim is a superset for most practical purposes; Vim 9 added Vim9script in response, keeping the lineage alive.
- **[[helix]]** — post-modern modal editor with no plugin system at all; ships LSP/tree-sitter as built-ins. A philosophical opposite of Neovim's "extensible by default" stance.
- **VS Code / Zed** — GUI editors with different extension models (Node.js/WASM); Neovim is often embedded inside them as a modal layer.

## See also

- [[vim-pack]]
- [[plugin-manager]]
- [[evgeni-chasnovski]]
- [[helix]]
- [[tree-sitter]]
