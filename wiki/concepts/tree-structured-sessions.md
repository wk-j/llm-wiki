---
title: Tree-structured Sessions
type: concept
tags: [ux, agents, context-management]
created: 2026-04-28
updated: 2026-09-12
sources: [mario-zechner-pi-agent.md, dillon-mulroy-ships-production-code-he-didnt-write.md]
---

# Tree-structured Sessions / เซสชันโครงสร้างต้นไม้

**Tree-structured Sessions** เป็นวิธีการจัดการประวัติการสนทนาใน coding agent (โดยเฉพาะใน [[pi-agent|pi]]) ที่เปลี่ยนจากการเก็บเป็นรายการแนวตั้ง (Linear chat) มาเป็นการเก็บเป็นโครงสร้างกิ่งก้าน (Tree)

## ทำไมต้องเป็นต้นไม้?

ในงานเขียน code ที่ซับซ้อน เรามักต้องมีการลองทำสิ่งต่างๆ (Exploration) หรือทำภารกิจย่อย (Sub-tasks):
- **Isolation**: การแตกกิ่ง (Branching) ช่วยให้เราแยกการทดลองออกเป็นส่วนๆ ถ้าทำไม่สำเร็จก็แค่กลับไปที่กิ่งก่อนหน้า (Checkpointed state)
- **Sub-agent Simulation**: เราสามารถแตกกิ่งเพื่อไปสั่งให้ agent "สรุปไฟล์ทั้งโปรเจกต์" แล้วนำแค่ผลลัพธ์นั้นกลับมาที่กิ่งหลัก เพื่อประหยัดพื้นที่ context
- **Parallel Contexts**: ช่วยให้เราทำงานหลายอย่างในโปรเจกต์เดียวกันพร้อมกันได้โดยไม่ทำให้ประวัติการคุยปนกัน

## Payoff / ผลคือ
ช่วยให้ Developer บริหารจัดการ context window ได้อย่างแม่นยำ ลดปัญหา [[context-rot]] และประหยัดค่าใช้จ่ายโดยไม่ต้องส่งประวัติที่ไม่จำเป็นกลับไปหาโมเดลซ้ำๆ

## Dillon ใช้ `/tree` เป็น human-curated context

[[dillon-mulroy|Dillon Mulroy]] ใช้ `/tree` ของ [[pi-agent|pi]] สำรวจ framework, storage API และ test setup แยกกันทีละกิ่ง เขามักเริ่มจากคำถามที่ตัวเองรู้คำตอบเพื่อเช็กว่า model เข้าใจ tech stack ตรงกัน แล้วคัดข้อความสุดท้ายด้วย `/copy` หรือให้เขียนลง Markdown ก่อนกลับไปที่ราก

เวลาย้อนกิ่ง pi ให้เลือกกลับเฉย ๆ ให้ระบบสรุป หรือกำหนด prompt สำหรับสรุป การย้อนนี้เปลี่ยนเฉพาะ conversation context ไม่ได้ rollback Git state

Dillon มองว่าวิธีนี้ดีกับงานของเขามากกว่า subagent เพราะคนเป็นผู้เลือกเองว่า context ใดสำคัญ ไม่ต้องรับ summary ที่ core agent เลือกมาให้ แต่ประโยชน์นี้มาพร้อมต้นทุน ผู้ใช้ต้องคุมกิ่งและมี intuition ว่า context แบบไหนทำให้ model ตอบดี

**ผลคือ:** tree session เป็นทางเลือกแบบ serial และคุมด้วยคน ไม่ใช่ parallelism แบบ agent fleet

## ดูเพิ่ม

- [[pi-agent]]
- [[compaction]] — วิธีลดขนาด context แบบดั้งเดิม (เส้นตรง)
- [[dillon-mulroy-ships-production-code-he-didnt-write]]
- [[subagent-patterns]]
