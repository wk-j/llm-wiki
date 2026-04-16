---
title: "Introducing Claude Opus 4.7"
type: source
tags: [ai, claude, anthropic, models, announcement]
created: 2026-04-16
updated: 2026-04-16
url: https://www.anthropic.com/news/claude-opus-4-7
date_published: 2026-04-16
sources: [Introducing Claude Opus 4.7.md]
---

# Introducing Claude Opus 4.7

[[anthropic|Anthropic]] product announcement for **Claude Opus 4.7**, released 2026-04-16. A software-engineering-focused direct upgrade to Opus 4.6, available across all Anthropic products, API, Amazon Bedrock, Vertex AI, and Microsoft Foundry.

## Core positioning

Opus 4.7 is a **direct upgrade to Opus 4.6** — same price, same API shape, improved quality. Notable themes:

- **Advanced software engineering** — gains on the hardest tasks; can be handed long-running work "that previously needed close supervision"
- **Self-verification** — the model "devises ways to verify its own outputs before reporting back"
- **Instruction following** — substantially more literal; prompts tuned for earlier models may now produce unexpected results
- **Tasteful output** — higher-quality interfaces, slides, docs
- Less broadly capable than **Claude Mythos Preview** ([[anthropic|Anthropic]]'s current frontier model), but better than Opus 4.6 across benchmarks

## Key capability upgrades

### Vision
- Accepts images up to **2,576 pixels on the long edge** (~3.75 megapixels)
- **~3× the pixel capacity** of prior Claude models
- Unlocks dense-screenshot agents, complex diagram extraction, pixel-perfect reference work
- Model-level change — no API parameter; users can downsample to save tokens

### Memory
- Better at using **file-system-based memory**
- Remembers notes across long, multi-session work and carries them to new tasks with less up-front context
- Direct relevance to [[llm-knowledge-bases|LLM-maintained knowledge bases]] and [[idea-file|idea files]]

### Benchmarks
- **State-of-the-art** on Finance Agent evaluation
- **State-of-the-art** on GDPval-AA (third-party economically-valuable knowledge-work eval)
- Better than Opus 4.6 on SWE-bench Verified/Pro/Multilingual, Terminal-Bench 2.0, CyberGym, MCP-Atlas

### Safety
- Similar overall safety profile to Opus 4.6
- **Improved**: honesty, prompt-injection resistance
- **Regressed**: modestly weaker on harm-reduction advice for controlled substances
- Alignment assessment: "largely well-aligned and trustworthy, though not fully ideal"
- Mythos Preview remains Anthropic's best-aligned model

## Pricing and availability

Same pricing as Opus 4.6:
- **$5 / million input tokens**
- **$25 / million output tokens**

Model ID: `claude-opus-4-7`. Available on Claude products, Claude API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry.

## Cybersecurity posture (Project Glasswing)

- Cyber capabilities **differentially reduced during training**
- Safeguards auto-detect and block prohibited/high-risk cyber requests
- **Cyber Verification Program** for legitimate security researchers (vulnerability research, pentesting, red-teaming)
- Opus 4.7 is the first model tested with these safeguards; learnings feed toward a broader Mythos-class release

## Also launching today

### New `xhigh` effort level
See [[effort-levels]]. A new tier between `high` and `max`. In [[claude-code|Claude Code]], default raised to `xhigh` for all plans. For coding/agentic use, recommendation is to start with `high` or `xhigh`.

### Task budgets (API, public beta)
Guide Claude's token spend across longer runs — prioritize work within a budget.

### `/ultrareview` slash command (Claude Code)
Dedicated review session that reads through changes and flags bugs / design issues. Three free sessions for Pro and Max users.

### Auto mode extended to Max users
Permissions option where Claude makes decisions on the user's behalf — longer autonomous runs with less risk than "skip all permissions."

## Migration from 4.6 → 4.7

Two token-usage changes to plan for:

1. **Updated tokenizer** — same input maps to more tokens (roughly **1.0–1.35×** depending on content).
2. **More thinking at higher effort** — particularly on later turns in agentic settings.

Net effect on internal coding eval: **favorable** tokens-per-result across all effort levels. Anthropic recommends measuring on real traffic.

Controls:
- Tune the effort parameter (see [[effort-levels]])
- Use task budgets
- Prompt for conciseness
- Use the [[advisor-strategy]] to keep Opus usage intermittent

## Implications for existing wiki topics

- **[[advisor-strategy]]**: Opus 4.7 becomes the natural advisor model succeeding Opus 4.6 in the Sonnet-executor + Opus-advisor pattern.
- **[[claude-code-session-management]]**: `xhigh` default and `/ultrareview` change the turn-by-turn palette; auto mode is a new branch for long autonomous work.
- **[[llm-knowledge-bases]] / [[idea-file]]**: Better file-system memory means less up-front context loading per session.
- **[[llm-coding-pitfalls]]**: Self-verification before reporting back addresses Karpathy's "weak success criteria" pitfall.

## See also

- [[anthropic]]
- [[claude]]
- [[claude-opus-4-7]]
- [[claude-code]]
- [[effort-levels]]
- [[advisor-strategy]]
- [[claude-code-session-management]]
