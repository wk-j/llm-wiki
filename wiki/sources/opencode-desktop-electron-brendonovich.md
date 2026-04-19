---
title: "Moving OpenCode Desktop to Electron (@brendonovich)"
type: source
tags: [tooling, desktop-apps, electron, tauri, opencode, architecture, webkit, chromium, bun, node]
created: 2026-04-19
updated: 2026-04-19
sources: []
---

# Moving OpenCode Desktop to Electron

Canonical writeup by **@brendonovich** (OpenCode lead engineer, ex-[[@cap]]) on why [[opencode|OpenCode]] Desktop was rebuilt on [[electron|Electron]] and the [[tauri|Tauri]] build is being retired. Posted 2026-03-25 on X: https://x.com/brendonovich/status/2045725889422610602

This is the primary source backing the earlier Grok-summarized writeup in [[opencode-tauri-to-electron]]. It adds three details the summary missed: **WebKit rendering issues**, **Bun → Node migration**, and **plugin compatibility fallout**.

## Architecture baseline

OpenCode is client-server, **TypeScript end-to-end**:

- **Server:** runs agent loops, talks to LLMs, owns a SQLite DB. Invoked as `opencode serve`.
- **Clients:** TUI and Web UI. The Web UI is HTTP-only — it requires a running server.

Desktop existed to give users a one-download experience instead of asking them to run `opencode serve` in a terminal.

## Why Tauri broke down

### 1. WebKit is "asssss" (Adam, quoted)

Tauri uses the OS's native webview. On macOS and Linux that's **WebKit**, which:

- Has **worse rendering performance** than Chromium for OpenCode's UI
- Has **style inconsistencies** with Chromium, making cross-platform visual parity hard

Tauri has an ongoing CEF (Chromium Embedded Framework) effort to swap this out, but the timeline is **uncertain**.

### 2. CLI sidecar was fragile

Bundling the CLI and spawning `opencode serve` on startup:

- Slowed launch (extra process startup)
- **Occasionally just failed**, especially on Windows (per @LukeParkerDev's attempts to stabilize it)

### 3. Bun → Node migration was happening anyway

The team wanted to move server code from **Bun** to **Node** for other reasons. Once that was done, the server could run directly inside Electron's built-in Node process — no CLI, no sidecar, no IPC. That migration *plus* the WebKit issue is what tipped the decision.

## Why Tauri-as-framework isn't at fault

Brendonovich is explicit: **Tauri itself is "little more than a Rust library for launching and communicating with webviews."** You get Tauri's performance advantage when your app's heavy work is **in Rust** — e.g. [[@cap]] doing native video encoding/rendering. OpenCode's heavy work is all TypeScript, so any Rust in the shell "wasn't going to move the needle unless we rewrote the entire core."

Quote: *"Tauri is great, just isn't the right fit for our use case. If you're building an app with a simpler UI that demands native performance or easy access to system APIs, I think Tauri is still a great fit."*

## Fallout: Bun-specific plugins break

Because the server now runs under Node, **any plugins relying on Bun-specific APIs stop working in newer Desktop versions.** The team is deferring the full plugin story to OpenCode 2.0.

## Trade-offs accepted

- **Bundle size:** Electron ships Chromium, so bundles are larger. "It's a trade-off we're willing to make."

## Takeaways

1. **Pick the shell whose main-process runtime hosts your heavy layer in-process.** JS/Node core → Electron. Rust core → Tauri. Crossing the boundary via sidecar/IPC costs startup time *and* reliability.
2. **Native webviews aren't a free win.** WebKit vs Chromium parity is a real tax when your UI is complex. Tauri's CEF path may eventually help, but "eventually" isn't a ship date.
3. **Runtime migrations cascade.** Moving Bun → Node wasn't just a runtime swap — it unlocked the Electron in-process architecture *and* broke a class of user plugins. Downstream costs need to be priced in.

## See also

- [[opencode-tauri-to-electron]] — earlier Grok summary of the same decision
- [[opencode]]
- [[electron]]
- [[tauri]]
