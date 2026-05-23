---
title: Addy Osmani
type: entity
tags: [ai, software-engineering, web, google, agents]
created: 2026-05-10
updated: 2026-05-10
sources: [Agent Harness Engineering.md, 5 Agent Design patterns for Long-running AI Agents.md]
---

# Addy Osmani

[[google-cloud|Google Cloud]] / Google engineer และผู้เขียนด้าน web performance, software engineering, และ agent architecture. ใน wiki นี้ Addy สำคัญเพราะช่วยจัดภาษาของวงการ agent จาก "เลือก model" ไปสู่ "ออกแบบ runtime และ harness"

## บทบาทใน wiki นี้

- เขียน [[google-cloud-long-running-agent-patterns]] ร่วมกับ Shubham Saboo — สรุป 5 pattern สำหรับ [[long-running-agents|agent ที่อยู่ข้ามวัน]]
- เขียน [[agent-harness-engineering]] — สังเคราะห์แนวคิดว่า **Agent = Model + Harness** และเสนอให้มอง agent failure เป็นสัญญาณสำหรับปรับ harness

## แนวคิดที่เชื่อมกับ Addy

- [[long-running-agents]] — checkpoint/resume, delegated approval, memory-layered context, ambient processing, fleet orchestration
- [[coding-harness]] — prompt, tools, filesystem, sandbox, memory, hooks, subagent, และ observability รอบ model
- [[harness-ratchet]] — ทุก mistake ของ agent ควรกลายเป็น rule/hook/test ที่กัน failure class เดิม

## See also

- [[google-cloud]]
- [[google-cloud-long-running-agent-patterns]]
- [[agent-harness-engineering]]
- [[coding-harness]]
- [[harness-ratchet]]
