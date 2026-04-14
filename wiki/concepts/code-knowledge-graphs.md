---
title: Code Knowledge Graphs
type: concept
tags: [knowledge-graphs, code-intelligence, developer-tools, ai-agents]
created: 2026-04-13
updated: 2026-04-13
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md]
---

# Code Knowledge Graphs

A knowledge graph built from a codebase's structure — representing functions, classes, modules, imports, call chains, inheritance, and execution flows as nodes and edges. Unlike flat text search or embeddings over code snippets, a code knowledge graph captures **relationships**: who calls what, what depends on what, how execution flows from entry points through the system.

## Why they matter for AI agents

AI coding tools typically work with file contents and text search. They can find a function but don't know its full dependency graph. Editing a function without knowing its callers leads to breaking changes. A code knowledge graph gives agents structural awareness — blast radius analysis, process tracing, and confidence-scored dependency chains.

## Construction pipeline (as exemplified by [[gitnexus]])

1. **AST parsing** — extract symbols (functions, classes, interfaces) using Tree-sitter
2. **Resolution** — resolve cross-file imports, calls, heritage, and receiver types
3. **Clustering** — group related symbols into functional communities (e.g., Leiden algorithm)
4. **Process tracing** — follow execution flows from entry points through call chains
5. **Search indexing** — build hybrid indexes (BM25 + semantic) over the graph

## Precomputed vs. query-time structure

Traditional [[graph-rag]] stores edges and lets the LLM explore at query time, requiring multiple hops. The precomputed approach (as in [[gitnexus]]) resolves clusters, processes, and confidence scores at index time, so a single tool call returns complete structural context.

## Key operations

- **Impact analysis** — given a symbol, find everything upstream (depends on it) and downstream (it depends on) with confidence scores
- **Context** — 360-degree view of a symbol: callers, callees, process participation
- **Change detection** — map git diffs to affected processes and risk levels
- **Process-grouped search** — search results organized by execution flows, not just file matches

## See also

- [[gitnexus]]
- [[graph-rag]]
- [[model-context-protocol]]
- [[llm-knowledge-bases]]
