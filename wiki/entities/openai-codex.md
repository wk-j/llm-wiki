---
title: Codex (OpenAI)
type: entity
tags: [ai, tools, cli, coding, harness]
created: 2026-04-18
updated: 2026-06-28
sources: [alex-ker-harnesses-optimize.md, Piyalitt Ittichaiwong - GPT-5.5 Launch.md, "รู้จักกับ Loop Engineering — mikelopster transcript"]
---

# Codex (OpenAI)

Coding harness จาก [[openai|OpenAI]] — เป็นหนึ่งใน harness หลักๆ ในตลาด เทียบเคียงได้กับ [[claude-code|Claude Code]], [[opencode|OpenCode]], Cursor, Deep Agent CLI, และ Roo Code ไฟล์นี้ถูกตั้งชื่อว่า `openai-codex` เพื่อแยกความแตกต่างจากโมเดล "OpenAI Codex" ยุค 2021 ที่เก่ากว่า

## ตำแหน่งในภูมิทัศน์ของ Harness (ตาม Alex Ker, 18 เม.ย. 2026)

### จุดที่เหมือนกับเจ้าอื่น

- **Skills progressive disclosure:** Codex, Claude Code, และ OpenCode ต่างก็ใช้รูปแบบเดียวกัน — คือจะโหลดแค่ชื่อและคำอธิบายของ skill ตอนเริ่มต้น; ส่วน `SKILL.md` ทั้งหมดจะถูกโหลดเมื่อต้องการใช้งาน เอกสารของ Codex เอง **เรียกสิ่งนี้อย่างชัดเจนว่า "progressive disclosure"** และยกให้เป็นหัวใจหลักในการทำให้ context สะอาด

### จุดที่แตกต่าง — การจัดการ MCP tool

| Harness | กลยุทธ์การโหลด MCP tool |
|---|---|
| [[claude-code\|Claude Code]] | โหลด tool-search index ตอนเริ่มต้น; ดึง schema เมื่อต้องการใช้งาน (~85% context reduction ตามที่ Anthropic รายงาน) |
| **Codex** | โหลด definition ของ MCP tool ที่ตั้งค่าไว้ทั้งหมดเข้ามาใน context ตอนเริ่ม session |
| [[opencode\|OpenCode]] | โหลด definition ของ MCP tool ที่ตั้งค่าไว้ทั้งหมดเข้ามาใน context ตอนเริ่ม session (เอกสารเตือนให้ผู้ใช้จำกัดจำนวน server) |

ดังนั้น ผู้ใช้ Codex ที่ต้องพึ่งพา MCP server จำนวนมากจะเสีย "ภาษี context" ตอนเริ่มต้นมากกว่าผู้ใช้ Claude Code — ผลในทางปฏิบัติคือ: ควรเลือกเชื่อมต่อ MCP server อย่างระมัดระวังในแต่ละโปรเจกต์บน Codex

## การใช้งานภายใน OpenAI (จาก GPT-5.5 launch, 2026-04-23)

- 85%+ ของพนักงาน OpenAI ใช้ Codex **ทุกสัปดาห์** — ครอบคลุม eng / finance / comms / marketing / data science / PM
- ตัวอย่าง: ฝ่ายการเงินตรวจ K-1 จำนวน 24,771 ฟอร์ม / 71,637 หน้า เสร็จเร็วขึ้น 2 สัปดาห์จากปีก่อน
- Codex + [[gpt-5-5|GPT-5.5]] เขียน custom heuristic algorithm แบ่งและกระจาย production traffic → เพิ่มความเร็ว token generation > 20% (โมเดลช่วยพัฒนา infra ที่ serve ตัวเอง)
- Plan coverage กว้างขึ้น: Plus / Pro / Business / Enterprise / **Edu** / **Go** พร้อม context window 400K

## Schedule และ goal-oriented work

[[mikelopster]] ใน [[mikelopster-loop-engineering|คลิป Loop Engineering]] วาง Codex ไว้เป็นอีก surface ที่มี primitive แนว loop ถึงแม้ในคลิปจะบอกว่าไม่ได้มี `/loop` แบบเดียวกับ Claude Code. เขาชี้ไปที่ schedule / scheduled task และแนว `/goal`: ผู้ใช้ระบุเป้าหมาย แล้ว agent แตกงาน, สร้าง checklist/subagent, และ verify ไปเรื่อย ๆ จนถึงเงื่อนไขจบ.

มุมนี้ทำให้ Codex อยู่ในกลุ่มเดียวกับ [[claude-code|Claude Code]] ในฐานะ coding harness ที่เริ่มรองรับ workflow แบบ [[loop-engineering|loop engineering]]. แต่ข้อจำกัดเหมือนกัน: ถ้า feedback gate ไม่ชัด หรือ output ยังต้องให้คนตัดสินทุกครั้ง ก็จะกลายเป็น [[orchestration-tax|orchestration tax]] มากกว่าการเพิ่ม throughput.

## ดูเพิ่ม

- [[claude-code]]
- [[opencode]]
- [[openai]]
- [[gpt-5-5]]
- [[alex-ker-harnesses-optimize]]
- [[coding-harness]]
- [[progressive-disclosure]]
- [[model-context-protocol]]
- [[loop-engineering]]
- [[mikelopster-loop-engineering]]
