---
title: "Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI"
type: source
tags: [ai, software-engineering, agents, harness-engineering, openai]
url: https://www.youtube.com/watch?v=am_oeAoUhew
date_ingested: 2026-04-28
created: 2026-04-28
updated: 2026-04-28
sources: []
---

# Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI

Ryan Lopopolo from [[openai]] presents a vision for software engineering where humans focus on steering and systems design, while agents handle 100% of the implementation. He advocates for "Harness Engineering" — building the automated guardrails that allow agents to operate autonomously at scale.

## Key Takeaways

### 1. Code is Free
- Implementation, refactoring, and deletion are no longer scarce resources because agents can perform them in parallel at infinite scale.
- The real constraints are **human time**, **attention**, and **model context**.
- Code should be treated as a "disposable build artifact" compiled from specifications (prompts and guardrails).

### 2. Token Billionaires
- Reaching AGI requires leaning into the idea that models can do the "full job."
- Ryan's team is banned from touching editors directly; they must work through agents to internalize a Staff Engineer mindset.
- High token consumption (1B+ output tokens/day) is a sign of high leverage and automation.

### 3. Durable Feedback Loops
- Instead of manually fixing agent errors (slop), engineers should convert feedback into permanent system constraints.
- Fixes should be encoded as **Lint Rules**, **Tests**, or **Documentation** that agents read and follow.
- This eliminates "durable classes of failures" systematically.

### 4. Just-in-Time Context
- Avoid frontloading all instructions into the prompt (which wastes context and causes noise).
- Use **Reviewer Agents** or **Lint/Test failures** to provide specific remediation steps only when the agent fails or reaches a validation gate.
- This allows agents to "self-heal" without human intervention.

### 5. Reviewer Personas
- Deploy specialized agents (e.g., Security, Reliability, Architect) to review every push.
- These agents assert expectations based on the team's written "Acceptance Criteria."

## Notable Quotes
- "Implementation is no longer the scarce resource... Code is free."
- "Every time I have to type 'continue' to the agent is a failure of the harness."
- "You can just simply say 'do not produce slop.' Don't accept slop. You won't get slop in your codebase."

## See also
- [[harness-engineering]]
- [[ryan-lopopolo]]
- [[openai]]
- [[code-is-free]]
- [[token-billionaire]]
- [[just-in-time-context]]
