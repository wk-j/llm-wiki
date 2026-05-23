---
title: Agent Harness Engineering
type: source
tags: [ai, agents, harness, software-engineering]
url: https://x.com/addyosmani/status/2053231239721885918
date_ingested: 2026-05-10
created: 2026-05-10
updated: 2026-05-10
sources: []
---

# Agent Harness Engineering / วิศวกรรม Harness ของ Agent

โพสต์นี้ของ [[addy-osmani|Addy Osmani]] (วิศวกรที่เขียนเรื่อง web performance และ agent architecture) สรุปกระแสหนึ่งที่เริ่มชัดในปี 2026: งานสำคัญของ coding agent ไม่ได้อยู่แค่การเลือก model แต่คือการออกแบบ **harness** (โครงรอบ model ที่ให้ context, tools, state, policy, และ feedback loop)

แก่นสั้น ๆ คือ **Agent = Model + Harness**. ถ้าสองเครื่องมือใช้ model เดียวกัน แต่มี prompt, tool, sandbox, hooks, memory, และ subagent ต่างกัน พฤติกรรมที่ได้ก็จะต่างกันมาก ตัว model เป็นแค่ input หนึ่งของระบบ ตัว harness คือสิ่งที่ทำให้ model ทำงานจริงได้

## แก่นความคิด

Addy ชี้ว่าช่วงสองปีที่ผ่านมา วงการถกกันมากเรื่อง "model ไหนฉลาดกว่า" แต่การใช้งานจริงกลับถูกกำหนดโดยสิ่งรอบ model จำนวนมาก เช่น `AGENTS.md`, `CLAUDE.md`, skill files, MCP tools, sandbox, context compaction, subagent routing, hooks, log/trace, และ cost meter

พูดแบบ engineer: agent คือ loop ที่คิด → เรียก tool → ดูผล → ทำต่อ. Harness คือคนออกแบบ loop นั้นและโลกที่ loop เข้าไปแตะ

**ได้อะไร:** ถ้า harness ดี model ธรรมดาก็ทำงานได้ไกลกว่า model เก่งที่ถูกใส่ใน harness แย่ ๆ

## เปลี่ยนจากโทษ model เป็นแก้ harness

โพสต์นี้เสนอให้เลิกมอง failure ของ agent เป็นเรื่อง "รอ model รุ่นหน้า" ก่อนเสมอ ถ้า agent พลาดซ้ำ ๆ ส่วนใหญ่เราทำอะไรกับ harness ได้:

- ถ้า agent เมิน convention ให้เพิ่มกฎสั้น ๆ ใน `AGENTS.md`
- ถ้า agent รันคำสั่งเสี่ยง ให้เขียน hook กันก่อน tool call
- ถ้า agent หลงในงาน 40 ขั้น ให้แยก planner กับ executor
- ถ้า agent ship code พัง ให้เอา typecheck/test failure ย้อนกลับเข้า loop

ตรงนี้โยงกับ [[humanlayer|HumanLayer]] (บริษัทที่ทำ agent harness) ที่มอง failure หลายแบบเป็น **configuration problem** มากกว่า model problem

**ได้อะไร:** งานปรับปรุง agent กลายเป็น engineering surface ที่ทีมควบคุมได้เอง ไม่ต้องรอ vendor อย่างเดียว

## Ratchet: ความผิดพลาดต้องกลายเป็นกฎ

ส่วนที่มีน้ำหนักที่สุดคือ pattern ที่หน้านี้เรียก [[harness-ratchet|Harness Ratchet]]: ทุกครั้งที่ agent ทำพลาด ให้แปลงความพลาดนั้นเป็น constraint ถาวรใน harness

ตัวอย่างจากโพสต์: ถ้า agent ส่ง PR ที่ comment out test แล้วหลุด merge ไป ครั้งต่อไปต้องมีหลายชั้นมารับ:

- `AGENTS.md` บอกชัดว่าอย่า comment out test
- pre-commit hook ดัก `.skip(` หรือ test ที่ถูกปิด
- reviewer subagent ต้อง block งานลักษณะนี้

Addy เน้นว่ากฎใน prompt ที่ดีควร trace กลับไปหา failure จริงในอดีตได้ ไม่ใช่กฎที่เขียนเผื่อทุกอย่างตั้งแต่วันแรก

**ผลคือ:** harness ของแต่ละทีมจะไม่เหมือนกัน เพราะมันสะสมประวัติ failure ของ codebase และ workflow นั้น ๆ

## Component taxonomy: harness มีอะไรบ้าง

Addy จัด component ของ harness ตาม behavior ที่ต้องการ ไม่ใช่ตามชื่อ feature:

| Behavior ที่ต้องการ | Harness component |
|---|---|
| เก็บ state และประสานงานข้าม agent | filesystem, worktree, Git |
| ให้ agent สร้าง tool เองได้ | bash, code execution |
| รันได้โดยไม่ทำ host พัง | sandbox, permission gate |
| เรียนรู้ข้าม session | memory files, `AGENTS.md`, search, MCP |
| ไม่ให้ context เน่า | [[compaction]], tool-output offloading, [[progressive-disclosure]] |
| ทำงานยาว | loops, planner/executor split, self-verification |
| บังคับ policy จริง | hooks, middleware, lint/test gate |
| ลด prompt bloat | concise rulebook, focused tools |

หลักตรวจง่าย ๆ คือ: ถ้าบอกไม่ได้ว่า component นี้มีไว้ให้เกิด behavior อะไร ก็ควรตัดออก

## Context rot และ progressive disclosure

โพสต์นี้ยืนยันสอง concept ที่ wiki มีอยู่แล้ว:

- [[context-rot]] — พอ context ยาวขึ้น model คิดแย่ลง แม้ยังไม่ชน hard limit
- [[progressive-disclosure]] — อย่าโหลด instruction/tool/schema ทั้งหมดตั้งแต่ต้น ให้เปิดเผยเมื่อมีงานที่ต้องใช้

Addy เพิ่มคำว่า **tool-call offloading**: output ใหญ่ ๆ เช่น log 2,000 บรรทัด ไม่ควรยัดเข้า context ทั้งก้อน ควรเก็บใน filesystem แล้วส่งเฉพาะส่วนสำคัญกลับเข้า loop

**ได้อะไร:** context window เหลือไว้ให้ reasoning แทนที่จะถูกกินด้วยคู่มือและ output ดิบ

## Hooks คือ enforcement layer

โพสต์นี้แยก "ขอให้ agent ทำ" ออกจาก "บังคับให้ระบบทำ" ชัดเจนขึ้น Hook คือกลไกที่รันตาม lifecycle เช่น ก่อน tool call, หลังแก้ไฟล์, ก่อน commit

หน้าที่ของ hook:

- block คำสั่งทำลายข้อมูล
- auto-format เพื่อลด token ที่เสียกับ style feedback
- รัน test/typecheck แล้วส่ง error กลับเข้า loop

หลักที่ดีคือ **success silent, failure verbose**. ถ้า typecheck ผ่าน ไม่ต้องพูดอะไรกับ agent. ถ้าพัง ให้ส่ง error ที่แก้ได้กลับเข้า context

**ได้อะไร:** feedback loop กลายเป็นระบบ ไม่ใช่คนต้องคอยเตือนซ้ำใน chat

## Harness-as-a-Service

Addy มองว่าตลาดกำลังขยับจาก LLM API ไปสู่ **Harness API** หรือ runtime สำเร็จรูปที่มี loop, tools, sandbox, context management, hooks, และ memory มาให้

แทนที่จะสร้าง orchestration ทุกอย่างเอง ทีมจะเลือก framework แล้วปรับ surface เฉพาะ domain ของตัวเอง เช่น prompt, tool, policy, และ evaluator

[[flue|Flue]] ของ [[fred-schott|Fred Schott]] ถูกยกเป็นตัวอย่าง framework ที่รับแนวคิดนี้ไปทำเป็นเครื่องมือ

**ได้อะไร:** งานของทีมย้ายจาก "สร้าง agent runtime จากศูนย์" เป็น "ปรับ harness ให้เข้ากับ failure history และ workflow ของเรา"

## เชื่อมกับแหล่งอื่นใน wiki

- [[coding-harness]] — Addy ใช้คำว่า harness ในความหมายเดียวกับ Alex Ker: scaffolding ทั้งหมดรอบ model
- [[harness-engineering]] — ขยายคำนี้จาก pipeline review agent ของ Panutat ไปสู่ discipline ของการปรับ scaffold รอบ agent ทั้งระบบ
- [[ryan-lopopolo-harness-engineering]] — แนวคิด durable feedback loops ตรงกับ Harness Ratchet: ความพลาดต้องกลายเป็น lint/test/docs ไม่ใช่ feedback ครั้งเดียว
- [[long-running-agents]] — Addy เคยเขียน pattern ของ agent ที่อยู่ข้ามวันกับ Shubham Saboo; source นี้เป็นมุมที่กว้างกว่าเรื่อง runtime ของ coding agent
- [[agent-runtime-untrusted]] — sandbox, permission gate, audit, และ policy ภายนอก model คือส่วนที่ harness ต้องรับผิดชอบ

## See also

- [[addy-osmani]]
- [[vtrivedy]]
- [[coding-harness]]
- [[harness-engineering]]
- [[harness-ratchet]]
- [[context-rot]]
- [[progressive-disclosure]]
- [[humanlayer]]
- [[claude-code]]
- [[flue]]
