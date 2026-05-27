---
title: Hotcache

Last updated: 2026-05-27 (DeepSWE/FrontierSWE benchmark ingest)

## Wiki state

- **86 sources ingested**, **162 concept pages**, **129 entity pages**, **0 analysis pages** (all indexed)
- **All source, concept, entity, and analysis pages are Thai-primary.** Keep English for technical terms, proper nouns, filenames, tags, and direct quotes.
- Topics: **DeepSWE / FrontierSWE benchmarks**, **Benchmark Contamination**, **Behavioral Verifier**, **Reward Hacking**, **Long-Horizon Coding**, **Hashline**, **Edit Tool Formats**, **Harness Problem / Edit Boundary**, **oh-my-pi**, **Can Bölük**, **Software After Software**, **Process Drag**, **Value Migration from Code**, **Agent Harness Engineering**, **Harness Ratchet**, **Coding Harness**, **OpenCode vs Anthropic**, plus prior topics (AI + 3D, ASR, memory, slop, TOC, etc.).

## Recent activity

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
  sources/              # One summary per ingested source (86 files)
  entities/             # People, orgs, products (129 files)
  concepts/             # Ideas, frameworks, themes (162 files)
  analysis/             # Saved query results (0 pages)
CLAUDE.md               # Schema and workflows
hotcache.md             # This file — read first each session
```
