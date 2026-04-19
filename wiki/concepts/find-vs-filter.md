---
title: Find vs. Filter
type: concept
tags: [ai, prompting, code-review, claude, claude-opus-4-7]
created: 2026-04-20
updated: 2026-04-20
sources: [Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md]
---

# Find vs. Filter / แยกขั้นหา กับ ขั้นกรอง ออกจากกัน

## เรื่องมันเริ่มจากตรงนี้

ลองนึกว่าคุณใช้ [[claude-opus-4-7|Opus 4.7]] (model ตัวใหม่ของ Anthropic ที่ออกเมษา 2026) ช่วย review code แล้วเขียน prompt ว่า:

> "ช่วย review PR นี้หน่อย รายงานเฉพาะ bug ที่ severity สูง"

Claude ตอบกลับมาว่า "ไม่พบปัญหาสำคัญครับ" คุณก็ merge

ผ่านไปสามวัน bug โผล่ใน production

มา dig ดูทีหลังถึงรู้ว่า Claude **เจอ bug ตั้งแต่แรกแล้ว** แค่ตัดสินเองว่า "อันนี้ severity ไม่สูงพอตามที่ user บอก" เลยไม่รายงาน

นี่คือปัญหาที่ pattern "find vs. filter" พยายามแก้

## ทำไม 4.7 ถึงเจอปัญหานี้หนักกว่า 4.6

[[claude-opus-4-7|Opus 4.7]] ทำตาม instruction **literal มากขึ้น** — แปลว่าทำตามคำสั่งตรง ๆ ตามตัวอักษร ไม่เดาใจ ไม่ยืดหยุ่น

ฟังดูดี แต่ผลข้างเคียงคือ ถ้าเราบอกว่า *"รายงานเฉพาะของสำคัญ"* มันจะทำ **2 ขั้นในหัวพร้อมกัน** — หาปัญหา + ตัดสินว่าสำคัญพอไหม — แล้วเงียบเฉพาะที่มันตัดสินว่าไม่ผ่านเกณฑ์

Anthropic เคย test เอง ([[claude-opus-4-7-migration-pachaar|ตัวเลขจาก Pachaar]]):

- 4.7 เจอ bug ได้ **แม่นกว่า** 4.6 ทั้ง recall (เจอครบขึ้น) และ precision (เจอแล้วถูกขึ้น)
- แต่พอใส่บรรทัด `"be conservative"` หรือ `"report only high-severity"` เข้าไปใน prompt — **recall ตก** ทันที เพราะ model เจอแล้วกรองทิ้งเอง

4.6 โชคดีที่ค่อนข้าง "ขี้ฟ้อง" อยู่แล้ว การกรองเอาเองเลยไม่ค่อยเกิด พอ 4.7 ทำตามคำสั่งเป๊ะขึ้น ปัญหาการกรองตัวเองก็โผล่ชัด

**ผลคือ** prompt ที่เคย work บน 4.6 (เพราะ model ไม่ค่อยเชื่อเรา) กลับพังบน 4.7 (เพราะ model เชื่อเรามากขึ้น)

## วิธีแก้: แยก 2 ขั้นออกจากกันชัด ๆ

หลักง่าย ๆ คือ อย่าสั่งให้ model ทำ 2 อย่างพร้อมกัน

1. **Find** — หาทุกอย่างที่น่าสงสัย รวมของที่ไม่แน่ใจด้วย ยังไม่ต้องตัดสินว่าสำคัญไหม
2. **Filter** — ค่อยมาจัดอันดับ/ตัดทิ้งในรอบสอง (หรือให้คน / agent ตัวอื่นทำ)

เหมือนให้น้อง intern ไฮไลต์ทุกจุดในโค้ดที่ตัวเองงงก่อน แล้วค่อยให้ senior มานั่งเคาะว่าอันไหน merge ได้ อันไหนต้องแก้ — แทนที่จะบอก intern ว่า "ไฮไลต์เฉพาะที่สำคัญนะ" เพราะ intern จะไฮไลต์แค่ของที่ตัวเองมั่นใจ ซึ่งมักคือของที่ชัดจนเกินไปจนไม่ใช่ bug จริง ๆ

## Prompt ที่ใช้ได้จริง

### ถ้ามี pipeline สองขั้น (find แยกจาก filter)

Pachaar เสนอ prompt หน้าตานี้สำหรับขั้น find:

> "Report every issue you find, including ones you are uncertain about or consider low-severity. Do not filter for importance or confidence at this stage. Your goal here is coverage: it is better to surface a finding that later gets filtered out than to silently drop a real bug. For each finding, include your confidence level and an estimated severity so a downstream filter can rank them."

แปลไอเดียหลัก:

- บอกตรง ๆ ว่า **ขั้นนี้ห้ามกรอง**
- อธิบาย **ทำไม** (รอบนี้เน้นหาให้ครบ รอบหน้าค่อยกรอง) — ให้ reasoning ของ model ตรงกับเจตนาเรา ไม่ใช่แค่ทำตามคำสั่งแห้ง ๆ
- ขอ **metadata** (confidence + severity) ติดกับ finding แต่ละตัว เพื่อให้ขั้นถัดไปเอาไปจัดอันดับได้

**ได้อะไร** — Claude จะไม่เงียบของที่ตัวเองไม่มั่นใจ เราเห็นทุกอย่างที่มันเห็น แล้วเป็นคนตัดสินเองว่าของไหนควรแก้

### ถ้ามีรอบเดียว ไม่มี downstream filter

บางทีเราไม่ได้สร้าง pipeline ซับซ้อน แค่อยาก review ในช็อตเดียว Pachaar แนะนำว่า **เลิกใช้คำความรู้สึก ใช้ threshold ที่จับต้องได้แทน**:

> "Report any bugs that could cause incorrect behavior, a test failure, or a misleading result; only omit pure style or naming preferences."

จุดต่างคือ:

- `"incorrect behavior / test failure / misleading result"` — model เช็กได้จากหลักฐานจริงในโค้ด
- `"high-severity"` / `"be conservative"` — ความรู้สึก ไม่มีเกณฑ์ 4.7 เลยตีความ literal ตามความเข้าใจตัวเอง แล้วตัดของสีเทาทิ้งหมด

**ได้อะไร** — คำสั่งที่เป็นรูปธรรม model ตีความตรงกับเราได้ ไม่ใช่ตีเอง

## ใช้ได้กับงานอื่นด้วย ไม่ใช่แค่ review code

pattern เดียวกันเจอได้ทุกที่ที่ขั้น "หา" กับขั้น "ตัดสิน" ปนกันได้ง่าย:

- **security audit** — scan vuln ให้ครบก่อน แล้วค่อยจัด severity
- **content moderation** — flag ทุก content น่าสงสัย แล้วค่อยตัดสินว่า action อะไร
- **alert/log triage** — detect anomaly ทุกอัน แล้วค่อย route ไปทีมไหน
- **สรุปงานวิจัย** — highlight ทุกจุดที่น่าสนใจ แล้วค่อยย่อ

ทุกเคสแก้เหมือนกัน: **แยกขั้น → ขอ metadata ติดทุก finding → เอาไปตัดสินในขั้นท้าย**

## See also

- [[claude-opus-4-7]]
- [[claude-opus-4-7-migration-pachaar]]
- [[delegation-mindset]] — ท่ามอบงานภาพรวมของ 4.7
- [[subagent-patterns]] — ถ้าแยกขั้น find กับ filter เป็นคนละ subagent เลย
- [[advisor-strategy]] — executor รุ่นเล็กทำ find, advisor รุ่นใหญ่ทำ filter
- [[harness-engineering]] — ถ้าออกแบบ reviewer agent อย่ารวม find + filter ในตัวเดียว
- [[llm-coding-pitfalls]]
