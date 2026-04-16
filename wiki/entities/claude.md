---
title: Claude
type: entity
tags: [ai, models, anthropic, llm]
created: 2026-04-16
updated: 2026-04-16
sources: [Introducing Claude Opus 4.7.md, The advisor strategy Give Sonnet an intelligence boost with Opus.md]
---

# Claude

Family of AI models from [[anthropic|Anthropic]]. Three standard tiers — **Opus** (most capable), **Sonnet** (balanced), **Haiku** (fastest/cheapest) — plus a frontier **Mythos** preview line.

## Current generation (2026-04)

| Model | Tier | Notes |
|---|---|---|
| **[[claude-opus-4-7]]** | Flagship | Released 2026-04-16; successor to Opus 4.6 |
| Claude Opus 4.6 | Flagship (prior) | Still referenced in some APIs and benchmarks |
| Claude Sonnet 4.6 | Balanced | Common executor model in [[advisor-strategy\|advisor pattern]] |
| Claude Haiku 4.5 | Fast | ID `claude-haiku-4-5-20251001` |
| Claude Mythos Preview | Frontier preview | Most capable overall; release restricted for safety |

## Common capabilities

- Multimodal (text + images; Opus 4.7 supports up to 2,576 px long edge)
- Tool use / function calling
- Prompt caching
- Effort levels — `medium` / `high` / `xhigh` / `max`; see [[effort-levels]]
- [[model-context-protocol|MCP]] — tool/data integration protocol
- [[advisor-strategy]] — cheaper Sonnet/Haiku as executor with Opus as advisor
- File-system-based memory (improved in Opus 4.7)

## Surfaces

- [[claude-code|Claude Code]] (CLI)
- Claude.ai (web + desktop apps)
- IDE extensions (VS Code, JetBrains)
- Claude API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry

## See also

- [[anthropic]]
- [[claude-opus-4-7]]
- [[claude-code]]
- [[effort-levels]]
- [[advisor-strategy]]
