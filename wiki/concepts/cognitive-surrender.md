---
title: Cognitive Surrender
type: concept
tags: [ai, psychology, developer-experience, attention, code-review]
created: 2026-05-29
updated: 2026-05-29
sources: [The Orchestration Tax.md]
---

# Cognitive Surrender / การยอมแพ้ทางความคิด

**Cognitive Surrender** คือภาวะที่เรา **ยอมรับโค้ด (หรืองาน) ของ AI agent ทั้งที่ยังไม่ได้ตั้งความเห็นของตัวเอง** — ไม่ใช่เพราะมั่นใจว่ามันถูก แต่เพราะการจะคิดวิเคราะห์เองมันกินความสนใจที่เราไม่เหลือแล้ว เป็นคำที่ [[addy-osmani|Addy Osmani]] ใช้ (ลิงก์จากบล็อก [cognitive-surrender](https://addyosmani.com/blog/cognitive-surrender/) ของเขา) และยกมาเป็นหนึ่งในอาการของ [[orchestration-tax]] ในโพสต์ [[the-orchestration-tax]]

> you just accept the agent's code because forming your own opinion costs attention you don't have anymore
> (เรายอมรับโค้ดของ agent ไปเฉย ๆ เพราะการจะตั้งความเห็นของตัวเองกินความสนใจที่เราไม่เหลือแล้ว)

## มันเกิดยังไง

Cognitive surrender ไม่ได้เกิดจากความขี้เกียจ แต่เกิดจาก **attention หมด** พอเราเปิด agent หลายตัวเกินกว่าที่ review ไหว ([[orchestration-tax]]) สมองซึ่งเป็น serial resource ตัวเดียวก็ทำงานเกินกำลัง พอถึงจุดหนึ่งการ "ตั้งคำถามกับงานของ agent" มันแพงเกินกว่าจะจ่าย เราเลยเลือกทางที่ถูกกว่าในระยะสั้น — **ยอมรับมันไป**

ต่างจากการขี้เกียจตรงที่คนคนนั้นมัก *รู้สึกว่ายุ่งและทำงานหนัก* อยู่ด้วยซ้ำ (ดู busy ≠ productive ใน [[orchestration-tax]]) — มันคือการยอมแพ้ภายใต้ภาระ ไม่ใช่การเลี่ยงงาน

## ทำไมอันตราย

อันตรายเพราะมันมองไม่เห็นและสะสม:

- ทุกครั้งที่ยอมรับโดยไม่เข้าใจ เราสร้าง [[cognitive-debt]] — mental model ต่อโค้ดเบสค่อย ๆ เก่าและไม่ตรงจริง
- มันคือกลไกที่ระบบใช้ "อ้อม" คอขวดมนุษย์ ด้วยการ **แอบลดมาตรฐานของเราลงเงียบ ๆ** แทนที่จะเคารพว่าเรา review ได้แค่ไหน
- ไม่โผล่บน dashboard วันนี้ โผล่ตอน production พังแล้วพบว่าไม่รู้แล้วว่าระบบทำงานยังไง

## วิธีกัน

ตรงกับวิธีแก้ orchestration tax — โดยเฉพาะ:

- **Scale fleet to review rate** — อย่าเปิด agent เกินที่ review ได้จริง cognitive surrender คือสัญญาณว่าเปิดเยอะไป
- **Only spend the lock on judgement** — ให้ agent พิสูจน์ส่วนน่าเบื่อเอง (test/screenshot) เพื่อให้ attention ที่เหลือพอจะตั้งความเห็นกับ 20% ที่สำคัญ
- เทียบกับ [[acceptance-bottleneck]] ของ ChrisZa: การ "accept" งานต้องผูกกับความเข้าใจและความรับผิดชอบจริง — cognitive surrender คือ acceptance ที่ขาดสองอย่างนั้น

## ลูปยิ่งดี ยิ่งล่อให้ยอมแพ้

ใน [[loop-engineering]] Addy เตือนว่า cognitive surrender เป็นหนึ่งในสามอย่างที่ **คมขึ้น** เมื่อลูปดีขึ้น (อีกสองคือ verification ยังเป็นของเรา + comprehension debt). พอลูปรันเองไม่มีคนดู มันยั่วยวนให้เลิกมีความเห็นแล้วรับอะไรก็ตามที่มันคืนมา

> Designing the loop is the cure when you do it with judgement and the accelerant when you do it to avoid thinking — same action, opposite result.
> (ออกแบบลูปคือ *ยา* ถ้าทำด้วยวิจารณญาณ และเป็น *ตัวเร่ง* ถ้าทำเพื่อเลี่ยงการคิด — ทำเหมือนกันเป๊ะ ผลตรงข้าม)

## See also

- [[orchestration-tax]]
- [[the-orchestration-tax]]
- [[cognitive-debt]]
- [[acceptance-bottleneck]]
- [[care-allocation]]
- [[skill-atrophy]]
- [[loop-engineering]]
- [[addy-osmani]]
