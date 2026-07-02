---
title: Ubiquitous Language
type: concept
tags: [ddd, ai-alignment, communication, vocabulary]
created: 2026-05-09
updated: 2026-07-02
sources: [matt-pocock-software-fundamentals.md, zoran-horvat-domain-model-persistence.md]
---

# Ubiquitous Language / ภาษาที่ใช้ร่วมกันทุกที่

**Ubiquitous Language** เป็นแนวคิดจาก Domain-Driven Design (DDD) โดย Eric Evans ที่ [[matt-pocock]] นำมาประยุกต์ใช้เพื่อเป็นสะพานเชื่อมระหว่าง "มนุษย์" กับ "AI" ในการพัฒนาซอฟต์แวร์

## แก่นความคิด
คือการสร้าง "ชุดคำศัพท์กลาง" ที่ทุกคน (Domain expert, Developer, AI) ใช้เหมือนกันเป๊ะๆ ทั้งในบทสนทนา ในเอกสาร และในตัวโค้ด

- **ในบริบท AI**: มันคือ markdown file ที่รวบรวมคำศัพท์ (Glossary) ของโปรเจกต์ไว้เป็นตาราง เพื่อให้ AI เข้าใจว่าคำแต่ละคำใน code base นี้หมายถึงอะไรกันแน่
- **Ubiquitous Language Skill**: Skill ที่ Pocock สร้างขึ้นเพื่อ scan code base แล้วสร้าง markdown file นี้ออกมาโดยอัตโนมัติ

## ทำไมถึงสำคัญ
1. **ลดความเยิ่นเย้อ (Less verbose)**: เมื่อ AI เข้าใจศัพท์เฉพาะทางตรงกับเรา มันก็ไม่จำเป็นต้องอธิบายซ้ำซากหรือใช้คำฟุ่มเฟือย
2. **Alignment**: มั่นใจได้ว่า implementation ที่ AI เขียนจะใช้ชื่อตัวแปรหรือโครงสร้างที่ตรงตามโดเมนของธุรกิจจริงๆ
3. **ลดกำแพงภาษา (Language Gap)**: แก้ปัญหาเวลาที่ domain expert พูดอย่าง แต่โปรแกรมเมอร์ (หรือ AI) เข้าใจไปอีกอย่าง

## ผลคือ (Payoff)
ทำให้การคิด (Thinking trace) ของ AI มีประสิทธิภาพมากขึ้น และลดโอกาสที่ AI จะ hallucinate หรือสร้างศัพท์ใหม่ที่ไม่อยู่ในสารบบของระบบเดิม

## มุม Domain Model

โพสต์ของ [[zoran-horvat|Zoran Horvat]] เพิ่มมุมที่ใกล้ DDD ดั้งเดิมกว่า: ภาษากลางไม่ควรอยู่แค่ใน glossary หรือ prompt แต่ควรอยู่ใน type ของระบบด้วย. ถ้าธุรกิจมี `Money`, `Currency`, `OrderId`, หรือ `UtcTimestamp` code ก็ควรมี concept เหล่านี้เป็น [[value-objects|value objects]] หรือ type ที่ enforce rule ได้.

ตรงนี้ทำให้ [[ubiquitous-language|Ubiquitous Language]] เชื่อมกับ [[domain-model-persistence-separation]] โดยตรง. Database อาจเก็บเป็น column primitive ได้ แต่ domain model ควรยังพูดภาษาของปัญหา ไม่ใช่ภาษาของ schema อย่างเดียว.

## ดูเพิ่ม
- [[matt-pocock]]
- [[zoran-horvat]]
- [[domain-modeling]]
- [[domain-model-persistence-separation]]
- [[value-objects]]
- [[domain-to-ai-translator]]
- [[grill-me]]
