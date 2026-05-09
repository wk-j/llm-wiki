---
title: Milvus
type: entity
tags: [database, vector-search, infrastructure, open-source]
created: 2026-05-08
updated: 2026-05-08
sources: [why-im-against-claude-codes-grep-only-retrieval.md]
---

# Milvus / มิลวัส

Milvus เป็น open-source [[vector-search|vector database]] ที่ออกแบบมาสำหรับงาน AI และ machine learning ในสเกลใหญ่ ทำหน้าที่เก็บและค้นหา [[embedding|embeddings]] ของข้อมูลที่ไม่มีโครงสร้าง (unstructured data) เช่น รูปภาพ วิดีโอ หรือในบริบทของ [[claude-code]] คือ "code snippets"

## บทบาทในระบบ AI
- **ความเร็วสเกลใหญ่:** รองรับการค้นหา vector นับพันล้านรายการด้วยความเร็วสูง
- **การจัดการ Codebase:** ถูกนำมาใช้เป็นฐานข้อมูลหลักในเครื่องมืออย่าง [[claude-context]] เพื่อทำ [[semantic-retrieval]] ให้กับ coding agents
- **ประสิทธิภาพเหนือ Grep:** ต่างจาก [[agentic-search]] ที่ใช้การค้นหาคำตรงๆ (literal matching), Milvus ช่วยให้ agent หา code ที่ "ความหมายเหมือนกัน" ได้แม้จะใช้คำต่างกัน

## ทำไมถึงสำคัญ
ในยุคที่ codebase มีขนาดใหญ่เกินกว่าจะยัดลง context window ทั้งหมด การมี Milvus ช่วยให้เราทำ RAG (Retrieval-Augmented Generation) ที่แม่นยำขึ้น ช่วยลด [[token-optimization|token bloat]] และประหยัดค่าใช้จ่ายได้มาก

## See also
- [[zilliz]]
- [[claude-context]]
- [[semantic-retrieval]]
