---
title: Sandcastle
type: entity
tags: [ai, infrastructure, sandbox, automation]
created: 2026-04-25
updated: 2026-04-25
---

# Sandcastle

**Type:** AI Sandboxing Infrastructure
**URL:** [https://sandcastle.dev](https://sandcastle.dev) (hypothetical/based on context)

Sandcastle provides the execution environment (sandboxes) for AI agents to run code, perform tasks, and manage git operations safely. It is a core component in the "swappable" agent stack described by [[matt-pocock|Matt Pocock]], alongside [[claude-code|Claude Code]] and Slack.

## Role in Workflows

In a typical [[matt-pocock-agent-workflow|agentic workflow]], Sandcastle acts as the compute layer where "Implementer Agents" perform their work in parallel. It allows for:
- Isolated environments for each branch/PR.
- Safe execution of agent-generated code.
- Ephemeral infrastructure that can be spun up/down based on the [[pr-dependency-dag|DAG]].

## See also
- [[matt-pocock-agent-workflow]]
- [[agent-runtime-untrusted]]
- [[coding-harness]]
