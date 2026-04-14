---
title: Holographic UI
type: source
tags: [ui, design, sci-fi, holographic, css, frontend]
created: 2026-04-14
updated: 2026-04-14
sources: [Holographic UI.md]
---

# Holographic UI

A comprehensive design skill for building holographic interfaces — UIs that simulate light projected into space. Covers five variant palettes, CSS rendering techniques, animation library, component recipes, and layout patterns.

## Core principle

The fundamental illusion: **the interface is made of light, not matter.** Every design decision reinforces this — transparent backgrounds, glowing edges, breathing animations, floating depth layers.

## Five variants

| Variant | Color story | Reference | Signature |
|---|---|---|---|
| **Pure Holo** | Cyan/blue monochromatic | Minority Report, Iron Man | Thin glowing borders, nested panels, data as light streams |
| **Bio-Holo** | Bioluminescent blue-green | Avatar, Na'vi network | Curved organic borders, particle trails, web-like connections |
| **Military Holo** | Amber/orange on near-black | The Expanse, war rooms | Tight text grids, tactical overlays, angular bracket framing |
| **Ghost Holo** | Purple/magenta on dark blue-black | Ghost in the Shell, Cyberpunk | Scan-line artifacts, glitch distortion, dual-color data streams |
| **Clean Holo** | White/silver on dark | Apple Vision, near-future | Frosted glass panels, subtle borders, typography-forward |

## Rendering techniques

- **Glass Panel** — core primitive: `rgba()` background, 1px glowing border, triple box-shadow (outer diffuse + inner fill + edge hot line), backdrop-filter blur, scan-line pseudo-element overlay
- **Depth Layering** — three Z-planes (front/mid/back) with decreasing opacity and shadow intensity to simulate projection distance
- **Corner Accents** — partial border geometry on corners only instead of full borders, using pseudo-elements
- **Glow Text** — text-shadow with matching accent color, wide letter-spacing (≥0.08em), light font weights

## Animation library

| Animation | Purpose | Usage |
|---|---|---|
| `holo-materialize` | Panel mount/load | Mandatory — every panel on appear |
| `holo-breathe` | Standby glow pulse | Mandatory — all idle panels, 3–5s infinite |
| `holo-scan` | Active processing indicator | Mandatory — at least one per screen |
| `holo-ring-spin` | Circular data meter rotation | Mandatory — any ring/loader |
| `holo-glitch` | Glitch distortion | Optional — Ghost variant |
| `holo-float` | Ambient particle drift | Optional — enhances "light in air" illusion |
| `holo-vanish` | Dematerialization exit | Optional — panel dismissal |

## Component recipes

- **HoloRing** — SVG circular status arc with spinning dashed outer ring and data arc fill
- **HoloGrid** — radar/map display with concentric ring gradients, crosshair grid, and conic-gradient sweep
- **HoloStream** — scrolling data ticker with horizontal infinite animation
- **HoloBar** — thin progress indicator with gradient fill and bright endpoint marker
- **HoloParticles** — JS-generated ambient floating dots with randomized size, position, and animation timing

## Layout patterns

- **Command Deck** — 3-panel with central display flanked by status/data panels, bottom ticker bar
- **Floating Cards** — scattered grid with slight rotation and varied depth for 3D projection feel
- **Cockpit** — horizontal information bands (nav bar / large visual + instruments / alerts)

## 10 non-negotiable rules

1. Dark background only (`#000000`–`#0d0d20`)
2. All panels semi-transparent (`rgba()` only)
3. Every border must glow (box-shadow required)
4. Minimum one breathing panel + one scan animation
5. Text must have text-shadow glow
6. No pure white text — use palette-tinted near-white
7. No sharp corners > 2px border-radius
8. Letter-spacing minimum 0.08em on labels
9. Use Google Fonts (Exo 2, Rajdhani, Orbitron, Share Tech Mono)
10. No background images — pure light constructs only

## See also

- [[holographic-ui]]
- [[diegetic-ui]]
- [[glassmorphism]]
- [[retro-futurism]]
- [[ui-style-categories]]
