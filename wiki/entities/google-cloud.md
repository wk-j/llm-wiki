---
title: Google Cloud
type: entity
tags: [company, cloud, google, ai-platform]
created: 2026-04-23
updated: 2026-08-16
sources: [google-cloud-long-running-agent-patterns.md, Agent Harness Engineering.md, the-new-software-lifecycle.md]
---

# Google Cloud

เป็นส่วนธุรกิจคลาวด์สำหรับองค์กรของ Google ในแวดวง LLM-agent นั้น Google Cloud ให้บริการ **[[gemini-enterprise-agent-platform]]** และเป็นผู้จัดงานประชุม **Cloud Next** ที่ใช้ประกาศการเปลี่ยนแปลงของแพลตฟอร์ม (ในงาน Cloud Next '26 ได้มีการเปิดตัว Agent Runtime ที่ทำงานได้นาน 7 วัน)

ผลิตภัณฑ์ agent-platform ของ Google Cloud นั้นแข่งขันกับ Claude Code + MCP stack ของ Anthropic และ Bedrock Agents ของ Amazon จุดขายที่ Google Cloud ชูในปี 2026 คือ **ความสามารถในการทำงานต่อเนื่องยาวนานพร้อมเครื่องมือควบคุมดูแล (governance primitives)** เช่น Agent Identity / Registry / Gateway แทนที่จะเน้นคุณภาพของ model เพียงอย่างเดียว ซึ่งสอดคล้องกับการวางตำแหน่งตัวเองในฐานะผู้ให้บริการ infrastructure ในขณะที่ Gemini ยังต้องไล่ตามคู่แข่งในด้าน coding benchmarks (จากข้อมูล ณ ปัจจุบัน [[kimi-k2-6-tech-blog|ตาราง benchmark ของ Kimi]] และ [[claude-opus-4-7]] ทั้งคู่มีคะแนนสูงกว่า Gemini 3.1 Pro ในการทดสอบด้าน coding อย่าง SWE-Bench)

## Developer advocates ที่มีใน Wiki

- **[[addy-osmani|Addy Osmani]]** — วิศวกรที่ทำงานด้าน Chrome/web-perf มายาวนาน; หนึ่งในผู้เขียนบทความ 5-patterns และผู้เขียน [[agent-harness-engineering]]
- **Shubham Saboo** — DevRel จาก Google Cloud; หนึ่งในผู้เขียนบทความ

## AI-driven SDLC และ Agents CLI

ใน [[the-new-software-lifecycle|The New Software Lifecycle]] Addy สรุป whitepaper ของ Google ที่เขาร่วมเขียนว่า AI เร่ง implementation มากกว่า phase ที่ใช้ judgement. [[ai-driven-sdlc|AI-driven SDLC]] จึงต้องขยับ spec, architecture และ verification ให้มาอยู่ใกล้ loop ของ agent มากขึ้น

บทความใช้ **Google Agents CLI** เป็นภาพของ product direction: coding agent ใน terminal สร้าง project, ทำ eval และ deploy ไป Agent Engine ผ่านคำสั่งภาษาคนชุดเดียว. MCP ใช้ต่อ tool ส่วน A2A ใช้ส่งงานระหว่าง agent. นี่เป็นคำอธิบายจากผู้ร่วมสร้าง ecosystem จึงบอกทิศทางได้ดี แต่ยังไม่พิสูจน์ว่า prototype ทุกตัวพร้อมขึ้น production โดยไม่ต้องเพิ่ม permission, governance และ observability

**ได้อะไร:** Google Cloud กำลังพยายามรวมวงจร build–eval–deploy ของ agent ให้เป็น workflow เดียวกับ coding agent แทนการแยก prototype กับ production เป็นคนละ stack

## ดูเพิ่ม

- [[gemini-enterprise-agent-platform]]
- [[google-cloud-long-running-agent-patterns]]
- [[long-running-agents]]
- [[addy-osmani]]
- [[the-new-software-lifecycle]]
- [[ai-driven-sdlc]]
