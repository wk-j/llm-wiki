---
title: "The Advisor Strategy: Give Agents an Intelligence Boost"
type: source
tags: [ai, agents, cost-optimization, claude, api]
created: 2026-04-16
updated: 2026-04-16
url: https://claude.com/blog/the-advisor-strategy
date_published: 2026-04-09
sources: []
---

# The Advisor Strategy: Give Agents an Intelligence Boost

Anthropic blog post (2026-04-09) introducing the **advisor strategy** and the `advisor_20260301` API tool for the Claude Messages API.

## Core idea

Pair a stronger model (Opus) as an **advisor** with a cheaper model (Sonnet or Haiku) as an **executor**. The executor drives the task end-to-end — calling tools, reading results, iterating. When it hits a decision it can't solve, it escalates to the advisor. The advisor returns a plan, correction, or stop signal, then the executor resumes.

This **inverts** the typical [[ai-orchestrator|orchestrator-worker pattern]], where a larger model decomposes work and delegates to smaller workers. Here the smaller model drives and escalates without decomposition or orchestration logic.

## Benchmark results

| Configuration | SWE-bench Multilingual | BrowseComp | Terminal-Bench 2.0 | Cost vs. Sonnet solo |
|---|---|---|---|---|
| Sonnet solo | baseline | baseline | baseline | 1.0x |
| Sonnet + Opus advisor | **+2.7pp** | improved | improved | **−11.9%** |
| Haiku solo | — | 19.7% | — | — |
| Haiku + Opus advisor | — | **41.2%** (2.1x) | — | **−85%** vs Sonnet |

Key finding: the advisor *reduces* total cost because its guidance helps the executor avoid expensive dead-end tool loops.

## API shape

```python
response = client.messages.create(
    model="claude-sonnet-4-6",  # executor
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-6",  # or claude-opus-4-7 (released 2026-04-16)
            "max_uses": 3,
        },
    ],
    messages=[...]
)
```

- **Single request**: model handoff happens inside one `/v1/messages` call — no extra round-trips or context management.
- **Pricing**: advisor tokens billed at advisor model rates; executor tokens at executor rates. Advisor typically generates 400–700 tokens per invocation.
- **Cost controls**: `max_uses` caps advisor calls per request. Advisor tokens reported separately in usage block.
- **Composable**: works alongside web search, code execution, and other tools in the same loop.

## See also

- [[advisor-strategy]]
- [[ai-orchestrator]]
- [[model-context-protocol]]
- [[claude-opus-4-7]]
- [[anthropic]]
