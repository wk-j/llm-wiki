---
title: Advisor Strategy
type: concept
tags: [ai, agents, cost-optimization, architecture]
created: 2026-04-16
updated: 2026-04-16
sources: [advisor-strategy.md, Introducing Claude Opus 4.7.md]
---

# Advisor Strategy

An agent architecture where a **cheaper, faster model** (the executor) drives a task end-to-end, escalating to a **stronger, more expensive model** (the advisor) only at decision points it cannot resolve alone. The advisor provides plans, corrections, or stop signals but never calls tools or produces user-facing output.

## How it differs from orchestrator-worker

The traditional [[ai-orchestrator|orchestrator-worker pattern]] uses a large model to decompose work and delegate subtasks to smaller workers. The advisor strategy inverts this:

| | Orchestrator-worker | Advisor strategy |
|---|---|---|
| **Who drives** | Large model | Small model |
| **Who does tool calls** | Workers (small) | Executor (small) |
| **Role of large model** | Decompose, dispatch, merge | Advise on demand |
| **When large model runs** | Every step | Only at escalation |
| **Cost profile** | High (large model always active) | Low (large model intermittent) |

The executor avoids the overhead of decomposition, a worker pool, and orchestration logic. Frontier-level reasoning applies only when needed.

## Why it can be cheaper than the executor alone

Counter-intuitively, adding a more expensive advisor can *reduce* total cost. The advisor's short guidance (400–700 tokens) steers the executor away from expensive dead-end tool loops that would otherwise burn many executor turns.

## When to use

- High-volume agentic workloads where cost matters but quality cannot drop below a threshold.
- Tasks where the executor handles 80%+ of decisions competently — the advisor covers the hard 20%.
- Scenarios where latency of a full Opus run is unacceptable but occasional Opus consultation is fine.

## API support

[[anthropic|Anthropic]] ships the `advisor_20260301` tool type in the Messages API. The executor model decides when to invoke it; handoff happens within a single API request.

With [[claude-opus-4-7|Opus 4.7]] (released 2026-04-16), the natural advisor model upgrades from `claude-opus-4-6` to `claude-opus-4-7` — same API shape and pricing. Executor-side, Sonnet 4.6 and Haiku 4.5 remain the typical choices.

## See also

- [[ai-orchestrator]]
- [[harness-engineering]]
- [[llm-coding-pitfalls]]
- [[model-context-protocol]]
- [[claude-opus-4-7]]
- [[effort-levels]]
