# Hotcache

Last updated: 2026-04-12

## Wiki state

- **1 source ingested**, **4 concept pages**, **0 entity pages**, **0 analysis pages**
- Topic so far: UI/UX design styles taxonomy

## Recent activity

- Initialized wiki structure: `raw/`, `wiki/` with subdirs (sources, entities, concepts, analysis)
- Ingested "UI Style Categories" — a clipped Claude conversation cataloging ~40+ UI styles across 11 categories
- Created pages: `ui-style-categories` (source), `diegetic-ui`, `glassmorphism`, `brutalism`, `retro-futurism` (concepts)
- Dangling wikilinks exist for: neumorphism, claymorphism, cyberpunk-neon, vaporwave, synthwave, y2k-aesthetic, memphis-design, art-deco, blobmorphism, anti-design — these will become pages when relevant sources arrive

## Directory layout

```
raw/                    # Immutable source documents
  UI style categories.md
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source
  entities/             # People, orgs, products
  concepts/             # Ideas, frameworks, themes
  analysis/             # Saved query results
CLAUDE.md               # Schema and workflows
hotcache.md             # This file — read first each session
```

## Key conventions

- Obsidian-style `[[wikilinks]]` for cross-references
- Files named lowercase with hyphens
- Every page has YAML frontmatter (title, type, tags, created, updated, sources)
- LLM owns `wiki/`; never modifies `raw/`
- Operations: ingest, query, lint
