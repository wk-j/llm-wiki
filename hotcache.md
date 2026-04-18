# Hotcache

Last updated: 2026-04-18 (concept pages switched to Thai-primary)

## Wiki state

- **20 sources ingested**, **37 concept pages**, **23 entity pages**, **0 analysis pages** (all indexed — prior lint gap closed)
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), cassette futurism CSS implementation, game UI taxonomy (diegetic/non-diegetic/spatial/meta), holographic UI (5 variants, rendering, animations, components), LLM knowledge base pattern (meta), LLM coding pitfalls / Karpathy guidelines (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter, Neovim), Soviet Cosmism philosophy (Fedorov, Tsiolkovsky, Vernadsky, noosphere), C# 14 language features (extension members, `field` keyword), idea files / agent-era knowledge sharing, Memex (1945 precursor to LLM wikis), advisor strategy (inverted orchestrator-worker), TUIs and terminal pagers (viewport, $PAGER, Unicode widths, lore/kl/wander), Claude Code session management (context rot, compaction, rewind, subagents), Claude Opus 4.7 announcement (SWE gains, self-verification, 2576px vision, xhigh effort, /ultrareview, auto mode, tokenizer, Project Glasswing), vim.pack / Neovim 0.12 plugin manager (three-function API, lockfile, autocmd hooks, moderate lazy loading), **AI + 3D hybrid workflow (Andrew Price — Blender block-in → Flux.1 Depth in ComfyUI → Meshy mesh extraction → Blender staging; judgement-vs-automation skill framework; generalizes to engineering-role-shift for software)**

## Recent activity

- **Shifted concept pages to Thai-primary body language.** CLAUDE.md `## Bilingual content` rewritten per-page-type: concepts = Thai body with English technical terms (product names, domain jargon, code identifiers, direct English-source quotes); sources/entities/analysis = English by default. Tooling stays English (filenames, wikilink targets, frontmatter, index.md entries). `wiki/concepts/ai-3d-workflow.md` rewritten as the Thai-primary reference demo. Existing 36 other concept pages NOT yet retrofitted — still English-primary until explicitly converted.
- Prior iteration (superseded): added bilingual "mix is allowed" convention with English-primary default; `ai-3d-workflow.md` was initially English-primary with Thai supplements.
- Ingested Andrew Price X thread "Will AI replace 3D software?" (North American Blender Conference Q&A) — new source (will-ai-replace-3d-software), 4 new entities (andrew-price, blender, comfyui, flux), 2 new concepts (ai-3d-workflow, judgement-vs-automation); updated engineering-role-shift with cross-links; closed index lint gap by indexing software-engineer-role-ai-era, engineering-role-shift, ai-orchestrator, domain-to-ai-translator
- Previous: Evgeni Chasnovski vim.pack guide, Anthropic Claude Opus 4.7 announcement, @trq212 Claude Code session management, Leo Robinovitch terminal pager, Anthropic advisor strategy blog
- Dangling wikilinks: neumorphism, claymorphism, cyberpunk-neon, vaporwave, synthwave, y2k-aesthetic, memphis-design, art-deco, blobmorphism, anti-design, kakoune, brutalist-futurism
- Intentional: Meshy (AI image-to-3D) referenced in prose inside `will-ai-replace-3d-software` and `ai-3d-workflow`; no standalone entity page — narrow tool, one-off mention

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
  A Guide to vim pack.md
  Will AI replace 3D software?.md
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (20 files)
  entities/             # People, orgs, products (23 files)
  concepts/             # Ideas, frameworks, themes (37 files)
  analysis/             # Saved query results (0 pages)
CLAUDE.md               # Schema and workflows
hotcache.md             # This file — read first each session
```

## Key conventions

- Obsidian-style `[[wikilinks]]` for cross-references
- Files named lowercase with hyphens
- Every page has YAML frontmatter (title, type, tags, created, updated, sources)
- LLM owns `wiki/`; never modifies `raw/`
- **Concept pages = Thai-primary body** (English technical terms / tool names / quotes stay English); sources/entities/analysis default to English. Filenames, wikilink targets, frontmatter, index entries stay English. See CLAUDE.md `## Bilingual content` and `ai-3d-workflow.md` demo
- Operations: ingest, query, lint
