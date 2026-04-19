---
title: Delegation Mindset
type: concept
tags: [ai, prompting, claude, claude-code, coding-harness, workflow]
created: 2026-04-20
updated: 2026-04-20
sources: [Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md]
---

# Delegation Mindset / วิธีคิดแบบมอบงาน

แนวคิดการคุยกับ [[claude-opus-4-7|Opus 4.7]] เหมือนมอบงานให้ **engineer ที่เก่งและอยู่ห่าง** ไม่ใช่คู่ pair programming ที่นั่งข้างกัน ที่มา: [[claude-opus-4-7-migration-pachaar|Akshay Pachaar]] สังเกตว่าพอ upgrade จาก 4.6 มา 4.7 แล้วค่า token พุ่งขึ้นเป็นเท่าตัวทั้ง ๆ ที่ prompt เหมือนเดิม ปัญหาไม่ได้อยู่ที่ model แต่อยู่ที่ **สไตล์การคุย**.

## ทำไมสไตล์เดิมเจ๊ง

บน 4.6 คุณแชทเป็นรอบ ๆ ได้สบาย — ถาม 2 คำ ตอบ 2 คำ ใส่ constraint เพิ่มทีหลัง ไม่เสียหาย

บน 4.7 ทุก user turn = ทริกเกอร์ reasoning รอบใหม่ ([[adaptive-thinking]]). model คิดลึกทุกครั้งที่เราพิมพ์อะไรเข้าไป ไม่ว่า turn นั้นจะสมควรคิดลึกหรือไม่ พอคุยเป็นรอบเล็ก ๆ หลาย turn ก็เลยเสีย token reasoning ซ้ำแล้วซ้ำเล่าโดยไม่ได้คุณภาพเพิ่มตามสัดส่วน

พูดง่าย ๆ: **ต้นทุนต่อ user turn แพงขึ้น คุณภาพต่อ turn ก็ไม่ได้เพิ่มตาม** ถ้ายังเน้นถี่ ๆ สั้น ๆ เหมือนเดิม ได้ขาดทุนแน่นอน

## สามท่าหลักที่ Pachaar แนะนำ

### 1) ยัดทุกอย่างไว้ใน turn แรก

เขียน prompt เดียวที่ครบทั้ง:

- **intent** — อยากได้อะไรจริง ๆ
- **constraints** — ข้อจำกัด (เทคโนโลยี, สไตล์, performance)
- **acceptance criteria** — จบงานเมื่อไหร่ถึงเรียกว่าผ่าน
- **file paths** — ชี้ไฟล์ที่เกี่ยวข้องให้ชัด

prompt สั้นแบบคลุมเครือที่ค่อย ๆ เติม context หลาย turn = แพงและคุณภาพตก ทั้งคู่

### 2) รวมคำถามเป็นชุด (batch)

ถ้ามี 3 คำถามเกี่ยวกัน อย่าถามทีละข้อ รวมเป็น message เดียว model มี context พอเดินต่อเองโดยไม่ต้อง check-in กับเราทุกก้าว

### 3) ใช้ [[auto-mode|auto mode]] (Shift+Tab) สำหรับงานที่ไว้ใจได้

ใน [[claude-code|Claude Code]] มี [[auto-mode|auto mode]] — permission mode ที่มี classifier คั่นกลาง auto-approve action ปลอดภัย block action เสี่ยง เหมาะกับงาน long-running ที่ไว้ใจได้ ตัดการถามยืนยันที่ไม่จำเป็นออก ลด cycle time (รายละเอียดและข้อจำกัดอยู่ในหน้า concept)

เสริมได้อีกว่าให้ Claude ส่งเสียงเมื่อจบงาน (มันจะสร้าง hook เอง) เราไม่ต้องนั่งเฝ้าหน้าจอ

**ผลคือ** reasoning overhead เกิดหนเดียวที่ turn แรก ไม่เกิดซ้ำทุก turn ถัด ๆ ไป — ต้นทุน token ลด คุณภาพเพิ่ม เพราะ model ได้เห็นภาพรวมครบตั้งแต่ต้น

## ความเชื่อมโยงกับแนวคิดอื่น

- **[[instruction-budget]]** — Alex Ker เตือนว่าอย่ายัด instruction เกินไม่กี่ร้อยข้อ *Delegation mindset ไม่ขัดกับข้อนี้ — หมายถึงใส่ context (ไฟล์, intent, criteria) ให้ครบ ไม่ใช่ใส่ rule เป็นร้อย ๆ ข้อ*
- **[[coding-harness]]** — R.P.I. framework (Role / Purpose / Instructions) เป็นวิธีเขียน turn-1 ที่ครบแบบมีโครง
- **[[ai-orchestrator]]** — บทบาท orchestrator เป็น delegation mindset ที่ scale ขึ้นไปอีกชั้น: สั่ง subagent/pipeline ทำงาน ไม่ใช่ทำเอง
- **[[harness-engineering]]** — Panutat มอง reviewer agent เป็นตัวรับมอบงาน ไม่ใช่ให้คนไปรีวิวตรง ๆ ทิศเดียวกัน

## เมื่อไหร่ไม่ควรใช้ท่านี้

- งาน exploratory ที่ยังไม่รู้ตัวเองว่าต้องการอะไร — การคุยเป็น turn ย่อย ๆ อาจคุ้มเพราะคำตอบรอบแรกช่วย shape คำถามรอบต่อไป
- debugging ที่ต้องการ feedback สด ๆ ต่อ tool output
- งานสั้นมาก ๆ ที่ไม่ได้เสีย reasoning นานอยู่แล้ว

## ที่มาของสำนวน

Pachaar: *"Treat Claude like a capable engineer you delegate to, not a pair programmer you guide line by line."* (คำเดิมจาก source)

## See also

- [[claude-opus-4-7]]
- [[claude-opus-4-7-migration-pachaar]]
- [[adaptive-thinking]]
- [[coding-harness]]
- [[instruction-budget]]
- [[ai-orchestrator]]
- [[harness-engineering]]
