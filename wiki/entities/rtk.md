---
title: RTK (RTK-AI)
type: entity
tags: [product, cli, rust, ai-tooling]
created: 2026-04-25
updated: 2026-04-25
sources: [rtk-github.md]
---

# RTK (RTK-AI)

**RTK** คือ CLI proxy ประสิทธิภาพสูงที่เขียนด้วยภาษา Rust ออกแบบมาเพื่อลดการใช้ token ของ LLM ลง 60–90% โดยการทำหน้าที่เป็นตัวกลาง (wrapper) ระหว่าง AI agent กับ shell เพื่อกรองและบีบอัด output ก่อนส่งกลับเข้า context window

## ความสามารถหลัก (Core Capabilities)

- **Output Compression:** ใช้กลยุทธ์ Filtering (ตัด noise), Grouping (รวมกลุ่มไฟล์/error), Truncation (ตัดส่วนที่ไม่สำคัญ), และ Deduplication (ลดความซ้ำซ้อนของ log)
- **Tee Recovery:** เมื่อคำสั่งรันพลาด RTK จะบันทึก full output ไว้ในไฟล์โลคัล เพื่อให้ agent เรียกดูได้ภายหลังโดยไม่ต้องรันคำสั่งแพงๆ ซ้ำ
- **Analytics:** คำสั่ง `rtk gain` แสดงสถิติการประหยัด token และค่าใช้จ่ายในรูปแบบ ASCII graph
- **Smart Heuristics:**
    - `rtk smart`: สรุปเนื้อหาไฟล์ใน 2 บรรทัด
    - `rtk read --l aggressive`: แสดงเฉพาะ signature ของฟังก์ชัน (strip bodies)

## การทำงานร่วมกับเครื่องมืออื่น (Integrations)

RTK รองรับคำสั่งมากกว่า 100 คำสั่งในหลาย ecosystem (Git, Docker, AWS, K8s, etc.) และทำงานร่วมกับ agent หลายตัว:
- [[claude-code|Claude Code]]
- [[cursor|Cursor]]
- [[opencode|OpenCode]]
- Gemini CLI

## See also

- [[token-optimization|การเพิ่มประสิทธิภาพ Token (Token Optimization)]]
- [[compaction|การบดอัดบริบท (Context Compaction)]]
- [[coding-harness|เครื่องมือช่วยเขียนโค้ด (Coding Harness)]]
