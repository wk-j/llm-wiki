---
title: Addy Osmani
type: entity
tags: [ai, software-engineering, web, google, agents]
created: 2026-05-10
updated: 2026-06-09
sources: [Agent Harness Engineering.md, 5 Agent Design patterns for Long-running AI Agents.md, The Orchestration Tax.md, "Loop Engineering..md"]
---

# Addy Osmani

[[google-cloud|Google Cloud]] / Google engineer และผู้เขียนด้าน web performance, software engineering, และ agent architecture. ใน wiki นี้ Addy สำคัญเพราะช่วยจัดภาษาของวงการ agent จาก "เลือก model" ไปสู่ "ออกแบบ runtime และ harness"

## บทบาทใน wiki นี้

- เขียน [[google-cloud-long-running-agent-patterns]] ร่วมกับ Shubham Saboo — สรุป 5 pattern สำหรับ [[long-running-agents|agent ที่อยู่ข้ามวัน]]
- เขียน [[agent-harness-engineering]] — สังเคราะห์แนวคิดว่า **Agent = Model + Harness** และเสนอให้มอง agent failure เป็นสัญญาณสำหรับปรับ harness
- เขียน [[the-orchestration-tax]] — แกะแนวคิด [[orchestration-tax|orchestration tax]] (ชื่อที่ Richard Seroter ตั้งบน panel Google I/O): มนุษย์คือ serial resource ตัวเดียวที่ขนานไม่ได้ในวง agent ต้องออกแบบ attention เหมือนออกแบบระบบ concurrent
- เขียน [[loop-engineering-osmani]] — เสนอ [[loop-engineering|loop engineering]]: เลิกเป็นคนพิมพ์ prompt เอง ไปออกแบบ "ลูป" ที่พิมพ์ prompt ให้ agent แทน; ลูป = harness ที่รันบน timer + แตก helper + ป้อนงานตัวเอง; 5 ชิ้น + memory; อยู่ชั้นบนของ [[agent-harness-engineering]] หนึ่งชั้น

## แนวคิดที่เชื่อมกับ Addy

- [[loop-engineering]] — ออกแบบระบบที่ prompt agent แทนเรา; 5 ชิ้น + memory; จุดงัดย้ายจาก prompt ไปเป็นลูป
- [[git-worktrees]] — isolation เชิงกลไกของ agent ขนาน; worktree กันไฟล์ชน แต่ไม่เพิ่ม review bandwidth
- [[orchestration-tax]] — ช่องว่างระหว่างของที่ agent ผลิตได้กับของที่มนุษย์ merge ได้จริง; เราคือ GIL ของ agent
- [[long-running-agents]] — checkpoint/resume, delegated approval, memory-layered context, ambient processing, fleet orchestration
- [[coding-harness]] — prompt, tools, filesystem, sandbox, memory, hooks, subagent, และ observability รอบ model
- [[harness-ratchet]] — ทุก mistake ของ agent ควรกลายเป็น rule/hook/test ที่กัน failure class เดิม

## See also

- [[google-cloud]]
- [[google-cloud-long-running-agent-patterns]]
- [[agent-harness-engineering]]
- [[loop-engineering-osmani]]
- [[loop-engineering]]
- [[git-worktrees]]
- [[the-orchestration-tax]]
- [[orchestration-tax]]
- [[coding-harness]]
- [[harness-ratchet]]
