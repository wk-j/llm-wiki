# Hotcache

Last updated: 2026-04-14 (Karpathy guidelines ingest)

## Wiki state

- **11 sources ingested**, **20 concept pages**, **10 entity pages**, **0 analysis pages**
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), cassette futurism CSS implementation, game UI taxonomy (diegetic/non-diegetic/spatial/meta), holographic UI (5 variants, rendering techniques, animations, components), LLM knowledge base pattern (meta), LLM coding pitfalls / Karpathy guidelines (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter), Soviet Cosmism philosophy (Fedorov, Tsiolkovsky, Vernadsky, noosphere)

## Recent activity

- Ingested forrestchang/andrej-karpathy-skills — new source (karpathy-guidelines), new concept (llm-coding-pitfalls), new entity (forrestchang), updated andrej-karpathy entity
- Previous: Holographic UI, Soviet Cosmism philosophy, Imetomi/retro-futuristic-ui-design, Four Horsemen of Game UI, Helix 25.07
- Dangling wikilinks: neumorphism, claymorphism, cyberpunk-neon, vaporwave, synthwave, y2k-aesthetic, memphis-design, art-deco, blobmorphism, anti-design, kakoune, brutalist-futurism

## Directory layout

```
raw/                    # Immutable source documents
  UI style categories.md
  LLM Knowledge Bases Thread by @karpathy.md
  Retro futuristic UI design.md
  Retro futuristic UI design 2.md
  Soviet Cosmism UI style.md
  Soviet Cosmism philosophy.md
  Holographic UI.md
  abhigyanpatwariGitNexus...md
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (11 pages)
  entities/             # People, orgs, products (10 pages)
  concepts/             # Ideas, frameworks, themes (20 pages)
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
