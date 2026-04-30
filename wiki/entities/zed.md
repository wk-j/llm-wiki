---
title: Zed
type: entity
tags: [editor, rust, ai, collaboration]
created: 2026-04-29
updated: 2026-04-29
sources: [zed-is-1-0.md]
---

# Zed / เซด

**Zed** คือ Code Editor ประสิทธิภาพสูงที่พัฒนาโดยทีมผู้สร้าง [[atom]] และ [[vscode|Electron]] (Nathan Sobo และคณะ) โดยมีเป้าหมายเพื่อสร้างเครื่องมือที่เร็วที่สุดสำหรับการเขียนโค้ดและรองรับการทำงานร่วมกับ AI อย่างเต็มรูปแบบ

## แก่นความคิด (Core Philosophy)

### ประสิทธิภาพระดับวิดีโอเกม
Zed ปฏิเสธแนวทางการใช้ [[electron]] หรือ Web technology แบบ Editor ทั่วไป แต่เลือกสร้างด้วยภาษา [[rust]] และใช้โครงสร้างแบบวิดีโอเกมที่ส่งข้อมูลตรงไปยัง GPU ผ่าน framework ที่ชื่อว่า [[gpui]] ทำให้การตอบสนอง (latency) ต่ำมาก และใช้ทรัพยากรเครื่องน้อย

### AI-Native
ต่างจาก Editor อื่นที่นำ AI มา "แปะ" เพิ่มทีหลัง Zed ออกแบบ primitives ของตัวเองให้รองรับ AI ตั้งแต่แรก:
- **[[agent-client-protocol|Agent Client Protocol (ACP)]]**: มาตรฐานกลางที่ทำให้ผู้ใช้เลือกใช้ AI Agent ตัวไหนก็ได้ใน Zed เช่น [[claude]], Codex, หรือ [[opencode]]
- **Parallel Agents**: ความสามารถในการรัน Agent หลายตัวพร้อมกันเพื่อแก้ปัญหาที่ซับซ้อน
- **Edit Prediction**: การทำนายและแนะนำการแก้ไขโค้ดในระดับ keystroke

### การทำงานร่วมกันยุคใหม่
Zed มองว่าการ collaboration ไม่ใช่แค่คนคุยกับคน แต่คือ "คน + AI Agent" ทำงานในพื้นที่เดียวกัน (Shared Space) โดยใช้เทคโนโลยี [[deltadb]] เพื่อจัดการสถานะของโค้ดที่เปลี่ยนแปลงตลอดเวลา

## ประวัติและสถานะ
- **1.0 Release**: ประกาศเข้าสู่สถานะ 1.0 เมื่อวันที่ 29 เมษายน 2026
- **Open Source**: เปิด code เป็น open source ตั้งแต่ช่วงต้นปี 2024
- **Platforms**: รองรับ macOS, Windows และ Linux

## ดูเพิ่ม
- [[zed-industries]] — บริษัทผู้พัฒนา
- [[deltadb]] — ระบบ Sync ข้อมูลเบื้องหลัง
- [[gpui]] — UI Framework ของ Zed
