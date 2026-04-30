---
title: iii (Triple I)
type: entity
tags: [software, framework, open-source, agent-infrastructure]
created: 2026-04-29
updated: 2026-04-29
sources: [the-harness-is-the-backend.md]
---

# iii (Triple I) / ไอ-ไอ-ไอ

iii เป็น Framework ระบบหลังบ้าน (Backend Engine) แบบ Open Source ที่ออกแบบมาเพื่อรองรับยุคของ AI Agent โดยเฉพาะ พัฒนาโดย [[mf-piccolo]] และทีมงาน มีแนวคิดหลักคือการยุบรวมโครงสร้างพื้นฐานของ Agent เข้าเป็นส่วนเดียวกับ Backend

## คุณสมบัติหลัก

- **[[wtf-primitives|WTF Architecture]]:** ใช้ Primitives เพียง 3 อย่าง (Worker, Trigger, Function) ในการจัดการทุกอย่าง
- **Language Agnostic:** รองรับ SDK ทั้ง TypeScript, Python, และ Rust โดยสื่อสารผ่าน JSON over WebSocket (Open Wire Protocol)
- **Agent-Ready Primitives:** ทำให้ AI Agent สามารถใช้งานระบบ Queue, State Management, และ Pub/Sub ได้เสมือนเป็นบริการหนึ่งในระบบ
- **Live Extension:** ระบบสามารถขยายตัวได้ที่ runtime (ไม่ต้อง restart) เมื่อมี Worker ใหม่เชื่อมต่อเข้ามา
- **Isolated Execution:** รองรับการสร้าง MicroVM Sandbox สำหรับรันโค้ดที่ไม่น่าไว้ใจ (untrusted code)

## ปรัชญาการออกแบบ

iii เชื่อว่า **"The Harness is the Backend"** (บังเหียนคือระบบหลังบ้าน) หมายความว่าเราไม่ควรสร้างระบบจัดการ Agent (Harness) แยกต่างหาก แต่ควรสร้าง Backend ที่มีความยืดหยุ่นพอที่จะเป็น Harness ให้กับ Agent ได้ในตัว

## See also

- [[mf-piccolo]]
- [[the-harness-is-the-backend]]
- [[wtf-primitives]]
- [[harness-engineering]]
