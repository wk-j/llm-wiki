---
title: "OpenCode: Tauri to Electron Switch Reasons"
source: "https://grok.com/c/0ad3423d-b6dd-4a4d-a831-060d78d09dc3?rid=7a76bf57-831d-48b1-8459-6230d3208b53"
author:
published:
created: 2026-04-18
description: "Grok is an AI assistant built by xAI. Chat, create images, write code, and get real-time answers from the web and X."
tags:
  - "clippings"
---
**OpenCode switched their desktop app from Tauri to Electron primarily because it was faster, more reliable, and a better architectural fit for their specific setup** —even though Tauri is generally lighter-weight and Rust-based.

The lead engineer (@brendonovich) explained it directly in replies to the announcement post:

- Their core logic is a JS/Bun server (opencode serve) that handles most of the app's heavy lifting (AI agents, code editing, etc.). The Rust component in the Tauri version was "always tiny compared to the server anyway."
- **In Tauri**: They had to spawn the server as a separate process/sidecar. This added startup overhead, inter-process communication (IPC) latency, and reliability issues (e.g., potential crashes or inconsistencies, especially on Windows/Linux).
- **In Electron**: They can run the entire JS server directly in the main process (Node runtime). No extra spawning, no IPC overhead → noticeably faster startup and smoother operation. Chromium also gives better/more consistent frontend performance for their complex UI.

He summarized: "Tauri is fast but requires overhead since we have to spawn 'opencode serve' in a separate process. Electron lets us run the server js in the main process." And "Tauri is great, just isn't the right fit for our use case."

The short video in the original post demonstrates this in action (side-by-side on macOS): the Electron beta launches quicker, opens the app window faster, and feels more responsive right away compared to the prior Tauri build.

The team plans to fully replace the Tauri build with the Electron one soon (beta is available via their GitHub). A longer writeup was teased but the core reasons above cover it from the devs themselves.

Tauri is still excellent for many apps (smaller bundles, native webviews, security model), but OpenCode's architecture—heavy JS server + web frontend—made Electron the pragmatic win for speed and stability. This isn't a "Tauri is bad" story; it's a "right tool for the job" one.

(If you're trying the beta, the link is in the post: [https://github.com/anomalyco/opencode-beta](https://github.com/anomalyco/opencode-beta))