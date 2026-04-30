---
title: Software 3.0
type: concept
tags: [ai, software-engineering, programming-paradigm, karpathy]
created: 2026-04-30
updated: 2026-04-30
sources: [Andrej Karpathy From Vibe Coding to Agentic Engineering.md]
---

# Software 3.0 / ซอฟต์แวร์ 3.0

**Software 3.0** เป็นวิวัฒนาการล่าสุดของการสร้างซอฟต์แวร์ที่เปลี่ยนจากการเขียนโค้ด (Software 1.0) หรือการเทรน model (Software 2.0) มาเป็นการ "ใช้ภาษา" เพื่อควบคุม AI ที่ทำหน้าที่เป็นคอมพิวเตอร์ที่โปรแกรมได้ (Programmable Computer)

## ประวัติและวิวัฒนาการ
- **Software 1.0**: มนุษย์เขียน "กฎ" (Code) ให้คอมพิวเตอร์ทำตามทีละขั้นตอน (Explicit Rules)
- **Software 2.0**: มนุษย์จัดเตรียม "ข้อมูล" (Data) และเป้าหมาย เพื่อให้คอมพิวเตอร์เรียนรู้ "ค่าน้ำหนัก" (Weights) เอง (เช่น Neural Networks)
- **Software 3.0**: มนุษย์ใช้ "คำสั่ง" (Prompts) ในบริบท (Context Window) เพื่อควบคุม LLM ที่เป็นระบบประมวลผลที่มีความฉลาดในตัวอยู่แล้ว

## แก่นความคิด
ใน Software 3.0 ตัว LLM เปรียบเสมือน **Interpreter** หรือระบบปฏิบัติการใหม่ โดยที่:
- **Context Window** คือคันโยก (Lever) หลักในการโปรแกรม
- **Natural Language** คือภาษาโปรแกรมใหม่ (The hottest new programming language is English)
- **Agentic Capability** คือการที่ซอฟต์แวร์สามารถปรับตัวและแก้ปัญหาหน้างานได้เองโดยไม่ต้องเขียนดักไว้ล่วงหน้าทุกกรณี

## ตัวอย่าง: Agents as the Installer
ในการลงโปรแกรมแบบเดิม (Software 1.0) เราต้องเขียน Bash Script ที่ซับซ้อนเพื่อรองรับทุก OS และจัดการ Error แต่ใน Software 3.0 เราแค่ส่งชุดคำสั่ง (Instruction) ให้ Agent แล้วมันจะ "ดูหน้างาน" บนเครื่องคอมพิวเตอร์นั้นๆ และจัดการติดตั้งให้สำเร็จด้วยตัวเอง

## Payoff / ผลคือ
- **Flexible & Adaptive**: ซอฟต์แวร์สามารถทำงานในสภาพแวดล้อมที่หลากหลายได้ดีขึ้น
- **Faster Development**: ลดเวลาในการเขียนและทดสอบรายละเอียดเล็กน้อย (Boilerplate)
- **New Capabilities**: สามารถสร้างระบบที่จัดการกับข้อมูลที่ไม่มีโครงสร้าง (Unstructured Data) ได้อย่างมีประสิทธิภาพ

## ดูเพิ่ม
- [[vibe-coding]]
- [[agentic-engineering]]
- [[andrej-karpathy]]
