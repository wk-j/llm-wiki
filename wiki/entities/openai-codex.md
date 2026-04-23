---
title: Codex (OpenAI)
type: entity
tags: [ai, tools, cli, coding, harness]
created: 2026-04-18
updated: 2026-04-23
sources: [alex-ker-harnesses-optimize.md]
---

# Codex (OpenAI)

Coding harness จาก OpenAI — เป็นหนึ่งใน harness หลักๆ ในตลาด เทียบเคียงได้กับ [[claude-code|Claude Code]], [[opencode|OpenCode]], Cursor, Deep Agent CLI, และ Roo Code ไฟล์นี้ถูกตั้งชื่อว่า `openai-codex` เพื่อแยกความแตกต่างจากโมเดล "OpenAI Codex" ยุค 2021 ที่เก่ากว่า

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

## ดูเพิ่ม

- [[claude-code]]
- [[opencode]]
- [[alex-ker-harnesses-optimize]]
- [[coding-harness]]
- [[progressive-disclosure]]
- [[model-context-protocol]]
