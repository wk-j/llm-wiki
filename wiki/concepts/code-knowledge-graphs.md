---
title: Code Knowledge Graphs
type: concept
tags: [knowledge-graphs, code-intelligence, developer-tools, ai-agents]
created: 2026-04-13
updated: 2026-04-23
sources: [abhigyanpatwariGitNexus GitNexus The Zero-Server Code Intelligence Engine.md]
---

# Code Knowledge Graphs

Code Knowledge Graph คือ knowledge graph ที่สร้างขึ้นจากโครงสร้างของ codebase โดยแสดง functions, classes, modules, imports, call chains, inheritance, และ execution flows ในรูปแบบของโหนดและเส้นเชื่อม (nodes and edges) สิ่งนี้แตกต่างจากการค้นหาแบบ flat text หรือการใช้ embeddings กับ code snippets เพราะ Code Knowledge Graph สามารถจับ **ความสัมพันธ์** ของโค้ดได้: ใครเรียกใช้ฟังก์ชันอะไร, อะไรขึ้นอยู่กับอะไร, และ execution flow ไหลจาก entry point ไปยังส่วนต่างๆ ของระบบได้อย่างไร

## ความสำคัญสำหรับ AI agents

เครื่องมือ AI สำหรับการเขียนโค้ดส่วนใหญ่มักทำงานกับเนื้อหาของไฟล์และการค้นหาข้อความ ซึ่งสามารถหาฟังก์ชันได้แต่ไม่ทราบถึง dependency graph ทั้งหมดของมัน การแก้ไขฟังก์ชันโดยไม่ทราบว่ามีใครเรียกใช้บ้างอาจนำไปสู่ breaking changes ได้ Code Knowledge Graph ช่วยให้ agent มีความตระหนักรู้เชิงโครงสร้าง (structural awareness) — ทำให้สามารถวิเคราะห์ผลกระทบ (blast radius analysis), ติดตามกระบวนการ (process tracing), และแสดง chuỗi phụ thuộc ที่มีคะแนนความเชื่อมั่นได้

## ขั้นตอนการสร้าง (ตามตัวอย่างของ [[gitnexus]])

1.  **AST parsing** — ดึงสัญลักษณ์ (symbols) เช่น functions, classes, interfaces โดยใช้ Tree-sitter
2.  **Resolution** — แก้ปัญหาการ resolve import ข้ามไฟล์, การเรียกใช้, การสืบทอด (heritage), และประเภทของ receiver
3.  **Clustering** — จัดกลุ่มสัญลักษณ์ที่เกี่ยวข้องกันเป็นกลุ่มฟังก์ชัน (functional communities) (เช่น การใช้อัลกอริทึม Leiden)
4.  **Process tracing** — ติดตาม execution flows จาก entry points ผ่าน call chains
5.  **Search indexing** — สร้าง hybrid indexes (BM25 + semantic) บนกราฟ

## Precomputed vs. Query-time Structure

[[graph-rag]] แบบดั้งเดิมจะเก็บเฉพาะเส้นเชื่อมและให้ LLM สำรวจตอน query time ซึ่งต้องใช้หลาย "hop" ในการค้นหา ในขณะที่แนวทางแบบ precomputed (ดังที่ใช้ใน [[gitnexus]]) จะทำการ resolve clusters, processes, และ confidence scores ไว้ล่วงหน้าตั้งแต่ตอน index ทำให้การเรียกใช้ tool เพียงครั้งเดียวสามารถคืนค่า structural context ที่สมบูรณ์ได้

## การดำเนินการที่สำคัญ

-   **Impact analysis** — เมื่อกำหนดสัญลักษณ์มาให้ สามารถค้นหาสิ่งที่อยู่ upstream (ขึ้นอยู่กับสัญลักษณ์นั้น) และ downstream (สิ่งที่สัญลักษณ์นั้นขึ้นอยู่กับ) พร้อม confidence scores
-   **Context** — มุมมอง 360 องศาของสัญลักษณ์: callers, callees, และการมีส่วนร่วมใน process
-   **Change detection** — แมป git diffs กับ processes ที่ได้รับผลกระทบและระดับความเสี่ยง
-   **Process-grouped search** — ผลการค้นหาที่จัดกลุ่มตาม execution flows ไม่ใช่แค่การจับคู่ไฟล์

## ดูเพิ่มเติม

- [[gitnexus]]
- [[graph-rag]]
- [[model-context-protocol]]
- [[llm-knowledge-bases]]
