---
title: Vercel
type: entity
tags: [cloud, platform, ai-sdk, agents, sandbox]
created: 2026-10-11
updated: 2026-10-11
sources: [matt-pocock-agent-workflow.md, opencode-vs-claude-code-morph.md, andrej-karpathy-vibe-coding-to-agentic-engineering.md]
---

# Vercel / เวอร์เซล

Vercel เป็น cloud platform สำหรับ deploy เว็บ ใน wiki นี้ยังไม่มี source ไหนพูดถึง Vercel เป็นเรื่องหลัก ชื่อนี้โผล่มาในฐานะส่วนประกอบของเรื่องอื่น หน้านี้เลยรวบรวมไว้ว่าแต่ละที่ใช้ Vercel ทำอะไร

## โผล่ในบริบทไหนบ้าง

- **Chat SDK สำหรับ orchestration** — workflow ของ [[matt-pocock|Matt Pocock]] (เจ้าของคอร์ส Total TypeScript ที่หันมาทำ agent workflow) ใช้ [[sandcastle|Sandcastle]] คู่กับ Chat SDK ของ Vercel สั่ง agent ผ่าน Slack ดู [[matt-pocock-agent-workflow]]
- **Vercel AI SDK ใน OpenCode** — [[opencode|OpenCode]] (coding harness แบบ open-source) จัดการ context ผ่าน Vercel AI SDK ซึ่งทำงานต่างกันไปตาม provider และไม่มีคำสั่งแบบ `/compact` ดู [[opencode-vs-claude-code-morph]]
- **Vercel sandboxes สำหรับ agent ที่รันนอกเครื่อง** — Sandcastle เปิด remote agent หลายตัวพร้อมกันบน sandbox ของ Vercel แล้ว pull commit กลับเข้า workspace บนเครื่อง ดู [[sandcastle]] กับ [[afk-agents]]
- **ตัวอย่างงาน deploy** — [[andrej-karpathy|Andrej Karpathy]] (นักวิจัย AI ผู้ตั้งคำว่า vibe coding) ยกการตั้ง DNS กับ Vercel ด้วยมือเป็นตัวอย่างงานที่ควรสั่งด้วย prompt ได้แล้ว ดู [[andrej-karpathy-vibe-coding-to-agentic-engineering]]

ผลคือ ใน wiki นี้ Vercel อยู่ในฐานะโครงสร้างพื้นฐานรอบ agent ทั้ง SDK, sandbox และที่ deploy ยังไม่มีข้อมูลตรงจากบริษัทเอง

## See also

- [[sandcastle]]
- [[afk-agents]]
- [[opencode]]
- [[matt-pocock]]
