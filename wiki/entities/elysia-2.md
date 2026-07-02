---
title: Elysia 2
type: entity
tags: [software, ai-coding, codebase, release]
created: 2026-07-02
updated: 2026-07-02
sources: [aom-fable-elysia-2-audit.md]
---

# Elysia 2 / เอลิเซีย 2

[[elysia-2|Elysia 2]] คือ codebase/project ที่ [[aom-khunpanitchot|Aom Khunpanitchot]] พูดถึงใน source [[aom-fable-elysia-2-audit|Fable audit Elysia 2]]. จากโพสต์นี้ Aom เขียนและดูแล codebase นี้มาประมาณ 4 ปี และกำลังตัดสินใจว่าจะขยับสถานะจาก alpha ไป stable/RC ได้หรือยัง.

Capture ที่ให้มาไม่มี repo, product page, หรือคำอธิบาย domain ของ Elysia 2. ดังนั้นหน้านี้บันทึกเฉพาะบทบาทของมันในแหล่งนี้: เป็น codebase จริงที่ใช้ทดสอบความลึกของ AI code audit.

## บทบาทใน source นี้

ก่อนใช้ [[fable|Fable]], Aom ให้ AI หลายตัว audit Elysia 2 แล้วส่วนใหญ่บอกว่าพร้อม stable release หรือ RC. เขายังลอง update plugin 11 ตัวและบอกว่าทำงานได้แทบไม่ต้องแก้ code. นี่ทำให้เขาเชื่อว่า Elysia 2 น่าจะพร้อมขยับสถานะ.

Fable กลับสรุปต่าง: ยังไม่เหมาะขึ้น RC และส่ง report 104 ข้อ. ความต่างนี้ทำให้ Elysia 2 กลายเป็นเคสตัวอย่างของ release judgement ในยุค agent: คำว่า "พร้อม" ไม่ควรมาจาก model verdict เดี่ยว แต่ควรมาจากปัญหา, severity, evidence, และ owner decision.

**ได้อะไร:** Elysia 2 เป็นสนามจริงที่โชว์ว่า [[deep-agent-audit|deep agent audit]] อาจเปลี่ยน release confidence ได้ แม้ plugin smoke test และ AI reviewer ตัวอื่นดูผ่าน.

## See also

- [[aom-fable-elysia-2-audit]]
- [[aom-khunpanitchot]]
- [[fable]]
- [[deep-agent-audit]]
- [[agentic-code-review]]
- [[model-honesty]]
