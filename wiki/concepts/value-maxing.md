---
title: Value Maxing
type: concept
tags: [ai, economics, models, agents, codex]
created: 2026-07-05
updated: 2026-07-05
sources: [piyalitt-codex-keynote-attention-not-token.md]
---

# Value Maxing / รีดคุณค่า ไม่ใช่ token

**Value maxing** คือแนวคิดจากทีม [[openai-codex|Codex]] ที่ keynote [[ai-engineer-worlds-fair|AI Engineer World's Fair]] (สรุปใน [[piyalitt-codex-keynote-attention-not-token]]): เมื่อ agent มีประโยชน์แบบก้าวกระโดด คำถามถัดไปไม่ใช่ "ใช้ token เยอะที่สุด" แต่คือ **จะรีดคุณค่าออกมาอย่างไร** — ฉลาดขึ้น ถูกลง และเร็วขึ้น**พร้อมกัน**

[[alexander-embiricos|Alexander Embiricos]] เล่าว่าบทสนทนากับผู้บริหาร engineering ส่วนใหญ่วนอยู่รอบเรื่องนี้. ต่างจาก [[tokenmaxxing|tokenmaxxing]] ที่เน้นปริมาณการใช้ token โดยไม่นับ ROI

## แกนที่หนึ่ง: คุ้มค่า (intelligence per dollar)

ทุกคนอยากได้ความฉลาดระดับ frontier **และ** ปริมาณความฉลาดต่อเงินสูงสุด. ตัวอย่างที่ keynote ยก (ยัง source-attributed จนกว่าจะตรวจจาก OpenAI โดยตรง):

| Model | Claim บนเวที |
|---|---|
| **GPT-5.6 Terra** | ความฉลาดระดับ [[gpt-5-5\|GPT-5.5]] ในราคาครึ่งเดียว |
| **Luna** | ชนะ model ดังหลายตัว ราคา $1/1M input, $6/1M output |
| รุ่นบนสุดตระกูล 5.6 | ขึ้นนำ Terminal Bench (ตามกราฟบนเวที) |

**ผลคือ:** การเลือก model ไม่ใช่แค่ "แพงสุด = ดีสุด" แต่เป็นการจับคู่งานกับจุด sweet spot บนกราฟ คุณภาพ/ราคา

## แกนที่สอง: ความเร็ว (latency unlocks new workflows)

GPT-5.3 Codex Spark เคยพิสูจน์ว่าความเร็วปลดล็อก workflow ใหม่ แต่ผู้ใช้ไม่อยากแลกความฉลาด. รอบ keynote นี้ทีมโชว์ frontier ของตระกูล 5.6 รันบน **Cerebras** ที่ **750 token/วินาที** (เปิดใช้เดือนถัดไป ตามโพสต์)

ภาพเปรียบเทียบ: ได้ PR ขนาดใหญ่ใน ~10 วินาที. ประเด็นไม่ใช่แค่คำตอบเดียวเร็วขึ้น แต่คือสิ่งที่ความเร็วระดับนั้นเปิดทางให้ทำ — เช่น ปล่อย agent ลอง **5–6 แนวทางขนาน** แล้วคัดอันดี ในเวลาน้อยกว่าที่เมื่อก่อนใช้สร้างคำตอบเดียว

ความรู้สึจึงเปลี่ยนจาก "นั่งรอ AI ตอบ" เป็น "เพื่อนร่วมงานโชว์ผลลัพธ์ไปพร้อมกับที่มันทำ"

## ความตึงกับ wiki อื่น

- [[ai-token-economics]] / [[enterprise-ai-roi]] — value maxing เป็นมุมฝั่ง vendor ที่พยายามตอบ CFO ว่า "แพงขึ้นแต่คุ้ม" ไม่ใช่แค่ "ใช้เยอะขึ้น"
- [[code-is-free]] — implementation ถูกลงได้ แต่ token bill ยังต้องนับ; value maxing ไม่ได้แปลว่า usage ฟรี
- [[orchestration-tax]] — ความเร็วช่วยลองหลายทางได้ แต่คนยังต้องตัดสินใจ merge งานที่ชนะ — attention ยังเป็นคอขวด

## See also

- [[piyalitt-codex-keynote-attention-not-token]]
- [[tokenmaxxing]]
- [[ai-token-economics]]
- [[openai-codex]]
- [[gpt-5-6-sol]]
