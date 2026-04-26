# Hotcache

Last updated: 2026-04-25 (Guillermo Rauch talk ingest)

## Wiki state

- **42 sources ingested**, **61 concept pages**, **49 entity pages**, **0 analysis pages** (all indexed)
- **All concept and entity pages are now Thai-primary.** Source summaries remain in English.
- Topics: UI/UX design styles, retro-futurism design system (5 subgenres), cassette futurism CSS implementation, game UI taxonomy (diegetic/non-diegetic/spatial/meta), holographic UI (5 variants, rendering, animations, components), LLM knowledge base pattern (meta), LLM coding pitfalls / Karpathy guidelines (meta), code intelligence / knowledge graphs, text editors / parsing (Helix, tree-sitter, Neovim), Soviet Cosmism philosophy (Fedorov, Tsiolkovsky, Vernadsky, noosphere), C# 14 language features (extension members, `field` keyword), idea files / agent-era knowledge sharing, Memex (1945 precursor to LLM wikis), advisor strategy (inverted orchestrator-worker), TUIs and terminal pagers (viewport, $PAGER, Unicode widths, lore/kl/wander), Claude Code session management (context rot, compaction, rewind, subagents), Claude Opus 4.7 announcement (SWE gains, self-verification, 2576px vision, xhigh effort, /ultrareview, auto mode, tokenizer, Project Glasswing), vim.pack / Neovim 0.12 plugin manager (three-function API, lockfile, autocmd hooks, moderate lazy loading), AI + 3D hybrid workflow (Andrew Price — Blender block-in → Flux.1 Depth in ComfyUI → Meshy mesh extraction → Blender staging), Harness Engineering (Panutat Tejasen — human can't review AI framework choices; design orchestration of review/test/audit agents), Nattee Niparnan series on Chula CEDT pedagogy in the LLM era (LLM-in-grader with −10/click cost, $140 Coding Agent PoC replacing 3–4 RAs, taste paradox, core DS/Algo/Discrete Math theory becomes MORE important, High-level Design Choices pushed down from Senior to junior), Harness optimization (Alex Ker) — harness as scaffolding tool (Claude Code, Codex, OpenCode, Cursor); instruction budget "dumb zone" past ~few-hundred instructions; progressive disclosure for CLIs / Skills / MCP (Claude Code tool-search 85% context reduction); R.P.I. prompt framework; subagent patterns (parallel fan-out vs sequential pipeline — pipeline = Panutat's review-agent harness as Alex Ker's coding-harness); **RTK (RTK-AI) — Rust CLI proxy for token optimization; Generative UI / Ephemeral Apps (Guillermo Rauch) — on-demand interface generation; apps as disposable single-purpose tools; LLMs as customers; "Pit of Success" via frameworks (Next.js).**
- **Claude Mythos Preview / Project Glasswing** — Anthropic's most capable model; autonomously finds and exploits zero-day vulnerabilities in every major OS and browser; cyber capabilities emerged without explicit security training; thousands of high/critical vulns found (89% severity agreement with humans, zero false positives on memory corruption); deliberately not made generally available; Project Glasswing distributes access to vetted critical partners; key finding: offensive cyber capability is inevitable side effect of general model improvement, not something you train for; validates [[agent-runtime-untrusted]] (APTS) at full scale

## Recent activity

- Ingested **Building the Generative Web with AI ft Vercel CEO Guillermo Rauch** (2026-04-25). Talk on generative UI, ephemeral apps, and the shift to on-demand software. Vercel now optimizes for AI agents as primary "customers." New source `rauch-generative-web`, new entities `guillermo-rauch`, `vercel`, `v0-dev`, new Thai-primary concepts `generative-ui`, `ephemeral-apps`.
- Ingested **RTK-AI GitHub repository** (2026-04-25). High-performance CLI proxy in Rust for token consumption reduction (60-90%). Strategies: filtering, grouping, truncation, deduplication. Features: `rtk gain` (analytics), `rtk smart` (heuristics), `rtk read` (stripped bodies), Tee Recovery. Complements Claude Code, Cursor, OpenCode. New source `rtk-github`, new entity `rtk`, new Thai-primary concept `token-optimization` (folding in Alex Ker and Claude 4.7 strategies).
- Ingested **Piyalitt Ittichaiwong Thai FB post on GPT-5.5 launch** (2026-04-24). Thai PhD researcher + 20yr programmer with early access. Two layers: (1) subjective — "first model I can't compete with"; near-Mythos Preview capability but broadly accessible; flags SWE-Bench Pro memorization flag (Anthropic card too; he thinks unintentional mistake not benchmaxx); "ไม่ต้องพูดถึง Opus 4.7 เลยครับ"; (2) OpenAI launch summary — Terminal-Bench 2.0 82.7% SOTA, SWE-Bench Pro 58.6% (memorization ⚠️), GDPval 84.9%, OSWorld 78.7%, Tau2 Telecom 98%, BixBench 80.5%, CyberGym 81.8% vs Opus 4.7 73.1%; OpenAI internal: 85%+ weekly Codex use; Codex wrote traffic splitter that gave >20% token-gen speedup (model improving its own infra); new Ramsey-number proof (Lean-verified); pricing: $5/$30 per 1M (Pro $30/$180), 1M ctx, 400K in Codex; Fast mode +1.5× speed / 2.5× price; **2× price of GPT-5.4, slightly > Opus 4.7 — pricing inversion** (historically ~½ Opus). 3 new entities (`piyalitt-ittichaiwong`, `openai`, `gpt-5-5`), 1 new source (`piyalitt-gpt-5-5-launch`). Updated `claude-opus-4-7` (competition section w/ senior-engineer testimonial on reasoning/autonomy edge) and `openai-codex` (linked to openai parent + internal-usage section). No new concept — competitive-model datapoint folded into existing entity pages. Two cross-cutting implications for the wiki: (a) SWE-Bench Pro is now flagged on two 2026 launches (Kimi K2.6 curated table + GPT-5.5 memorization sign) — treat as weak ranking axis; (b) pricing inversion at flagship tier signals OpenAI paying real compute cost to reach Mythos-class mass-market capability.
- Ingested **Aaron Levie X post on agent-automation jobs** (2026-04-24). Box CEO arguing the chatbot→production-agent transition needs *dedicated headcount*, not side projects. 8-item job spec: map workflows / deploy / keep context fresh / wire internal systems / build evals / HITL design / manage upgrades / change management. Lives in IT or eng or business function — title varies by company. Levie frames it as "future of software engineering in non-tech companies." New source `aaron-levie-agent-automation-jobs`, new entity `aaron-levie`, new Thai-primary concept `agent-enablement-role` (with relationship table to ai-orchestrator / domain-to-ai-translator / harness-engineering / long-running-agents — Levie's enterprise-deployer angle complements builder/practitioner concepts already in wiki). Updated `engineering-role-shift` to add agent-enablement-role to its "บทบาทใหม่" list. Distinguishes from "AI Engineer" by including change management — closer to AI-era Solutions Engineer than ML Engineer.
- Ingested **"Stop Slop" by Hardik Pandya** (GitHub, 2026-04-23). A "skill" for LLMs to remove AI writing patterns ("tells") from prose. It provides rules and examples to make writing more direct, active, and human-like. New source `stop-slop-source`, new entity `hardik-pandya`, new Thai-primary concept `stop-slop-concept`.

## Directory layout

```
raw/                    # Immutable source documents
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (39 files)
  entities/             # People, orgs, products (43 files)
  concepts/             # Ideas, frameworks, themes (58 files)
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
