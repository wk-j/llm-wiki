# Hotcache

Last updated: 2026-04-28 (Nattee Niparnan Ep 3 ingest)

## Wiki state

- **53 sources ingested**, **77 concept pages**, **64 entity pages**, **0 analysis pages** (all indexed)
- **All concept and entity pages are now Thai-primary.** Source summaries remain in English, except for Thai-source summaries (like thClaws or Nattee's series) which are in Thai.
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), cassette futurism CSS implementation, game UI taxonomy (diegetic/non-diegetic/spatial/meta), holographic UI (5 variants, rendering, animations, components), LLM knowledge base pattern (meta), LLM coding pitfalls / Karpathy guidelines (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter, Neovim), Soviet Cosmism philosophy (Fedorov, Tsiolkovsky, Vernadsky, noosphere), C# 14 language features (extension members, `field` keyword), idea files / agent-era knowledge sharing, Memex (1945 precursor to LLM wikis), advisor strategy (inverted orchestrator-worker), TUIs and terminal pagers (viewport, $PAGER, Unicode widths, lore/kl/wander), Claude Code session management (context rot, compaction, rewind, subagents), Claude Opus 4.7 announcement (SWE gains, self-verification, 2576px vision, xhigh effort, /ultrareview, auto mode, tokenizer, Project Glasswing), vim.pack / Neovim 0.12 plugin manager (three-function API, lockfile, autocmd hooks, moderate lazy loading), AI + 3D hybrid workflow (Andrew Price — Blender block-in → Flux.1 Depth in ComfyUI → Meshy mesh extraction → Blender staging), Harness Engineering (Panutat Tejasen — human can't review AI framework choices; design orchestration of review/test/audit agents), Nattee Niparnan series on Chula CEDT pedagogy in the LLM era, **Eh Gland (ต่อมเอ๊ะ)**, **Horror Vacui (โรคกลัวที่ว่าง)**, **Shrinking Generalist Moat (เป็ดไม่รอด)**, Harness optimization (Alex Ker), Open Source Governance (Panutat Tejasen), Papercut Features, Agentic Usage, Usage-Based Billing, GitHub AI Credits, DeepSeek Efficiency (Low-cost training, MLA, GRPO, MoE, Open-weight strategy), Sputnik Moment (AI) (Market shift due to DeepSeek's 2025 breakthroughs), Microsoft AI Independence (Mustafa Suleyman, home-grown models, OpenAI partnership restructure).

## Recent activity

- Ingested **วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง Ep. 3** (2026-04-28). Nattee Niparnan explores using AI to close personal gaps (tests, UI/UX) and warns that the generalist ("เป็ด") moat is shrinking as AI handles breadth tasks effortlessly. Introduced the **Eh Gland (ต่อมเอ๊ะ)** as the intuitive judgment required to review AI, and warned of **Horror Vacui (โรคกลัวที่ว่าง)** in design. Updated `nattee-niparnan`, `taste-paradox`, and `engineering-role-shift`.
- Ingested **Microsoft & OpenAI Partnership Restructure** (2026-04-28). Microsoft and OpenAI announced a shift to a non-exclusive "open relationship." OpenAI is now permitted to license models to third-party cloud platforms (Google, Amazon), while Microsoft retains a non-exclusive IP license through 2032. Created source `microsoft-openai-partnership-2026`, entity `microsoft` (Thai-primary), and updated `openai` (Thai-primary).
- Ingested **DeepSeek Wikipedia** (2026-04-27). Comprehensive overview of DeepSeek, the Chinese AI lab that disrupted the industry with high-efficiency models (V3, R1) trained at a fraction of Silicon Valley costs. Introduced technical concepts: `mla-attention`, `grpo`, `mixture-of-experts`, and `open-weight-models`. Added entities: `deepseek`, `high-flyer`, and `liang-wenfeng`. Highlighted the `sputnik-moment-ai` for the industry.

## Directory layout

```
raw/                    # Immutable source documents
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (53 files)
  entities/             # People, orgs, products (64 files)
  concepts/             # Ideas, frameworks, themes (77 files)
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
