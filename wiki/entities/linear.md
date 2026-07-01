---
title: Linear
type: entity
tags: [developer-tools, project-management, agents]
created: 2026-06-29
updated: 2026-06-29
sources: ["i don't want to use your agent — @RhysSullivan.md"]
---

# Linear / Linear

**Linear** คือเครื่องมือจัดการ issue, project, roadmap, และ product work สำหรับทีม software. ในโพสต์ [[i-dont-want-to-use-your-agent]] ของ [[rhys-sullivan|Rhys Sullivan]] Linear เป็นตัวอย่าง product ที่มี agent ของตัวเอง แต่ power user อาจอยากให้ agent ประจำวันของตัวเองเข้าถึง Linear แทน.

## ในกรอบ BYO agent

สำหรับ [[bring-your-own-agent|BYO agent]], Linear ไม่ได้มีค่าจาก chat UI อย่างเดียว. สิ่งที่มีค่ากว่าคือ primitive ที่ agent อื่นใช้ได้:

- skill สำหรับแตก problem ใหญ่เป็น ticket ที่ทำได้จริง
- API/MCP/CLI สำหรับอ่านและเปิด issue
- project context, priority, owner, status, และ relation ระหว่างงาน
- deeplink กลับ UI ให้คนตรวจและตัดสินใจ

ผลคือ agent ของผู้ใช้ทำ planning ใน local context ได้ แล้วค่อย sync งานเข้า Linear.

## See also

- [[bring-your-own-agent]]
- [[i-dont-want-to-use-your-agent]]
- [[model-context-protocol]]
- [[agent-experience]]
