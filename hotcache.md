# Hotcache

Last updated: 2026-05-23 (Software Writing Software ingest)

## Wiki state

- **82 sources ingested**, **148 concept pages**, **116 entity pages**, **0 analysis pages** (all indexed)
- **All source, concept, entity, and analysis pages are Thai-primary.** Keep English for technical terms, proper nouns, filenames, tags, and direct quotes.
- Topics: **Just-in-Time Software**, **Personalized Development Environment**, **luai.nvim**, **Agent Handoff Documents**, **Throwaway Prototyping**, **Dual-Axis Code Review**, **Writing Fragments**, **Agent Harness Engineering**, **Harness Ratchet**, **Harness-as-a-Service**, **Coding Harness**, **Harness Engineering**, **HTML Artifacts**, **Custom Editing Interfaces**, **Throwaway Editors**, **Software Fundamentals**, **Software Entropy**, **Specs-to-Code**, **Grill Me**, **Ubiquitous Language**, **Deep Modules**, **Granite Speech**, **Automatic Speech Recognition**, **Non-Autoregressive ASR**, **Keyword Biasing**, **Speaker-Attributed ASR**, **Word Error Rate**, **Dreaming**, **Agent Memory as File System**, **Self-Learning Agents**, **Claude Managed Agents**, **Monkey Paw Balancing**, **Live Service Stagnation**, **Endgame Stagnation**, **Helldivers 2 Review Crisis**, **Cognitive Debt**, **Skill Atrophy**, **Vendor Lock-In**, **Care Allocation**, **Agentic Engineering**, **Software 3.0**, **Jagged Intelligence**, **Vibe Coding**, **Verifiability**, **Agent-Native Infrastructure**, **The Harness is the Backend**, **WTF Primitives**, **iii (Triple I)**, **thClaws Marketplace**, **Rabbit Hole**, **Host Bridge**, **Enterprise AI Security**, **Agent Dashboards**, **Playback Pattern**, **Grounding**, **Cheaper to Correct**, **Mercury Agent Memory**, **Memory Drift**, **Selective Injection**, **Memory Scoring**, **Memory Decay**, **Hybrid Memory Architecture**, UI/UX design styles, **Impeccable**, **AI Slop**, **Text Slop**, **Theory of Constraints**, **Local Optimization Trap**, **Lead Time**, **Malleable Tools**, **Tree-structured Sessions**, **TerminalBench**, **Hidden Context**, **Clanker Slop**, **Vibecoded Slop**, **Alignment Bottleneck**, **ACE**, **BullshitBench**, **Reasoning Regression**, **Code is Free**, **Token Billionaire**, **Just-in-Time Context**, **Eh Gland**, **Horror Vacui**, **Advisor Strategy**, **Claude Code Session Management**, **Holographic UI**, **Soviet Cosmism**, **Cassette Futurism**, **AI + 3D Workflow**, **Agentic Search**, **Semantic Retrieval**, **AST-Based Chunking**, **Merkle Tree-based Sync**, **Milvus**, **Zilliz**.

## Recent activity

- Ingested **"Software Writing Software (gone right!)" — TJ DeVries** (2026-05-23). Created `[[software-writing-software-gone-right]]`, `[[personalized-development-environment]]`, `[[just-in-time-software]]`, `[[tj-devries]]`, and `[[luaai-nvim]]`. Key point: `luai.nvim` makes AI generate missing Lua functions inside Neovim, saves them as modules, and reuses/improves them later — a micro-scale example of malleable tools and personal software.
- Ingested **"New Skills! /handoff, /prototype, /review and /writing-* | Skills Changelog" — Matt Pocock** (2026-05-12). Created `[[new-skills-handoff-prototype-review-writing]]`, `[[agent-handoff-documents]]`, `[[throwaway-prototyping]]`, `[[dual-axis-code-review]]`, and `[[writing-fragments]]`. Key point: Pocock is turning agent work into phase routing — handoff to fresh context, prototype to resolve unknowns with artifacts, review along standards/spec axes, and write from human fragments before shaping prose.
- Ingested **"Agent Harness Engineering" — Addy Osmani** (2026-05-10). Created `[[agent-harness-engineering]]`, `[[harness-ratchet]]`, and entities for `[[addy-osmani]]`, `[[vtrivedy]]`, `[[fred-schott]]`, `[[flue]]`. Key point: **Agent = Model + Harness**; every real agent failure should become a durable harness constraint (rule, hook, lint/test gate, reviewer agent), while obsolete scaffolding should be pruned as models improve.
- Ingested **"Using Claude Code: The Unreasonable Effectiveness of HTML" — Thariq S.** (2026-05-09). Post by a Claude Code engineer advocating for HTML as a high-signal communication medium. Key concepts: [[html-artifacts]] (richer information density via SVG/JS), [[custom-editing-interfaces]] (throwaway editors with export buttons), and maintaining human-in-the-loop for complex plans and code reviews.
- Ingested **"Software Fundamentals Matter More Than Ever" — Matt Pocock** (2026-05-09). Talk arguing that AI coding tools are tactical sergeants requiring strategic guidance from humans grounded in software fundamentals. Key concepts: [[grill-me]] (alignment), [[ubiquitous-language]] (shared vocabulary), [[deep-modules]] (abstraction for delegation), [[software-entropy]] (the risk of specs-to-code), and [[specs-to-code]] trap.
- Ingested **Granite 4.1 - The Fastest ASR?** (2026-05-09). Video by [[sam-witteveen|Sam Witteveen]] explaining [[granite-speech|Granite Speech]] 4.1 from [[ibm|IBM]] as three 2B ASR variants.
- Ingested **Memory and dreaming for self-learning agents** (2026-05-09). Anthropic talk by Mahes (Platform PM) launching [[dreaming]] in research preview alongside [[agent-memory-filesystem|memory-as-filesystem]] in [[claude-managed-agents|Claude Managed Agents API]].
- Ingested **Helldivers 2 Just Fell to “Mostly Negative” Reviews** (2026-05-08). Video by SwanyPlaysGames reporting on the 2026 review crisis for [[helldivers-2]].

## Directory layout

```
raw/                    # Immutable source documents
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (82 files)
  entities/             # People, orgs, products (116 files)
  concepts/             # Ideas, frameworks, themes (148 files)
  analysis/             # Saved query results (0 pages)
CLAUDE.md               # Schema and workflows
hotcache.md             # This file — read first each session
```
