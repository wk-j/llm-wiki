---
title: "บทบาทของวิศวกรซอฟต์แวร์ในยุค AI"
type: source
tags: [ai, software-engineering, career, roles, thai]
created: 2026-04-15
updated: 2026-04-15
sources: [software-engineer-role-ai-era.md]
---

# บทบาทของวิศวกรซอฟต์แวร์ในยุค AI

Thai-language blog post arguing that software engineering roles are not disappearing under AI, but **shifting outward from the middle** — toward upstream framing and downstream verification — while the middle (boilerplate, basic CRUD, routine logic) is absorbed.

Source was pasted in as content; no URL provided.

## Core thesis

Work splits in two directions at once:

- **ต้นน้ำ (upstream):** more time on requirements gathering, architecture, and problem definition.
- **ปลายน้ำ (downstream):** more time on reviewing, evaluating, and controlling AI output.
- **The middle shrinks:** boilerplate, CRUD scaffolding, and routine logic get automated.

See [[engineering-role-shift]] for the pattern generalized.

## Six new roles

| # | Thai | English | Core responsibility |
|---|---|---|---|
| 1 | ผู้ควบคุม AI | [[ai-orchestrator\|AI Orchestrator]] | Design and direct pipelines of AI agents |
| 2 | สถาปนิกระบบ | Systems Architect | Decide *what* to build and *why* — structure, data flow, integration |
| 3 | ผู้คุมคุณภาพ | Quality Gatekeeper | Catch silent bugs, security holes, architectural misfits in AI output |
| 4 | นักแปลความต้องการ | [[domain-to-ai-translator\|Domain-to-AI Translator]] | Convert fuzzy business requirements into AI-executable specs |
| 5 | ผู้สร้างเครื่องมือ AI | AI Tool Builder | Build RAG systems, agent frameworks, [[model-context-protocol\|MCP]] servers, eval pipelines |
| 6 | ผู้ดูแลความปลอดภัย | Governance & Safety Owner | Ensure AI systems meet regulatory and risk requirements |

The post calls out **Domain-to-AI Translator** (#4) as the hardest role for AI itself to replace — the skill of turning ambiguous real-world requirements into precise specifications.

## Skills ranked up vs. down

| Replaced by AI | More valuable |
|---|---|
| Writing boilerplate | System design |
| Memorizing syntax | Problem analysis |
| Basic CRUD work | Domain knowledge |
| Repetitive refactoring | Architectural judgment |
| Routine test writing | Debugging complex issues |

## Closing line

> วิศวกรซอฟต์แวร์ในยุค AI ไม่ใช่แค่ผู้เขียนโค้ดอีกต่อไป แต่เป็นนักคิดเชิงระบบที่กำกับเครื่องมืออัจฉริยะ — ฝีมือเปลี่ยนจากการจำ syntax ไปสู่การใช้วิจารณญาณ

*Software engineers in the AI era are no longer just code writers, but systems thinkers directing intelligent tools — craft shifts from memorizing syntax to applying judgment.*

## Takeaways

- The "engineers are obsolete" framing is rejected; replaced with a bimodal shift (upstream + downstream grow; middle shrinks).
- Taste, judgment, and domain fluency are the compounding skills. Syntax recall and scaffolding speed are not.
- The Tool Builder role (#5) aligns with the growing infrastructure layer around LLMs — agent frameworks, [[model-context-protocol|MCP]], evals.
- Overlaps with [[llm-coding-pitfalls]]: Quality Gatekeeper exists because AI output "looks confident but fails silently" — the same failure mode [[andrej-karpathy|Karpathy]] documented.

## See also

- [[engineering-role-shift]]
- [[ai-orchestrator]]
- [[domain-to-ai-translator]]
- [[llm-coding-pitfalls]]
- [[model-context-protocol]]
