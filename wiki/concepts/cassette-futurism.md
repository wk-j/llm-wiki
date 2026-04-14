---
title: Cassette Futurism
type: concept
tags: [ui, design, retro-futurism, sci-fi]
created: 2026-04-13
updated: 2026-04-14
sources: [Retro futuristic UI design 2.md, "Imetomiretro-futuristic-ui-design Creating web-based retro effects is quite hard, use this for inspiration.md"]
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

## CSS CRT technique

[[imetomi-retro-futuristic-ui|Imetomi's React components]] prove that convincing CRT effects need only **pure CSS layering** — no WebGL or canvas. The recipe: stack 5–7 semi-transparent layers (scanlines via repeating gradients, vignette via radial gradient, specular highlight, glass overlay, edge shadows) on top of content. Each layer is trivial; the composite is convincing. Key details:

- Elliptical `border-radius` for screen curvature
- `text-shadow` stacking for phosphor glow (amber `#ff6a00` or green `#00ff41`)
- CSS `perspective` on a wrapper for subtle 3D depth
- Hue-rotation + position jitter for glitch effects

## See also

- [[retro-futurism]]
- [[atompunk]]
- [[raygun-gothic]]
- [[imetomi-retro-futuristic-ui]]
- [[nathan-david-jones]]
