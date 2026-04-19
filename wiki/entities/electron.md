---
title: Electron
type: entity
tags: [desktop-apps, javascript, node, frameworks, tooling]
created: 2026-04-18
updated: 2026-04-18
sources: [opencode-tauri-to-electron.md, opencode-desktop-electron-brendonovich.md]
---

# Electron

Desktop application framework bundling **Chromium** for the frontend and **Node.js** for the main process. The incumbent — Slack, VS Code, Discord, Figma desktop all ship on Electron. Commonly criticized for bundle size and memory usage versus [[tauri|Tauri]].

## Where it wins (per @brendonovich, 2026-04-18)

When the app's heavy logic is **already JS/Node/Bun**, Electron's Node main process hosts that logic **in-process** — no sidecar, no IPC hop. This is why [[opencode|OpenCode]] switched from Tauri: their `opencode serve` server (migrated from Bun to Node as part of the same move) runs directly inside Electron's main, cutting startup overhead and removing a class of cross-platform reliability bugs. **Chromium** also gives more consistent frontend rendering across OSes than platform-native webviews — relevant because Tauri uses **WebKit** on macOS/Linux, where rendering perf and style parity are measurably worse for complex UIs. Trade-off explicitly accepted: larger bundle size.

Full primary-source reasoning: [[opencode-desktop-electron-brendonovich]].

## See also

- [[tauri]]
- [[opencode]]
- [[opencode-desktop-electron-brendonovich]]
- [[opencode-tauri-to-electron]]
