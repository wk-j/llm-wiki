---
title: Retro Futuristic UI Design
type: source
tags: [ui, design, retro-futurism, css, design-system]
created: 2026-04-13
updated: 2026-04-13
sources: [Retro futuristic UI design.md, Retro futuristic UI design 2.md]
---

# Retro Futuristic UI Design

A Claude conversation that explains the retro-futurism UI philosophy and provides a complete design system for building retro-futuristic interfaces. The two clips come from the same conversation — the first introduces the concept, the second provides the full skill file.

## Core philosophy

Retro-futurism UI is built on one central tension: **the past's imagination of the future**. Not how the future actually looks, but how someone in 1955 or 1970 *dreamed* it would look. It blends the tactile craftsmanship of the analog era (bakelite knobs, vacuum tubes, physical dials) with the ambition of the space age (mission control panels, radar screens, telemetry readouts).

## Five subgenres

| Subgenre | Era | Feel | Key References |
|---|---|---|---|
| [[raygun-gothic]] | 1930s–50s | Streamlined chrome, atomic optimism | Flash Gordon, Buck Rogers, The Rocketeer |
| [[atompunk]] | 1950s–60s | Atomic age, suburban utopia, fallout shelters | Fallout series, Disney's Tomorrowland, early NASA |
| Space Age / NASA Core | 1960s–70s | Mission control precision, slide-rule elegance | Apollo program, 2001: A Space Odyssey |
| [[cassette-futurism]] | 1970s–80s | Clunky terminals, VHS noise, tape-era computing | Alien's MUTHUR, WarGames, BBC Micro |
| Soviet Cosmism | 1960s–80s | Bold constructivist geometry, stark functionalism | Soyuz dashboards, Soviet propaganda posters |

## Era-accurate color palettes

- **Raygun Gothic**: Dark mahogany bg, warm amber `#f5c842`, red-orange accent
- **Atompunk / Fallout**: Dark green bg, phosphor green `#33ff33`, yellow accent
- **NASA Mission Control**: Midnight bg, sky blue `#4fc3f7`, white accent, orange alert
- **Cassette / VHS**: Near-black bg, matrix green `#00ff41`, magenta accent
- **Soviet Constructivist**: Dark rust bg, soviet red `#e63946`, gold accent
- **Art Deco Tech**: Near black bg, gold `#d4af37`, pale gold accent

## Typography rules

| Use Case | Font | Feel |
|---|---|---|
| Terminal/Readouts | VT323, Share Tech Mono | CRT phosphor text |
| Panel Headers | Orbitron (700–900) | Space-age authority |
| Data Labels | Rajdhani (600) | Military technical |
| Typewriter/Atompunk | Special Elite | Mechanical age |
| Pixel/8-bit | Press Start 2P | Early digital |

Hard rule: never use Inter, Roboto, or Arial — they break the illusion.

## Shape grammar

Concentric circles (power/radar), chevrons (direction/loading), segmented arcs (gauges), diamonds (alerts), ruled lines (structure), hexagons (data containers), corner brackets (targeting/framing).

## Three implementation patterns

1. **Terminal / Phosphor Screen** — the interface IS an old computer terminal. Green phosphor on dark glass, scanlines, cursor blink. Components: TerminalWindow, PhosphorText, CommandLine, ASCII ProgressBar, StatusReadout.

2. **Mission Control / NASA Panel** — precision engineering aesthetic. Dark blue-black, cold sky blue, analog gauges in SVG. Components: GaugeArc, SevenSegDisplay, MissionTimer, TelemetryRow, StatusMatrix, FrequencyBand.

3. **Art Deco Tech / Raygun Gothic** — ornate geometric borders, warm amber/gold, fan shapes, symmetry. Components: DecoGauge, ArtDecoCard, FanMeter, OrnamentDivider, ChromeButton, VoltmeterDisplay.

## Eight non-negotiable aesthetic rules

1. No flat modern colors — warm ambers, phosphor greens, NASA blues, art deco golds
2. No rounded-corner cards — sharp corners, notched corners, or mechanically-framed panels
3. Always include a texture layer — scanlines, noise, grain, or vignette
4. Always include phosphor/neon glow via text-shadow and box-shadow
5. No modern sans-serif fonts
6. Always include at least one analog-style element (gauge, dial, segmented display)
7. Data must look measured — fixed-width columns, aligned decimals, unit labels
8. Label everything in small-caps or all-caps

## See also

- [[retro-futurism]]
- [[ui-style-categories]]
- [[diegetic-ui]]
