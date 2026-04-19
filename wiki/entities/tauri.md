---
title: Tauri
type: entity
tags: [desktop-apps, rust, frameworks, tooling]
created: 2026-04-18
updated: 2026-04-18
sources: [opencode-tauri-to-electron.md, opencode-desktop-electron-brendonovich.md]
---

# Tauri

Rust-based desktop application framework. Uses the OS's **native webview** (WebKit on macOS, WebView2 on Windows, webkitgtk on Linux) for the frontend and Rust for the main process. Positioned against [[electron|Electron]] on bundle size, memory footprint, and security model.

## Strengths (per @brendonovich, 2026-04-18)

- Small bundle size (no bundled Chromium)
- Native webviews
- Strong security model
- Fast in the common case

## Where it doesn't fit

When the app's heavy logic runs in a **non-Rust runtime** (Node, Bun, Python), Tauri forces that runtime into a **sidecar process** — adding startup cost, IPC latency, and cross-platform reliability issues. [[opencode|OpenCode]] hit this and switched to Electron; see [[opencode-desktop-electron-brendonovich]] for the primary-source reasoning (and [[opencode-tauri-to-electron]] for the earlier Grok summary).

## WebKit caveat (macOS + Linux)

Tauri uses the **OS-native webview** — Chromium-equivalent **WebView2** on Windows, but **WebKit** on macOS and webkitgtk on Linux. For complex UIs, WebKit has measurably worse rendering perf than Chromium and subtle style inconsistencies, making cross-platform visual parity hard. A **CEF (Chromium Embedded Framework)** backend is in progress to swap the webview for Chromium, but stabilization timing is uncertain (per @brendonovich, 2026-03).

## The Rust-heavy-core sweet spot

Tauri is *"little more than a Rust library for launching and communicating with webviews"* (@brendonovich). You realize its perf advantage when the app's heavy work is written **in Rust** — @brendonovich cites [[@cap]] doing native video encoding/rendering in Rust as the canonical fit. If the heavy work is JS/Python/other, the Rust shell can't move the needle.

## See also

- [[electron]]
- [[opencode]]
- [[opencode-tauri-to-electron]]
