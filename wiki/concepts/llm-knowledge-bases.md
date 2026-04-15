---
title: LLM Knowledge Bases
type: concept
tags: [llm, knowledge-management, obsidian, workflow, meta]
created: 2026-04-12
updated: 2026-04-16
sources: [LLM Knowledge Bases Thread by @karpathy.md, "Karpathy's LLM Wiki The Complete Guide to His Idea File.md"]
---

# LLM Knowledge Bases

A pattern for building personal knowledge bases where the LLM writes and maintains all content. The human curates sources, asks questions, and directs the analysis. The LLM handles summarizing, cross-referencing, filing, and bookkeeping.

This wiki is an implementation of this pattern. The pattern was described as an [[idea-file]] by [[andrej-karpathy]] in a GitHub gist (Apr 2026).

## Why wikis beat RAG

Most people's experience with LLMs and documents is RAG: upload files, retrieve chunks at query time, generate an answer. The problem: "The LLM is rediscovering knowledge from scratch on every question. There's no accumulation."

| Dimension | Traditional RAG | LLM Wiki |
|---|---|---|
| When knowledge is processed | At query time (every question) | At ingest time (once per source) |
| Cross-references | Discovered ad-hoc per query | Pre-built and maintained |
| Contradictions | May not be noticed | Flagged during ingestion |
| Knowledge accumulation | None — starts fresh each query | Compounds with every source and query |
| Output format | Chat responses (ephemeral) | Persistent markdown files (durable) |
| Who maintains it | The system (black box) | The LLM (transparent, editable) |
| Examples | NotebookLM, ChatGPT uploads | This wiki |

Key line: "The knowledge is compiled once and then kept current, not re-derived on every query."

## Architecture (three layers)

1. **Raw sources** — immutable collection of source documents. The LLM reads but never modifies.
2. **The wiki** — LLM-generated markdown files. Summaries, entity pages, concept pages, analysis. The LLM owns this entirely.
3. **The schema** — instructions file (`CLAUDE.md` / `AGENTS.md`) defining structure, conventions, and workflows. Co-evolved with the LLM over time as you discover what works for your domain.

Karpathy's analogy: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## Operations

| Operation | Description |
|---|---|
| **Ingest** | Read a source, create summary, update entity/concept pages, update index and log. A single ingest may touch 10–15 pages. |
| **Query** | Search index → read relevant pages → synthesize answer → optionally file back as analysis page |
| **Lint** | Health check: contradictions, orphan pages, missing pages, stale data, suggested questions |

The compounding loop: sources get ingested into the wiki, queries generate new insights, and the best insights get filed back as wiki pages. "This way your explorations compound in the knowledge base just like ingested sources do."

## Why it works

- LLMs eliminate the maintenance burden that kills human-maintained wikis: "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."
- Cross-references, summaries, and consistency checks happen automatically
- Knowledge compounds — each source and query enriches the whole wiki
- At moderate scale (~100 sources, ~400K words), index files suffice without RAG infrastructure

## Scale considerations

- Small (< 50 sources): index file is sufficient for navigation
- Medium (~100 sources, ~400K words): still works with index files per [[andrej-karpathy]]
- Large: may need a search engine — **qmd** (by Tobi Lütke, Shopify CEO): hybrid BM25/vector/LLM-reranked search, runs locally, has CLI and MCP server

## Historical connection

The pattern is spiritually descended from [[vannevar-bush]]'s 1945 [[memex]] concept — private, curated knowledge with associative trails. The web evolved away from that toward public infrastructure. Bush's unsolved problem was maintenance. LLMs solve it.

## See also

- [[karpathy-llm-knowledge-bases]]
- [[karpathy-llm-wiki-idea-file]]
- [[andrej-karpathy]]
- [[idea-file]]
- [[memex]]
