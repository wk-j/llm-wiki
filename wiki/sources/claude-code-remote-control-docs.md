---
title: Claude Code — Remote Control (docs)
type: source
tags: [ai, claude-code, remote-control, mobile, docs]
created: 2026-04-21
updated: 2026-04-21
sources: [Remote Control - Claude Code Docs.md]
---

# Claude Code — Remote Control (docs)

Anthropic official docs page for **Remote Control** — a feature that lets you drive a [[claude-code|Claude Code]] session running on your local machine from `claude.ai/code` or the Claude mobile app. The session stays local; the web/mobile surface is just a window into it.

- URL: https://code.claude.com/docs/en/remote-control.md
- Requires CC v2.1.51+ (VS Code command: v2.1.79+; push notifications: v2.1.110+)
- Available on Pro / Max / Team / Enterprise (not API keys). Team/Enterprise needs admin to enable.

## Core model

**Local session + Anthropic relay.** CC on your machine makes outbound HTTPS only — never opens inbound ports. It registers with the Anthropic API and polls for work. When you connect from mobile/web, Anthropic routes messages between the client and your local session over a streaming connection. TLS throughout; short-lived per-purpose credentials.

**Consequence:** full local environment (filesystem, MCP servers, tools, project config, `@` file autocomplete) is available from phone/browser. Contrast [[claude-code-on-the-web]] (cloud-hosted — no local files/MCP).

## Three CLI invocation modes + VS Code

1. **Server mode** — `claude remote-control`. Terminal stays in listener mode. Shows URL; spacebar toggles QR. Supports multiple sessions (default capacity 32).
2. **Interactive** — `claude --remote-control` (`--rc`). Full local TUI, also remote-controllable.
3. **From existing session** — `/remote-control` (`/rc`) inside CC. Carries conversation history forward.
4. **VS Code extension** — `/remote-control` in prompt box; banner shows status.

Always-on toggle: `/config` → **Enable Remote Control for all sessions** = `true`. Each CC process then registers one remote session (multiple processes = multiple sessions).

### Server mode flags worth remembering

- `--spawn same-dir|worktree|session` — `worktree` gives each on-demand session its own git worktree (no conflicts); `session` = single-session mode (rejects extra connections). Press `w` at runtime to toggle `same-dir` ↔ `worktree`.
- `--capacity <N>` — max concurrent (default 32)
- `--sandbox` / `--no-sandbox` — filesystem/network isolation (off by default)
- `--name "…"` — custom session title
- `--verbose`

## Connect from another device

- Session URL → browser (claude.ai/code)
- QR code → Claude mobile app (iOS/Android)
- Or find by name in session list (computer icon + green dot = online)

Title priority: explicit `--name` > `/rename` > last meaningful message > auto-generated `hostname-graceful-unicorn`. `/mobile` shows a QR to download the Claude app.

## Mobile push notifications

When RC is active, Claude can push to phone — typically when a long task finishes or a decision is needed. Prompt-level request works: "notify me when the tests finish." Only on/off; no per-event config. Enable via `/config` → **Push when Claude decides**.

## Limitations (the important ones)

- **Local process must keep running.** Close terminal / quit VS Code = session ends.
- **~10 min network outage** = session times out, process exits.
- **Ultraplan disconnects RC** — both occupy the `claude.ai/code` interface; only one at a time.
- **Commands with interactive pickers are CLI-only**: `/mcp`, `/plugin`, `/resume`. Text-output commands (`/compact`, `/clear`, `/context`, `/cost`, `/exit`, `/extra-usage`, `/recap`, `/reload-plugins`) work from mobile/web.
- **Outside server mode: one remote session per interactive process.**
- **Auth gotchas:** API keys / `setup-token` / `CLAUDE_CODE_OAUTH_TOKEN` / Bedrock / Vertex / Foundry all disqualify — RC needs a full-scope claude.ai OAuth session.

## Where RC sits in the "work away from terminal" landscape

The docs include a canonical comparison table with five ways to work when you're not at the terminal:

| Option | Trigger | Where Claude runs | Best for |
|---|---|---|---|
| **Dispatch** | Message a task from Claude mobile | Your machine (Desktop app) | Delegate while away, minimal setup |
| **Remote Control** | Drive running session from claude.ai/code or mobile | Your machine (CLI or VS Code) | Steering in-progress work from another device |
| **Channels** | Push events from Telegram/Discord/custom server | Your machine (CLI) | Reacting to external events (CI, chat) |
| **Slack** | `@Claude` mention in channel | Anthropic cloud | PRs and reviews from team chat |
| **Scheduled tasks** | Cron schedule | CLI / Desktop / cloud | Recurring automation (daily reviews) |

Mental model: the axis is **(where does Claude run?) × (how is work triggered?)**. Remote Control is *local execution, human-driven, multi-device*. Claude Code on the web is *cloud execution, human-driven*. Dispatch is *local (via Desktop), mobile-triggered*. Channels is *local, external-event-triggered*.

## Key takeaways for this wiki

- Anthropic is building out a **family of surfaces on top of local CC**, unified by claude.ai/code as the remote interface. RC is the "same session, different screen" option.
- The **local-execution stance** preserves the [[agent-runtime-untrusted|local harness as trust boundary]] — none of your files/MCP get uploaded. Remote just sees the session; local still owns the sandbox/permissions.
- **Network posture** is noteworthy: outbound-only polling, no inbound ports. This matters for restrictive corp networks and aligns with how CC already operates.
- **Interoperability constraints** are real: Ultraplan kicks RC off; pickers stay local-only. Plan accordingly if mixing features.
- `--spawn worktree` for RC server mode is a natural fit for the existing [[subagent-patterns|parallel-fan-out pattern]] at the session level — multiple remote users / devices without file conflicts.

## See also

- [[claude-code]]
- [[claude-code-remote-surfaces]]
- [[claude-code-session-management]]
- [[auto-mode]]
- [[agent-runtime-untrusted]]
