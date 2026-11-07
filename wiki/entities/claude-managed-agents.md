---
title: Claude Managed Agents
type: entity
tags: [anthropic, agent-platform, managed-service, api]
created: 2026-05-09
updated: 2026-11-07
sources: [memory-and-dreaming-self-learning-agents, components-of-agent-memory-anthropic.md]
---

# Claude Managed Agents / Claude Managed Agents API

แพลตฟอร์มของ [[anthropic|Anthropic]] ที่รัน agent ให้ลูกค้าแทนที่จะให้ลูกค้าจัด runtime เอง — เทียบกับ [[gemini-enterprise-agent-platform|Gemini Enterprise Agent Platform]] ของ [[google-cloud|Google Cloud]] (Agent Runtime) คือแนวเดียวกัน คือเอา agent ออกจาก laptop/CI ของลูกค้า ไปฝากไว้บนของผู้ผลิตโมเดล

ข้อมูลส่วนใหญ่ในหน้านี้มาจาก talk **[[memory-and-dreaming-self-learning-agents|Memory and dreaming for self-learning agents]]** (Mahes, 2026-05-09)

## ความสามารถหลัก (สถานะ พ.ค. 2026)

### Memory (public beta)

[[agent-memory-filesystem|Memory เป็น file system]] ที่ Claude จัดการเอง คุณสมบัติ:

- **Permission scopes** — read-only / read-write per memory store
- **Optimistic concurrency** — content-hash precondition กัน clobber
- **Version history + attribution** — รู้ว่า agent ตัวไหน session ไหน เขียนเมื่อไหร่
- **Standalone API** — เข้าถึง memory ได้นอก runtime (PII scan, clone ออก)

### Dreaming (research preview, เปิด 2026-05-09)

[[dreaming|Dreaming]] = batch process นอก session อ่าน transcript ข้าม agent ผลิต diff ที่ apply กับ memory store

Trigger ผ่าน console (cron) หรือ API (event) ผลลัพธ์ดู/approve ได้ก่อน apply

## ตำแหน่งใน lineup

| Surface | สถานะ |
|---|---|
| Claude API (raw) | GA |
| [[claude-code\|Claude Code]] (CLI/IDE) | GA |
| Agent SDK | GA |
| **Managed Agents API** | public beta (memory) + research preview (dreaming) |

## Customer ที่อ้างถึงใน talk

- **Rocketin** — knowledge agent ภายใน first-pass mistake ลด 90% หลังใช้ memory
- **[[harvey-ai|Harvey]]** — legal benchmark task completion rate 6× หลังเปิด dreaming

## เปรียบเทียบกับคู่แข่ง

- **[[gemini-enterprise-agent-platform|Google Cloud Agent Runtime]]** — โฟกัส 7-day long-running, Memory Bank/Profiles เป็น layer แยก, governance triad (Identity/Registry/Gateway)
- **OpenAI Managed Agents** (ถ้ามี) — ยังไม่ได้ map เข้ามาใน wiki นี้

## การใช้ในงานทดสอบ memory (พ.ย. 2026)

[[components-of-agent-memory-anthropic|บทความ The Components of Agent Memory]] ใช้ Managed Agents รันงานฐานข้อมูลของ CL-Bench 1.0 โดยเริ่ม session ใหม่ทุกคำถาม และส่งต่อโฟลเดอร์ memory ผลจึงช่วยดูว่าบทเรียนจากรอบก่อนมีประโยชน์หรือไม่ โดยไม่พึ่งประวัติใน context เดิม

บทความยังแยก [[agent-memory-hierarchy|ชั้นของ memory]] ออกจากกลไกจัดเก็บและ [[dreaming|การทบทวนเบื้องหลัง]] ข้อมูลนี้เพิ่มกรณีใช้งาน แต่ไม่ได้ยืนยันใหม่ว่าสถานะ beta/preview ในหัวข้อเดือน พ.ค. ด้านบนยังเหมือนเดิม

## See also

- [[anthropic]]
- [[claude-opus-4-7]]
- [[agent-memory-filesystem]]
- [[dreaming]]
- [[self-learning-agents]]
- [[memory-and-dreaming-self-learning-agents]]
- [[gemini-enterprise-agent-platform]]
