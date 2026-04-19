---
title: "What's new in Claude Opus 4.7 (Anthropic docs)"
type: source
tags: [ai, claude, anthropic, models, api, migration, docs]
created: 2026-04-19
updated: 2026-04-19
url: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7.md
date_published: 2026-04-16
sources: [Whats new in Claude Opus 4.7 - Anthropic Docs.md]
---

# What's new in Claude Opus 4.7 (Anthropic docs)

Developer-facing companion to the [[claude-opus-4-7-announcement|Opus 4.7 announcement]]. Covers API-level breaking changes, new knobs (`task_budget`, `xhigh`, adaptive-thinking-only), behavior changes, and migration notes — the stuff the marketing post skips.

## Model card

- **Model ID:** `claude-opus-4-7`
- **Context:** 1M tokens at standard pricing (no long-context premium)
- **Max output:** 128k tokens
- **Thinking:** [[adaptive-thinking|adaptive thinking]] only — extended-thinking budgets removed

## Headline new features

### High-resolution image support
- 2576 px / 3.75 MP max (up from 1568 px / 1.15 MP in prior Claudes)
- **Coordinates now 1:1 with actual pixels** — no scale-factor math when mapping coords back to images
- Improved low-level perception (pointing, measuring, counting) and natural-image bounding-box localization
- High-res images cost more tokens; downsample if you don't need the fidelity

### `xhigh` effort level
- Start with `xhigh` for coding/agentic use; minimum `high` for most intelligence-sensitive tasks
- Messages API only; Claude Managed Agents chooses effort automatically
- See [[effort-levels]]

### Task budgets (beta)
- Beta header: `task-budgets-2026-03-13`
- Set via `output_config.task_budget = {"type": "tokens", "total": N}`; minimum 20k
- Advisory, not hard — distinct from `max_tokens`. Model sees a running countdown
- Don't set for open-ended quality-critical work
- See [[task-budgets]]

## Breaking changes (Messages API)

Managed Agents unaffected. Three API-breaking changes + one silent behavior change:

| Change | What breaks | Migration |
|---|---|---|
| Extended thinking budgets removed | `thinking.budget_tokens` → 400 | Use `thinking: {type: "adaptive"}` + `output_config.effort` |
| Sampling params removed | Non-default `temperature` / `top_p` / `top_k` → 400 | Omit entirely; prompt for the behavior |
| Thinking content omitted by default | Silent; stream still shows thinking blocks but `thinking` field is empty | Opt in with `thinking.display = "summarized"` |
| New tokenizer | Same text maps to 1.0×–1.35× tokens; `count_tokens` returns different numbers | Raise `max_tokens` headroom, revisit compaction triggers |

**Gotcha:** adaptive thinking is **off by default** on 4.7. Requests with no `thinking` field run without thinking — unlike some earlier setups. Opt in explicitly.

**Streaming gotcha:** if your product streams reasoning to users, the new default (empty `thinking` field) will appear as a long silent pause before output begins. Set `display: "summarized"` to restore visible progress.

## Capability improvements

- **.docx redlining / .pptx editing** — better at producing and self-checking tracked changes and slide layouts
- **Charts/figures** — improved programmatic tool-calling with PIL-style libs, down to pixel-level data transcription
- **Memory** — better at writing/using file-system memory; direct payoff for agents with scratchpads, notes files, or [[llm-knowledge-bases|LLM-maintained wikis]]
- Existing prompts with "double-check the slide layout before returning"-style scaffolding: try removing and re-baselining

## Behavior changes (prompt-level, not API-breaking)

- **More literal instruction following** — especially at lower effort. Won't generalize from one item to another, won't infer unasked requests
- **Response length calibrates to task complexity** rather than defaulting to fixed verbosity
- **Fewer tool calls by default**, more reasoning instead — raising effort increases tool use
- **More direct, opinionated tone** — less validation-forward, fewer emoji than 4.6
- **More regular progress updates** in long agentic traces (drop your "give me interim status" scaffolding)
- **Fewer subagents spawned by default** — steerable by prompt
- **Real-time cyber safeguards** — refusals on prohibited/high-risk topics; legit security work → Cyber Verification Program

## Implications for wiki topics

- **[[claude-code-session-management]]** — "more regular progress updates" and "fewer subagents by default" change the feel of long agentic runs; scaffolding added for earlier models may now be counterproductive
- **[[llm-coding-pitfalls]]** — literal instruction following addresses the "scope drift" pitfall; fewer unsolicited generalizations
- **[[coding-harness]]** — harness authors should re-examine boilerplate ("always respond with X") now that 4.7 calibrates length to task complexity
- **[[subagent-patterns]]** — the default shift (fewer subagents) means fan-out now requires explicit prompting
- **[[advisor-strategy]]** — `task_budget` is a new lever to cap advisor-as-pipeline-judge spend
- **[[llm-knowledge-bases]] / [[idea-file]]** — file-system memory gains directly benefit the wiki pattern itself

## See also

- [[claude-opus-4-7-announcement]] — marketing/positioning companion
- [[claude-opus-4-7]]
- [[effort-levels]]
- [[task-budgets]]
- [[adaptive-thinking]]
- [[claude]]
- [[anthropic]]
