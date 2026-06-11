---
title: Facts-First (Executable Facts)
type: concept
tags: [ai-coding, testing, verification, specs, sdd]
created: 2026-06-11
updated: 2026-06-11
sources: ["Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete..md"]
---

# Facts-First / เขียน "ข้อเท็จจริงที่รันได้" แทนสเปก

**Facts-first** คือแนวทางจาก [[jaroslaw-wasowski|Jaroslaw Wasowski]] (ใน [[stop-writing-specs-start-writing-facts]]): แทนที่จะเก็บความจริงของระบบไว้ใน prose spec ที่ model ต้องตีความ ให้เก็บเป็น **fact — executable assertion** ที่เครื่องตรวจเองได้ เช่น `expired JWT returns 401` เป็น test หนึ่งตัวใน CI ผ่านหรือตกตัดสินด้วย exit code ไม่ใช่การอ่าน

จุดต่างกับ spec อยู่ที่เส้นทางการตรวจ: spec ผ่านการตีความของ model (ซึ่ง [[llm-nondeterminism|ไม่ deterministic]] — สุ่มใหม่ทุกครั้งที่อ่าน) ส่วน fact ผ่าน runtime ของภาษาโปรแกรม ผลคือ fact ตัวเดิมรอดข้าม model upgrade ได้โดยไม่ต้องแก้ — เคสนำของบทความคือ test ที่เขียน June 2025 ผ่าน CI ข้าม Sonnet 3.5 → 3.7 → 4 → Opus 4.5+ ขณะที่ spec 1,500 คำของ endpoint เดียวกันถูกตีความใหม่ 4 รอบ

> เทียบง่าย ๆ: office memo ต้องให้ intern ทุกคนตีความเอง แต่กฎแรงโน้มถ่วงไม่ต้อง — นั่นคือความต่างระหว่าง bureaucracy กับ physics

## สามระดับของ fact

1. **Single test** — คู่ input/output เฉพาะเจาะจงหนึ่งคู่
2. **Property** — predicate ที่ต้องจริงเสมอ เช่น "ทุก sorted list ผล binary_search ต้องถูก" (ดู [[property-based-testing]])
3. **Contract** — precondition + postcondition + invariant แบบ Design by Contract

ทุกระดับเป็น Boolean ที่ตรวจตอน runtime: ผ่านหรือตก ไม่มี "แล้วแต่" มี lifecycle กำกับใน git ว่า fact แต่ละตัวอยู่ขั้นไหน: `@draft → @spec → @implemented` โดยเงื่อนไขความจริงคือคำสั่ง shell ที่ exit 0 — เป็นวินัยที่ฝังใน git ไม่ใช่ framework

## ไม่ใช่ของใหม่ — การสังเคราะห์ 57 ปี

Wasowski ย้ำเองว่า facts-first ไม่ใช่ paradigm ใหม่ แต่เป็นการเอางาน formal methods กับ testing ที่กระจัดกระจายมา 57 ปีมาประกอบใหม่ในยุค AI:

- **1969** — Hoare triple `{P} C {Q}` (C.A.R. Hoare): ถ้าเงื่อนไข P จริงก่อนรัน C แล้ว Q ต้องจริงหลังรัน — "หน่วยเล็กสุดของ fact เกี่ยวกับ behavior"
- **1992** — Design by Contract (Bertrand Meyer, Eiffel): `require` / `ensure` / `invariant` บังคับตอน runtime
- **2000** — QuickCheck: [[property-based-testing|property-based testing]] แบบสุ่ม input
- **2026** — Agent Behavioral Contracts: contract สำหรับกำกับ agent ยุค AI (งานแรก ๆ วัดได้ 5–7 violations ต่อ session, overhead < 10ms)

## เกณฑ์ตัดสินว่าอะไรควรเป็น spec อะไรควรเป็น fact

ข้อเสนอนี้ไม่ได้ทิ้ง [[spec-driven-development|SDD]] ทั้งหมด — เกณฑ์ข้อเดียวคือ **มีมนุษย์นอกทีมอ่าน artifact นั้นไหม?** (auditor, partner, คนเข้าทีมใหม่) ถ้ามี → เก็บเป็น spec เพราะตรงนั้น ceremony คือตัวสินค้า ถ้าไม่มีใครอ่านนอกจาก CI → ย้ายเป็น fact

แผนย้าย 90 วันแบ่งสามช่วง ช่วงละ 30 วัน: **Audit** (แยก spec สามกอง ยังไม่ลบอะไร ใช้ agent ขุด implicit invariant จากโค้ดบน endpoint เสี่ยงสูง) → **Pivot** (API contract → Pact test, invariant → Hypothesis/QuickCheck, กลับ testing pyramid ให้ contract/integration มากขึ้น) → **Gate** (`facts check` เป็นด่านบังคับใน CI; feature ใหม่ต้องมี failing fact ก่อนลงมือ — จังหวะเดียวกับ TDD)

**ผลคือ:** ความจริงของระบบไม่ขึ้นกับอารมณ์ของ interpreter — model จะเปลี่ยนรุ่นกี่ครั้ง fact ก็ตรวจแบบเดิม แถมประหยัด token กว่าให้ model อ่าน spec ยาว ๆ ทุกรอบ

## โยงกับหน้าอื่น

- [[verifiability]] — facts-first คือการบังคับให้ "ความต้องการ" กลายเป็นของ verifiable ซึ่งเป็นเงื่อนไขที่ทำให้ AI ทำงานแบบ automation ได้จริง
- [[harness-guides-sensors]] — ในภาษาของ Böckeler fact คือ **computational sensor**: deterministic, เร็ว, ถูก, รันได้ทุก commit — ต่างจาก spec ที่เป็น inferential guide
- [[harness-ratchet]] — fact ใหม่หนึ่งตัวต่อ failure หนึ่งเรื่อง = กลไก ratchet เดียวกัน
- [[behavioral-verifier]] — หลักเดียวกันในโลก benchmark: ตรวจพฤติกรรม ไม่ตรวจการตีความ
- [[specs-to-code]] — กับดักที่ facts-first ออกแบบมาเลี่ยง

## See also

- [[stop-writing-specs-start-writing-facts]]
- [[spec-driven-development]]
- [[property-based-testing]]
- [[intent-gap]]
- [[llm-nondeterminism]]
- [[verifiability]]
- [[harness-guides-sensors]]
