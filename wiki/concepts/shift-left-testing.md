---
title: Shift-Left Testing
type: concept
tags: [testing, quality, agile]
created: 2026-04-28
updated: 2026-06-16
sources: [jeeraphan-lairat-ai-coding-speed.md, Agentic Code Review.md]
---

# Shift-Left Testing / การทดสอบตั้งแต่เนิ่นๆ

แนวคิดการขยับกิจกรรมด้าน Testing มาไว้ที่ช่วงต้นของวงจรการพัฒนา (ขยับไปทางซ้ายของเส้น Timeline) แทนที่จะรอให้โค้ดเสร็จก่อนค่อยเริ่มทำ

## วิธีการในบริบท AI Speed
1. **เตรียม Test Case ก่อน:** เขียนหรือออกแบบ Test Case ให้เสร็จตั้งแต่ก่อนเริ่ม Coding (หรือก่อน Sprint Planning)
2. **Clear Definition of Done:** ทำให้ทุกคนเห็นภาพตรงกันว่า "งานเสร็จ" คืออะไรตั้งแต่แรก
3. **ลดการรอคอย:** เมื่อโค้ดเสร็จ ทีมสามารถเทสได้ทันทีเพราะมีเกณฑ์การตัดสินรอไว้อยู่แล้ว

## ผลลัพธ์
- ลดระยะเวลาใน stage "Ready to Test"
- ลดอัตราการ Reject งานกลับไปแก้
- เป็นพื้นฐานสำคัญของการทำ Self-testing โดย Developer

## โยงกับ harness ของ coding agent

[[birgitta-bockeler|Birgitta Böckeler]] ต่อยอดหลัก "keep quality left" เข้ากับ coding agent ใน [[harness-guides-sensors]]: feedback sensor (test, linter, review agent) ควรกระจายตาม lifecycle ตามต้นทุน/ความเร็ว — ของเร็วรันก่อน commit, ของแพง (mutation testing, review ภาพรวม) รันใน pipeline จุดต่างคือ sensor พวกนี้ไม่ได้ป้อนกลับให้แค่คน แต่ป้อนเข้า self-correcting loop ของ agent ด้วย

[[addy-osmani|Addy Osmani]] เติมมุม code review ใน [[agentic-code-review]]: เมื่อ agent เขียนโค้ดเยอะขึ้น CI ต้องเป็น "กำแพงที่ไม่ขยับ". Agent อาจลบ test, skip lint, ลด coverage threshold, หรือแก้ assertion ให้ตรงกับ behavior ที่ผิดเพื่อให้เขียว. ดังนั้น test diff ต้องอ่านก่อน และ gate แบบ deterministic ต้องแข็งกว่าเดิม

## See also
- [[lead-time]]
- [[theory-of-constraints]]
- [[harness-guides-sensors]]
- [[birgitta-bockeler]]
- [[agentic-code-review]]
