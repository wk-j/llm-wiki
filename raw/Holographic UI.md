---
title: "Claude Conversation"
source: "https://claude.ai/customize/skills"
author:
published:
created: 2026-04-14
description: "Claude conversation with 2 messages"
tags:
  - "clippings"
---
**Claude**

Design and build Holographic UI — luminous, semi-transparent floating interfaces inspired by Minority Report, Avatar, Iron Man's lab projections, The Expanse data panels, and sci-fi holographic displays. Use this skill whenever the user asks for a "holographic" interface, "holo panel", "floating UI", "projection display", "translucent sci-fi interface", "volumetric UI", "ghost panel", "glass morphism sci-fi", or anything that should look like light projected into thin air. Also trigger for "Minority Report style", "hologram display", "holo dashboard", "projection UI", "light panel", "holographic data visualization", "future glass interface", "sci-fi transparent panel", "Avatar Na'vi UI", "The Expanse style", "Ghost in the Shell interface", or "AR hologram". Use even if the user only says "make it look like a hologram" or "floating glowing panels". This skill is specifically focused on holographic aesthetics — for broader diegetic/in-world UI use the diegetic-ui skill.

---

**Claude**

## Holographic UI Skill

Build production-grade **Holographic UI** — interfaces that look like pure light projected into space, semi-transparent, glowing, and weightless.

---

## What is Holographic UI?

Holographic UI simulates light-emitted interfaces that exist as projected energy rather than physical screens. The fundamental illusion: **the interface is made of light, not matter.**

| Characteristic | Physical Screen UI | Holographic UI |
| --- | --- | --- |
| Background | Solid / opaque | Transparent / see-through |
| Borders | Solid lines | Glowing edges, soft halos |
| Depth | Flat | Layered Z-planes, parallax |
| Color | RGB gamut | Monochromatic or duochromatic glow |
| Interaction | Click/tap | Gesture, proximity, hover |
| State change | Immediate | Fade / dematerialize |

---

## The 5 Holographic Variants

### Variant 1: Pure Holo (Minority Report / Iron Man Lab)

Cyan/blue monochromatic. Floating panels in dark void. Maximum translucency.

```
:root {
  --holo-void: #000913;
  --holo-surface: rgba(0, 160, 255, 0.04);
  --holo-border: rgba(0, 200, 255, 0.25);
  --holo-edge-glow: rgba(0, 220, 255, 0.6);
  --holo-text: rgba(160, 235, 255, 0.92);
  --holo-text-dim: rgba(80, 180, 220, 0.5);
  --holo-accent: rgba(0, 255, 220, 0.8);
  --holo-warn: rgba(255, 180, 0, 0.85);
  --holo-critical: rgba(255, 60, 60, 0.9);
  --holo-grid: rgba(0, 180, 255, 0.035);
  --holo-font: 'Exo 2', 'Rajdhani', 'Share Tech Mono', sans-serif;
}
```

**Signature look:** Thin glowing borders, nested panel layers, data flows as light streams.

### Variant 2: Bio-Holo (Avatar / Na'vi Network)

Bioluminescent blue-green. Organic flowing shapes. Nature + technology.

```
:root {
  --bio-void: #010a06;
  --bio-surface: rgba(0, 255, 150, 0.03);
  --bio-border: rgba(0, 220, 130, 0.22);
  --bio-edge-glow: rgba(60, 255, 180, 0.55);
  --bio-text: rgba(140, 255, 200, 0.9);
  --bio-text-dim: rgba(60, 200, 130, 0.5);
  --bio-accent: rgba(100, 255, 220, 0.85);
  --bio-pulse: rgba(0, 255, 130, 0.4);
  --bio-font: 'Exo 2', 'Orbitron', monospace;
}
```

**Signature look:** Curved organic borders, particle trail effects, web-like connection lines.

### Variant 3: Military Holo (The Expanse / War Room)

Amber/orange on near-black. Dense data. High information-to-space ratio.

```
:root {
  --mil-void: #080500;
  --mil-surface: rgba(255, 140, 0, 0.03);
  --mil-border: rgba(255, 160, 20, 0.22);
  --mil-edge-glow: rgba(255, 180, 40, 0.55);
  --mil-text: rgba(255, 210, 120, 0.92);
  --mil-text-dim: rgba(200, 150, 60, 0.5);
  --mil-accent: rgba(255, 100, 0, 0.9);
  --mil-ok: rgba(100, 255, 80, 0.8);
  --mil-font: 'Share Tech Mono', 'Courier New', monospace;
}
```

**Signature look:** Tight text grids, tactical overlays, angular bracket framing, dense readouts.

### Variant 4: Ghost Holo (Ghost in the Shell / Cyberpunk)

Purple/magenta on dark blue-black. Data archaeology. Glitch aesthetic.

```
:root {
  --ghost-void: #05010f;
  --ghost-surface: rgba(180, 0, 255, 0.03);
  --ghost-border: rgba(200, 60, 255, 0.2);
  --ghost-edge-glow: rgba(220, 100, 255, 0.5);
  --ghost-text: rgba(220, 180, 255, 0.9);
  --ghost-text-dim: rgba(140, 80, 200, 0.5);
  --ghost-accent: rgba(255, 80, 220, 0.85);
  --ghost-data: rgba(0, 200, 255, 0.7);
  --ghost-font: 'Share Tech Mono', 'Courier New', monospace;
}
```

**Signature look:** Scan-line artifacts, glitch distortion, dual-color data streams, corrupted text effects.

### Variant 5: Clean Holo (Near-Future UI / Apple Vision style)

White/silver on dark. Premium, minimal. Information without noise.

```
:root {
  --clean-void: #080810;
  --clean-surface: rgba(255, 255, 255, 0.04);
  --clean-border: rgba(200, 210, 255, 0.18);
  --clean-edge-glow: rgba(220, 230, 255, 0.45);
  --clean-text: rgba(235, 240, 255, 0.92);
  --clean-text-dim: rgba(160, 170, 200, 0.5);
  --clean-accent: rgba(100, 160, 255, 0.9);
  --clean-font: 'Inter', 'Exo 2', sans-serif;
}
```

**Signature look:** Frosted glass panels, very subtle borders, typography-forward, breathing space.

---

## Holographic Rendering Techniques

### The Glass Panel (Core Primitive)

Every holographic UI is built from glass panels. Master this first.

```
.holo-panel {
  background: var(--holo-surface);
  border: 1px solid var(--holo-border);
  box-shadow:
    0 0 20px rgba(0, 200, 255, 0.08),    /* outer diffuse glow */
    inset 0 0 30px rgba(0, 200, 255, 0.04), /* inner fill light */
    0 0 1px rgba(0, 220, 255, 0.6);      /* edge hot line */
  backdrop-filter: blur(8px);
  position: relative;
  overflow: hidden;
}

/* Scan line overlay — always present */
.holo-panel::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0, 200, 255, 0.015) 2px,
    rgba(0, 200, 255, 0.015) 4px
  );
  pointer-events: none;
}
```

### Depth Layering (Z-planes)

Holographic UIs have depth. Use layered shadows to simulate Z separation:

```
/* Foreground panel — closest to viewer */
.layer-front {
  box-shadow: 0 20px 60px rgba(0,0,0,0.8), 0 0 30px rgba(0,200,255,0.15);
  z-index: 30;
}
/* Mid panel */
.layer-mid {
  box-shadow: 0 10px 40px rgba(0,0,0,0.6), 0 0 20px rgba(0,200,255,0.08);
  z-index: 20;
  opacity: 0.9;
}
/* Background panel — furthest away, most transparent */
.layer-back {
  box-shadow: 0 5px 20px rgba(0,0,0,0.4);
  z-index: 10;
  opacity: 0.7;
}
```

### Corner Accents

Holographic panels use corner geometry instead of full borders:

```
.holo-panel-cornered {
  border: none;
  position: relative;
}
.holo-panel-cornered::before,
.holo-panel-cornered::after {
  content: '';
  position: absolute;
  width: 12px; height: 12px;
  border-color: var(--holo-edge-glow);
  border-style: solid;
  opacity: 0.8;
}
.holo-panel-cornered::before {
  top: 0; left: 0;
  border-width: 1px 0 0 1px;
}
.holo-panel-cornered::after {
  bottom: 0; right: 0;
  border-width: 0 1px 1px 0;
}
/* Use JS or additional pseudo-elements for all 4 corners */
```

### Holographic Glow Text

```
.holo-text-primary {
  color: var(--holo-text);
  text-shadow:
    0 0 8px rgba(0, 200, 255, 0.8),
    0 0 20px rgba(0, 200, 255, 0.4);
  letter-spacing: 0.12em;
  font-weight: 300;
}

.holo-text-label {
  color: var(--holo-text-dim);
  text-transform: uppercase;
  letter-spacing: 0.2em;
  font-size: 0.7em;
  font-weight: 400;
}

.holo-text-data {
  color: var(--holo-accent);
  font-family: var(--holo-font);
  font-weight: 600;
  text-shadow: 0 0 12px currentColor;
}
```

---

## Animation Library

```
/* ─── MANDATORY: Panel materialization ─── */
@keyframes holo-materialize {
  from {
    opacity: 0;
    transform: scale(0.96);
    filter: blur(4px);
  }
  to {
    opacity: 1;
    transform: scale(1);
    filter: blur(0);
  }
}

/* ─── MANDATORY: Breathing glow (standby state) ─── */
@keyframes holo-breathe {
  0%, 100% { opacity: 0.85; box-shadow: 0 0 20px rgba(0,200,255,0.08); }
  50%       { opacity: 1.0;  box-shadow: 0 0 35px rgba(0,200,255,0.18); }
}

/* ─── MANDATORY: Data stream / scan ─── */
@keyframes holo-scan {
  0%   { transform: translateY(-100%); opacity: 0; }
  10%  { opacity: 0.6; }
  90%  { opacity: 0.6; }
  100% { transform: translateY(200%); opacity: 0; }
}

/* ─── MANDATORY: Rotation ring ─── */
@keyframes holo-ring-spin {
  to { transform: rotate(360deg); }
}

/* ─── OPTIONAL: Glitch distortion ─── */
@keyframes holo-glitch {
  0%,95%,100% { transform: translate(0); clip-path: none; }
  96%  { transform: translate(-2px, 1px); clip-path: inset(20% 0 30% 0); }
  97%  { transform: translate(2px, -1px); clip-path: inset(60% 0 5% 0); }
  98%  { transform: translate(-1px, 2px); clip-path: inset(40% 0 50% 0); }
}

/* ─── OPTIONAL: Particle float ─── */
@keyframes holo-float {
  0%,100% { transform: translateY(0) translateX(0); opacity: 0.6; }
  33%     { transform: translateY(-8px) translateX(4px); opacity: 1; }
  66%     { transform: translateY(-4px) translateX(-4px); opacity: 0.8; }
}

/* ─── OPTIONAL: Dematerialization ─── */
@keyframes holo-vanish {
  to { opacity: 0; transform: scale(1.04); filter: blur(6px); }
}
```

### Usage rules:

- **`holo-materialize`** — Every panel on mount/load
- **`holo-breathe`** — All idle/standby panels, duration 3–5s infinite
- **`holo-scan`** — At least one element per screen, represents active processing
- **`holo-ring-spin`** — Any circular data meter or loader

---

## Component Recipes

### HoloRing — Circular Status Arc

```html
<!-- SVG-based for crisp rendering -->
<svg viewBox="0 0 100 100" class="holo-ring">
  <!-- Background track -->
  <circle cx="50" cy="50" r="42"
    fill="none" stroke="rgba(0,200,255,0.1)" stroke-width="2"/>
  <!-- Spinning outer ring -->
  <circle cx="50" cy="50" r="46"
    fill="none" stroke="rgba(0,200,255,0.3)" stroke-width="0.5"
    stroke-dasharray="4 8"
    style="animation: holo-ring-spin 8s linear infinite"/>
  <!-- Data arc (fill with stroke-dashoffset) -->
  <circle cx="50" cy="50" r="42"
    fill="none" stroke="rgba(0,220,255,0.8)" stroke-width="2.5"
    stroke-linecap="round" stroke-dasharray="264" stroke-dashoffset="80"
    transform="rotate(-90 50 50)"
    style="filter: drop-shadow(0 0 4px rgba(0,220,255,0.8))"/>
  <!-- Center value -->
  <text x="50" y="55" text-anchor="middle" font-size="18"
    fill="rgba(160,235,255,0.92)" font-family="Exo 2, monospace">74%</text>
</svg>
```

### HoloGrid — Radar / Map Display

```
.holo-grid-container {
  position: relative;
  aspect-ratio: 1;
}
.holo-grid-bg {
  background-image:
    /* Concentric rings */
    radial-gradient(circle, transparent 30%, rgba(0,200,255,0.06) 30.5%, transparent 31%),
    radial-gradient(circle, transparent 60%, rgba(0,200,255,0.04) 60.5%, transparent 61%),
    radial-gradient(circle, transparent 85%, rgba(0,200,255,0.03) 85.5%, transparent 86%),
    /* Cross hairs */
    linear-gradient(rgba(0,200,255,0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,200,255,0.05) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 100% 100%, 25% 25%, 25% 25%;
}
.holo-sweep {
  position: absolute;
  inset: 0;
  background: conic-gradient(
    from 0deg,
    rgba(0,220,255,0.12),
    transparent 70deg
  );
  animation: holo-ring-spin 4s linear infinite;
  border-radius: 50%;
}
```

### HoloStream — Scrolling Data Ticker

```
.holo-stream {
  overflow: hidden;
  height: 1.6em;
  position: relative;
}
.holo-stream-inner {
  display: flex;
  gap: 2em;
  animation: holo-ticker 15s linear infinite;
  white-space: nowrap;
  color: var(--holo-text-dim);
  font-size: 0.72em;
  letter-spacing: 0.08em;
}
@keyframes holo-ticker {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
```

### HoloBar — Progress / Level Indicator

```
.holo-bar-track {
  height: 3px;
  background: rgba(0,200,255,0.1);
  position: relative;
  overflow: visible;
}
.holo-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, rgba(0,180,255,0.6), rgba(0,240,255,1));
  box-shadow: 0 0 8px rgba(0,220,255,0.8), 0 0 20px rgba(0,200,255,0.4);
  position: relative;
}
.holo-bar-fill::after {
  content: '';
  position: absolute;
  right: -1px;
  top: -3px; bottom: -3px;
  width: 3px;
  background: white;
  box-shadow: 0 0 8px rgba(0,220,255,1), 0 0 16px rgba(0,220,255,0.8);
}
```

### HoloParticles — Ambient Floating Particles (JS)

```javascript
function createHoloParticles(container, count = 20) {
  for (let i = 0; i < count; i++) {
    const p = document.createElement('div');
    p.style.cssText = \`
      position: absolute;
      width: ${Math.random() * 2 + 1}px;
      height: ${Math.random() * 2 + 1}px;
      background: rgba(0, 220, 255, ${Math.random() * 0.5 + 0.2});
      border-radius: 50%;
      left: ${Math.random() * 100}%;
      top: ${Math.random() * 100}%;
      box-shadow: 0 0 4px rgba(0,220,255,0.8);
      animation: holo-float ${3 + Math.random() * 4}s ease-in-out
                 ${Math.random() * 3}s infinite;
      pointer-events: none;
    \`;
    container.appendChild(p);
  }
}
```

---

## Layout Patterns

### The Command Deck (3-panel center focus)

```
┌────────────┬──────────────────────┬────────────┐
│  LEFT      │                      │  RIGHT     │
│  PANEL     │   CENTRAL DISPLAY    │  PANEL     │
│  - status  │   (main holo ring,   │  - data    │
│  - metrics │    map, or primary   │  - streams │
│  - alerts  │    visualization)    │  - logs    │
└────────────┴──────────────────────┴────────────┘
│              TICKER BAR / STATUS ROW            │
└─────────────────────────────────────────────────┘
```

### The Floating Cards (Multi-panel scattered)

Cards positioned with slight rotation and varied opacity/depth — simulates 3D projection space.

```
.holo-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
}
.holo-card:nth-child(odd) { transform: rotate(-0.3deg); }
.holo-card:nth-child(even) { transform: rotate(0.3deg); }
```

### The Cockpit (Horizontal bands)

Data in horizontal information bands — common in spaceship/aircraft holographics.

```
┌─────────────────────────────────────────────────┐
│ TOP BAR: NAVIGATION / ORIENTATION               │
├───────────────────────────┬─────────────────────┤
│  LARGE VISUAL DISPLAY     │  INSTRUMENT CLUSTER │
│  (map / radar / 3D)       │  - speed / heading  │
│                           │  - power / shields  │
├───────────────────────────┴─────────────────────┤
│ BOTTOM: ALERTS / COMMS / QUICK ACCESS           │
└─────────────────────────────────────────────────┘
```

---

## Step-by-Step Build Process

### Step 1 — Identify Variant

Ask or infer:

- **Color story**: cyan (pure), green (bio), amber (military), purple (ghost), white (clean)?
- **Information type**: status monitoring? navigation? data viz? control panel?
- **Interactivity level**: display only? hover states? full interactive controls?

### Step 2 — Set the Void

Always start with the dark background and base grid:

```
body {
  background: var(--holo-void);
  min-height: 100vh;
  background-image: radial-gradient(
    ellipse at 50% 50%,
    rgba(0,60,120,0.15) 0%,
    transparent 70%
  );
}
```

### Step 3 — Build Panels Outside-In

1. Outer container with scan-line overlay
2. Panel shells (glass panels, correct variant colors)
3. Corner accents and border geometry
4. Inner content (text, meters, grids)
5. Animations last

### Step 4 — Add the Breath

Set ALL idle panels to `animation: holo-breathe 4s ease-in-out infinite`. Offset delays: `animation-delay: 0s, 1.3s, 2.7s` across panels for organic feel.

### Step 5 — Add the Scan

Include at least one scan-line element that moves across the screen — represents active processing. This is what makes a static mockup feel live.

### Step 6 — Add Particles (if space permits)

Ambient floating particles dramatically increase the "holographic light in air" illusion. Keep count low (15–30) and opacity subtle (0.2–0.5).

---

## Non-Negotiable Rules

1. **Background must be dark** (`#000000` to `#0d0d20` range) — holograms don't project in daylight
2. **All panels semi-transparent** — `rgba()` backgrounds only, never solid color fills
3. **Every border must glow** — `box-shadow` with matching color on every bordered element
4. **At minimum: one breathing panel + one scan animation** — static holographics feel broken
5. **Text must have text-shadow glow** matching the panel's accent color
6. **No white text** — use tinted-white matching the variant palette (e.g., `rgba(160,235,255,0.92)`)
7. **No sharp corners > 2px** on panels (holograms have no physical edges — use 0–2px border-radius)
8. **Letter-spacing minimum 0.08em** on all labels — tight tracking breaks the illusion
9. **Use Google Fonts** — import at least one: `Exo 2`, `Rajdhani`, `Orbitron`, or `Share Tech Mono`
10. **No background images or photographic elements** — holographic UIs are pure light constructs

---

## Quick-Start Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Holographic UI</title>
<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@200;300;400;600&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
:root {
  --holo-void: #000913;
  --holo-surface: rgba(0, 160, 255, 0.04);
  --holo-border: rgba(0, 200, 255, 0.25);
  --holo-edge-glow: rgba(0, 220, 255, 0.6);
  --holo-text: rgba(160, 235, 255, 0.92);
  --holo-text-dim: rgba(80, 180, 220, 0.5);
  --holo-accent: rgba(0, 255, 220, 0.85);
  --holo-warn: rgba(255, 180, 0, 0.85);
  --holo-font: 'Exo 2', sans-serif;
  --mono-font: 'Share Tech Mono', monospace;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: var(--holo-void);
  background-image: radial-gradient(ellipse at 50% 30%, rgba(0,60,140,0.2) 0%, transparent 65%);
  color: var(--holo-text);
  font-family: var(--holo-font);
  min-height: 100vh;
  overflow: hidden;
}
.holo-panel {
  background: var(--holo-surface);
  border: 1px solid var(--holo-border);
  box-shadow: 0 0 20px rgba(0,200,255,0.08), inset 0 0 30px rgba(0,200,255,0.03), 0 0 1px var(--holo-edge-glow);
  position: relative;
  overflow: hidden;
  animation: holo-breathe 4s ease-in-out infinite;
}
.holo-panel::before {
  content: '';
  position: absolute; inset: 0;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,200,255,0.015) 2px, rgba(0,200,255,0.015) 4px);
  pointer-events: none;
}
@keyframes holo-breathe {
  0%,100% { box-shadow: 0 0 20px rgba(0,200,255,0.08), inset 0 0 30px rgba(0,200,255,0.03), 0 0 1px var(--holo-edge-glow); }
  50%     { box-shadow: 0 0 35px rgba(0,200,255,0.16), inset 0 0 40px rgba(0,200,255,0.06), 0 0 2px var(--holo-edge-glow); }
}
@keyframes holo-materialize {
  from { opacity: 0; transform: scale(0.97); filter: blur(3px); }
  to   { opacity: 1; transform: scale(1);    filter: blur(0); }
}
</style>
</head>
<body>
  <!-- Build here -->
</body>
</html>
```

---

## Reference Files

- `references/components.md` — Full component library (HoloRing, HoloGrid, HoloStream, HoloParticles, etc.)
- `references/variants.md` — Complete CSS variable sets for all 5 variants with usage notes
- `references/animations.md` — Full animation library with timing recommendations
- `references/layout-templates.md` — Complete layout HTML for Command Deck, Floating Cards, Cockpit