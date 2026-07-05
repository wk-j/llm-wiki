---
title: Fable
type: entity
tags: [ai, agents, models, anthropic, code-review]
created: 2026-07-02
updated: 2026-07-05
sources: [aom-fable-elysia-2-audit.md, a-field-guide-to-fable-finding-your-unknowns.md, fables-judgement-simon-willison.md]
---

# Fable / เฟเบิล

**Claude Fable 5** คือ model ในตระกูล [[claude|Claude]] ของ [[anthropic|Anthropic]] ข้อมูลนี้ชัดขึ้นจาก source ที่สอง: [[field-guide-to-fable-finding-unknowns|A Field Guide to Fable]] โดย [[thariq-shihipar|Thariq Shihipar]] (ทีม [[claude-code|Claude Code]]) ซึ่งเรียกเต็ม ๆ ว่า "Claude Fable 5" และอ้างถึง launch video จากบัญชี ClaudeDevs ที่ตัดต่อด้วย Claude Code ทั้งตัว

ก่อนหน้านั้น Fable ปรากฏครั้งแรกใน [[aom-fable-elysia-2-audit|Fable audit Elysia 2]] ซึ่งหน้านี้เคยบันทึกเป็นคำถามเปิดว่า Fable เป็น model, harness, product surface, หรือชุด workflow — field guide เคลียร์แกนหลักแล้วว่าเป็น model แต่รายละเอียด spec/tier/pricing ยังไม่อยู่ใน wiki และคำว่า "ultracode auto mode" ในเคสของ Aom น่าจะเป็น harness/โหมดการรันที่ห่อ model อีกชั้น ซึ่งยังไม่มีข้อมูลตรง

## Claim หลักจาก field guide (2026-07)

Thariq อ้างว่า Fable เป็น model ตัวแรกที่คุณภาพงานถูกจำกัดด้วยความสามารถของ *ผู้ใช้* ในการเคลียร์ [[unknowns-matrix|unknowns]] ไม่ใช่ความสามารถของ model — ยิ่ง model แรง คอขวดยิ่งย้ายมาที่ [[map-vs-territory|แผนที่]] (prompt/skills/context) ที่ผู้ใช้ส่งให้ เก็บเป็นความเห็นส่วนตัวของคนใน Anthropic ไม่ใช่ benchmark

## สิ่งที่ source แรกอ้าง (เคส Elysia 2)

ในเคส Elysia 2, [[aom-khunpanitchot|Aom Khunpanitchot]] เล่าว่า Fable:

## สิ่งที่ source นี้อ้าง

ในเคส Elysia 2, [[aom-khunpanitchot|Aom Khunpanitchot]] เล่าว่า Fable:

- ใช้ prompt สั้นมากเมื่อเทียบกับ agent อื่นที่เขาสั่ง audit แบบละเอียด
- รันยาวผ่าน ultracode auto mode จนชน limit
- แตก agent เกือบ 100 ตัว
- สร้าง report 104 ข้อ ยาวประมาณ 24,000 คำ / 174,000 ตัวอักษร
- สรุปว่า Elysia 2 ยังไม่เหมาะขึ้น RC แม้ AI ตัวอื่นบอกว่าพร้อม stable หรือ RC

**ได้อะไร:** Fable ใน source นี้เป็นหลักฐานเชิงประสบการณ์ว่า agent fan-out + long-running audit อาจให้ผลต่างจากการถาม frontier model ทีละตัว.

## การใช้ดุลพินิจของ Fable (Simon Willison, 2026-07)

[[fables-judgement-simon-willison|โพสต์ของ Simon Willison]] เพิ่มมุมเรื่องวิธีสั่ง Fable: ทีม [[claude-code|Claude Code]] ([[cat-wu|Cat Wu]], [[thariq-shihipar|Thariq Shihipar]]) แนะให้ปล่อย Fable **ใช้ดุลพินิจของตัวเอง** ในเรื่องวิธีทำงาน (เช่น เมื่อไหร่ควรเขียน test) แทนสั่งกฎตายตัว — ดู [[judgement-based-prompting]].

ยังมีเคล็ดประหยัดโควตาของ [[jesse-vincent|Jesse Vincent]]: ตอน Fable กำลังจะขึ้นราคา ให้บอก Fable ไปใช้ model ที่ถูกลงทำงานเล็ก ๆ โดยให้ Fable เลือก model เอง. Simon ลองแล้วบอกว่าได้งานเยอะขึ้นและโควตา Fable ลดช้าลง. นี่ทำให้ Fable ในเคสนี้ทำหน้าที่คล้าย orchestrator ที่เลือก model ให้ subagent ตาม [[advisor-strategy]].

## Caveat

ยังไม่มี report 104 ข้อใน wiki และยังไม่ได้ verify ว่าปัญหาแต่ละข้อจริงหรือสำคัญแค่ไหน. ดังนั้นหน้านี้ไม่ควรสรุปว่า Fable "ถูกกว่า" agent อื่นทั้งหมด. สิ่งที่ยืนยันได้จาก source คือ Aom รับรู้ว่า report ของ Fable ลึกและ actionable กว่าการ review ที่เขาเคยได้จาก model อื่นในงานนี้.

## See also

- [[field-guide-to-fable-finding-unknowns]]
- [[aom-fable-elysia-2-audit]]
- [[claude]]
- [[anthropic]]
- [[map-vs-territory]]
- [[unknowns-matrix]]
- [[elysia-2]]
- [[deep-agent-audit]]
- [[agentic-code-review]]
- [[coding-harness]]
- [[dynamic-workflows]]
- [[fables-judgement-simon-willison]]
- [[judgement-based-prompting]]
- [[advisor-strategy]]
