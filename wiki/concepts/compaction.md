---
title: Compaction
type: concept
tags: [ai, context-management, claude-code, productivity]
created: 2026-04-16
updated: 2026-04-16
sources: [Using Claude Code Session Management & 1M Context.md]
---

# Compaction

A session management technique where a **long conversation is summarized into a shorter representation**, replacing the full history with that summary so work can continue on top of it. In [[claude-code|Claude Code]], triggered with `/compact` or automatically when approaching the context limit.

## How it works

Claude reads the current session history, generates a summary of what happened (decisions made, files read, approaches tried, current state), and replaces the message history with that summary. The summary is typically far fewer tokens than the original — shedding weight while (ideally) preserving the task-relevant signal.

## Manual vs. autocompact

**Manual (`/compact`):** Human triggers it deliberately. Can pass instructions to steer what gets kept: `/compact focus on the auth refactor, drop the test debugging`. Produces a more targeted summary.

**Autocompact:** Fires automatically when the context window nears its limit. The model is at its *weakest* at this point (peak [[context-rot]]). Direction is inferred without instruction — summary quality depends on how predictable the work has been.

## What causes bad compacts

A compact fails when the model can't predict what will matter next. Classic example: autocompact fires after a long debugging session; the next message references "that other warning in bar.ts." The model dropped it because the session's weight was on debugging, not warnings. The fix is to **compact proactively** — before the window forces it — and tell Claude explicitly what matters.

## Compact vs. clear

Compaction and `/clear` both shed context weight but differ in who does the work:

| | `/compact` | `/clear` |
|---|---|---|
| **Who summarizes** | Claude | Human |
| **What's kept** | What Claude judges relevant | What human chose to write down |
| **Effort** | Low | Higher |
| **Fidelity** | Lossy; model's judgment | Precise; human's judgment |
| **Best for** | Continuing same task | Starting distinct task; high-stakes handoffs |

## Steering a compact

Pass instructions inline: `/compact focus on X, ignore Y`. Useful for suppressing large volumes of irrelevant tool output (test run logs, file read dumps) while preserving the decisions and current state.

## See also

- [[context-rot]]
- [[claude-code-session-management]]
- [[claude-code]]
- [[advisor-strategy]]
