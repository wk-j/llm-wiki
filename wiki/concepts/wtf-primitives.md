---
title: WTF Primitives (Worker-Trigger-Function)
type: concept
tags: [architecture, backend, agent-infrastructure, iii]
created: 2026-04-29
updated: 2026-04-29
sources: [the-harness-is-the-backend.md]
---

# WTF Primitives (Worker-Trigger-Function) / ชุดคำสั่งพื้นฐาน WTF

WTF Primitives เป็นกรอบความคิดเชิงสถาปัตยกรรม (Architectural Framework) ที่ยุบหมวดหมู่ของระบบหลังบ้าน (Backend) ที่ซับซ้อนให้เหลือเพียง 3 องค์ประกอบพื้นฐานที่ทำงานร่วมกันได้อย่างเป็นสากล แนวคิดนี้เป็นรากฐานของโปรเจกต์ [[iii-triple-i]]

## องค์ประกอบ 3 อย่าง

1.  **Function (ฟังก์ชัน):**
    - คือ "หน่วยของงาน" (Unit of Work) ที่มีชื่อเรียก (Identifier) ที่แน่นอน (เช่น `orders::validate`)
    - รับ Input และคืนค่า Output
    - สามารถเขียนด้วยภาษาใดก็ได้ และรันอยู่ที่ไหนก็ได้

2.  **Trigger (ทริกเกอร์):**
    - คือ "ตัวกระตุ้น" ที่ทำให้ Function ทำงาน
    - มีความหลากหลาย: Direct Call, HTTP Endpoint, Cron Job, Queue Subscription, หรือ State Change
    - เป็นแบบ Declarative (ประกาศไว้ว่า "รันฟังก์ชันนี้เมื่อเกิดสิ่งนี้ขึ้น") โดยระบบจะจัดการเรื่อง routing และ delivery ให้เอง

3.  **Worker (เวิร์กเกอร์):**
    - คือ "กระบวนการ" (Process) ใด ๆ ที่เชื่อมต่อกับระบบเพื่อลงทะเบียน Function และ Trigger
    - ไม่ว่าจะเป็น API Service (TS), ML Pipeline (Python), Microservice (Rust), หรือแม้แต่ **AI Agent** ทั้งหมดล้วนเป็น Worker ในระดับที่เท่าเทียมกัน

## ทำไมต้อง WTF?

ในสถาปัตยกรรมแบบเดิม (Traditional Architecture) เราแยกแยะหมวดหมู่ของเครื่องมือ (Categories of Products) ออกจากกัน เช่น Queue, Stream, Sandbox, Agent Orchestrator ซึ่งแต่ละอย่างมีวิธีเชื่อมต่อและ Lifecycle ที่ต่างกัน

**WTF Collapse (การยุบหมวดหมู่):**
แทนที่จะต้องเรียนรู้วิธีใช้เครื่องมือหลายสิบประเภท WTF เปลี่ยนคำถามเป็น "จะเพิ่มความสามารถนี้ได้อย่างไร?" คำตอบเดียวคือ **"Add a Worker"** (เพิ่ม Worker ใหม่ที่ลงทะเบียน Function และ Trigger ที่ต้องการ)

## ประโยชน์ต่อ AI Agent

- **Seamless Integration:** Agent ไม่ได้มองว่า Backend เป็น "คนอื่น" ที่ต้องเรียกผ่าน API แต่ Agent คือส่วนหนึ่งของ Backend ที่สามารถใช้ Queue หรือจัดการ State ได้โดยตรง
- **Agentic Sandboxing:** Agent สามารถสร้าง "Sandbox Worker" (เช่น MicroVM) ขึ้นมาได้เองแบบ recursive เพื่อรันโค้ดที่อันตรายได้อย่างปลอดภัย
- **Unified Observability:** เมื่อทุกอย่างใช้ Primitives เดียวกัน การทำ Distributed Tracing จะครอบคลุมตั้งแต่ตัว Agent ไปจนถึงงานใน Queue และ Database write ใน trace เดียวกัน (End-to-end tracing)

## See also

- [[iii-triple-i]]
- [[the-harness-is-the-backend]]
- [[harness-engineering]]
- [[ai-orchestrator]]
