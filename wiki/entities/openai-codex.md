---
title: Codex (OpenAI)
type: entity
tags: [ai, tools, cli, coding, harness]
created: 2026-04-18
updated: 2026-04-18
sources: [alex-ker-harnesses-optimize.md]
---

# Codex (OpenAI)

OpenAI's coding harness — one of the major harnesses in the landscape alongside [[claude-code|Claude Code]], [[opencode|OpenCode]], Cursor, Deep Agent CLI, and Roo Code. Filed under `openai-codex` to disambiguate from the older 2021-era "OpenAI Codex" model.

## Position in harness landscape (per Alex Ker, 2026-04-18)

### Convergence with others

- **Skills progressive disclosure:** Codex, Claude Code, and OpenCode all implement the same pattern — only skill name + description load at startup; full `SKILL.md` loads on demand. Codex's own docs **explicitly call this "progressive disclosure"** and credit it as core to keeping context clean.

### Divergence — MCP tool handling

| Harness | MCP tool loading strategy |
|---|---|
| [[claude-code\|Claude Code]] | Tool-search index at startup; pulls schemas on demand (~85% context reduction per Anthropic) |
| **Codex** | Loads all configured MCP tool definitions into context at session start |
| [[opencode\|OpenCode]] | Loads all configured MCP tool definitions into context at session start (docs warn users to limit server count) |

So Codex users who rely on many MCP servers pay a larger context tax upfront than Claude Code users — actionable implication: be selective about which MCP servers to connect per-project on Codex.

## See also

- [[claude-code]]
- [[opencode]]
- [[alex-ker-harnesses-optimize]]
- [[coding-harness]]
- [[progressive-disclosure]]
- [[model-context-protocol]]
