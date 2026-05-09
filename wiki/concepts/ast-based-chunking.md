---
title: AST-Based Chunking
type: concept
tags: [parsing, code-analysis, retrieval, rag]
created: 2026-05-08
updated: 2026-05-08
sources: [why-im-against-claude-codes-grep-only-retrieval.md]
---

# AST-Based Chunking / การแบ่งข้อมูลตามโครงสร้างโค้ด

AST-Based Chunking คือเทคนิคการแบ่ง code ออกเป็นส่วนย่อยๆ (chunks) เพื่อนำไปทำ indexing โดยยึดตาม **Abstract Syntax Tree (AST)** หรือโครงสร้างทางภาษาของ code นั้นๆ แทนการแบ่งตามจำนวนบรรทัดแบบดั้งเดิม

## ทำไมต้องแบ่งตาม AST?
การแบ่ง code แบบปกติ (เช่น ทุกๆ 50 บรรทัด) มักจะทำให้เนื้อหาขาดตอน เช่น ฟังก์ชันหนึ่งอาจจะโดนตัดแบ่งครึ่ง ทำให้ AI เข้าใจผิดพลาด แต่ AST-Based Chunking จะเข้าใจว่าส่วนไหนคือฟังก์ชัน ส่วนไหนคือคลาส:
- **รักษาบริบท:** เก็บฟังก์ชันหรือคลาสไว้เป็นก้อนเดียวกันเสมอ
- **คุณภาพของ Context:** เมื่อ Agent ดึงข้อมูลมาใช้งาน จะได้ code ที่สมบูรณ์ในตัวเอง (self-contained)
- **ประหยัด Token:** ดึงมาเฉพาะฟังก์ชันที่จำเป็น ไม่ต้องแถมบรรทัดที่ไม่เกี่ยวข้องที่อยู่ติดกันมาด้วย

## เครื่องมือที่ใช้
ส่วนใหญ่นิยมใช้ [[tree-sitter]] ในการ parse code เพราะเร็วและรองรับหลายภาษา ซึ่งเป็นหัวใจสำคัญของเครื่องมืออย่าง [[claude-context]]

## ได้อะไร? (The Payoff)
ผลคือ RAG ที่มีประสิทธิภาพสูงขึ้น AI ไม่ต้องพยายามเดาเนื้อหาที่ขาดหายไป และลดปริมาณ token ที่ไม่จำเป็นลงได้อย่างมาก

## See also
- [[tree-sitter]]
- [[semantic-retrieval]]
- [[claude-context]]
