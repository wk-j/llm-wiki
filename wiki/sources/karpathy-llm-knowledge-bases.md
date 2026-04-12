---
title: "LLM Knowledge Bases — Thread by @karpathy"
type: source
tags: [llm, knowledge-management, obsidian, workflow]
created: 2026-04-12
updated: 2026-04-12
sources: [LLM Knowledge Bases Thread by @karpathy.md]
---

# LLM Knowledge Bases — Thread by @karpathy

Twitter thread by [[andrej-karpathy]] (2026-04-02) describing his workflow for using LLMs to build personal knowledge bases.

## Core workflow

1. **Ingest** — Index source documents (articles, papers, repos, images) into `raw/`. Use LLM to incrementally "compile" a wiki of `.md` files. Uses Obsidian Web Clipper + hotkey to download images locally.
2. **IDE** — Obsidian as the frontend to view raw data, compiled wiki, and derived visualizations. LLM writes and maintains all wiki content. Marp plugin for slides.
3. **Q&A** — At scale (~100 articles, ~400K words), ask complex questions against the wiki. LLM researches answers across pages. Index files + brief summaries work well enough — no RAG needed at this scale.
4. **Output** — Render answers as markdown, Marp slides, or matplotlib images — all viewable in Obsidian. File outputs back into the wiki so explorations compound.
5. **Linting** — Run LLM health checks: find inconsistencies, impute missing data with web search, discover connections, suggest new questions.
6. **Extra tools** — Vibe-coded a small search engine over the wiki (web UI + CLI for LLM tool use).

## Key insights

- "A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge"
- Schema kept in `AGENTS.md` — LLMs get nested `.md` directories easily
- Early ingests are manual and human-in-the-loop. After a while, the LLM "gets" the pattern and marginal documents become easy: "just say 'file this new doc to our wiki'"
- No need for fully autonomous batch processing — one-by-one with human guidance works well
- Future direction: synthetic data generation + finetuning to put knowledge in weights instead of context

## Notable replies

- On incremental compilation: not fully autonomous, human stays in the loop especially early on
- On tooling: keeps it "super simple and flat" — nested directory of `.md` and `.png`, schema in `AGENTS.md`, custom tools vibe-coded as needed
- "I vibe code products with twitter"

## See also

- [[llm-knowledge-bases]]
- [[andrej-karpathy]]
