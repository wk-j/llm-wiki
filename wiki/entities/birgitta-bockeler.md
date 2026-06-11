---
title: Birgitta Böckeler
type: entity
tags: [people, thoughtworks, ai, software-engineering]
created: 2026-06-08
updated: 2026-06-11
sources: [harness-engineering-bockeler.md, "Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete..md"]
---

# Birgitta Böckeler

Birgitta Böckeler เป็น engineer / Global Lead for AI-assisted Software Delivery ที่ [[thoughtworks|Thoughtworks]] เธอเขียนงานชุด "Exploring Generative AI" บน martinfowler.com มาต่อเนื่อง โดยมองจากมุมคนที่ลงมือใช้ coding agent ทำงานจริง ไม่ใช่มุมขายของ

งานที่ wiki นี้เก็บไว้คือ [[harness-engineering-bockeler|Harness engineering for coding agent users]] (2026-04-02) — บทความที่เสนอกรอบคิดว่า harness ที่ผู้ใช้สร้างเองคือ **ระบบ control** ที่ทำจาก guides (feedforward) + sensors (feedback) แยก computational/inferential และทำงานเหมือน cybernetic governor กลั่นเป็นหน้าแนวคิดที่ [[harness-guides-sensors]]

ก่อนหน้านั้นเธอเขียน memo สั้น ๆ เรื่อง harness engineering (2026-02-17) ตอนคำนี้เพิ่งโผล่ แล้วบทความฉบับเต็มข้างบนมา supersede memo นั้น เธอยังเป็นคนรวบรวม catalog ของ **coding agent failure modes** ที่ถูกอ้างถึงในบทความ (เอามา map กับ maintainability harness ว่า sensor แบบไหนจับ failure อะไรได้/ไม่ได้)

## จุดยืนที่น่าสนใจ

- มองคำว่า "harness" แบบ bounded context — แยก **builder harness** (เจ้าของเครื่องมือสร้าง) ออกจาก **user harness** (เราสร้างเอง) ชัดเจน
- ยอมรับตรง ๆ ว่า **behaviour harness** (กำกับว่าแอปทำงานถูกตามต้องการไหม) ยังเป็นปัญหาที่ไม่มีคำตอบดี — ไม่ overclaim
- ยกเครดิต Kief Morris ที่เสนอมุม cybernetics เข้ามาในการคุยเรื่องนี้
- เตือนเรื่อง **spec-as-source** ไว้ก่อนใคร — ว่ามันอาจรับมรดก "the flaws of both MDD and LLMs: inflexibility and non-determinism" คำเตือนนี้ถูก [[jaroslaw-wasowski|Jaroslaw Wasowski]] ยกไปเป็นหลักฐานใน [[stop-writing-specs-start-writing-facts]] (critique ของ [[spec-driven-development|SDD]])

## See also

- [[thoughtworks]]
- [[harness-engineering-bockeler]]
- [[harness-guides-sensors]]
- [[coding-harness]]
- [[harness-engineering]]
