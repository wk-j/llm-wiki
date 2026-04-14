---
title: "Helix Release 25.07 Highlights"
type: source
tags: [text-editors, tree-sitter, lsp, modal-editing]
created: 2026-04-14
updated: 2026-04-14
sources: [Helix - Release 25.07 Highlights.md]
---

# Helix Release 25.07 Highlights

Source: [helix-editor.com release notes](https://helix-editor.com/news/release-25-07-highlights/), published 2025-07-15. 195 contributors.

## Key features

### File explorer

New `<space>e` picker for hierarchical directory browsing. Unlike the recursive file picker (`<space>f`), this opens one directory at a time — more precise for large projects.

### LSP document colors

Helix now requests `textDocument/documentColor` from language servers (e.g. `tailwindcss-language-server`) and renders inline color swatches, similar to inlay hints but for RGB colors.

### Command mode rewrite

Complete rewrite of command-line parsing, fixing bugs (e.g. filenames with spaces) and adding:

- **Flags**: CLI-style flags for typable commands. `:rsort` replaced by `:sort --reverse`. `:write` family gains `--no-format`. Flags auto-complete.
- **Expansions**: Interpolation syntax inspired by [[kakoune]]. `%{buffer_name}`, `%{cursor_line}` for editor state. `%sh{...}` for shell commands. `%u{...}` for Unicode. Example: `:echo %sh{git blame -L %{cursor_line},+1 %{buffer_name}}`
- **Extensible parsing**: `:set-option` uses `serde_json` streaming deserializer. Shell commands (`:run-shell-command`, `:pipe`) pass arguments raw — no double-escaping.

## Tree-house

The biggest change: replacement of the forked `tree-sitter-highlight` crate with [[tree-house]], a new crate built from scratch.

### Why replace the old highlighter?

The original highlighter was a fork of `tree-sitter-highlight` that separated parsed trees from queries (inspired by the Atom editor). Over time it became unmaintainable — longstanding bugs were incompatible with its design.

### What Tree-house improves

- **Injection tree**: Layers (root language + injected languages) form a tree structure. Lookup is logarithmic instead of linear scan.
- **Incremental injections**: Only re-parses and reruns injection queries for layers that actually changed. Editing one list item in a large Markdown document only re-parses root + that inline layer.
- **Locals fix**: Parameter highlights (from `locals.scm`) no longer disappear when the definition scrolls out of view. Definitions are tracked at parse-time and stored in a tree for fast lookup.
- **Cross-injection queries**: New `TreeCursor` and `QueryIter` types work across injection layers seamlessly. Future: all [[tree-sitter]]-based features (indentation, textobjects, code folding) should respect language boundaries in injected code.
- **Nested injections**: Supports deeply nested cases like Rust doc comments containing Markdown containing Rust code fences.

## See also

- [[helix]]
- [[tree-sitter]]
- [[tree-house]]
