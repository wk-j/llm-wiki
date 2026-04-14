---
title: Cassette Futurism
type: concept
tags: [ui, design, retro-futurism, sci-fi]
created: 2026-04-13
updated: 2026-04-13
sources: [Retro futuristic UI design 2.md]
---

# Cassette Futurism

A [[retro-futurism]] subgenre rooted in the 1970s–80s — the era of clunky terminals, VHS noise, and tape-era computing. The future as imagined by someone who just saw a BBC Micro and thought *this is where it's all going*.

## Visual characteristics

- Near-black backgrounds (`#050508`)
- Matrix green (`#00ff41`) as primary, magenta accent, yellow alerts
- CRT scanlines and phosphor glow effects
- Monospace fonts (VT323, Share Tech Mono)
- ASCII progress bars, cursor blink, terminal-style text rendering

## Key references

- Alien's MUTHUR computer interface
- WarGames (1983)
- BBC Micro and early home computing
- VHS-era recording equipment

## Implementation

The interface IS an old computer terminal. Uses the Terminal / Phosphor Screen pattern: green phosphor on dark glass, scanlines, cursor blink. Key components include TerminalWindow, PhosphorText, CommandLine, and ASCII ProgressBar.

## See also

- [[retro-futurism]]
- [[atompunk]]
- [[raygun-gothic]]
