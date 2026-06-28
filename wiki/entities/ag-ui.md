---
title: AG-UI (Agent-User Interaction Protocol)
type: entity
tags: [product, ai, agents, protocol, standard, self-learning]
created: 2026-06-26
updated: 2026-06-26
sources: [Self Learning for Agents Clearly Explained.md]
---

# AG-UI (Agent-User Interaction Protocol)

open standard protocol จาก [[copilotkit|CopilotKit]] ที่ **stream ทุก event ระหว่าง app, user และ agent แบบ real-time**. ต่างจากการเก็บแค่ text ตรงที่ AG-UI แบกทุกชนิดของ event — tool call, state change, approval — ไม่ใช่แค่คำที่คนพิมพ์.

จุดสำคัญในวิกินี้ (ดู [[learning-from-users]]): เพราะ AG-UI พา **agent's miss กับ person's fix มาลงที่เดียวกัน** มันเลยกลายเป็นจุดเก็บสัญญาณการเรียนรู้จาก user ได้. ตัวอย่าง refund — agent ปฏิเสธคำขอเกินลิมิต, manager อนุมัติด้วยมือ; click ของ manager ยิงผ่าน AG-UI อยู่แล้ว แค่อ่าน event เดียวกันก็เก็บคู่ "พลาด+แก้" เป็น [[agent-memory-types|procedural memory]] ได้แทบไม่มีต้นทุน.

เทียบ position: AG-UI อยู่ที่ชั้น **คน↔agent** ขณะที่ [[model-context-protocol|MCP]] อยู่ที่ชั้น **agent↔tool/data** — คนละด้านของ agent.

## See also

- [[copilotkit]]
- [[learning-from-users]]
- [[self-learning-for-agents-explained]]
- [[agent-memory-types]]
- [[model-context-protocol]]
