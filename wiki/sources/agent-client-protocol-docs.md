---
title: Agent Client Protocol (ACP) Official Documentation
type: source
tags: [ai, protocol, coding, standard, zed, jetbrains]
created: 2026-04-26
updated: 2026-04-26
sources: [https://agentclientprotocol.com]
---

# Agent Client Protocol (ACP) Official Documentation

The official website for the **Agent Client Protocol (ACP)**, an open standard for communication between AI agents and code editors.

## Key Technical Specifications

### Architecture
- **Local Agents:** Run as sub-processes. Communication via **JSON-RPC 2.0 over stdio**.
- **Remote Agents:** Communication via **HTTP or WebSocket** (WIP).
- **Format:** Uses **Markdown** for text communication.
- **MCP Compatibility:** Re-uses **Model Context Protocol (MCP)** JSON representations where possible.

### Core Protocol Lifecycle
1. **Initialization:** Handshake between client (IDE) and agent.
2. **Session Management:** Creation and listing of interaction sessions.
3. **Prompt Turns:** The main loop of conversation and tool execution.

### Capabilities
- **Standardized Tools:** Support for file system access, terminal interaction, and multi-file editing.
- **Live Proposals:** Custom types for displaying and applying diffs directly in the editor UI.
- **Agent Following:** Capabilities for the editor to track agent actions across files.

## Ecosystem
- **Editors:** Zed, JetBrains IDEs, Neovim, Emacs.
- **Agents:** Gemini CLI, Claude Code, GitHub Copilot CLI.
- **SDKs:** TypeScript (@agentclientprotocol/sdk), Python, Rust, Java, Kotlin.
