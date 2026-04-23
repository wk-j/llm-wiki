---
title: Gemini Enterprise Agent Platform
type: entity
tags: [product, agent-platform, google-cloud, long-running-agents]
created: 2026-04-23
updated: 2026-04-23
sources: [google-cloud-long-running-agent-patterns.md]
---

# Gemini Enterprise Agent Platform / แพลตฟอร์มเอเจนต์สำหรับองค์กร

เป็นแพลตฟอร์ม managed ของ [[google-cloud|Google Cloud]] สำหรับสร้างและดูแล AI agent ซึ่งเปิดตัวเวอร์ชันสำหรับ [[long-running-agents|agent ที่ทำงานนานๆ]] ในงาน **Cloud Next '26** ตัวแพลตฟอร์มนี้เป็นหัวใจหลักในสาสน์ของ Google ที่ว่า agent workload ต้องการ infrastructure ที่ดี ไม่ใช่แค่ model ที่เก่ง

## ส่วนประกอบต่างๆ ที่ถูกอ้างอิงใน Wiki

- **Agent Runtime** — สภาพแวดล้อมสำหรับรัน agent; สามารถคงสถานะ (persistent state) ได้นานสูงสุด **7 วัน**; มี sandboxed filesystem และ bash; กลับมาทำงานต่อ (resume) ได้ในเวลาไม่ถึงวินาที (sub-second cold start); ไม่ใช้ compute เลยระหว่างที่พักการทำงาน (paused)
- **Agent Development Kit (ADK)** — เฟรมเวิร์กสำหรับสร้าง agent; มี `google.adk.Agent`, `google.adk.ToolContext`; ใช้ declarative workflow แบบ graph-based สำหรับการจัดระเบียบ coordinator/worker
- **Mission Control** — หน้าจอ UI สำหรับผู้ดูแล (operator); มี inbox ที่จัดกลุ่มสัญญาณต่างๆ เป็น "Needs your input" / "Errors" / "Completed"
- **Memory Bank** — หน่วยความจำระยะยาว (long-term memory) ที่คัดกรองแบบไดนามิก จัดระเบียบตามหัวข้อ (topic-organized)
- **Memory Profiles** — หน่วยความจำขณะทำงาน (working memory) ที่มีความหน่วงต่ำ (low-latency) สำหรับเก็บรายละเอียดที่ต้องการความแม่นยำสูง
- **Agent Identity** — ตัวตนของ agent แต่ละตัวในรูปแบบ cryptographic เหมือน service account; ใช้กำหนดขอบเขตการเข้าถึง memory และ tool
- **Agent Registry** — ระบบ service discovery สำหรับ agent; คอยติดตาม agent ที่ทำงานอยู่, เวอร์ชันของ prompt และ code, และสถานะการทำงาน
- **Agent Gateway** — ทำหน้าที่เหมือน API Gateway สำหรับ LLM โดยจะอยู่ระหว่าง agent กับ memory/tools ของมัน; เป็นที่สำหรับกำหนด policy จากภายนอก (out-of-model enforcement) ซึ่งเป็นแนวทางเดียวกับหลักการ [[agent-runtime-untrusted|APTS-SC-020]]
- **Agent Observability** — ระบบ monitoring สำหรับ agent แต่ละตัวใน deployment แบบ fleet
- **Batch and Event-Driven Agents** — รูปแบบ agent ที่ทำงานในเบื้องหลัง (ambient agent); มี connector ต่อตรงกับตาราง BigQuery และ Pub/Sub stream
- **Bring Your Own Container** — สามารถใช้ container ของตัวเองสำหรับ agent แต่ละตัว (per-specialist containers) เพื่อทำ CI/CD และแยกส่วนการทำงาน (isolation) ทำให้ deploy ที่ไม่ดี ไม่กระทบ agent ทั้งฝูง

## การวางตำแหน่ง (Positioning)

สถาปัตยกรรมหลักของแพลตฟอร์มนี้คือ **agent ควรถูกควบคุมดูแลเหมือน microservices**: มี cryptographic identity, service registry, การบังคับใช้ policy ผ่าน API gateway, และ observability สำหรับแต่ละ service แนวคิดนี้สะท้อนหลักการของ OWASP APTS ที่ว่าเราควร [[agent-runtime-untrusted|ปฏิบัติกับ agent runtime เหมือนเป็นสิ่งที่ไม่น่าเชื่อถือ (untrusted)]] — policy จะอยู่นอก model, สามารถตรวจสอบได้, และเปลี่ยนแปลงได้โดยไม่ต้อง deploy agent ใหม่ทั้งหมด

## ดูเพิ่ม

- [[google-cloud]]
- [[long-running-agents]]
- [[google-cloud-long-running-agent-patterns]]
- [[agent-runtime-untrusted]]
- [[subagent-patterns]]
- [[agent-swarm]]
