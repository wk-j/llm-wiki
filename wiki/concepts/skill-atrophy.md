---
title: Skill Atrophy
type: concept
tags: [psychology, ai, learning]
created: 2026-05-05
updated: 2026-06-11
sources: [agentic-coding-trap.md, How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md]
---

# Skill Atrophy / ภาวะทักษะถดถอย

**Skill Atrophy** ในบริบทของ AI คือภาวะที่ทักษะการเขียนโปรแกรม การคิดเชิงวิพากษ์ (critical thinking) และการแก้ปัญหา (problem-solving) ของนักพัฒนาถดถอยลง เนื่องจากการปล่อยให้ AI Agent เป็นผู้คิดและลงมือทำแทนอยู่เป็นประจำ

นี่คือ **"The Supervision Paradox"** (ความย้อนแย้งของการคุมงาน) ที่บริษัทอย่าง Anthropic เตือนเอาไว้: การจะคุมและใช้งาน AI Agent ให้ได้ผลดีนั้นต้องอาศัยทักษะการเขียนโค้ดและ critical thinking ขั้นสูง แต่ทักษะเหล่านี้กลับเป็นสิ่งที่จะถดถอยลงเมื่อเราใช้งาน AI Agent มากเกินไป

[[lars-faye]] ชี้ให้เห็นว่าการเรียนรู้ของโปรแกรมเมอร์นั้นต้องอาศัย "ความยากลำบาก" (friction) การอ่านรีวิวโค้ดอย่างเดียวให้ผลแค่ 50% ของการเรียนรู้ เมื่อเราตัดความยากในการแก้บั๊กและการเขียนโค้ดด้วยตัวเองออกไป ทักษะการสร้าง mental model และ [[eh-gland]] ก็จะค่อยๆ หายไปตามด้วย ภาวะนี้สามารถเกิดขึ้นได้อย่างรวดเร็วในเวลาเพียงไม่กี่เดือน

## เส้นแบ่งสำหรับคนที่กำลังเรียน

ในช่วงถามตอบของ [[how-to-keep-shipping-away-from-desk|talk ของ Zack Proser]], คนฟังถามตรง ๆ ว่าวิธี delegate งานให้ agent จะทำให้คนต้นอาชีพเสียโอกาสฝึกหรือไม่. คำตอบของ [[zack-proser|Zack Proser]] คือ **อย่าใช้ AI ทำสิ่งที่เรายังทำเองไม่เป็น**.

นี่ไม่ใช่กฎห้ามใช้ AI ตอนเรียน. ใช้ agent ช่วยถามว่า mental model ตรงไหนยังมัว, ให้มัน quiz, หรือช่วยพาเรียนลึกขึ้นได้. แต่เรื่องที่กำลังสร้างพื้นฐานควรยังลงมือเขียน แก้ bug และเจอความเจ็บด้วยตัวเองก่อน. พอมีประสบการณ์พอจะจับ hallucination และ design แย่ได้แล้ว ค่อย delegate เพื่อเพิ่มความเร็ว.

**ได้อะไร:** ใช้ AI เร่งการเรียนโดยไม่ยกการสร้าง judgement ให้ AI ไปด้วย.

## See also

- [[cognitive-debt]]
- [[taste-paradox]]
- [[agentic-engineering]]
- [[developer-balance]]
- [[how-to-keep-shipping-away-from-desk]]
