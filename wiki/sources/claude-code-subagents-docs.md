---
title: "Claude Code Docs: Create custom subagents"
type: source
tags: [ai, claude-code, agents, subagents, harness, documentation]
created: 2026-04-18
updated: 2026-04-18
sources: [Create custom subagents - Claude Code Docs.md]
---

# Claude Code Docs: Create custom subagents

**Source:** Anthropic / Claude Code official documentation
**URL:** https://code.claude.com/docs/en/sub-agents.md

Canonical reference for [[claude-code|Claude Code]]'s subagent system. Extends prior coverage in [[claude-code-session-management]] (subagents as one of five session-management options) and [[alex-ker-harnesses-optimize]] (subagent design patterns) with the concrete mechanics: file format, scopes, tool restrictions, memory, hooks, invocation, foreground/background, resumption.

## Summary

A **subagent** is a specialized assistant that runs in its own context window with its own system prompt, tool allowlist, and permission mode. When the parent conversation delegates, the subagent does the work off-screen and returns only a summary. This preserves context, enforces tool constraints, enables reuse, specializes behavior, and lets cheaper models (Haiku) handle expensive sub-tasks.

Key constraint up front: **subagents cannot spawn other subagents.** For nested delegation use [[skills|Skills]] or chain subagents from the main thread. For parallel workers with their own sessions, see `agent teams` (separate feature).

## Built-in subagents

| Name | Model | Tools | Purpose |
|---|---|---|---|
| **Explore** | Haiku | Read-only (no Write/Edit) | File discovery, code search; caller specifies `quick`/`medium`/`very thorough` |
| **Plan** | Inherits | Read-only | Research during plan mode; prevents infinite nesting |
| **general-purpose** | Inherits | All tools | Complex multi-step research + modification |
| **statusline-setup** | Sonnet | — | Auto-invoked by `/statusline` |
| **Claude Code Guide** | Haiku | — | Auto-invoked on Claude Code feature questions |

All inherit the parent's permissions plus their own tool restrictions.

## File format

Markdown + YAML frontmatter. Only `name` and `description` are required.

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

### Frontmatter fields

| Field | Purpose |
|---|---|
| `name` | Lowercase-hyphen unique identifier |
| `description` | The field Claude uses to decide when to delegate — write it for the router, not for humans |
| `tools` | Allowlist of [tools](https://code.claude.com/docs/en/tools-reference); inherits all if omitted |
| `disallowedTools` | Denylist; applied before `tools` resolution if both set |
| `model` | `sonnet` / `opus` / `haiku` / full ID (e.g. `claude-opus-4-7`) / `inherit` (default) |
| `permissionMode` | `default` / `acceptEdits` / `auto` / `dontAsk` / `bypassPermissions` / `plan` — but parent `bypassPermissions` / `acceptEdits` / `auto` override child |
| `maxTurns` | Hard stop on agentic turns |
| `skills` | List of [[skills\|Skills]] to **inject fully** at startup (not inherited from parent) |
| `mcpServers` | Inline MCP definitions or named references to session-level servers |
| `hooks` | Lifecycle hooks scoped to this subagent (plugin subagents cannot use this, nor `mcpServers`/`permissionMode`) |
| `memory` | `user` / `project` / `local` — enables persistent directory across conversations |
| `background` | `true` = always run concurrently (default foreground) |
| `effort` | Override session [[effort-levels]]: `low`/`medium`/`high`/`xhigh`/`max` |
| `isolation` | `worktree` — give the subagent a temporary git worktree; auto-cleaned if no changes |
| `color` | Display color in task list |
| `initialPrompt` | Auto-submitted first turn when the agent runs as *main session* via `--agent` |

Subagents receive only their own system prompt plus basic environment details — **not** the main Claude Code system prompt.

## Scope and priority

When multiple subagents share a name, the higher-priority definition wins:

| Priority | Location | Scope |
|---|---|---|
| 1 (highest) | Managed settings `.claude/agents/` | Organization-wide |
| 2 | `--agents` CLI JSON | Current session only, ephemeral |
| 3 | `.claude/agents/` | Project (check into version control) |
| 4 | `~/.claude/agents/` | All your projects |
| 5 (lowest) | Plugin `agents/` | Where the plugin is enabled |

`--add-dir` directories are **not** scanned for subagents (they grant file access only).

## Tool restrictions

Three levers: `tools` (allowlist), `disallowedTools` (denylist), and `permissions.deny` in settings with `Agent(subagent-name)` form to block whole subagent types.

`Agent(agent_type)` inside `tools` restricts which subagents a **main-thread agent** (started with `claude --agent`) can spawn. `Agent` alone = any. Omitting `Agent` = cannot spawn. Has no effect in normal subagent definitions (since subagents can't spawn subagents).

Renamed note: in v2.1.63 `Task` became `Agent`; `Task(...)` still works as alias.

## Persistent memory

`memory: user | project | local` gives the subagent a directory that survives across conversations — an explicit, scoped version of the pattern this wiki uses.

| Scope | Location |
|---|---|
| `user` | `~/.claude/agent-memory/<name>/` |
| `project` | `.claude/agent-memory/<name>/` (checked in) |
| `local` | `.claude/agent-memory-local/<name>/` (not checked in) |

When enabled, the subagent's system prompt auto-includes the first 200 lines or 25 KB of `MEMORY.md` (whichever comes first) plus curation instructions, and Read/Write/Edit are auto-enabled.

Recommended default: `project`. The pattern echoes this repo's own `MEMORY.md` + per-memory file convention at `/Users/wk/.claude/projects/-Users-wk-Source-second-brain/memory/`.

## Hooks

Two placements:

1. **Frontmatter hooks** — fire only while that subagent is active; cleaned up on finish. Fire on Agent-tool spawn or @-mention; **not** when the agent runs as main session via `--agent`.
2. **`settings.json` hooks** — `SubagentStart` / `SubagentStop` fire in the main session around subagent lifecycle (with optional `matcher` for agent type name). Frontmatter `Stop` is auto-converted to `SubagentStop` at runtime.

Primary use: `PreToolUse` hook to block disallowed command variants (e.g. only allow `SELECT`), using exit code 2 to feed a refusal back to the subagent.

## Invocation

Three escalating patterns:

- **Natural language** — name the subagent; Claude decides. "Use proactively" in the description encourages auto-delegation.
- **@-mention** — `@"code-reviewer (agent)"` or `@agent-<name>` guarantees that one task runs on that subagent. Plugin form: `@agent-<plugin>:<name>`.
- **`--agent <name>`** — the whole session's main thread takes that subagent's system prompt, tool restrictions, and model. Replaces the default Claude Code system prompt entirely (CLAUDE.md and project memory still load). Persists across resume. Can also be set in `.claude/settings.json`: `{"agent": "code-reviewer"}`.

## Foreground vs background

- **Foreground** — blocks main conversation; permission prompts and `AskUserQuestion` pass through.
- **Background** — runs concurrently; tool permissions must be pre-approved before launch, and any unapproved tool call auto-denies at runtime. If a background subagent needs to ask a clarifying question, that tool call fails but the subagent continues.

Claude picks based on the task; user can ask "run this in the background" or press **Ctrl+B** to background a running task. Disable entirely with `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.

## Resumption

Each invocation creates a fresh instance by default. To continue an earlier subagent's work, ask Claude to resume — it uses `SendMessage` with the stored agent ID (requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). Resumed subagents keep their full prior transcript, tool calls, and reasoning.

Subagent transcripts are stored separately at `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl` and **are unaffected by main-conversation compaction**. Subagents support their own auto-compaction at ~95% capacity (tune with `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`). Cleanup: `cleanupPeriodDays` (default 30).

## Best-practice checklist (verbatim spirit)

- **One task per subagent.** Don't build a generalist.
- **Detailed descriptions.** Claude routes on description; vague description = dead agent.
- **Minimum tools.** Least privilege, smaller attention surface.
- **Check into VCS** (`.claude/agents/`). Share project subagents with the team.

## Subagents vs main conversation

Use **main** for iterative refinement, multi-phase shared context, quick targeted changes, and latency-sensitive work. Use **subagents** for verbose output you won't reference, tool-restriction enforcement, or self-contained work that can return a summary. Prefer [[skills|Skills]] when you want reusable prompts/workflows in the main context rather than isolated. For quick meta-questions, `/btw` (no tool access, answer discarded).

## Cross-references and dialogue with existing pages

- Mechanics side of [[subagent-patterns]] (Alex Ker's fan-out and pipeline) — this doc supplies the how, that page supplies the when.
- [[harness-engineering]] (Panutat) — pipeline-of-review-agents now has a first-class implementation surface: `.claude/agents/` checked into the repo.
- [[progressive-disclosure]] — built-in subagents (`Explore`, `Plan`) are themselves a disclosure layer: exploration results stay out of the main window.
- [[llm-knowledge-bases]] — `memory: project` is Claude Code's own version of the `MEMORY.md` + per-file pattern this wiki uses.
- [[advisor-strategy]] — `model: haiku` subagents that escalate with `inherit` (or `opus`) on hard decisions is a clean in-harness implementation of the executor/advisor split.

## See also

- [[claude-code]]
- [[claude-code-session-management]]
- [[subagent-patterns]]
- [[coding-harness]]
- [[progressive-disclosure]]
- [[harness-engineering]]
- [[advisor-strategy]]
- [[instruction-budget]]
