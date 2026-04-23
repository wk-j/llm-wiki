---
title: Adaptive Thinking
type: concept
tags: [ai, claude, anthropic, api, reasoning]
created: 2026-04-19
updated: 2026-04-23
sources: [claude-opus-4-7-whats-new-docs]
---

# Adaptive Thinking / การคิดแบบปรับตัวของ Claude

**Adaptive thinking** คือ `thinking mode` เดียวที่ [[claude-opus-4-7|Opus 4.7]] รองรับ โดย Model จะตัดสินใจเองว่าจะใช้เวลาคิดนานแค่ไหนตามความซับซ้อนของงาน แทนที่ API caller จะต้องกำหนด `thinking budget` เป็นตัวเลขตายตัวเหมือนในรุ่นก่อนหน้า

## จาก Extended สู่ Adaptive

ใน Opus 4.6, การเปิดใช้งาน thinking จะใช้ pattern ที่เรียกว่า **extended thinking** โดย API caller จะส่ง `thinking: {"type": "enabled", "budget_tokens": 32000}` เพื่ออนุญาตให้ model คิดได้ไม่เกินจำนวน token ที่กำหนด วิธีนี้มีข้อดีคือคาดเดาได้ แต่ข้อเสียคือผู้ใช้ประเมินได้ยากว่าแต่ละงานต้องใช้ thinking budget เท่าไหร่

ใน Opus 4.7, pattern นี้ถูกยกเลิกไปทั้งหมด:

```python
# Before (Opus 4.6)
thinking = {"type": "enabled", "budget_tokens": 32000}

# After (Opus 4.7)
thinking = {"type": "adaptive"}
output_config = {"effort": "high"}
```

หากยังส่ง `budget_tokens` ไปที่ Opus 4.7 จะได้รับ **400 error** กลับมาทันที Anthropic ระบุว่าจากการทดสอบภายใน `adaptive` ให้ผลลัพธ์ที่ดีกว่า `extended` อย่างมีนัยสำคัญ จึงตัดสินใจเลิกใช้ budget-based thinking ไปเลย

## ค่าเริ่มต้นคือ "ปิด"

โดยปกติแล้ว adaptive thinking จะ**ถูกปิดเป็นค่าเริ่มต้น**บน Opus 4.7 Request ที่ไม่ได้ระบุ field `thinking` จะหมายถึง "ไม่ต้องคิด" หากต้องการให้ model คิด, เราต้องใส่ `thinking: {"type": "adaptive"}` ไปใน request อย่างชัดเจน ซึ่งต่างจาก Opus 4.6 ที่ในบาง setup, thinking อาจถูกเปิดใช้งานอยู่แล้วโดยอัตโนมัติ ดังนั้นควรตรวจสอบ code เดิมว่ามีการ opt-in ไว้อย่างไร

## Thinking output ก็หายไปโดยปริยาย

อีกหนึ่ง breaking change ที่ซ่อนอยู่คือ **โดย default แล้ว `thinking content` จะไม่ถูกส่งกลับมาใน response** ถึงแม้ stream จะยังมี block `thinking` อยู่ แต่ content ข้างในจะเป็น string ว่างเปล่า เว้นแต่เราจะ opt-in

```python
thinking = {
    "type": "adaptive",
    "display": "summarized",  # หรือ "omitted" (ค่า default)
}
```

ผลกระทบคือ: ถ้า product ของเรามีการ stream reasoning ให้ user ดู (เช่น แสดงข้อความ "กำลังคิด...") เมื่อเปลี่ยนมาใช้ 4.7 จะกลายเป็น**การหยุดค้างไปนาน (long pause) ก่อนจะมี output** ออกมา วิธีแก้คือให้เพิ่ม `display: "summarized"` เพื่อให้ model ส่ง progress การคิดกลับมาเหมือนเดิม

## ความสัมพันธ์กับ Effort Level

Adaptive thinking ไม่ใช่สิ่งเดียวกับ [[effort-levels|effort level]] แต่เป็นสองสิ่งที่ทำงานคู่กัน:

- `effort` เป็นการบอก *capability tier* ของ model — `medium` / `high` / `xhigh` / `max`
- `thinking: adaptive` เป็นการให้ *สิทธิ์* model ในการคิดพิจารณาก่อนจะตอบ

คำแนะนำของ Anthropic คือ: สำหรับ Opus 4.7 ให้ใช้ `xhigh` สำหรับงาน coding/agentic, `high` เป็นอย่างน้อยสำหรับงานที่ต้องการความแม่นยำสูง และเปิด adaptive thinking ควบคู่ไปด้วยเสมอถ้าต้องการคุณภาพผลลัพธ์ที่ดีที่สุด

## See also

- [[claude-opus-4-7]]
- [[claude-opus-4-7-whats-new-docs]]
- [[effort-levels]]
- [[task-budgets]]
