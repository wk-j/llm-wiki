---
title: OpenCode
type: entity
tags: [ai, tools, cli, coding, harness, open-source]
created: 2026-04-18
updated: 2026-04-18
sources: [alex-ker-harnesses-optimize.md]
---

# OpenCode

Open-source coding harness — one of the major harnesses in the landscape alongside [[claude-code|Claude Code]], [[openai-codex|Codex]], Cursor, Deep Agent CLI, and Roo Code.

## Position in harness landscape (per Alex Ker, 2026-04-18)

### Convergence with others

- **Skills progressive disclosure:** OpenCode, Claude Code, and Codex all implement the same pattern — only skill name + description load at startup; full `SKILL.md` loads on demand.

### MCP tool handling

OpenCode loads all configured MCP tool definitions into context at session start. **The OpenCode docs explicitly warn users to limit which servers they enable, because context fills fast.** That warning is itself a signal: users who attach many MCP servers without discipline will run into [[instruction-budget|instruction-budget]] pressure early in the session.

Contrast [[claude-code|Claude Code]], which ships a tool-search index and loads schemas on demand (~85% context reduction per Anthropic).

## See also

- [[claude-code]]
- [[openai-codex]]
- [[alex-ker-harnesses-optimize]]
- [[coding-harness]]
- [[progressive-disclosure]]
- [[model-context-protocol]]
