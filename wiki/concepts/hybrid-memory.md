---
title: Hybrid Memory Architecture
type: concept
tags: [agent-memory, architecture, design-pattern]
created: 2026-04-28
updated: 2026-04-28
sources: [why-karpathys-second-brain-breaks]
---

# Hybrid Memory Architecture / สถาปัตยกรรมความจำแบบผสม

แนวทางการออกแบบระบบความจำของ AI Agent ที่แบ่งโครงสร้างออกเป็นสองส่วน เพื่อให้ตอบโจทย์ทั้งการใช้งานของ "มนุษย์" และประสิทธิภาพของ "เครื่องจักร"

## โครงสร้างแบบผสม

สถาปัตยกรรมนี้แบ่งความจำออกเป็นสองชั้น (layers) ที่ทำงานร่วมกัน:

1.  **Markdown Interface (สำหรับมนุษย์):**
    - ใช้เก็บบันทึก (Notes), รายงาน (Reports), และไฟล์ระบุตัวตน (Persona files)
    - เน้นให้อ่านง่ายและแก้ไขได้ด้วยมือ (Human-readable/editable)
    - เป็นส่วนที่มนุษย์เป็นเจ้าของและใช้ควบคุมทิศทางของ Agent (Human-owned)

2.  **Structured Substrate (สำหรับเครื่องจักร):**
    - ใช้เก็บข้อเท็จจริง (Facts), เอนทิตี (Entities), ความสัมพันธ์ (Relationships), และสถานะของงาน (Task state)
    - มีข้อมูลกำกับชัดเจน เช่น เวลา (Timestamps) และคะแนนความสำคัญ ([[memory-scoring|Scoring]])
    - เน้นความเร็วในการค้นหาและความประหยัด Token (Machine-efficient)

## ผลลัพธ์ที่ได้

- **ในมุมของมนุษย์:** สบายใจเพราะสามารถตรวจสอบและแก้ไขข้อมูลหรือความเชื่อของ Agent ได้ผ่านไฟล์ Markdown ที่คุ้นเคย (เช่น Obsidian หรือ VS Code)
- **ในมุมของ Agent:** ทำงานได้แม่นยำและประหยัดค่าใช้จ่าย เพราะมีฐานข้อมูลเบื้องหลังที่ออกแบบมาเพื่อการประมวลผลของ AI โดยเฉพาะ ไม่ต้องเสียเวลาเดาจากหน้าเอกสารที่ยาวเหยียด

## See also
- [[mercury]]
- [[ctrl-alt-zaid]]
- [[selective-injection]]
