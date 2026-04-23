---
title: Model Context Protocol (MCP)
type: concept
tags: [mcp, ai-agents, developer-tools, protocols]
created: 2026-04-13
updated: 2026-04-23
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md]
---

# Model Context Protocol (MCP)

เป็น protocol แบบเปิดสำหรับเชื่อมต่อ AI agents เข้ากับเครื่องมือ, แหล่งข้อมูล, และบริการภายนอก MCP มี interface ที่เป็นมาตรฐาน เพื่อให้เครื่องมือที่สร้างขึ้นครั้งเดียวสามารถใช้งานได้กับ AI agent ใดๆ ที่เข้ากันได้ — เช่น Claude Code, Cursor, Codex, Windsurf, OpenCode, และอื่นๆ

## การทำงาน

MCP server จะเปิดเผย:

-   **Tools** — ฟังก์ชันที่ agent สามารถเรียกใช้ได้ (เช่น search, analyze, rename)
-   **Resources** — ข้อมูลที่ agent สามารถเข้าถึงเพื่ออ่านได้ (เช่น schema definitions, statistics)
-   **Prompts** — workflow templates สำหรับงานทั่วไป

เซิร์ฟเวอร์สื่อสารผ่าน stdio (สำหรับเครื่องมือ CLI ในเครื่อง) หรือ HTTP AI agent จะค้นพบเครื่องมือที่มีอยู่และเรียกใช้ตามความจำเป็นในระหว่างกระบวนการ reasoning

## ความสำคัญ

หากไม่มี MCP, การรวมเครื่องมือทุกครั้งจะเป็นการสร้าง custom adapter สำหรับแต่ละ editor/agent แต่ด้วย MCP, เครื่องมืออย่าง [[gitnexus]] สามารถ implement server เพียงครั้งเดียวและทำงานได้กับ agent ทั้งหมดที่เข้ากันได้ ซึ่งสร้าง ecosystem ที่นักพัฒนาเครื่องมือสร้างเพียงครั้งเดียว และนักพัฒนา agent สามารถนำไปใช้ได้อย่างอิสระ

## ตัวอย่าง: การรวม GitNexus MCP

[[gitnexus]] เปิดเผยเครื่องมือ 16 อย่างผ่าน MCP รวมถึง `query`, `context`, `impact`, `detect_changes`, `rename`, และ `cypher` นอกจากนี้ยังให้ resource URIs สำหรับ metadata ของ repo และ prompts สำหรับ workflow ที่มีคำแนะนำ Claude Code มีการรวมที่ลึกที่สุดด้วย hooks เพิ่มเติม (PreToolUse/PostToolUse) ที่เพิ่มประสิทธิภาพการค้นหาด้วย graph context และทำการ re-index อัตโนมัติหลังจากการ commit

## ดูเพิ่มเติม

- [[gitnexus]]
- [[code-knowledge-graphs]]
