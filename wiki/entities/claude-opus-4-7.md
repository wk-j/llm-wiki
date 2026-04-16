---
title: Claude Opus 4.7
type: entity
tags: [ai, models, anthropic, claude, opus]
created: 2026-04-16
updated: 2026-04-16
sources: [Introducing Claude Opus 4.7.md]
---

# Claude Opus 4.7

[[anthropic|Anthropic]]'s flagship general-availability model as of **2026-04-16**. Direct successor to Opus 4.6.

**Model ID:** `claude-opus-4-7`
**Pricing:** $5 / million input tokens, $25 / million output tokens (unchanged from 4.6)

## Positioning relative to siblings

- **Better than Opus 4.6** across benchmarks (SWE-bench, Terminal-Bench 2.0, CyberGym, MCP-Atlas, Finance Agent, GDPval-AA)
- **Less broadly capable than Claude Mythos Preview** ([[anthropic|Anthropic]]'s frontier, release-restricted)
- Shares API shape with Sonnet 4.6 and Haiku 4.5 — [[effort-levels]], prompt caching, tools

## Headline improvements over Opus 4.6

| Area | Change |
|---|---|
| **Software engineering** | Notable gains on hardest tasks; reliable on long-running coding work |
| **Self-verification** | Model devises its own checks before reporting back |
| **Instruction following** | Substantially more literal — old prompts may need retuning |
| **Vision** | Up to 2,576 px on long edge (~3× prior Claude models) |
| **File-system memory** | Better at carrying notes across multi-session work |
| **Prompt injection resistance** | Improved |
| **Honesty** | Improved |
| **Tasteful outputs** | Higher-quality UIs, slides, docs |

## Regressions / tradeoffs

- Modestly weaker on harm-reduction advice for controlled substances
- **More tokens used**: updated tokenizer (+0–35% on identical input) and more thinking at higher effort on later agentic turns — net effect on internal coding eval token cost is still favorable

## New controls launched alongside

- **`xhigh` effort level** — see [[effort-levels]]
- **Task budgets** (API, public beta) — token-spend ceilings across longer runs
- **`/ultrareview`** slash command in [[claude-code|Claude Code]]
- **Auto mode** extended to Claude Code Max users

## Cyber posture

- Cyber capabilities **differentially reduced during training**
- Automatic safeguards block prohibited / high-risk cyber requests
- **Cyber Verification Program** for legitimate security research
- Part of [[anthropic|Anthropic]]'s **Project Glasswing** — pilot safeguards on 4.7 before broader Mythos-class release

## Availability

- Claude products (Claude.ai, [[claude-code|Claude Code]])
- Claude API (`claude-opus-4-7`)
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry

## Role in existing wiki patterns

- **[[advisor-strategy|Advisor strategy]]**: natural advisor model succeeding Opus 4.6
- **[[llm-knowledge-bases|LLM wikis]]**: better file-system memory reduces session reloading cost
- **[[claude-code-session-management|Session management]]**: default [[claude-code|Claude Code]] effort raised to `xhigh`; auto mode is a new long-run option

## See also

- [[claude]]
- [[anthropic]]
- [[claude-code]]
- [[effort-levels]]
- [[advisor-strategy]]
