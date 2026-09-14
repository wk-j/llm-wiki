---
title: Claude Opus 5
type: entity
tags: [ai, models, anthropic, claude, opus, agents, safety]
created: 2026-09-10
updated: 2026-09-10
sources: [boris-cherny-cut-80-percent-claude-code-prompt.md]
---

# Claude Opus 5

**Claude Opus 5** คือ model ในตระกูล [[claude|Claude]] ของ [[anthropic|Anthropic]] ใน [[boris-cherny-cut-80-percent-claude-code-prompt|บทสัมภาษณ์ที่ Y Combinator]] [[boris-cherny|Boris Cherny]] บอกว่าเปิดตัวก่อนวันสัมภาษณ์หนึ่งวัน แต่ wiki ยังไม่ได้ ingest release note, model card, ราคา หรือ benchmark ทางการ จึงยังไม่ระบุวันเปิดตัวแบบปฏิทินและไม่เติม spec ที่ transcript ไม่ได้ให้มา

## สิ่งที่ Boris อ้างในเวทีนี้

- ทำงานต่อเนื่องได้เป็นวัน สัปดาห์ หรือเดือน โดยเฉพาะเมื่อใช้กับ auto mode
- ฉลาดพอให้ทีม Claude Code ลบ system prompt ออกราว 80% เพราะคำสั่งที่เคยชดเชย model รุ่นก่อนหมดความจำเป็น
- เมื่อต่อกับ model alignment, prompt-injection classifier และ auto-mode classifier ทีมยังสาธิต prompt injection ให้สำเร็จไม่ได้
- vision กับ computer use ดีขึ้นมาก แต่การตรวจ UI ที่คลาดระดับ pixel ยังไม่สมบูรณ์
- ทำงานระดับ rewrite ข้ามภาษาได้ และ Boris เชื่อว่า Opus 5 ทำเคสแบบ Bun Zig-to-Rust ได้เช่นกัน

ทุกข้อเป็น first-party claim จากบทสัมภาษณ์ ไม่ใช่ผลทดสอบอิสระ

## ความสัมพันธ์กับ Opus 4.8 และ Fable

หน้า [[claude-opus-4-8|Opus 4.8]] เก็บสถานะว่าเป็น flagship ตอนเปิดตัว 28 พฤษภาคม 2026 ส่วนบทสัมภาษณ์ใหม่นี้บอกว่า Opus 5 เพิ่งออกภายหลัง จึงเก็บทั้งสอง claim ตามเวลา ไม่แก้ประวัติว่า 4.8 เคยเป็น flagship

[[fable|Claude Fable 5]] ก็ยังเป็น entity แยก ตอนเล่า [[bun-in-rust|Bun rewrite]] Boris บอกว่า Fable เป็นรุ่นที่เริ่มทำงานนี้ได้ และ Opus 5 ก็น่าจะทำได้ คำพูดนี้ชี้ว่าสองชื่อไม่ควรถูก merge โดยไม่มีหลักฐานเพิ่ม

## ขอบเขตด้านความปลอดภัย

คำว่า prompt injection “สาธิตไม่ได้แล้ว” เป็นสัญญาณว่าพฤติกรรม model ดีขึ้น แต่ไม่ได้ลบ threat model ของ [[agent-runtime-untrusted]] ระบบที่เข้าถึงไฟล์ network หรือ production tool ยังควรมี permission, sandbox, allowlist และ audit trail อยู่นอก model

**ได้อะไร:** ความต้านทานของ model เป็น defense อีกชั้น ไม่ใช่เหตุผลให้รื้อ control ที่ตรวจสอบได้ออก

## See also

- [[claude]]
- [[anthropic]]
- [[claude-code]]
- [[claude-opus-4-8]]
- [[fable]]
- [[boris-cherny]]
- [[prompt-ablation]]
- [[model-elicitation]]
- [[agent-runtime-untrusted]]
