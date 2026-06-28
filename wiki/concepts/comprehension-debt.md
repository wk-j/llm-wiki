---
title: Comprehension Debt
type: concept
tags: [ai, software-engineering, code-review, cognition, agents]
created: 2026-06-16
updated: 2026-06-16
sources: ["Loop Engineering..md", Agentic Code Review.md]
---

# Comprehension Debt / หนี้ความเข้าใจ

**Comprehension debt** คือช่องว่างระหว่าง "ระบบทำงานจริงอย่างไร" กับ "คนในทีมเข้าใจว่ามันทำงานอย่างไร". ในยุค coding agent ช่องว่างนี้โตเร็วขึ้น เพราะ agent ผลิต code path ใหม่ได้มากกว่าที่มนุษย์อ่านและปรับ mental model ตามทัน.

[[addy-osmani|Addy Osmani]] (วิศวกร Google ที่เขียนเรื่อง agent architecture) ใช้คำนี้ใน [[loop-engineering|loop engineering]] และ [[agentic-code-review|agentic code review]]. แก่นคือ: ลูปและ agent ไม่ได้แค่สร้าง technical debt ได้เร็วขึ้น แต่มันทำให้คน **ไม่รู้แล้วว่าระบบจริงเป็นแบบไหน** ได้เร็วขึ้นด้วย.

## ต่างจาก cognitive debt อย่างไร

[[cognitive-debt|Cognitive debt]] กว้างกว่า: mental model ของคนต่อระบบเก่า, ไม่ตรง, หรือหนักเกินกว่าจะถือไว้. Comprehension debt เป็นกรณีเฉพาะที่เกิดจากการเปลี่ยนแปลงวิ่งเร็วกว่า understanding.

ตัวอย่างง่าย ๆ:

- agent เพิ่ม retry logic ใน payment path แต่ไม่มีใครรู้ว่า retry ซ้ำได้กี่ครั้ง
- agent rewrite test ให้ผ่าน behavior ใหม่ แล้วทีมคิดว่าพฤติกรรมเดิมยังถูกกันอยู่
- cloud agent ship PR เล็ก ๆ หลายสิบอันต่อวัน แต่ไม่มีใครเห็นภาพรวมว่า module boundary เปลี่ยนไปแล้ว

**ผลคือ:** production อาจยังเขียว แต่ทีมเริ่ม debug ด้วยแผนที่เก่า.

## ทำไม code review เป็นจุดรับหนี้

Review เคยทำหน้าที่สองอย่างพร้อมกัน: จับ bug และกระจายความเข้าใจ. พอ agent ผลิต PR มากขึ้น งานจับ bug อาจโยนให้ test/AI reviewer ช่วยได้บางส่วน แต่ส่วน "กระจายความเข้าใจ" ยังต้องมีคนรับ.

ใน [[agentic-code-review]] Addy เตือนว่าถ้า reviewer เป็นคนแรกที่เคยอ่านโค้ดจากมนุษย์เลย review จะไม่ได้แค่ตรวจ correctness แต่ต้องกู้ intent, อ่านผลกระทบ, และ update mental model ไปพร้อมกัน. ถ้า volume มากเกินไป ทีมจะเริ่ม rubber-stamp แล้วหนี้ความเข้าใจสะสม.

## วิธีกัน

- **PR เล็กพอให้คนอ่านจริง** — ขนาด diff เป็น design constraint
- **แนบ intent และ decision log** — ให้ reviewer เข้าใจ why ก่อนจมใน how
- **อ่าน test diff ก่อน** — test ที่ถูกแก้ผิดทำให้ทีมเข้าใจ behavior ผิด
- **ใช้ AI reviewer เป็น triage sensor** — ให้มันชี้จุดเสี่ยง เพื่อให้คนใช้ attention กับส่วนที่เปลี่ยน mental model
- **ทำ review sampling แบบตั้งใจ** — ถ้าคนอ่านทุกบรรทัดไม่ได้ ต้องสุ่ม/audit path ที่กระทบ architecture และ behavior ไม่ใช่สุ่มแบบสะดวก
- **อัปเดต docs/skills/harness เมื่อเจอ pattern ซ้ำ** — เปลี่ยนหนี้ความเข้าใจให้เป็น [[harness-ratchet|harness ratchet]]

**ได้อะไร:** ทีมไม่จำเป็นต้องอ่านทุกบรรทัด แต่ต้องมีวิธีรักษา mental model ของระบบให้ตามความจริงทัน.

## See also

- [[agentic-code-review]]
- [[loop-engineering]]
- [[orchestration-tax]]
- [[cognitive-debt]]
- [[cognitive-surrender]]
- [[harness-ratchet]]
- [[harness-guides-sensors]]
