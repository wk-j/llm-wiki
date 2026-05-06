---
title: Agentic Coding is a Trap
type: source
tags: [agentic-coding, psychology, developer-experience, ai]
url: https://larsfaye.com/articles/agentic-coding-is-a-trap
date_ingested: 2026-05-05
created: 2026-05-05
updated: 2026-05-05
sources: []
---

# Agentic Coding is a Trap

A critical essay by [[lars-faye]] warning against the over-reliance on autonomous coding agents (Agentic Coding) and the "Spec Driven Development" (SDD) trend. The central thesis is that delegating the actual writing of code to AI models creates a dangerous disconnect between the developer and the codebase, leading to [[skill-atrophy]] and [[cognitive-debt]].

## Key Takeaways

- **The Supervision Paradox:** Effectively supervising and orchestrating agents requires deep coding skills and critical thinking—the exact skills that atrophy when developers stop wrestling with code directly.
- **Not Just Another Abstraction:** Unlike moving from Assembly to C, which raised the level of abstraction deterministically, moving to LLMs introduces probabilistic ambiguity. The mental fog reported by developers is real and documented, not just resistance to change.
- **Coding is Planning:** For many developers (including [[dax|Dax]], creator of [[opencode]]), the act of writing code is the process of figuring out the architecture and constraints. Forcing these developers to write giant specs upfront breaks their natural workflow.
- **Vendor Lock-In on Skills:** Over-reliance on subsidized AI models creates a dangerous [[vendor-lock-in]]. If the models get "nerfed", have an outage, or prices skyrocket (due to [[usage-based-billing]]), entire teams can come to a standstill.
- **The Ship's Computer Model:** The author advocates demoting AI from "orchestrated worker" to a secondary process (like the Ship's Computer in Star Trek). The human should stay engaged with implementation, manually coding 20%-100% of the task, and using AI for ad-hoc generation, research, and interactive documentation.
- **Review Limit:** Never ask an agent to generate more code than you can thoroughly review in one sitting.

## See also

- [[agentic-engineering]]
- [[vibe-coding]]
- [[taste-paradox]]
- [[eh-gland]]
- [[simon-willison]]
