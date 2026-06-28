---
title: CopilotKit
type: entity
tags: [product, ai, agents, framework, self-learning]
created: 2026-06-26
updated: 2026-06-26
sources: [Self Learning for Agents Clearly Explained.md]
---

# CopilotKit

framework/แพลตฟอร์มสำหรับสร้าง interface ที่ user กับ agent ทำงานเคียงกัน. ในวิกินี้ปรากฏผ่าน thread [[self-learning-for-agents-explained]] ของ [[ataiiam|@ataiiam]] (คนจากทีม CopilotKit). จุดยืนของ CopilotKit คือ **interface ที่คนกับ agent ทำงานร่วมกันเป็นที่เดียวที่เห็นทั้ง "สิ่งที่คนทำ" และ "สิ่งที่ agent ทำ"** — จึงเป็นจุดเก็บสัญญาณการเรียนรู้ที่ดีที่สุด (ดู [[learning-from-users]]).

- เป็นผู้อยู่เบื้องหลัง open standard **[[ag-ui|AG-UI]]** (Agent-User Interaction Protocol) ที่ stream ทุก event ระหว่าง app/user/agent แบบ real-time
- สินค้า **CopilotKit Intelligence** เก็บคู่ "agent พลาด + คนแก้" แล้วป้อนกลับเป็น [[agent-memory-types|procedural memory]]; เป็น self-hostable (ทุกอย่างที่เรียนอยู่ใน infra ของลูกค้า) และอ้างว่า live ที่ Fortune 500

> ข้อสังเกต: thread ที่อธิบายกรอบ self-learning ปิดท้ายด้วย pitch CopilotKit Intelligence — กรอบ 3 ชั้นมีค่าในตัว แต่ข้อสรุป "context-from-users ดีที่สุด" ตรงกับสินค้าของผู้เขียนพอดี.

## See also

- [[self-learning-for-agents-explained]]
- [[ag-ui]]
- [[learning-from-users]]
- [[ataiiam]]
- [[agent-memory-types]]
