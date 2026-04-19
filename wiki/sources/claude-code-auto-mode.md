---
title: "Auto mode for Claude Code (Anthropic blog)"
type: source
tags: [ai, claude, claude-code, permissions, anthropic, autonomy]
created: 2026-04-20
updated: 2026-04-20
url: https://claude.com/blog/auto-mode-for-claude-code
date_published: 2026-03-24
sources: [claude.com blog]
---

# Auto mode for Claude Code

Anthropic blog post (2026-03-24) introducing **auto mode**, a new permissions mode in [[claude-code|Claude Code]] that sits between default permission prompts and `--dangerously-skip-permissions`. Research preview; initially Team plan, then Enterprise + API.

## What it is

A permission mode where Claude makes permission decisions on the user's behalf. Before each tool call runs, a **classifier** reviews it:

- **Safe actions** proceed automatically.
- **Risky actions** are blocked; Claude is redirected to take a different approach.
- If Claude keeps insisting on blocked actions, a permission prompt eventually surfaces to the user.

The classifier watches for: mass file deletion, sensitive data exfiltration, malicious code execution. Full block list: [permission-modes docs](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default).

## Why it exists

Default Claude Code permissions require approval for every file write and bash command — safe, but incompatible with "kick it off and walk away" long-running tasks. `--dangerously-skip-permissions` removes friction but also removes safety; Anthropic recommends it only inside isolated environments.

Auto mode is the **middle path**: fewer interruptions than default, less risk than full skip.

## Caveats

- **Not risk-free.** Classifier may still allow risky actions when user intent is ambiguous or Claude lacks environmental context. Still recommended to run inside an isolated environment.
- May **occasionally block benign actions**.
- **Small cost/latency impact** on tool calls (classifier runs per call).

## Enabling it

- **CLI:** `claude --enable-auto-mode`, then cycle to it with **Shift+Tab**.
- **Desktop / VS Code extension:** toggle on in Settings → Claude Code first, then select from the permission-mode dropdown.
- **Desktop default:** off; enabled at org level under Organization Settings → Claude Code.
- **Admins can disable:** set `"disableAutoMode": "disable"` in managed settings.

## Availability

- Works with Claude Sonnet 4.6 and Opus 4.6 (source dated 2026-03-24; predates the 2026-04-16 Opus 4.7 launch — see [[claude-opus-4-7-announcement]] for the 4.7 extension to Max users).
- Research preview on Team plan; Enterprise + API "in the coming days".

## Connections

- **[[delegation-mindset]]** — auto mode is one of Akshay Pachaar's three recommended delegation moves on [[claude-opus-4-7|Opus 4.7]]: lets Claude finish long tasks without check-in overhead.
- **[[coding-harness]]** — permission mode is a core harness control surface; auto mode is a new position on that spectrum.
- **[[claude-code-session-management]]** — pairs with long-running sessions where approval prompts would otherwise fragment the run.

## See also

- [[auto-mode]]
- [[claude-code]]
- [[claude-opus-4-7]]
- [[delegation-mindset]]
