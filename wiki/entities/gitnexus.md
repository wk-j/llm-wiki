---
title: GitNexus
type: entity
tags: [developer-tools, code-intelligence, knowledge-graphs, mcp, open-source]
created: 2026-04-13
updated: 2026-04-13
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md]
---

# GitNexus

Open-source code intelligence engine that indexes codebases into [[code-knowledge-graphs|knowledge graphs]] and exposes them to AI agents via [[model-context-protocol|MCP]]. Created by Abhigyan Patwari; enterprise offering through [[akon-labs]].

## What it does

Builds a complete graph of a codebase — functions, classes, imports, call chains, clusters, execution flows — then lets AI coding tools query that graph through smart, precomputed tools. The core claim: traditional [[graph-rag]] requires multiple LLM query hops to understand structure; GitNexus precomputes relationships so tools return complete context in one call.

## Key details

- **License**: Open source (GitHub: abhigyanpatwari/GitNexus)
- **Languages**: 14 supported via Tree-sitter (TypeScript, Python, Java, Go, Rust, C#, etc.)
- **Database**: LadybugDB (embedded graph DB with vector support)
- **Interfaces**: CLI + MCP server (for daily dev), Web UI (browser-based, no server)
- **Editor support**: Claude Code (full — MCP + skills + hooks), Cursor, Codex, Windsurf, OpenCode
- **Install**: `npm install -g gitnexus` (CLI) or gitnexus.vercel.app (web)
- **Privacy**: Fully local (CLI) or fully in-browser (web) — no code leaves the machine

## Positioning

> "Like DeepWiki, but deeper. DeepWiki helps you understand code. GitNexus lets you analyze it — because a knowledge graph tracks every relationship, not just descriptions."

## See also

- [[akon-labs]]
- [[code-knowledge-graphs]]
- [[model-context-protocol]]
- [[graph-rag]]
