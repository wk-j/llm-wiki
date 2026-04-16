# Hotcache

Last updated: 2026-04-16 (Claude Opus 4.7 announcement ingest)

## Wiki state

- **18 sources ingested**, **30 concept pages**, **17 entity pages**, **0 analysis pages** (index-tracked)
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), cassette futurism CSS implementation, game UI taxonomy (diegetic/non-diegetic/spatial/meta), holographic UI (5 variants, rendering techniques, animations, components), LLM knowledge base pattern (meta), LLM coding pitfalls / Karpathy guidelines (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter), Soviet Cosmism philosophy (Fedorov, Tsiolkovsky, Vernadsky, noosphere), C# 14 language features (extension members, `field` keyword), idea files / agent-era knowledge sharing, Memex (1945 precursor to LLM wikis), advisor strategy (inverted orchestrator-worker), TUIs and terminal pagers (viewport architecture, $PAGER, Unicode terminal widths, lore/kl/wander), Claude Code session management (context rot, compaction, rewind, subagents), **Claude Opus 4.7 announcement** (SWE gains, self-verification, 2576px vision, xhigh effort, /ultrareview, auto mode, tokenizer change 1.0–1.35×, Project Glasswing cyber posture)

## Recent activity

- Ingested Anthropic blog "Introducing Claude Opus 4.7" — new source (claude-opus-4-7-announcement), 4 new entities (anthropic, claude, claude-opus-4-7, claude-code), 1 new concept (effort-levels); cross-linked into advisor-strategy, claude-code-session-management, context-rot, compaction
- Previous: @trq212 Claude Code session management, Leo Robinovitch terminal pager, Anthropic advisor strategy blog, Karpathy LLM Wiki idea file, C# 14
- Dangling wikilinks: neumorphism, claymorphism, cyberpunk-neon, vaporwave, synthwave, y2k-aesthetic, memphis-design, art-deco, blobmorphism, anti-design, kakoune, brutalist-futurism
- Lint gap: `ai-orchestrator`, `engineering-role-shift`, `domain-to-ai-translator`, and source `software-engineer-role-ai-era` exist as files but are not listed in `wiki/index.md` (carried over from prior ingest)

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
  The advisor strategy...md
  I Made a Terminal Pager...md
  Using Claude Code Session Management & 1M Context.md
  Introducing Claude Opus 4.7.md
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (18 files)
  entities/             # People, orgs, products (17 files)
  concepts/             # Ideas, frameworks, themes (33 files)
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
