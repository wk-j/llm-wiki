---
title: Impeccable
type: entity
tags: [design, tool, open-source, claude-code]
created: 2026-04-28
updated: 2026-04-28
sources: [chase-ai-claude-code-impeccable.md]
---

# Impeccable / อิมเพกเคเบิล

Impeccable คือ open-source GitHub repository ที่ออกแบบมาเพื่อเป็น "design skill" ให้กับ [[claude-code|Claude Code]] โดยเฉพาะ เพื่อแก้ปัญหาการสร้าง UI ที่ดูเป็น "AI slop" หรือดูจืดชืดไม่มีรสนิยม โดยการเพิ่มคำศัพท์และมาตรฐานการออกแบบระดับมืออาชีพเข้าไปในตัว Agent

## แก่นสำคัญ (Core Concept)

Impeccable ไม่ใช่แค่ prompt สั้นๆ แต่เป็นระบบที่ประกอบด้วย 23 คำสั่ง (commands) และไฟล์อ้างอิงเฉพาะด้าน 7 ไฟล์ที่ครอบคลุมหลักการออกแบบสำคัญ:
- **Typography** (ตัวอักษร)
- **Color** (สี)
- **Spatial Design** (การจัดการพื้นที่)
- **Responsiveness** (การแสดงผลตามขนาดหน้าจอ)
- **Interactions** (การตอบสนอง)
- **Motion** (การเคลื่อนไหว)
- **UX Writing** (การใช้คำใน UI)

## ฟีเจอร์ที่โดดเด่น

- **Impeccable Live (Alpha):** โหมดแก้โค้ดแบบเห็นผลทันทีใน browser (Live editing) ซึ่งเราสามารถคลิกเลือก component แล้วสั่ง "bolder" (ทำให้เด่นขึ้น) หรือ "delight" (เพิ่มลูกเล่น) ได้โดยตรงผ่านหน้าจอ และตัว Agent จะแก้โค้ดให้ตามสั่ง
- **Design Interview:** เมื่อเริ่มโปรเจกต์ใหม่ด้วยคำสั่ง `impeccable craft` ตัว Agent จะสัมภาษณ์เราอย่างละเอียดเพื่อสร้างไฟล์ `product.md` และ `design.md` เพื่อใช้เป็นฐานในการออกแบบ (คล้ายกับมาตรฐานของ Google Stitch)
- **Reverse Engineering:** คำสั่ง `impeccable document` สามารถอ่าน codebase เดิมที่มีอยู่แล้วเพื่อสร้าง `design.md` สรุปกฎการออกแบบปัจจุบันออกมาให้
- **Design Audit:** คำสั่ง `impeccable critique` จะทำการตรวจสุขภาพการออกแบบ (Design Health Score) และหาจุดที่เป็น "AI slop" หรือ anti-patterns ต่างๆ

## ประโยชน์ที่ได้รับ (Payoff)
การใช้ Impeccable ช่วยให้ developer ที่อาจจะไม่ถนัดเรื่อง design สามารถสร้างหน้าตาเว็บที่มี "taste" และดูเป็นมืออาชีพมากขึ้น โดยการยืมสมองและมาตรฐานการออกแบบที่ฝังอยู่ในตัว skill นี้มาใช้ผ่าน [[claude-code|Claude Code]]

## See also

- [[claude-code]]
- [[ai-slop]]
- [[chase-ai]]
