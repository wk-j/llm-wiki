---
title: "Andrej Karpathy: From Vibe Coding to Agentic Engineering"
type: source
tags: [ai, agents, engineering, vibe-coding, software-3-0]
created: 2026-04-30
updated: 2026-04-30
sources: [https://www.youtube.com/watch?v=96jN2OCOfLs]
---

# Andrej Karpathy: From Vibe Coding to Agentic Engineering

Andrej Karpathy (co-founder of OpenAI, former head of AI at Tesla, and now founder of Eureka Labs) talks with Sequoia partner Stephanie Zhan at AI Ascent 2026 about the shift from "vibe coding" to "agentic engineering."

## Key Takeaways

### Vibe Coding vs. Agentic Engineering
- **Vibe Coding**: Raising the floor for everyone. It allows people who aren't traditional programmers to build software by "vibing" with the model.
- **Agentic Engineering**: Preserving the quality bar of professional software while gaining massive speedups (10x+). It is an engineering discipline involving the coordination of powerful but "jagged" agents.
- The transition happened around December 2025/2026 when models started producing complex chunks of code correctly without human intervention.

### Software 3.0
- **Software 1.0**: Explicit rules (writing code).
- **Software 2.0**: Learned weights (programming by data sets and architectures).
- **Software 3.0**: Programming by prompting. The context window is the lever over the LLM interpreter.
- Example: "Agents as the Installer." Instead of a complex bash script, the installation process is a set of instructions given to an agent that debugs and adapts to the local environment.

### Jagged Intelligence (Animals vs. Ghosts)
- LLMs are **"Jagged Entities"**: They can refactor 100k lines of code or find zero-day vulnerabilities but fail at simple logic like "strawberry letters" or "car wash distance" (walking vs. driving).
- **Ghosts, not Animals**: LLMs are statistical simulation circuits "summoned" via prompts. They lack intrinsic motivation, curiosity, or "animal" intelligence.
- This jaggedness comes from what is **verifiable** and what the labs choose to put into the Reinforcement Learning (RL) data distribution.

### The Human Role: Director of Taste
- Humans move from "implementers" to "directors."
- **Outsource thinking, not understanding**: You can let agents handle the "how" (API details, specific logic), but the human must still provide the "what" and "why" (spec, taste, judgment, aesthetics).
- Understanding remains the bottleneck for directing agents effectively.

### Agent-Native Infrastructure
- Current infrastructure (docs, APIs, deployment) is written for humans.
- Future infrastructure should be **Agent-Native**: Sensor/actuator abstractions and data structures legible to LLMs.
- Example: Deploying should be a prompt, not manual configuration of DNS/Vercel settings.

## Notable Quotes
- "You can outsource your thinking, but you can't outsource your understanding."
- "The neural net becomes the host process and the CPUs become the co-processor."
- "I've never felt more behind as a programmer."

## Related
- [[andrej-karpathy]]
- [[vibe-coding]]
- [[agentic-engineering]]
- [[software-3-0]]
- [[jagged-intelligence]]
- [[verifiability]]
