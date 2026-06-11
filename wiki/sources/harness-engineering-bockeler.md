---
title: "Harness engineering for coding agent users"
type: source
tags: [ai, agents, harness, software-engineering, feedback-loop, cybernetics, thoughtworks]
created: 2026-06-08
updated: 2026-06-08
sources: [Harness engineering for coding agent users.md]
url: https://martinfowler.com/articles/harness-engineering.html
author: Birgitta Böckeler
published: 2026-04-02
---

# Harness engineering for coding agent users / วิศวกรรม Harness สำหรับคนใช้ coding agent

บทความโดย [[birgitta-bockeler|Birgitta Böckeler]] (engineer ที่ [[thoughtworks|Thoughtworks]]) ตีพิมพ์บน martinfowler.com (2026-04-02) เสนอ **กรอบคิด (mental model)** สำหรับคนที่ *ใช้* coding agent ว่าจะสร้างความเชื่อมั่นในงานของ agent ได้ยังไง ผ่านการออกแบบ harness เป็น **ระบบ control** ดูหน้าแนวคิดที่กลั่นออกมาแล้วที่ [[harness-guides-sensors]]

> "Building this outer harness is emerging as an ongoing engineering practice, not a one-time configuration."
> — การสร้าง harness ชั้นนอกนี้กำลังกลายเป็นงานวิศวกรรมที่ทำต่อเนื่อง ไม่ใช่ config ครั้งเดียวจบ

## harness สามชั้น (bounded contexts)

คำว่า harness = ทุกอย่างใน agent ที่ไม่ใช่ model (**Agent = Model + Harness**) ซึ่งกว้างไป Böckeler จำกัดความให้คนใช้ coding agent โดยวาดเป็นวงซ้อนสามชั้น: **model** (ชั้นใน) → **builder harness** (เจ้าของเครื่องมือสร้างให้: system prompt, code retrieval, orchestration) → **user harness** (ชั้นนอกที่ผู้ใช้สร้างเองให้เข้ากับ use case) บทความโฟกัสชั้นนอก

เป้าหมายของ outer harness ที่ดี: (1) เพิ่มโอกาส agent ทำถูกตั้งแต่แรก (2) มี feedback loop ดักแก้ก่อนถึงคน → ลด review toil + คุณภาพระบบดีขึ้น + เปลือง token น้อยลง

## Computational vs Inferential

guide/sensor แบ่งตามวิธีรันได้สองแบบ:

- **Computational** — รันด้วย CPU, deterministic, เร็ว (มิลลิวินาที–วินาที), เชื่อถือได้: test, linter, type checker, structural analysis
- **Inferential** — รันด้วย model (GPU/NPU), semantic, ช้า/แพง/non-deterministic: AI code review, "LLM as judge"

computational ถูกพอจะรันทุกการเปลี่ยนแปลง; inferential ใช้ตรงที่ต้องการวิจารณญาณเชิงความหมายและไม่ต้องรันทุก commit

## The steering loop

งานคนคือ **steer** — ปรับ harness ทีละรอบ หลัก: ปัญหาเดิมเกิดซ้ำหลายครั้ง → ปรับ feedforward/feedback ให้เกิดยากขึ้นหรือไม่เกิดอีก (ตรงกับ [[harness-ratchet]]) และใช้ AI ช่วยปรับ harness ได้: เขียน structural test, ร่าง rule จาก pattern, scaffold custom linter, ขุด codebase มาทำ how-to

## Timing: Keep quality left

สาย [[shift-left-testing|continuous integration]]: เจอเร็ว = แก้ถูก กระจาย sensor ตาม lifecycle —

- **ก่อน commit/integrate**: linter, test เร็ว, review agent เบา ๆ
- **หลัง integrate (pipeline)**: mutation testing, review ภาพรวม + รันของเร็วซ้ำ
- **drift/health sensor นอก lifecycle**: dead-code, คุณภาพ coverage, dependency scan, agent ดู SLO ที่ค่อย ๆ แย่, AI judge สุ่มเช็คคุณภาพ + จับ log ผิดปกติ

## Regulation categories

harness = **cybernetic governor** (ตัวกำกับสายไซเบอร์เนติกส์ — feedforward + feedback คุมระบบเข้าสู่สภาพที่ต้องการ) แยกเป็นสามมิติ:

1. **Maintainability harness** — คุมคุณภาพโค้ดภายใน *ง่ายสุดตอนนี้*: computational จับโครงสร้าง (โค้ดซ้ำ, complexity, coverage, drift, style) แน่นอน; LLM จับของเชิงความหมาย (semantic dup, test ซ้ำ, brute-force, over-engineer) ได้บ้างแต่แพง; ของหนักสุด (วินิจฉัยผิด, feature เกิน, เข้าใจคำสั่งผิด) จับไม่ค่อยได้ — "correctness อยู่นอก remit ของ sensor ถ้าคนไม่ได้บอกแต่แรกว่าต้องการอะไร"
2. **Architecture fitness harness** — คือ [[fitness-function|fitness function]]: skill ป้อน perf requirement + perf test feedback; logging standard + ให้ agent สะท้อนคุณภาพ log
3. **Behaviour harness** — "ช้างในห้อง" ยังไม่มีคำตอบดี: ปัจจุบัน feedforward = functional spec, feedback = test เขียว + coverage + mutation + manual แต่ฝากความหวังไว้กับ test ที่ AI สร้างเองมากไป; pattern **approved fixtures** ช่วยได้บางงาน ไม่ใช่คำตอบเหมารวม

## Harnessability

บาง codebase ครอบง่ายกว่า: strongly typed → ได้ type checker ฟรี; module ขอบเขตชัด → ตั้ง architecture rule ได้; framework อย่าง Spring ซ่อนรายละเอียด → เพิ่มโอกาสสำเร็จโดยปริยาย greenfield ฝัง harnessability ได้แต่วันแรก; legacy หนี้เยอะเจอ paradox: **harness จำเป็นที่สุดตรงที่สร้างยากที่สุด**

## Harness templates

service topology ที่ครอบ 80% ของงาน (business service เปิด API, event processor, data dashboard) อาจกลายเป็น **harness template** — ชุด guide+sensor สำเร็จที่ leash agent ให้อยู่ในโครงสร้าง/convention/stack ของ topology นั้น แต่เจอปัญหา sync/versioning แบบ service template และหนักกว่าเพราะ inferential control ทดสอบยาก

## หลักฐานจากสนามจริง (ใน "open questions")

- **OpenAI** เขียนถึง harness ของตัวเอง: layered architecture บังคับด้วย custom linter + structural test, มี "garbage collection" คอยสแกน drift แล้วให้ agent เสนอแก้ — สรุปว่า "ความท้าทายยากสุดตอนนี้คือการออกแบบ environment, feedback loop, control system"
- **Stripe minions**: pre-push hook ที่เลือก linter ตาม heuristic, เน้น "shift feedback left", "blueprints" ฝัง sensor เข้า workflow
- Mutation/structural testing กลับมาได้รับความนิยม (computational sensor ที่เคยถูกมองข้าม)
- มีกระแสเรื่อง integrate LSP / code intelligence (computational feedforward guide)
- ทีม Thoughtworks สู้ architecture drift ด้วย "janitor army" + custom linter ผสม agent

## หมายเหตุ

- บทความนี้ **supersede** memo ฉบับแรกของ Böckeler (2026-02-17) ที่เพิ่งนิยามคำว่า harness engineering
- ตอนท้ายระบุว่าใช้ GenAI (Claude + [[claude-code|Claude Code]]) ช่วย research, ดึงไอเดียจาก note เดิม, และขัดเกลาภาษา

## See also

- [[harness-guides-sensors]]
- [[birgitta-bockeler]]
- [[thoughtworks]]
- [[coding-harness]]
- [[harness-engineering]]
- [[harness-ratchet]]
- [[shift-left-testing]]
- [[what-weve-learned-building-cloud-agents]]
