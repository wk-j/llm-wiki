---
title: Find vs. Filter
type: concept
tags: [ai, prompting, code-review, claude, claude-opus-4-7]
created: 2026-04-20
updated: 2026-04-23
sources: [Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md]
---

# Find vs. Filter / แยกขั้นหา กับ ขั้นกรอง ออกจากกัน

## จุดเริ่มต้นของปัญหา

ลองนึกภาพว่าคุณใช้ [[claude-opus-4-7|Opus 4.7]] (model ตัวใหม่ของ Anthropic ที่เปิดตัวเมษายน 2026) เพื่อช่วยรีวิวโค้ด แล้วเขียน prompt ว่า:

> "ช่วยรีวิว PR นี้หน่อย และรายงานเฉพาะ bug ที่มี severity สูง"

Claude ตอบกลับมาว่า "ไม่พบปัญหาสำคัญครับ" คุณจึงทำการ merge

สามวันต่อมา, bug เกิดขึ้นใน production

เมื่อกลับมาตรวจสอบ, พบว่า Claude **เจอ bug ตั้งแต่แรกแล้ว** แต่ตัดสินใจเองว่า "ปัญหานี้ severity ไม่สูงพอตามที่ user บอก" จึงไม่ได้รายงานออกมา

นี่คือปัญหาที่ pattern "find vs. filter" พยายามแก้ไข

## ทำไม 4.7 ถึงเจอปัญหานี้หนักกว่า 4.6

[[claude-opus-4-7|Opus 4.7]] ทำตาม instruction **ตรงตัวมากขึ้น (literal)** — หมายความว่ามันทำตามคำสั่งตามตัวอักษรอย่างเคร่งครัด ไม่เดาใจ และไม่ยืดหยุ่น

ซึ่งฟังดูดี แต่ผลข้างเคียงคือ ถ้าเราบอกว่า *"รายงานเฉพาะสิ่งที่สำคัญ"* มันจะทำ **2 ขั้นตอนในหัวพร้อมกัน** — คือการหาปัญหาและการตัดสินใจว่าสำคัญพอหรือไม่ — แล้วจะเงียบในส่วนที่มันตัดสินว่าไม่ผ่านเกณฑ์

Anthropic ได้ทำการทดสอบเอง ([[claude-opus-4-7-migration-pachaar|ตัวเลขจาก Pachaar]]):

-   4.7 สามารถหา bug ได้ **แม่นยำกว่า** 4.6 ทั้งในด้าน recall (เจอครบถ้วนกว่า) และ precision (สิ่งที่เจอถูกต้องกว่า)
-   แต่เมื่อใส่บรรทัด `"be conservative"` หรือ `"report only high-severity"` เข้าไปใน prompt — **recall จะลดลงทันที** เพราะ model เจอแล้วแต่กรองทิ้งเอง

4.6 โชคดีที่ค่อนข้าง "ขี้ฟ้อง" อยู่แล้ว ทำให้การกรองเองไม่ค่อยเกิดขึ้น แต่เมื่อ 4.7 ทำตามคำสั่งได้เป๊ะขึ้น ปัญหาการกรองตัวเองจึงปรากฏชัดขึ้น

**ผลลัพธ์คือ** prompt ที่เคยใช้ได้ผลกับ 4.6 (เพราะ model ไม่ค่อยเชื่อฟัง) กลับใช้ไม่ได้ผลกับ 4.7 (เพราะ model เชื่อฟังมากขึ้น)

## วิธีแก้: แยก 2 ขั้นตอนออกจากกันอย่างชัดเจน

หลักการง่ายๆ คือ อย่าสั่งให้ model ทำ 2 อย่างพร้อมกัน:

1.  **Find** — ค้นหาทุกอย่างที่น่าสงสัย รวมถึงสิ่งที่ไม่แน่ใจด้วย โดยยังไม่ต้องตัดสินใจว่าสำคัญหรือไม่
2.  **Filter** — ค่อยมาจัดลำดับหรือตัดทิ้งในรอบที่สอง (หรือให้คนหรือ agent ตัวอื่นทำ)

เปรียบเสมือนการให้น้อง intern ไฮไลต์ทุกจุดในโค้ดที่ตัวเองไม่เข้าใจก่อน แล้วค่อยให้ senior มาพิจารณาว่าส่วนไหน merge ได้ หรือส่วนไหนต้องแก้ไข — แทนที่จะบอก intern ว่า "ไฮไลต์เฉพาะส่วนที่สำคัญนะ" เพราะ intern จะไฮไลต์เฉพาะส่วนที่ตัวเองมั่นใจ ซึ่งมักจะเป็นสิ่งที่ชัดเจนเกินไปจนไม่ใช่ bug จริงๆ

## Prompt ที่ใช้งานได้จริง

### ถ้ามี pipeline สองขั้น (find แยกจาก filter)

Pachaar เสนอ prompt สำหรับขั้นตอน find ดังนี้:

> "Report every issue you find, including ones you are uncertain about or consider low-severity. Do not filter for importance or confidence at this stage. Your goal here is coverage: it is better to surface a finding that later gets filtered out than to silently drop a real bug. For each finding, include your confidence level and an estimated severity so a downstream filter can rank them."

**แนวคิดหลัก:**

-   บอกตรงๆ ว่า **ขั้นตอนนี้ห้ามกรอง**
-   อธิบาย **เหตุผล** (รอบนี้เน้นหาให้ครบ, รอบหน้าค่อยกรอง) — เพื่อให้ reasoning ของ model ตรงกับเจตนาของเรา ไม่ใช่แค่ทำตามคำสั่งแบบแห้งๆ
-   ขอ **metadata** (confidence + severity) สำหรับแต่ละ finding เพื่อให้ขั้นตอนถัดไปสามารถนำไปจัดลำดับได้

**ข้อดี** — Claude จะไม่เงียบในสิ่งที่ตัวเองไม่มั่นใจ เราจะเห็นทุกอย่างที่มันเห็น แล้วจึงเป็นผู้ตัดสินใจเองว่าสิ่งไหนควรแก้ไข

### ถ้ามีรอบเดียว ไม่มี downstream filter

บางครั้งเราไม่ได้สร้าง pipeline ที่ซับซ้อน แต่อยากรีวิวให้เสร็จในครั้งเดียว Pachaar แนะนำให้ **เลิกใช้คำที่เป็นความรู้สึก และหันมาใช้ threshold ที่จับต้องได้แทน**:

> "Report any bugs that could cause incorrect behavior, a test failure, or a misleading result; only omit pure style or naming preferences."

**จุดที่แตกต่าง:**

-   `"incorrect behavior / test failure / misleading result"` — model สามารถตรวจสอบได้จากหลักฐานจริงในโค้ด
-   `"high-severity"` / `"be conservative"` — เป็นความรู้สึกที่ไม่มีเกณฑ์ชัดเจน 4.7 จึงตีความตามตัวอักษรตามความเข้าใจของตัวเอง แล้วตัดสิ่งที่เป็นสีเทาทิ้งไป

**ข้อดี** — คำสั่งที่เป็นรูปธรรมทำให้ model สามารถตีความได้ตรงกับความต้องการของเรามากขึ้น

## ประยุกต์ใช้กับงานอื่น

pattern นี้สามารถพบได้ในทุกที่ที่ขั้นตอน "การหา" และ "การตัดสินใจ" อาจปะปนกัน:

-   **security audit** — สแกนหาช่องโหว่ให้ครบก่อน แล้วค่อยจัดระดับความรุนแรง
-   **content moderation** — flag ทุก content ที่น่าสงสัย แล้วค่อยตัดสินใจว่าจะดำเนินการอย่างไร
-   **alert/log triage** — ตรวจจับ anomaly ทั้งหมด แล้วค่อยส่งต่อไปยังทีมที่เกี่ยวข้อง
-   **สรุปงานวิจัย** — ไฮไลต์ทุกจุดที่น่าสนใจ แล้วค่อยนำมาย่อ

ทุกกรณีแก้ไขได้ในทำนองเดียวกัน: **แยกขั้นตอน → ขอ metadata สำหรับทุก finding → นำไปตัดสินใจในขั้นตอนสุดท้าย**

## ดูเพิ่มเติม

- [[claude-opus-4-7]]
- [[claude-opus-4-7-migration-pachaar]]
- [[delegation-mindset]] — ภาพรวมการมอบหมายงานสำหรับ 4.7
- [[subagent-patterns]] — หากแยกขั้นตอน find และ filter เป็นคนละ subagent
- [[advisor-strategy]] — executor รุ่นเล็กทำ find, advisor รุ่นใหญ่ทำ filter
- [[harness-engineering]] — หากออกแบบ reviewer agent, อย่ารวม find + filter ไว้ในตัวเดียว
- [[llm-coding-pitfalls]]
