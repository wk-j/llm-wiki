---
title: Graph RAG
type: concept
tags: [rag, knowledge-graphs, ai, llm]
created: 2026-04-13
updated: 2026-04-13
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md]
---

# Graph RAG

Retrieval-Augmented Generation that uses a knowledge graph as its retrieval backend instead of (or alongside) a vector store. The graph provides structured, relational context — not just similar text chunks, but connected entities, typed relationships, and traversable paths.

## How it differs from vector RAG

| | **Vector RAG** | **Graph RAG** |
|---|---|---|
| **Retrieval** | Nearest-neighbor embedding search | Graph traversal + optional embedding search |
| **Context** | Chunks of similar text | Structured relationships between entities |
| **Strength** | Semantic similarity | Multi-hop reasoning, dependency tracking |
| **Weakness** | Misses structural relationships | More complex to build and maintain |

## Traditional vs. precomputed Graph RAG

Traditional Graph RAG gives the LLM raw graph edges and expects it to explore iteratively — often requiring 4+ query hops to understand one symbol's context. [[gitnexus]] exemplifies a **precomputed** approach: clustering, process tracing, and confidence scoring happen at index time, so the LLM receives complete structural context in a single tool response.

This distinction matters for:
- **Reliability** — the LLM can't accidentally miss context that's already pre-assembled
- **Token efficiency** — no multi-query chains
- **Model democratization** — smaller models work because the tool does the heavy lifting

## Applications

- [[code-knowledge-graphs|Code intelligence]] — structural codebase understanding for AI agents
- Enterprise knowledge management — connecting documents, people, concepts
- Scientific literature — traversing citation and concept networks
- Conversational AI — grounding responses in factual relationship graphs

## See also

- [[code-knowledge-graphs]]
- [[gitnexus]]
- [[llm-knowledge-bases]]
