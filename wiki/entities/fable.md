---
title: Fable
type: entity
tags: [ai, agents, code-review, coding-harness]
created: 2026-07-02
updated: 2026-07-02
sources: [aom-fable-elysia-2-audit.md]
---

# Fable / เฟเบิล

[[fable|Fable]] คือ AI agent/harness ที่ปรากฏใน source [[aom-fable-elysia-2-audit|Fable audit Elysia 2]]. จากโพสต์นี้ Fable ถูกใช้ทำ code review/audit แบบหนักกับ [[elysia-2|Elysia 2]] โดยเปิด ultracode auto mode และแตกตัวเป็น agent เกือบ 100 ตัว.

ข้อมูลใน wiki ตอนนี้มาจากโพสต์เดียว จึงควรอ่านแบบระวัง: ยังไม่รู้แน่ชัดว่า Fable เป็น model, harness, product surface, หรือชุด workflow ที่ห่อ model หลายตัวไว้ข้างใน.

## สิ่งที่ source นี้อ้าง

ในเคส Elysia 2, [[aom-khunpanitchot|Aom Khunpanitchot]] เล่าว่า Fable:

- ใช้ prompt สั้นมากเมื่อเทียบกับ agent อื่นที่เขาสั่ง audit แบบละเอียด
- รันยาวผ่าน ultracode auto mode จนชน limit
- แตก agent เกือบ 100 ตัว
- สร้าง report 104 ข้อ ยาวประมาณ 24,000 คำ / 174,000 ตัวอักษร
- สรุปว่า Elysia 2 ยังไม่เหมาะขึ้น RC แม้ AI ตัวอื่นบอกว่าพร้อม stable หรือ RC

**ได้อะไร:** Fable ใน source นี้เป็นหลักฐานเชิงประสบการณ์ว่า agent fan-out + long-running audit อาจให้ผลต่างจากการถาม frontier model ทีละตัว.

## Caveat

ยังไม่มี report 104 ข้อใน wiki และยังไม่ได้ verify ว่าปัญหาแต่ละข้อจริงหรือสำคัญแค่ไหน. ดังนั้นหน้านี้ไม่ควรสรุปว่า Fable "ถูกกว่า" agent อื่นทั้งหมด. สิ่งที่ยืนยันได้จาก source คือ Aom รับรู้ว่า report ของ Fable ลึกและ actionable กว่าการ review ที่เขาเคยได้จาก model อื่นในงานนี้.

## See also

- [[aom-fable-elysia-2-audit]]
- [[elysia-2]]
- [[deep-agent-audit]]
- [[agentic-code-review]]
- [[coding-harness]]
- [[dynamic-workflows]]
