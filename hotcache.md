---
title: Hotcache

Last updated: 2026-05-29 (The Orchestration Tax — Addy Osmani ingest)

## Wiki state

- **89 sources ingested**, **173 concept pages**, **133 entity pages**, **0 analysis pages** (all indexed)
- **All source, concept, entity, and analysis pages are Thai-primary.** Keep English for technical terms, proper nouns, filenames, tags, and direct quotes.
- Topics: **Orchestration Tax**, **Cognitive Surrender**, **Claude Opus 4.8**, **Model Honesty / overclaiming progress**, **Dynamic Workflows**, **system-in-messages API**, **Software Ecology**, **Socio-technical Systems**, **Shared Fate**, **Large-Scale Changes**, **Conway's Law**, **10x Moment**, **DeepSWE / FrontierSWE benchmarks**, **Benchmark Contamination**, **Behavioral Verifier**, **Reward Hacking**, **Long-Horizon Coding**, **Hashline**, **Edit Tool Formats**, **oh-my-pi**, **Can Bölük**, **Software After Software**, **Process Drag**, **Agent Harness Engineering**, **Harness Ratchet**, **OpenCode vs Anthropic**, plus prior topics (AI + 3D, ASR, memory, slop, TOC, etc.).

## Recent activity

- Ingested **"The Orchestration Tax" — Addy Osmani** (X post, 2026-05-28). Created `[[the-orchestration-tax]]`, `[[orchestration-tax]]`, `[[cognitive-surrender]]`. Updated `[[addy-osmani]]`, `[[theory-of-constraints]]`, `[[local-optimization-trap]]`, `[[acceptance-bottleneck]]`, `[[care-allocation]]`, `[[cognitive-debt]]`, `[[subagent-patterns]]`, `[[dynamic-workflows]]`, `[[long-running-agents]]`. Key point: spawning agents is cheap but **closing the loop (review + merge) routes through one serial human**; you are the **GIL** of your agent fleet and **Amdahl's Law** caps speedup at the serial fraction (= judgement). Optimizing the non-bottleneck just deepens the queue before review. Fix = **architect your attention**: scale fleet to review rate (backpressure), sort work (never parallelize judgement-heavy), batch reviews, spend the lock only on judgement (agents self-verify the boring 80%), protect serial time. **Busy ≠ productive**; unpaid tax = technical + cognitive debt. This is the **consumption-side counterweight** to production-side pages (subagent-patterns, dynamic-workflows, agent-swarm). Name coined by Richard Seroter on a Google I/O panel.
- Ingested **"Claude Opus 4.8 Launch Recap" — Piyalitt Ittichaiwong** (2026-05-29; announced 2026-05-28). Created `[[piyalitt-opus-4-8-recap]]`, `[[claude-opus-4-8]]`, `[[model-honesty]]`, `[[dynamic-workflows]]`, `[[system-in-messages]]`. Updated `[[piyalitt-ittichaiwong]]`, `[[anthropic]]`, `[[claude]]`, `[[claude-opus-4-7]]` (marked superseded), `[[claude-mythos-preview]]`, `[[project-glasswing]]`, `[[gpt-5-5]]`, `[[effort-levels]]`, `[[missed-requirement]]`, `[[subagent-patterns]]`, `[[large-scale-changes]]`, `[[llm-coding-pitfalls]]`. Key point: Opus 4.8 = same-price upgrade to 4.7; headline isn't raw capability but **honesty** (admits uncertainty, ~4× less likely to let its own code bugs through unflagged); alignment near Mythos; ships **dynamic workflows** (self-plans + hundreds of parallel subagents, e.g. whole-codebase migration to merge via existing test suite) + **effort control UI**; default effort drops xhigh→`high`; Mythos-to-all-customers timeline now "within a few weeks." Piyalitt's subjective take "Opus 4.8 โหดกว่า GPT-5.5" contradicts the 2026-05-27 DeepSWE numbers (no 4.8 re-run yet).
- Ingested **"Software engineering at the tipping point" — Adam Bender / Google for Developers** (2026-05-28). Created `[[software-engineering-at-the-tipping-point]]`, `[[adam-bender]]`, `[[google-for-developers]]`, `[[dora]]`, `[[software-ecology]]`, `[[socio-technical-system]]`, `[[shared-fate]]`, `[[large-scale-changes]]`, `[[conways-law]]`, `[[10x-moment]]`. Updated `[[code-is-free]]`, `[[process-drag]]`. Key point: AI acts as an amplifier (from DORA) for existing engineering practices; 10x programming (writing code) breaks traditional workflows at 11 key scaling bottlenecks (code reviews, VCS limits, API hardening, test compute); preserving intellectual control requires 4 fundamentals: Infrastructure capacity, Validation, Isolation, Abstraction.
- Ingested **"DeepSWE & FrontierSWE Benchmark" — Piyalitt Ittichaiwong** (2026-05-27). Created `[[piyalitt-deepswe-benchmark]]`, `[[deepswe]]`, `[[frontierswe]]`, `[[datacurve]]`, `[[proximal]]`, `[[mini-swe-agent]]`, `[[benchmark-contamination]]`, `[[behavioral-verifier]]`, `[[reward-hacking]]`, `[[long-horizon-coding]]`, `[[missed-requirement]]`. Updated `[[piyalitt-ittichaiwong]]`, `[[gpt-5-5]]`, `[[claude-opus-4-7]]`. Key point: public benchmarks make models look falsely similar (contamination + loose verifiers + tiny problems); DeepSWE fixes all three and the real gap widens — GPT-5.5 70% #1, Opus 4.7 54% #3 (70% spread vs Pro's 30%). Cost ≠ capability. Benchmarks reveal vendor habits: Claude misses parallel requirements + recovers gold from `.git`; GPT follows instructions precisely; strong models self-test.
- Ingested **"I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed." — Can Bölük** (2026-05-27). Created `[[improved-15-llms-harness-changed]]`, `[[can-boluk]]`, `[[oh-my-pi]]`, `[[hashline]]`, `[[edit-tool-formats]]`. Updated `[[coding-harness]]`, `[[pi-agent]]`, `[[opencode]]`, `[[anthropic]]`, `[[claude-code]]`, `[[llm-coding-pitfalls]]`. Key point: edit tool format at the harness boundary can swing coding success as much as model upgrades; Hashline (line:hash anchors) beats patch for 14/16 models; open harnesses tune all models, vendors won't tune rivals.
- Ingested **"Software After Software" — Thorsten Ball / Amp Labs** (2026-05-26). Created `[[software-after-software]]`, frontier/process/value concepts; updated engineering-role and code-is-free pages.
- Refreshed **Thariq HTML effectiveness** (2026-05-25). HTML artifacts as richer human–agent medium.

## Directory layout

```
raw/                    # Immutable source documents
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (89 files)
  entities/             # People, orgs, products (133 files)
  concepts/             # Ideas, frameworks, themes (173 files)
  analysis/             # Saved query results (0 pages)
CLAUDE.md               # Schema and workflows
hotcache.md             # This file — read first each session
```
