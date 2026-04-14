---
title: Tree-house
type: concept
tags: [parsing, syntax-highlighting, text-editors, helix, tree-sitter]
created: 2026-04-14
updated: 2026-04-14
sources: [Helix - Release 25.07 Highlights.md]
---

# Tree-house

A Rust crate ([`tree-house`](https://github.com/helix-editor/tree-house)) built by the [[helix]] team as a ground-up replacement for their forked `tree-sitter-highlight` highlighter. Introduced in Helix 25.07.

## Architecture

Tree-house separates parsing from querying (what worked well in the old approach) while fixing fundamental design issues.

**Injection tree**: The core `Syntax` type represents a parsed document as a tree of layers. The root layer covers the full document in its primary language. Child layers represent injections (e.g. JavaScript inside HTML `<script>` tags). Each layer has its own [[tree-sitter]] syntax tree — a "tree of trees." Layer lookup is O(log n) instead of O(n).

**`TreeCursor`**: Mirrors Tree-sitter's `TreeCursor` API but crosses injection layer boundaries transparently.

**`QueryIter`**: Runs any query across all injection layers — not just highlights. Enables features like indentation and textobjects to respect language boundaries in injected code.

## Key improvements over the old highlighter

- **Incremental injections**: Only re-parses layers that actually changed from edits. The old approach did unnecessary work across all layers.
- **Locals fix**: `locals.scm` definitions (e.g. parameter names) are tracked at parse-time and stored in a tree. Parameter highlights no longer disappear when the definition scrolls out of view.
- **Nested injections**: Handles deep nesting robustly (Rust → doc comment Markdown → code fence Rust).
- **Future**: Opens the door for parallel parsing.

## See also

- [[tree-sitter]]
- [[helix]]
- [[helix-release-25-07]]
