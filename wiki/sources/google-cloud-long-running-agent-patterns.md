---
title: "5 Agent Design Patterns for Long-running AI Agents"
type: source
tags: [ai, agents, long-running, google-cloud, gemini-enterprise, architecture]
created: 2026-04-23
updated: 2026-04-23
sources: [5 Agent Design patterns for Long-running AI Agents.md]
---

# 5 Agent Design Patterns for Long-running AI Agents

Google Cloud Tech article by **Addy Osmani** and **Shubham Saboo**, posted on X (@GoogleCloudTech, 2026-04-22). Promotes the Cloud Next '26 announcement that **Agent Runtime** (on the Gemini Enterprise Agent Platform) now supports long-running agents with up to **7 days** of persistent state. Positioned for workflows that don't fit one conversation turn: insurance claim batches, week-long sales sequences, cross-system financial reconciliation.

Treat as a vendor blog — the patterns are legitimately general, but the governance story is a product pitch for Google's Agent Identity / Agent Registry / Agent Gateway / Memory Bank / Memory Profiles / Mission Control.

## Core framing

Short-lived agents reconstruct context from a database every turn and lose the reasoning chain, soft signals, and confidence gradients that made prior decisions coherent. Long-running agents keep that state alive across days — the agent is a **server process**, not a request handler.

## The five patterns

### 1. Checkpoint-and-Resume

Multi-day workflow fails on document 201 of 500 — without checkpointing, restart from zero. Agent Runtime gives a sandboxed filesystem + bash, so intermediate results, processing logs, and idempotency markers are durable. Code example (ADK `DocumentProcessor`) checkpoints every 50 docs — granularity balances durability against overhead. Analogous to a data pipeline, not a request handler.

### 2. Delegated Approval (Human-in-the-Loop)

Critique of common HITL: serialize to JSON, webhook, hope someone sees the notification, rehydrate hours later with lost implicit context. Long-running variant: agent **pauses in place** — full reasoning chain, working memory, tool call history, pending action all intact. Zero compute while paused, sub-second cold start on resume. Mission Control inbox categorizes signals into "Needs your input" / "Errors" / "Completed" so a fleet of 20 agents doesn't get lost in Slack.

### 3. Memory-Layered Context

Two layers:
- **Memory Bank** — long-term, dynamically generated from conversations, organized by topic
- **Memory Profiles** — low-latency access to specific high-accuracy details (working memory)

Biggest new risk called out: **memory drift.** An agent "learns" from a few atypical interactions that a shortcut is acceptable, then applies it broadly. Shared memory pools across agents → cross-workflow data leakage.

Governance triad (positioned as IAM-for-agents):
- **Agent Identity** — cryptographic identity, like a service account; scopes which memory banks / tools the agent can reach
- **Agent Registry** — service discovery; which agents are active, what version of prompt+code, what execution state
- **Agent Gateway** — API-gateway-for-LLMs between agent and its memory+tools; evaluates requests against org policy (e.g. block PII writes to long-term memory)

Key principle: **audit what agents remember, not just what they do.** Memory shapes behavior over time.

### 4. Ambient Processing

Not all long-running agents are human-facing. **Batch / Event-Driven Agents** connect to BigQuery and Pub/Sub, run for days, process streams, escalate only on edge cases. Example: content moderation agent.

Architectural claim: don't hardcode policy into ambient agents. Externalize to Agent Gateway so one policy update propagates to the whole fleet without redeploys. Agent Identity selects which policies apply; Registry tracks which version runs against which policy set.

### 5. Fleet Orchestration

Coordinator + specialist agents, each with its own Identity / Gateway policy / Registry entry. Sales prospecting example (Lead Research → Outreach → Scoring → Follow-up specialists). Containers per specialist (Bring Your Own Container) → bad deploy in one doesn't cascade. ADK provides graph-based declarative workflows for the coordination logic.

Framed as the classic **coordinator/worker** distributed-systems pattern — what's new is ADK hosting it natively and Agent Observability tracking per-specialist versions.

## Composition

> A compliance system might use Checkpoint-and-Resume for document processing, Delegated Approval for review gates, Memory-Layered Context for cross-session knowledge, and Fleet Orchestration to coordinate specialists.

Decision heuristic offered: **what is the longest uninterrupted unit of work your agent needs to perform?** Minutes → don't need long-running agents. Hours to days → these patterns are where you start.

## Product name reference

- **Agent Runtime** — the execution platform offering the 7-day state
- **Agent Development Kit (ADK)** — Google's agent-authoring framework; code sample in the article uses `from google.adk import Agent, ToolContext`
- **Mission Control** — operator UI (inbox, categorized notifications)
- **Memory Bank** + **Memory Profiles** — managed memory layers
- **Agent Identity / Registry / Gateway** — governance triad
- **Agent Observability** — per-agent monitoring
- **Batch and Event-Driven Agents** — ambient-agent surfaces with BigQuery + Pub/Sub integration

## Relationship to existing wiki

- **[[subagent-patterns]]** — Fleet Orchestration is a larger-scale, cross-process sibling of the pipeline/fan-out patterns; coordinator-worker is an explicit mention
- **[[agent-runtime-untrusted]]** — Agent Gateway as out-of-model policy enforcement is essentially APTS-SC-020 (external allowlist) rebranded as a product. Memory-drift governance is an APTS-MR-023-shaped concern that APTS doesn't currently spell out
- **[[auto-mode]]** — classifier gating at harness layer is the Claude Code parallel to Agent Gateway
- **[[agent-swarm]]** — Kimi K2.6's scale-out 300-subagent pattern is the same coordinator/worker shape as Fleet Orchestration, but ambient + persistent rather than single-task
- **[[advisor-strategy]]** — coordinator + cheap specialists matches the executor/advisor split conceptually
- **[[claude-code-session-management]]** — Checkpoint-and-Resume is the persistent-agent analogue of what compaction/rewind solve for a single session

## What's net-new

- **Memory drift** as a named failure mode (agent behavior warps via accumulated atypical experience; cross-agent memory leakage)
- **Pause-in-place** HITL framing — pause consumes zero compute, state stays resident; contrast with serialize → webhook → rehydrate
- **Fleet governance vocabulary** mapped to microservice infra primitives (Identity / Registry / Gateway / Observability)
- **Ambient agents** as a first-class category distinct from interactive long-runs
- Concrete 7-day state budget as an actual platform capability rather than a research pattern

## What to treat with caution

- Vendor blog; governance is framed to sell the product stack. The *patterns* are general, the *implementations* are Google-specific. A Claude Code + MCP + custom HITL setup can realize the same patterns with different pieces.
- No benchmarks or case studies — all examples are illustrative code or hypothetical scenarios
- "Sub-second cold starts" and "zero compute while paused" are marketing claims, not measured numbers

## See also

- [[long-running-agents]]
- [[google-cloud]]
- [[gemini-enterprise-agent-platform]]
- [[subagent-patterns]]
- [[agent-runtime-untrusted]]
- [[auto-mode]]
- [[agent-swarm]]
