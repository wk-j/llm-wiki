---
title: "Imetomi/retro-futuristic-ui-design"
type: source
tags: [ui, design, retro-futurism, cassette-futurism, react, css, open-source]
created: 2026-04-14
updated: 2026-04-14
sources: ["Imetomiretro-futuristic-ui-design Creating web-based retro effects is quite hard, use this for inspiration.md"]
url: https://github.com/Imetomi/retro-futuristic-ui-design
---

# Imetomi/retro-futuristic-ui-design

Open-source React + TypeScript component library implementing [[cassette-futurism]] UI effects — CRT terminals and LCD surveillance devices inspired by Alien (1979), Blade Runner, and Signalis. Built with Vite, MIT licensed.

## Key components

### CRT Terminal

An amber phosphor CRT display achieved through **7 layered CSS elements**:

1. **Base screen** — dark background with elliptical border-radius for curvature
2. **Scanlines** — repeating 3px CSS gradient stripes (`::before`)
3. **Vignette** — radial gradient darkening edges (`::after`)
4. **Glass overlay** — additional edge darkening for depth
5. **Specular highlight** — light reflection on curved glass (upper-left)
6. **Edge shadow** — inset shadows reinforcing the curve illusion
7. **Reflection** — subtle top highlight

Additional features: random glitch effect (hue rotation + position jitter), boot sequence with typewriter text reveal, keyboard-navigable menu (arrows + Enter), blinking cursor, beige monitor bezel with vent slots and green power LED.

Content sits inside a 3D-transformed container with CSS `perspective` for subtle depth.

### LCD Surveillance Device

A greenish LCD with pixel grid effect, camera lens with glass reflections and focal markings, physical control buttons (power/menu/select) with 3D press effect, red LED indicator, speaker grille, and grayish plastic housing. "THE COMPANY" branding echoes the Alien universe.

## Color palettes

### Amber phosphor (CRT default)
| Role | Value |
|---|---|
| Primary | `#ff6a00` |
| Dimmed | `#994400` |
| Border | `#331a00` |
| Strong glow | `rgba(255, 106, 0, 0.8)` |
| Subtle glow | `rgba(255, 106, 0, 0.3)` |

### Green phosphor (IBM-style alternative)
| Role | Value |
|---|---|
| Primary | `#00ff41` |
| Dimmed | `#00802b` |
| Border | `#003311` |

### LCD screen
| Role | Value |
|---|---|
| Background | `#4a5a3a` → `#354525` gradient |
| Text | `#1a2a10` |
| Housing | `#e8e8e8` → `#a0a0a0` gradient |

## Typography

VT323 (terminal text), Share Tech Mono (monospace), Orbitron (space-age headers) — all loaded via Google Fonts CSS import.

## Technical insight

The core lesson: **convincing CRT/LCD effects are achievable with pure CSS layering** — no WebGL, no canvas, no shaders. The secret is stacking 5–7 semi-transparent pseudo-elements and overlays (scanlines, vignettes, reflections, glows) on top of the content layer. Each layer is simple; the composite is convincing.

## Design credits

Inspired by concept artist [[nathan-david-jones]] and the broader [[cassette-futurism]] aesthetic movement. Moodboard references Alien, Blade Runner, and real-world vintage computing hardware.

## See also

- [[cassette-futurism]]
- [[retro-futurism]]
- [[retro-futuristic-ui-design]] — the earlier design system source (palettes, typography, patterns)
- [[nathan-david-jones]]
