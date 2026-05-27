---
title: Hashline
type: concept
tags: [ai, harness, coding, tools, agents]
created: 2026-05-27
updated: 2026-05-27
sources: [improved-15-llms-harness-changed.md]
---

# Hashline / แฮชไลน์

**Hashline** คือรูปแบบ edit tool ที่ [[can-boluk|Can Bölük]] ใส่ใน [[oh-my-pi|oh-my-pi]] — แทนที่จะให้ model คัดลอก old text กลับมา (แบบ `str_replace`) หรือเขียน diff string (แบบ `apply_patch`) model แค่ **อ้าง identifier สั้น ๆ ต่อบรรทัด** ที่ harness แปะให้ตอน read/grep

## ทำงานยังไง

พอ model เห็นไฟล์ แต่ละบรรทัดจะมาในรูป `lineNumber:contentHash|content`:

```fallback
1:a3|function hello() {
2:f1|  return "world";
3:0e|}
```

คำสั่ง edit ก็แค่อ้าง tag — replace บรรทัด `2:f1`, replace ช่วง `1:a3`–`3:0e`, หรือ insert หลัง `3:0e` ถ้าไฟล์เปลี่ยนหลัง read ครั้งล่าสุด แฮชไม่ตรง harness **reject ก่อนเขียน** (เป็น optimistic concurrency กลาย ๆ)

**หลัก:** ถ้า model จำ tag สั้น ๆ ได้ ก็แปลว่ารู้ anchor จริง — ไม่ต้องมานั่งพิสูจน์ด้วยการ reproduce whitespace ทั้งก้อน

## ทำไมถึงสำคัญ

ใน [[improved-15-llms-harness-changed|benchmark ของ Can]] (16 model, งานแก้ bug ในไฟล์ React):

- **Patch แย่ที่สุด** เกือบทุกตัว — model เก่งจริงแต่ความสามารถถูกบังด้วย mechanical failure
- **Hashline ชนะหรือเสมอ Replace** ส่วนใหญ่; **Hashline v2** ดีขึ้นอีก 12/16
- **ตัวอ่อนยิ่งได้เยอะ** — เช่น Grok Code Fast 1 จาก 6.7% → 68.3%
- **Gemini 3 Flash:** +8pp success, ~−21% output tokens (รวมแล้ว benchmark ทั้งชุด ~$300)

> "+8% improvement in the success rate of Gemini is bigger than most model upgrades deliver, and it cost zero training compute."

**ได้อะไร:** ปรับ harness ที่ edit boundary บางครั้งให้ผลเทียบเท่า upgrade model เลย — แล้วก็ไม่ต้องใช้ training compute สักนิด

## เทียบกับแนวอื่น

ดูตารางเต็มที่ [[edit-tool-formats]] — สรุปสั้น ๆ:

| แนว | ปัญหาหลัก |
|---|---|
| Patch / diff string | model ต้องเขียนตาม diff format เฉพาะของ vendor |
| str_replace | ต้อง match ตัวอักษรเป๊ะ; เจอหลายที่ = reject |
| Fine-tuned merge (Cursor) | บวกต้นทุน model เพิ่ม; ไฟล์สั้นยังสู้ full rewrite ไม่ได้ |
| **Hashline** | ต้องมี hash ใน context; ไม่ใช่ทุก model ที่ได้กำไร (เช่น DeepSeek V3.2) |

## See also

- [[edit-tool-formats]]
- [[improved-15-llms-harness-changed]]
- [[oh-my-pi]]
- [[can-boluk]]
- [[coding-harness]]
- [[llm-coding-pitfalls]]
