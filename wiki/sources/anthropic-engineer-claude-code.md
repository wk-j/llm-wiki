---
title: "This Anthropic Engineer Uses Claude Code Differently Than Everyone Else"
type: source
tags: [claude-code, workflow, agentic-search, prompt-engineering]
url: "https://www.youtube.com/watch?v=nhE-hj7tZSE"
created: 2026-05-04
updated: 2026-05-04
sources: []
---

# This Anthropic Engineer Uses Claude Code Differently Than Everyone Else

A presentation by [[cal-rueb|Cal Rueb]], an engineer at [[anthropic|Anthropic]] who works on the Applied AI team and contributes heavily to [[claude-code|Claude Code]]. The talk covers the internal logic, best practices, and intended workflow for getting the most out of Claude Code.

## Key Takeaways

- **Pure Agent Architecture:** Claude Code doesn't use complex RAG or indexing. It relies on [[agentic-search|Agentic Search]]—using tools like `grep`, `glob`, and `find` to explore codebases iteratively, just like a human engineer would.
- **CLAUDE.md is the Memory:** Since the agent has no long-term memory between sessions, the `[[claude-md|CLAUDE.md]]` file serves as the state transfer. Cal advises reviewing it when moving to newer models (like Claude 4/Opus 4.7), as better instruction following means you might be able to remove some rules.
- **Workflow Best Practices:**
  - **Thought Partner:** Ask Claude to search around and propose a plan *before* it starts writing any files.
  - **Context Management:** Use `/compact` when the context window fills up to summarize state for the next session.
  - **Auto-accept and Permissions:** Speed up workflow by configuring auto-accept (e.g., Shift+Tab) for commands you trust.
  - **Double Escape:** Pressing `Escape` stops the agent if it goes off-path. Pressing it twice (`/rewind`) jumps back in the conversation.
- **New Capabilities:** Claude 4 models can now "think" between tool calls (extended thinking/think hard), which drastically improves complex debugging and search strategies.
