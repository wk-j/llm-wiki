---
title: Idea File
type: concept
tags: [llm, ai-agents, knowledge-sharing, open-source]
created: 2026-04-16
updated: 2026-04-16
sources: ["Karpathy's LLM Wiki The Complete Guide to His Idea File.md"]
---

# Idea File

A document that describes a *pattern* or *system* at a conceptual level — not code, not an app — intended to be given to an LLM agent that will then instantiate a version customized to the user's environment, tools, and preferences. Coined by [[andrej-karpathy]] in April 2026 alongside his LLM Wiki gist.

## The core idea

In the pre-agent era, sharing a useful tool meant sharing the *implementation*: a GitHub repo, an npm package, a Docker image. The recipient clones, configures, and runs it. In a world where everyone has an LLM agent (Claude Code, Codex, Cursor, OpenCode), sharing the *idea* is often more valuable than sharing the code.

Karpathy's exact words:
> "In this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it for your specific needs."

Why the shift:
- **Portability** — an idea works across any tool stack; code is specific to one
- **Customization** — your agent builds it for your exact setup, not the author's
- **Intentional vagueness** — the gist is "intentionally kept a little bit abstract/vague because there are so many directions to take this in"

## How to use one

1. Copy the idea file (a markdown gist or document)
2. Paste it into your LLM agent's context
3. Tell the agent: "Set up a [system] based on this idea file for [your topic]"
4. The agent creates the directory structure, schema, and walks you through first use

## Format characteristics

- Written in markdown
- Describes architecture, operations, and conventions — not implementation
- Contains worked examples but no runnable code
- Ends with something like: "The document's only job is to communicate the pattern. Your LLM can figure out the rest."
- Optionally has a Discussion tab (GitHub gist) for community contributions — "open ideas" rather than open source

## Relationship to open source

Traditional open source: share code → others fork/adapt. Idea files: share a pattern → each agent builds a custom version. This is **open ideas** — the collaborative space is around refining the concept, not merging PRs. The Discussion tab on Karpathy's gist embodies this: people adjust the idea or contribute their own, without needing to agree on implementation details.

## Notable examples

- Karpathy's "LLM Wiki" gist — describes the [[llm-knowledge-bases]] pattern; what this wiki was built from
- The CLAUDE.md / AGENTS.md schema inside any LLM wiki is itself an idea file for the LLM to follow

## See also

- [[andrej-karpathy]]
- [[llm-knowledge-bases]]
- [[karpathy-llm-wiki-idea-file]]
