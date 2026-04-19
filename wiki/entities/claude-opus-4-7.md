---
title: Claude Opus 4.7
type: entity
tags: [ai, models, anthropic, claude, opus]
created: 2026-04-16
updated: 2026-04-20
sources: [Introducing Claude Opus 4.7.md, Whats new in Claude Opus 4.7 - Anthropic Docs.md, Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md]
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
- **[[task-budgets|Task budgets]]** (API, public beta; beta header `task-budgets-2026-03-13`) — advisory token target across a full agentic loop; distinct from `max_tokens`
- **`/ultrareview`** slash command in [[claude-code|Claude Code]]
- **[[auto-mode|Auto mode]]** extended to Claude Code Max users (the permission mode itself shipped earlier, 2026-03-24, for Team plan — see [[claude-code-auto-mode]])

## API breaking changes (Messages API; Managed Agents unaffected)

- **Extended thinking budgets removed** — `thinking.budget_tokens` → 400. [[adaptive-thinking|Adaptive thinking]] is the only thinking-on mode. Off by default on 4.7 — must opt in explicitly.
- **Sampling parameters removed** — non-default `temperature` / `top_p` / `top_k` → 400. Prompt for the behavior instead.
- **Thinking content omitted by default** — silent change; `thinking` field is empty unless `display: "summarized"` set. Product that streams reasoning to users will show a long pause.
- **New tokenizer** — same text uses ~1.0–1.35× tokens; raise `max_tokens` headroom, revisit compaction triggers. 1M context at standard pricing (no long-context premium).
- **Prefilled assistant responses deprecated** (starting Claude 4.6). Returns **400 error on Mythos Preview**. Redesign prompts that relied on assistant prefills to steer output shape. (Source: [[claude-opus-4-7-migration-pachaar|Pachaar migration guide]].)

## Behavior changes (prompt-level)

- More literal instruction following (especially at lower effort)
- Response length calibrates to task complexity
- Fewer tool calls and fewer subagents by default (raise effort / prompt to increase)
- More direct, opinionated tone; fewer emoji than 4.6
- More regular progress updates during long agentic traces — drop scaffolding added to force interim status
- **Every user turn triggers reasoning** — multi-turn chatty prompting inflates tokens on 4.7 where it was cheap on 4.6. Front-load context into turn 1; see [[delegation-mindset]].
- **Literal-following can drop code-review recall** when harness says "conservative" or "only high-severity" — model finds bugs, then filters them out itself. Fix: [[find-vs-filter]] — separate discovery from triage.

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
