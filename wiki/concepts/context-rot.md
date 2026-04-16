---
title: Context Rot
type: concept
tags: [ai, context-management, claude-code, performance]
created: 2026-04-16
updated: 2026-04-16
sources: [Using Claude Code Session Management & 1M Context.md]
---

# Context Rot

The observation that **LLM output quality degrades as the context window fills**. As more tokens accumulate, attention spreads across a larger surface; older, irrelevant content distracts from the current task and reduces effective reasoning quality.

## Characteristics

- **Gradual, not sudden.** Rot begins well before the hard context limit.
- **Task-dependent.** Simple retrieval tasks tolerate longer contexts better than reasoning-heavy tasks.
- **For [[claude-code|Claude Code]]'s 1M context model:** noticeable around 300–400k tokens ([[anthropic|Anthropic]]'s observed threshold), but not a rigid rule.

## Why it matters for session design

Context rot is the hidden cost of long sessions. Even when a session is technically viable (tokens remain), the model becomes incrementally less capable. This is why session management techniques ([[compaction]], /rewind, subagents) exist — not just to avoid hitting the limit, but to keep the active context *useful*.

The model is also at its **least intelligent point** when autocompact fires (context rot is at its worst). This makes proactive manual compaction — with explicit steering — more reliable than leaving it to autocompact.

## Mitigations

| Technique | How it helps |
|-----------|-------------|
| **/rewind** | Drop failed attempts from context immediately rather than accumulating them |
| **/compact** (proactive) | Shed weight before rot peaks; steer the summary |
| **/clear + new session** | Full reset; human writes focused brief |
| **Subagents** | Intermediate work stays in a fresh context; only result returns to parent |
| **New session per task** | Prevents rot from accumulating across unrelated work |

## See also

- [[compaction]]
- [[claude-code-session-management]]
- [[claude-code]]
- [[ai-orchestrator]]
