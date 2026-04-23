---
title: GitNexus
type: entity
tags: [developer-tools, code-intelligence, knowledge-graphs, mcp, open-source]
created: 2026-04-13
updated: 2026-04-23
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md]
---

# GitNexus

Code intelligence engine แบบ open-source ที่ทำ index codebase ให้เป็น [[code-knowledge-graphs|knowledge graphs]] และเปิดให้ AI agents เข้าถึงได้ผ่าน [[model-context-protocol|MCP]] สร้างโดย Abhigyan Patwari; มีเวอร์ชันสำหรับองค์กรผ่าน [[akon-labs]]

## สิ่งที่ทำ

สร้างกราฟที่สมบูรณ์ของ codebase — ซึ่งรวมถึง functions, classes, imports, call chains, clusters, execution flows — จากนั้นให้เครื่องมือเขียนโค้ด AI สามารถ query กราฟนั้นผ่านเครื่องมืออัจฉริยะที่คำนวณไว้ล่วงหน้า ข้ออ้างหลักคือ: [[graph-rag]] แบบดั้งเดิมต้องใช้การ query LLM หลาย hop เพื่อทำความเข้าใจโครงสร้าง; แต่ GitNexus จะคำนวณความสัมพันธ์ไว้ล่วงหน้าเพื่อให้เครื่องมือสามารถคืน context ที่สมบูรณ์ได้ในการเรียกเพียงครั้งเดียว

## รายละเอียดสำคัญ

- **License**: Open source (GitHub: abhigyanpatwari/GitNexus)
- **Languages**: รองรับ 14 ภาษาผ่าน Tree-sitter (TypeScript, Python, Java, Go, Rust, C#, etc.)
- **Database**: LadybugDB (embedded graph DB ที่รองรับ vector)
- **Interfaces**: CLI + MCP server (สำหรับงานพัฒนารายวัน), Web UI (ทำงานบนเบราว์เซอร์, ไม่ต้องมี server)
- **Editor support**: Claude Code (รองรับเต็มรูปแบบ — MCP + skills + hooks), Cursor, Codex, Windsurf, OpenCode
- **Install**: `npm install -g gitnexus` (CLI) หรือ gitnexus.vercel.app (web)
- **Privacy**: ทำงานบนเครื่องทั้งหมด (CLI) หรือในเบราว์เซอร์ทั้งหมด (web) — โค้ดไม่ออกจากเครื่อง

## การวางตำแหน่ง (Positioning)

> "เหมือน DeepWiki, แต่ลึกกว่า DeepWiki ช่วยให้คุณเข้าใจโค้ด แต่ GitNexus ให้คุณวิเคราะห์มันได้ — เพราะ knowledge graph จะติดตามทุกความสัมพันธ์ ไม่ใช่แค่คำอธิบาย"

## ดูเพิ่ม

- [[akon-labs]]
- [[code-knowledge-graphs]]
- [[model-context-protocol]]
- [[graph-rag]]
