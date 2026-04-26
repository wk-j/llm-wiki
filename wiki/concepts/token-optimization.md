---
title: Token Optimization / การเพิ่มประสิทธิภาพ Token
type: concept
tags: [ai, tokens, efficiency, context-window]
created: 2026-04-25
updated: 2026-04-25
sources: [rtk-github.md, alex-ker-harnesses-optimize.md, claude-opus-4-7-whats-new-docs.md]
---

# Token Optimization / การเพิ่มประสิทธิภาพ Token

**Token Optimization** คือเทคนิคหรือกระบวนการในการลดจำนวน token ที่ส่งไปยัง LLM โดยที่ยังรักษาข้อมูลสำคัญ (information density) ไว้ครบถ้วน เพื่อประหยัดค่าใช้จ่ายและป้องกัน [[context-rot|ปัญหา context เต็ม]]

## กลยุทธ์ที่ใช้ (Strategies)

ในบริบทของ AI Agents และ CLI เครื่องมืออย่าง [[rtk|RTK]] และ [[claude-code|Claude Code]] ใช้เทคนิคดังนี้:

1.  **Output Filtering:** ตัดข้อมูลที่เป็น noise เช่น whitespace, comments, หรือ boilerplate code ที่ไม่จำเป็นต่อการวิเคราะห์
2.  **Semantic Truncation:** การตัดส่วนที่ไม่สำคัญออกโดยอิงจากความหมาย เช่น การเหลือเฉพาะ function signature (`rtk read --l aggressive`) หรือการตัดช่วงกลางของไฟล์ log ที่ซ้ำซ้อน
3.  **Grouping & Deduplication:** การรวมกลุ่มข้อมูลที่คล้ายกัน (เช่น ไฟล์ใน directory เดียวกัน) หรือการยุบรวม log lines ที่ซ้ำกันแล้วใส่ตัวเลขระบุจำนวนครั้งแทน
4.  **Heuristic Summary:** การใช้ heuristic สั้นๆ เพื่ออธิบายเนื้อหาไฟล์แทนการอ่านไฟล์ทั้งหมด เช่น `rtk smart` ที่สรุปไฟล์ใน 2 บรรทัด
5.  **Progressive Disclosure:** การเปิดเผยข้อมูลทีละส่วน (เช่น การหาคำสั่งผ่าน [[model-context-protocol|MCP]] แทนการโหลด manual ทั้งหมด) ตามที่ [[alex-ker|Alex Ker]] แนะนำ

## ทำไมถึงสำคัญ (Why it matters)

- **ขยายขีดจำกัด Context:** ช่วยให้ agent ทำงานกับโปรเจกต์ขนาดใหญ่ได้นานขึ้นก่อนจะถึงขีดจำกัดของ context window
- **ลดต้นทุน (Cost Reduction):** การลด token ลง 60-90% ส่งผลโดยตรงต่อค่า API bills
- **เพิ่มความเร็ว (Latency):** จำนวน token ที่น้อยลงหมายถึงเวลาในการประมวลผล (TTFT และ generation time) ที่เร็วขึ้น
- **ลด Error:** ลดโอกาสที่ LLM จะสับสนหรือ "หลง" (lost in the middle) เมื่อเจอบริบทที่ยาวเกินไป

## See also

- [[rtk|RTK (CLI Proxy สำหรับบีบอัด output)]]
- [[compaction|Context Compaction ใน Claude Code]]
- [[instruction-budget|งบประมาณคำสั่ง (Instruction Budget)]]
- [[context-rot|การเสื่อมของบริบท (Context Rot)]]
