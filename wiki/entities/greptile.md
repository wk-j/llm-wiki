---
title: Greptile
type: entity
tags: [ai, code-review, developer-tools]
created: 2026-06-16
updated: 2026-06-16
sources: [Agentic Code Review.md]
---

# Greptile

**Greptile** คือ AI code review / code intelligence tool ที่ปรากฏใน [[agentic-code-review|Agentic Code Review]] ของ [[addy-osmani|Addy Osmani]] ในฐานะ reviewer ที่มี character ต่างจาก [[coderabbit|CodeRabbit]]. Addy อ้าง benchmark บางชุดว่า Greptile จับ bug ด้าน correctness / architecture ได้ดี แต่ trade-off กับ precision/recall ต้องวัดกับ codebase จริง.

## ที่ทางในวิกินี้

Greptile เป็นตัวอย่างของหลัก **heterogeneous review**: ใช้ AI reviewer หลายตัวที่คิดไม่เหมือนกัน ดีกว่าใช้สำเนาของ model เดียวกันหลายรอบ. คุณค่าคือทำให้ human reviewer เห็น risk ที่ tool อีกตัวอาจไม่ flag.

## See also

- [[agentic-code-review]]
- [[coderabbit]]
- [[harness-guides-sensors]]
- [[orchestration-tax]]
