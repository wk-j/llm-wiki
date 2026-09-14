---
title: Plannotator
type: entity
tags: [product, developer-tools, code-review, ai, agents]
created: 2026-09-12
updated: 2026-09-12
sources: [dillon-mulroy-ships-production-code-he-didnt-write.md]
---

# Plannotator / เครื่องมือ annotate plan และ review diff ในเครื่อง

**Plannotator** เป็นเครื่องมือ local review และ annotation ที่ [[dillon-mulroy|Dillon Mulroy]] ใช้ใน [[dillon-mulroy-ships-production-code-he-didnt-write|workflow กับ coding agent]] บทสัมภาษณ์ระบุว่าใช้ร่วมกับ pi, OpenCode, Codex และ Claude Code ได้ ข้อมูลนี้ยังไม่ได้ตรวจเทียบกับเอกสารของผลิตภัณฑ์ในการ ingest ครั้งนี้

## สองจังหวะที่ใช้

ตอน review code ผู้ใช้เรียกคำสั่ง review แล้ว Plannotator เปิด local web app หน้าตาคล้าย GitHub PR review จากนั้นอ่าน diff ทีละไฟล์ ใส่ comment และ submit กลับเข้า agent session ให้แก้ต่อ

ตอนคุย plan ผู้ใช้เปิดไฟล์เพื่อ highlight และ comment ได้ หรือดึงข้อความล่าสุดของ agent มา annotate โดยตรง Dillon ใช้วิธีนี้ค่อย ๆ ปรับ shared understanding จน plan มี shape ใกล้ tech spec แล้วจึงเขียนลง Markdown และเริ่ม implement

**ผลคือ:** feedback ไม่ต้องรอให้ push PR และไม่หลุดออกจาก session ที่ agent กำลังทำงาน แต่ตัวเครื่องมือไม่ได้รับรองว่า review ครบหรือ code พร้อม production

## See also

- [[dillon-mulroy-ships-production-code-he-didnt-write]]
- [[dillon-mulroy]]
- [[agentic-code-review]]
- [[pi-agent]]
- [[stacked-pull-requests]]
