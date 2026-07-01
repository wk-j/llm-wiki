---
title: Good Night Have Fun
type: entity
tags: [ai, agents, long-running, loops, workflow]
created: 2026-07-01
updated: 2026-07-01
sources: [l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# Good Night Have Fun

**Good Night Have Fun** หรือ `gnhf` คือ tool ของ [[kun-chen|Kun Chen]] สำหรับปล่อย agent ทำงานยาวด้วย objective, cap, และ stop condition ที่กำหนดไว้. ใน [[l8-principals-agentic-engineering-workflow-kun-chen|วิดีโอ workflow]] เขาใช้มันกับงาน usability loop: ให้ agent แกล้งเป็นเด็ก 7 ขวบ ใช้แอป, หา problem แรก, fix, แล้ววนซ้ำ.

งานที่เหมาะคือสิ่งที่มีสัญญาณตรวจได้หรือมี judgement ที่ agent พอรับผิดชอบได้ เช่น ลด page-load time, เพิ่ม E2E coverage, หรือทดลอง hypothesis เพื่อ improve metric. Kun ชอบมันเพราะควบคุม token cap, iteration cap, และ stop condition ได้ชัดกว่าการปล่อย goal แบบกว้าง ๆ.

## See also

- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[long-running-agents]]
- [[loop-engineering]]
- [[orchestration-tax]]
- [[behavioral-verifier]]
