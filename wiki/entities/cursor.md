---
title: Cursor
type: entity
tags: [company, product, ai, coding-harness, cloud-agents, ide]
created: 2026-06-05
updated: 2026-06-05
sources: [What we’ve learned building cloud agents.md, improved-15-llms-harness-changed.md]
---

# Cursor

**Cursor** คือบริษัทและผลิตภัณฑ์ AI coding — เป็น IDE/[[coding-harness|coding harness]] ที่ฝัง AI agent ไว้สำหรับเขียนและแก้โค้ด. นอกจาก editor บน laptop แล้ว Cursor ยังทำ **cloud agent** — agent ที่รันบน VM ในคลาวด์ ทำงานขนานและรันงานยาวข้ามวันได้ ดู [[cloud-agents]].

## สิ่งที่น่าจำ

- **ทำ harness ของตัวเอง ไม่ได้ใช้ของ vendor ตรง ๆ** — Cursor fine-tune model แยกสำหรับ merge edit เอง. [[can-boluk|Can Bölük]] ตั้งข้อสังเกตว่า แม้ Cursor จะมี merge model ของตัวเอง ก็ยังยอมรับว่าไฟล์สั้น ๆ การ rewrite ทั้งไฟล์ยังชนะ diff อยู่ ดู [[edit-tool-formats]].
- **Cloud agent infrastructure** — ในบล็อก [[what-weve-learned-building-cloud-agents|What We've Learned Building Cloud Agents]] (โดย [[josh-ma|Josh Ma]], 2026-06-02) Cursor เล่าว่า:
  - ย้าย agent loop ไปอยู่บน [[temporal|Temporal]] เพื่อ [[durable-execution|durable execution]] — ดัน reliability จาก "one 9" เป็นเกิน "two 9s"
  - Temporal จัดการ **50 ล้าน+ action/วัน** ข้าม **7 ล้าน+ workflow**
  - **มากกว่า 40% ของ PR ใน Cursor monorepo มาจาก cloud agent** และยังเพิ่มขึ้น
  - สร้างสิ่งที่เหมือน "enterprise IT สำหรับ agent" — secret redaction, network policy, credential management

## จุดยืนเชิงแนวคิด

บทเรียนหลักของ Cursor คือ การเอา agent ขึ้นคลาวด์ไม่ใช่แค่ port local agent ขึ้น server แต่เป็นการ **สร้าง operating layer รอบตัว agent** — environment, durability, conversation state ต้องประกอบใหม่หมด. โดยเฉพาะข้อสรุปว่า [[agent-development-environment|environment คือตัวสินค้า]] และแนวโน้ม **"รู้จักหลบให้ agent ทำงาน"** (ย้าย logic จาก harness ที่ deterministic ไปเป็น tool ที่ agent คุมเอง พอ model ฉลาดขึ้น).

## See also

- [[what-weve-learned-building-cloud-agents]]
- [[josh-ma]]
- [[cloud-agents]]
- [[temporal]]
- [[durable-execution]]
- [[agent-development-environment]]
- [[coding-harness]]
- [[edit-tool-formats]]
- [[can-boluk]]
