---
title: Peter Steinberger
type: entity
tags: [people, agents, openclaw, openai, loop-engineering]
created: 2026-07-05
updated: 2026-07-05
sources: [piyalitt-codex-keynote-attention-not-token.md]
---

# Peter Steinberger

**Peter Steinberger** (ชื่อเล่นในวงการ: **the Clawfather**) คือผู้สร้าง **OpenClaw** — ระบบ agent ที่ขยายขอบเขตสิ่งที่เป็นไปได้จนผลักให้ OpenAI ต้องคล่องตัวขึ้น. ตอนนี้ร่วมงานกับ [[openai|OpenAI]] แล้ว และขึ้นเวที keynote ของทีม [[openai-codex|Codex]] ใน [[ai-engineer-worlds-fair|AI Engineer World's Fair]] (สรุปใน [[piyalitt-codex-keynote-attention-not-token]])

## ทำไมถึงน่าฟัง

Peter เป็นตัวอย่าง power user ที่เปลี่ยนวิธีทำงานเร็วกว่า harness ของตลาด — จาก 10+ terminal ที่คอย polling ไปเป็น **manager agent ตัวเดียว** ที่กระจายงานให้ worker. ประโยคที่ wiki อ้างบ่อยจากเขา:

> "I thought I was orchestrating, but I was just polling."

และ:

> "อนาคตไม่ใช่การเปิด terminal 20 หน้าต่าง แต่คือ loop ที่ดีกว่าเดิม"

## วิธีทำงานปัจจุบัน (ตาม keynote ผ่าน Piyalitt)

- คุยกับ **manager agent** ตัวเดียวรันต่อเนื่องระยะยาว → กระจายงานไปทีม worker
- งานยากจริงค่อยลงไป pair กับ worker โดยตรง
- สรุปตัวเองว่า: *บริหารผู้จัดการของบริษัทเล็ก ๆ ที่พนักงานเป็น agent*

สามอย่างที่ทำให้ loop นี้ทำงาน:

1. **Server-side compaction** — session ยาวเสถียร ไม่ต้องเปิดใหม่เลี่ยง context rot
2. **ระบบประสานงาน** — thread เดียวคุมหลาย project
3. **Automation** — ปลุก manager เมื่อมีเหตุการณ์ (issue ใหม่ ฯลฯ)

## Bottleneck ที่ย้ายที่

Peter เล่าว่าข้อจำกัดหลักย้ายตามลำดับ:

| ช่วง | ข้อจำกัด | วิธีแก้ (ชั่วคราว) |
|---|---|---|
| ปีที่แล้ว | token | เข้าไปทำงานที่ OpenAI (แซวว่า scale ไม่ได้) |
| ถัดมา | compute | test box — รัน test บนเครื่องอื่น |
| วันนี้ | [[attention-bottleneck\|attention]] | ไม่มีวิธีซื้อเพิ่ม — ต้องออกแบบ loop ให้รบกวนเราเฉพาะจังหวะที่ judgement สร้างความต่าง |

## Inner / outer loop

ใน open source project ของเขา: issue เข้ามา → manager ตัดสินใจ → worker สืบ/แก้/test → agent รีวิวอีกชั้น → ส่ง PR กลับเมื่อต้องการ Peter จริง ๆ → Peter รีวิวรอบเดียว อนุมัติหรือทิ้งโน้ต → loop หมุนต่อ. ดู [[inner-loop-outer-loop]]

## โจทย์ที่ยังเปิด

Peter บอกตรง ๆ ว่ายังไม่มีรูปแบบสุดท้ายสำหรับ manager ที่:

- ไม่ผูกกับโน้ตบุ๊กเครื่องเดียว
- เชื่อมทุกเครื่องของเขาเอง รู้เองว่างานไหน cloud ได้ งานไหนต้อง local
- ส่งข้อความหาได้จากทุกที่ (Slack ฯลฯ) ไม่ใช่แค่ session ในแอปเดียว
- **ออกแบบ loop ทั้งหมดให้เราเอง** เมื่อเราบอกเป้าหมาย — ยังไม่มีใครแก้สำเร็จ

เขาปิดว่า model พัฒนาเร็วกว่า harness และองค์กร — การออกแบบ harness คือโจทย์ engineering ข้อถัดไป

## ดูเพิ่ม

- [[piyalitt-codex-keynote-attention-not-token]]
- [[loop-engineering]]
- [[inner-loop-outer-loop]]
- [[attention-bottleneck]]
- [[orchestration-tax]]
- [[openai-codex]]
