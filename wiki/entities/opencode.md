---
title: OpenCode
type: entity
tags: [ai, tools, cli, coding, harness, open-source]
created: 2026-04-18
updated: 2026-04-18
sources: [alex-ker-harnesses-optimize.md, opencode-tauri-to-electron.md, opencode-desktop-electron-brendonovich.md]
---

# OpenCode

Open-source coding harness — one of the major harnesses in the landscape alongside [[claude-code|Claude Code]], [[openai-codex|Codex]], Cursor, Deep Agent CLI, and Roo Code.

## Position in harness landscape (per Alex Ker, 2026-04-18)

### Convergence with others

- **Skills progressive disclosure:** OpenCode, Claude Code, and Codex all implement the same pattern — only skill name + description load at startup; full `SKILL.md` loads on demand.

### MCP tool handling

OpenCode loads all configured MCP tool definitions into context at session start. **The OpenCode docs explicitly warn users to limit which servers they enable, because context fills fast.** That warning is itself a signal: users who attach many MCP servers without discipline will run into [[instruction-budget|instruction-budget]] pressure early in the session.

Contrast [[claude-code|Claude Code]], which ships a tool-search index and loads schemas on demand (~85% context reduction per Anthropic).

## Architecture

TypeScript end-to-end, client-server. Server (`opencode serve`) runs agent loops, talks to LLMs, owns a SQLite DB. Clients (TUI, Web UI) talk to it over HTTP. Desktop exists to bundle that server + UI into a one-download app.

## Desktop shell: Tauri → Electron (announced 2026-03-25)

OpenCode's desktop app migrated from [[tauri|Tauri]] to [[electron|Electron]]. Per lead engineer **@brendonovich**, three reasons combined:

1. **JS server can't run in Tauri's main process.** Under Tauri, `opencode serve` had to run as a **sidecar** — extra startup cost, IPC latency, and reliability issues (especially on Windows). Electron's Node main hosts it in-process.
2. **WebKit (Tauri on macOS/Linux) has worse rendering perf and style inconsistencies vs Chromium**, making consistent cross-platform UI hard.
3. **Bun → Node migration** was already underway for other reasons; once complete, the server could drop straight into Electron's built-in Node.

Fallout: **any plugins relying on Bun-specific APIs will not work in newer Desktop versions** — the full plugin story is deferred to OpenCode 2.0. Bundle-size regression is explicitly accepted.

Framed as "right tool for the job," not Tauri-is-bad. Primary source: [[opencode-desktop-electron-brendonovich]]. Earlier summary: [[opencode-tauri-to-electron]].

## See also

- [[claude-code]]
- [[openai-codex]]
- [[alex-ker-harnesses-optimize]]
- [[opencode-desktop-electron-brendonovich]]
- [[opencode-tauri-to-electron]]
- [[tauri]]
- [[electron]]
- [[coding-harness]]
- [[progressive-disclosure]]
- [[model-context-protocol]]
