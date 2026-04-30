---
title: "Zed is 1.0"
type: source
tags: [zed, editor, ai, rust, collaboration, deltadb, gpui]
created: 2026-04-29
updated: 2026-04-29
sources: [Zed is 1.0.md]
---

# Zed is 1.0

Official blog post from Zed Industries announcing the 1.0 release of the [[zed]] editor. This milestone marks the maturity of their custom-built, high-performance foundations and their shift towards an AI-native, collaborative future.

## Key Takeaways

### Foundational Architecture
- **Rejecting Electron**: Zed moves away from the web-technology stack (Chromium/Electron) used in [[atom]] and [[vscode]] to overcome performance ceilings.
- **Video Game Engine Design**: Built "like a video game" to feed data directly to GPU shaders.
- **GPUI Framework**: A custom UI framework built from scratch in [[rust]] for extreme performance and deep stack ownership.

### AI-Native Editor
- **Foundation vs. Bolt-on**: AI is built into the editor's core primitives rather than as a plugin.
- **Parallel Agents**: Support for running multiple agents simultaneously.
- **Agent Client Protocol (ACP)**: An open protocol allowing users to bring their own agents (e.g., [[claude]], Codex, [[opencode]], Cursor) into Zed.
- **Edit Prediction**: Keystroke-level suggestions for the next code change.

### The Future of Collaboration
- **Human-Agent Collaboration**: Shifting from real-time human collaboration to a model where humans and AI agents work in the same shared space.
- **DeltaDB**: A new synchronization engine built on [[crdts]] to track character-level changes across the codebase.
- **Team Integration**: Allows teammates to join conversations with agents to review and evolve agentic code in context.

### Business & Maturity
- **Zed for Business**: Launching features for engineering teams, including centralized billing and RBAC.
- **Multi-Platform**: Reached 1.0 maturity across macOS, Windows, and Linux.

## Key Entities & Concepts Mentioned
- [[zed]] — The high-performance editor.
- [[gpui]] — The custom UI framework.
- [[deltadb]] — The CRDT-based sync engine.
- [[agent-client-protocol]] — Open standard for agent integration.
- [[zed-industries]] — The company behind Zed.
