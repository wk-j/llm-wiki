---
title: Semantic Retrieval
type: concept
tags: [retrieval, ai, vector-search, rag]
created: 2026-05-08
updated: 2026-05-08
sources: [why-im-against-claude-codes-grep-only-retrieval.md]
---

# Semantic Retrieval / การดึงข้อมูลเชิงความหมาย

Semantic Retrieval คือการค้นหาข้อมูลโดยเน้นที่ **"ความหมาย" (Intent)** มากกว่าการจับคู่คำตรงๆ (Keyword Matching) โดยใช้เทคโนโลยี [[embedding]] เพื่อเปลี่ยนข้อความให้เป็น vector และค้นหาความใกล้เคียงในเชิงพื้นที่ (vector space)

## ในบริบทของ AI Coding
เมื่อ Agent ต้องทำงานกับ codebase ขนาดใหญ่ Semantic Retrieval มีข้อดีเหนือ [[agentic-search]] (grep) ดังนี้:
- **ค้นหาได้แม้ใช้คำต่างกัน:** เช่น หาฟังก์ชันจัดการ login ได้แม้จะค้นหาด้วยคำว่า "auth"
- **ลด [[token-optimization|token bloat]]:** ดึงมาเฉพาะฟังก์ชันหรือคลาสที่เกี่ยวข้องจริงๆ ไม่ต้องดึงมาทั้งไฟล์
- **ความเร็ว:** ค้นหาใน vector database ครั้งเดียวได้ผลลัพธ์ที่แม่นยำ ไม่ต้องรัน grep ซ้ำไปซ้ำมาหลายรอบ (Time Tax)

## วิธีการทำงาน
1. **Chunking:** แบ่ง code เป็นส่วนๆ (นิยมใช้ [[ast-based-chunking]])
2. **Embedding:** แปลง code แต่ละส่วนเป็นตัวเลข (vector)
3. **Indexing:** เก็บไว้ใน vector database อย่าง [[milvus]]
4. **Retrieval:** เมื่อมีคำถาม Agent จะแปลงคำถามเป็น vector แล้วไปหา code ที่ "ใกล้เคียง" ที่สุดมาตอบ

## See also
- [[vector-search]]
- [[claude-context]]
- [[agentic-search]]
- [[token-optimization]]
