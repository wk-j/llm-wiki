---
title: "New Skills! /handoff, /prototype, /review and /writing-* | Skills Changelog"
type: source
tags: [ai, skills, claude-code, workflow, prototyping, review, writing]
url: https://www.youtube.com/watch?v=DNqsMXH6Eog
date_ingested: 2026-05-12
created: 2026-05-12
updated: 2026-05-12
sources: ["New Skills! handoff, prototype, review and writing-*  Skills Changelog.md"]
---

# New Skills! /handoff, /prototype, /review and /writing-* | Skills Changelog

วิดีโอ changelog ของ [[matt-pocock|Matt Pocock]] (TypeScript expert และคนทำ workflow agent) อธิบาย skill ชุดใหม่ใน ecosystem ของเขา โดยแกนหลักคือการทำให้ agent ทำงานข้าม context window ได้ดีขึ้น และใช้ prototype เป็นพื้นที่ทดลองก่อน commit กับ implementation จริง

## ใจความสำคัญ

- **`/handoff`** สร้างเอกสารส่งต่องานชั่วคราว เพื่อให้ agent ตัวใหม่รับ context, intent, และ skill ที่ควรใช้ต่อได้ ดู [[agent-handoff-documents]]
- **`/prototype`** ใช้สร้าง prototype แบบทิ้งได้ ทั้ง UI prototype และ logic prototype เพื่อหาคำตอบที่อ่านจาก spec อย่างเดียวไม่ได้ ดู [[throwaway-prototyping]]
- **`/review`** ยังอยู่ระหว่างทำ เป็น code review skill ที่แยกการตรวจเป็นสองแกน คือ repo standards กับ spec fidelity ดู [[dual-axis-code-review]]
- **`/writing-*`** ยังอยู่ระหว่างทำ เป็นชุด writing skills ที่เริ่มจาก fragments ไปเป็น beats แล้วค่อย shape งานเขียน ดู [[writing-fragments]]

## `/handoff`: ส่งต่องานข้าม context window

`/handoff` มีไว้ตอน session เดิมเริ่มยาวหรือกำลังอยู่ในงานหนึ่ง แต่ต้องแตกไปทำงานอีกแบบหนึ่ง เช่น อยู่ใน [[grill-me|grilling session]] แล้วพบว่าต้อง prototype โค้ดจริงก่อนตัดสินใจต่อ

ตัว skill จะเขียน handoff document ไปไว้ใน temp path. เอกสารนี้ไม่ใช่ knowledge base ถาวร แต่เป็น bridge ระหว่าง agent สอง session. เนื้อหาที่สำคัญไม่ใช่แค่ "คุยอะไรกันมา" แต่รวมถึงเจตนา น้ำเสียงของงาน และ skill ที่ session ถัดไปควรใช้

Pocock เน้นอีกข้อว่า handoff ไม่ควร copy artifact ที่มีอยู่แล้วซ้ำ ถ้ามี plan, PRD, หรือไฟล์ prototype อยู่แล้ว ให้ reference เป็น path หรือ URL แทน

**ได้อะไร:** แยกงานใหม่ออกไปใน context window สด โดยไม่ทำให้ session หลักพองและโดน [[context-rot|context rot]]

## สอง pattern ของ handoff

Pocock แยกการใช้ handoff เป็นสองแบบ

| Pattern | ใช้เมื่อไหร่ | ผล |
|---|---|---|
| Fire and forget | เจอ bug หรือ task แทรกกลาง session | เปิด agent ใหม่ไปจัดการ แล้วไม่ต้องลากงานนั้นกลับเข้าหลักมากนัก |
| DIY subagent | ต้องแตกไปทดลอง แล้วเอาผลกลับมาคุยต่อ | ได้ agent อีกตัวที่มี context window เต็ม และยัง spawn subagent เองได้ |

ตรงนี้ต่างจาก subagent ปกติ เพราะมนุษย์เป็นคนเปิด session ใหม่เองและคุม handoff เอง. มันจึงอยู่กึ่งกลางระหว่าง [[subagent-patterns]] กับ manual session management ใน [[claude-code-session-management]]

## `/prototype`: ใช้ prototype เป็น research

Pocock มอง prototyping เป็น research spike. ใน AI engineering งานจำนวนมากมี unknown unknowns ที่ตอบไม่ได้จากการคุยหรือเขียน spec. ต้องลองเห็น behavior จริงก่อน

`/prototype` ไม่ได้หมายถึง UI อย่างเดียว

- **UI prototype** — สร้างหลาย variation ที่ต่างกันชัดเจน แล้วให้มนุษย์เลือก เดินลง design tree และผสมสิ่งที่ชอบจากหลายแบบ
- **Logic prototype** — สร้าง terminal app เล็ก ๆ เพื่อผลัก state machine ผ่าน case ที่คิดบนกระดาษยาก เช่น entity ใน database ที่เปลี่ยน state จาก action ของผู้ใช้

Pocock เชื่อว่าหน้า UI ยังต้องมีมนุษย์อยู่ใน loop เพราะรสนิยม style และบริบทของแอปตัดสินจาก token อย่างเดียวไม่ได้. Agent มัก "มองไม่เห็น" งานที่ตัวเองสร้าง จึงต้องให้คนชี้ว่าอะไรดูดี ใช้ได้ หรือหลุดจาก product language

**ได้อะไร:** prototype ทำให้ decision ถูกย้ายจากการเดาใน prompt ไปเป็นการดู artifact จริง แล้วค่อยส่งต่อให้ implementation agent ทำของจริง

## Bug fixes ใน skill อื่น

วิดีโอยังพูดถึงการแก้ skill เดิมสองเรื่อง

1. **`grill-with-docs` ใช้ XML tags แยกส่วน instruction กับ supporting info** — Pocock เรียกปัญหานี้ว่า prompt loudness. ถ้า supporting info "ดัง" กว่า instruction หลัก model อาจหลุดไป implement เร็วเกินไป การห่อด้วย XML tags ช่วยบอก model ว่าส่วนไหนคือหน้าที่หลัก ส่วนไหนคือข้อมูลประกอบ
2. **`to-PRD` และ `to-issues` เปลี่ยน label เป็น ready for agent triage** — issue ที่แตกจาก PRD แล้วควรพร้อมให้ agent ทำ ไม่ควรกลับไปอยู่ในคิว `needs triage`

## งานที่ยังไม่เสร็จ: writing และ review

ชุด writing skills แบ่งเป็นสามช่วง

- **Fragments** — เก็บประโยค ไอเดีย หรือ observation แบบดิบ แล้วให้ AI ช่วยถามต่อเพื่อทำให้ fragment ดีขึ้น
- **Beats** — จัด fragment เป็นจังหวะของ article/story โดยเสนอทางเดินถัดไปหลายทาง
- **Shape** — review งานสุดท้ายให้ไม่มีกลิ่น AI และมี structure ที่เหมาะกับงานเขียนนั้น

ส่วน review skill ใช้แนวคิดสองแกน

- **Standards** — diff ทำตาม convention, coding standards, และ shape ของ repo หรือไม่
- **Spec** — diff ทำสิ่งที่ issue/PRD ขอไว้จริงหรือไม่

Pocock ระบุว่าถ้าดูแค่ standards จะพลาด spec. ถ้าดูแค่ spec จะพลาด convention ของ codebase. แนวทางที่เสนอคือแตก subagent สองตัวมาตรวจคนละแกน แล้วรวมผล

## ความเชื่อมโยงกับ wiki

- ยืนยันว่า [[context-rot]] ไม่ใช่เรื่องของการเต็ม context อย่างเดียว แต่เป็นเหตุผลให้ต้องมี handoff และ prototype session แยก
- ต่อเติม [[subagent-patterns]] ด้วย pattern ที่มนุษย์เปิด session ใหม่เองแทน subagent ใน harness
- เชื่อมกับ [[alignment-bottleneck]] เพราะ prototype และ grill ลดความคลาดเคลื่อนก่อน implementation
- เชื่อมกับ [[ai-orchestrator]] เพราะทักษะสำคัญคือเลือกจังหวะว่าเมื่อไหร่ควร grill, prototype, handoff, review, หรือ implement

## See also

- [[matt-pocock]]
- [[agent-handoff-documents]]
- [[throwaway-prototyping]]
- [[dual-axis-code-review]]
- [[writing-fragments]]
- [[grill-me]]
- [[context-rot]]
- [[subagent-patterns]]
