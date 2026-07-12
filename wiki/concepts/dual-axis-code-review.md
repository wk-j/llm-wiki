---
title: Dual-Axis Code Review
type: concept
tags: [ai, code-review, agents, software-engineering, skills]
created: 2026-05-12
updated: 2026-07-12
sources: ["New Skills! handoff, prototype, review and writing-*  Skills Changelog.md", new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets.md]
---

# Dual-Axis Code Review / รีวิวโค้ดสองแกน

**Dual-axis code review** คือแนวคิดการรีวิว diff ด้วยสองคำถามแยกกัน: โค้ดทำตามมาตรฐานของ repo ไหม และโค้ดทำตาม spec จริงไหม. [[matt-pocock|Matt Pocock]] เคยเสนอเป็น skill `/review` ที่อยู่ระหว่างพัฒนา และใน [[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets|Skills v1.1]] มันถูกนำมาใช้จริงเป็นส่วนของ implementation lifecycle แล้ว.

## ปัญหาที่ต้องแยกเป็นสองแกน

Code review โดย agent มักพลาดเพราะคำว่า "review" กว้างเกินไป. ถ้า prompt ให้ดูทุกอย่างพร้อมกัน model อาจจับเฉพาะเรื่องที่เห็นง่าย เช่น style หรือ bug ชัด ๆ แล้วพลาดคำถามใหญ่

Pocock แยกเป็นสองแกน

| แกน | คำถามหลัก | ความเสี่ยงถ้าไม่ดู |
|---|---|---|
| Standards | diff เข้ากับ convention, architecture, และ pattern ของ repo ไหม | โค้ดใช้ได้ แต่แปลกจากระบบเดิม ดูแลยาก |
| Spec | diff ทำตาม issue หรือ PRD ที่ตกลงไว้จริงไหม | โค้ดสวย แต่แก้ผิดปัญหา |

**ได้อะไร:** review ไม่กลายเป็น checklist กว้าง ๆ แต่มี lens ชัดเจนสองชุด

## ทำไม standards ยากกว่า spec

Spec มักอยู่ใน issue หรือ PRD. Agent อ่านแล้วเทียบกับ diff ได้ค่อนข้างตรง

Standards ยากกว่า เพราะมาตรฐานของแต่ละ repo อยู่กระจายในโค้ดเดิม, test, naming, folder shape, error handling, และ undocumented convention. Pocock จึงมองว่าอาจต้องมี skill อีกตัวที่สกัด coding standards จาก repo ก่อน เพื่อให้ review skill มีฐานอ้างอิง

ตรงนี้เชื่อมกับ [[grounding]]: reviewer ที่ดีควร cite code evidence ไม่ใช่อ้าง taste ลอย ๆ

## ใช้ subagent สองตัว

รูปแบบที่ Pocock เสนอคือให้ review skill แตก subagent สองตัวแบบขนาน

- ตัวหนึ่งดู standards ของ codebase
- อีกตัวดู fidelity ต่อ issue/PRD

จากนั้น main agent หรือ judge รวมผล. รูปนี้เป็น [[subagent-patterns|pipeline/fan-out hybrid]] เพราะงานเดียวถูกส่องสอง lens พร้อมกัน แล้วค่อยรวมเป็น review เดียว

## ความเชื่อมโยงกับ code-is-free

ถ้า implementation ถูกลงเพราะ agent เขียนโค้ดเร็วขึ้น review จะกลายเป็นคอขวดใหม่. [[code-is-free]] มองว่าต้นทุนย้ายไปที่ maintenance และ review. Dual-axis review เป็นวิธีทำให้คอขวดนี้คมขึ้น แทนที่จะให้ reviewer agent พูดกว้าง ๆ

**ผลคือ:** มนุษย์ยังตัดสินใจสุดท้าย แต่ agent ช่วยแยกความเสี่ยงเป็นสองกองที่อ่านง่ายกว่าเดิม

## v1.1 เพิ่ม refactoring smells

v1.1 เติม vocabulary จากหนังสือ *Refactoring* ของ Martin Fowler เข้า standards axis เช่น mysterious name, duplicated code, feature envy, data clumps, primitive obsession, repeated switches, divergent change, speculative generality และ message chains.

แนวคิดคือ model รู้จักคำเหล่านี้จาก training priors อยู่แล้ว. Skill จึงไม่ต้องอธิบายตำราทั้งเล่ม แค่เรียกชื่อพร้อม gloss สั้น ๆ เพื่อเปิด lens ให้ reviewer มองหา. Pocock รายงานว่าทดลองสองสัปดาห์แล้วช่วยคุณภาพ code มาก แต่เป็น field report ของผู้สร้าง ยังไม่ใช่การทดลองเปรียบเทียบ.

**ได้อะไร:** standards axis ตรวจได้ลึกกว่า formatting/convention และชี้ design smell ด้วยภาษาที่ทีมตามแก้ต่อได้.

## See also

- [[new-skills-handoff-prototype-review-writing]]
- [[subagent-patterns]]
- [[harness-engineering]]
- [[grounding]]
- [[code-is-free]]
- [[software-entropy]]
- [[alignment-bottleneck]]
- [[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets]]
