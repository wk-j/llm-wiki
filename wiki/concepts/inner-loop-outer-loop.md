---
title: Inner Loop Outer Loop
type: concept
tags: [ai, agents, loop-engineering, orchestration, workflow]
created: 2026-07-05
updated: 2026-07-05
sources: [piyalitt-codex-keynote-attention-not-token.md, stop-building-ai-agents-old-way.md, loop-engineering-osmani.md]
---

# Inner Loop / Outer Loop / ลูปใน–ลูปนอก

**Inner loop / outer loop** คือวิธีแบ่งงานระหว่าง agent กับมนุษย์ในงานยาว ๆ: **agent ทำงานวนชั้นใน** เช่น สืบหา แก้ รัน test และให้ agent อีกตัวรีวิวซ้ำ ส่วน **มนุษย์อยู่ชั้นนอก** คอยกำหนดเป้าหมาย ตัดสินใจเรื่อง product และอนุมัติ merge เมื่อถึงจังหวะที่ต้องใช้ judgement จริง ๆ

[[peter-steinberger|Peter Steinberger]] วาดภาพนี้บนเวที Codex keynote (สรุปใน [[piyalitt-codex-keynote-attention-not-token]]) เพราะมันทำให้ [[loop-engineering|loop engineering]] ดูเป็นงานจริง ไม่ใช่แค่คำสวย ๆ เรื่อง automation

## Loop ของ Peter (open source project)

1. มีคนเปิด issue เข้ามา
2. **Manager agent** ตื่นขึ้นมา → เทียบ issue กับเป้าหมาย/วิสัยทัศน์ของ project → ตัดสินใจว่าน่าทำไหม
3. ถ้าใช่ → สร้าง **worker** หนึ่งตัวให้สืบหา แก้ และรัน test
4. **Agent อีกตัว** รีวิวผลลัพธ์ซ้ำอีกชั้น
5. Peter **ไม่ต้อง** นั่งดู agent ทำงานหรืออ่านทุกข้อความระหว่างทาง
6. เมื่อ manager ต้องการ Peter จริง ๆ → ส่ง PR พร้อม issue ต้นทาง + diff (บางครั้งแถมวิดีโอ/build ให้ VNC ดู)
7. Peter รีวิวรอบเดียว ทิ้งโน้ต หรืออนุมัติ → loop หมุนต่อจน merge เองหลังผ่านการตรวจครบ

**ผลคือ:** มนุษย์จ่าย [[attention-bottleneck|attention]] แค่จังหวะที่ judgement สร้างความแตกต่าง ไม่ใช่ทุก tool call

## จาก polling สู่ orchestration จริง

Peter ยอมรับว่าเคยเปิด 10+ terminal แล้วรู้สึกว่ากำลัง orchestrate แต่จริง ๆ แค่ **polling**. ตัวเขาเองเป็น scheduler, router, และ memory ของทั้งระบบ. การย้ายไปใช้ **manager agent ตัวเดียว** กับ worker หลายตัว คือการย้ายงานวนชั้นในไปอยู่ในระบบ แทนที่จะเก็บไว้ในหัวคน

สามชิ้นที่ทำให้ทำได้:

1. Server-side compaction (session ยาวเสถียร)
2. ระบบประสานงาน (thread เดียวคุมหลาย project)
3. Automation ปลุก manager เมื่อมีเหตุการณ์

## ความต่างจาก outer loop ใน long-running agent controls

[[stop-building-ai-agents-old-way]] ใช้คำ **outer loop** ในความหมายของ control system: มี evaluator แยกจาก executor, มี verifier เป็นหลักฐาน, และกันไม่ให้ agent หยุดเร็วเกินไป. แนวคิดสอดคล้องกันตรงที่ชั้นบนไม่ได้ลงมือทำ execution เอง แต่คุมเกณฑ์และตัดสินเมื่อหลักฐานพอ

| มุม | Peter (keynote) | Prompt Engineering (video) |
|---|---|---|
| Inner loop | manager → worker → reviewer agent | executor agent + tools |
| Outer loop | Peter อนุมัติ PR / ทิ้งโน้ต | human + evaluator + verifiers + goal contract |
| เป้าหมาย | ไม่ polling; attention ไปที่ judgement | agent รันยาวไม่หลุดทาง |

## โจทย์ที่ยังเปิด

Peter บอกว่ายังไม่มีรูปแบบสุดท้าย. Manager ไม่ควรผูกกับโน้ตบุ๊กหรือแอปเดียว ควรสั่งผ่าน Slack ได้ และเมื่อเราบอกเป้าหมาย **agent ควรออกแบบ loop ทั้งหมดให้เราเอง** ได้เลย. วันนี้ยังไม่มีใครแก้สำเร็จ

## See also

- [[piyalitt-codex-keynote-attention-not-token]]
- [[peter-steinberger]]
- [[loop-engineering]]
- [[attention-bottleneck]]
- [[orchestration-tax]]
- [[long-running-agents]]
- [[stop-building-ai-agents-old-way]]
