---
title: LLM Coding Pitfalls
type: concept
tags: [llm, coding, claude-code, workflow, meta]
created: 2026-04-14
updated: 2026-04-14
sources: [forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls..md]
---

# LLM Coding Pitfalls

Recurring failure modes that LLMs exhibit when editing code, as observed by [[andrej-karpathy]] and codified into the [[karpathy-guidelines]] skill. The pitfalls are behavioral, not capability-limited: the model *can* do the right thing but defaults to the wrong one unless instructed otherwise.

## The four pitfalls

| Pitfall | What it looks like | Corrective principle |
|---|---|---|
| **Hidden confusion** | Silently picking one of several interpretations; fabricating assumptions rather than asking | Surface assumptions; ask when uncertain |
| **Overcomplication** | Adding speculative abstractions, flags, error handlers for impossible states, 200 lines where 50 suffice | Minimum code that solves the problem |
| **Scope drift** | "Improving" adjacent code, reformatting, refactoring unrelated sections, deleting pre-existing dead code | Surgical changes — every line traces to the request |
| **Weak success criteria** | Declaring "done" without verification; treating "make it work" as sufficient | Goal-driven execution with verifiable checks |

## Why they happen

LLMs are trained on code that often contains defensive handling, abstractions, and cleanup commits. They pattern-match toward "what good code looks like" instead of "what this specific task requires." They also want to appear competent — which rewards silent interpretation over asking, and broad activity over narrow precision.

## Countermeasure pattern

The countermeasure in [[karpathy-guidelines]] isn't model tuning — it's an instruction file (`SKILL.md`, `CLAUDE.md`, `AGENTS.md`) read at session start. The same lightweight-schema approach Karpathy uses for [[llm-knowledge-bases]]: behavior steered by a shared markdown contract rather than tooling.

Tradeoff: these guidelines bias toward caution over speed. For trivial tasks, they may be overkill.

## See also

- [[karpathy-guidelines]]
- [[andrej-karpathy]]
- [[llm-knowledge-bases]]
