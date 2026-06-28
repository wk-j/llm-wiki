---
title: Letta
type: entity
tags: [product, ai, agents, agent-memory, self-learning]
created: 2026-06-26
updated: 2026-06-26
sources: [Self Learning for Agents Clearly Explained.md]
---

# Letta

แพลตฟอร์ม agent memory ที่ทำ continual learning โดย **ตรึง weight ไว้แล้วเรียนใน plain text ที่อ่าน/diff/ลบได้**. ในวิกินี้ปรากฏใน [[self-learning-for-agents-explained]] เป็นตัวแทน "Context Approach #1 — เขียน memory ใหม่เบื้องหลัง" ใน [[three-learning-layers]].

กลไกสำคัญ: **agent ที่คุยกับ user แก้ core memory ตัวเองไม่ได้** — มี agent แยกตัวเขียน memory ใหม่ตอน idle (Letta เรียก *sleep-time compute*). แนวคิดเดียวกับ OpenClaw ที่รัน nightly **[[dreaming|dreaming]] pass** บนไฟล์ memory และกับ [[dreaming|dreaming]] ของ [[anthropic|Anthropic]] — ทั้งหมดคือ "process แยกที่ curate memory นอก hot path".

จุดขายที่ thread ชู: **weight ชั่วคราว แต่ text อยู่ถาวร** — ย้าย memory ไป model ใหม่ได้ หรือ roll back ได้ ต่างจากการ fine-tune ที่ความรู้ฝังใน weight แล้วเอาออกยาก.

## See also

- [[three-learning-layers]]
- [[dreaming]]
- [[agent-memory-types]]
- [[self-learning-agents]]
- [[self-learning-for-agents-explained]]
