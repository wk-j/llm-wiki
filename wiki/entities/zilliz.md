---
title: Zilliz
type: entity
tags: [company, cloud, vector-search]
created: 2026-05-08
updated: 2026-05-08
sources: [why-im-against-claude-codes-grep-only-retrieval.md]
---

# Zilliz / ซิลลิซ

Zilliz เป็นบริษัทที่อยู่เบื้องหลัง [[milvus]] (open-source vector database) โดยให้บริการ **Zilliz Cloud** ซึ่งเป็นเวอร์ชัน managed service สำหรับองค์กรที่ต้องการความสะดวกและสเกลที่ใหญ่ขึ้น

## ความเกี่ยวข้องกับ Coding Agents
- **Backbone ของ RAG:** Zilliz Cloud ถูกใช้เป็นโครงสร้างพื้นฐานสำหรับการทำ [[semantic-retrieval]] ในเครื่องมืออย่าง [[claude-context]]
- **การจัดการ Context:** ช่วยให้ coding agents สามารถดึงเฉพาะ code ส่วนที่เกี่ยวข้องจริงๆ มาใช้งาน แทนที่จะต้องอ่านทั้งไฟล์ ช่วยแก้ปัญหา [[token-optimization|token bloat]]

## See also
- [[milvus]]
- [[claude-context]]
- [[semantic-retrieval]]
