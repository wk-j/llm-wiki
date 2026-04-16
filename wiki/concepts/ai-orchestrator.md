---
title: AI Orchestrator
type: concept
tags: [ai, software-engineering, agents, roles]
created: 2026-04-15
updated: 2026-04-15
sources: [software-engineer-role-ai-era.md, Using Claude Code Session Management & 1M Context.md]
---

# AI Orchestrator

An engineering role defined by **directing pipelines of AI agents** rather than directly writing the code those agents produce. Framed in the source post as the new definition of senior developer work.

## Responsibilities

- Design the pipeline: which agents exist, what each does, what context each receives.
- Decide sequencing: when an agent runs, what triggers it, how it hands off.
- Define handoffs: how output from one agent becomes input for the next.
- Set quality gates: where human review or automated evaluation sits between steps.

## Why this is a senior-developer role

Orchestrating agents is one level of abstraction above writing code. It requires:

- A system-level mental model (same skill as [[engineering-role-shift|Systems Architect]] work).
- Familiarity with each agent's failure modes so you can route around them.
- Judgment about when a step should be deterministic code vs. an LLM call.

A junior can run a single agent on a prompt. Orchestration is composing *many* agents, each of which is individually unreliable, into a system that is collectively reliable — closer in flavor to distributed systems engineering than to prompt engineering.

## Subagents as context management

Spawning subagents is also a [[context-rot]] mitigation technique. Each subagent receives a fresh context window; intermediate tool output stays isolated. Only the final result returns to the parent session. The mental test: *"Will I need this intermediate output again, or just the conclusion?"* If the latter, delegate to a subagent. See [[compaction]] for the alternative when context has already grown large.

## Related infrastructure

Orchestration builds on the tooling layer that the AI Tool Builder role produces:

- [[model-context-protocol|MCP]] servers — give agents access to tools and data.
- Agent frameworks — scaffolding for multi-step, multi-agent workflows.
- Evaluation pipelines — catch silent regressions when an agent or prompt changes.
- RAG systems — ground agent output in specific knowledge bases (cf. [[llm-knowledge-bases]]).

## The advisor inversion

The [[advisor-strategy]] explicitly inverts the orchestrator-worker pattern: instead of a large model decomposing and delegating, a small model drives end-to-end and escalates to a large model only at hard decision points. This can be cheaper than the small model running solo because advisory guidance prevents expensive dead-end tool loops.

## See also

- [[advisor-strategy]]
- [[engineering-role-shift]]
- [[domain-to-ai-translator]]
- [[model-context-protocol]]
- [[llm-coding-pitfalls]]
- [[software-engineer-role-ai-era]]
