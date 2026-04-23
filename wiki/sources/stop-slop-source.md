---
title: Stop Slop
type: source
tags: [ai, writing, style, llm, prompt engineering]
created: 2026-04-23
updated: 2026-04-23
sources: [https://github.com/hardikpandya/stop-slop]
---

# Stop Slop by Hardik Pandya

**Stop Slop** is a "skill" for large language models, published on GitHub by Hardik Pandya. It's a set of instructions designed to help an AI like Claude remove predictable writing patterns, or "AI tells," from its prose to sound more human.

The goal is to produce writing that is more direct, dense, authentic, and respectful of the reader's intelligence.

## Key Components

The repository is structured as a skill that an agent can load.

-   **`SKILL.md`**: The core instruction file. It outlines rules for eliminating filler, breaking formulaic structures, using active voice, being specific, varying rhythm, and trusting the reader. It also includes a scoring rubric to rate prose on dimensions like Directness, Rhythm, Trust, Authenticity, and Density.
-   **`references/phrases.md`**: A list of "banned" words and phrases. This includes throat-clearing openers ("Here's the thing:"), emphasis crutches ("Let that sink in."), business jargon ("Lean into"), and a long list of adverbs.
-   **`references/structures.md`**: A guide to avoiding cliché structural patterns like binary contrasts ("Not X, but Y"), negative listing, dramatic sentence fragments, and giving false agency to inanimate objects ("the data tells us"). It strongly advocates for using active voice and naming the human actor in any sentence.
-   **`references/examples.md`**: A series of "before and after" examples that demonstrate how to apply the rules to transform stilted AI prose into more direct, human-like writing.

## Core Principles

-   **Cut filler:** Remove anything that doesn't add meaning.
-   **Be direct:** State claims without rhetorical setup or hand-holding.
-   **Name the actor:** Use active voice and identify the human subject responsible for an action.
-   **Vary rhythm:** Mix sentence lengths and structures to avoid a metronomic feel.
-   **Trust the reader:** Don't over-explain or add unnecessary emphasis.
