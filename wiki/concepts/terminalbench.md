---
title: TerminalBench
type: concept
tags: [benchmark, agents, terminal, evaluation]
created: 2026-04-28
updated: 2026-04-28
sources: [mario-zechner-pi-agent.md]
---

# TerminalBench / เทอร์มินัลเบนช์

**TerminalBench** เป็นเกณฑ์วัดประสิทธิภาพ (Benchmark) และระบบประเมิน (Evaluation harness) สำหรับ AI Agents ที่ทำงานผ่าน Terminal

## ลักษณะการทดสอบ

TerminalBench ไม่ได้ทดสอบแค่การเขียน code แต่ทดสอบความสามารถในการ "ใช้คอมพิวเตอร์" (Computer use) ในภาพรวม:
- **82+ Tasks**: ครอบคลุมตั้งแต่การตั้งค่าระบบ, การแก้ปัญหาเน็ตเวิร์ก, ไปจนถึงการเขียนโปรแกรมที่ซับซ้อน
- **Agent + Model**: การวัดผลจะทำเป็นคู่ (Harness + Model) เช่น `pi + Claude 4.5` เพื่อดูว่าตัวครอบ (Harness) ไหนช่วยรีดประสิทธิภาพของโมเดลออกมาได้ดีที่สุด
- **Diverse Scenarios**: มีโจทย์ตั้งแต่ระดับง่ายไปจนถึงระดับที่ต้องใช้การวางแผนหลายขั้นตอน (Multi-step planning)

## ความสำคัญ

เป็นตัวชี้วัดที่ทำให้วงการเห็นว่าความเรียบง่าย (Minimalism) อย่างใน [[terminus-agent]] หรือ [[pi-agent]] สามารถให้ผลลัพธ์ที่ดีกว่าเครื่องมือที่ซับซ้อนแต่จัดการ context ได้ไม่ดี

## ดูเพิ่ม

- [[terminus-agent]]
- [[pi-agent]]
- [[arena-ai]] — ระบบวัดผลอีกแบบที่เน้นการโหวตจากคน
