---
title: Armin Ronacher
type: entity
tags: [developer, open-source, ai, software-engineering]
created: 2026-07-04
updated: 2026-10-07
sources: [code-isnt-free-mario-zechner-hard-truths-coding-ai.md, what-is-codemode-armin-ronacher.md]
---

# Armin Ronacher / อาร์มิน โรนาเคอร์

**Armin Ronacher** เป็นนักพัฒนา open source ที่ใน source [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]] ถูกกล่าวถึงในฐานะคนร่วมงานของ [[mario-zechner|Mario Zechner]] ที่ [[earendil|Earendil]] และเริ่มช่วยทำ [[pi-agent|pi]].

ในบทสัมภาษณ์ Mario เรียก Armin ว่าเป็น "junior" ที่ดีที่สุดที่เขาเคยมี ในความหมายว่า Armin กำลังเรียนรู้และรับงานใน pi ได้มากขึ้น เพื่อให้วันหนึ่งสามารถช่วยถือบทบาทนำของโปรเจกต์ได้.

## มุมของ Armin เรื่อง tool, bash และ Codemode

ใน [[what-is-codemode-armin-ronacher|What is Codemode]] (บล็อกของเขาเอง 2026-10-06) Armin เขียนในฐานะคนทำ Pi โดยตรง เขาเล่าว่า Pi 1.0 เพิ่ม MCP support ผ่าน [[codemode|Codemode]] และอธิบายว่าไม่ได้กลับลำจากโพสต์ปีก่อน ("Code Is All You Need", "MCP needs code") ที่เชียร์ให้ agent ใช้ script กับ CLI แทน custom tool

เหตุผลของเขาคือ bash ยังเป็นทางหลัก แต่ต่อได้แค่โปรแกรมที่รันได้ งานที่ต้องแตะตัว harness เช่น ดูรูป สั่ง subagent หรือเรียก model อื่น ต้องไปอยู่อีกฝั่ง เขาเลยแยกภาพ [[harness-vs-execution-environment|brains vs hands]] แล้ววาง Codemode ไว้ฝั่ง harness ใน sandbox ของตัวเอง

เขายังบอกว่า MCP ecosystem กำลังมาถึงข้อสรุปเดียวกับที่เขาพูดไว้ปีก่อน คือ code และเสนอสี่อย่างที่ MCP server ควรมี: structured content, รูปทรง output คงที่, binary ใหญ่ และ tool search ที่ประกอบข้าม server ได้

**ผลคือ:** Armin ไม่ได้มอง MCP กับ CLI เป็นคู่แข่ง เขามองว่าทั้งคู่ควรถูกเรียกผ่าน code

## Open questions

- รายละเอียดบทบาทของ Armin ใน Earendil ยังอิงจากบทสัมภาษณ์ของ Mario ส่วนบล็อก Codemode ยืนยันแค่ว่าเขาเขียนในนาม "we" ของทีม Pi
- โพสต์ปีก่อนของเขา ("Code Is All You Need", "MCP needs code", "better models worse tools") ยังไม่ได้ ingest

## See also

- [[earendil]]
- [[mario-zechner]]
- [[pi-agent]]
- [[what-is-codemode-armin-ronacher]]
- [[codemode]]
- [[harness-vs-execution-environment]]
