---
title: Effort Levels
type: concept
tags: [ai, claude, claude-code, performance, cost-optimization]
created: 2026-04-16
updated: 2026-04-16
sources: [Introducing Claude Opus 4.7.md]
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
- [[advisor-strategy]]
- [[claude-code-session-management]]
