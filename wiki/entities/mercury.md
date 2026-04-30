---
title: Mercury
type: entity
tags: [agent-memory, open-source, infrastructure]
created: 2026-04-28
updated: 2026-04-28
sources: [why-karpathys-second-brain-breaks]
---

# Mercury / เมอร์คิวรี

ระบบโครงสร้างพื้นฐานสำหรับ Agent Memory (ความจำเอเจนต์) แบบ Open-source (MIT License) ที่ออกแบบมาเพื่อแก้ปัญหาความไม่มีประสิทธิภาพของระบบจดจำข้อมูลแบบไฟล์ Markdown ทั่วไปเมื่อนำมาใช้กับ Agent ขนาดใหญ่

## แนวคิดหลัก

Mercury ออกแบบภายใต้หลักการ **"Identity should be human-owned. Memory should be machine-efficient."** (ตัวตนเป็นของมนุษย์ ความจำเป็นของเครื่องจักร)

- **Editable Identity (ตัวตนที่แก้ไขได้):** ส่วนที่เป็น Persona (บุคลิก) และข้อมูลระบุตัวตน เปิดให้มนุษย์แก้ไขได้ผ่านไฟล์ Markdown เพื่อให้คนสามารถควบคุมทิศทางของ Agent ได้ง่าย
- **Operational Memory (ความจำสำหรับการทำงาน):** ส่วนที่เป็นความจำเชิงเทคนิค ถูกปรับแต่งให้เน้นการดึงข้อมูล (Retrieval) ที่รวดเร็วและคำนึงถึงการใช้ Token (Token-aware) เพื่อความประหยัดและแม่นยำ

## คุณสมบัติสำคัญ

- **[[selective-injection|Selective Injection]] (การเลือกฉีดความจำ):** เลือกใส่เฉพาะความจำที่จำเป็นเข้าสู่บริบท (Context) ของ AI เท่านั้น ไม่โหลดข้อมูลทั้งหน้าโดยไม่จำเป็น
- **Structured Retrieval (การดึงข้อมูลแบบโครงสร้าง):** รองรับการค้นหาข้อเท็จจริง (Facts) หรือสถานะงาน (Task state) ได้อย่างแม่นยำ
- **Scoring & Decay (การให้คะแนนและการเลือนลาง):** มีระบบให้คะแนนความจำตามความสดใหม่และความสำคัญ พร้อมระบบเก็บข้อมูลเก่าเข้าคลัง (Archiving) เพื่อไม่ให้รบกวนการทำงานปัจจุบัน

## ข้อมูลโปรเจกต์
- **Website:** [mercury.cosmicstack.org](https://mercury.cosmicstack.org/)
- **License:** MIT

## See also
- [[ctrl-alt-zaid]]
- [[selective-injection]]
- [[memory-scoring]]
- [[hybrid-memory]]
