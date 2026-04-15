---
title: Andrej Karpathy
type: entity
tags: [person, ai, llm]
created: 2026-04-12
updated: 2026-04-16
sources: [LLM Knowledge Bases Thread by @karpathy.md, forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls..md, "Karpathy's LLM Wiki The Complete Guide to His Idea File.md"]
---

# Andrej Karpathy

AI researcher and educator. Former Director of AI at Tesla, co-founder of OpenAI. Coined the term "vibe coding." Known for making deep learning accessible (Stanford CS231n, YouTube lectures). Active on Twitter (@karpathy).

## Relevance to this wiki

Originator of several patterns this wiki touches:

- **[[llm-knowledge-bases]]** — LLM-compiled personal wikis (2026-04-02 thread). The pattern this wiki implements.
- **[[idea-file]]** — sharing abstract patterns for LLM agents to instantiate, rather than sharing code (2026-04-04 gist follow-up).
- **[[llm-coding-pitfalls]]** — public observations on LLM code-editing failure modes ([tweet](https://x.com/karpathy/status/2015883857489522876)), later packaged by [[forrestchang]] as the [[karpathy-guidelines]] Claude Code skill.

All three prescribe lightweight markdown instruction files (`AGENTS.md`, `CLAUDE.md`, `SKILL.md`) rather than custom tooling.

## The idea file gist

After his LLM Knowledge Bases tweet went viral ("Wow, this tweet went very viral!"), Karpathy published a GitHub gist titled "LLM Wiki" — not code, not an app, but an [[idea-file]]: a structured description of the architecture, philosophy, and tooling. Its stated purpose: "The document's only job is to communicate the pattern. Your LLM can figure out the rest."

He explicitly connects the pattern to [[vannevar-bush]]'s 1945 [[memex]] concept — private, curated, associative trails. "The part he couldn't solve was who does the maintenance. The LLM handles that."

## Key practices

- Uses Obsidian as IDE for knowledge work; LLM writes on one side, Obsidian graph view on the other
- Keeps schema in `AGENTS.md` (we use `CLAUDE.md`)
- Prefers simple, flat directory structures over complex tooling
- Stays in the loop during early ingests, reduces involvement as the LLM learns the pattern
- Vibe-codes custom tools (search engines, data processing) as needs arise
- His research wiki: ~100 articles, ~400K words on a single ML research topic

## See also

- [[karpathy-llm-knowledge-bases]]
- [[karpathy-llm-wiki-idea-file]]
- [[karpathy-guidelines]]
- [[llm-knowledge-bases]]
- [[llm-coding-pitfalls]]
- [[idea-file]]
- [[memex]]
