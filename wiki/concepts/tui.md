---
title: TUI (Terminal User Interface)
type: concept
tags: [terminal, tui, ui, software-engineering]
created: 2026-04-16
updated: 2026-04-16
sources: [leo-robinovitch-terminal-pager.md]
---

# TUI (Terminal User Interface)

Terminal applications that behave like interactive graphical applications, but run entirely within a terminal. TUIs use the **alt screen** to temporarily take over the full terminal display and present components: title bars, sidebars, text viewports, lists, input fields.

## Distinguishing characteristics

| | Pager / CLI | TUI |
|---|---|---|
| **Screen** | Inline (scrollback) | Alt screen (full takeover) |
| **Components** | One text stream | Multiple composed components |
| **Input** | Minimal | Rich keyboard-driven navigation |
| **Smallest unit** | Character / line | Terminal grid cell |

The grid-cell constraint forces TUIs to be minimal and hierarchical. Each screen shows exactly what's needed, with keyboard shortcuts to drill in or pivot — rather than one sprawling scrollable page.

## Common components

- **Viewport** — scrollable, searchable text region (the most fundamental TUI component)
- **List/picker** — selectable item collections
- **Input field** — text entry
- **Status bar / help line** — contextual key hints

## Frameworks

- **[Bubble Tea](https://github.com/charmbracelet/bubbletea)** (Go) — Elm-inspired model-update-view architecture; used by [[leo-robinovitch]] for lore, kl, wander
- **Ratatui** (Rust) — used widely in the Rust ecosystem; used by [[helix]] conceptually (Helix has its own rendering layer)

## Examples in this wiki

- [[helix]] — modal text editor, written in Rust
- [[leo-robinovitch-terminal-pager|lore, kl, wander]] — Leo Robinovitch's Go TUIs

## See also

- [[terminal-pager]]
- [[helix]]
- [[leo-robinovitch]]
