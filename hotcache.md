# Hotcache

Last updated: 2026-04-28 (Mario Zechner pi-agent ingest)

## Wiki state

- **57 sources ingested**, **91 concept pages**, **74 entity pages**, **0 analysis pages** (all indexed)
- **All concept and entity pages are now Thai-primary.** Source summaries remain in English, except for Thai-source summaries (like thClaws or Nattee's series) which are in Thai.
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), cassette futurism CSS implementation, game UI taxonomy (diegetic/non-diegetic/spatial/meta), holographic UI (5 variants, rendering, animations, components), LLM knowledge base pattern (meta), LLM coding pitfalls / Karpathy guidelines (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter, Neovim), Soviet Cosmism philosophy (Fedorov, Tsiolkovsky, Vernadsky, noosphere), C# 14 language features (extension members, `field` keyword), idea files / agent-era knowledge sharing, Memex (1945 precursor to LLM wikis), advisor strategy (inverted orchestrator-worker), TUIs and terminal pagers (viewport, $PAGER, Unicode widths, lore/kl/wander), Claude Code session management (context rot, compaction, rewind, subagents), Claude Opus 4.7 announcement (SWE gains, self-verification, 2576px vision, xhigh effort, /ultrareview, auto mode, tokenizer, Project Glasswing), vim.pack / Neovim 0.12 plugin manager (three-function API, lockfile, autocmd hooks, moderate lazy loading), AI + 3D hybrid workflow (Andrew Price — Blender block-in → Flux.1 Depth in ComfyUI → Meshy mesh extraction → Blender staging), **Harness Engineering** (Panutat Tejasen & Ryan Lopopolo), **Code is Free**, **Token Billionaire**, **Just-in-Time Context**, **Collaborative AI Engineering** (Maggie Appleton), **Alignment Bottleneck**, **ACE**, **BullshitBench** (Peter Gostev), **Dissatisfaction Rate**, **Reasoning Regression**, **pi-agent** (Mario Zechner — minimalist malleable terminal agent), **Malleable Tools**, **Tree-structured Sessions** (branching history), **TerminalBench** (agent evaluation), **Clanker Slop** (AI-generated spam) and human verification (**Vouch**).

## Recent activity

- Ingested **Mario Zechner (Pi) I Hated Every Coding Agent, So I Built My Own** (2026-04-28). Mario Zechner critiques "spaceship" agents like Claude Code and introduces **pi**, a minimalist, extensible terminal agent. Key concepts: **Malleable Tools**, **Tree-structured Sessions**, **TerminalBench**, and **Clanker Slop** (and how to fight it with **Vouch**).
- Ingested **Peter Gostev (Arena.ai) What Models Still Suck At** (2026-04-28). Peter Gostev introduces **BullshitBench**, a benchmark for testing if LLMs can push back on nonsense. He highlights the **Dissatisfaction Rate** from Chatbot Arena (9% overall, higher for experts) and warns of **Reasoning Regression**, where reasoning models (like GPT-5.4) spend excessive tokens justifying false premises rather than rejecting them.
- Ingested **Maggie Appleton (GitHub Next) Collaborative AI Engineering** (2026-04-28). Maggie Appleton argues that "Alignment" is the new bottleneck in software development as implementation becomes cheap. She critiques the "one man, two dozen Claudes" theory and presents **ACE (Agent Collaboration Environment)**, a prototype for multiplayer team-agent collaboration. Key concepts: **Alignment Bottleneck**, **Vibecoded Slop**, and **Team Pulse**.
- Ingested **Ryan Lopopolo (OpenAI) Harness Engineering** (2026-04-28). Ryan Lopopolo presents a Staff Engineer perspective on agent-exclusively workflows. Key concepts: **Code is Free** (abundance of code makes human attention the bottleneck), **Token Billionaire** (high output volume as a productivity strategy), **Just-in-Time Context** (injecting instructions via error messages), and **Durable Feedback Loop** (converting review comments into lints/tests). Created source `ryan-lopopolo-harness-engineering`, entity `ryan-lopopolo`, and updated `harness-engineering` and `openai`.
- Ingested **วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง Ep. 3** (2026-04-28). Nattee Niparnan explores using AI to close personal gaps (tests, UI/UX) and warns that the generalist ("เป็ด") moat is shrinking as AI handles breadth tasks effortlessly. Introduced the **Eh Gland (ต่อมเอ๊ะ)** as the intuitive judgment required to review AI, and warned of **Horror Vacui (โรคกลัวที่ว่าง)** in design. Updated `nattee-niparnan`, `taste-paradox`, and `engineering-role-shift`.

## Directory layout

```
raw/                    # Immutable source documents
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (57 files)
  entities/             # People, orgs, products (74 files)
  concepts/             # Ideas, frameworks, themes (91 files)
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
