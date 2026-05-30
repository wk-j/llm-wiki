---
title: System in Messages Array
type: concept
tags: [ai, claude, api, prompt-caching, agents, anthropic]
created: 2026-05-29
updated: 2026-05-29
sources: [Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md]
---

# System in Messages Array / ใส่ system ใน array ของ messages

ฟีเจอร์ Claude Messages API ที่เปิดตัวพร้อม [[claude-opus-4-8|Opus 4.8]] — ตอนนี้ใส่ `system` (คำสั่งระบบ) เข้าไป **ใน array ของ `messages`** ได้แล้ว ไม่ใช่แค่ใน field `system` ก้อนเดียวตอนต้น

## ปัญหาที่มันแก้

เดิมที agent ที่รันยาวๆ ถ้าอยากอัปเดตคำสั่งกลางคัน — เช่นเปลี่ยนสิทธิ์ที่ทำได้ ปรับงบ token หรืออัปเดตข้อมูล environment — ทำได้ลำบาก สองทางเลือกเดิมต่างก็มีข้อเสีย:

- ยัดข้อมูลใหม่แฝงเข้าไปใน **user turn** — ผิดธรรมชาติ เพราะมันไม่ใช่คำพูดของ user จริง
- แก้ `system` ก้อนต้น — แต่ทำแบบนั้น **prompt cache พัง** ทั้งก้อน ([[compaction|cache]] ที่สะสมไว้ใช้ไม่ได้) ต้องจ่ายค่า process context ใหม่หมด

## วิธีใหม่

ใส่ `system` เป็น item หนึ่งใน array `messages` ระหว่างทาง — developer เลย **อัปเดตคำสั่งให้ Claude กลางงานได้โดยไม่พัง prompt cache** และไม่ต้องเนียนผ่าน user turn ตัวอย่างการใช้:

- อัปเดต **สิทธิ์การใช้งาน** (permissions) ที่ agent ทำได้ระหว่างที่มันกำลังรัน
- ปรับ **งบ token** (token budget) กลางคัน
- ป้อน **ข้อมูล environment** ใหม่ที่เพิ่งเปลี่ยน

**ผลคือ:** loop ของ agent ที่รันยาวปรับเงื่อนไขกลางทางได้แบบลื่นๆ โดยไม่เสียทั้งเงิน (cache) และไม่เสียความสะอาดของบทสนทนา

## ทำไมสำคัญกับธีมของวิกินี้

- ต่อเนื่องกับข้อสังเกตใน [[claude-opus-4-7|Opus 4.7]] ที่ว่า "ทุก user turn กระตุ้นให้เกิด reasoning เปลือง token" และคำแนะนำให้ [[delegation-mindset|อัด context ทั้งหมดไว้ turn แรก]] — ฟีเจอร์นี้เปิดทางสายกลาง คืออัปเดตได้กลางคันโดยไม่ต้องเปิด user turn ใหม่
- เป็นชิ้นส่วนที่เข้ากับงาน agent รันยาวอย่าง [[dynamic-workflows|dynamic workflows]] และ [[long-running-agents]] ที่เงื่อนไข (สิทธิ์ / งบ) อาจต้องเปลี่ยนระหว่างทาง

## ดูเพิ่ม

- [[claude-opus-4-8]]
- [[dynamic-workflows]]
- [[delegation-mindset]]
- [[long-running-agents]]
- [[piyalitt-opus-4-8-recap]]
