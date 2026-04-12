---
title: LLM Knowledge Bases
type: concept
tags: [llm, knowledge-management, obsidian, workflow, meta]
created: 2026-04-12
updated: 2026-04-12
sources: [LLM Knowledge Bases Thread by @karpathy.md]
---

# LLM Knowledge Bases

A pattern for building personal knowledge bases where the LLM writes and maintains all content. The human curates sources, asks questions, and directs the analysis. The LLM handles summarizing, cross-referencing, filing, and bookkeeping.

This wiki is an implementation of this pattern.

## Architecture (three layers)

1. **Raw sources** — immutable collection of source documents. The LLM reads but never modifies.
2. **The wiki** — LLM-generated markdown files. Summaries, entity pages, concept pages, analysis. The LLM owns this entirely.
3. **The schema** — instructions file (`CLAUDE.md` / `AGENTS.md`) defining structure, conventions, and workflows.

## Operations

| Operation | Description |
|---|---|
| **Ingest** | Read a source, create summary, update entity/concept pages, update index and log |
| **Query** | Search index → read relevant pages → synthesize answer → optionally file back as analysis page |
| **Lint** | Health check: contradictions, orphan pages, missing pages, stale data, suggested questions |

## Why it works

- LLMs eliminate the maintenance burden that kills human-maintained wikis
- Cross-references, summaries, and consistency checks happen automatically
- Knowledge compounds — each source and query enriches the whole wiki
- At moderate scale (~100 sources, ~400K words), index files suffice without RAG infrastructure

## Scale considerations

- Small (< 50 sources): index file is sufficient for navigation
- Medium (~100 sources, ~400K words): still works with index files per [[andrej-karpathy]]
- Large: may need a search engine (e.g. qmd — hybrid BM25/vector search for markdown)

## See also

- [[karpathy-llm-knowledge-bases]]
- [[andrej-karpathy]]
