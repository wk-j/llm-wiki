---
title: "OpenCode vs Claude Code (2026): Open Source Freedom vs Anthropic Polish"
source: "https://www.morphllm.com/comparisons/opencode-vs-claude-code"
author:
  - "[[Morph Team]]"
published: 2026-02-28
created: 2026-04-20
description: "112K vs 71K GitHub stars. Anthropic's OAuth block, OpenCode Black, desktop apps, and 4% of all GitHub commits. Full 2026 feature comparison."
tags:
  - "clippings"
---
## TL;DR: The Quick Answer

#### The One-Sentence Verdict

**OpenCode** = Open source + 75 providers + desktop app + 2.5M monthly devs.  
**Claude Code** = Proprietary + Anthropic-only + 4% of all GitHub commits + production polish.

OpenCode has pulled far ahead on GitHub stars (112K vs 71K as of February 2026), but Claude Code dominates actual usage: 4% of all public GitHub commits, 135K per day. The architectures couldn't be more different. Claude Code is a vertical integration masterpiece. OpenCode is a horizontal flexibility play. And since Anthropic's January 2026 OAuth block, the relationship between them is now openly adversarial.

## GitHub Stars: The 112K vs 71K Battle

![OpenCode terminal interface showing an AI coding agent working on a codebase with Claude Opus 4.5](https://www.morphllm.com/news/opencode-terminal-ui.png)

OpenCode's terminal UI. Source: github.com/anomalyco/opencode

OpenCode (now under [anomalyco/opencode](https://github.com/anomalyco/opencode) after SST rebranded to Anomaly) has more than doubled its stars since January. At 112,837 stars, 779 contributors, and 80 releases in Jan+Feb 2026 alone, the velocity is staggering. Claude Code sits at 71,500 stars, but the more telling metric is commit share: 4% of all public GitHub commits (135K/day), projected to hit 20%+ by end of 2026 according to SemiAnalysis.

| Metric | OpenCode | Claude Code |
| --- | --- | --- |
| GitHub Stars | 112,837 | ~71,500 |
| Contributors | 779 | Anthropic team |
| Latest Version | v1.2.15 (Feb 26, 2026) | v2.1.63 (Feb 28, 2026) |
| License | MIT (open source) | Proprietary |
| Primary Language | TypeScript (84%) | TypeScript/Node.js |
| Monthly Active Devs | 2.5M | Not disclosed (4% of GH commits) |
| Release Cadence | 80 releases in 2 months | Regular (versioned) |

![Claude Code GitHub commits over time showing 135K+ daily commits, approximately 4% of all public GitHub commits](https://www.morphllm.com/images/claude-code-github-commits-chart.png)

Source: SemiAnalysis / GitHub Search API. Claude Code now accounts for ~4% of all public GitHub commits.

### The Anthropic OAuth Block: The Watershed Moment

On January 9, 2026, Anthropic silently blocked OpenCode from using Claude via consumer OAuth tokens. OpenCode removed Claude Pro/Max support from the codebase, citing "anthropic legal requests." The developer backlash on Hacker News was immediate and fierce.

OpenCode responded by launching Black, an enterprise API gateway with $20/$100/$200/mo tiers. They also launched Zen, a pay-as-you-go curated gateway. OpenAI publicly welcomed third-party tools as counter-positioning, calling out Anthropic's approach by name.

This event split the community. Developers who valued provider freedom rallied around OpenCode. Developers who wanted the tightest possible model integration stayed with Claude Code. The coexistence period is over.

## System Prompt Deep Dive

We extracted Claude Code's system prompts from the compiled source code. Here's what powers each tool's "brain."

### Claude Code System Prompt Architecture

Claude Code v2.1.63 uses a modular prompt system with 40+ components totaling thousands of tokens:

#### Claude Code Prompt Structure (Extracted)

```
// Claude Code System Prompt Components
├── Core System Prompt (2,896 tokens)
│   ├── Identity & capabilities
│   ├── Tool usage instructions
│   └── Response formatting rules
│
├── Subagent Prompts
│   ├── Plan Mode Enhanced (633 tokens)
│   ├── Explore Agent (516 tokens)
│   └── Task Tool (294 tokens)
│
├── Tool Descriptions (20 built-in tools)
│   ├── Write, Read, Edit, Bash
│   ├── Task, TodoWrite, Glob, Grep
│   ├── WebFetch, WebSearch
│   └── NotebookEdit, KillShell, etc.
│
├── Utility Prompts
│   ├── Conversation summarization
│   ├── Session management
│   ├── CLAUDE.md creation (384 tokens)
│   ├── Security review (2,610 tokens)
│   └── Agent creation architect (1,110 tokens)
│
└── Slash Command Prompts
    ├── /pr-comments (402 tokens)
    ├── /review-pr (243 tokens)
    └── /security-review (2,610 tokens)
```

### OpenCode System Prompt Architecture

OpenCode uses a file-based prompt system with YAML frontmatter:

#### OpenCode Agent Configuration

```
# .opencode/agents/build.md (Primary Agent)
---
name: build
description: Default agent for development work
mode: primary
model: anthropic/claude-sonnet-4  # Or any provider
temperature: 0.7
tools:
  write: true
  edit: true
  bash: true
  webfetch: true
  task: true
  todo: true
permission:
  edit: allow
  bash: ask
  webfetch: allow
maxSteps: 50
---

You are a coding assistant focused on software development.
[Custom instructions follow...]

# .opencode/agents/plan.md (Read-only Agent)
---
name: plan
description: Analysis and exploration agent
mode: primary
permission:
  edit: deny
  bash: ask
---

You are an analyst. Read code, explain patterns,
but do not modify files unless explicitly asked.
```

#### The Customization Gap

**Claude Code**: Core prompts are baked in. You can add instructions via CLAUDE.md and auto-memory persists across sessions, but you cannot modify the 2,896-token core prompt without third-party tools like `tweakcc`.  
  
**OpenCode**: Everything is a markdown file. Drop new agents in `.opencode/agents/` and they're instantly available. v1.2.0 migrated session storage to SQLite (replacing flat files), and the Tauri desktop app ships on macOS/Windows/Linux. ACP integration with Zed and JetBrains is now official.

## Tool Definitions: 20+ Tools Compared

Claude Code ships with 20 built-in tools. OpenCode has a similar core set but approaches extensibility differently.

### Claude Code Built-in Tools (Extracted)

#### Claude Code Tool Inventory

```
// Claude Code v2.1.63 Built-in Tools
const CLAUDE_CODE_TOOLS = [
  // File Operations
  "Read",           // Read files with line ranges
  "Write",          // Create/overwrite files
  "Edit",           // Search-replace edits
  "Glob",           // Find files by pattern
  "Grep",           // Search file contents

  // Execution
  "Bash",           // Execute shell commands
  "KillShell",      // Terminate running shells
  "NotebookEdit",   // Edit Jupyter notebooks

  // Agent System
  "Task",           // Spawn subagents
  "TodoWrite",      // Track task progress

  // Web & External
  "WebFetch",       // Fetch web content
  "WebSearch",      // Search the web

  // IDE Integration
  "AskUserQuestion", // Request user input
  "EnterPlanMode",   // Switch to planning
  "ExitPlanMode",    // Exit planning

  // MCP Tools
  "mcp__*",         // Dynamically loaded MCP tools
];
```

### OpenCode Built-in Tools

#### OpenCode Tool Inventory

```
// OpenCode Built-in Tools
const OPENCODE_TOOLS = [
  // File Operations
  "read",           // Read files with line ranges
  "write",          // Create/overwrite files
  "edit",           // Search-replace edits
  "glob",           // Find files by pattern
  "grep",           // Search with ripgrep

  // Execution
  "bash",           // Execute shell commands

  // Agent System
  "task",           // Spawn subagents
  "todo",           // Track task progress
  "skill",          // Load reusable instruction sets

  // Web
  "webfetch",       // Fetch and process web content

  // MCP Tools
  "mcp_*",          // Declaratively configured MCP tools
];
```

| Tool Category | Claude Code | OpenCode |
| --- | --- | --- |
| File editing | Edit (search-replace) | edit (search-replace) |
| Web search | WebSearch (built-in) | Via MCP |
| Notebook support | NotebookEdit (native) | Via MCP |
| Skill system | Skills folder | skill tool (native) |
| LSP integration | Limited | Out-of-the-box |
| MCP loading | Eager (all at once) | Declarative (per-agent) |

### The MCP Tool Search Revolution

Anthropic recently released MCP Tool Search for Claude Code, introducing "lazy loading" for tools. This reduced token usage from ~134K to ~5K in their testing. OpenCode has always used declarative tool loading:

#### MCP Tool Configuration Comparison

```
// Claude Code: MCP tools via mcp.json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    }
  }
}
// All tools loaded into context at startup
// New: Tool Search enables lazy loading

// OpenCode: Declarative per-agent control
// opencode.json
{
  "tools": {
    "mymcp_*": true,          // Enable for all agents
    "dangerous_tool": false   // Disable globally
  },
  "agent": {
    "build": {
      "tools": {
        "mymcp_write": true,
        "mymcp_delete": false  // Disable for this agent
      }
    }
  }
}
```

## Subagent Architecture Analysis

This is where the tools diverge most dramatically. Claude Code ships with **native, production-grade subagents** (Plan, Explore, Task) tuned for Anthropic models. OpenCode treats agents as **user-configurable YAML files** with superior interactivity but less out-of-box polish.

#### The Key Trade-off

**Claude Code**: Native Explore subagent that "just works" for codebase navigation. No configuration needed.  
  
**OpenCode**: Tab to switch agents, @mention to invoke subagents, HTTP API for remote control. More interactive, but you configure the agents yourself.

### Claude Code Subagent System (Native)

#### Claude Code Agent Hierarchy

```
// Claude Code Subagent Architecture
Primary Context
│
├── Plan Mode (633 tokens prompt)
│   ├── Triggered via /plan or EnterPlanMode tool
│   ├── Read-only by default
│   ├── Outputs plan to file for approval
│   └── Exits with ExitPlanMode tool
│
├── Explore Agent (516 tokens prompt)
│   ├── Fast codebase navigation
│   ├── Read-only access
│   └── Returns findings to parent
│
├── Task Agent (294 tokens prompt)
│   ├── Complex multi-step workflows
│   ├── Own context window
│   ├── Can run in background
│   └── Results summarized to parent
│
└── Custom Agents (user-defined)
    ├── Defined in .claude/agents/
    └── Inherit tool access from config

// Key Feature: Checkpoint System
// Esc twice = instant rewind to last checkpoint
// Unique to Claude Code, not available in OpenCode
```

### OpenCode Subagent System (User-Configurable)

#### OpenCode Agent Hierarchy + Interactivity

```
// OpenCode Agent Architecture
// KEY ADVANTAGE: Superior interactivity

Primary Agents (Tab to switch instantly)
├── Build Agent (default)
│   ├── All tools enabled
│   ├── Full filesystem access
│   └── For development work
│
└── Plan Agent
    ├── Read-only by default
    ├── Asks permission for bash
    └── For analysis/exploration

// INTERACTIVITY FEATURES:
// 1. Tab - instant agent switching
// 2. @agent_name - invoke any subagent inline
// 3. HTTP API - control from mobile/remote
// 4. Persistent sessions - survives terminal close

Subagents (via Task tool or @mention)
├── @general - Complex multi-step tasks
├── @explore - Read-only codebase navigation
└── @custom - Your own agents from .opencode/agents/

// Example: Mobile workflow
$ curl http://localhost:7860/api/message \
  -d '{"message": "@explore find auth handlers"}'
// Review results on phone, continue on laptop
```

Native Explore subagent

OpenCode

Claude Code

Interactive agent switching

OpenCode

Claude Code

Checkpoint/Undo system

OpenCode

Claude Code

Remote/mobile control

OpenCode

Claude Code

#### Claude Code's Killer Features

**Native Explore subagent:** Claude Code's Explore agent (516-token prompt) is production-tuned for codebase navigation. It "just works" without configuration, crucial for quickly understanding unfamiliar codebases.  
  
**Instant rewind:** Esc twice to restore to the last checkpoint. When an agent goes off-track, you instantly recover. OpenCode has no equivalent. You're stuck with manual git operations.

#### OpenCode's Killer Feature: Interactivity

**Tab switching:** Instantly swap between Build and Plan agents without commands.  
**@mentions:** Invoke any subagent inline with `@explore`, `@general`, or custom agents.  
**HTTP API:** Control sessions from mobile, tablets, or remote machines. Start a task at your desk, review on your phone.

## Context Management & Compaction

Long coding sessions require sophisticated context management. Without it, [context rot](https://www.morphllm.com/context-rot) degrades agent performance as earlier instructions get pushed out. Both tools handle this differently, and tools like [FlashCompact](https://www.morphllm.com/flashcompact) can accelerate [context compression](https://www.morphllm.com/context-compression) regardless of which agent you use.

### Claude Code Context Strategy

#### Claude Code Context Management

```
// Claude Code uses automatic compaction
// Triggered near context limit

// Compaction process:
1. Detect approaching context limit
2. Summarize previous messages (utility prompt)
3. Preserve critical context (file contents, etc.)
4. Continue with reduced token count

// Manual compaction:
$ /compact     # Slash command to force compaction

// Context advice from Anthropic:
// "If using Claude in an agent harness that compacts context,
// add this to your prompt so Claude can behave accordingly.
// Otherwise Claude may try to wrap up work as it
// approaches the context limit."
```

### OpenCode Context Strategy

#### OpenCode Context Management

```
// OpenCode uses Vercel AI SDK's context handling
// Provider-dependent behavior

// Session persistence:
// - Server-side state via Hono HTTP API
// - Sessions survive terminal closure
// - Can reconnect from mobile app

// Manual summarization:
// No built-in /compact equivalent
// Rely on starting new sessions for clean context

// LSP Integration:
// - Automatic symbol awareness
// - Language-specific context enrichment
// - Better code navigation than text-based approaches
```

| Feature | Claude Code | OpenCode |
| --- | --- | --- |
| Auto-compaction | Yes (built-in) | Provider-dependent |
| Manual compaction | /compact command | Not available |
| Session persistence | In-session only | Server-side (survives close) |
| LSP awareness | Limited | Native integration |

## Permission & Security Models

How each tool handles dangerous operations reveals their security philosophies.

### Claude Code Permission System

#### Claude Code Permission Configuration

```
// claude.permissions in settings.json
{
  "claude.permissions": {
    "edit": "ask",           // ask | allow | deny
    "bash": "ask",
    "bash.rm": "deny",       // Specific command patterns
    "bash.git": "allow",
    "webfetch": "allow"
  }
}

// Permission flow:
1. Tool call requested
2. Check permission config
3. If "ask": Show confirmation dialog
4. If "allow": Execute immediately
5. If "deny": Block with error

// Dangerous operation detection:
// Built-in heuristics for destructive commands
// Even with "allow", warns on rm -rf /, etc.
```

### OpenCode Permission System

#### OpenCode Permission Configuration

```
// opencode.json permission configuration
{
  "permission": {
    "edit": "allow",
    "bash": {
      "*": "ask",              // Default: ask for all
      "git *": "allow",        // Allow git commands
      "npm test": "allow",
      "npm install": "ask",
      "rm -rf *": "deny",      // Block dangerous patterns
      "sudo *": "deny"
    },
    "webfetch": "allow",
    "task": {
      "general": "allow",
      "explore": "allow",
      "custom-*": "ask"
    },
    "skill": {
      "pr-review": "allow",
      "dangerous-*": "deny"
    }
  }
}

// Permission inheritance:
// Agent-specific overrides in frontmatter
// Last matching glob pattern wins
```

#### Security Philosophy Difference

**Claude Code** assumes you want protection by default, with explicit allows. Better for teams with mixed trust levels.  
  
**OpenCode** assumes power users who want granular control via glob patterns. More flexible but requires careful configuration.

## MCP Integration Patterns

Both tools support the Model Context Protocol, but with different loading strategies.

### Claude Code MCP Approach

- **Eager loading**: All MCP tools loaded at startup (changing with Tool Search)
- **Token cost**: ~134K tokens with many MCPs (reduced to ~5K with Tool Search)
- **Configuration**: `mcp.json` in project root
- **Server types**: Supports stdio and HTTP MCP servers

### OpenCode MCP Approach

- **Declarative loading**: Tools loaded per-agent based on config
- **Glob patterns**: `mymcp_*: true` enables all tools from an MCP
- **Configuration**: `opencode.json` or `opencode.jsonc`
- **Context efficiency**: Only configured tools enter context

#### MCP Configuration Comparison

```
// Claude Code: mcp.json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": { "DATABASE_URL": "..." }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}

// OpenCode: opencode.json
{
  "mcp": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": { "DATABASE_URL": "..." }
    }
  },
  "agent": {
    "build": {
      "tools": {
        "postgres_query": true,
        "postgres_execute": false  // Read-only for this agent
      }
    }
  }
}
```

## Performance Benchmarks

Real-world task benchmarks reveal practical differences.

| Task | OpenCode | Claude Code |
| --- | --- | --- |
| Cross-file refactor | ✓ Correct, 4m 20s | ✓ Correct, 2m 15s |
| Bug fix from error | ✓ Correct, 3m 10s | ✓ Correct, 1m 45s |
| Test generation | 94 tests, 8m 50s | 73 tests, 5m 9s |
| Total time | 16m 20s | 9m 9s |
| Code reformatting bugs | Yes (all 3 models) | No |

Claude Code completes tasks ~45% faster, but OpenCode generates ~29% more tests. The reformatting bug ("All three models tested with OpenCode tried to reformat existing code") suggests a harness-level issue, not model quality.

### Formal Benchmarks (February 2026)

Claude Code with WarpGrep v2 now hits 57.5% on SWE-bench Pro and 68.8% on ARC-AGI-2 (nearly 2x improvement over prior scores). The 100K-line C compiler demo (16 agents, $20K in API costs) demonstrated multi-agent orchestration at a scale nobody else has publicly replicated. Anthropic ($380B valuation, $14B ARR) is investing heavily in making Claude Code the default developer interface.

### Token Efficiency

Claude Code's model-specific optimization shows in token usage:

57.5%

SWE-bench Pro (CC)

68.8%

ARC-AGI-2 (CC)

135K/day

CC GitHub Commits

~29%

OC test coverage gain

## The Pricing Reality

![OpenAI and Anthropic quarterly ARR comparison showing the Claude Code moment accelerating Anthropic's revenue](https://www.morphllm.com/news/anthropic-arr-growth.png)

Source: SemiAnalysis. Anthropic's ARR growth accelerated sharply at the "Claude Code Moment." This revenue trajectory shapes the pricing dynamics between OpenCode (free/BYOK) and Claude Code (subscription).

This is where OpenCode has an unassailable advantage.

| Aspect | OpenCode | Claude Code |
| --- | --- | --- |
| Tool cost | Free (MIT license) | Free |
| Model access | BYOK + Black ($20/$100/$200/mo) + Zen (pay-as-you-go) | $20-200/mo Anthropic |
| Total minimum cost | $0 (with free tiers or local models) | $20/month |
| Enterprise option | Self-hosted or Black gateway | Anthropic Enterprise |
| Local model support | Yes (Ollama) | No |
| Desktop app | Yes (Tauri: macOS/Win/Linux) | VS Code extension (5.2M installs) |

#### Post-OAuth Block Pricing Landscape

After Anthropic blocked consumer OAuth access, OpenCode launched Black ($20/$100/$200/mo) and Zen (pay-as-you-go) as first-party model gateways. Users can also bring their own API keys from any provider, use free tiers, or run local models. Claude Code requires a $20/month Claude Pro subscription at minimum, with heavy users on $100-200/month tiers. New providers like Kilo and Venice give OpenCode users more options. Claude Code counters with VS Code integration (5.2M installs, 4.0/5 rating) and remote control from mobile via QR scan.

## Decision Framework

🌐

### OpenCode

The open-source multi-provider rebel

Provider Freedom

75+ providers + local

Interactivity

Tab switch, @mentions, HTTP API

Native Subagents

User-defined agents

Checkpoint/Undo

Manual git only

Ecosystem Lock-in

None (BYOK)

Best For

Multi-provider setupsLocal modelsRemote/mobile controlCustom workflows

"Best interactivity, bring your own everything."

🎯

### Claude Code

Anthropic's polished ecosystem play

Provider Freedom

Anthropic only

Interactivity

Slash commands only

Native Subagents

Plan, Explore, Task built-in

Checkpoint/Undo

Instant rewind (Esc×2)

Ecosystem Lock-in

Full Anthropic lock

Best For

Codebase explorationEnterprise teamsComplex refactoringNiche languages

"Native Explore agent + instant undo = polish."

| Your Priority | Best Choice | Why |
| --- | --- | --- |
| Use multiple AI providers | OpenCode | 75+ providers vs Anthropic-only |
| Maximum polish & reliability | Claude Code | Production-grade UX |
| Local model support | OpenCode | Native Ollama integration |
| Instant undo/rewind | Claude Code | Checkpoint system (Esc×2) |
| Cost optimization | OpenCode | Free tool + BYOK |
| Deterministic outputs | Claude Code | Claude model consistency |
| Remote/mobile control | OpenCode | Client/server architecture |
| Enterprise compliance | Depends | Claude for support, OpenCode for self-host |

> "TL;DR: if you have time to experiment, use OpenCode with sonnet-4. Otherwise, use Claude Code."

## Frequently Asked Questions

### Is OpenCode or Claude Code better for coding in 2026?

Claude Code if you want Anthropic's polish, SWE-bench Pro 57.5% accuracy, and the tool behind 4% of all GitHub commits. OpenCode if you want provider freedom, 2.5M monthly active developers worth of community support, and a desktop app. After the January 2026 OAuth block, the choice is also political: open ecosystem vs. vertically integrated.

### What are the differences in system prompts?

Claude Code uses a 2,896-token core system prompt with 20 built-in tool descriptions and specialized subagent prompts (Plan: 633 tokens, Explore: 516 tokens, Task: 294 tokens). OpenCode uses modular markdown-based prompts stored in `.opencode/agents/` with YAML frontmatter for configuration, allowing complete customization.

### Which has better tool support?

Claude Code has 20 built-in tools including Write, Read, Edit, Bash, Task, TodoWrite, and more. OpenCode has similar core tools but treats MCP tools more declaratively. Both support MCP extensibility, but Claude Code's tools are more tightly integrated with its checkpoint system.

### Can I use Claude models with OpenCode?

Only via API keys. In January 2026, Anthropic blocked OpenCode from using Claude through consumer OAuth tokens. OpenCode removed Claude Pro/Max support, citing "anthropic legal requests." You can still use Claude through direct API keys or through OpenCode Black/Zen gateways, but consumer subscription access is gone. OpenCode also added adaptive thinking support for Claude Sonnet 4.6 and Opus 4.6 for API key users.

### Supercharge Any AI Coding Agent with Morph

Whether you use OpenCode, Claude Code, or Codex, Morph Fast Apply processes your code edits 100x faster with 98% first-pass accuracy. Works with any harness, any provider.