---
title: Tree-structured Sessions
type: concept
tags: [ux, agents, context-management]
created: 2026-04-28
updated: 2026-04-28
sources: [mario-zechner-pi-agent.md]
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

## ดูเพิ่ม

- [[pi-agent]]
- [[compaction]] — วิธีลดขนาด context แบบดั้งเดิม (เส้นตรง)
