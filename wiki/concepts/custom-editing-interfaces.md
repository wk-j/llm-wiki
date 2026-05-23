---
title: Custom Editing Interfaces
type: concept
tags: [html, tools, productivity, workflow, artifacts]
created: 2026-05-09
updated: 2026-05-09
sources: [thariq-html-effectiveness.md]
---

# Custom Editing Interfaces / อินเทอร์เฟซแก้ไขเฉพาะกิจ

**Custom Editing Interfaces** (หรือ Throwaway Editors) คือการสั่งให้ AI สร้างเครื่องมือแก้ไขข้อมูลรูปแบบ HTML ขึ้นมาเพื่อใช้งานสำหรับ "งานเดียว" (Single task) โดยเฉพาะ ไม่ใช่เพื่อสร้างเป็นโปรเจกต์หรือซอฟต์แวร์ที่ใช้ถาวร

## แก่นความคิด
ในบางครั้งการอธิบายการแก้ไขข้อมูลที่ซับซ้อนผ่าน Text Box นั้นยากเกินไป (เช่น การเรียงลำดับตั๋วงาน 30 ใบ) วิธีแก้คือให้ AI สร้าง "Editor ชั่วคราว" ขึ้นมา:
- **Purpose-built**: สร้างมาเพื่อจัดการข้อมูลชุดเดียวในตอนนั้น
- **Visual Interaction**: ใช้ GUI (เช่น การลากวาง card, การกด toggle) เพื่อจัดการข้อมูล
- **Export to Prompt**: หัวใจสำคัญคือต้องมีปุ่ม "Copy as Prompt" หรือ "Copy as JSON" เพื่อเอาข้อมูลที่แก้ไขเสร็จแล้วกลับไปวางใน [[claude-code]] เพื่อให้ AI ทำงานต่อ

## ตัวอย่างการใช้งาน
- **Triage**: สร้างกระดาน Kanban ชั่วคราวเพื่อลากตั๋วงานแบ่งกลุ่ม (Now/Next/Later) แล้วส่งลำดับสุดท้ายกลับให้ AI
- **Config Editor**: สร้าง Form สำหรับแก้ไข JSON/YAML ที่ซับซ้อน มีการตรวจสอบความสัมพันธ์ (Dependencies) ระหว่างค่าต่างๆ
- **Prompt Tuning**: สร้าง Editor หน้าคู่ (Side-by-side) เพื่อลองใส่ input หลายๆ แบบดูผลลัพธ์ของ prompt แบบ real-time

## ผลคือ (Payoff)
ช่วยให้มนุษย์สามารถตัดสินใจในเรื่องที่ "ต้องใช้สายตาหรือความรู้สึก" (Visual/Taste-based decisions) ได้แม่นยำขึ้น โดยไม่ต้องเสียเวลาเขียนโค้ดสร้างเครื่องมือเอง และยังคงรักษาการควบคุม (Control) ไว้ในมือมนุษย์ได้อย่างมีประสิทธิภาพ

## ดูเพิ่ม
- [[html-artifacts]]
- [[claude-code]]
- [[thariq-html-effectiveness]]
