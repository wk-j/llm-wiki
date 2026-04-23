---
title: Taste Paradox
type: concept
tags: [ai, education, skills, judgment, coding-agent, curriculum]
created: 2026-04-18
updated: 2026-04-18
sources: [llm-era-computer-engineering-nattee.md]
---

# Taste Paradox / ปัญหา taste ในยุค Agent

Loop ที่ขัดแย้งในตัวเอง: **Coding Agent ทำให้คนข้ามขั้นตอนฝึกมือได้ — แต่ขั้นตอนฝึกมือนั่นแหละคือสิ่งที่สร้าง judgment (ต่อมเอ๊ะ) ในการคุม Agent** เสนอโดย [[nattee-niparnan|Nattee Niparnan]] ใน Ep. 2 ของซีรีส์ *วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง* (2026-04-17)

> "Agent ทำให้เราข้ามขั้นตอนฝึกมือได้ แต่ขั้นตอนฝึกมือนั่นแหละที่สร้าง judgment ให้เราคุม Agent ได้ มันวนเป็นลูป" — Nattee

## รูปแบบของ loop

```
(อยาก) review Agent ได้ดี
    ↓ ต้อง
เคยทำเอง / มี taste / มีต่อมเอ๊ะ
    ↓ ต้อง
เคย "ฝึกมือ" งานชนิดนั้นมาก่อน
    ↓ แต่
Agent ทำให้ข้ามการฝึกมือได้
    ↑
return ... (กลับไปต้นทาง)
```

## Case แบบรูปธรรม (Nattee, PoC Web App, $140)

Nattee จับ bug เรื่อง authorization ได้ (Buyer ลบ resource ของ Seller ได้ แม้ทุก endpoint ผ่าน unit test) **เพราะเคยเขียน auth เอง** — รู้ว่าควรเอ๊ะตรงไหน, test ต่อยังไง

คำถามของ Nattee: ถ้าเป็นคนที่ **ไม่เคยเขียน auth เอง** เคยแต่สั่ง Agent ทำ → จะรู้ได้ยังไงว่าตรงไหนควรเอ๊ะ?

นี่ไม่ใช่ skill gap ชั่วคราว — เป็น pattern ที่เกิดกับทุกโดเมน: DB transaction, race condition, caching invalidation, security headers, permission model — ทุกอันที่คนเคยหัดจน "รู้ถึงกระดูก" ผ่านการเจ็บตัวเอง

## "ใช้ Agent เป็น" vs "review Agent เป็น"

Nattee แยกสอง skill ออกจากกัน:

| Skill | สอนยากแค่ไหน | วิธีสอน |
|---|---|---|
| **ใช้ Agent เป็น** | ง่าย | ยัดใน 1–2 วิชาก็พอ — command / prompt / workflow |
| **review Agent เป็น** (มีต่อมเอ๊ะ) | ยากมาก | ต้องฝึกมือมาก่อน — แต่ Agent ก็ "ประหยัดเวลา" ด้วยการให้ข้ามขั้นนั้นพอดี |

ปมอยู่ที่ข้อที่สอง — เป็นสิ่งที่หลักสูตรยัง "คิดไม่ตก"

## คำถามหลักสูตรที่ยังตอบไม่ได้

Nattee สรุปเป็นคำถามเดียว: *"นิสิตต้องฝึกมือลึกแค่ไหนถึงจะพอ?"*

- ฝึกทุกเรื่องลึกเหมือนเดิม → ไม่ make sense เมื่อ Agent ทำแทนได้จริง
- ไม่ฝึกเลย → ไม่มีทางมี taste ที่จะคุม Agent ได้
- ฝึกแค่บางเรื่อง → จะเลือกยังไงว่า *เรื่องไหน* คือ anchor ของ taste

คำถามที่เกี่ยวเนื่อง: *Dijkstra paradox* จาก Ep. 1 — *"ต้องรู้ไหมว่าเมื่อไรจะใช้ Dijkstra?"* ถ้าไม่เคยเรียน แล้ว LLM เลือกผิด นิสิตจะรู้ได้ยังไงว่ามันผิด — เป็น taste paradox เวอร์ชันของทฤษฎี algorithm

## ความสัมพันธ์กับ [[harness-engineering]] (Panutat) — คนละ layer ของปัญหาเดียวกัน

Panutat และ Nattee เห็นปัญหาเดียวกัน (การ review งาน Agent ทำมือไม่ไหว) แต่มองคนละจุด:

| | Panutat ([[harness-engineering]]) | Nattee (taste paradox) |
|---|---|---|
| **จุดที่โฟกัส** | *scope* ของการ review | *origin* ของคนที่มา review |
| **ปัญหาที่ยก** | คนรู้น้อยกว่า Agent — ตรวจ library choice ไม่ทัน | คนจะมี taste ได้ไง ถ้า Agent ให้ข้ามการฝึกมือ |
| **คำตอบที่เสนอ** | ใช้ agent อีกหลายตัวเป็น harness | ยังตอบไม่ได้ — *"คิดมาเป็นปีแล้วก็ยังคิดไม่ตก"* |
| **หน่วยของคำตอบ** | ออกแบบระบบ (technology) | ออกแบบหลักสูตร (pedagogy) |

ไม่ขัดกัน — **Harness เป็นคำตอบ *เชิงระบบ* ของ "คนตรวจไม่ทัน"; Taste paradox คือคำถาม *เชิงพัฒนาคน* ของ "คนจะกลายเป็น reviewer ได้ยังไง"** จะสร้าง harness ที่ดีได้ ก็ยังต้องมีคนที่มี taste มา *ออกแบบ* harness อยู่ดี

## ทำไม framework นี้สำคัญ

- **ชัดเจนกว่า "AI replaces jobs" แบบทั่วไป** — ไม่ได้พูดว่างานหายไป แต่พูดว่า *ขั้นตอนการเรียนรู้* ของงานที่ไม่หายไปกลับเข้าถึงยาก
- **เชื่อม [[engineering-role-shift]] ให้ครบ** — เดิมบอกว่างาน review ขยายตัว แต่ไม่ได้บอกว่า reviewer ต้องมาจากไหน; taste paradox เติมช่องว่างนี้
- **ใช้ได้ข้ามโดเมน** — Andrew Price ใน [[judgement-vs-automation]] พูดถึง taste ในงานศิลป์ (lighting, layout, narrative); Nattee พูดถึง taste ในงานวิศวะ (authorization, algorithm choice, systemic concerns) — คือประเด็นเดียวกัน

## Open questions

ข้อสังเกตจากฝั่ง wiki ที่ต่อยอดจากข้อเสนอของ Nattee:

- **Depth threshold** — มี "ฝึกมือขั้นต่ำ" หรือไม่? เช่น ฝึกจน debug ด้วยตัวเองเป็นแล้วค่อยให้ใช้ Agent?
- **Anchor domain** — ถ้าเลือกฝึกลึกบางเรื่อง จะเลือกยังไง? Systems? Security? Data? หรือเลือกตามความสนใจ (แต่เสี่ยงขาด taste ในโดเมนที่ไม่ได้เลือก)
- **Fading skill** — engineer senior ที่ปล่อยให้ Agent เขียนนานพอ taste จะ atrophy ไหม? "use it or lose it" ใช้กับ judgment ด้วยหรือเปล่า
- **Harness สอน taste ได้ไหม** — ถ้า harness agent ชี้จุดที่ผิดให้เห็นเป็นประจำ junior จะ *เรียน* ผ่าน harness จนเกิด taste ได้ไหม, หรือจะแค่ไว้ใจ harness โดยไม่เกิด taste เอง (เหมือน GPS กับคนที่ไม่เคย navigate ด้วยแผนที่)

## ฝั่งคู่กัน: เมื่อ *มี* taste แล้วเลือก model ยังไง

[[somkiat-khitwongwattana|Somkiat Khitwongwattana]] ([[model-choice-by-expertise]]) เสนอฝั่งตรงข้ามของคำถาม: สมมุติว่ามี taste แล้ว (Domain Expert ลงโค้ดเอง) — ใช้แค่ Claude Sonnet 4.5 ก็พอสำหรับงานส่วนใหญ่ model ใหม่จำเป็นก็ต่อเมื่อคน vibe-code โดยไม่มี knowledge และต้องการให้ model ชดเชย taste ที่ขาด taste paradox ตอบว่า *taste มาจากไหน*; Somkiat ตอบว่า *เมื่อมีแล้วใช้อย่างไรให้คุ้ม*

## See also

- [[nattee-niparnan]]
- [[llm-era-computer-engineering-nattee]]
- [[harness-engineering]]
- [[panutat-tejasen]]
- [[engineering-role-shift]]
- [[judgement-vs-automation]]
- [[llm-coding-pitfalls]]
- [[ai-orchestrator]]
- [[model-choice-by-expertise]]
