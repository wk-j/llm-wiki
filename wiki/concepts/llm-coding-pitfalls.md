---
title: LLM Coding Pitfalls
type: concept
tags: [llm, coding, claude-code, workflow, meta]
created: 2026-04-14
updated: 2026-04-18
sources: [forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls..md, llm-era-computer-engineering-nattee.md]
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

## War story — the authorization bug (Nattee, 2026-04-17)

A concrete case from [[nattee-niparnan|Nattee Niparnan]]'s Ep. 2 PoC Web App illustrates how multiple pitfalls compound into a silent but dangerous outcome:

- Each endpoint **passed its unit tests** — individually they looked correct
- **Integration testing revealed** that a Buyer could delete a Seller's resource
- Root cause: no one — human or agent — treated authorization as a **system-wide concern**; each endpoint was built in isolation
- Once told, the Agent fixed the whole system in one commit without difficulty

This is *scope drift* inverted: rather than the Agent wandering beyond the request, it stayed **too narrowly inside** each request and missed the cross-cutting invariant. Combined with *weak success criteria* ("unit tests pass") and *hidden confusion* (it chose a per-endpoint interpretation of authorization without asking), the result was code that looked correct in every local view and failed globally.

> "Agent มันไม่รู้หรอกว่าต้องแก้เรื่องนี้ ถ้าเราไม่สั่ง" — Nattee

Lesson for the pitfalls model: the failure modes aren't independent. Narrow scope + passing-test success criterion + unchallenged default interpretation = confident-looking output that silently breaks a cross-cutting property. The corrective isn't fixing one pitfall — it's asking the Agent explicitly about the *system*, not just the part. This is also the clearest reason the [[taste-paradox]] matters: you can't review for a property your training never taught you to look for.

## See also

- [[karpathy-guidelines]]
- [[andrej-karpathy]]
- [[harness-engineering]]
- [[llm-knowledge-bases]]
- [[taste-paradox]]
- [[nattee-niparnan]]
- [[llm-era-computer-engineering-nattee]]
