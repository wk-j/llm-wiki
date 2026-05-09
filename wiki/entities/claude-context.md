---
title: Claude Context
type: entity
tags: [tool, rag, claude-code, open-source]
created: 2026-05-08
updated: 2026-05-08
sources: [why-im-against-claude-codes-grep-only-retrieval.md]
---

# Claude Context / โคลด คอนเทกต์

Claude Context เป็นเครื่องมือ open-source ที่ช่วยเสริมประสิทธิภาพการดึงข้อมูล (retrieval) ให้กับ [[claude-code]] โดยเปลี่ยนจากการค้นหาแบบ grep ดั้งเดิม มาใช้ [[semantic-retrieval]] ผ่าน vector database อย่าง [[milvus]] หรือ [[zilliz]]

## ฟีเจอร์หลัก
- **Semantic Search:** ช่วยให้ Agent หา code เจอตามความหมาย (intent) ไม่ใช่แค่ keyword
- **[[ast-based-chunking]]:** ใช้ `tree-sitter` ย่อย code เป็นฟังก์ชันหรือคลาส ทำให้ context ที่ดึงมามีคุณภาพสูงและไม่หลุดประเด็น
- **[[merkle-tree-sync]]:** ตรวจสอบการเปลี่ยนแปลงของไฟล์ใน codebase อย่างรวดเร็ว เพื่ออัปเดต index เฉพาะส่วนที่เปลี่ยน
- **MCP Integration:** เชื่อมต่อกับ Claude และเครื่องมืออื่นๆ ผ่าน [[model-context-protocol|MCP]]

## ทำไมต้องใช้?
เป้าหมายหลักคือการแก้ปัญหา "Token Bloat" และ "Time Tax" ใน [[claude-code]] ดั้งเดิม โดย Claude Context อ้างว่าสามารถลดการใช้ token ได้กว่า 40% และช่วยให้ Agent เข้าถึง context ที่ถูกต้องได้เร็วกว่าการรัน grep หลายๆ รอบ

## See also
- [[claude-code]]
- [[agentic-search]]
- [[semantic-retrieval]]
