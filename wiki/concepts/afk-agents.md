---
title: AFK Agents (Away From Keyboard)
type: concept
tags: [ai, agents, afk, workflow, parallelism, automation]
created: 2026-06-21
updated: 2026-06-21
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md"]
---

# AFK Agents / ทำงานแบบไม่ต้องนั่งเฝ้า

**AFK (away from keyboard) คือการโยนงานที่ scope ชัดแล้วให้ agent ไปทำเองโดยเราไม่ต้องนั่งกดอนุมัติทีละขั้น — ตรงข้ามกับงานแบบ human-in-the-loop ที่เราต้องอยู่กับ agent ตลอด.** [[matt-pocock|Matt Pocock]] บอกว่านี่คือจุดเปลี่ยนที่ทำให้เขาผลิตงานได้เยอะขึ้นมหาศาล

## งานสองแบบ

Matt แยกงานกับ agent เป็นสองแบบ:

- **Human-in-the-loop** — เราอยู่กับ agent คุยกันไปมา เหมาะกับ **planning**, งานซับซ้อน, และงานที่ยัง **unscoped** (ยังไม่รู้ขอบเขตชัด) ต้องค่อย ๆ figure out ด้วยกัน
- **AFK** — งานที่ **scope แล้ว** โยนให้ agent ไปทำเอง ไม่ต้องนั่งเฝ้า ไม่ต้องคอยตอบ permission request

> "The moment that I discovered AFK was the moment I really got into AI coding and the moment I was really able to massively increase my output."
> (วินาทีที่ผมค้นพบ AFK คือวินาทีที่ผมเอาจริงกับ AI coding และเริ่มเพิ่ม output ได้มหาศาล)

## ทำไมถึงพลิกเกม

พอเราถอนตัวออกจากลูป (ไม่ต้องคอยกดอนุมัติ คอยตอบคำถาม) ก็เหมือนมี **"เรา" หลายคนทำงานขนานกัน** — สอง สาม สี่ ห้าตัว วิ่งผลิตโค้ดพร้อมกัน แล้วเราค่อยมา review ทีหลัง. นี่คือสิ่งที่ปลดล็อก parallelism จริง ๆ ไม่ใช่แค่เร่ง agent ตัวเดียวให้เร็วขึ้น

เงื่อนไขสำคัญคือ **งานต้อง scope ชัด** ก่อน. งานที่ยัง unscoped ควรอยู่ในโหมด human-in-the-loop จนกว่าจะ scope ได้ — แล้วค่อยส่งเข้า AFK. ตรงนี้เชื่อมกับ [[grill-me]] (ใช้ซักให้เข้าใจตรงกันก่อน) และ [[queues-over-loops]] (scope งานบนคิวก่อน agent หยิบไปทำ)

## ทำ AFK ยังไง (setup ของ Matt)

- ใช้ [[sandcastle|Sandcastle]] รัน agent ใน sandbox (Docker/Podman) — กันไม่ให้ agent ทำพังเครื่อง (ลบ home dir, exfiltrate env var)
- รันบน **GitHub Actions** — agent หยิบ issue ที่ติด label ไปทำ, เปิด PR, มี review agent ตรวจ
- ใช้ Vercel sandboxes หรือ remote VM เพื่อ parallelize นอกเครื่องตัวเอง แล้ว pull commit กลับ local

> ได้อะไร: AFK ทำให้ throughput ไม่ผูกกับเวลาที่เรานั่งเฝ้าหน้าจอ — แต่เพดานใหม่กลายเป็น **review bandwidth** ของเราแทน (ดู [[orchestration-tax]])

## เทียบกับเรื่องอื่น

- **[[orchestration-tax]]** — AFK เพิ่มของให้ผลิต แต่ปิดลูป (review + merge) ยังต้องผ่านคนคนเดียว → ยิ่ง AFK เยอะ ยิ่งต้องระวัง orchestration tax
- **[[developer-balance]]** — [[zack-proser|Zack Proser]] ก็พูดเรื่อง AFK / steer แบบไม่ต้องเฝ้าโต๊ะเหมือนกัน; ประเด็นร่วมคือรักษา judgement และสุขภาพไว้ ไม่ใช่กลายเป็นงาน always-on
- **[[long-running-agents]]** — AFK agent ที่รันนานต้องการ durable state / checkpoint

## ดูเพิ่ม

- [[queues-over-loops]]
- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[sandcastle]]
- [[orchestration-tax]]
- [[developer-balance]]
- [[loop-engineering]]
- [[long-running-agents]]
