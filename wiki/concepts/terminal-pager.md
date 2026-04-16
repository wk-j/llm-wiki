---
title: Terminal Pager
type: concept
tags: [terminal, tui, text-navigation, tools]
created: 2026-04-16
updated: 2026-04-16
sources: [leo-robinovitch-terminal-pager.md]
---

# Terminal Pager

A program for interactively navigating multi-page text in a terminal. Used when output is too long to read at once: git diffs, man pages, logs, database results, AI tool output.

## How programs invoke pagers

Programs check the `$PAGER` environment variable. If set and stdout is a TTY (interactive session), they spawn the pager as a child process and pipe their output into its stdin. When stdout is not a TTY (e.g. `git diff | grep ...`), the pager is skipped.

Specialised overrides exist: `$GIT_PAGER` for git, `$BAT_PAGER` for bat's inner pager, etc.

## Common pagers

| Pager | Notes |
|---|---|
| `less` | Default fallback on most systems; highly configurable; text lost on exit by default (`-X` to persist) |
| `bat` | Syntax highlighting + line numbers; calls another pager internally |
| `most` | Multi-window, splits |
| `delta` | Specialised for git diffs; side-by-side, syntax highlighting |
| `lore` | [[leo-robinovitch|Leo Robinovitch]]'s Go pager, built on his `viewport` component |
| `cat` | Set `PAGER=cat` to disable paging entirely |

## Useful `less` options

- `-X` / `--no-init` — keep output in terminal after quit
- `-i` / `--ignore-case` — case-insensitive search
- `-R` — pass ANSI escape codes through (color output)

## Pagers vs TUIs

Pagers typically display a single stream of text in the alt screen (or inline). [[tui|TUIs]] compose multiple pager-like components alongside other UI elements. Leo Robinovitch's `viewport` component is a reusable mini-pager intended for embedding in TUIs.

## See also

- [[tui]]
- [[leo-robinovitch-terminal-pager]]
- [[leo-robinovitch]]
