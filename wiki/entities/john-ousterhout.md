---
title: John Ousterhout
type: entity
tags: [professor, computer-science, architecture, author]
created: 2026-05-09
updated: 2026-05-09
sources: [matt-pocock-software-fundamentals.md]
---

# John Ousterhout / จอห์น อูสเตอร์เฮาท์

**Role:** ศาสตราจารย์ด้านวิทยาการคอมพิวเตอร์ที่ Stanford University และผู้แต่งหนังสือ *A Philosophy of Software Design*

John Ousterhout เป็นบุคคลสำคัญที่มีอิทธิพลต่อแนวคิดการออกแบบซอฟต์แวร์สมัยใหม่ โดยเฉพาะในยุคที่ AI เข้ามามีบทบาทสำคัญในการเขียนโค้ด (ตามที่ [[matt-pocock]] นำมาอ้างถึง)

## แนวคิดหลัก
1. **[[deep-modules]]**: เสนอว่า module ที่ดีควรมี interface ที่เรียบง่าย (simple interface) แต่ซ่อนความสามารถที่ซับซ้อนไว้ข้างใน (deep functionality) เพื่อลดภาระทางความคิด (cognitive load) ของผู้ใช้
2. **Complexity is the Enemy**: นิยามความซับซ้อนว่าคืออะไรก็ตามที่ทำให้ระบบเข้าใจยากหรือแก้ไขยาก
3. **Information Hiding**: การซ่อนรายละเอียดการทำงานไว้เบื้องหลัง interface เพื่อให้การเปลี่ยนแปลงภายในไม่กระทบต่อภายนอก

## อิทธิพลต่อ AI Engineering
ในบริบทของ [[agentic-engineering]], แนวคิดของ Ousterhout ช่วยให้วิศวกรออกแบบระบบที่ "AI คุมได้" โดยการกำหนด interface ที่ชัดเจน (Deep Modules) และปล่อยให้ AI จัดการ implementation ภายในขอบเขตที่กำหนดไว้

## ดูเพิ่ม
- [[matt-pocock]]
- [[deep-modules]]
- [[software-architecture]]
