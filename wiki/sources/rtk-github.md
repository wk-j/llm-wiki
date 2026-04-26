---
title: RTK (RTK-AI) GitHub Repository
type: source
tags: [ai, agents, cli, rust, optimization, tokens]
created: 2026-04-25
updated: 2026-04-25
sources: [https://github.com/rtk-ai/rtk]
---

# RTK (RTK-AI) GitHub Repository

High-performance CLI proxy written in Rust designed to reduce LLM token consumption by 60–90%. It intercepts command outputs and compresses them for agent consumption.

## Key Features

- **Smart Filtering:** Removes noise (comments, whitespace, boilerplate).
- **Grouping:** Aggregates files by directory or errors by type.
- **Truncation:** Retains relevant context while cutting redundant info.
- **Deduplication:** Collapses repeated log lines into counts.
- **Broad Support:** 100+ commands (Git, AWS, Docker, K8s, Jest, Pytest, Cargo, etc.).
- **Tee Recovery:** Saves full, unfiltered output to a local file on failure.
- **Analytics:** `rtk gain` command provides statistics and ASCII graphs of token savings.
- **Heuristics:** `rtk smart` for 2-line file summaries; `rtk read --l aggressive` for signature-only views.

## Architecture

- **Transparent Proxy:** Sits between the agent (e.g., Claude Code, Cursor) and the shell.
- **Auto-Rewrite Hook:** Bash hook transparently rewrites commands for the agent.
- **Single Rust Binary:** Optimized for speed (<10ms overhead).

## Integration

Supports 12+ AI tools including:
- **CLI:** [[claude-code|Claude Code]], Gemini CLI, GitHub Copilot CLI.
- **IDE:** [[cursor|Cursor]], Windsurf, VS Code Copilot.
- **Browser/Extension:** [[opencode|OpenCode]], [[cline|Cline (Roo Code)]].

## Payoff

Maximizes effective context window and minimizes API costs by focusing on optimizing "sensory input" (shell output).
