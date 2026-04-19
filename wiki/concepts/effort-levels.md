---
title: Effort Levels
type: concept
tags: [ai, claude, claude-code, performance, cost-optimization]
created: 2026-04-16
updated: 2026-04-20
sources: [Introducing Claude Opus 4.7.md, Whats new in Claude Opus 4.7 - Anthropic Docs.md, Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md]
---

# Effort Levels

[[anthropic|Anthropic]]'s explicit parameter for trading **reasoning quality against latency and token cost** on [[claude|Claude]] models. The caller picks a tier; the model allocates more or less thinking time accordingly.

## Tiers (as of Opus 4.7)

| Level | Position | When to use |
|---|---|---|
| `medium` | Low | Simple tasks, quick responses |
| `high` | Mid-high | Recommended starting point for coding / agentic use |
| **`xhigh`** | New with Opus 4.7 | Extra reasoning for hard problems; default in [[claude-code\|Claude Code]] |
| `max` | Top | Hardest problems; highest latency and token cost |

`xhigh` was introduced with [[claude-opus-4-7|Opus 4.7]] to give finer-grained control between `high` and `max`.

**Third-party claim:** [[claude-opus-4-7-migration-pachaar|Pachaar's migration guide]] describes five tiers (adding `low` below `medium`) for "latency-sensitive, tightly scoped work." Anthropic's official docs list only the four above. Treat `low` as unverified until Anthropic confirms.

## Mid-task effort toggling

Effort is not a set-once knob. Pachaar's pattern: **raise and lower effort across phases of the same task** to control token spend.

- `xhigh` for the design/planning phase (hardest reasoning, picks architecture)
- `high` for straightforward implementation once the plan is set
- `max` briefly for a stubborn debugging moment, then back down

Opus 4.7 respects effort more strictly than 4.6 — if `low`/`medium` feels under-thought, raise effort instead of padding the prompt with "think harder" language.

**Opus 4.7 recommendation** (from the docs): start with `xhigh` for coding and agentic use cases; use a minimum of `high` for most intelligence-sensitive use cases. Messages API only — Claude Managed Agents picks effort automatically.

## Relation to adaptive thinking

Effort ≠ thinking. [[adaptive-thinking|Adaptive thinking]] is a separate on/off-and-display setting that controls whether the model is allowed to reason before replying. On 4.7, thinking is off by default — `effort` alone won't turn it on; caller must pass `thinking: {type: "adaptive"}` explicitly.

## Effect on token usage

Higher effort means more thinking — especially on later turns in agentic settings. Combined with [[claude-opus-4-7|Opus 4.7]]'s updated tokenizer (input maps to 1.0–1.35× more tokens), migrations need real-traffic measurement. Anthropic's internal coding eval shows favorable tokens-per-result across all effort levels after the upgrade.

## Controlling cost

- Lower effort for simpler tasks
- **Task budgets** (API, public beta) — ceiling on token spend per run
- Prompt the model to be more concise
- Use the [[advisor-strategy]] — keep the executor on a modest effort, escalate to an Opus advisor only at hard decisions

## See also

- [[claude-opus-4-7]]
- [[claude-code]]
- [[adaptive-thinking]]
- [[task-budgets]]
- [[advisor-strategy]]
- [[claude-code-session-management]]
