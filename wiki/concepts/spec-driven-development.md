---
title: Spec-Driven Development (SDD)
type: concept
tags: [ai-coding, sdd, specs, workflow, methodology]
created: 2026-06-11
updated: 2026-07-04
sources: ["Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete..md", code-isnt-free-mario-zechner-hard-truths-coding-ai.md]
---

# Spec-Driven Development (SDD) / พัฒนาซอฟต์แวร์โดยให้สเปกนำ

**Spec-Driven Development (SDD)** คือแนวทางที่ให้เขียน specification เป็น artifact หลักก่อน แล้วให้ AI agent สร้างโค้ดจาก spec นั้น — ตัว spec เป็น source of truth ส่วนโค้ดเป็นผลพลอยได้ที่ regenerate ใหม่ได้เสมอ movement นี้เกิดขึ้นเพื่อแก้ความวุ่นวายของ [[vibe-coding]] (เขียนโค้ดด้วยการคุยกับ AI แบบไม่มีโครง)

## เครื่องมือใน movement

ช่วง August 2025 – March 2026 เครื่องมือโผล่ครบทั้ง stack รวมกันเกิน 200k GitHub stars:

- **[[spec-kit|Spec Kit]]** (GitHub) — ~90k stars ณ Q2 2026 ตัวใหญ่สุดของ movement
- **Kiro** (Amazon) — บังคับใช้ EARS notation (รูปแบบเขียน requirement แบบมีโครงตายตัว)
- **OpenSpec** — โตเร็ว triple-digit ใน 6 เดือน ใช้สถาปัตยกรรมแบบ delta
- **BMAD** — ~50k stars ใช้ persona stack

คำสัญญา 4 ข้อของ movement: deterministic code generation, hallucination น้อยลง, validate ได้ก่อนมีโค้ด, intent เป็น source of truth

## คำวิจารณ์หลัก: spec เป็นคำทำนาย ไม่ใช่สัญญา

[[jaroslaw-wasowski|Jaroslaw Wasowski]] (อดีตคนเชียร์ SDD 6 บทความ) สรุปจุดพังไว้ใน [[stop-writing-specs-start-writing-facts]] ว่า:

> "A spec isn't a contract with the model. It's a prediction about the model. And models change."

spec ที่เป็น prose ต้องผ่านการตีความของ model ทุกครั้งที่อ่าน และ [[llm-nondeterminism|LLM ไม่ deterministic แม้ temperature 0]] — spec เดิมจึงให้โค้ดต่างกันได้ในแต่ละรอบ และพอเปลี่ยนรุ่น model ก็เท่ากับ "เปลี่ยนตัว interpreter" ไม่ใช่แค่อัปเดต เปรียบเหมือน office memo ที่ intern แต่ละคนตีความไม่เหมือนกัน — "Models are giant disgruntled interns, except their mood changes with every API call"

อาการที่ตามมาคือ **spec drift** — spec กับโค้ดหลุดจากกันเรื่อย ๆ จน Spec Kit ต้องออกคำสั่ง `/speckit.spec-drift` มาแก้ (May 2026) ปัญหาลึกกว่านั้นคือ [[intent-gap]]: ภาษาคนตรวจสอบด้วยเครื่องไม่ได้ จึงไม่มีทางรู้แน่ว่าโค้ดที่ได้ตรงเจตนาไหม

[[birgitta-bockeler|Birgitta Böckeler]] (Thoughtworks) เตือนไว้คล้ายกันว่า spec-as-source อาจรับมรดก "the flaws of both MDD and LLMs: inflexibility and non-determinism" — แข็งทื่อแบบ Model-Driven Development แล้วยังไม่แน่นอนแบบ LLM อีก

ทางออกที่ Wasowski เสนอคือ [[facts-first]]: เก็บความจริงของระบบเป็น executable assertion ที่เครื่องตรวจเองได้ แทน prose ที่ model ต้องตีความ

## Mario's critique: hyper-waterfall

[[mario-zechner|Mario Zechner]] วิจารณ์ SDD ใน [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]] ว่าเสี่ยงเป็น **hyper-waterfall**. ความเร็วของ agent ทำให้ waterfall รอบใหม่ดูน่าเชื่อกว่าเดิม เพราะ turnaround จาก spec ไปเป็น software อาจเหลือไม่กี่ชั่วโมง. แต่ปัญหาหลักยังอยู่: prose spec ไม่มีทางละเอียดเท่า program จริง. ช่องว่างที่ไม่ได้เขียนไว้จะถูก agent เติมเอง.

สิ่งที่ agent ใช้เติมช่องว่างมักมาจาก pattern เฉลี่ยบน internet ไม่ใช่ความเข้าใจเฉพาะของระบบตรงหน้า. สำหรับ Mario, "enterprise vibe coding" คือ vibe coding ที่เพิ่มขั้นตอนให้ agent เขียน spec ยาวก่อน แต่ถ้าคนไม่คิด architecture และไม่ verify ความจริง มันยังเป็นปัญหาเดิม.

**เปิดคำถาม:** คำวิจารณ์นี้ไม่ลบฝั่ง Brooker ที่บอกว่า spec มีค่าเมื่อมีคนนอกทีมต้องอ่าน. มันเตือนว่าอย่าใช้ spec เป็นข้ออ้างให้คนเลิกคิด เพราะ prose ไม่ได้แทน judgement.

## ฝั่งป้องกัน: Brooker กับขอบเขตที่ SDD ชนะจริง

[[marc-brooker|Marc Brooker]] (AWS) ป้องกัน SDD ไว้แข็งแรงที่สุด (April 2026): spec ที่ดีคือ "explicit, versioned, living artifacts" — ใช้แบบ iterative ไม่ใช่ waterfall แม้แต่ Wasowski เองก็ยอมรับว่า SDD ชนะชัดใน 3 โดเมน:

1. **Compliance / regulation** — spec เป็นหลักฐานทางกฎหมาย (DO-178C, ISO 26262, EU AI Act) — ceremony คือตัวสินค้า ไม่ใช่ต้นทุน
2. **Cross-team B2B integration** — ตอนค่า coordination แพงกว่าค่า implement (OpenAPI ของ Stripe, Pact contracts)
3. **Onboarding** — คนใหม่อ่าน spec ไม่อ่าน test; markdown อธิบาย *why* ได้

เกณฑ์ตัดง่าย ๆ: **มีมนุษย์นอกทีมอ่าน artifact นี้ไหม?** ถ้ามี → เก็บเป็น spec ถ้าไม่มี → ควรเป็น fact

## โยงกับหน้าอื่น

- [[specs-to-code]] — กับดักเวอร์ชัน Matt Pocock: เขียน spec แล้วไม่ดูโค้ดเลย — SDD แบบสุดโต่งคือสิ่งเดียวกัน คำวิจารณ์สองสายนี้มาบรรจบกัน
- [[facts-first]] — ข้อเสนอทดแทนใน inner loop
- [[llm-nondeterminism]] — กลไกที่ทำให้คำสัญญา "deterministic code generation" เป็นไปไม่ได้
- [[harness-guides-sensors]] — ในกรอบของ Böckeler spec เป็น guide แบบ inferential (ต้องให้ model ตีความ) ขณะที่ test เป็น sensor แบบ computational

## See also

- [[stop-writing-specs-start-writing-facts]]
- [[facts-first]]
- [[intent-gap]]
- [[llm-nondeterminism]]
- [[specs-to-code]]
- [[spec-kit]]
- [[marc-brooker]]
- [[vibe-coding]]
- [[code-isnt-free-mario-zechner-hard-truths-coding-ai]]
