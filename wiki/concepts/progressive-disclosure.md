---
title: Progressive Disclosure
type: concept
tags: [ai, prompt-engineering, context-management, harness, mcp, skills]
created: 2026-04-18
updated: 2026-04-18
sources: [alex-ker-harnesses-optimize.md]
---

# Progressive Disclosure / เปิดเผยทีละนิด

**Progressive disclosure** คือการบอก agent ว่า "มีอะไรให้ใช้บ้าง" แต่ยังไม่โหลดเนื้อหาจริงเข้า context จนกว่าจะต้องใช้ — เป็นวิธีหลักที่ใช้รับมือกับ [[instruction-budget]] ได้โดยไม่ต้องตัดขอบเขตงาน

คำนี้ [[openai-codex|Codex]] ใช้เป็นชื่อทางการในเอกสารตัวเอง [[alex-ker|Alex Ker]] จัดเป็นหนึ่งในสามเรื่องหลักที่ทำให้ output ของ harness ไม่กลายเป็น slop

## แก่นความคิด

หลักเดียวกับที่ engineer ใช้ CLI อยู่แล้ว — รัน `--help` ก่อนเพื่อดูว่ามี subcommand อะไร พอเจออันที่อยากใช้ค่อยรัน `subcommand --help` ต่อเพื่อดู flag ไม่มีใครนั่งจำทุก flag ตั้งแต่แรก

เอาตรรกะเดียวกันมาใช้กับ agent:

- ตัว agent ต้องรู้ว่า *มี* อะไรให้ใช้ (ชื่อที่บอกตัวเองได้ + description สั้น ๆ)
- ยังไม่ต้องรู้ *รายละเอียด* จนกว่าจะเจองานที่ต้องใช้จริง
- ถึงตอนนั้นค่อยดึง body เต็มเข้ามา

ข้อดีคือ context window ยังเหลือที่ไว้ให้ reasoning ไม่ถูก reference document กินจนหมด

## เอาไปใช้ได้สามที่

### 1. CLI

ที่ได้ผลที่สุดคือ **CLI ที่ตัว model ไม่เคยเห็นตอน train** — tool ภายในบริษัทที่ห่อ API ของทีมตัวเอง ไม่มี training data ให้ model เดาได้เลย

วิธี:
- เขียนใน CLAUDE.md แค่บรรทัดเดียว เช่น *"use uv for Python package management, run uv --help to discover subcommands before assuming syntax"*
- ตัว agent ไปรัน `mycli --help` หา subcommand เอง
- แล้วรัน `mycli deploy --help` ต่อเพื่อดู flag เฉพาะ
- Context ไม่ต้องแบก reference เต็มไว้ตั้งแต่แรก

`kubectl` กับ `gh` ไม่ใช่ test case ที่ดี เพราะ model เจอ tool พวกนี้ใน training data อยู่แล้ว test case จริงคือ tool ที่ไม่มีใครนอกบริษัทคุณเคยใช้

### 2. Skills

วงการ harness ลงเอยที่จุดเดียวกันหมด — [[claude-code|Claude Code]], [[openai-codex|Codex]], [[opencode|OpenCode]] ทำแบบเดียวกัน:

- พอ session เริ่ม โหลดแค่ **ชื่อ + description** ของแต่ละ skill
- ตัว agent เลือกเองว่า skill ไหนเข้ากับงานตอนนี้
- เจอแล้วค่อยโหลด `SKILL.md` ทั้งไฟล์
- Skill ยังชี้ต่อไป reference file หรือ script ย่อยได้อีก — ก็โหลดตอนต้องใช้เหมือนกัน

สิ่งที่ engineer ต้องทำให้ดี:
- Description **ต้องชัดและเจาะจง** — ตัว agent เลือก skill จาก description อย่างเดียว ไม่ได้อ่าน body
- แยก instruction ย่อย ๆ เป็น skill ต่างหาก อย่ายัดเข้า CLAUDE.md หลัก
- ตั้งชื่อไฟล์ให้บอกตัวเองได้ว่าเกี่ยวกับอะไร

### 3. MCP tools

ตรงนี้ harness ต่างกันชัด:

| Harness | กลยุทธ์ |
|---|---|
| [[claude-code\|Claude Code]] | Tool-search index ตอน startup → ดึง schema มาตอน search เจอ (context ลด ~85% ตามที่ Anthropic บอก) |
| [[openai-codex\|Codex]] | โหลด MCP tool definition ทั้งหมดตั้งแต่ startup |
| [[opencode\|OpenCode]] | โหลด MCP tool definition ทั้งหมดตั้งแต่ startup (docs เตือนว่าต้อง limit จำนวน server) |

ถ้า harness ไม่จัดการให้ ก็ต้องจัดการเอง:

- เลือก MCP server ให้เหมาะกับงานแต่ละ project อย่าต่อหมดทุกตัว
- เขียน tool description ให้**เฉพาะเจาะจงและมี keyword เยอะ** — เวลา search-based discovery ทำงานจะได้เจอ
- ปลด MCP server ที่ไม่ใช้ออกจาก session — ประหยัดทั้ง context และ inference token

## เหตุผลเบื้องหลัง

ตัว agent ไม่ได้ฉลาดขึ้นเพราะมี context เยอะขึ้น — กลับกัน [[context-rot]] กับ [[instruction-budget]] ทำให้ performance แย่ลงพอข้อมูลท่วมเกิน Progressive disclosure ยอมแลก latency นิดหน่อย (ตัว agent ต้องเดิน 2–3 step ไปค้นเอง) แลกกับ attention ที่จดจ่อตรงที่ควรจด — คุ้ม

## See also

- [[instruction-budget]]
- [[context-rot]]
- [[coding-harness]]
- [[alex-ker-harnesses-optimize]]
- [[claude-code]]
- [[openai-codex]]
- [[opencode]]
- [[model-context-protocol]]
- [[claude-code-session-management]]
