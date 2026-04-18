# Hotcache

Last updated: 2026-04-18 (Nattee Niparnan Ep. 1 + Ep. 2 ingest — adds taste-paradox concept)

## Wiki state

- **22 sources ingested**, **39 concept pages**, **25 entity pages**, **0 analysis pages** (all indexed)
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), cassette futurism CSS implementation, game UI taxonomy (diegetic/non-diegetic/spatial/meta), holographic UI (5 variants, rendering, animations, components), LLM knowledge base pattern (meta), LLM coding pitfalls / Karpathy guidelines (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter, Neovim), Soviet Cosmism philosophy (Fedorov, Tsiolkovsky, Vernadsky, noosphere), C# 14 language features (extension members, `field` keyword), idea files / agent-era knowledge sharing, Memex (1945 precursor to LLM wikis), advisor strategy (inverted orchestrator-worker), TUIs and terminal pagers (viewport, $PAGER, Unicode widths, lore/kl/wander), Claude Code session management (context rot, compaction, rewind, subagents), Claude Opus 4.7 announcement (SWE gains, self-verification, 2576px vision, xhigh effort, /ultrareview, auto mode, tokenizer, Project Glasswing), vim.pack / Neovim 0.12 plugin manager (three-function API, lockfile, autocmd hooks, moderate lazy loading), AI + 3D hybrid workflow (Andrew Price — Blender block-in → Flux.1 Depth in ComfyUI → Meshy mesh extraction → Blender staging), Harness Engineering (Panutat Tejasen — human can't review AI framework choices; design orchestration of review/test/audit agents), **Nattee Niparnan series on Chula CEDT pedagogy in the LLM era — LLM-in-grader with −10/click cost, $140 Coding Agent PoC replacing 3–4 RAs, taste paradox (Agent lets you skip practice but practice is what builds judgment to control the Agent), core DS/Algo/Discrete Math theory becomes MORE important, High-level Design Choices pushed down from Senior to junior**

## Recent activity

- Ingested **Nattee Niparnan**'s two-part Thai Facebook series *"วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง"* (Ep. 1 on 2026-04-10, Ep. 2 on ~2026-04-17). Created: source `llm-era-computer-engineering-nattee` (Thai body, combined summary), entity `nattee-niparnan`, Thai-primary concept `taste-paradox` (recursive skill-acquisition loop where Agent lets you skip practice but practice is what builds the judgment needed to control it). Updated 5 existing concept pages: `engineering-role-shift` (core theory more important; design choices forced onto juniors), `harness-engineering` (side-by-side with taste-paradox — complementary at different layers), `judgement-vs-automation` (resource-calculus rotation: framework selection criteria shift from team fluency/speed to Agent stability/token cost), `ai-orchestrator` (downward pressure — orchestration now entry-level), `llm-coding-pitfalls` (authorization war story as concrete multi-pitfall illustration). Explicit Nattee–Panutat dialogue: Panutat = *scope of reviewability* (library choice); Nattee = *origin of the reviewer* (how taste is acquired). Not contradictory — complementary layers of the same problem.
- Prior: Ingested Panutat Tejasen Facebook post (Thai) on **Harness Engineering** — new source `harness-engineering-panutat`, new entity `panutat-tejasen`, new concept `harness-engineering`. First concept page written Thai-primary from scratch under the new convention. Cross-linked into `ai-orchestrator` and `engineering-role-shift`. Key claim: humans can no longer meaningfully "review" or "advise" an AI agent's framework/library choices (knowledge asymmetry) — curriculum should teach orchestration of code-review / test / E2E / security-audit agents instead.
- **Shifted concept pages to Thai-primary body language.** CLAUDE.md `## Bilingual content` rewritten per-page-type: concepts = Thai body with English technical terms (product names, domain jargon, code identifiers, direct English-source quotes); sources/entities/analysis = English by default (sources switch to Thai when source is Thai). Tooling stays English (filenames, wikilink targets, frontmatter, index.md entries). `wiki/concepts/ai-3d-workflow.md` rewritten as the Thai-primary reference demo. Existing 36 other concept pages NOT yet retrofitted — still English-primary until explicitly converted.
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
  Harness Engineering - Panutat Tejasen.md
  LLM Era Computer Engineering - Nattee Niparnan.md
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (22 files)
  entities/             # People, orgs, products (25 files)
  concepts/             # Ideas, frameworks, themes (39 files)
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
