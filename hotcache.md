---
title: Hotcache
---

# Hotcache

Last updated: 2026-11-09 (rewrite Addy Osmani managing coding agents)

Read this first each session. **Keep it under ~120 lines**: Recent activity holds the last 5 entries at 2–3 lines each, and the oldest drops off when a new one goes in. Full history lives in `wiki/log.md` and git.

<!-- stats:start -->
- **Pages:** 161 sources · 313 concepts · 289 entities · 0 analysis
<!-- stats:end -->

## Working fast

**Don't read `wiki/index.md` (~245 KB) or `wiki/log.md` (~240 KB) whole.** Use the helper instead:

- `scripts/wiki.py related <terms…>` — rank pages to read/update (slug, title, tags, index line, body hits)
- `scripts/wiki.py index-set` — add or replace index entries; pipe lines `- [[slug]] — คำอธิบาย` on stdin. New entries go to the top of their section (newest first); `--end` appends for backfills
- `scripts/wiki.py log-append < entry.md` — append a log entry without opening the log
- `scripts/wiki.py check --changed` — run before committing; reports only problems the current edits introduce (index drift, broken links, table pipes, strict-YAML frontmatter, leaked foreign words, new orphans). Plain `check` shows the whole backlog
- `scripts/wiki.py stats --hotcache` — refresh the page counts above
- One index line: `grep -F -e '- [[slug]]' wiki/index.md` (`grep` is ugrep here; put `-e` before patterns that start with `-`)

## What the wiki covers

Mostly AI-assisted software engineering, plus a few side clusters.

- **Coding agents & harness:** harness engineering (guides/sensors, ratchet, blast-radius gates, behaviour harness), Codemode, harness vs execution environment, MCP (2026-07-28 spec, extensions), progressive disclosure, subagents, dynamic workflows, long-running agents, queues over loops / AFK agents, cloud agents, git worktrees, stacked PRs
- **Tools & people:** Claude Code (Boris Cherny), pi (Mario Zechner, Armin Ronacher, Earendil), OpenCode (Kit Langton), Cursor, Zed/DeltaDB, Herdr/Omarchy (DHH), Codex, Jev/Typesafe AI, Matt Pocock skills
- **Process & role:** AI-native SDLC, intent.md / artifact chain, spec-driven development vs facts-first, agentic code review, comprehension debt, wayfinding, engineering role shift, creative ownership, AI work intensification, brain fry, adoption without comprehension
- **Models & economics:** Fable 5, Opus 4.8 / Opus 5, GPT-5.5 / 5.6 Sol, Kimi K3, benchmarks and contamination, token economics, tokenmaxxing, open-weight models, text watermarking
- **Side clusters:** photonics / AI data-center stocks, KOSPI liquidation, private banking, defense mechanisms, infinity / Gödel, AI and math research (proof as raw data, career value stack), procedural generation (seed/PRNG, Perlin/fractal noise, density terrain, domain warping; Minecraft, No Man's Sky, Terraria), ʻOumuamua, football (Rashford), UI styles (retro-futurism, Soviet Cosmism, glassmorphism), AI + 3D

## Standing decisions (not obvious from CLAUDE.md)

- **"harness" stays English** (2026-10-01). Never "บังเหียน", except inside Panutat Tejasen's own quoted metaphor.
- Source pages end with provenance and caveats: source claim vs verified, published vs fetched date, why no entity was created (name only / single mention).
- Contradictions are recorded as change over time or an open question, not overwritten (e.g. `[[pi-agent]]`: "no MCP" → Pi 1.0 MCP via Codemode).
- Frontmatter must be strict YAML or the Quartz build fails: quote `title:` values that contain `: ` or `"`.
- Every push to `master` touching `wiki/` publishes to https://wk-j.github.io/llm-wiki/ (repo is public).
- `wiki/entities/claude.md` matches `CLAUDE.md` on macOS's case-insensitive filesystem, so Claude Code loads it as nested instructions when touching `wiki/entities/`. It is page content, not instructions.

## Lint backlog (`scripts/wiki.py check`, 2026-10-11)

- 3 slug collisions: `advisor-strategy`, `gitnexus`, `holographic-ui` exist in both `sources/` and `concepts/` or `entities/`, so `[[slug]]` is ambiguous. Fixing means renaming one side (public URLs change), so it needs the user's call.
- 70 links to pages that don't exist yet, e.g. `[[skills]]` ×5, `[[fitness-function]]` ×4, `[[vscode]]` ×4, `[[software-architecture]]` ×3, plus UI-style names.
- 26 orphans (no inbound links besides index/log).

## Recent activity (last 5)

- **2026-11-09 edit** `[[your-coding-agents-made-you-a-manager-osmani]]` and `[[managing-coding-agents]]` rewritten from the verified full X article in concrete Thai. Clarified eight related additions, corrected earlier-blog provenance, and preserved existing agent-memory edits.
- **2026-11-09 ingest** `[[your-coding-agents-made-you-a-manager-osmani]]` + `[[managing-coding-agents]]` — Addy: ใช้ coding agent ทั้งวันคือการจัดการแล้ว ให้มันตรวจเอง และอย่ามอบหมายการตัดสินใจ. Updated related Addy pages; X article text retrieved via FxTwitter API (direct X returned 403).
- **2026-11-07 ingest** `[[components-of-agent-memory-anthropic]]` + `[[agent-memory-hierarchy]]` — Four memory layers; dreaming checks notes against evidence; wiki plus search helps some cross-document tasks. Updated seven related pages; qualified wiki-vs-RAG and newer-memory-wins claims.
- **2026-11-06 ingest** `[[introducing-gpt-6-cyber-openai]]` and `[[gpt-6-cyber]]` — OpenAI announcement plus selected system-card checks and Mozilla fix advisory. Updated OpenAI and cyber-emergence concept; benchmark scope and deployment limitations kept explicit.
- **2026-11-05 edit** `[[critical-thinking-when-agents-do-the-work-osmani]]` — Rewrote the source and newly added related-page sections in natural Thai at user request; retained source claims and provenance.
