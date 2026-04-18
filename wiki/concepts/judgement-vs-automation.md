---
title: Judgement vs. Automation
type: concept
tags: [ai, automation, skills, work, future-of-work]
created: 2026-04-18
updated: 2026-04-18
sources: ["Will AI replace 3D software?.md", llm-era-computer-engineering-nattee.md]
---

# Judgement vs. Automation

A heuristic for predicting which skills get automated: **predictable outputs get automated; judgement-heavy outputs with unpredictable results don't.** Stated succinctly by [[andrew-price|Andrew Price]]: *"If you can predict it, you can train it."*

## The 100-artist test

Ask the same task of 100 practitioners. How much does the output vary?

| Variance | Category | Example (3D/creative) | Automation risk |
|---|---|---|---|
| Low (similar outputs) | Predictable | Retopology, rig weight-painting, clean-up passes | **High** — trainable |
| High (100 different results) | Judgement-heavy | Layout, lighting, color, design, narrative, worldbuilding | **Low** — taste is the product |

The thought experiment is the whole rule.

## Why this framing is useful

- **Personal career bet.** Shifts the question from "will my job be automated?" to "which parts of my day are predictable, and which hinge on taste?"
- **Team portfolio.** Lean headcount toward the judgement tasks; pair junior/predictable work with AI-assisted pipelines.
- **Learning priorities.** Train the parts of your craft that resist automation. Predictable skills are still learnable, but they are not a defensible moat.

## Complementary thesis: hybrid practitioners win

Price pairs the judgement rule with a replacement thesis: *"An artist who uses AI will [replace you]."* The artist with judgement *plus* an AI-augmented pipeline dominates both the pure-AI generalist (no taste) and the pure-3D specialist (too slow). See [[ai-3d-workflow]] for the concrete pipeline. His plumber analogy applies across domains: refusing a tool at 10× the cost is not a viable long-term position.

## Scope — generalizes beyond 3D

Price's examples are all from 3D/visual art, but the rule generalizes cleanly:

- **Software engineering** — boilerplate/CRUD (predictable, automatable) vs. architectural decisions, requirements negotiation, and code review (judgement-heavy). This is exactly the split described in [[engineering-role-shift]]: the middle hollows out while [[ai-orchestrator]]-style upstream and downstream roles expand.
- **Writing** — template filler vs. argument construction.
- **Research** — literature summarization vs. novel framing.

## The compromise criteria rotate — a concrete illustration

Judgement doesn't disappear when automation arrives; its *inputs* rotate. [[nattee-niparnan|Nattee Niparnan]]'s Ep. 2 PoC (2026-04-17) gives a crisp example from framework-selection:

| Era | Questions that drove the choice |
|---|---|
| **Pre-Agent** | "What is the team fluent in?" "Which stack writes fastest?" |
| **With Agent** | "Which framework does the Agent write *most stably* in?" "Which one burns fewer tokens?" |

> "คำถามที่เมื่อ 2 ปีที่แล้วไม่มีในสมองเลย" — Nattee

The act of weighing tradeoffs is unchanged — that's still judgment. But the *resources* being weighed (agent stability, token cost) are new, and a senior who ignores them will make stale choices. The judgment-heavy quadrant is not a fixed list of tasks; it's whichever tasks still require *choosing under current constraints*, and the constraints shift.

See [[taste-paradox]] for the companion worry: acquiring the judgment needed to make these new tradeoffs may itself be harder in the Agent era, because hands-on practice gets skipped.

## Entry-level hiring signal

Price's prediction is general ("judgement survives, predictable tasks go"). Nattee surfaces the labor-market implication from the buyer side: a consulting PoC that would have hired **3–4 RAs** now hires **zero** and spends $140 on tools instead. Whatever corporate arguments exist for keeping junior pipelines alive ("someone has to grow into Senior"), the buy-side incentive to hire fewer entry-level engineers is sharpening fast. This is the pragmatic fallout of the "predictable tasks get automated" rule — junior-level work is, by definition, still predictable.

## See also

- [[will-ai-replace-3d-software]]
- [[ai-3d-workflow]]
- [[andrew-price]]
- [[engineering-role-shift]]
- [[ai-orchestrator]]
- [[harness-engineering]]
- [[domain-to-ai-translator]]
- [[taste-paradox]]
- [[nattee-niparnan]]
- [[llm-era-computer-engineering-nattee]]
