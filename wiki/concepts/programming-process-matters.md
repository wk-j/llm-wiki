---
title: Programming Process Matters
type: concept
tags: [ai, programming, world-models, software-quality]
created: 2026-07-03
updated: 2026-07-03
sources: [eternal-sloptember.md]
---

# Programming Process Matters / วิธีคิดตอนเขียนโปรแกรมสำคัญ

Programming Process Matters คือข้อโต้แย้งว่า programming ไม่ใช่แค่การผลิตข้อความ code ที่หน้าตาเหมือน code. สิ่งสำคัญคือ process ที่สร้าง code: เข้าใจระบบ, model ผลกระทบ, เห็น constraint, ตัดสิน tradeoff, แล้วรับผิดชอบตอนมันพัง

## ต่างจาก “model ยังไม่เก่งพอ”

ใน [[eternal-sloptember|The Eternal Sloptember]] ผู้เขียนไม่ได้บอกแค่ว่า coding agents รุ่นนี้ยัง polish ไม่ดี. เขาบอกว่าปัญหาอาจอยู่ที่ชนิดของ model: LLM mimic distribution ของ programming ได้ แต่ยังไม่มี process แบบคนที่เข้าใจระบบจริง

ถ้าข้อวิจารณ์นี้ถูก การเพิ่ม benchmark score หรือ RLVR อย่างเดียวอาจทำให้ output ดูถูกขึ้น แต่ไม่จำเป็นต้องทำให้ agent เข้าใจ programming มากขึ้น

## world model สำคัญตรงไหน

ผู้เขียนบอกว่า real programming agents ต้องมี world models. ในบริบทนี้ world model หมายถึง model ภายในที่เข้าใจว่า code เปลี่ยนแล้วระบบจริงจะเปลี่ยนอย่างไร ไม่ใช่แค่เดา token ถัดไปหรือหาวิธีผ่าน test

ตัวอย่างเชิง software:

- รู้ว่า change นี้กระทบ invariant ไหน
- รู้ว่า test ผ่านเพราะ behavior ถูก ไม่ใช่เพราะ test ถูกทำให้อ่อนลง
- รู้ว่า abstraction ใหม่จะทำให้ maintainer เข้าใจง่ายขึ้นหรือยากขึ้น
- รู้ว่า failure mode จริงอยู่ตรงไหน แม้ prompt ไม่ได้บอก

## ความตึงกับ harness-first

wiki นี้มีสาย harness-first หลายหน้า เช่น [[coding-harness]], [[harness-engineering]], และ [[harness-guides-sensors]]. หน้านี้ไม่ได้ลบ claim เหล่านั้น. มันเพิ่มข้อทักว่า harness อาจช่วยคุม output ได้มาก แต่ถ้า process ข้างในยังไม่เข้าใจโลกจริง ก็ต้องมี verifier และ human judgement หนุนอยู่ดี

เปิดคำถามไว้: world model จะเกิดจาก model architecture ใหม่, memory/context ที่ดีขึ้น, harness ที่บังคับ interaction กับโลกจริง, หรือการรวมหลายอย่างเข้าด้วยกัน

## See also

- [[quality-proxy-collapse]]
- [[world-models]]
- [[behavioral-verifier]]
- [[coding-harness]]
- [[agentic-coding-trap]]
