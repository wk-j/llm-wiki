---
title: Holographic UI
type: concept
tags: [ui, design, sci-fi, holographic, glassmorphism, diegetic]
created: 2026-04-14
updated: 2026-04-14
sources: [Holographic UI.md]
---

# Holographic UI

A UI design language that simulates light-emitted interfaces projected into space — semi-transparent, glowing, and weightless. The core illusion: **the interface is made of light, not matter.**

Holographic UI sits at the intersection of [[glassmorphism]] (shared transparency and backdrop-blur techniques) and [[diegetic-ui]] (the "Holographic Projection" sub-style), but is a distinct system with its own constraints and vocabulary.

## Holographic vs. physical screen UI

| Property | Physical Screen | Holographic |
|---|---|---|
| Background | Solid / opaque | Transparent / see-through |
| Borders | Solid lines | Glowing edges, soft halos |
| Depth | Flat | Layered Z-planes, parallax |
| Color | Full RGB gamut | Monochromatic or duochromatic glow |
| Interaction | Click/tap | Gesture, proximity, hover |
| State change | Immediate | Fade / dematerialize |

## Five variants

Each variant has a distinct color story and cultural reference:

- **Pure Holo** — Cyan/blue monochromatic. Minority Report, Iron Man's lab. Maximum translucency, thin glowing borders, nested panel layers.
- **Bio-Holo** — Bioluminescent blue-green. Avatar / Na'vi network. Organic flowing shapes, curved borders, particle trails, web-like connections.
- **Military Holo** — Amber/orange on near-black. The Expanse war rooms. Dense data, tight text grids, tactical overlays, angular bracket framing.
- **Ghost Holo** — Purple/magenta on dark blue-black. Ghost in the Shell, Cyberpunk. Scan-line artifacts, glitch distortion, corrupted text effects.
- **Clean Holo** — White/silver on dark. Apple Vision, near-future. Frosted glass panels, very subtle borders, typography-forward, breathing space.

## Core rendering primitives

### The Glass Panel

The fundamental building block. Every holographic interface is composed of glass panels:

- `rgba()` background (never solid)
- 1px border with matching glow color
- Triple box-shadow: outer diffuse glow + inner fill light + edge hot line
- `backdrop-filter: blur()` for depth
- Scan-line overlay via `::before` pseudo-element with repeating-linear-gradient

### Depth layering

Three Z-planes simulate projection distance — front (full opacity, strong shadow), mid (0.9 opacity), back (0.7 opacity, minimal shadow).

### Corner accents

Partial border geometry on corners only (using pseudo-elements) instead of full borders — reinforces the projected-light feel.

### Glow text

Text-shadow matching the panel accent color. Wide letter-spacing (≥0.08em). Light font weights. Distinct styles for primary text, dim labels, and data values.

## Animation vocabulary

Four mandatory animations create the "living light" illusion:

1. **Materialize** — panel fade-in with slight scale-up and blur clear (on mount)
2. **Breathe** — subtle glow pulse on all idle panels (3–5s cycle, staggered delays)
3. **Scan** — a moving element representing active processing (at least one per screen)
4. **Ring spin** — continuous rotation on any circular meter or loader

Optional: glitch distortion (Ghost variant), particle float (ambient atmosphere), vanish/dematerialize (exit animation).

## Layout patterns

- **Command Deck** — center-focused 3-panel layout with flanking status/data panels and bottom ticker
- **Floating Cards** — scattered grid with slight rotation and varied depth
- **Cockpit** — horizontal information bands (navigation / main visual + instruments / alerts)

## Design constraints

- Background must be dark (#000000–#0d0d20) — holograms don't project in daylight
- All panels semi-transparent — `rgba()` only, never solid fills
- Every border must glow via box-shadow
- No pure white text — use palette-tinted near-white
- No sharp corners > 2px border-radius
- No photographic elements — holographic UIs are pure light constructs
- Typography: Google Fonts — Exo 2, Rajdhani, Orbitron, or Share Tech Mono

## Relationship to other styles

Holographic UI overlaps with but is distinct from:

- **[[glassmorphism]]** — shares backdrop-blur and transparency, but glassmorphism uses bright/colorful backgrounds while holographic requires dark void backgrounds
- **[[diegetic-ui]]** — holographic projection is one of five diegetic sub-styles; holographic UI is a broader design system that works outside game/narrative contexts too
- **[[retro-futurism]]** — the Military Holo and Ghost Holo variants share visual DNA with [[cassette-futurism]] and [[soviet-cosmism]] respectively, but holographic UI aims for "future" rather than "past's future"
- **[[cyberpunk-neon]]** — Ghost Holo variant overlaps with cyberpunk aesthetics (purple/magenta, glitch effects)

## See also

- [[diegetic-ui]]
- [[glassmorphism]]
- [[retro-futurism]]
- [[ui-style-categories]]
- [[cassette-futurism]]
- [[soviet-cosmism]]
