---
title: "Matt Pocock: New High-Concurrency Agent Workflow"
type: source
tags: [ai, agents, workflow, automation, slack, sandcastle, claude-code, dag]
created: 2026-04-25
updated: 2026-04-25
sources: [clipboard-1777051288740.png]
---

# Matt Pocock: New High-Concurrency Agent Workflow

**Source:** Matt Pocock (@mattpocockuk) on X (Twitter)
**Date:** April 2026

Matt Pocock outlines a high-efficiency software development lifecycle driven by swappable agent dependencies.

## The "New Flow"

1. **`/triage` (Slack):** Command initiates discussion threads with agents for each repo issue requiring triage.
2. **Issue Resolution:** Human and agents resolve discussions until issues are "ready for the agent."
3. **`/implement` (Slack):** Initiates the implementation phase.
4. **DAG Generation:** A **Planning Agent** creates a Directed Acyclic Graph (DAG) of all branches based on PRs, modeling dependencies between them.
5. **Parallel Implementation:** **Implementer Agents** work on all branches in the DAG in parallel, each with its own Slack thread for updates.
6. **Concurrency Management:** The `/implement` command can be re-run at any time with new issues; the DAG is recomputed for maximum concurrency.
7. **Human-in-the-Loop Review:** Humans review and merge PRs while implementation continues on other branches.
8. **Architectural Guardrails:** Periodic `/review` commands run on the whole codebase to identify architectural improvements or documentation drift.

## Technology Stack

- **Orchestration:** Driven by [[sandcastle|Sandcastle]] and [[vercel|Vercel]]'s Chat SDK.
- **Components:** Slack, [[claude-code|Claude Code]], and Sandboxes are treated as "swappable dependencies."

## Key Concepts

- **[[pr-dependency-dag|PR Dependency DAG]]:** The core structure that enables massive parallelism without merge conflicts.
- **Implementer Agent:** Specialized worker agents assigned to specific branches.
- **Swappable Infrastructure:** Decoupling the UI (Slack), the Intelligence ([[claude-code|Claude Code]]), and the Execution ([[sandcastle|Sandcastle]]).

## See also
- [[matt-pocock]]
- [[pr-dependency-dag]]
- [[subagent-patterns]]
- [[sandcastle]]
- [[vercel]]
