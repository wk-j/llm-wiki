---
title: "I Made a Terminal Pager — Leo Robinovitch"
type: source
tags: [tui, terminal, go, text-navigation, unicode]
created: 2026-04-16
updated: 2026-04-16
url: https://theleo.zone/posts/pager/
sources: []
---

# I Made a Terminal Pager — Leo Robinovitch

Blog post by [[leo-robinovitch]] describing how he built a reusable `viewport` Go component and then used it to make his own [[terminal-pager]] called `lore`.

## Context: why pagers exist

Terminals are a grid of monospace cells. Short output prints directly; long output spanning multiple pages is usually piped through a [[terminal-pager]] (controlled by the `$PAGER` env var). Programs like `git`, `man`, etc. check if stdout is a TTY, then spawn `$PAGER` as a child process. Common pagers: `less` (default fallback), `bat`, `most`, `delta`.

## TUIs and the viewport component

[[tui|TUIs]] differ from pagers: they take over the full alt screen and contain multiple components. Leo's `viewport` is the component that fills the TUI role of a mini pager. It's written in Go and integrates with the [Bubble Tea](https://github.com/charmbracelet/bubbletea) TUI framework.

### Three-module architecture

| Module | Role |
|---|---|
| `item` | Wraps a string; handles Unicode widths; supports `Take(startWidth, takeWidth)` for efficient slicing |
| `viewport` | Displays items; handles scroll, wrap/unwrap, horizontal pan, ANSI codes, selection |
| `filterableviewport` | Adds search (exact, regex, case-insensitive) and match navigation to viewport |

### item: Unicode terminal-width handling

Not all characters occupy 1 terminal cell:
- Most ASCII: 1 cell
- Wide characters (CJK, some emoji like ✨): 2 cells
- Combining characters (U+0301 COMBINING ACUTE ACCENT): 0 cells

Leo distinguishes: **code points** (Unicode numbers) → **graphemes** (human-perceived characters) → **terminal cell width**. The `Item` builds a sparse internal map of code points to byte offsets and terminal cell widths on construction, allowing O(1) slicing by cell position.

Three concrete implementations:
- `SingleItem` — eager map at construction; for immutable strings (e.g. k8s logs)
- `MultiItem` — spans multiple SingleItems; supports dynamic prefixing (line numbers, timestamps) without rebuilding
- `MultiLineItem` — for items spanning multiple line breaks (e.g. prettified JSON)

### Search and filtering

Separate keyboard shortcuts for exact match (`/`), regex (`r`), case-insensitive (`i`, implemented as `(?i)` prefix). Applied searches are buffered in memory, navigable with up/down arrows. `x` toggles between match-only and matches-with-context views. `n/N` navigate between matches.

### Selection

The viewport is generic over an `Object` type: `New[T Object](width, height int, opts ...Option[T])`. Callers handle keyboard events like `enter`, call `GetSelectedItem()`, and respond to the typed result.

## lore: the pager itself

[lore](https://github.com/robinovitch61/lore/) is a Bubble Tea TUI that wraps the viewport component into a standalone `$PAGER`. It supports a subset of `less` features but designed to match Leo's actual daily use. He sets `export PAGER=lore` in his shell.

## Leo's other TUIs using viewport

- **kl** — Kubernetes log viewer; two viewports: entity tree (left) + logs (right); supports search, JSON prettification, single-log zoom
- **wander** — Nomad job manager

## See also

- [[leo-robinovitch]]
- [[tui]]
- [[terminal-pager]]
- [[helix]]
