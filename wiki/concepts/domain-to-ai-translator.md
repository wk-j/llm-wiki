---
title: Domain-to-AI Translator
type: concept
tags: [ai, software-engineering, requirements, roles]
created: 2026-04-15
updated: 2026-04-15
sources: [software-engineer-role-ai-era.md]
---

# Domain-to-AI Translator

An engineering role defined by **converting ambiguous real-world business requirements into specifications precise enough for AI to execute correctly**. The source post calls this "the hardest skill for AI itself to replace."

## The translation problem

Business requirements in the wild are:

- **Ambiguous** — "make checkout faster" doesn't say *how much* faster or *where* the current bottleneck is.
- **Incomplete** — stakeholders omit constraints that feel obvious to them but aren't written down.
- **Context-laden** — the "right" answer depends on regulatory, customer, or internal-political factors that never appear in the ticket.
- **Contradictory** — different stakeholders want incompatible things.

AI executes instructions well, but resolves ambiguity poorly. Whoever sits between the business and the AI determines how much of the real problem actually gets solved.

## Why this resists automation

Translation requires:

1. **Implicit-context inference** — knowing what the stakeholder meant but didn't say.
2. **Tradeoff negotiation** — asking the right question to force an unspoken choice.
3. **Domain fluency** — recognizing that a request violates an invariant the business cares about.
4. **Judgment about completeness** — deciding when a spec is specific enough to hand off without further clarification.

All four depend on cumulative, hard-to-transfer knowledge of a specific organization, product, and industry.

## What a good translation looks like

A good translated spec:

- States success criteria verifiable without re-asking the stakeholder.
- Names invariants the solution must preserve.
- Calls out known edge cases and how to handle each.
- Leaves no decision points the AI would have to guess at.

Compare with [[llm-coding-pitfalls]] principle #4 ("Goal-Driven Execution"): [[andrej-karpathy|Karpathy]]'s observation that strong success criteria let an LLM loop independently, while weak ones ("make it work") require constant clarification. Domain-to-AI translation is the upstream act that produces strong criteria.

## Relationship to prompt engineering

Prompt engineering is a subset of this work focused on the wording of the final instruction to the model. Domain translation is the larger activity that produces *what should be said* in the first place — most of which is gathered from humans, not from a model.

## See also

- [[engineering-role-shift]]
- [[ai-orchestrator]]
- [[llm-coding-pitfalls]]
- [[software-engineer-role-ai-era]]
