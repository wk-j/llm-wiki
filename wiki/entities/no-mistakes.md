---
title: No Mistakes
type: entity
tags: [ai, agents, code-review, validation, ci, workflow]
created: 2026-07-01
updated: 2026-07-01
sources: [l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# No Mistakes

**No Mistakes** คือ validation pipeline ของ [[kun-chen|Kun Chen]] สำหรับพา first-pass agent code ไปสู่ PR ที่มีหลักฐานว่าทำงานได้. ใน [[l8-principals-agentic-engineering-workflow-kun-chen|วิดีโอ workflow]] มันคือชั้นที่ทำให้เขาไม่ต้องอ่านทุก diff ด้วยตัวเองตั้งแต่แรก.

Pipeline ทำหลายอย่าง: สร้าง branch/commit, รันใน worktree แยก, วิเคราะห์ intent จาก agent session, rebase บน latest main, ทำ adversarial review, self-correct ปัญหาชัด ๆ, test แบบ end-to-end, เก็บ evidence, update docs, lint, push PR, และ babysit PR ต่อจน merge.

แก่นไม่ใช่ "ไม่ต้อง review" แต่คือ **risk-tiered review with evidence**. คนยังตัดสินใจท้ายสุด โดยเฉพาะเรื่อง ambiguous หรือ high-risk แต่ไม่ต้องใช้ attention กับงานที่ pipeline พิสูจน์เองได้.

## See also

- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[agentic-code-review]]
- [[orchestration-tax]]
- [[harness-guides-sensors]]
- [[behavioral-verifier]]
- [[model-honesty]]
