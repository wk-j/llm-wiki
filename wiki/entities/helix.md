---
title: Helix
type: entity
tags: [text-editors, modal-editing, rust, lsp, tree-sitter]
created: 2026-04-14
updated: 2026-04-14
sources: [Helix - Release 25.07 Highlights.md]
---

# Helix

A post-modern modal text editor written in Rust. Built-in support for multiple selections, [[tree-sitter]], Language Server Protocol (LSP), and experimental Debug Adapter Protocol (DAP).

## Key design choices

- **No plugin system** — features are built-in rather than requiring plugins (contrast with Neovim/Vim)
- **Multiple selections** as a first-class editing primitive (inspired by [[kakoune]])
- **Tree-sitter native** — syntax highlighting, indentation, textobjects all powered by [[tree-sitter]] queries
- **LSP native** — code actions, completions, diagnostics, document colors all built-in
- **Pickers** — telescope-like UI component used throughout (file picker, file explorer, symbol picker, etc.)

## Tree-sitter integration

Helix's tree-sitter integration has gone through several stages:

1. **Original**: Used official `tree-sitter` and `tree-sitter-highlight` Rust crates
2. **Forked highlighter**: Custom fork separating parsed trees from queries, inspired by Atom editor
3. **[[tree-house]]** (25.07): Ground-up rewrite as a standalone crate with proper injection tree, incremental re-parsing, and fixed locals scoping

## Links

- [GitHub](https://github.com/helix-editor/helix/)
- [Matrix community](https://matrix.to/#/#helix-community:matrix.org)
- [Website](https://helix-editor.com)

## See also

- [[tree-sitter]]
- [[tree-house]]
- [[helix-release-25-07]]
