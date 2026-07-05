---
title: Value Maxing
type: concept
tags: [ai, economics, models, agents, codex]
created: 2026-07-05
updated: 2026-07-05
sources: [piyalitt-codex-keynote-attention-not-token.md]
---

# Value Maxing / รีดคุณค่า ไม่ใช่ token

**Value maxing** คือแนวคิดจากทีม [[openai-codex|Codex]] ที่ keynote [[ai-engineer-worlds-fair|AI Engineer World's Fair]] (สรุปใน [[piyalitt-codex-keynote-attention-not-token]]). พอ agent เริ่มมีประโยชน์แบบก้าวกระโดด คำถามถัดไปไม่ใช่ “จะใช้ token ให้เยอะที่สุดได้อย่างไร” แต่คือ **จะรีดคุณค่าออกมาอย่างไร** ให้ฉลาดขึ้น ถูกลง และเร็วขึ้นพร้อมกัน

[[alexander-embiricos|Alexander Embiricos]] เล่าว่าเวลาคุยกับผู้บริหาร engineering ประเด็นมักวนอยู่รอบเรื่องนี้. มันต่างจาก [[tokenmaxxing|tokenmaxxing]] ที่เน้นใช้ token ให้เยอะโดยยังไม่ตอบว่า ROI คุ้มจริงไหม

## แกนที่หนึ่ง: คุ้มค่า (intelligence per dollar)

ทุกคนอยากได้ความฉลาดระดับ frontier **และ** อยากได้ความฉลาดต่อเงินให้มากที่สุด. ตัวอย่างที่ keynote ยกยังเป็นข้อมูลผ่านแหล่งรอง จึงควร source-attributed จนกว่าจะตรวจจาก OpenAI โดยตรง:

| Model | Claim บนเวที |
|---|---|
| **GPT-5.6 Terra** | ความฉลาดระดับ [[gpt-5-5\|GPT-5.5]] ในราคาครึ่งเดียว |
| **Luna** | ชนะ model ดังหลายตัว ราคา $1/1M input, $6/1M output |
| รุ่นบนสุดตระกูล 5.6 | ขึ้นนำ Terminal Bench (ตามกราฟบนเวที) |

**ผลคือ:** การเลือก model ไม่ใช่แค่ “แพงสุด = ดีสุด” แต่ต้องจับคู่งานกับจุด sweet spot ระหว่างคุณภาพ ราคา และความเร็ว

## แกนที่สอง: ความเร็ว (latency unlocks new workflows)

GPT-5.3 Codex Spark เคยพิสูจน์แล้วว่าความเร็วปลดล็อก workflow ใหม่ได้ แต่ผู้ใช้ก็ไม่อยากแลกความฉลาดทิ้งไป. ใน keynote รอบนี้ ทีมโชว์ frontier ของตระกูล 5.6 ที่รันบน **Cerebras** ด้วยความเร็ว **750 token/วินาที** (ตามโพสต์คือจะเปิดใช้เดือนถัดไป)

ภาพเปรียบเทียบคือได้ PR ขนาดใหญ่ในราว 10 วินาที. ประเด็นไม่ใช่แค่คำตอบเดียวเร็วขึ้น แต่คือสิ่งที่ความเร็วระดับนั้นทำให้เป็นไปได้ เช่น ปล่อย agent ลอง **5–6 แนวทางขนาน** แล้วคัดอันที่ดีที่สุด ในเวลาน้อยกว่าที่เมื่อก่อนใช้สร้างคำตอบเดียว

ความรู้สึกจึงเปลี่ยนจาก “นั่งรอ AI ตอบ” เป็น “เพื่อนร่วมงานโชว์ผลลัพธ์ไปพร้อมกับที่มันทำ”

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
