---
title: Retro-Futurism
type: concept
tags: [ui, design, sci-fi, retro, design-system]
created: 2026-04-12
updated: 2026-04-13
sources: [UI style categories.md, Retro futuristic UI design.md, Retro futuristic UI design 2.md]
---

# Retro-Futurism

A UI design philosophy built on one central tension: **the past's imagination of the future**. Not how the future actually looks, but how someone in 1955 or 1970 *dreamed* it would look. It blends the tactile craftsmanship of the analog era (bakelite knobs, vacuum tubes, physical dials) with the ambition of the space age (mission control panels, radar screens, telemetry readouts).

## Five subgenres

| Subgenre | Era | Feel | Key References |
|---|---|---|---|
| **[[raygun-gothic]]** | 1930s–50s | Streamlined chrome, atomic optimism | Flash Gordon, Buck Rogers, The Rocketeer |
| **[[atompunk]]** | 1950s–60s | Atomic age, suburban utopia | Fallout series, Disney's Tomorrowland |
| **Space Age / NASA Core** | 1960s–70s | Mission control precision, slide-rule elegance | Apollo program, 2001: A Space Odyssey |
| **[[cassette-futurism]]** | 1970s–80s | Clunky terminals, VHS noise | Alien's MUTHUR, WarGames |
| **[[soviet-cosmism]]** | 1960s–80s | Constructivist geometry, stark functionalism | Soyuz dashboards |

## Core design principles

### The analog-digital paradox

Retro-futurism UIs look *mechanical* but are actually digital. Dials and gauges display data via SVG. Buttons look physical/backlit but respond to clicks. The "screen" has visible pixels or CRT curvature.

### Era-accurate color palettes

Each subgenre has a distinct palette — warm ambers for Raygun Gothic, phosphor greens for Atompunk, sky blues for NASA, and soviet reds for Cosmism. Mixing palettes across subgenres breaks the illusion.

### Typography

Fonts must evoke machine-age craftsmanship: Orbitron for space-age headers, VT323 for terminal readouts, Rajdhani for data labels, Special Elite for typewriter text. Modern sans-serifs (Inter, Roboto, Arial) are forbidden.

### Shape grammar

Concentric circles (power/radar), chevrons (direction/loading), segmented arcs (analog gauges), diamonds (alerts), ruled lines (structure), hexagons (data containers), corner brackets (targeting/framing).

### Texture and noise

Retro-futurism relies on simulated physical media: CRT scanlines, phosphor glow, static/noise, vignettes, and flicker animations.

## Non-negotiable aesthetic rules

1. No flat modern colors — use warm ambers, phosphor greens, NASA blues, art deco golds
2. No rounded-corner cards — sharp or notched corners only (max `border-radius: 3px`)
3. Always include a texture layer (scanlines, noise, grain, or vignette)
4. Always include phosphor/neon glow
5. No modern sans-serif fonts
6. At least one analog-style element (gauge, dial, segmented display)
7. Data must look measured — fixed-width columns, aligned decimals, unit labels
8. Label everything in small-caps or all-caps

## Implementation patterns

Three main approaches, each with distinct component sets:

- **Terminal / Phosphor Screen** — green phosphor on dark glass, CRT scanlines, cursor blink (Fallout / Cassette Futurism)
- **Mission Control / NASA Panel** — dark blue-black, sky blue, SVG analog gauges, seven-segment displays
- **Art Deco Tech / Raygun Gothic** — ornate geometric borders, warm amber/gold, fan shapes, symmetry

## Related styles on the spectrum

| Style | Era reference | Mood |
|---|---|---|
| **Retro-Futurism** | 1930s–80s sci-fi | Nostalgic wonder |
| **[[synthwave]]** | 80s music/film | Neon-soaked atmosphere |
| **[[vaporwave]]** | 90s internet | Ironic, dreamy, glitched |
| **[[cyberpunk-neon]]** | Near-future dystopia | Gritty, high-tech low-life |

These overlap significantly but differ in mood and cultural reference. Retro-futurism is the broadest — spanning from 1930s Raygun Gothic through 1980s Cassette Futurism — while synthwave and vaporwave are narrower aesthetic movements.

## See also

- [[retro-futuristic-ui-design]] — full design system source
- [[diegetic-ui]]
- [[brutalism]]
- [[ui-style-categories]]
