---
title: Agentic Code Review
type: concept
tags: [ai, agents, code-review, verification, software-engineering]
created: 2026-06-16
updated: 2026-07-02
sources: [Agentic Code Review.md, aom-fable-elysia-2-audit.md]
---

# Agentic Code Review / การ review โค้ดในยุค agent

**Agentic code review** คือวิธีออกแบบ code review ใหม่เมื่อ coding agent ผลิตโค้ดได้เร็วกว่า review capacity ของมนุษย์หลายเท่า. แก่นไม่ใช่ "ให้ AI review แทนคน" แต่คือ **จัดระบบความเชื่อมั่น**: ใช้ deterministic gate, AI reviewer, risk tier, และ human judgement ให้ถูกที่.

[[addy-osmani|Addy Osmani]] (วิศวกร Google ที่เขียนเรื่อง [[orchestration-tax|orchestration tax]] และ [[loop-engineering|loop engineering]]) สรุปใน [[agentic-code-review|Agentic Code Review]] ว่า writing cheap ลงแล้ว แต่ understanding ยังแพงเท่าเดิม. Review เลยกลายเป็น skill ที่ leverage สูงที่สุดใน software ตอนนี้.

## ปัญหาหลัก: output โตเร็วกว่า trust

สมัยก่อน senior engineer อ่านโค้ดได้เร็วกว่า junior เขียนโค้ด. Review เลยตาม production ทันโดยไม่ต้องออกแบบมาก. Agent ทำลายสมดุลนั้น. มันผลิต diff ใหญ่และดูเรียบร้อยได้เร็วมาก แต่ human reading speed ไม่ได้เร็วขึ้น.

นี่คือรูปเฉพาะของ [[orchestration-tax|orchestration tax]]: คอขวดไม่ใช่การเขียนแล้ว แต่คือการตัดสินว่า change นี้ถูกไหม, ควร merge ไหม, และใครเข้าใจพอจะรับผิดชอบมัน.

**ได้อะไร:** ถ้าเพิ่ม agent โดยไม่เพิ่ม review system ระบบจะไม่ ship ดีขึ้นเท่าที่ dashboard บอก. มันแค่สะสม unread code, shallow review, และ [[cognitive-surrender|cognitive surrender]].

## Review ต้อง tier ตาม blast radius

Agentic review เริ่มจากถามว่า "ถ้าพัง เสียหายแค่ไหน" ไม่ใช่ "ใครเขียน". ตัวแปรหลักมีสามตัว:

- **Blast radius** — bug กระทบอะไร: ไม่มีใคร, ผู้ใช้จริง, เงิน, privacy, security, on-call
- **อายุของโค้ด** — prototype ที่ทิ้งได้ หรือ subsystem ที่จะอยู่หลายปี
- **จำนวนคนที่ต้องเข้าใจ** — solo builder หรือทีมที่ต้อง share ownership

ดังนั้น review depth ต้องเป็น dial:

| บริบท | Review ที่สมเหตุสมผล |
|---|---|
| Solo / no users / throwaway | test จริง + automation + อ่านส่วนเสี่ยง |
| เริ่มมี users / team เล็ก | intake evidence + PR เล็ก + owner review ตรง path สำคัญ |
| Legacy / high-blast-radius | type/test/CI + AI reviewers ต่างชนิด + system owner + security/architecture pass |

**ผลคือ:** ไม่เสีย human attention กับ boilerplate แต่ก็ไม่เอา "tests pass" ไปแทน judgement ใน path ที่พังแล้วเจ็บ.

## Intent ต้องมากับ PR

Agent PR มักมีปัญหาแปลกกว่ามนุษย์เขียน: โค้ดอาจดูดี แต่ไม่มีใครรู้ว่า "ทำไม" มันออกมาแบบนั้น. Reasoning trace ของ agent เคยมีอยู่ตอนทำงาน แต่หายไปก่อนถึง PR. Reviewer เลยต้องย้อนสร้าง intent เองจาก diff.

Agentic review จึงควร require ก่อน review:

- purpose ของ change
- decision log สั้น ๆ: เลือกวิธีนี้เพราะอะไร, ตัดทางเลือกอะไรทิ้ง
- test output / proof ว่ารันแล้ว
- risk note: path ไหนเปลี่ยน, user impact คืออะไร
- PR ที่เล็กพอให้คนอ่านจริง

ตรงนี้ผูกกับ [[intent-gap|intent gap]] โดยตรง. Natural language plan อย่างเดียวไม่พอ แต่ไม่มี intent เลยก็ทำให้ reviewer กลายเป็นคนแรกที่ต้องเข้าใจโค้ดจากศูนย์.

**ได้อะไร:** ย้ายงานกู้ intent กลับไปที่คน/agent ที่ submit PR ซึ่งมี context ถูกกว่า แทนให้ reviewer จ่ายแพงทีหลัง.

## AI reviewer เป็น sensor ไม่ใช่ verdict

AI reviewer มีประโยชน์มากใน agentic review เพราะมันเป็น [[harness-guides-sensors|inferential sensor]] ที่จับสิ่งเชิงความหมายได้: bug pattern, missing edge case, architecture smell, security concern. แต่ output ของมันควรเป็น input ให้มนุษย์ ไม่ใช่คำตัดสินสุดท้าย.

หลักใช้ที่สำคัญ:

- ใช้ reviewer ที่ต่าง character กันในงานเสี่ยง เช่น ตัวหนึ่งเน้น correctness อีกตัวเน้น production failure severity
- อย่าวัดจาก benchmark กลางอย่างเดียว ให้วัดกับ codebase ของตัวเอง
- ให้ AI reviewer ช่วยจัดลำดับ attention: safe-looking, needs work, high-risk
- อย่า auto-merge เพราะ AI บอกว่า looks good

ความต่างของ reviewer สำคัญเพราะ blind spot ของ model มัก correlated. สี่สำเนาของ model เดียวกันไม่เท่ากับสี่มุมมอง.

**ผลคือ:** AI review ช่วยให้มนุษย์ใช้เวลาในจุดที่แพงที่สุด แต่ accountability ยังอยู่กับคนกด merge.

## Deep audit เป็น review tier สูง

[[aom-khunpanitchot|Aom Khunpanitchot]] ให้ตัวอย่างสุดโต่งใน [[aom-fable-elysia-2-audit|Fable audit Elysia 2]]. เขาให้ AI หลายตัว audit [[elysia-2|Elysia 2]] แล้วส่วนใหญ่บอกว่าพร้อม stable/RC. แต่ [[fable|Fable]] รันผ่าน ultracode auto mode, แตก agent เกือบ 100 ตัว, แล้วส่ง report 104 ข้อที่สรุปว่ายังไม่เหมาะขึ้น RC.

นี่คือ [[deep-agent-audit|deep agent audit]]: ไม่ใช่ review ทุก PR แต่เป็น review tier สูงสำหรับ release gate หรือ codebase สำคัญ. จุดที่ควรเชื่อไม่ใช่ "Fable บอกว่าไม่พร้อม" แต่คือ report มีปัญหาที่ trace ได้, severity ชัด, วิธีแก้ชัด, และมีการ verify.

**ได้อะไร:** AI reviewer มีหลายระดับ. งานประจำใช้ sensor เบา ๆ ได้ แต่งาน release ควรยอมจ่าย budget ให้ audit ลึกขึ้น แล้วให้มนุษย์ตัดสินจาก evidence ไม่ใช่จากความมั่นใจของ model.

## Deterministic gate ต้องแข็งกว่าเดิม

ยิ่ง agent เก่งในการทำให้ dashboard เขียว ยิ่งต้องรักษา gate ที่ไม่ถูกกล่อมด้วยภาษา. CI, type checker, linter, test, coverage threshold, mutation testing, security scan คือกำแพงที่ควรย้ายซ้ายและย้ายยาก.

จุดที่ต้องอ่านด้วยตาคน:

- test ถูกลบหรือ skip
- coverage threshold ถูกลด
- assertion ถูก rewrite ให้ตรงกับ behavior ใหม่
- helper ถูก copy ทั้งที่มีของเดิม
- user-controlled text ไหลเข้า LLM call แล้วกลายเป็น prompt injection surface
- lint/build gate ถูกลดความเข้มเพื่อให้ผ่าน

นี่คือ [[shift-left-testing|shift-left testing]] ในยุค agent: ของ deterministic และถูกควรล้มงานตั้งแต่ต้น. ของ inferential ใช้เสริมตรงที่ต้องตีความ.

**ได้อะไร:** ลดงาน review ที่ควรให้เครื่องจับอยู่แล้ว และกัน failure mode ที่ agent "ทำให้เขียว" โดยทำให้มาตรฐานต่ำลง.

## Human on the loop

ในระบบ agentic review คนไม่จำเป็นต้องอ่านทุกบรรทัดเสมอไป โดยเฉพาะในงาน low-risk. แต่คนยังต้องอยู่ **บนลูป** (human on the loop): sampling, spot-checking, audit, escalation, และตัดสินใจ merge ใน path สำคัญ.

งานที่ยังไม่ควรยกให้ model ทั้งหมด:

- ตัดสินว่า change นี้ควรทำตั้งแต่แรกไหม
- ตัดสิน trade-off ที่กระทบ product / user / org
- high-blast-radius gate
- requirement ที่ไม่มีใครเขียนไว้
- ownership หลัง merge

ตรงนี้คือขอบเขตของ [[loop-engineering|loop engineering]]. ลูปช่วยผลิตและตรวจได้มากขึ้น แต่ถ้าปิดลูปด้วย model ทั้งหมด เราอาจได้ [[cognitive-surrender|borrowed confidence]]: ระบบมั่นใจแทนเรา ทั้งที่ไม่มีคนเข้าใจจริง.

## วิธีจำสั้น ๆ

Agentic code review = **risk tier + evidence intake + deterministic gates + heterogeneous AI sensors + human ownership**.

ถ้าขาด risk tier จะ review หนักเกินในงานเล็กและเบาเกินในงานใหญ่. ถ้าขาด evidence intake reviewer ต้องกู้ intent เอง. ถ้าขาด deterministic gate agent จะ optimize เขียวแทน optimize ถูก. ถ้าขาด AI sensor คนจะจมใน volume. ถ้าขาด human ownership ไม่มีใครรับผิดชอบตอน production พัง.

## See also

- [[agentic-code-review]]
- [[addy-osmani]]
- [[orchestration-tax]]
- [[loop-engineering]]
- [[harness-guides-sensors]]
- [[cognitive-surrender]]
- [[shift-left-testing]]
- [[facts-first]]
- [[intent-gap]]
- [[behavioral-verifier]]
- [[developer-balance]]
- [[deep-agent-audit]]
- [[aom-fable-elysia-2-audit]]
