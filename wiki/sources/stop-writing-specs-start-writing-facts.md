---
title: "Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete."
type: source
url: https://medium.com/gitconnected/stop-writing-specs-start-writing-facts-the-entire-sdd-movement-is-already-obsolete-9045f7061e26
author: Jaroslaw Wasowski
published: 2026-05-12
date_ingested: 2026-06-11
tags: [ai-coding, sdd, specs, testing, verification, non-determinism]
sources: ["Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete..md"]
created: 2026-06-11
updated: 2026-06-11
---

# Stop Writing Specs. Start Writing Facts. (Jaroslaw Wasowski)

[[jaroslaw-wasowski|Jaroslaw Wasowski]] (นักเขียน Medium ที่เคยเขียนเชียร์ [[spec-driven-development|Spec-Driven Development]] มาแล้ว 6 บทความ) ออกมาถอนคำพูดครึ่งแรกของตัวเอง: SDD ไม่ใช่คำตอบของ vibe coding chaos อย่างที่เคยบอก เพราะสมมติฐานพื้นฐานของมันพังตั้งแต่ระดับกลไก — **spec ที่เป็น prose ต้องผ่านการตีความของ model ทุกครั้งที่อ่าน ส่วน test ผ่านแค่ exit code** ข้อเสนอคือย้ายจาก "เขียน spec" ไป "เขียน fact" (assertion ที่รันได้จริง) ดูแนวคิดเต็มที่ [[facts-first]]

> "A spec isn't a contract with the model. It's a prediction about the model. And models change."
> — spec ไม่ใช่สัญญากับ model แต่เป็น *คำทำนาย* เกี่ยวกับ model และ model ก็เปลี่ยนไปเรื่อย ๆ

หลักฐานนำเรื่อง: test หนึ่งตัวที่เขียนเมื่อ June 2025 ผ่าน CI โดยไม่ต้องแก้เลยข้าม Sonnet 3.5 → 3.7 → 4 → Opus 4.5+ ขณะที่ spec 1,500 คำที่อธิบาย endpoint เดียวกัน ต้องตีความใหม่ 4 รอบ

## กายวิภาคของ movement: 0→100 ใน 10 เดือน แล้วเริ่มร่วง

Google Trends ของคำว่า "spec driven development" อยู่ที่ศูนย์มา 4 ปี แล้วพุ่งจาก 0 ไป 100 ระหว่าง August 2025 – March 2026 ก่อนร่วงกลับมา 86 ใน May 2026 ผู้เขียนมองว่านี่คือเส้นโค้ง "industrialization at peak" แบบเดียวกับตอนคนถอยจาก AOP framework หนัก ๆ กับ monolithic ESB

ในช่วงเดียวกัน เครื่องมือทั้ง stack ก็โผล่ครบ: [[spec-kit|Spec Kit]] จาก GitHub (~90k stars ณ Q2 2026), Kiro จาก Amazon (บังคับ EARS notation), OpenSpec, BMAD (~50k stars) — รวม 5 framework หลักทะลุ 200k GitHub stars

SDD สัญญา 4 อย่าง: deterministic code generation, hallucination น้อยลง, validate ก่อนเขียนโค้ด, intent เป็น source of truth ผู้เขียนทดสอบครบทุกข้อใน 6 บทความที่ผ่านมา วันนี้เหลือใช้จริงอย่างเดียว: Spec Kit Step 1 เป็นกระดาษทด (sketchpad)

> "The tools themselves aren't broken. The assumption they stand on is."
> — ตัวเครื่องมือไม่ได้พัง สมมติฐานที่มันยืนอยู่ต่างหากที่พัง

## ทำไม spec ถึงเป็นแค่คำทำนาย — กลไก non-determinism

หัวใจของ critique อยู่ที่ [[llm-nondeterminism|ความไม่แน่นอนของ LLM]]: ทุกครั้งที่ model อ่าน prose มันกำลังสุ่มตัวอย่างจากการแจกแจงของการตีความ **แม้ตั้ง temperature 0.0** สาเหตุเป็นเรื่องระบบล้วน ๆ — floating-point non-associativity, batch scheduling, fused-attention kernels — แก้ด้วย prose ที่เขียนดีขึ้นไม่ได้

ตัวเลขที่บทความยกมา:

- งานวิจัยอิสระพบ **80 unique completions จาก 1,000 prompts เหมือนกันเป๊ะ** ใน deterministic mode
- งาน IBM บน RAG workflow สายการเงิน: **model 100B+ ให้ output ซ้ำเดิมแค่ 12.5% ของรอบรัน** ขณะที่ model 7–8B ให้ผลตรงกันหมด — สวนทางความหวังว่า "รอ model เก่งขึ้นแล้ว spec จะเวิร์กเอง"
- งานของ Sclar et al. (2023): การเปลี่ยน format สุดขั้วบน model รุ่นอ่อนทำ accuracy แกว่งได้ถึง 76 จุด (ผู้เขียนออกตัวว่าเป็นเคสสุดขั้ว ไม่ใช่ whitespace ธรรมดา)
- ข้าม vendor ก็ไม่รอด: model ของแต่ละเจ้าละเมิด constitution ของเจ้าอื่นมากกว่าของตัวเองหลายเท่า — **spec เป็น vendor-shaped ไม่ใช่ universal**

[[birgitta-bockeler|Birgitta Böckeler]] (Thoughtworks) ถูกอ้างถึงในทางเดียวกัน: เธอเตือนว่า spec-as-source อาจรับมรดก "the flaws of both MDD and LLMs: inflexibility and non-determinism" (ข้อเสียของทั้ง Model-Driven Development และ LLM — คือทั้งแข็งทื่อและไม่แน่นอน)

อีกแกนคือ [[intent-gap]]: Shuvendu K. Lahiri (Microsoft Research) ชี้ว่า "AI-generated code is plausible by construction but not correct by construction" — โค้ดที่ AI สร้าง *ดูสมเหตุสมผล* โดยกำเนิด แต่ไม่ได้ *ถูกต้อง* โดยกำเนิด ระยะห่างระหว่างสิ่งที่คนตั้งใจกับสิ่งที่โปรแกรมทำจริงคือช่องว่างที่ spec ภาษาคนตรวจไม่ได้

แถมยังมี **spec drift** (spec กับโค้ดค่อย ๆ หลุดจากกัน เทียบ schema drift ใน database) — Spec Kit ถึงกับออกคำสั่ง `/speckit.spec-drift` ใน May 2026 ผู้เขียนอ่านว่านั่นคือการยอมรับว่า drift เป็นความเสี่ยงจริงระดับต้องมีเครื่องมือเฉพาะ

> "A model migration isn't an update — it's a change of interpreter."
> — การย้ายรุ่น model ไม่ใช่การอัปเดต แต่คือการเปลี่ยนตัวแปลภาษา

## Fact = executable assertion — สิ่งที่รอดจากการ sampling

fact คือสิ่งที่เครื่องตรวจเองได้โดยไม่ต้อง "อ่าน": test ผ่าน/ตก, exit code 0 หรือไม่ใช่ 0 — ไม่มีการตีความ ไม่มีการสุ่ม ไม่มีอารมณ์ ผู้เขียนแบ่ง granularity เป็น 3 ระดับ:

1. **Single test** — คู่ input/output เฉพาะเจาะจง (เช่น `expired JWT returns 401`)
2. **Property** — predicate ครอบจักรวาล เช่น "ทุก sorted list ผลของ binary_search ต้องถูก" (สาย [[property-based-testing]])
3. **Contract** — precondition + postcondition + invariant แบบ Design by Contract

มี lifecycle กำกับใน git: `@draft → @spec → @implemented` โดยเงื่อนไขความจริงคือ shell command ที่ exit 0 — "This isn't a framework — it's discipline embedded in git" (ไม่ใช่ framework แต่เป็นวินัยที่ฝังอยู่ใน git)

### ลำดับวงศ์ 57 ปี — ไม่ใช่ paradigm ใหม่

ผู้เขียนย้ำว่า facts-first ไม่ใช่การปฏิวัติ แต่เป็นการสังเคราะห์งานเก่า 57 ปีเข้ากับยุค AI:

- **1969** — Hoare triple `{P} C {Q}` (C.A.R. Hoare): "หน่วยเล็กสุดของ fact เกี่ยวกับ behavior"
- **1992** — Design by Contract ของ Bertrand Meyer ใน Eiffel: `require` / `ensure` / `invariant` บังคับตอน runtime
- **2000** — QuickCheck: property-based testing แบบสุ่ม
- **2026** — Agent Behavioral Contracts: งานวิชาการยุคแรกวัดได้ 5–7 violations ต่อ session, overhead ต่ำกว่า 10ms

เคส production ที่แรงสุด: งานของ John Hughes ที่ Quviq — โค้ด Erlang 60,000 บรรทัดที่ผู้ผลิตรถยนต์สวีเดน ใช้ PBT test แค่ 450 บรรทัด เจอบั๊ก 25 ตัว รวม race condition ที่ example-based test เข้าไม่ถึง (อัตราส่วน 1:133)

## ขอบเขตที่ SDD ยังชนะ — "ceremony is the product"

ผู้เขียนยกคำป้องกัน SDD ที่แรงสุดของ [[marc-brooker|Marc Brooker]] (AWS, April 2026): "specifications are making explicit, versioned, living artifacts" — ใน SDD แบบ iterative ไม่ใช่ waterfall แล้วยอมรับตรง ๆ ว่าคำป้องกันนี้แข็งกว่าที่นักวิจารณ์ส่วนใหญ่ให้เครดิต SDD ไม่ใช่ความผิดพลาด แค่โดเมนใช้งานแคบกว่าที่คนเชียร์สัญญาไว้ สามโดเมนที่ SDD ชนะชัด:

1. **Compliance / regulation** — spec คือหลักฐานทางกฎหมาย ไม่ใช่ documentation (DO-178C ต้องการ bidirectional traceability, ISO 26262, EU AI Act ปรับได้ถึง €15M หรือ 3% ของ turnover) — ตรงนี้ ceremony *คือ* ตัวสินค้า
2. **Cross-team B2B integration** — 500 วิศวกร 20 ทีม ค่า coordination แพงกว่าค่า implement (OpenAPI ของ Stripe เป็นสัญญากับ partner; Boost Insurance รายงาน service stability ดีขึ้น 80% หลังใช้ Pact)
3. **Onboarding / knowledge transfer** — คนใหม่อ่าน spec ไม่ได้อ่าน test; markdown อธิบาย *why*

เกณฑ์ตัดสินข้อเดียว: **artifact นั้นมีมนุษย์นอกทีมอ่านไหม (auditor, partner, คนใหม่)?** ถ้าใช่ → คงเป็น spec ถ้าไม่ → ย้ายเข้า fact-set

## แผนย้าย 90 วัน — Audit, Pivot, Gate

- **Phase 1 Audit (วัน 1–30)** — ยังไม่ลบอะไร แยก spec เป็น 3 กอง: คนนอกทีมอ่าน (เก็บ), เอกสารตายที่ไม่มีใครเปิด (รอ deprecate), implicit invariants บน endpoint เสี่ยงสูง (auth, payment) ที่มีแต่ prose — ใช้ agent ทำ retrofitting ขุด invariant จริงจากโค้ด ได้ลิสต์ fact `@draft`
- **Phase 2 Pivot (วัน 31–60)** — แปลง spec ขอบระบบเป็น fact: API contract → Pact test, property/invariant → Hypothesis/QuickCheck, data model invariant → runtime assertion; **กลับ testing pyramid** (unit น้อยลง contract/integration มากขึ้น); feature ใหม่รัน spec กับ fact คู่กัน 30 วันเป็น A/B
- **Phase 3 Gate (วัน 61–90)** — `facts check` เป็นด่านบังคับใน CI; feature ใหม่ต้องมี failing fact ก่อนลงมือ (จังหวะ TDD ในเปลือกใหม่); deprecate prose spec นอกโซน compliance/onboarding

โบนัสเชิงปฏิบัติ: ทีมที่ใช้ SDD tooling หนัก ๆ ชนเพดาน token ของ plan (เคสชัดสุดคือ OpenSpec) ส่วน `facts check` ตรวจทั้ง repo ด้วย token น้อยกว่าให้ model อ่าน spec — ย้ายแล้วไม่ใช่แค่ลดภาระสมอง แต่ลดบิลด้วย

## บทสรุปของผู้เขียน

> "PRDs are going away. Specs are leaving the inner loop. Facts survive everywhere."
> — PRD กำลังหายไป, spec กำลังออกจาก inner loop, fact อยู่รอดได้ทุกที่

สี่ takeaway: (1) spec เป็นคำทำนายเกี่ยวกับ model ไม่ใช่สัญญา; (2) fact = invariant ที่เครื่องรันตรวจได้ รอด model upgrade เพราะไม่ผ่านการตีความ; (3) SDD ชนะตรงที่มี auditor/partner/คนใหม่อ่าน artifact — ที่อื่นแพ้; (4) ย้ายได้ใน 90 วัน แต่ละ phase มี ROI ของตัวเอง เริ่มจาก **fact เดียว** พรุ่งนี้เช้า

## ข้อควรระวังตอนอ่าน

- ผู้เขียนออกตัวเองว่าข้อสรุปมาจาก **6 โปรเจกต์ของตัวเอง ไม่มี control group** — "I maintain that distance, and you should too"
- หลักฐานเชิง "movement กำลังตาย" พิงกับ Google Trends (100→86 ใน 2 เดือน) ซึ่งเป็นสัญญาณอ่อน — ความสนใจค้นหาลดไม่เท่ากับการใช้งานจริงลด
- โทนบทความเป็น Medium-rhetoric จัดจ้าน (พาดหัวว่า "obsolete" แต่เนื้อในยอมรับเองว่า SDD ยังชนะใน 3 โดเมนใหญ่) — ข้อเสนอจริงใกล้เคียง "จำกัดขอบเขต SDD แล้วเสริมด้วย executable facts" มากกว่า "ทิ้ง SDD"
- จุดที่แข็งแรงสุดของบทความคือกลไก [[llm-nondeterminism]] กับเกณฑ์ "ใครอ่าน artifact" — สองอย่างนี้ยืนได้ด้วยตัวเองแม้ไม่ซื้อ thesis ใหญ่

## See also

- [[facts-first]] — แนวคิดหลักที่กลั่นจากบทความนี้
- [[spec-driven-development]] — ฝั่งที่ถูกวิจารณ์ + ขอบเขตที่ยังชนะ
- [[llm-nondeterminism]] — กลไกที่ทำให้ spec เป็นแค่คำทำนาย
- [[intent-gap]] — ช่องว่างระหว่างเจตนากับโค้ด
- [[property-based-testing]] — fact ระดับ property
- [[specs-to-code]] — กับดักเดียวกันในเวอร์ชันของ Matt Pocock
- [[verifiability]] / [[behavioral-verifier]] — ทำไมของที่เครื่องตรวจได้ถึงชนะ
- [[harness-guides-sensors]] — fact คือ computational sensor ในกรอบของ Böckeler
