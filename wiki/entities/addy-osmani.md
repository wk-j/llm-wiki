---
title: Addy Osmani
type: entity
tags: [ai, software-engineering, web, google, agents]
created: 2026-05-10
updated: 2026-11-05
sources: [Agent Harness Engineering.md, 5 Agent Design patterns for Long-running AI Agents.md, The Orchestration Tax.md, "Loop Engineering..md", Agentic Code Review.md, the-new-software-lifecycle.md, critical-thinking-when-agents-do-the-work-osmani.md]
---

# Addy Osmani

Addy Osmani เขียนเรื่องประสิทธิภาพเว็บ การพัฒนาซอฟต์แวร์ และการออกแบบระบบรอบ AI agent งานของเขาใน wiki นี้ช่วยอธิบายว่า การใช้ agent ให้ได้ผลต้องคิดไกลกว่าแค่เลือก model ต้องดูด้วยว่าจะจัดเครื่องมือ วิธีตรวจงาน และขั้นตอนทำงานอย่างไร

แหล่งเก่าใน wiki กล่าวถึงเขาในบทบาทวิศวกรที่ Google และ [[google-cloud|Google Cloud]] ส่วนโปรไฟล์ X ที่อ่านวันที่ 2026-11-05 ระบุว่าเขาทำงานกับ Claude Code ที่ Anthropic

## บทบาทใน wiki นี้

- เขียน [[google-cloud-long-running-agent-patterns]] ร่วมกับ Shubham Saboo — สรุป 5 pattern สำหรับ [[long-running-agents|agent ที่อยู่ข้ามวัน]]
- เขียน [[agent-harness-engineering]] — สังเคราะห์แนวคิดว่า **Agent = Model + Harness** และเสนอให้มอง agent failure เป็นสัญญาณสำหรับปรับ harness
- เขียน [[the-orchestration-tax]] — แกะแนวคิด [[orchestration-tax|orchestration tax]] (ชื่อที่ Richard Seroter ตั้งบน panel Google I/O): มนุษย์คือ serial resource ตัวเดียวที่ขนานไม่ได้ในวง agent ต้องออกแบบ attention เหมือนออกแบบระบบ concurrent
- เขียน [[loop-engineering-osmani]] — เสนอ [[loop-engineering|loop engineering]]: เลิกเป็นคนพิมพ์ prompt เอง ไปออกแบบ "ลูป" ที่พิมพ์ prompt ให้ agent แทน; ลูป = harness ที่รันบน timer + แตก helper + ป้อนงานตัวเอง; 5 ชิ้น + memory; อยู่ชั้นบนของ [[agent-harness-engineering]] หนึ่งชั้น
- เขียน [[agentic-code-review]] — วางกรอบ [[agentic-code-review|agentic code review]]: เมื่อ agent ผลิตโค้ดเร็วกว่า human review capacity งานสำคัญย้ายไปที่ risk-tiered review, evidence intake, heterogeneous AI reviewers, deterministic gates, และมนุษย์ที่ยัง own merge
- เขียน [[the-new-software-lifecycle]] จาก whitepaper ที่ร่วมเขียนกับ Google — เสนอ [[ai-driven-sdlc|AI-driven SDLC]] ว่า implementation เร็วขึ้นไม่เท่ากับ lifecycle ทั้งเส้นเร็วตาม; specification, architecture และ verification กลายเป็นคอขวดใหม่

## แนวคิดที่เชื่อมกับ Addy

- [[agentic-code-review]] — review ในยุค agent ต้องจัดตาม blast radius และ evidence ไม่ใช่อ่านทุก diff เท่ากัน
- [[loop-engineering]] — ออกแบบระบบที่ prompt agent แทนเรา; 5 ชิ้น + memory; จุดงัดย้ายจาก prompt ไปเป็นลูป
- [[git-worktrees]] — isolation เชิงกลไกของ agent ขนาน; worktree กันไฟล์ชน แต่ไม่เพิ่ม review bandwidth
- [[orchestration-tax]] — ช่องว่างระหว่างของที่ agent ผลิตได้กับของที่มนุษย์ merge ได้จริง; เราคือ GIL ของ agent
- [[long-running-agents]] — checkpoint/resume, delegated approval, memory-layered context, ambient processing, fleet orchestration
- [[coding-harness]] — prompt, tools, filesystem, sandbox, memory, hooks, subagent, และ observability รอบ model
- [[harness-ratchet]] — ทุก mistake ของ agent ควรกลายเป็น rule/hook/test ที่กัน failure class เดิม
- [[ai-driven-sdlc]] — วงจรพัฒนาที่เอา harness, context, output/trajectory eval และ model routing มาวางเป็นระบบเดียว

## เมื่อ agent ทำงานแทน เรายังต้องคิดเองตรงไหน

ใน [[critical-thinking-when-agents-do-the-work-osmani|บทความวันที่ 2026-11-03]] Addy ชวนให้ตั้งสมมติฐานก่อนถาม AI และอ่านหลักฐานก่อนเชื่อว่างานเสร็จ แม้ agent จะช่วยทั้งเขียนโค้ดและตรวจงานได้ คนส่งงานก็ยังต้องอธิบายและรับผิดชอบผล

เขาเชื่อม [[cognitive-surrender|การเลิกคิดตรวจเอง]] กับ [[comprehension-debt|หนี้ความเข้าใจ]] โดยไม่ได้คาดหวังให้คนจำระบบทั้งหมด ขอให้รู้ว่าตรงไหนยังไม่เข้าใจ และกลับไปทำความเข้าใจส่วนนั้นได้เมื่อต้องใช้

โปรไฟล์ที่มากับโพสต์ระบุว่าเขาทำงานกับ Claude Code ที่ Anthropic ส่วนแหล่งเก่าในหน้านี้กล่าวถึงบทบาทที่ Google ยังไม่ทราบวันย้ายงานจากแหล่งนี้

## See also

- [[google-cloud]]
- [[google-cloud-long-running-agent-patterns]]
- [[agent-harness-engineering]]
- [[agentic-code-review]]
- [[loop-engineering-osmani]]
- [[loop-engineering]]
- [[git-worktrees]]
- [[the-orchestration-tax]]
- [[orchestration-tax]]
- [[coding-harness]]
- [[harness-ratchet]]
- [[the-new-software-lifecycle]]
- [[ai-driven-sdlc]]
