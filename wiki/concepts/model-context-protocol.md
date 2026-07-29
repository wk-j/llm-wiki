---
title: Model Context Protocol (MCP)
type: concept
tags: [mcp, ai-agents, developer-tools, protocols]
created: 2026-04-13
updated: 2026-07-29
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md, "i don't want to use your agent — @RhysSullivan.md", bringing-mcp-2026-07-28-to-claude.md]
---

# Model Context Protocol (MCP) / โปรโตคอลเชื่อม AI กับเครื่องมือ

MCP เป็น protocol แบบเปิดสำหรับเชื่อม AI agent เข้ากับเครื่องมือ แหล่งข้อมูล และบริการภายนอก. มันกำหนด interface กลาง เพื่อให้ server ที่สร้างครั้งเดียวใช้กับ agent ที่รองรับ MCP ได้หลายตัว เช่น Claude Code, Cursor, Codex, Windsurf และ OpenCode.

## การทำงาน

MCP server จะเปิดเผย:

- **Tools** — ฟังก์ชันที่ agent เรียกใช้ได้ เช่น search, analyze, rename
- **Resources** — ข้อมูลที่ agent อ่านได้ เช่น schema หรือ statistics
- **Prompts** — workflow template สำหรับงานที่เกิดซ้ำ

server สื่อสารผ่าน stdio สำหรับเครื่องมือในเครื่อง หรือผ่าน HTTP สำหรับ server ระยะไกล. agent ค้นหาความสามารถที่มี แล้วเรียกใช้เมื่อจำเป็น.

**ได้อะไร:** agent ไม่ต้องรู้ implementation ภายในของทุกระบบ. มันคุยผ่าน protocol เดียว แล้ว server เป็นคนแปลงไปหา API, database หรือ CLI ของจริง.

## รุ่น 2026-07-28: core เบาลง ส่วน state แยกออกไป

ประกาศ [[bringing-mcp-2026-07-28-to-claude|Bringing MCP 2026-07-28 to Claude]] บอกว่า MCP รุ่นที่ห้าเปลี่ยน core จาก protocol แบบ bidirectional ที่อิง session state ไปเป็น request/response. server จึงรับ request บน serverless หรือ edge worker ตัวใดก็ได้ง่ายขึ้น ไม่ต้องผูกทุกอย่างกับ connection เดิม.

แต่ “stateless core” ไม่ได้แปลว่าระบบจริงไม่มี state. งานบางชนิดยังต้องจำ:

- UI แบบโต้ตอบต้องจำว่าผู้ใช้กำลังดูหรือแก้อะไร
- งานที่รันนานต้องมี `taskId`, progress และผลลัพธ์ที่กลับมาตามได้
- auth ต้องจำ identity, consent และ policy

รุ่นนี้จึงแยกความสามารถพวกนั้นไปอยู่ใน [[mcp-extensions|MCP Extensions]]. MCP Apps ดูแล interactive UI. MCP Tasks ดูแลงาน async ผ่าน durable handle. auth extensions เติม flow สำหรับ machine-to-machine และ enterprise identity.

**ผลคือ:** stateless core ลดภาระ session management แต่ไม่ได้ลบ state. มันย้าย state ไปอยู่ใน primitive ที่ตั้งใจรับผิดชอบเรื่องนั้น.

## การรองรับไม่ได้มาเป็นก้อนเดียว

Extension เป็น opt-in. client กับ server ต้องประกาศว่ารองรับ extension เดียวกันก่อนใช้. เพราะงั้นคำว่า “รองรับ MCP 2026-07-28” ยังไม่พอจะบอกว่า Apps, Tasks หรือ enterprise auth ใช้ได้ครบ.

ตัวอย่าง: server อาจส่ง MCP App ให้ Claude ได้ แต่ต้องเตรียม text fallback สำหรับ client ที่ไม่มี UI extension. งานแบบ Tasks ก็ต้องตรวจว่าอีกฝั่งประกาศ capability ก่อนคืน `taskId`.

**ได้อะไร:** ecosystem ค่อยๆ เพิ่มความสามารถได้โดย client รุ่นเก่ายังใช้ core ต่อ แต่ผู้พัฒนาต้องเช็ก support matrix ของ surface จริง ไม่ใช่ดูแค่ protocol version.

## ความสำคัญ

ถ้าไม่มี MCP การรวมเครื่องมือแต่ละครั้งต้องสร้าง custom adapter แยกตาม editor หรือ agent. เมื่อมี MCP เครื่องมืออย่าง [[gitnexus|GitNexus]] ทำ server ครั้งเดียว แล้วเปิดให้ agent ที่เข้ากันได้เรียกใช้.

**ได้อะไร:** ผู้สร้างเครื่องมือไม่ต้องวิ่งตามทุก agent client และผู้ใช้ย้าย product primitive เดิมข้าม harness ได้ง่ายขึ้น.

## Product expertise เป็น MCP

[[rhys-sullivan|Rhys Sullivan]] เพิ่มมุม product-side ใน [[i-dont-want-to-use-your-agent]]: บริษัทที่มี in-app agent ไม่ควรขังความรู้ของ product ไว้ใน chat UI อย่างเดียว. ถ้าเปิดความรู้เดียวกันเป็น MCP/API/CLI และ skills, power user ก็เอา [[bring-your-own-agent|agent ของตัวเอง]] มาใช้กับ product ได้.

ตัวอย่าง: [[cloudflare|Cloudflare]] เปิด tool สำหรับอ่าน config และรัน CLI, [[posthog|PostHog]] เปิด query tools กับ deeplink ไป dashboard, [[linear|Linear]] เปิด issue/project tools. MCP ทำให้ agent หลายค่ายใช้ product primitive เดียวกันได้ แทนที่บริษัทต้องสร้าง adapter แยกให้ทุก agent.

**ได้อะไร:** MCP ไม่ใช่แค่ integration protocol. มันเป็นวิธีแปลง product expertise ให้พกพาได้ระหว่าง agent.

## ตัวอย่าง: การรวม GitNexus MCP

[[gitnexus|GitNexus]] เปิดเครื่องมือ 16 อย่างผ่าน MCP รวมถึง `query`, `context`, `impact`, `detect_changes`, `rename` และ `cypher`. มันยังให้ resource URI สำหรับ metadata ของ repo และ prompt สำหรับ workflow. Claude Code ต่อได้ลึกขึ้นด้วย hooks ที่เติม graph context ก่อนเรียก tool และ re-index หลัง commit.

**ผลคือ:** MCP ทำหน้าที่เป็นฐานร่วม ส่วนความสามารถเฉพาะ client ยังวางเพิ่มรอบ protocol ได้.

## ดูเพิ่มเติม

- [[bringing-mcp-2026-07-28-to-claude]]
- [[mcp-extensions]]
- [[gitnexus]]
- [[code-knowledge-graphs]]
- [[bring-your-own-agent]]
- [[i-dont-want-to-use-your-agent]]
