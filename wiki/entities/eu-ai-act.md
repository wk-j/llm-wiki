---
title: EU AI Act
type: entity
tags: [regulation, ai, eu, transparency, policy]
created: 2026-08-16
updated: 2026-08-16
sources: [claude-text-watermarking-squintist.md]
---

# EU AI Act

กฎหมายกำกับ AI ของสหภาพยุโรป ใน wiki นี้เข้ามาผ่านมุมเดียวก่อน: **Article 50 (transparency)** ซึ่งเป็นเหตุผลหลักที่ lab ใหญ่เริ่ม [[llm-text-watermarking|watermark ข้อความ]] — ตามที่ [[claude-text-watermarking-squintist|วิดีโอของ Squintist]] สรุปว่า "ทำไม lab ถึงทำ? คำตอบสั้น ๆ คือ Brussels"

## Article 50: ภาระ mark เนื้อหา AI

- ตั้งแต่ **2 สิงหาคม** (2026 ตาม timeline ของวิดีโอ) output ของ generative AI ต้องถูก mark แบบ **machine-readable** — เหตุผลของ EU: เมื่อเครื่อง generate ได้วันละล้านคำ คนต้องมีทางแยกข้อความเครื่องจากข้อความคน (fake reviews, fraud, impersonation)
- มี**ข้อยกเว้น standard editing**: แก้สะกด แก้ grammar และแปลภาษา ไม่ต้อง mark — European Commission มี guideline แยกว่าอะไรนับเป็น standard editing

จุดตึงที่ควรจำ: กฎหมายยกเว้นงานแก้เล็ก แต่ [[anthropic|Anthropic]] mark ทุกอย่างที่ผ่าน model อยู่ดี เพราะ watermark ฝังที่ sampler แยกประเภทงานไม่ได้ — ผลคือรายงานที่คนเขียนเองแล้วให้ Claude ขัด grammar ก็อาจติด mark ทั้งที่กฎหมายไม่บังคับ

## Code of Practice on Transparency

Code of Practice ของ European Commission เติมรายละเอียดที่กฎหมายไม่ระบุ:

- Watermark ข้อความ free-form ที่ยาวกว่าหนึ่งย่อหน้าจริงจัง
- ให้คนตรวจ mark ได้ฟรี — แต่สำหรับ **plain text** ยอมให้จำกัดตัวตรวจไว้กับ verified experts ก่อน เพราะ text mark เป็นชนิดที่เชื่อถือได้น้อยที่สุด (ล้างออกได้ ดู [[llm-text-watermarking]])
- ผู้ลงนาม: **Anthropic, Google, OpenAI, Meta, Microsoft, Mistral** — ตัว code เป็น voluntary แต่กฎหมายข้างหลังไม่ใช่

## ช่องที่ยังบังคับไม่ถึง

[[open-weight-models|Open model]] ที่คนดาวน์โหลดไปรันเอง บังคับให้ watermark ไม่ได้ เพราะคนรันคุม sampling เอง — คนที่อยากล้าง mark ใช้ open model 9B บนเครื่องบ้าน rewrite ข้อความก็จบ นี่คือช่องว่างเชิงบังคับใช้แบบเดียวกับที่ [[frontier-ai-standards-body|ข้อเสนอ governance ของ Hassabis]] เจอ: weights ที่แพร่แล้วเรียกคืนไม่ได้

## คำถามเปิด

- วิดีโอเล่าเฉพาะมุม Article 50 — ส่วนอื่นของ AI Act (risk tiers, GPAI obligations, enforcement) ยังไม่มี source ใน wiki
- ผลจริงต่อผู้ใช้นอก EU และรายละเอียด rollout ต่อ lab แต่ละเจ้า ยังต้องตามจากเอกสารต้นทาง

## See also

- [[claude-text-watermarking-squintist]]
- [[llm-text-watermarking]]
- [[synthid]]
- [[ai-text-detectors]]
- [[open-weight-models]]
- [[frontier-ai-standards-body]]
