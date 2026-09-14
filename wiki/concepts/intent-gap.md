---
title: Intent Gap
type: concept
tags: [ai-coding, verification, specs, formal-methods]
created: 2026-06-11
updated: 2026-09-09
sources: ["Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete..md", claude-codes-new-intent-md-rob-shocks.md]
---

# Intent Gap / ช่องว่างระหว่างเจตนากับโค้ด

**Intent gap** คือระยะห่างระหว่าง *สิ่งที่ผู้ใช้ตั้งใจ* กับ *สิ่งที่โปรแกรมทำจริง* คำนี้มาจาก Shuvendu K. Lahiri (นักวิจัยที่ Microsoft Research) พร้อมประโยคที่จับแก่นได้คม:

> "AI-generated code is plausible by construction but not correct by construction."
> — โค้ดที่ AI สร้าง *ดูสมเหตุสมผล* โดยกำเนิด แต่ไม่ได้ *ถูกต้อง* โดยกำเนิด

LLM ถูกฝึกให้สร้างของที่ดูเข้าท่า — โค้ดอ่านลื่น ตั้งชื่อดี โครงสร้างคุ้นตา — แต่ความเข้าท่านั้นไม่ได้การันตีว่ามันตรงกับเจตนาของคนสั่งเลย ตรงนี้คือเหตุผลว่าทำไมโค้ดจาก AI ถึง "ดูถูกแต่ผิด" ได้บ่อย: มันถูก optimize มาให้ plausible ไม่ใช่ correct

## ทำไม spec ภาษาคนปิดช่องนี้ไม่ได้

spec ที่เป็น natural language เป็นของ informal — เครื่องตรวจไม่ได้ (uncheckable) จึงทำได้แค่ *หวัง* ว่า model ตีความตรงเจตนา ซ้ำร้าย [[llm-nondeterminism|การตีความนั้นยังสุ่มใหม่ทุกครั้ง]] มุมของ Lahiri คือ **formal specification เป็นกลไก verify เดียวที่ scale ได้** — ของที่เครื่องเช็คเองได้เท่านั้นที่ปิด gap ได้จริง ซึ่งไปทางเดียวกับข้อเสนอ [[facts-first]] (เก็บเจตนาเป็น executable assertion)

ในคำของ [[jaroslaw-wasowski|Wasowski]]: [[spec-driven-development|SDD]] "confuses an answer with a statistical approximation of an answer" — เอาค่าประมาณเชิงสถิติของคำตอบมาใช้แทนคำตอบ

## โยงกับหน้าอื่น

ปัญหานี้โผล่ในหน้าอื่นของ wiki หลายรูป:

- [[harness-guides-sensors]] — Böckeler ชี้ว่า failure ที่กระทบหนักสุด (เข้าใจคำสั่งผิด วินิจฉัยผิด ทำเกินสั่ง) คือของที่ sensor ไหน ๆ ก็จับไม่ได้ ถ้าคนไม่เคยบอกว่าต้องการอะไร — นั่นคือ intent gap ตัวเดียวกัน
- [[missed-requirement]] — อาการ intent gap แบบหนึ่ง: ทำมาครบ ๆ แต่ตกข้อกำหนดที่ซ่อนอยู่
- [[model-honesty]] — ฝั่ง model พยายามลด gap จากด้านของมัน: ยอมรับเมื่อไม่แน่ใจ แทนที่จะเนียนส่งของ plausible
- [[verifiability]] — ยิ่งงานนิยามผลถูก/ผิดได้ชัด intent gap ยิ่งแคบลงโดยโครงสร้าง
- [[map-vs-territory]] / [[unknowns-matrix]] — มุมฝั่ง prompting ของ gap เดียวกัน: Thariq (ทีม Claude Code) มองว่า gap มาจาก unknowns ของผู้ใช้ที่ยังไม่ถูกเคลียร์ และเสนอเทคนิคหา unknowns ก่อน/ระหว่าง/หลังลงมือ; ฝั่ง facts-first ปิด gap ด้วย executable assertion — สองแนวเสริมกัน ไม่แทนกัน

## intent.md ปิด gap ได้แค่ช่วงแรก

[[intent-md|`intent.md`]] ใน playbook ที่ [[claude-codes-new-intent-md-rob-shocks|Rob Shocks อธิบาย]] ช่วยด้านที่หน้านี้เคยยังไม่มี artifact รองรับ: ให้ agent สัมภาษณ์ originator แล้วเก็บ problem, desired outcome, constraint และ open question ก่อนข้อมูลจะผ่านหลาย handoff Originator ต้องอ่านและแก้สิ่งที่ agent เข้าใจผิดเอง

วิธีนี้ลด gap ระหว่าง "สิ่งที่คนต้นเรื่องพูด" กับ "สิ่งที่ product และ engineering ได้รับ" แต่ยังไม่ปิด gap ระหว่าง prose กับ behavior ของโปรแกรม เพราะ `intent.md` ยังตรวจ executable behavior ไม่ได้

**ผลคือ:** discovery artifact กับ formal/executable fact แก้คนละช่วงของช่องว่าง ต้องใช้คู่กันแทนการเลือกอย่างใดอย่างหนึ่ง

## See also

- [[stop-writing-specs-start-writing-facts]]
- [[facts-first]]
- [[spec-driven-development]]
- [[llm-nondeterminism]]
- [[missed-requirement]]
- [[verifiability]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[intent-md]]
- [[artifact-chain]]
