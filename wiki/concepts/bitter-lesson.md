---
title: The Bitter Lesson
type: concept
tags: [ml, ai, compute, scaling, harness]
created: 2026-06-21
updated: 2026-06-21
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md"]
---

# The Bitter Lesson / บทเรียนอันขมขื่น

**The bitter lesson คือไอเดียคลาสสิกใน ML ว่า "ไม่ว่าคุณจะ optimize ด้วยมือเก่งแค่ไหน raw compute ก็จะชนะคุณในระยะยาว" — เพราะ compute เพิ่มขึ้นเร็วมากจนวิธีที่พึ่ง compute ล้วน ๆ แซงวิธีที่ฝังความรู้มนุษย์ไว้.** (เป็นบทความดังของ Rich Sutton) ในพอดแคสต์ [[matt-pocock|Matt Pocock]] × [[david-ondrej|David Ondrej]] (2026-06-19) มันถูกหยิบมาเป็น "ความตึง" ในการตัดสินใจว่าควรลงแรงที่ harness หรือรอ model ดีขึ้นเอง

## ใจความ

> "Whatever you do in machine learning research, raw compute will just beat you every time because compute is increasing at such a high rate."
> (ไม่ว่าคุณทำอะไรในงานวิจัย ML สุดท้าย raw compute ชนะคุณทุกครั้ง เพราะ compute โตเร็วมาก)

บทเรียนเดิมเป็นเรื่องของนักวิจัย ML: วิธีที่ใส่ความรู้เฉพาะทางของมนุษย์ลงไป (hand-crafted features, rules) มักแพ้วิธีทั่วไปที่เรียนจากข้อมูล + compute มหาศาลในระยะยาว

## ความตึงในยุค agentic

David ใช้ bitter lesson ดันมุมว่า "ถ้าเปลี่ยน engine (model) ที่ดีกว่าเข้าไป ทุกอย่างที่อยู่บน harness ก็ดีขึ้นทันที" — งั้นทำไมต้องเสียเวลา optimize harness?

Matt ยอมรับตรง ๆ ว่าเขาอาจกำลัง **ตกหลุมด้านกลับของ bitter lesson** คือเอาแต่ขัด harness แทนที่จะรอ model ดีขึ้นเอง. แต่จุดยืนเขาคือ:

- **อย่ารอเฉย ๆ** — David เห็นด้วยว่าการนั่งรอ AGI โดยไม่ทำอะไรเป็นเรื่องโง่
- **แต่ก็อย่าทุ่มทุกอย่างไปที่ model** — ถ้า over-optimize รอบ model ตัวเดียว จะเสีย focus จาก fundamentals ที่เวิร์กมา 30-40 ปี
- harness และ codebase คือ **สิ่งที่เราคุมได้จริง** (ดู [[coding-harness]]) — ทำให้ agent-agnostic ไว้ ของก็น่าจะเวิร์กต่อแม้ model เปลี่ยน

> ได้อะไร: bitter lesson เตือนว่าอย่าฝังตัวกับ trick ที่ผูกกับ model รุ่นเดียว — แต่ก็ไม่ได้แปลว่าให้เลิกทำ harness แล้วรอ compute. ของที่ทนต่อ model upgrade คือ software fundamentals และ harness ที่ไม่ผูกกับ model (ตรงกับ [[facts-first]]: fact ที่ checkต ด้วย exit code รอด model migration ส่วน prose ไม่รอด)

## ดูเพิ่ม

- [[matt-pocock-agentic-workflow]]
- [[matt-pocock]]
- [[coding-harness]]
- [[harness-engineering]]
- [[facts-first]]
- [[verifiability]]
