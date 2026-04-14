---
title: "GitNexus: The Zero-Server Code Intelligence Engine"
type: source
tags: [developer-tools, knowledge-graphs, code-intelligence, mcp, graph-rag, ai-agents]
created: 2026-04-13
updated: 2026-04-13
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md]
---

# GitNexus: The Zero-Server Code Intelligence Engine

GitHub README for [[gitnexus]], an open-source code intelligence engine by [[akon-labs]].

## Key idea

AI coding tools (Cursor, Claude Code, Codex) don't truly understand codebase structure. They edit a function without knowing dozens of others depend on its return type, shipping breaking changes. GitNexus solves this by building a [[code-knowledge-graphs|code knowledge graph]] that maps every dependency, call chain, cluster, and execution flow, then exposing it through smart tools via [[model-context-protocol|MCP]].

## Core innovation: Precomputed Relational Intelligence

Traditional [[graph-rag]] gives an LLM raw graph edges and hopes it explores enough — requiring multiple query hops. GitNexus **precomputes structure at index time** (clustering, process tracing, confidence scoring) so tools return complete context in a single call. This means even smaller models get full architectural clarity.

## Two interfaces

| | **CLI + MCP** | **Web UI** |
|---|---|---|
| **For** | Daily dev with Cursor, Claude Code, Codex | Quick exploration, demos |
| **Scale** | Full repos, any size | ~5k files (browser memory) or unlimited via backend |
| **Privacy** | Everything local | Everything in-browser |
| **Storage** | LadybugDB native | LadybugDB WASM |
| **Parsing** | Tree-sitter native | Tree-sitter WASM |

Bridge mode (`gitnexus serve`) connects the two — web UI auto-detects the local server.

## Capabilities

- **Impact analysis** — blast radius with depth grouping and confidence scoring
- **Process-grouped search** — hybrid BM25 + semantic + RRF, results grouped by execution flows
- **360-degree symbol context** — all callers, callees, process participation for any symbol
- **Multi-file rename** — coordinated rename via graph + text search
- **Git-diff change detection** — maps changed lines to affected processes and risk levels
- **Wiki generation** — LLM-powered docs from the knowledge graph
- **Cypher queries** — raw graph queries for custom exploration

## Indexing pipeline

1. **Structure** — file tree mapping
2. **Parsing** — AST extraction via Tree-sitter (14 languages)
3. **Resolution** — cross-file imports, calls, heritage, constructor inference, receiver types
4. **Clustering** — Leiden community detection groups related symbols
5. **Processes** — traces execution flows from entry points through call chains
6. **Search** — builds hybrid search indexes

## MCP integration

Exposes 16 tools (11 per-repo + 5 group) including `query`, `context`, `impact`, `detect_changes`, `rename`, and `cypher`. Also provides resource URIs and guided workflow prompts. Claude Code gets the deepest integration: MCP tools + agent skills + PreToolUse/PostToolUse hooks.

## Multi-repo architecture

Global registry at `~/.gitnexus/registry.json`. One MCP server serves all indexed repos. LadybugDB connections opened lazily, evicted after 5 min inactivity (max 5 concurrent).

## Tech stack

Tree-sitter (AST parsing), LadybugDB (graph database), Graphology (clustering), transformers.js (embeddings), Sigma.js (WebGL visualization), React 18 + Vite + Tailwind v4 (web frontend).

## Enterprise

Available via [[akon-labs]] as SaaS or self-hosted. Adds PR review, auto-updating code wiki, auto-reindexing, multi-repo unified graphs, OCaml support. Upcoming: auto regression forensics, end-to-end test generation.

## See also

- [[gitnexus]]
- [[akon-labs]]
- [[code-knowledge-graphs]]
- [[graph-rag]]
- [[model-context-protocol]]
- [[llm-knowledge-bases]]
