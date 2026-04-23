---
title: Moonshot AI
type: entity
tags: [ai, company, china, open-source, llm]
created: 2026-04-21
updated: 2026-04-23
sources: [Kimi K2.6 Tech Blog Advancing Open-Source Coding.md]
---

# Moonshot AI

บริษัท AI Lab จากประเทศจีน ผู้อยู่เบื้องหลังตระกูลโมเดล **Kimi** (Kimi.com, Kimi App, platform.kimi.ai) บริษัทจะปล่อย model weights เป็น open-source และเน้นแข่งขันในด้าน coding และ agent workload ที่ต้องทำงานระยะยาว (long-horizon) แทนที่จะแข่งด้านการให้เหตุผล (reasoning) หรือ vision โดยตรง

## ผลิตภัณฑ์และบริการ

- **[[kimi-k2-6|Kimi K2.6]]** (เม.ย. 2026) — โมเดล open-source flagship ด้าน coding; รุ่นก่อนหน้าคือ Kimi K2.5
- **Kimi.com** — consumer chat interface
- **Kimi App** — แอปพลิเคชันบนมือถือ
- **platform.kimi.ai** — API สำหรับนักพัฒนา
- **Kimi Code** (kimi.com/code) — interface สำหรับงาน coding โดยเฉพาะ
- **Kimi Agent Swarm** (kimi.com/agent-swarm) — interface สำหรับจัดการ [[agent-swarm|agent swarm]]
- **Claw Groups** — พรีวิวฟีเจอร์การทำงานร่วมกันของ agent ต่างค่าย (heterogeneous BYO-Agents); โดย K2.6 ทำหน้าที่เป็น adaptive coordinator
- **Kimi Vendor Verifier (KVV)** — เครื่องมือตรวจสอบสำหรับผู้ให้บริการ API บุคคลที่สามที่นำ model weights ของ Kimi ไปให้บริการต่อ; ใช้เป็นข้อมูลอ้างอิงในการทำซ้ำคะแนนที่เป็นทางการ

## ชุดประเมินผลภายใน

- **Kimi Code Bench** — benchmark สำหรับวัดผล coding แบบ end-to-end ภายใน
- **Kimi Design Bench** — ชุดประเมินผลการออกแบบ frontend/full-stack 4 หมวดหมู่ (Visual Input / Landing Page / Full-Stack / Creative Programming)
- **Claw Bench** — ชุดประเมินผล proactive-agent: Coding / IM ecosystem / Info research / Scheduled tasks / Memory

## การวางตำแหน่ง (Positioning)

- เป็นผู้ท้าชิงในฝั่ง open-source โดยเน้นที่ **coding + agentic** เป็นพิเศษ — ไม่ได้ชูประเด็นเรื่องการให้เหตุผลระดับ frontier หรือความสามารถด้าน vision ที่ทัดเทียมกัน
- เปรียบเทียบ benchmark กับ GPT-5.4, Claude Opus 4.6, Gemini 3.1 Pro; แต่ที่น่าสังเกตคือไม่ได้รวม Claude Opus 4.7 ไว้ในตารางเปรียบเทียบตอนเปิดตัว K2.6
- ใช้ agent stack ของตัวเองในการทำงานภายใน (ทีม marketing ทำงานผ่าน Claw Groups; งาน RL infra ops ทำโดย K2.6 agent ที่รันอัตโนมัตินาน 5 วัน)

## ดูเพิ่ม

- [[kimi-k2-6]]
- [[agent-swarm]]
- [[kimi-k2-6-tech-blog]]
