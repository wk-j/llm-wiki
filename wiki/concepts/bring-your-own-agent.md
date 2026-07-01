---
title: Bring Your Own Agent
type: concept
tags: [ai, agents, harness, mcp, skills, product, developer-tools]
created: 2026-06-29
updated: 2026-06-29
sources: ["i don't want to use your agent — @RhysSullivan.md"]
---

# Bring Your Own Agent / เอา agent ของตัวเองมาใช้

**Bring Your Own Agent (BYO agent)** คือแนวคิดว่า product ไม่ควรล็อกความฉลาดไว้ใน in-app agent ของตัวเองอย่างเดียว. Product ควรเปิดความรู้และ action surface เป็น [[model-context-protocol|MCP]], API, CLI, docs, และ [[skill-procedures-vs-abilities|skills]] เพื่อให้ agent ประจำวันของผู้ใช้เอาไปใช้ได้.

[[rhys-sullivan|Rhys Sullivan]] เสนอกรอบนี้ในโพสต์ [[i-dont-want-to-use-your-agent|i don't want to use your agent]]. เขาไม่ได้บอกว่า in-app agent แย่. เขาบอกว่า power user มี agent, model, local files, repo, terminal, memory, และ workflow ของตัวเองอยู่แล้ว. Product ควรทำให้ agent นั้นกลายเป็น expert ใน product ไม่ใช่บังคับให้ user ย้ายเข้า chat อีกช่อง.

## ปัญหา: product agent ไม่ใช่ daily-driver agent

หลายบริษัทเริ่มใส่ agent ใน dashboard. แบบนี้ดีสำหรับ user ทั่วไป เพราะไม่ต้อง setup อะไร. แต่สำหรับ power user มันชนสองเรื่อง:

- **Model ceiling** — บริษัทอาจใช้ model ที่ถูกกว่าเพื่อคุมต้นทุน ส่วน user จ่าย frontier model เองอยู่แล้ว
- **Context ceiling** — agent ในเว็บเห็นเฉพาะ product นั้น แต่ daily-driver agent เห็น local repo, file, terminal, script, issue, memory, และ workflow ส่วนตัว

ผลคือ product agent อาจตอบเรื่อง product ได้ดี แต่ยังไม่ใช่ที่ทำงานหลักของ user.

## สิ่งที่ product ควรขายจริง ๆ

ในกรอบนี้ สิ่งที่บริษัทควรทำให้พกพาได้ไม่ใช่ "agent ทั้งตัว" แต่เป็น **product expertise**:

- docs ที่ agent อ่านแล้วรู้ product surface จริง
- CLI/API/MCP tools ที่เรียก action จริงได้
- resources เช่น schema, metrics, config, permissions, account state
- prompts หรือ skills สำหรับ workflow เฉพาะทาง
- deeplink ไป UI เพื่อให้คนตรวจหรือดูภาพต่อได้

ตัวอย่างง่าย ๆ: [[linear|Linear]] ไม่จำเป็นต้องชนะ Claude Code หรือ Codex ในฐานะ agent. Linear ควรทำให้ agent ของผู้ใช้แตก problem เป็น ticket, อ่าน project context, จัด priority, และเปิด issue ได้ดี.

## โครงสร้างที่ดี: internal agent ใช้ primitive เดียวกัน

ทางที่ประหยัดแรงที่สุดคือบริษัทสร้าง in-app agent ของตัวเองจาก primitive เดียวกับที่เปิดให้ power user:

| ชั้น | user ทั่วไป | power user |
|---|---|---|
| UI | ใช้ chat ใน product | ใช้ agent ประจำวันของตัวเอง |
| Knowledge | product docs / internal prompts | skills + docs package เดียวกัน |
| Action | internal tool calls | MCP / API / CLI เดียวกัน |
| Review | ดูผลใน dashboard | deeplink กลับ dashboard หรือ PR/ticket |

แบบนี้บริษัทมี source of truth เดียว. ถ้า update docs, skill, หรือ tool schema ทั้ง in-app agent และ external agent ได้ประโยชน์พร้อมกัน.

## เชื่อมกับ harness-first

กรอบนี้ต่อกับ [[coding-harness]] โดยตรง. ถ้า agent = model + harness + environment แล้ว power user มักมี harness/environment ของตัวเองที่ดีกว่าสำหรับงานของเขา. Product จึงควรยอมให้ความรู้ของ product เดินทางเข้า harness นั้นได้.

มันยังเป็นการแยก [[three-learning-layers|สามชั้นของการเรียนรู้]] ให้ชัด:

- **Model** — user เลือกเอง อาจเป็น frontier model ที่จ่ายเงินเอง
- **Harness** — user ใช้ของประจำ เช่น Codex, Claude Code, OpenCode, Cursor, pi
- **Context** — บริษัทส่ง product knowledge, skills, docs, และ tools ให้

ตรงนี้คือประโยชน์จริง: บริษัทไม่ต้องแบกต้นทุน model แรงสุดให้ทุกคน แต่ยังทำให้ power user ใช้ product ได้ลึกขึ้น.

## ข้อควรระวัง

BYO agent ไม่ใช่คำตอบสำหรับทุกคน. user ปกติยังต้องการ chat ที่ใช้ได้ทันทีใน product. ถ้าบริษัททำแต่ MCP/CLI/skills แล้วไม่มี surface ง่าย ๆ ก็ทิ้งคนส่วนใหญ่.

อีกเรื่องคือ security. การเปิด tool ให้ external agent เรียกต้องมี permission, audit log, scope, rate limit, และ human confirmation สำหรับ action เสี่ยง. ไม่อย่างนั้น product expertise จะกลายเป็นช่องทางให้ agent ทำผิดเร็วขึ้น.

## ได้อะไร

BYO agent เปลี่ยนคำถามจาก "บริษัทเราควรสร้าง agent ไหม" เป็น "ความรู้ของ product เราเอาไปใช้ใน agent อื่นได้ดีแค่ไหน". บริษัทที่ตอบข้อนี้ได้ จะได้ทั้ง user ธรรมดาที่ใช้ in-app chat และ power user ที่ฝัง product เข้า workflow ของตัวเอง.

## See also

- [[i-dont-want-to-use-your-agent]]
- [[coding-harness]]
- [[model-context-protocol]]
- [[skill-procedures-vs-abilities]]
- [[agent-experience]]
- [[three-learning-layers]]
- [[meta-harness]]
