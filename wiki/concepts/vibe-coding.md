---
title: Vibe Coding
type: concept
tags: [ai, coding, automation, karpathy]
created: 2026-04-30
updated: 2026-08-15
sources: [Andrej Karpathy From Vibe Coding to Agentic Engineering.md, andrew-ng-ai-engineering-skills-map.md]
---

# Vibe Coding / การเขียนโปรแกรมตามอารมณ์

**Vibe Coding** เป็นคำที่บัญญัติโดย [[andrej-karpathy]] เพื่ออธิบายสภาวะที่มนุษย์เขียนโปรแกรมโดยการสื่อสารทิศทาง ความต้องการ และ "vibe" ให้กับ AI แล้วให้ AI เป็นคนจัดการ implementation ทั้งหมด โดยที่มนุษย์แทบไม่ต้องแตะต้องโค้ดเลย

## แก่นความคิด
หัวใจของ Vibe Coding คือการ "raising the floor" (ยกระดับพื้นฐาน) ทำให้ใครก็ตามที่มีไอเดียสามารถสร้างซอฟต์แวร์ได้โดยไม่ต้องมีความรู้ด้าน syntax เชิงลึก มนุษย์ทำหน้าที่เป็นผู้ตรวจทานและปรับจูนความรู้สึกของผลลัพธ์ (Iterative vibing)

- **Input**: Natural language, screenshots, abstract goals.
- **Output**: Functional code blocks.
- **Payoff**: ลดแรงต้านในการเริ่มต้นโปรเจกต์ (Zero to One) ได้อย่างมหาศาล

## ความแตกต่างระหว่าง Vibe Coding กับ Agentic Engineering
ในมุมมองของ Karpathy (2026):
- **Vibe Coding** คือการเน้นความเร็วและการเข้าถึง (Accessibility) เหมาะสำหรับ side projects หรือการพิสูจน์ไอเดีย
- **[[agentic-engineering]]** คือการนำ vibe coding มาทำให้เป็นระเบียบวินัยทางวิศวกรรม เพื่อรักษาคุณภาพและสเกลในระดับ professional

## ทำไมถึงสำคัญ
Vibe Coding เปลี่ยนความสัมพันธ์ระหว่างโปรแกรมเมอร์กับคอมพิวเตอร์ จาก "ผู้สั่งการระดับ micro" (Micro-manager) เป็น "ผู้กำกับ" (Director) ที่เน้นไปที่ผลลัพธ์และความสวยงามมากกว่ารายละเอียดทางเทคนิค

## ความเสี่ยงและการควบคุม
แม้ Vibe Coding จะช่วยให้เริ่มต้นได้เร็ว แต่ [[matt-pocock]] เตือนว่าหากทำโดยขาดพื้นฐานวิศวกรรม (Software Fundamentals) จะนำไปสู่สภาวะ "Outrunning your headlights" หรือการขับรถเร็วกว่าไฟหน้า คือ AI เขียนโค้ดเร็วเกินกว่าที่เราจะตรวจสอบความถูกต้องได้ทัน นำไปสู่ [[software-entropy]] ในที่สุด

## Ng: ปัญหาไม่ใช่การ vibe code แต่คือการไม่รู้ว่ากำลังแลกอะไร

[[andrew-ng|Andrew Ng]] อธิบายกลไกของความเสี่ยงนี้ไว้ชัดใน [[ai-engineering-skills-map|AI Engineering Skills Map]]:

> "It also leads to much better outcomes than those for an inexperienced developer who vibe codes a solution without knowing the tradeoffs their coding agent is making — which will often be poor ones, because they don't know what context to give their coding agent."

ประเด็นคือ **coding agent ตัดสินใจแลกอะไรกับอะไรอยู่ตลอดเวลา** — เลือก library, เลือกโครงสร้างข้อมูล, เลือกว่าจะ optimize ความเร็วหรือความอ่านง่าย คนที่ไม่มีพื้นฐานไม่ได้แค่ตรวจไม่ออกว่า agent เลือกอะไร แต่ **ไม่รู้ว่าต้องป้อน context อะไรให้มันตั้งแต่แรก** ผลที่ได้จึงมักเป็นตัวเลือกที่ไม่ดี

Ng เลยจัด software engineering fundamentals เป็นทักษะแยกอีกหนึ่งข้อ โดยให้เหตุผลว่าพื้นฐานคือ "ภาษาที่แม่นยำ" ที่ใช้ steer agent ตรงนี้เสริมคำเตือน "outrunning your headlights" ของ [[matt-pocock]] ข้างบนด้วยสาเหตุที่ต่างมุมเล็กน้อย — Pocock เน้นว่าตรวจไม่ทัน ส่วน Ng เน้นว่าสั่งไม่เป็น

**ผลคือ:** vibe coding ไม่ได้แย่ในตัวมันเอง สิ่งที่ทำให้ผลลัพธ์ต่างกันคือคนสั่งรู้หรือไม่รู้ว่ามี tradeoff อะไรวางอยู่บนโต๊ะ

## ดูเพิ่ม
- [[agentic-engineering]]
- [[software-3-0]]
- [[andrej-karpathy]]
- [[ai-engineering-skills-map]]
- [[andrew-ng]]
- [[vibecoded-slop]] — เมื่อ vibe coding ขาดการตรวจสอบคุณภาพ
- [[matt-pocock-software-fundamentals]] — มุมมองที่เน้นย้ำถึงความสำคัญของพื้นฐานซอฟต์แวร์ในยุค AI
