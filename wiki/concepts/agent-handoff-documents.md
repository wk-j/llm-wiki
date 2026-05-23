---
title: Agent Handoff Documents
type: concept
tags: [ai, agents, context-management, skills, workflow]
created: 2026-05-12
updated: 2026-05-12
sources: ["New Skills! handoff, prototype, review and writing-*  Skills Changelog.md"]
---

# Agent Handoff Documents / เอกสารส่งต่องานให้ agent

**Agent handoff document** คือเอกสารสั้น ๆ ที่สรุป session ปัจจุบันให้ agent ตัวใหม่รับงานต่อได้ โดยไม่ต้องแบก transcript ทั้งก้อนเข้า context. [[matt-pocock|Matt Pocock]] เสนอผ่าน skill `/handoff` ใน changelog เดือนพฤษภาคม 2026

## แก่นความคิด

ปัญหาคือ session ที่ดีมักยาวขึ้นเรื่อย ๆ. พอถึงจุดหนึ่ง เราอาจยังไม่อยากทิ้งความเข้าใจเดิม แต่ก็ไม่อยากให้ agent ทำงานใหม่ใน context ที่เริ่มรก

Handoff document เลยทำหน้าที่เป็น bridge. มันเก็บเฉพาะสิ่งที่ session ถัดไปต้องใช้

- เป้าหมายปัจจุบัน
- สิ่งที่ตัดสินใจแล้ว
- สิ่งที่ยังไม่แน่ใจ
- path หรือ URL ของ artifact ที่มีอยู่แล้ว
- skill หรือ workflow ที่ agent ตัวถัดไปควรใช้

**ได้อะไร:** เริ่ม agent ใหม่ด้วย context ที่คมกว่าเดิม โดยยังไม่เสียเจตนาของ session เก่า

## ไม่ใช่ compaction แบบเดียวกัน

[[compaction]] คือการย่อ transcript เพื่อให้ session เดิมไปต่อ. Handoff document ต่างออกไป เพราะมันตั้งใจให้ session ใหม่รับงานต่อ

ความต่างสำคัญคือ handoff ต้องสรุป "vibe" และ intent ด้วย. ถ้า session เดิมเป็น [[grill-me|grilling session]] agent ตัวใหม่ควรรู้ว่าต้องถามต่อ ไม่ใช่รีบ implement

## Pattern การใช้งาน

มีสองแบบที่ใช้บ่อย

| Pattern | อธิบาย | ตัวอย่าง |
|---|---|---|
| Fire and forget | ส่งงานแทรกไปให้ agent ใหม่ แล้วไม่ต้องกลับมามาก | ระหว่าง plan เจอ bug เล็ก ๆ เลย handoff ให้ agent อีกตัว fix |
| DIY subagent | เปิด session ใหม่เหมือน subagent ที่มนุษย์คุมเอง แล้วส่งผลกลับมา | ระหว่าง grill ต้องลอง prototype ก่อน จึงเปิด agent ใหม่ไปทดลอง แล้วเอาบทเรียนกลับมาคุยต่อ |

DIY subagent ต่างจาก [[subagent-patterns|subagent]] ปกติตรงที่ agent ใหม่มี context window เต็มของตัวเอง และถ้า harness รองรับก็สามารถ spawn subagent ต่อได้

## หลักการเขียน handoff ที่ดี

Handoff ที่ดีไม่ควร dump ทุกอย่าง เพราะจะพา [[context-rot]] จาก session เก่าตามไปด้วย

- อ้างถึง artifact ด้วย path/URL แทนการ copy ซ้ำ
- บอกสถานะของงานตรง ๆ ว่าอะไรเสร็จ อะไรค้าง
- บอกข้อห้ามหรือขอบเขตที่ตกลงกันแล้ว
- แนะนำ skill ถัดไป เช่น `prototype`, `grill-me`, `review`

**ผลคือ:** handoff กลายเป็น control surface ของ [[ai-orchestrator|AI orchestrator]] ไม่ใช่แค่ summary อัตโนมัติ

## See also

- [[new-skills-handoff-prototype-review-writing]]
- [[context-rot]]
- [[compaction]]
- [[subagent-patterns]]
- [[claude-code-session-management]]
- [[ai-orchestrator]]
- [[grill-me]]
