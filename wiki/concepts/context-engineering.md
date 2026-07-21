---
title: Context Engineering
type: concept
tags: [ai, context, prompt-engineering, agent-harness, documentation]
created: 2026-07-21
updated: 2026-07-21
sources: [teepagorn-ten-lessons-building-with-ai.md, mikelopster-loop-engineering.md, self-learning-for-agents-explained.md]
---

# Context Engineering / การจัดบริบทให้ AI ทำงานได้

**Context engineering** คือการจัดทุกอย่างที่ model ต้องเห็นเพื่อทำงานให้ถูก ไม่ใช่แค่เขียน prompt ให้ฟังดี สิ่งที่ต้องจัดอาจเป็นไฟล์ กฎ ตัวอย่าง tool, memory, test, error message และโครงสร้าง repo ที่ช่วยบอกว่าอะไรอยู่ตรงไหน

ใน [[teepagorn-ten-lessons-building-with-ai|10 บทเรียนจากการสร้างของด้วย AI]] ผู้เขียนสรุปสั้น ๆ ว่า AI ตอบได้ดีเท่ากับสิ่งที่มันเห็น ถ้า context ไม่พอ model ต้องเดา ส่วน [[mikelopster-loop-engineering]] วาง context engineering ไว้ระหว่าง prompt กับ loop: จากการสั่งครั้งเดียว ไปสู่การเตรียม environment ให้ agent วิ่งงานซ้ำได้โดยไม่หลง

## Prompt ต่างจาก context อย่างไร

- **Prompt** บอกงานรอบนี้ เช่น “เพิ่ม endpoint สำหรับยกเลิก order”
- **Context** ทำให้คำสั่งนั้นมีความหมาย เช่น schema, state transition, auth rule, coding convention, test เดิม และตัวอย่าง response
- **Harness** คุมว่า context ใดถูกส่งเมื่อไร และส่ง feedback อะไรกลับหลัง agent ลงมือ

Prompt ที่ชัดแต่ไม่มี context อาจได้ implementation ที่ดูสมเหตุผลแต่ผิดระบบ ส่วน context เยอะแต่ไม่คัดก็ทำให้ model เสีย attention กับข้อมูลที่ไม่เกี่ยวข้องและเกิด [[context-rot|context rot]]

**ได้อะไร:** คุณภาพไม่ได้มาจาก “คำสั่งมหัศจรรย์” แต่มาจากการให้หลักฐานและข้อจำกัดที่จำเป็นในเวลาที่เหมาะ

## Context มีหลายรูปแบบ

| รูปแบบ | ตัวอย่าง | ช่วยเรื่องอะไร |
| --- | --- | --- |
| โครงสร้าง | folder, filename, module boundary | ทำให้หาเจ้าของความรับผิดชอบเจอ |
| กฎ | AGENTS.md, style guide, architecture decision | ลดการเดา convention |
| ตัวอย่าง | fixture, screenshot, prior implementation | ทำให้ preference ที่อธิบายยากเห็นเป็นรูปธรรม |
| หลักฐานรันจริง | test, type error, log, metric | บอกว่า output ชนโลกจริงตรงไหน |
| ความจำ | decision, user preference, prior failure | ไม่ต้องเริ่มอธิบายใหม่ทุก session |
| Tool access | repo search, database read, browser | ให้ agent ไปดึง context ที่ต้องใช้เอง |

โครงสร้างที่ดีจึงเป็น context แบบเงียบ ๆ ชื่อและตำแหน่งไฟล์ช่วยบอกความหมายก่อนอ่านเนื้อหา ส่วน test และ error เป็น context ที่เครื่องสร้างให้หลังลงมือ

## ปัญหาของงาน high-context

ผู้เขียนโพสต์ Facebook ตั้งข้อสังเกตว่า งานที่ต้องอธิบายบริบทเยอะอาจใช้เวลาถ่ายทอดนานกว่าทำเอง นี่คือ **context transfer cost** ถ้างานเกิดครั้งเดียว การลงมือเองอาจถูกกว่า แต่ถ้างานจะเกิดซ้ำ การลงทุนทำ docs, test, example หรือ harness อาจคืนทุนในรอบถัดไป

วิธีคิดง่าย ๆ คือถามสามข้อ:

1. Context นี้ใช้ซ้ำกับงานอื่นได้ไหม
2. Agent ดึงจาก source of truth เองได้ไหม หรือคนต้องเล่าใหม่ทุกครั้ง
3. มี verifier ที่บอกได้ไหมว่า agent เข้าใจ context ถูก

ถ้าคำตอบคือใช้ครั้งเดียว ดึงเองไม่ได้ และตรวจยาก งานนั้นอาจยังเหมาะกับมนุษย์มากกว่า

**ผลคือ:** เป้าหมายไม่ใช่ยัด context ให้มากที่สุด แต่ลดค่าใช้จ่ายในการส่ง “บริบทที่ใช่” ซ้ำ ๆ

## ส่งทีเดียวหรือส่งเมื่อจำเป็น

Context engineering ไม่ได้แปลว่าต้อง front-load ทุกอย่าง [[just-in-time-context|Just-in-Time Context]] เสนอให้ส่งกฎหรือคำแนะนำเมื่อมี trigger เช่น lint fail, test fail หรือ reviewer พบปัญหา วิธีนี้ลด noise และทำให้ feedback ตรงกับ error ที่เพิ่งเกิด

อีกด้าน งานที่มี invariant สำคัญ เช่น security boundary หรือข้อห้ามทางกฎหมาย อาจต้องส่งก่อนลงมือ ไม่ควรรอให้ระบบพังแล้วค่อยเตือน การเลือก timing จึงขึ้นกับผลเสียของการเดาผิดและความแน่นอนของ trigger

## คำถามที่ยังเปิดอยู่

- Context ชนิดใดควรอยู่ใน prompt, file, tool, memory หรือ verifier
- จะวัดได้อย่างไรว่า context “พอ” โดยไม่รอ production failure
- เมื่อ docs กับ code ขัดกัน agent ควรเชื่ออะไร และใครต้องแก้ source of truth
- Context ที่ช่วย model วันนี้จะกลายเป็นข้อจำกัดเกินจำเป็นเมื่อ model รุ่นใหม่เก่งขึ้นหรือไม่
- การทำให้ agent อ่านง่ายจะทำให้ structure แย่สำหรับคนหรือ tool อื่นหรือเปล่า

## ดูเพิ่ม

- [[teepagorn-ten-lessons-building-with-ai]]
- [[just-in-time-context]]
- [[context-rot]]
- [[coding-harness]]
- [[harness-engineering]]
- [[map-vs-territory]]
- [[unknowns-matrix]]
- [[llm-knowledge-bases]]
