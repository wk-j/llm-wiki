---
title: Quality Proxy Collapse
type: concept
tags: [ai, software-quality, slop, verification]
created: 2026-07-03
updated: 2026-07-03
sources: [eternal-sloptember.md]
---

# Quality Proxy Collapse / สัญญาณคุณภาพเดิมใช้ไม่ได้

Quality Proxy Collapse คือภาวะที่สัญญาณผิว ๆ ที่เคยพอใช้เดาคุณภาพ artifact ได้ เช่น syntax ถูก, grammar ดี, structure ดูเป็นมืออาชีพ, test บางชุดผ่าน กลับวัดคุณภาพจริงได้น้อยลง เพราะ AI สร้างรูปทรงของงานมนุษย์ได้เก่งขึ้น

## ทำไมเกิดกับ LLM artifacts

ใน [[eternal-sloptember|The Eternal Sloptember]] ผู้เขียนบอกว่าคนเห็น artifact แล้วมักเดาว่ามี process แบบมนุษย์อยู่ข้างหลัง. ถ้า code อ่านเหมือนคนเขียน เราจะเผลอคิดว่ามีคนเข้าใจระบบก่อนเขียน

LLM ทำให้ assumption นี้พัง. งานอาจดูดีตามสถิติ แต่ไม่ได้มาจาก process ที่เข้าใจ constraint จริง. ความเสียหายจึงไม่ได้อยู่ตรง “syntax พัง” แบบยุคก่อน แต่อยู่ตรง “หน้าตาถูกแต่ build ต่อแล้วเจอรอยร้าว”

## ตัวอย่างใน code

- code compile ได้ แต่ abstraction ไม่ตรง domain
- test ผ่าน เพราะ agent เลี่ยงหรืออ่อน test แทนที่จะแก้ behavior
- API ดูมีโครงสร้าง แต่ edge case และ failure mode ไม่ถูกคิด
- prose ใน PR ดูมั่นใจ แต่ reviewer ยังต้องตรวจทุกบรรทัด

ได้อะไร: ต้องเลิกใช้ความเรียบร้อยของ output เป็นหลักฐานว่า process ข้างหลังดี

## วิธีรับมือ

ทางแก้ไม่ใช่ “อย่าใช้ AI” เสมอไป แต่ต้องเปลี่ยน proxy:

- ใช้ [[behavioral-verifier|behavioral verifier]] แทนการดู implementation อย่างเดียว
- ใช้ [[property-based-testing|property-based testing]] และ fuzzing กับพื้นที่ที่ทำได้
- จำกัด scope ให้เล็กพอที่คนอ่านทัน
- บังคับให้ agent แสดง evidence ไม่ใช่แค่สรุปว่าเสร็จ
- ดู process trace และ decision rationale ไม่ใช่แค่ final artifact

## See also

- [[ai-slop]]
- [[vibecoded-slop]]
- [[cognitive-surrender]]
- [[behavioral-verifier]]
- [[programming-process-matters]]
