# Hotcache

Last updated: 2026-04-14

## Wiki state

- **7 sources ingested**, **17 concept pages**, **4 entity pages**, **0 analysis pages**
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), game UI taxonomy (diegetic/non-diegetic/spatial/meta), LLM knowledge base pattern (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter)

## Recent activity

- Ingested "Four Horsemen of Game UI Design" — created source summary, 3 new concept pages (non-diegetic, spatial, meta UI), updated diegetic-ui
- Previous: Helix 25.07, Soviet Cosmism UI style, GitNexus
- Dangling wikilinks: neumorphism, claymorphism, cyberpunk-neon, vaporwave, synthwave, y2k-aesthetic, memphis-design, art-deco, blobmorphism, anti-design, kakoune

## Directory layout

```
raw/                    # Immutable source documents
  UI style categories.md
  LLM Knowledge Bases Thread by @karpathy.md
  Retro futuristic UI design.md
  Retro futuristic UI design 2.md
  Soviet Cosmism UI style.md
  abhigyanpatwariGitNexus...md
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (6 pages)
  entities/             # People, orgs, products (4 pages)
  concepts/             # Ideas, frameworks, themes (14 pages)
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
