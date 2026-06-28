---
title: Strategic vs Tactical Programming
type: concept
tags: [software-engineering, ai-coding, ousterhout, delegation, skills]
created: 2026-06-21
updated: 2026-06-21
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md", matt-pocock-software-fundamentals.md]
---

# Strategic vs Tactical Programming / โปรแกรมเชิงยุทธศาสตร์ vs เชิงยุทธวิธี

**[[matt-pocock|Matt Pocock]] ยืมแนวคิดจาก John Ousterhout (*A Philosophy of Software Design*) มาอธิบายว่า AI ได้กิน "tactical programming" ไปหมดแล้ว — งานที่เหลือให้คนคือ "strategic programming".** แนวคิดนี้เป็นแกนกลางของวิธีคิดที่ Matt พูดซ้ำหลายครั้ง (ทั้งในคลิป Software Fundamentals และพอดแคสต์กับ [[david-ondrej|David Ondrej]] 2026-06-19)

## สองระดับ

- **Tactical programming** = งานหน้างานรายวัน — เขียนโค้ดจริง, ยุ่งกับ syntax, ไล่ bug ที่โผล่มา, ทำ commit. "ชนะการรบ"
- **Strategic programming** = คิดยาว, มองภาพรวม — codebase ควรเป็นยังไง, จะเพิ่ม velocity ของทีมยังไง, ทำมากขึ้นด้วยของน้อยลงยังไง. "ชนะสงคราม ไม่ใช่แค่การรบ" เป็นเหมือนแม่ทัพที่นั่งอยู่บนสุด

## AI กิน tactical ไปแล้ว

> "AI has basically eaten tactical programming. It's gone... AI is just better at doing tactical programming than you are because it can do it for cheaper."
> (AI กินงาน tactical ไปหมดแล้ว... เพราะมันทำได้ถูกกว่าและเก่งกว่าเรา)

ผลคือเราต้องเก่ง **strategic** เพื่อรีดประโยชน์จาก "กองทัพ tactical programmer ไม่จำกัดจำนวน" ที่เพิ่งได้มา. Matt มองว่าจริง ๆ แล้ว strategic programming **ไม่ได้เปลี่ยนไปเพราะ AI เลย** — เดิมเรา delegate งานให้ junior/mid-level dev วันนี้แค่เปลี่ยนเป็น delegate ให้ AI. หลัก delegation เดิมยังใช้ได้หมด:

- ออกแบบส่วนที่ยากไว้ก่อน (design the hard parts up front)
- scope งานให้ชัดมาก ๆ
- คิดเรื่อง interface ระหว่าง module
- เขียน test scenario และ test ที่ดี
- ทำ doc แค่พอชี้ทางให้ AI ไปแก้ตรงที่ควรแก้

## ทักษะของเราคือเพดานของ AI

ข้อสรุปที่ Matt ย้ำบ่อย: **"your skills are the ceiling on what AI can do."** AI มี context ให้ทำงานเท่ากับที่เราป้อนให้ — ถ้าทักษะเราต่ำ AI ก็ไปไม่เกินนั้น

- AI ทำให้ **senior dev เก่งขึ้น ~10 เท่า** แต่ junior ได้ boost แค่นิดเดียว → "ไม่ค่อยคุ้มจะจ้าง junior เยอะ ๆ อีกแล้ว"
- "Getting good with AI is really about getting good at your domain" — เก่ง AI = เก่งในโดเมนของตัวเอง
- คนที่ยังเป็นแค่ tactical programmer ก้มหน้าทำงาน — "you can't be a code monkey anymore"

(หมายเหตุ: นี่เป็น claim เชิง opinion ของคนสอน dev; กระแสตรงข้ามก็มี เช่นมุมว่า junior ที่ embrace AI เต็มที่ก็ได้ alpha สูง — Matt เองก็ยอมว่า enthusiasm beats experience ในแง่ output)

## เชื่อมกับเรื่องอื่น

- **[[agent-experience]]** — strategic programming ที่ดีสร้าง codebase ที่ AX ดี
- **[[loop-engineering]] / [[queues-over-loops]]** — การออกแบบลูป/คิวคืองาน strategic ส่วน agent ทำ tactical ในนั้น
- **[[code-is-free]]** — ถ้า tactical (เขียนโค้ด) แทบฟรี ของที่หายากคือ judgement เชิง strategic
- **[[orchestration-tax]]** — คน strategic คือ serial bottleneck; งาน tactical ขนานได้แทบไม่จำกัด

## ดูเพิ่ม

- [[matt-pocock]]
- [[matt-pocock-software-fundamentals]]
- [[matt-pocock-agentic-workflow]]
- [[john-ousterhout]]
- [[agent-experience]]
- [[knowledge-skills-wisdom]]
- [[code-is-free]]
- [[orchestration-tax]]
