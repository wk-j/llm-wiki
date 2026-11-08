---
title: Addy Osmani
type: entity
tags: [ai, software-engineering, web, google, agents]
created: 2026-05-10
updated: 2026-11-09
sources: [Agent Harness Engineering.md, 5 Agent Design patterns for Long-running AI Agents.md, The Orchestration Tax.md, "Loop Engineering..md", Agentic Code Review.md, the-new-software-lifecycle.md, critical-thinking-when-agents-do-the-work-osmani.md, your-coding-agents-made-you-a-manager-osmani.md]
---

# Addy Osmani

Addy Osmani เขียนเรื่องประสิทธิภาพเว็บและการพัฒนาซอฟต์แวร์ หลายบทความของเขาอธิบายวิธีใช้ coding agent ตั้งแต่เตรียมข้อมูลและเครื่องมือให้ agent ไปจนถึงตรวจโค้ดที่มันเขียนก่อนนำไปใช้

แหล่งเก่าใน wiki กล่าวถึงเขาในบทบาทวิศวกรที่ Google และ [[google-cloud|Google Cloud]] ส่วนโปรไฟล์ X ที่อ่านวันที่ 2026-11-05 ระบุว่าเขาทำงานกับ Claude Code ที่ Anthropic

## บทบาทใน wiki นี้

- เขียน [[google-cloud-long-running-agent-patterns]] ร่วมกับ Shubham Saboo — เสนอ 5 วิธีออกแบบ [[long-running-agents|agent ที่ทำงานต่อเนื่องหลายวัน]] เช่น บันทึกความคืบหน้าเพื่อกลับมาทำต่อ หยุดรอคนอนุมัติ และแบ่งงานให้ agent หลายตัว
- เขียน [[agent-harness-engineering]] — อธิบายว่า agent ต้องมีทั้ง model และ harness ซึ่งเป็นซอฟต์แวร์ที่ส่งข้อมูลให้ model จัดการการเรียกเครื่องมือ และนำผลกลับมาให้ model ทำงานต่อ เมื่อ agent พลาดซ้ำ ทีมอาจแก้คำแนะนำ เครื่องมือ หรือขั้นตอนตรวจงานได้โดยไม่ต้องรอ model รุ่นใหม่
- เขียน [[the-orchestration-tax]] — อธิบาย [[orchestration-tax|ภาระติดตามและตรวจงานจากหลาย agent]] แม้ agent จะทำงานพร้อมกันได้ คนก็ยังอ่านและตัดสินใจได้ทีละเรื่อง ชื่อนี้มาจาก Richard Seroter บนเวที Google I/O
- เขียน [[loop-engineering-osmani]] — เสนอ [[loop-engineering|การให้ agent เริ่มงานและทำงานต่อเองตามเงื่อนไขที่กำหนด]] เช่น เริ่มตามตารางเวลา แบ่งงานให้ agent อีกตัวตรวจ แล้วบันทึกสิ่งที่ทำเสร็จและงานที่ยังค้างไว้ใช้ในรอบถัดไป
- เขียน [[agentic-code-review]] — เสนอวิธีตรวจโค้ดที่ agent เขียน โดยให้เวลาตรวจตามความเสียหายที่อาจเกิด ดูผล test และหลักฐานประกอบ ใช้ตัวตรวจหลายแบบ และให้คนตัดสินใจว่าจะ merge หรือไม่
- เขียน [[the-new-software-lifecycle]] จาก whitepaper ที่ร่วมเขียนกับ Google — ชี้ว่าแม้ AI จะเขียนโค้ดเร็วขึ้น ทีมก็ยังต้องใช้เวลาตกลงความต้องการ ออกแบบ และตรวจผล ดู [[ai-driven-sdlc|กระบวนการพัฒนาซอฟต์แวร์เมื่อใช้ AI]]
- เขียน [[your-coding-agents-made-you-a-manager-osmani]] — แนะนำวิธีสั่งงาน ตรวจผล และกำหนดสิทธิ์ให้ coding agent โดยคนยังตัดสินใจว่าจะนำงานไหนไปใช้ ดู [[managing-coding-agents]]

## แนวคิดที่เชื่อมกับ Addy

- [[agentic-code-review]] — เลือกวิธีตรวจจากสิ่งที่โค้ดนั้นอาจทำเสียหาย พร้อมดูผล test และหลักฐานว่าใช้งานได้จริง
- [[loop-engineering]] — กำหนดว่า agent จะเริ่มงานเมื่อไร ตรวจผลอย่างไร และทำอะไรต่อ โดยไม่ต้องให้คนพิมพ์สั่งทุกครั้ง
- [[git-worktrees]] — ให้แต่ละ agent แก้ไฟล์ใน working directory ของตัวเอง แต่คนยังต้องตรวจผลงานจากทุกตัว
- [[orchestration-tax]] — เปิด agent เพิ่มแล้ว คนอาจตรวจงานและตัดสินใจไม่ทัน แม้แต่ละตัวจะเขียนโค้ดได้เร็ว
- [[long-running-agents]] — ให้ agent ทำงานต่อเนื่อง โดยบันทึกความคืบหน้า เก็บข้อมูลที่ต้องใช้ต่อ และหยุดรอคนอนุมัติเมื่อจำเป็น
- [[coding-harness]] — ซอฟต์แวร์ที่จัดการคำสั่ง ข้อมูล เครื่องมือ สิทธิ์ และบันทึกการทำงาน เพื่อให้ model อ่านไฟล์ แก้โค้ด และตรวจผลได้
- [[harness-ratchet]] — นำข้อผิดพลาดที่เกิดซ้ำมาเขียนคำแนะนำหรือเพิ่ม test เพื่อช่วยป้องกันการพลาดแบบเดิม
- [[ai-driven-sdlc]] — วางขั้นตอนใช้ AI ตั้งแต่กำหนดความต้องการ เตรียมข้อมูลและเครื่องมือ ไปจนถึงตรวจโค้ดและส่งให้ผู้ใช้
- [[managing-coding-agents]] — มอบหมายงานให้ชัด ให้ agent ตรวจข้อผิดพลาดพื้นฐานเอง และให้คนตรวจสิ่งที่กระทบผู้ใช้หรือความปลอดภัยก่อนอนุมัติ

## เมื่อ agent ทำงานแทน เรายังต้องคิดเองตรงไหน

ใน [[critical-thinking-when-agents-do-the-work-osmani|บทความวันที่ 2026-11-03]] Addy ชวนให้ตั้งสมมติฐานก่อนถาม AI และอ่านหลักฐานก่อนเชื่อว่างานเสร็จ แม้ agent จะช่วยทั้งเขียนโค้ดและตรวจงานได้ คนส่งงานก็ยังต้องอธิบายและรับผิดชอบผล

เขาเชื่อม [[cognitive-surrender|การเลิกคิดตรวจเอง]] กับ [[comprehension-debt|หนี้ความเข้าใจ]] โดยไม่ได้คาดหวังให้คนจำระบบทั้งหมด ขอให้รู้ว่าตรงไหนยังไม่เข้าใจ และกลับไปทำความเข้าใจส่วนนั้นได้เมื่อต้องใช้

โปรไฟล์ที่มากับโพสต์ระบุว่าเขาทำงานกับ Claude Code ที่ Anthropic ส่วนแหล่งเก่าในหน้านี้กล่าวถึงบทบาทที่ Google ยังไม่ทราบวันย้ายงานจากแหล่งนี้


## เมื่อ agent ทำให้เราทำงานแบบผู้จัดการ

ใน [[your-coding-agents-made-you-a-manager-osmani|บทความวันที่ 2026-11-08]] Addy บอกว่านักพัฒนาที่ใช้ coding agent กำลังฝึกทักษะจัดการอยู่แล้ว ทั้งเลือกงาน อธิบายเป้าหมาย ติดตาม และตรวจผล เขาแนะนำให้บอกเหตุผลกับข้อจำกัดที่อ่านจากโค้ดไม่ได้ ให้ agent รันตรวจเอง และให้คนตัดสินใจเรื่องผลิตภัณฑ์ ความปลอดภัย และงานที่จะส่งให้ผู้ใช้

เรื่องนี้เชื่อมกับ [[orchestration-tax|ภาระติดตามงานจากหลาย agent]] เพราะถ้าเปิดเพิ่มโดยยังต้องตรวจทุกอย่างเอง คนก็อาจอ่านผลงานไม่ทัน เขายังเตือนเรื่อง [[cognitive-surrender|การเชื่อตาม AI โดยไม่ตรวจ]] และย้ำว่าการใช้ agent หลายตัวไม่ได้สอนให้เราสร้างแรงจูงใจ แก้ความขัดแย้ง หรือช่วยให้เพื่อนร่วมทีมพัฒนาฝีมือ

## See also

- [[your-coding-agents-made-you-a-manager-osmani]]
- [[managing-coding-agents]]
- [[critical-thinking-when-agents-do-the-work-osmani]]
- [[cognitive-surrender]]
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
