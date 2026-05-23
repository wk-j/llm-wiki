---
title: Deep Modules
type: concept
tags: [architecture, design-patterns, complexity, ousterhout]
created: 2026-05-09
updated: 2026-05-09
sources: [matt-pocock-software-fundamentals.md]
---

# Deep Modules / โมดูลแบบลึก

**Deep Modules** เป็นแนวคิดการออกแบบซอฟต์แวร์จากหนังสือ *A Philosophy of Software Design* โดย [[john-ousterhout]] ซึ่งได้รับความสนใจอย่างมากในยุค [[agentic-engineering]] เพราะเป็นโครงสร้างที่เอื้อต่อการทำงานร่วมกับ AI

## แก่นความคิด
โมดูลที่ดีควรมี **"Interface ที่เรียบง่าย แต่ซ่อนความสามารถที่ซับซ้อนไว้ข้างใน"**

- **Simple Interface**: ช่องทางการติดต่อสื่อสารจากภายนอกมีน้อยและชัดเจน (เช่น function call ไม่กี่ตัว)
- **Deep Functionality**: ข้างในโมดูลจัดการงานที่ซับซ้อนไว้มากมายโดยที่คนใช้ไม่ต้องรู้รายละเอียด (Information Hiding)
- **ตรงข้ามกับ Shallow Modules**: โมดูลที่ interface ซับซ้อนแต่ทำงานได้นิดเดียว (เช่นมี function เยอะแยะที่ต้องเรียกตามลำดับถึงจะทำงานได้)

## ทำไมถึงสำคัญในยุค AI
1. **Design the Interface, Delegate the Implementation**: มนุษย์สามารถทำหน้าที่ออกแบบ Interface (ตัวครอบข้างนอก) ให้ดีที่สุด แล้วปล่อยให้ AI เขียน Implementation (ไส้ใน) ได้อย่างอิสระ
2. **ลดภาระทางความคิด (Cognitive Load)**: มนุษย์ไม่ต้องจำรายละเอียดข้างในโมดูลทั้งหมด มองโมดูลเป็น "Gray Box" ที่ทดสอบได้จากข้างนอก
3. **AI Friendly**: AI มักจะสับสนเมื่อต้องเดินทางผ่านโมดูลเล็กๆ จำนวนมาก (Shallow modules) ที่เกี่ยวพันกันมั่วไปหมด แต่ถ้าเป็น Deep module ที่มีขอบเขตชัดเจน AI จะทำงานได้แม่นยำกว่า

## ผลคือ (Payoff)
ช่วยให้ระบบมี **Testability** สูง เพราะเราสามารถเขียน test ครอบที่ Interface ของโมดูลได้เลย ทำให้เรากล้าปล่อยให้ AI แก้ไขโค้ดข้างในโมดูลโดยไม่ต้องกลัวว่าจะทำระบบพัง (ถ้า test ยังผ่าน)

## ดูเพิ่ม
- [[john-ousterhout]]
- [[matt-pocock]]
- [[software-architecture]]
- [[verifiability]]
