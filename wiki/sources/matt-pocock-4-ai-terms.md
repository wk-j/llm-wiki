---
title: 4 of the most confusing terms in AI, defined
type: source
tags: [ai, architecture, definitions, agents]
created: 2026-05-04
updated: 2026-05-04
sources: [Matt Pocock - 4 AI Terms Defined.md]
---

# 4 of the most confusing terms in AI, defined / นิยาม 4 คำศัพท์ AI ที่น่าสับสนที่สุด

Source: [[matt-pocock|Matt Pocock]] (@mattpocockuk)
Date: 2026-05-04

Matt Pocock provides a crisp structural definition of the relationship between models and agents, clarifying how the same model can result in different agents depending on its implementation.

## Key Definitions

### 1. Model (ตัวโมเดล)
- **What it is**: A blob of parameters written during training.
- **Function**: Performs next-token prediction and nothing else.
- **Nature**: Stateless.
- **Example**: Claude 3.5 Opus is a model.

### 2. Harness (ตัวครอบ/ระบบสนับสนุน)
- **What it is**: Everything surrounding the model that enables it to function as an agent.
- **Components**: Tools, system prompt, context window management, session handling.
- **Importance**: It is the "wrapping" that provides state and capability to the stateless model.

### 3. Environment (สภาพแวดล้อม)
- **What it is**: The external world the agent acts upon.
- **Interaction**: Anything outside the harness that the agent perceives and acts on via tools.
- **Examples**: The file system, MCP servers (which add tools to the environment).

### 4. Agent (เอเจนท์)
- **The Formula**: `Agent = Model + Harnessed + In an Environment`
- **Distinction**: The same model (e.g., Opus) becomes different agents when paired with different harnesses (e.g., Claude Code vs. Claude Web).

## Key Takeaways

- **The Harness defines the Agent**: Since the model is stateless and fixed, the identity and capabilities of an agent are primarily determined by its harness.
- **Tools are part of the Environment/Harness interface**: MCP servers bridge the agent's harness to the environment by providing tools.
- **Stateless vs. Stateful**: Models are stateless; the state (memory, context, tools) is managed by the harness.

## See also

- [[coding-harness]]
- [[harness-engineering]]
- [[agentic-engineering]]
- [[model-context-protocol]]
