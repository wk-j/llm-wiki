---
title: Deep Agent Audit
type: concept
tags: [ai, agents, audit, code-review, verification, software-engineering]
created: 2026-07-02
updated: 2026-07-02
sources: [aom-fable-elysia-2-audit.md]
---

# Deep Agent Audit / การ audit โค้ดแบบ agent ลึก

**Deep agent audit** คือการปล่อย agent หรือ agent fleet ตรวจ codebase แบบลึกกว่าการ review ปกติ: อ่านหลาย path, แตกสมมติฐาน, หา edge case, ผูกปัญหากับหลักฐาน, เสนอวิธีแก้, และ verify ว่าปัญหามีจริง. คำนี้ใน wiki มาจาก source [[aom-fable-elysia-2-audit|Fable audit Elysia 2]] ที่ [[fable|Fable]] สร้าง report 104 ข้อให้ [[elysia-2|Elysia 2]].

มันต่างจากการถาม model ว่า "พร้อม release ไหม" เพราะ output ที่ดีไม่ใช่ verdict แต่เป็นรายการปัญหาที่เจ้าของระบบเอาไปตัดสินใจต่อได้.

## กลไกที่ทำให้ต่างจาก review ปกติ

ใน review ปกติ คนมักติดเพดานเวลา. อ่าน diff, ดู test, เช็ค path เสี่ยง แล้วตัดสินใจ. Deep agent audit ใช้ข้อได้เปรียบของ agent ตรงที่มันยอมทำงานซ้ำ ๆ ยาว ๆ ได้:

- แตก agent หลายตัวเพื่อดูคนละมุม
- ไล่ codebase เก่าและ path ที่ owner เริ่มชินจนมองข้าม
- เขียน report ที่มีปัญหา, severity, วิธีแก้, และวิธี verify
- ทำซ้ำจนกว่าจะชน budget/limit

ใน source ของ Aom, Fable แตก agent เกือบ 100 ตัวและสร้าง report 24,000 คำ. ถ้าข้ออ้างนี้ตรงกับงานจริง จุดได้เปรียบไม่ใช่ "มันฉลาดกว่าเสมอ" แต่คือมันลงทุน attention แบบที่มนุษย์ไม่คุ้มจะลงทุนกับทุก release.

**ได้อะไร:** agent เปลี่ยน audit จากงานที่แพงเกินทำบ่อย ให้กลายเป็นงานที่ทำได้บ่อยขึ้น แต่ยังต้องมีคนอ่านผลและตัดสินใจ.

## ความเสี่ยง: report ยาวไม่เท่ากับถูก

Deep audit เสี่ยงสร้าง [[orchestration-tax|orchestration tax]] แบบใหม่. Report 104 ข้ออาจช่วยมากถ้าข้อชี้ถูกและจัดลำดับดี. แต่ถ้ามี false positive เยอะ คนจะเสียเวลาตรวจ report แทนตรวจ code.

ดังนั้น report ที่ดีควรมี:

- severity แยกชัดว่าอะไร block RC, อะไรเป็น cleanup
- evidence ที่ trace กลับไปหา code/test ได้
- repro หรือ test case สำหรับ bug สำคัญ
- owner decision log ว่าข้อไหนรับ, ข้อไหน reject, เพราะอะไร
- follow-up patch หรือ issue ที่เล็กพอจะปิดได้จริง

**ผลคือ:** deep agent audit ต้องถูกวัดด้วย confirmed findings และ decision quality ไม่ใช่จำนวนคำหรือจำนวนข้อ.

## เชื่อมกับ agentic code review

[[agentic-code-review|Agentic Code Review]] บอกว่า AI reviewer เป็น sensor ไม่ใช่ verdict. Deep agent audit คือ sensor ที่ใช้เวลานานและกิน budget มากกว่า เหมาะกับ gate สำคัญ เช่น RC/stable release, security-sensitive subsystem, migration ใหญ่, หรือ codebase ที่ owner เริ่มไม่มั่นใจ.

ในงานเล็ก มันอาจเกินเหตุ. ในงาน release สำคัญ มันอาจถูกกว่าการให้ทีมมนุษย์ audit 2-3 สัปดาห์.

**ได้อะไร:** ใช้ deep audit เป็น review tier สูง ไม่ใช่ default ทุก PR.

## คำถามที่ต้องตอบก่อนเชื่อ

- confirmed bug rate เท่าไหร่.
- false positive rate เท่าไหร่.
- ข้อที่เจอเป็น correctness, security, compatibility, architecture, หรือ taste.
- agent verify เองด้วยอะไร: test, static analysis, code path reasoning, หรือแค่ narrative.
- report ลด risk หลัง release จริงไหม เมื่อเทียบกับเวลาอ่าน report.

## See also

- [[aom-fable-elysia-2-audit]]
- [[fable]]
- [[elysia-2]]
- [[agentic-code-review]]
- [[coding-harness]]
- [[orchestration-tax]]
- [[model-honesty]]
- [[behavioral-verifier]]
- [[long-running-agents]]
