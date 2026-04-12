# Hotcache

Last updated: 2026-04-12

## Wiki state

- **2 sources ingested**, **5 concept pages**, **1 entity page**, **0 analysis pages**
- Topics: UI/UX design styles, LLM knowledge base pattern (meta)

## Recent activity

- Ingested "UI Style Categories" — taxonomy of ~40+ UI styles across 11 categories
- Ingested "LLM Knowledge Bases Thread by @karpathy" — the original Twitter thread describing this wiki pattern
- Created entity page for Andrej Karpathy
- Created meta concept page for LLM Knowledge Bases (what this wiki implements)
- Dangling wikilinks for UI styles: neumorphism, claymorphism, cyberpunk-neon, vaporwave, synthwave, y2k-aesthetic, memphis-design, art-deco, blobmorphism, anti-design

## Directory layout

```
raw/                    # Immutable source documents
  UI style categories.md
  LLM Knowledge Bases Thread by @karpathy.md
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (2 pages)
  entities/             # People, orgs, products (1 page)
  concepts/             # Ideas, frameworks, themes (5 pages)
  analysis/             # Saved query results (0 pages)
CLAUDE.md               # Schema and workflows
hotcache.md             # This file — read first each session
```

## Key conventions

- Obsidian-style `[[wikilinks]]` for cross-references
- Files named lowercase with hyphens
- Every page has YAML frontmatter (title, type, tags, created, updated, sources)
- LLM owns `wiki/`; never modifies `raw/`
- Operations: ingest, query, lint
