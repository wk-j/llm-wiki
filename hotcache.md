# Hotcache

Last updated: 2026-04-27 (GitHub Copilot Usage-Based Billing ingest)

## Wiki state

- **45 sources ingested**, **67 concept pages**, **52 entity pages**, **0 analysis pages** (all indexed)
- **All concept and entity pages are now Thai-primary.** Source summaries remain in English, except for Thai-source summaries (like thClaws) which are in Thai.
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), cassette futurism CSS implementation, game UI taxonomy (diegetic/non-diegetic/spatial/meta), holographic UI (5 variants, rendering, animations, components), LLM knowledge base pattern (meta), LLM coding pitfalls / Karpathy guidelines (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter, Neovim), Soviet Cosmism philosophy (Fedorov, Tsiolkovsky, Vernadsky, noosphere), C# 14 language features (extension members, `field` keyword), idea files / agent-era knowledge sharing, Memex (1945 precursor to LLM wikis), advisor strategy (inverted orchestrator-worker), TUIs and terminal pagers (viewport, $PAGER, Unicode widths, lore/kl/wander), Claude Code session management (context rot, compaction, rewind, subagents), Claude Opus 4.7 announcement (SWE gains, self-verification, 2576px vision, xhigh effort, /ultrareview, auto mode, tokenizer, Project Glasswing), vim.pack / Neovim 0.12 plugin manager (three-function API, lockfile, autocmd hooks, moderate lazy loading), AI + 3D hybrid workflow (Andrew Price — Blender block-in → Flux.1 Depth in ComfyUI → Meshy mesh extraction → Blender staging), Harness Engineering (Panutat Tejasen — human can't review AI framework choices; design orchestration of review/test/audit agents), Nattee Niparnan series on Chula CEDT pedagogy in the LLM era, Harness optimization (Alex Ker), Open Source Governance (Panutat Tejasen), Papercut Features, **Agentic Usage** (The shift from autocomplete to multi-step repository-wide sessions), **Usage-Based Billing** (Consumption-based pricing for AI), **GitHub AI Credits** (GitHub's token-based currency).
- **Claude Mythos Preview / Project Glasswing** — Anthropic's most capable model; autonomously finds and exploits zero-day vulnerabilities in every major OS and browser; cyber capabilities emerged without explicit security training; thousands of high/critical vulns found (89% severity agreement with humans, zero false positives on memory corruption); deliberately not made generally available; Project Glasswing distributes access to vetted critical partners; key finding: offensive cyber capability is inevitable side effect of general model improvement, not something you train for; validates [[agent-runtime-untrusted]] (APTS) at full scale

## Recent activity

- Ingested **GitHub Copilot Usage-Based Billing Update** (2026-04-27). GitHub announcement regarding the move to usage-based billing starting June 1, 2026. Transitioning from PRUs to **GitHub AI Credits** driven by the compute demands of **Agentic Usage** (multi-step repo-wide sessions). Code completions remain unlimited, while agentic features draw from a monthly credit allotment. Created source `github-copilot-billing-update`, entities `github`, `github-copilot`, and Thai-primary concepts `agentic-usage`, `usage-based-billing`, `github-ai-credits`.
- Ingested **thClaws Positioning by Panutat Tejasen** (2026-04-27). Thai post on the importance of Governance in Open Source. Positioned thClaws as a community-driven project that responds to niche user needs faster than cloud-first products. Introduced concepts: `open-source-governance` (Thai-primary) and `papercut-features` (Thai-primary). Updated `thclaws` and `panutat-tejasen`.
- Ingested **thClaws Announcement by Panutat Tejasen** (2026-04-26). Thai post on the shift from LLM Wrappers to Harness Engineering. Announced thClaws, an open-source Rust port of Claude Code's core logic. Introduced "Product Overhang". New source `thclaws-announcement-panutat` (Thai), new entity `thclaws`, new Thai-primary concept `product-overhang`. Updated `panutat-tejasen` and `harness-engineering`.

## Directory layout

```
raw/                    # Immutable source documents
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (45 files)
  entities/             # People, orgs, products (52 files)
  concepts/             # Ideas, frameworks, themes (67 files)
  analysis/             # Saved query results (0 pages)
CLAUDE.md               # Schema and workflows
hotcache.md             # This file — read first each session
```

## Key conventions

- Obsidian-style `[[wikilinks]]` for cross-references
- Files named lowercase with hyphens
- Every page has YAML frontmatter (title, type, tags, created, updated, sources)
- LLM owns `wiki/`; never modifies `raw/`
- **All concept and entity pages are now Thai-primary.** Source summaries remain in English. Filenames, wikilink targets, frontmatter, index entries stay English. See CLAUDE.md `## Bilingual content`.
- Operations: ingest, query, lint
