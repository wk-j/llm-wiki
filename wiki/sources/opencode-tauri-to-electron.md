---
title: "OpenCode: Tauri to Electron switch reasons"
type: source
tags: [tooling, desktop-apps, electron, tauri, opencode, architecture]
created: 2026-04-18
updated: 2026-04-18
sources: []
---

# OpenCode: Tauri to Electron switch reasons

Grok-summarized explanation from [[opencode|OpenCode]]'s lead engineer **@brendonovich** on why their desktop app moved from [[tauri|Tauri]] to [[electron|Electron]]. Source: Grok chat, 2026-04-18.

> **Note (2026-04-19):** The primary-source writeup by @brendonovich is now ingested as [[opencode-desktop-electron-brendonovich]]. It adds WebKit rendering issues, the Bun → Node migration, and Bun-API plugin breakage — none of which made it into this Grok summary.

## Core argument

OpenCode is not a typical desktop app. Its heavy lifting (AI agents, code editing) happens in a **JS/Bun server** (`opencode serve`). The desktop shell is thin. So the question isn't "Rust-lightweight vs Chromium-heavy" in the abstract — it's "where does the server run relative to the shell?"

## Why Tauri was the wrong fit

- Tauri's Rust main process couldn't host the Bun/JS server directly, so OpenCode had to spawn it as a **sidecar process**.
- That added:
  - Startup overhead (extra process launch)
  - **IPC latency** between shell and server
  - Reliability problems — crashes and inconsistencies, especially on **Windows/Linux**
- The Rust component was "always tiny compared to the server anyway" — Tauri's main value prop (native Rust perf, small bundle) wasn't being exercised.

## Why Electron fits

- Electron's main process **is** a Node runtime, so OpenCode runs the JS server **in-process** — no sidecar, no IPC hop.
- Result: faster startup, smoother operation.
- Chromium also gives more consistent frontend rendering across OSes for OpenCode's complex UI.

Brendonovich's summary: *"Tauri is fast but requires overhead since we have to spawn 'opencode serve' in a separate process. Electron lets us run the server js in the main process."* And: *"Tauri is great, just isn't the right fit for our use case."*

## Demo

The announcement video shows side-by-side macOS launches: the Electron beta opens its window and becomes responsive noticeably faster than the prior Tauri build.

## Takeaway

Not a "Tauri bad" story. The lesson is **pick the shell whose main-process runtime matches where your logic already lives.** If your core is Rust, Tauri keeps the boundary thin. If your core is JS/Node/Bun, Electron keeps the boundary thin. Crossing the boundary costs an IPC hop and a process — and that cost dominates for apps where the "heavy" layer is the server, not the shell.

## See also

- [[opencode]]
- [[tauri]]
- [[electron]]
- [[coding-harness]]
