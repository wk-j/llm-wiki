---
title: Claude Code
type: entity
tags: [ai, claude, tools, agents, cli, coding]
created: 2026-04-16
updated: 2026-04-16
sources: [Introducing Claude Opus 4.7.md, Using Claude Code Session Management & 1M Context.md, forrestchang andrej-karpathy-skills.md]
---

# Claude Code

[[anthropic|Anthropic]]'s terminal-based coding agent — a CLI that drives [[claude|Claude]] through software engineering tasks with shell access, file edits, and tools. Also available as desktop app (Mac/Windows), web (claude.ai/code), and IDE extensions (VS Code, JetBrains).

## Session architecture

See [[claude-code-session-management]] for the full model. At each turn the user chooses from five options:

1. **Continue** — send another message
2. **`/rewind`** (esc esc) — jump back to a previous message, drop everything after
3. **`/clear`** — start fresh; user writes the new brief
4. **`/compact`** — AI summarizes history in place; see [[compaction]]
5. **Subagent** — delegate to a fresh-context agent; only result returns

These exist because of [[context-rot]] — model quality degrades as context fills. Claude Code's 1M token context is usable but the sweet spot sits well below it.

## Features and commands

- **Slash commands** — bundled (`/compact`, `/clear`, `/rewind`, `/ultrareview`, `/help`) plus user-defined
- **`/ultrareview`** — dedicated review session flagging bugs and design issues (launched with [[claude-opus-4-7|Opus 4.7]]; 3 free sessions for Pro/Max)
- **Subagents** — spawned via the Agent tool; fresh context window per agent
- **Skills** — packaged prompts/instructions (e.g., [[forrestchang]]'s [[llm-coding-pitfalls|karpathy-guidelines]])
- **Hooks** — shell commands triggered by harness events (configured in `settings.json`)
- **Auto mode** — permissions option where Claude decides on the user's behalf for longer autonomous runs (extended to Max users with Opus 4.7)
- **MCP servers** — integrate external tools via [[model-context-protocol]]
- **Fast mode** — `/fast` toggles a faster-output variant (available on Opus 4.6)

## Effort levels

With [[claude-opus-4-7|Opus 4.7]], the default effort in Claude Code was raised to **`xhigh`** for all plans. Recommended start for coding/agentic use: `high` or `xhigh`. See [[effort-levels]].

## 1M token context window

Enables long autonomous tasks (full-stack build in one session) but exposes [[context-rot]] around 300–400k tokens. Session management is the main user-facing skill.

## See also

- [[claude]]
- [[anthropic]]
- [[claude-opus-4-7]]
- [[claude-code-session-management]]
- [[context-rot]]
- [[compaction]]
- [[effort-levels]]
