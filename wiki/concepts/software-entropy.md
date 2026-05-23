---
title: Software Entropy
type: concept
tags: [entropy, debt, complexity, pragprog]
created: 2026-05-09
updated: 2026-05-09
sources: [matt-pocock-software-fundamentals.md]
---

# Software Entropy / เอนโทรปีของซอฟต์แวร์

**Software Entropy** คือแนวคิดจากหนังสือ *The Pragmatic Programmer* ที่อธิบายถึงสภาวะที่ซอฟต์แวร์ค่อยๆ เสื่อมสภาพ ผุพัง และยากต่อการจัดการเมื่อเวลาผ่านไป หากไม่มีการควบคุมดูแลที่ดี

## แก่นความคิด
ในทางฟิสิกส์ Entropy คือการที่ระบบมุ่งไปสู่ความโกลาหล (Disorder) ในซอฟต์แวร์ก็เช่นกัน:
- ทุกครั้งที่มีการแก้ไขโค้ดโดยไม่คำนึงถึง "การออกแบบภาพรวม" (Design of the whole system) โครงสร้างซอฟต์แวร์จะแย่ลงเรื่อยๆ
- **"Broken Window Theory"**: ถ้ามีโค้ดแย่ๆ จุดหนึ่งถูกปล่อยทิ้งไว้ คนอื่น (หรือ AI) ก็จะเริ่มเขียนโค้ดแย่ๆ ตามจุดนั้น จนทั้งระบบพัง

## ความเสี่ยงในยุค AI
[[matt-pocock]] เตือนว่า AI สามารถเร่งสปีดของ Software Entropy ได้มหาศาล:
- **Specs-to-code trap**: การเขียนแค่ spec แล้วให้ AI ปั่นโค้ดออกมาโดยไม่เข้าไปตรวจทาน จะทำให้โค้ดกลายเป็นขยะ (Garbage) เร็วมาก
- **Outrunning your headlights**: การให้ AI เขียนโค้ดปริมาณมากเกินไปโดยไม่มี feedback loop (test/types) มาคอยคุม จะทำให้ entropy พุ่งสูงจนคุมไม่อยู่

## วิธีแก้
1. **Invest in Design Daily**: หมั่นดูแลโครงสร้างระบบทุกวัน ไม่ใช่แค่สั่ง AI ทำงานให้เสร็จไปทีละอย่าง
2. **Refactoring**: กล้าที่จะปรับปรุงโค้ดให้ดีขึ้นเสมอเมื่อเห็นจุดที่เริ่มผุพัง
3. **Deep Modules**: ใช้การวางโครงสร้างที่แข็งแรงเพื่อกักเก็บความซับซ้อนไว้ในที่ที่คุมได้

## ดูเพิ่ม
- [[cognitive-debt]]
- [[vibe-coding]]
- [[deep-modules]]
- [[matt-pocock]]
