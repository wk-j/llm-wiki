---
title: HumanLayer
type: entity
tags: [ai, companies, harness, tools, prompt-engineering]
created: 2026-04-18
updated: 2026-05-10
sources: [alex-ker-harnesses-optimize.md, Agent Harness Engineering.md]
---

# HumanLayer

บริษัทที่สร้าง agent harness แบบ open-source — เป็นหนึ่งในสาม harness ที่ [[alex-ker|Alex Ker]] อ้างถึงว่าเป็นชุดเครื่องมือที่เขาใช้งานอยู่ ควบคู่ไปกับ Roo Code และ DeepAgent CLI. เว็บไซต์: [humanlayer.dev](https://www.humanlayer.dev/)

## เหตุผลที่ปรากฏใน wiki นี้

HumanLayer เป็นแหล่งที่มาของสองแนวคิดที่ถูกพูดถึงในวงการ harness-engineering:

- **[[instruction-budget|The "dumb zone"]]** — [[alex-ker|Alex Ker]] อ้างถึง Kyle (จาก HumanLayer) สำหรับข้อสังเกตที่ว่า LLM ที่มีความสามารถในการคิดระดับ frontier สามารถทำตามคำสั่งได้เพียง "ไม่กี่ร้อย" คำสั่งเท่านั้น ก่อนที่ความสนใจของมันจะกระจายออกไปและเริ่มพลาดคำสั่งที่เกี่ยวข้องท่ามกลางความฟุ้งเฟ้อของข้อมูล อ้างอิงจากบทความ: *"skill-issue-harness-engineering-for-coding-agents"* บน humanlayer.dev
- **R.P.I. framework** — `Research` → `Plan` → `Implement` แต่ละ prompt ควรทำหน้าที่เพียงอย่างใดอย่างหนึ่งจากสามอย่างนี้ ดูส่วน R.P.I. ใน [[coding-harness]]

ปัจจุบัน ทั้งสองแนวคิดนี้ได้กลายเป็นคำศัพท์มาตรฐานในโพสต์ที่เกี่ยวกับการปรับแต่ง harness

## ตำแหน่งในภูมิทัศน์ของ Harness

การสร้างแบรนด์ของ HumanLayer เองมองว่าการเลือก harness เป็น *skill issue* — harness ที่คุณยึดมั่นและปรับปรุงอยู่เสมอมีความสำคัญมากกว่าการเลือก harness ที่ดีที่สุดในนาม ซึ่งสอดคล้องกับข้อสรุปของ Alex Ker ที่ว่า "ให้ยึดมั่นกับ harness ตัวเดียว"

[[agent-harness-engineering]] อ้าง HumanLayer ในฐานะเสียงสำคัญที่ย้ำว่า agent failure จำนวนมากเป็น **configuration problem** มากกว่า model problem. ถ้า agent ทำพลาด คำถามแรกควรเป็น "harness ต้องเปลี่ยนอะไร" เช่น prompt, hook, permission, test loop, หรือ reviewer agent

## ดูเพิ่ม

- [[alex-ker]]
- [[alex-ker-harnesses-optimize]]
- [[coding-harness]]
- [[agent-harness-engineering]]
- [[instruction-budget]]
