---
title: "Using Claude Code: Session Management & 1M Context"
type: source
tags: [ai, claude-code, context-management, agents, productivity]
created: 2026-04-16
updated: 2026-04-16
sources: [Using Claude Code Session Management & 1M Context.md]
---

# Using Claude Code: Session Management & 1M Context

**Source:** Twitter/X thread by [[@trq212]], 2026-04-16  
**URL:** https://x.com/trq212/status/2044548257058328723

## Summary

Practical guide to managing [[claude-code|Claude Code]] sessions against the 1M token context window. Covers [[context-rot]], the five turn-by-turn branching options, [[compaction]], and subagents as context management tools.

## Key Takeaways

### The 1M context trade-off

The 1M token context window enables longer autonomous tasks — building a full-stack app from scratch in one session — but the same property opens the door to context pollution. **When to start a new session:** at the start of a new task. Grey area: related tasks where existing context provides a speed/cost advantage (e.g., writing docs for a feature just implemented).

### Context rot

Model performance degrades as context grows. Attention spreads over more tokens; older irrelevant content distracts from the current task. For the 1M context model, [[context-rot]] is observable around 300–400k tokens. Not a hard rule — highly task-dependent.

### Five branching options at every turn

| Option | What it does | When to use |
|--------|-------------|-------------|
| **Continue** | Send another message in the same session | Default; task is still on track |
| **/rewind** (esc esc) | Jump back to a previous message; drop everything after | Claude tried something that didn't work; re-prompt with what you learned |
| **/clear** | Start fresh; human writes the brief | Unrelated new task; deliberate context reset |
| **Compact** | AI summarizes session; replaces history with summary | Long session, need to shed weight, task continues |
| **Subagents** | Delegate to agent with fresh context; only result returns | Large intermediate output you won't need again |

### Rewind: the high-leverage habit

Double-tap Esc (or `/rewind`) to jump back to any prior message, dropping everything after it. Better than correcting forward: instead of "that didn't work, try X," rewind to just after the file reads and re-prompt with the learnings. Can also ask Claude to "summarize from here" for a handoff message to the rewound version.

### Compact vs. clear

**/compact** — AI decides what mattered. Lossy but automatic; can be steered with instructions (e.g., `/compact focus on auth refactor, drop test debugging`). The model is at its *least intelligent* point when compacting (context rot peak), so compact proactively — before the context window forces it.

**/clear** — Human decides what mattered. More work to write the handoff, but the resulting context is exactly what you chose. Useful when starting a clearly distinct task.

**What causes bad compacts:** Autocompact fires after a long debugging session and the next message references something tangential ("fix that other warning in bar.ts"). The model dropped it from the summary because the session was focused elsewhere. Solution: compact proactively with explicit instructions about what matters.

### Subagents as context management

When Claude spawns a subagent (via the Agent tool), the subagent gets its own fresh context window. It works independently and returns only its final result to the parent. Mental test: *"Will I need this intermediate output again, or just the conclusion?"*

Explicit subagent invocations:
- "Spin up a subagent to verify this work against the spec file."
- "Spin off a subagent to read that other codebase and summarize the auth flow, then implement it yourself."
- "Spin off a subagent to write docs based on my git changes."

## See also

- [[claude-code]]
- [[context-rot]]
- [[compaction]]
- [[advisor-strategy]]
- [[ai-orchestrator]]
- [[effort-levels]]
