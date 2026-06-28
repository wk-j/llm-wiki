---
title: Sandcastle
type: entity
tags: [ai, infrastructure, sandbox, automation]
created: 2026-04-25
updated: 2026-06-21
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md"]
---

# Sandcastle

**Type:** เครื่องมือรัน AI agent ภายใน sandbox — สร้างโดย [[matt-pocock|Matt Pocock]]

Sandcastle เปิดทางให้รัน agent (เช่น [[claude-code|Claude Code]]) **ข้างใน sandbox** เพื่อกันไม่ให้มันทำเรื่องอันตราย — เช่นเผลอลบ home directory หรือ exfiltrate environment variable ออกไปเว็บแปลก ๆ. เสียบ backend อย่าง **Docker** หรือ **Podman** เข้าไปแล้วสั่งให้ agent ทำงานในกล่องปิดได้

## บทบาทในเวิร์กโฟลว์ (พอดแคสต์ 2026-06)

Matt ทำงานส่วนใหญ่แบบ **[[afk-agents|AFK]]** ผ่าน Sandcastle:

- **Parallelize** — รันหลาย agent พร้อมกันบนเครื่องตัวเอง หรือใช้ **Vercel sandboxes** ปั๊ม remote agent ขึ้นมา แล้ว pull commit กลับเข้า workspace local
- **GitHub Actions** — Matt ผูก Sandcastle เข้ากับ GitHub Actions; ตัวอย่างคือ "agent review action" ที่รันบน PR: checkout branch → รัน review agent (เป็น prompt ที่เก็บไว้ local) → type check → ตอบกลับว่าผ่านไหม
- ใช้ GitHub issue เป็น **[[queues-over-loops|คิวงาน]]**: ติด label `agent explore` / `agent implement` ให้ agent หยิบงานไปทำเอง

> ได้อะไร: throughput ไม่ผูกกับ resource เครื่องตัวเอง และ agent ทำงานในกล่องปิด — spin up agent ไปทำอะไรสักอย่างได้เร็วมาก

## See also
- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[afk-agents]]
- [[queues-over-loops]]
- [[agent-runtime-untrusted]]
- [[coding-harness]]
- [[vercel]]
