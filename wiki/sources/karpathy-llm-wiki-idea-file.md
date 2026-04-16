---
title: "Karpathy's LLM Wiki: The Complete Guide to His Idea File"
type: source
tags: [llm, knowledge-management, obsidian, workflow, meta]
created: 2026-04-16
updated: 2026-04-16
sources: ["Karpathy's LLM Wiki The Complete Guide to His Idea File.md"]
---

# Karpathy's LLM Wiki: The Complete Guide to His Idea File

Published Apr 4 2026 on antigravity.codes. A deep dive into [[andrej-karpathy]]'s follow-up GitHub gist after his viral LLM Knowledge Bases tweet — covering every concept, tool, and technique with implementation examples.

Source: https://antigravity.codes/blog/karpathy-llm-wiki-idea-file  
Gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## The viral moment

The original Apr 3 2026 tweet described Karpathy's shift from spending tokens on code to spending tokens on **knowledge**. The follow-up gist was titled "LLM Wiki" and described the pattern at a conceptual/architectural level — not code, not an app, but an [[idea-file]].

## Idea Files — a new format for the agent era

Karpathy's definition: "In this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it for your specific needs."

The gist is "intentionally kept a little bit abstract/vague because there are so many directions to take this in." Its last line: "The document's only job is to communicate the pattern. Your LLM can figure out the rest."

## Wiki beats RAG

Karpathy's explicit comparison:

| Dimension | Traditional RAG | LLM Wiki |
|---|---|---|
| When knowledge is processed | At query time (every question) | At ingest time (once per source) |
| Cross-references | Discovered ad-hoc per query | Pre-built and maintained |
| Contradictions | May not be noticed | Flagged during ingestion |
| Knowledge accumulation | None — starts fresh each query | Compounds with every source and query |
| Output format | Chat responses (ephemeral) | Persistent markdown files (durable) |
| Who maintains it | The system (black box) | The LLM (transparent, editable) |
| Human role | Upload and query | Curate, explore, and question |
| Examples | NotebookLM, ChatGPT uploads | Karpathy's LLM Wiki pattern |

Key line: "The knowledge is compiled once and then kept current, not re-derived on every query."

## Three-layer architecture

1. **Raw sources** (`raw/`) — immutable. LLM reads but never modifies. Source of truth for verification.
2. **The wiki** (`wiki/`) — LLM-generated markdown. Summaries, entity pages, concept pages, comparisons. LLM owns entirely.
3. **The schema** (`CLAUDE.md` / `AGENTS.md` / `OPENCODE.md`) — tells the LLM conventions and workflows. "The key configuration file — what makes the LLM a disciplined wiki maintainer rather than a generic chatbot." Co-evolved with the LLM over time.

## Three operations

- **Ingest** — Drop source into `raw/`, tell LLM to process. A single ingest can touch 10–15 wiki pages: new summary, updated concept pages, updated entity pages, updated index, log entry.
- **Query** — LLM reads index, finds relevant pages, synthesizes with citations. Good answers can be filed back as wiki pages — "your explorations compound in the knowledge base just like ingested sources do."
- **Lint** — Health check: contradictions, stale claims, orphan pages, missing-concept pages, suggested investigations.

## Tool stack

| Tool | Role | Required? |
|---|---|---|
| LLM Agent (Claude Code, Codex, etc.) | Wiki maintainer | Required |
| Obsidian | IDE/viewer for browsing | Recommended |
| Obsidian Web Clipper | Clip web articles to markdown | Recommended |
| Git | Version control | Recommended |
| qmd (by Tobi Lütke) | Hybrid BM25/vector/LLM-reranked search for markdown | Optional (needed at scale) |
| Marp | Markdown slide decks | Optional |
| Dataview | SQL-like queries over frontmatter | Optional |

**qmd** specifics: built by Shopify CEO Tobi Lütke. Runs locally via `node-llama-cpp`. Has both CLI (LLM can shell out) and MCP server. Useful once the wiki grows beyond what `index.md` can handle in one context window.

**Image tip**: In Obsidian Settings → Files and links, set attachment folder to `raw/assets/`. Bind "Download attachments for current file" to a hotkey — downloads all images locally so the LLM can view them directly.

## Indexing and logging

- **`index.md`** — content catalog. LLM reads this first to find relevant pages at query time. "Works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure."
- **`log.md`** — append-only activity timeline. Consistent prefix (`## [YYYY-MM-DD] ingest | Title`) makes it parseable with `grep "^## [" log.md | tail -5`.

## Use cases

- Personal knowledge base (goals, health, psychology, journal entries)
- Research (Karpathy's primary use: ~100 articles, ~400K words on one ML topic)
- Reading a book (character/theme/timeline pages — like a personal fan wiki)
- Business/team (Slack threads, meeting transcripts, customer calls — LLM does maintenance no one wants to do)
- Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives

## The Memex connection

Karpathy closes with [[vannevar-bush]]'s 1945 [[memex]] concept: a personal, curated knowledge store with associative trails between documents. "Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that."

## Community patterns from the gist

- **`.brain` folder** — project-level persistent memory: `index.md`, `architecture.md`, `decisions.md`, `changelog.md`. Rule: "Read .brain before making changes. Update .brain after."
- **Inter-agent gists** — using GitHub gists to pass context between different AI agents (Claude, Grok, etc.) — agent-to-agent communication
- **Append-and-review note** — Karpathy's earlier simpler pattern (bearblog 2025): append-only notes file, periodically reviewed. LLM Wiki is the evolved version where the LLM does the review automatically.

## See also

- [[andrej-karpathy]]
- [[karpathy-llm-knowledge-bases]]
- [[llm-knowledge-bases]]
- [[idea-file]]
- [[memex]]
- [[vannevar-bush]]
