---
title: LangChain
type: entity
tags: [org, product, ai, agents, framework, harness]
created: 2026-06-26
updated: 2026-06-26
sources: [Self Learning for Agents Clearly Explained.md]
---

# LangChain

บริษัท/framework ด้าน AI agent นำโดย **Harrison Chase**. ในวิกินี้ปรากฏผ่าน thread [[self-learning-for-agents-explained]] หลายจุด:

- **ที่มาของกรอบ 3 ชั้น** — Harrison Chase เป็นคนแบ่ง agent เป็น model / harness / context ที่ [[three-learning-layers]] ใช้เป็นแกน
- **The art of loop engineering** — Sydney Runkle (LangChain) จัด loop ออกเป็น 4 ระดับ (verify → schedule → rewrite harness) และบอกว่าคุณค่าอยู่ที่ loop ชั้นนอก ดู [[loop-engineering]]
- **Deep Agents** — harness ที่ LangChain ปรับด้วยการ **เขียน harness ใหม่จาก trace ตัวเองโดยตรึง model ไว้** ได้ผลจาก 52.8 → 66.5 บน Terminal-Bench 2.0 (top 30 → top 5); agent เสนอ คนอนุมัติ — เป็น instance ของ Layer 2 (harness self-learning) ใน [[three-learning-layers]]

> หมายเหตุ: [[chase-ai|Chase AI]] ในวิกินี้เป็นคนละคน (content creator ด้าน Claude Code) ไม่เกี่ยวกับ Harrison Chase แห่ง LangChain.

## See also

- [[three-learning-layers]]
- [[loop-engineering]]
- [[self-learning-for-agents-explained]]
- [[harness-engineering]]
