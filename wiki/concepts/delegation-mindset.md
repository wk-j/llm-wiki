---
title: Delegation Mindset
type: concept
tags: [ai, prompting, claude, claude-code, coding-harness, workflow]
created: 2026-04-20
updated: 2026-07-05
sources: [Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md, fables-judgement-simon-willison.md]
---

# Delegation Mindset / วิธีคิดแบบมอบงาน

แนวคิดการสื่อสารกับ [[claude-opus-4-7|Opus 4.7]] เสมือนการมอบหมายงานให้ **วิศวกรที่เก่งแต่อยู่ห่างไกล** ไม่ใช่คู่ pair programming ที่นั่งอยู่ข้างๆ ที่มาของแนวคิดนี้คือ [[claude-opus-4-7-migration-pachaar|Akshay Pachaar]] ซึ่งสังเกตว่าเมื่ออัปเกรดจาก 4.6 เป็น 4.7 ค่า token พุ่งสูงขึ้นเป็นเท่าตัวทั้งที่ใช้ prompt เหมือนเดิม ปัญหานี้ไม่ได้อยู่ที่ตัว model แต่อยู่ที่ **สไตล์การสื่อสาร**

## ทำไมสไตล์เดิมถึงไม่ได้ผล

บน 4.6, คุณสามารถแชทแบบสั้นๆ ไปมาได้สบายๆ — ถามสองคำ ตอบสองคำ แล้วค่อยเพิ่มข้อจำกัดทีหลังได้โดยไม่มีปัญหา

บน 4.7, ทุก user turn จะกระตุ้นให้เกิด reasoning รอบใหม่ ([[adaptive-thinking]]) model จะคิดอย่างลึกซึ้งทุกครั้งที่เราพิมพ์อะไรเข้าไป ไม่ว่า turn นั้นจะสมควรต้องคิดลึกหรือไม่ก็ตาม ดังนั้น เมื่อเราคุยเป็นรอบเล็กๆ หลายๆ turn จะทำให้เสีย token reasoning ไปซ้ำแล้วซ้ำเล่าโดยที่คุณภาพไม่ได้เพิ่มขึ้นตามสัดส่วน

พูดง่ายๆ คือ: **ต้นทุนต่อ user turn แพงขึ้น แต่คุณภาพต่อ turn ไม่ได้เพิ่มขึ้นตาม** หากยังคงเน้นการสื่อสารที่สั้นและบ่อยเหมือนเดิม จะทำให้ขาดทุนแน่นอน

## สามเทคนิคหลักที่ Pachaar แนะนำ

### 1) รวมทุกอย่างไว้ใน turn แรก

เขียน prompt เดียวที่ครอบคลุมทุกอย่าง:

-   **Intent** — สิ่งที่ต้องการจริงๆ
-   **Constraints** — ข้อจำกัด (เทคโนโลยี, สไตล์, performance)
-   **Acceptance criteria** — งานจะเสร็จเมื่อไหร่ถึงจะเรียกว่าผ่าน
-   **File paths** — ระบุไฟล์ที่เกี่ยวข้องให้ชัดเจน

prompt ที่สั้นและคลุมเครือแล้วค่อยๆ เติม context ในหลายๆ turn จะทำให้สิ้นเปลืองและคุณภาพงานลดลง

### 2) รวมคำถามเป็นชุด (Batch)

หากมี 3 คำถามที่เกี่ยวข้องกัน อย่าถามทีละข้อ ให้รวมเป็น message เดียว เพื่อให้ model มี context เพียงพอที่จะทำงานต่อได้เองโดยไม่ต้องคอยเช็คอินกับเราทุกขั้นตอน

### 3) ใช้ [[auto-mode|auto mode]] (Shift+Tab) สำหรับงานที่เชื่อถือได้

ใน [[claude-code|Claude Code]] มี [[auto-mode]] ซึ่งเป็น permission mode ที่มี classifier คั่นกลางเพื่ออนุมัติ action ที่ปลอดภัยและบล็อก action ที่เสี่ยงโดยอัตโนมัติ เหมาะสำหรับงาน long-running ที่เชื่อถือได้ ซึ่งจะช่วยลดการถามยืนยันที่ไม่จำเป็นและลด cycle time (ดูรายละเอียดและข้อจำกัดในหน้า concept)

นอกจากนี้ ยังสามารถให้ Claude แจ้งเตือนเมื่อทำงานเสร็จได้ (โดยมันจะสร้าง hook ขึ้นมาเอง) ทำให้เราไม่ต้องคอยเฝ้าหน้าจอ

**ผลลัพธ์:** reasoning overhead จะเกิดขึ้นเพียงครั้งเดียวที่ turn แรก และไม่เกิดขึ้นซ้ำในทุกๆ turn ถัดไป — ทำให้ต้นทุน token ลดลงและคุณภาพงานเพิ่มขึ้น เพราะ model ได้เห็นภาพรวมทั้งหมดตั้งแต่เริ่มต้น

## ความเชื่อมโยงกับแนวคิดอื่น

-   **[[instruction-budget]]** — Alex Ker เตือนว่าไม่ควรใส่ instruction เกินสองสามร้อยข้อ *Delegation mindset ไม่ขัดแย้งกับข้อนี้ — หมายถึงการใส่ context (ไฟล์, intent, criteria) ให้ครบถ้วน ไม่ใช่การใส่ rule เป็นร้อยๆ ข้อ*
-   **[[coding-harness]]** — R.P.I. framework (Role / Purpose / Instructions) เป็นวิธีการเขียน turn-1 ที่มีโครงสร้างและครบถ้วน
-   **[[ai-orchestrator]]** — บทบาทของ orchestrator คือ delegation mindset ที่ขยายสเกลขึ้นไปอีกระดับ: การสั่งให้ subagent/pipeline ทำงานแทนที่จะทำเอง
-   **[[harness-engineering]]** — Panutat มองว่า reviewer agent คือผู้รับมอบหมายงาน ไม่ใช่ให้คนไปรีวิวโดยตรง ซึ่งเป็นไปในทิศทางเดียวกัน

## เมื่อไหร่ที่ไม่ควรใช้เทคนิคนี้

-   งาน exploratory ที่ยังไม่แน่ใจว่าต้องการอะไร — การคุยเป็น turn ย่อยๆ อาจคุ้มค่ากว่า เพราะคำตอบในรอบแรกจะช่วยกำหนดคำถามในรอบถัดไป
-   Debugging ที่ต้องการ feedback แบบทันทีต่อ tool output
-   งานที่สั้นมากๆ และไม่ได้ใช้ reasoning นานอยู่แล้ว

## ที่มาของสำนวน

Pachaar: *"Treat Claude like a capable engineer you delegate to, not a pair programmer you guide line by line."* (คำพูดเดิมจาก source)

## Ball's org-level extension

[[thorsten-ball|Thorsten Ball]] ใน [[software-after-software]] ข้อ 3.5 ขยาย mindset เดียวกันในระดับองค์กร:

> "The unit of work becomes the delegated task, not the code to be written."

Pachaar เสนอ delegation ที่ระดับ prompt (วิธีเขียน turn-1 ให้ครบ); Ball เสนอ delegation ที่ระดับ work unit (สิ่งที่เราคิดว่าเป็น "งานหนึ่งชิ้น" คือ task ที่ส่งให้ agent ไม่ใช่ code ที่จะเขียนเอง) ทั้งสองมุมเสริมกัน — pattern ระดับ prompt เป็น atom; pattern ระดับ work unit เป็น molecule

ดูต่อที่ [[reorganize-around-models]] ซึ่งเป็น implication ระดับ org chart ของ Ball

## มอบงานให้ subagent ที่ถูกลง

[[fables-judgement-simon-willison|Simon Willison]] (2026-07) แสดง delegation อีกชั้น: สั่ง Claude Code ว่างาน coding ให้ **เลือก model ที่ถูกลงเองแล้วรันใน [[subagent-patterns|subagent]]**. main loop เก็บ judgment, review, และ synthesis ไว้; งานเขียน code จริงส่งให้ worker ที่ถูกกว่า (sonnet สำหรับงานจริงจัง, haiku สำหรับงานจิ๊บ ๆ) แล้วรีวิวผลก่อน commit. เป็น delegation mindset ที่ผสมกับ [[judgement-based-prompting]] — ให้ model ใช้ดุลพินิจเลือกทั้งว่างานไหนควรมอบ และมอบให้ model ตัวไหน.

## ดูเพิ่มเติม

- [[claude-opus-4-7]]
- [[claude-opus-4-7-migration-pachaar]]
- [[adaptive-thinking]]
- [[coding-harness]]
- [[instruction-budget]]
- [[ai-orchestrator]]
- [[harness-engineering]]
- [[software-after-software]]
- [[reorganize-around-models]]
- [[fables-judgement-simon-willison]]
- [[judgement-based-prompting]]
- [[subagent-patterns]]

