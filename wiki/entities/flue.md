---
title: Flue
type: entity
tags: [ai, agents, harness, framework, tools]
created: 2026-05-10
updated: 2026-05-10
sources: [Agent Harness Engineering.md]
---

# Flue

**Flue** คือ agent harness framework ที่ [[fred-schott|Fred Schott]] สร้าง และถูก [[addy-osmani|Addy Osmani]] ยกเป็นตัวอย่างใน [[agent-harness-engineering]]

## ทำไมอยู่ใน wiki นี้

Flue เป็นตัวอย่างของแนวโน้ม **Harness-as-a-Service** หรืออย่างน้อย **harness framework**: ตลาดไม่ได้มีแค่ LLM API ที่ให้ completions แล้วจบ แต่เริ่มมี runtime ที่ให้ loop, tools, context handling, hooks, sandbox, และ recovery path มาเป็นโครงให้ทีมปรับต่อ

**ได้อะไร:** ทีมไม่ต้องสร้าง agent runtime จากศูนย์ แต่ยังต้องทำงานสำคัญเอง คือปรับ harness ให้เข้ากับ failure history, policy, และ workflow ของตัวเอง

## See also

- [[fred-schott]]
- [[agent-harness-engineering]]
- [[coding-harness]]
- [[harness-ratchet]]
