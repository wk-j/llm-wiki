---
title: Cloudflare
type: entity
tags: [cloud, developer-tools, infrastructure, agents]
created: 2026-06-29
updated: 2026-06-29
sources: ["i don't want to use your agent — @RhysSullivan.md"]
---

# Cloudflare / Cloudflare

**Cloudflare** คือแพลตฟอร์ม cloud, edge network, security, CDN, DNS, Workers, และ developer infrastructure. ในโพสต์ [[i-dont-want-to-use-your-agent]] ของ [[rhys-sullivan|Rhys Sullivan]] Cloudflare เป็นตัวอย่าง product surface ที่กว้างมาก จน agent ที่ดีต้องมีทั้ง docs, CLI commands, และ API tools ไม่ใช่แค่ chat ใน dashboard.

## ในกรอบ BYO agent

สำหรับ [[bring-your-own-agent|BYO agent]], Cloudflare ควรทำให้ agent ภายนอกเข้าใจ product ได้ผ่าน:

- docs ที่ agent อ่านแบบเจาะ product surface ได้
- CLI commands ที่ runbook ชัด
- MCP/API tools สำหรับอ่าน config และทำ action ภายใต้ permission
- deeplink ไป dashboard เมื่อต้องตรวจของจริง

ตรงนี้ช่วย power user ใช้ agent ประจำวันของตัวเองจัดการ infra โดยไม่ต้องย้าย context เข้า dashboard chat.

## See also

- [[bring-your-own-agent]]
- [[i-dont-want-to-use-your-agent]]
- [[model-context-protocol]]
- [[coding-harness]]
