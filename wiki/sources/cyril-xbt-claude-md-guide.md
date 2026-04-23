---
title: "How to Build a CLAUDE.md File That Makes Claude Code Actually Listen to You — FULL GUIDE"
type: source
tags: [claude-code, claude-md, prompt-engineering, workflow, x-post]
created: 2026-04-22
updated: 2026-04-22
url: https://x.com/cyrilXBT/status/2046589854776009208
author: "@cyrilXBT"
published: 2026-04-21
sources: []
---

# cyrilXBT — CLAUDE.md Guide

Opinionated X-post walkthrough on how to structure a `CLAUDE.md` file so [[claude-code|Claude Code]] picks up project context automatically. Directional, not authoritative — overlaps with canonical Claude Code docs on mechanics (file locations, session-start loading) but adds a prescriptive 7-section anatomy and example templates. Author frames it as "the single most underrated feature in Claude Code."

## Core claim

One file in the project root, read at the start of every session, acts as a persistent system prompt that travels with the project. Difference framed as "junior dev who needs hand-holding" vs "senior dev who gets it from day one." 20–30 min up-front investment pays back every session after.

## Three file locations

1. **Project root `CLAUDE.md`** — main one, read at session start inside that folder.
2. **Subdirectory `CLAUDE.md`** — for monorepos; Claude reads the relevant one based on working directory.
3. **Global `~/.claude/CLAUDE.md`** — applies to all projects; for personal preferences that never change.

## 7-section anatomy

1. **Project Overview** — 1–2 plain-English paragraphs: what the project is, who the user is, what the priorities are.
2. **Tech Stack** — explicit list: framework, styling, language, database, auth, deployment, package manager, state management, charts, etc.
3. **Coding Conventions** — specific rules: naming (PascalCase/kebab-case), exports (named vs default), function style, type strictness, component size limits, co-location rules.
4. **Never Do This** — hard stops on over-helpful behavior: no unprompted package installs, no unsolicited refactors, no `useEffect` for fetching, no placeholder comments, no inline styles, no `try/catch` wraps without telling user.
5. **File Structure** — annotated directory tree with rules about where things go and what's off-limits.
6. **Current Sprint Goals** — what you're actively building *and* what is explicitly out of scope this sprint.
7. **Important Context** — past decisions already ruled out, rate limits, infra constraints, project history (e.g. "we tried Socket.io, it leaked on Vercel — don't suggest it").

## Global file layer

Once patterns stabilize across projects, put permanent preferences in `~/.claude/CLAUDE.md`:

- language/runtime defaults (TS over JS, pnpm, arrow functions)
- communication rules ("don't start with 'Great question'", "write code first, explain after")
- universal never-list (no placeholder comments, no default exports in React, no `console.log` in deploy code)

Combined with project-level file = two layers of context at all times.

## Non-code use

Same file structure works for writing/content/research projects — Project Overview, Writing Style Rules, What I Never Want, Tone. Author's content-project example: "avoid 'utilize' — use 'use'", "no em dashes", "capitalization is for emotional emphasis, not random."

## Five common mistakes

1. **Too vague** — "write clean code" vs "use named exports, kebab-case, no default exports."
2. **Write once, never update** — evolve the file each sprint as decisions get made.
3. **Goals instead of context** — CLAUDE.md is a briefing doc, not a TODO list. Goals live in the Current Sprint section only; the rest should be stable.
4. **Skipping the NEVER section** — most valuable for experienced devs; you already know what you hate, write it down.
5. **No global file** — rewriting the same preferences across projects is pure waste.

## Composition with slash commands

Next level: `.claude/commands/*.md` — each file becomes a reusable `/command-name`. Example `/new-component`: spec lives in the command file (TS functional, named export, Tailwind, kebab-case, place in `src/components/features/`, ask name+purpose first). CLAUDE.md = project-wide context; slash commands = task-specific workflows.

## Takeaways

- **Structure beats length** — 7 labeled sections is the scaffold; content fills in per project.
- **"Never Do This" is the highest-leverage section** — explicit blocks on over-helpful defaults save the most correction time.
- **Two-layer context is the target state** — global preferences + project briefing, always loaded.
- **File is a living document** — update at end of each sprint with decisions made / approaches ruled out.

## Tensions with existing wiki content

The guide recommends a fairly prescriptive, rule-heavy CLAUDE.md (long "Never Do This" + detailed conventions). This sits in visible tension with [[instruction-budget]] — [[alex-ker|Alex Ker]] argues the file should hold **minimal requirements** and push behavioral detail into skills loaded via [[progressive-disclosure]], citing ETH research that LLM-generated prompts hurt performance and burn ~20% extra inference.

Reconciliation: both authors agree on **human-written, specific, non-vague**. They disagree on **volume**. Cyril optimizes for "Claude never does the annoying thing again" (accept rule-cost for correction-savings). Alex Ker optimizes for staying out of the "dumb zone" (keep CLAUDE.md lean, offload rules to skills).

For frontier models (Opus 4.7) with a few-hundred-rule budget, Cyril's 7-section template typically stays under — but a **long** "Never Do This" list plus detailed conventions can push it over, especially combined with a global file and a project file. See [[claude-md]] for the composed view and [[instruction-budget]] for the attention-cost mechanism.

## See also

- [[claude-md]]
- [[claude-code]]
- [[instruction-budget]]
- [[progressive-disclosure]]
- [[coding-harness]]
- [[alex-ker-harnesses-optimize]]
