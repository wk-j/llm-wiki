---
title: Adaptive Thinking
type: concept
tags: [ai, claude, anthropic, api, reasoning]
created: 2026-04-19
updated: 2026-04-19
sources: [Whats new in Claude Opus 4.7 - Anthropic Docs.md]
---

# Adaptive Thinking / Adaptive Thinking ของ Claude

**Adaptive thinking** คือ thinking mode เดียวที่ [[claude-opus-4-7|Opus 4.7]] รองรับ. Model ตัดสินใจเองว่าจะคิดนานแค่ไหน ตาม task ที่เจอ — แทนที่จะให้ caller กำหนด thinking budget เป็นตัวเลขตายตัวแบบรุ่นเก่า.

## จากของเดิมสู่ของใหม่

Opus 4.6 ใช้ **extended thinking** — caller ส่ง `thinking: {"type": "enabled", "budget_tokens": 32000}` เพื่อให้ thinking ใช้ได้ไม่เกิน N token. มีข้อดีตรง predictable แต่ข้อเสียคือ caller เดาไม่ออกว่างานไหนต้องใช้ thinking กี่ token.

Opus 4.7 ยก pattern นี้ทิ้ง:

```python
# Before (Opus 4.6)
thinking = {"type": "enabled", "budget_tokens": 32000}

# After (Opus 4.7)
thinking = {"type": "adaptive"}
output_config = {"effort": "high"}
```

ส่ง `budget_tokens` แล้วจะได้ **400 error**. Anthropic บอกว่า adaptive ชนะ extended อย่าง reliable ใน internal eval เลยเลิกสาย budget ไปเลย.

## Default เป็น "off"

Adaptive thinking **ปิดไว้ก่อน** บน 4.7. Request ที่ไม่มี field `thinking` = ไม่คิด. ถ้าต้องการให้คิด ต้องใส่ `thinking: {"type": "adaptive"}` เอง. อันนี้ต่างจาก 4.6 ที่บาง setup thinking เปิดอยู่โดย default. ควรเช็ค code เดิมว่า opt in ไว้หรือไม่.

## Thinking output ก็หายไปเงียบ ๆ

Break เล็ก ๆ ที่ซ่อนอยู่: **thinking content ไม่ return มาแล้วเป็น default**. Stream ยังมี thinking block อยู่ แต่ field `thinking` ข้างในเป็น empty string — ถ้าไม่ opt in.

```python
thinking = {
    "type": "adaptive",
    "display": "summarized",  # หรือ "omitted" (ค่า default)
}
```

ผลคือ: ถ้า product stream reasoning ให้ user ดู (แบบ "กำลังคิด..." indicator) — พอย้ายมา 4.7 จะเห็นเป็น **long pause ก่อน output** แทน. แก้ด้วย `display: "summarized"` เพื่อโชว์ progress.

## ความสัมพันธ์กับ effort

Adaptive thinking ≠ [[effort-levels|effort level]]. ใช้คู่กัน:

- `effort` บอก *capability tier* — medium / high / xhigh / max
- `thinking: adaptive` บอกว่า model ได้ *สิทธิ์คิด* ก่อน respond

Anthropic แนะนำ: Opus 4.7 → ใช้ `xhigh` สำหรับ coding/agentic, ใช้ `high` เป็นขั้นต่ำสำหรับงาน intelligence-sensitive, และเปิด adaptive thinking ไว้ถ้าต้องการคุณภาพ.

## See also

- [[claude-opus-4-7]]
- [[claude-opus-4-7-whats-new-docs]]
- [[effort-levels]]
- [[task-budgets]]
