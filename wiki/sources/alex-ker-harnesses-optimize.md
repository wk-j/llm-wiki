---
title: "Harnesses are everything. Here's how to optimize yours."
type: source
tags: [ai, claude-code, harness, agents, prompt-engineering, mcp, subagents]
created: 2026-04-18
updated: 2026-04-18
sources: [Harnesses are everything. Here's how to optimize yours..md]
---

# Harnesses are everything. Here's how to optimize yours.

**Source:** Twitter/X post by [[alex-ker|@thealexker]] (Alex Ker), 2026-04-18
**URL:** https://x.com/thealexker/status/2045203785304232162

## Framing

"Engineers used to argue about IDEs, now we argue about harnesses." The author positions the harness — [[claude-code|Claude Code]], [[openai-codex|Codex]], [[opencode|OpenCode]], Cursor, Deep Agent CLI, Roo Code, etc. — as the layer where engineering judgment actually applies in the AI coding era, not the model itself.

A harness is defined concretely as a `while (have next message) do {tool}` loop. Its primary jobs:

1. Manage context in an inherently stateless LLM via sessions and compressions.
2. Wrap the model with tool calls, I/O processing, and guardrails.

See [[coding-harness]].

## Three things you can change today

### 1. Keep .md files lean and human-written

- **[[instruction-budget|Instruction budget]]**: frontier LLMs can only follow "a few hundred" instructions before entering the "dumb zone" and start missing relevant instructions amongst the bloat. Giving too many instructions functionally encourages hallucination. (Sourced to Kyle from [[humanlayer|HumanLayer]].)
- **Human-written beats LLM-generated** for global system prompts (`CLAUDE.md` / `AGENTS.md`). Cited ETH research: LLM-generated system prompts degrade performance while costing ~20% more in inference.
- Describe minimal requirements: what the project is, who the end users are. Every token must fight for its place — it's injected globally on every session.
- **[[progressive-disclosure|Progressive disclosure]]** instead of front-loading: only let the agent pull context when needed; give individual `.md` files descriptive names so the agent can discover.

Three surfaces where progressive disclosure applies:

- **CLIs** — `mycli --help` → `mycli deploy --help`. Matters most for CLIs the model has never seen. Use a short `CLAUDE.md` line like *"use uv for Python package management, run uv --help to discover subcommands before assuming syntax"* as an entry-point pointer, not a full reference.
- **Skills** — [[claude-code|Claude Code]], [[openai-codex|Codex]], and [[opencode|OpenCode]] converged: load only name + description at startup; full `SKILL.md` loads on demand. Codex docs explicitly call this "progressive disclosure."
- **MCP tools** — this is where harnesses diverge. Claude Code has built-in MCP tool search, indexing names at startup and pulling schemas on demand (Anthropic reports ~85% context reduction). Codex and OpenCode load all configured MCP definitions upfront; OpenCode docs warn users to limit server count. **Actionable:** be selective which MCP servers you connect per project; write keyword-rich tool descriptions; disconnect irrelevant servers.

### 2. Use R.P.I. to work at a higher abstraction

HumanLayer's **R.P.I. framework** (`research` → `plan` → `implement`). Every prompt should do exactly one:

1. **Research** — hand the agent the problem; let it explore structure, prior art, function defs, file relationships. *No action taken at this step.*
2. **Plan** — agent writes a step-by-step execution plan. **Human proactively reviews and verifies.** "Outsourcing thinking or being lazy at this step will cost you dearly later on."
3. **Implement** — execute the approved plan in a new ("main") context window. If the plan is long, break it into subagents so intermediate state doesn't pollute main.

> "Operating a harness is leading it to behave in a way the best staff engineers approach problem-solving: break problems into subproblems, plan before implementing, get a second set of eyes on the plan."

See the R.P.I. section in [[coding-harness]].

### 3. Use subagents to maintain clean context

Core heuristic: **delegate to a subagent when a summary of the work is sufficient for the main agent.** If you'll want to ask "how does this connect to what I looked at earlier?", keep it in your primary window.

Two patterns (see [[subagent-patterns]]):

- **Parallel fan-out** — breadth. Spin up a subagent per candidate theory (e.g., three root-cause theories after an alert). Each investigates independently; main synthesizes summaries. Alex built a rudimentary version of this at [[baseten|Baseten]] when gpt-oss-120b launched ([gpt-oss-swarm](https://github.com/AlexKer/gpt-oss-swarm)). Also useful for sampling multiple model outputs concurrently (MiniMax M2.5 + GLM-5).
- **Pipelines** — depth. Push a feature through sequential roles: UX designer → architect → devil's advocate. Each stage adds analysis. Especially beneficial for non-deterministic LLM systems. Can use a frontier model as consolidating judge.

The pipeline pattern directly parallels [[harness-engineering]] (Panutat Tejasen's curricular formulation): the same subagent-pipeline pattern, seen from a pedagogy lens rather than a daily-productivity lens.

## Takeaway: Commit

"The best harness is the harness that you have customized and iterated on with human engineering." Switching harnesses constantly means losing institutional knowledge encoded in config files and failure-case logs.

**Recommendation:** pick the harness that covers the majority of team use cases; treat every failure as a data point (*what broke, at which step, under what conditions*); feed that back into `.md` files and prompting strategy.

## Key claims / attributions

| Claim | Attributed to |
|---|---|
| Few-hundred-instruction "dumb zone" | Kyle, [[humanlayer\|HumanLayer]] |
| LLM-generated system prompts underperform (+20% cost) | ETH research (cited, no link) |
| MCP tool search ~85% context reduction | [[anthropic\|Anthropic]] |
| R.P.I. framework | [[humanlayer\|HumanLayer]] |
| "Progressive disclosure" naming | [[openai-codex\|Codex]] docs (explicit) |

## See also

- [[alex-ker]]
- [[humanlayer]]
- [[coding-harness]]
- [[instruction-budget]]
- [[progressive-disclosure]]
- [[subagent-patterns]]
- [[harness-engineering]]
- [[claude-code-session-management]]
- [[ai-orchestrator]]
- [[advisor-strategy]]
- [[context-rot]]
- [[compaction]]
