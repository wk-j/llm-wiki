# Continue local sessions from any device with Remote Control

Source: https://code.claude.com/docs/en/remote-control.md
Ingested: 2026-04-21

> Continue a local Claude Code session from your phone, tablet, or any browser using Remote Control. Works with claude.ai/code and the Claude mobile app.

Note: Remote Control is available on all plans. On Team and Enterprise, it is off by default until an admin enables the Remote Control toggle in Claude Code admin settings.

Remote Control connects claude.ai/code or the Claude app for iOS and Android to a Claude Code session running on your machine. Start a task at your desk, then pick it up from your phone on the couch or a browser on another computer.

When you start a Remote Control session on your machine, Claude keeps running locally the entire time, so nothing moves to the cloud. With Remote Control you can:

- **Use your full local environment remotely**: filesystem, MCP servers, tools, and project configuration all stay available; typing `@` autocompletes file paths from your local project
- **Work from both surfaces at once**: conversation stays in sync across all connected devices; send messages from terminal, browser, and phone interchangeably
- **Survive interruptions**: if laptop sleeps or network drops, the session reconnects automatically when the machine comes back online

Unlike Claude Code on the web (which runs on cloud infrastructure), Remote Control sessions run directly on your machine and interact with your local filesystem. The web and mobile interfaces are just a window into that local session.

Note: Remote Control requires Claude Code v2.1.51 or later. Check with `claude --version`.

## Requirements

- **Subscription**: Pro, Max, Team, Enterprise. API keys not supported. Team/Enterprise admin must enable toggle.
- **Authentication**: `/login` via claude.ai.
- **Workspace trust**: run `claude` in project dir at least once to accept trust dialog.

## Start a Remote Control session

Three CLI invocation modes + VS Code.

### Server mode

```bash
claude remote-control
```

Stays running in terminal; waits for remote connections. Shows session URL, spacebar toggles QR code.

Flags:
- `--name "My Project"` — custom session title in claude.ai/code list
- `--remote-control-session-name-prefix <prefix>` — prefix for auto-generated names; default = hostname; env `CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX`
- `--spawn <mode>`:
  - `same-dir` (default): all sessions share cwd — conflicts if editing same files
  - `worktree`: each on-demand session gets its own git worktree (requires git repo)
  - `session`: single-session mode; rejects additional connections; startup only
  - runtime: press `w` to toggle `same-dir` ↔ `worktree`
- `--capacity <N>` — max concurrent sessions, default 32; incompatible with `--spawn=session`
- `--verbose` — detailed connection/session logs
- `--sandbox` / `--no-sandbox` — sandboxing for fs/network isolation (off by default)

### Interactive session

```bash
claude --remote-control
claude --remote-control "My Project"
```

(`--rc` alias) Normal interactive CC with Remote Control enabled. You type locally while session is also available remotely.

### From an existing session

```
/remote-control
/remote-control My Project
```

(`/rc` alias) Carries over current conversation history. `--verbose`, `--sandbox`, `--no-sandbox` not available here.

### VS Code

`/remote-control` or `/rc` in prompt box. Requires CC v2.1.79+. Banner with connection status; "Open in browser" link. No name argument, no QR code. Title derived from conversation or first prompt.

## Connect from another device

- Open session URL in any browser → claude.ai/code
- Scan QR code (spacebar in `claude remote-control`) → Claude app
- Open claude.ai/code or Claude app, find by name in session list (computer icon + green dot = online)

Title order: `--name` arg > `/rename` > last meaningful message > auto-generated `myhost-graceful-unicorn`.

If env already has active session: asked to continue or start new.

`/mobile` inside CC displays download QR for iOS/Android.

### Enable for all sessions

`/config` → **Enable Remote Control for all sessions** → `true`. Each interactive CC process then registers one remote session. Multiple instances = multiple sessions. For multiple sessions from one process, use server mode.

## Connection and security

Local CC session makes **outbound HTTPS only**; never opens inbound ports. Registers with Anthropic API, polls for work. Anthropic routes messages between web/mobile client and local session over streaming connection.

All traffic over TLS (same transport security as any CC session). Uses multiple short-lived credentials, each scoped and expiring independently.

## Remote Control vs Claude Code on the web

Both use claude.ai/code interface. Key difference: **where the session runs**.

- Remote Control → your machine → local MCP servers / tools / project config available
- Claude Code on the web → Anthropic-managed cloud infrastructure

Use Remote Control when mid-local-work, want to continue elsewhere. Use web when kicking off task without local setup, working on un-cloned repo, or running parallel tasks.

## Mobile push notifications

When RC is active, Claude can push to phone. Claude decides when (task finish, needs decision). Can request in prompt: `notify me when the tests finish`. Only on/off toggle; no per-event config.

Requires CC v2.1.110+.

Setup:
1. Install Claude mobile app (iOS/Android)
2. Sign in with same account
3. Allow notifications
4. `/config` → enable **Push when Claude decides**

Troubleshooting:
- `/config` shows **No mobile registered** → open Claude app on phone to refresh push token
- iOS Focus modes / notification summaries can suppress/delay
- Android aggressive battery optimization can delay — exempt Claude

## Limitations

- **One remote session per interactive process** — outside server mode. Use server mode for multiple concurrent.
- **Local process must keep running** — close terminal/quit VS Code/stop `claude` = session ends
- **Extended network outage** — machine awake but offline >~10 min = session times out, process exits
- **Ultraplan disconnects Remote Control** — both occupy claude.ai/code interface
- **Some commands are local-only** — interactive pickers (`/mcp`, `/plugin`, `/resume`) CLI only; text-output commands (`/compact`, `/clear`, `/context`, `/cost`, `/exit`, `/extra-usage`, `/recap`, `/reload-plugins`) work from mobile/web

## Troubleshooting

- **"Remote Control requires a claude.ai subscription"** — `claude auth login` with claude.ai option; unset `ANTHROPIC_API_KEY`
- **"Remote Control requires a full-scope login token"** — `claude setup-token` / `CLAUDE_CODE_OAUTH_TOKEN` are inference-only. Use `claude auth login`.
- **"Unable to determine your organization"** — `claude auth login` refresh
- **"Remote Control is not yet enabled for your account"** — unset `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` / `DISABLE_TELEMETRY`; RC doesn't work with Bedrock/Vertex/Foundry; else `/logout` then `/login`
- **"Remote Control is disabled by your organization's policy"** — three causes: API key/Console account (use claude.ai OAuth); Team/Enterprise admin hasn't enabled; admin toggle grayed out (data retention/compliance incompatible — contact Anthropic support)
- **"Remote credentials fetch failed"** — `--verbose` for details. Common: not signed in; firewall/proxy; session creation failed

## Choose the right approach (comparison table)

| Option | Trigger | Claude runs on | Setup | Best for |
|---|---|---|---|---|
| Dispatch | Message a task from Claude mobile app | Your machine (Desktop) | Pair mobile app with Desktop | Delegating work while away, minimal setup |
| Remote Control | Drive running session from claude.ai/code or Claude mobile | Your machine (CLI or VS Code) | Run `claude remote-control` | Steering in-progress work from another device |
| Channels | Push events from Telegram/Discord/own server | Your machine (CLI) | Install channel plugin or build own | Reacting to external events (CI failures, chat) |
| Slack | Mention `@Claude` in team channel | Anthropic cloud | Install Slack app with CC on the web enabled | PRs and reviews from team chat |
| Scheduled tasks | Set a schedule | CLI / Desktop / cloud | Pick frequency | Recurring automation (daily reviews) |

## Related

- Claude Code on the web — cloud sessions
- Ultraplan — cloud planning from terminal, review in browser
- Channels — Telegram/Discord/iMessage into session
- Dispatch — phone message → spawn Desktop session
- Authentication / CLI reference / Security / Data usage
