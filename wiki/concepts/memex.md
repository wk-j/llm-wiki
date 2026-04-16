---
title: Memex
type: concept
tags: [knowledge-management, history-of-computing, hypertext, information-architecture]
created: 2026-04-16
updated: 2026-04-16
sources: ["Karpathy's LLM Wiki The Complete Guide to His Idea File.md"]
---

# Memex

A hypothetical personal knowledge device described by [[vannevar-bush]] in his 1945 *Atlantic* essay "As We May Think." The Memex (memory + index) was a desk-sized machine where an individual could store all their books, records, and communications, search them rapidly, and create **associative trails** — linked sequences of documents with personal annotations.

## Core concept

Bush's key insight: the human mind works by *association*, not alphabetical order. Hierarchical filing systems force rigid categories. The Memex would let people create their own paths through knowledge — linking a chemistry paper to an economics report to a historical essay, following personal logic.

His famous quote: "Wholly new forms of encyclopedias will appear, ready-made with a mesh of associative trails running through them."

## Why it matters for LLM wikis

[[andrej-karpathy]] explicitly connects the [[llm-knowledge-bases]] pattern to the Memex:

> "The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that."

The web became *public and chaotic* rather than *private and curated*. The Memex imagined something personal. The LLM Wiki is closer to the original Memex vision:

| Dimension | Memex vision | The web | LLM Wiki |
|---|---|---|---|
| Ownership | Personal | Public | Personal |
| Curation | Active | Passive (search) | Active (ingest) |
| Cross-references | Associative trails | Hyperlinks | Wikilinks |
| Maintenance | Manual (unsolved) | Algorithmic (SEO) | LLM (solved) |

## The missing piece

Bush's unsolved problem: **who does the maintenance?** Creating associative trails, updating connections, keeping everything consistent is tedious manual work. Humans abandon knowledge systems because maintenance burden grows faster than value.

LLMs solve this: "LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."

## Historical influence

The Memex directly inspired the lineage that built the modern web:
- **Douglas Engelbart** — read Bush's 1945 article, "became infected with the idea," went on to invent the computer mouse and personal computing
- **Ted Nelson** — coined "hypertext" in 1965, directly inspired by Memex's associative trails
- **Tim Berners-Lee** — whose World Wide Web (1989) implemented hypertext at global scale

So the web is the Memex's descendant — but it evolved toward public infrastructure rather than personal knowledge management. The LLM Wiki pattern is a return to Bush's original intent.

## See also

- [[vannevar-bush]]
- [[llm-knowledge-bases]]
- [[andrej-karpathy]]
- [[karpathy-llm-wiki-idea-file]]
