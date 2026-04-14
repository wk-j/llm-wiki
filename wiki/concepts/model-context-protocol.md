---
title: Model Context Protocol (MCP)
type: concept
tags: [mcp, ai-agents, developer-tools, protocols]
created: 2026-04-13
updated: 2026-04-13
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md]
---

# Model Context Protocol (MCP)

An open protocol for connecting AI agents to external tools, data sources, and services. MCP provides a standardized interface so that tools built once can be used by any compatible AI agent — Claude Code, Cursor, Codex, Windsurf, OpenCode, and others.

## How it works

An MCP server exposes:
- **Tools** — callable functions the agent can invoke (e.g., search, analyze, rename)
- **Resources** — readable data the agent can access (e.g., schema definitions, statistics)
- **Prompts** — guided workflow templates for common tasks

The server communicates via stdio (for local CLI tools) or HTTP. The AI agent discovers available tools and calls them as needed during its reasoning process.

## Why it matters

Without MCP, every tool integration is a custom adapter per editor/agent. With MCP, a tool like [[gitnexus]] implements one server and works across all compatible agents. This creates an ecosystem where tool developers build once and agent developers consume freely.

## Example: GitNexus MCP integration

[[gitnexus]] exposes 16 tools via MCP including `query`, `context`, `impact`, `detect_changes`, `rename`, and `cypher`. It also provides resource URIs for repo metadata and prompts for guided workflows. Claude Code gets the deepest integration with additional hooks (PreToolUse/PostToolUse) that enrich searches with graph context and auto-reindex after commits.

## See also

- [[gitnexus]]
- [[code-knowledge-graphs]]
