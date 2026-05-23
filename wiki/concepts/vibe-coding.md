---
title: Vibe Coding
type: concept
tags: [ai, coding, automation, karpathy]
created: 2026-04-30
updated: 2026-04-30
sources: [Andrej Karpathy From Vibe Coding to Agentic Engineering.md]
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

## ดูเพิ่ม
- [[agentic-engineering]]
- [[software-3-0]]
- [[andrej-karpathy]]
- [[vibecoded-slop]] — เมื่อ vibe coding ขาดการตรวจสอบคุณภาพ
- [[matt-pocock-software-fundamentals]] — มุมมองที่เน้นย้ำถึงความสำคัญของพื้นฐานซอฟต์แวร์ในยุค AI
