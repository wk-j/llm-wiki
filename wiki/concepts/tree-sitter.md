---
title: Tree-sitter
type: concept
tags: [parsing, syntax-highlighting, text-editors, developer-tools]
created: 2026-04-14
updated: 2026-04-14
sources: [Helix - Release 25.07 Highlights.md]
---

# Tree-sitter

A framework for generating and using fast, error-tolerant parsers. You define a parser in a `grammar.js` file using the Grammar DSL, then use `tree-sitter` CLI tools to generate and test it.

## How it works

- **Incremental parsing**: Given the old syntax tree, Tree-sitter parses edits faster by reusing unchanged subtrees
- **Error-tolerant**: Produces a syntax tree even when source code has syntax errors — critical for editor use
- **Concrete syntax trees**: Produces full CSTs (not ASTs), preserving all tokens including whitespace and punctuation

## Queries

Tree-sitter queries (`*.scm` files) pattern-match against subtrees and capture nodes. Common query types:

| Query file | Purpose |
|---|---|
| `highlights.scm` | Map syntax nodes to highlight groups (keywords, strings, types, etc.) |
| `injections.scm` | Identify ranges that should be parsed as a different language |
| `locals.scm` | Track variable definitions and references for scope-aware highlighting |
| `indents.scm` | Define indentation rules based on syntax |
| `textobjects.scm` | Recognize structural units (functions, classes, parameters) for selection |

## Injections

Injections allow nested languages within a document. A Markdown code fence with a language tag triggers the injection of that language's parser for the fenced content. Injections can nest arbitrarily deep (e.g. Rust → doc comment Markdown → code fence Rust).

**Combined injections**: Multiple disjoint ranges (e.g. all doc comment lines in a function) treated as a single document for the injected parser.

## Adoption

- **Editors**: [[helix]], Neovim, Zed, Atom (defunct), Nova
- **Diff tools**: Difftastic (syntax-aware diffs)
- **Language servers**: Codebook (syntax-aware spell checking)
- **Platforms**: GitHub uses tree-sitter for code navigation and highlighting

## See also

- [[tree-house]]
- [[helix]]
