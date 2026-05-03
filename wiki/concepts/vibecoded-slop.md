---
title: Vibecoded Slop
type: concept
tags: [software-quality, ai, critique]
created: 2026-04-28
updated: 2026-05-03
sources: [maggie-appleton-collaborative-ai-engineering.md, building-pi-world-of-slop.md]
---

# Vibecoded Slop / ขยะที่สร้างด้วยความรู้สึก (โดยไร้การออกแบบ)

**Vibecoded Slop** คือคำเรียกซอฟต์แวร์หรือฟีเจอร์ที่ถูกสร้างขึ้นอย่างรวดเร็วโดยใช้ AI Agent ตามคำสั่งที่กว้างๆ หรือ "Vibe" ของผู้สั่ง โดยขาดการออกแบบที่รัดกุม (Craftsmanship) และขาดการคิดเชิงวิพากษ์ (Critical Thinking)

## ที่มาของคำ

คำนี้ถูกใช้โดย [[maggie-appleton]] เพื่อเตือนถึงอันตรายของการที่ Agent ทำงานเร็วเกินไปจนคนเลิก "คิด" และเลิก "วางแผน" ผลลัพธ์ที่ได้คือซอฟต์แวร์ที่มีปริมาณมากแต่คุณภาพต่ำ ใช้งานยาก หรือไม่ตอบโจทย์จริงๆ

## ลักษณะของ Vibecoded Slop

- **Surface-level Features**: มีฟีเจอร์เยอะแต่ใช้งานจริงได้ไม่ดี หรือขาดการเก็บรายละเอียด (edge cases)
- **Bloated Codebase**: โค้ดที่งอกออกมาอย่างรวดเร็วโดยไม่มีโครงสร้างที่ยั่งยืน
- **Lack of Intent**: สร้างขึ้นเพียงเพราะว่า "มันสร้างได้ง่าย" ไม่ใช่เพราะว่า "มันควรจะมี"
- **Compound Complexity**: agent เพิ่ม abstraction, duplication, compatibility layer, และ defensive code ได้เร็วมาก ถ้ามนุษย์ไม่อ่านทัน ความซับซ้อนจะสะสมเป็น system risk

## วิธีป้องกัน

การจะก้าวข้าม Vibecoded Slop ต้องอาศัยการรักษา **Craftsmanship** (งานฝีมือ) ซึ่งในยุค AI หมายถึงการใช้เวลาที่ประหยัดได้จากการเขียน code ไปทุ่มเทให้กับการวางแผน, การวิจัยผู้ใช้ (User Research), และการทบทวนสถาปัตยกรรมให้ลึกซึ้งยิ่งขึ้น

[[mario-zechner|Mario Zechner]] เสริมมุมที่ practical กว่านั้น: งาน critical ต้องอ่านทุกบรรทัด เพราะการอ่านคือ friction ที่สร้าง mental model ในหัวมนุษย์ ถ้าคนไม่อ่าน codebase เลย ตอน production พัง ทั้งคนและ agent จะไม่มี context พอจะแก้ปัญหาใหญ่ได้

## ดูเพิ่ม

- [[stop-slop-concept]] — แนวคิดคล้ายกันแต่เน้นที่สไตล์การเขียนของ AI
- [[clanker-slop]] — คำเรียกขยะหรือ spam ที่สร้างโดย AI ในวงการ Open Source
- [[alignment-bottleneck]] — คอขวดที่นำไปสู่การสร้าง Slop
- [[collaborative-ai-engineering]]
