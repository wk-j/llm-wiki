---
title: Programming Process Matters
type: concept
tags: [ai, programming, world-models, software-quality]
created: 2026-07-03
updated: 2026-08-25
sources: [eternal-sloptember.md, state-of-technology-and-joy-of-making-phoomparin-mano.md]
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

## จุดที่ไม่ลงรอยกับ harness-first

wiki นี้มีสาย harness-first หลายหน้า เช่น [[coding-harness]], [[harness-engineering]], และ [[harness-guides-sensors]]. หน้านี้ไม่ได้ลบ claim เหล่านั้น. มันเพิ่มข้อทักว่า harness อาจช่วยคุม output ได้มาก แต่ถ้า process ข้างในยังไม่เข้าใจโลกจริง ก็ต้องมี verifier และ human judgement หนุนอยู่ดี

เปิดคำถามไว้: world model จะเกิดจาก model architecture ใหม่, memory/context ที่ดีขึ้น, harness ที่บังคับ interaction กับโลกจริง, หรือการรวมหลายอย่างเข้าด้วยกัน

## Process มีคุณค่ามากกว่าความถูกต้อง

[[phoomparin-mano|Phoomparin Mano]] เพิ่มอีกแกนใน [[state-of-technology-and-joy-of-making-phoomparin-mano|State of Technology and the Joy of Making]]. ต่อให้ agent workflow สร้าง software ที่ใช้งานได้ process ก็ยังเป็นที่ที่คนสะสม mastery, curiosity, taste และ [[creative-ownership|creative ownership]].

นี่ต่างจากข้อวิจารณ์เรื่อง world model. ข้อวิจารณ์เดิมถามว่า agent เข้าใจระบบจริงพอให้ output ถูกหรือไม่. Phoomparin ถามว่า ถ้า output ถูกแล้ว แต่คนไม่ได้สนุกกับการลองและตัดสินใจด้วยตัวเอง เราเสียคุณค่าอะไรไปบ้าง.

สองคำถามต้องอยู่พร้อมกัน. อย่าโรแมนติไซส์ process ที่ช้าและผิดเพียงเพราะคนทำเอง. แต่อย่าใช้ test ผ่านลบคุณค่าด้านการเรียนรู้กับความหมายที่ test วัดไม่ได้.

**ผลคือ:** process มีทั้ง instrumental value คือช่วยให้งานถูก และ intrinsic value คือทำให้คนเรียนรู้และรู้สึกว่างานเป็นของตัวเอง.

## See also

- [[quality-proxy-collapse]]
- [[world-models]]
- [[behavioral-verifier]]
- [[coding-harness]]
- [[agentic-coding-trap]]
- [[state-of-technology-and-joy-of-making-phoomparin-mano]]
- [[creative-ownership]]
