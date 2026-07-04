---
title: Clanker Slop
type: concept
tags: [ai, spam, open-source, critique]
created: 2026-04-28
updated: 2026-07-04
sources: [mario-zechner-pi-agent.md, building-pi-world-of-slop.md, code-isnt-free-mario-zechner-hard-truths-coding-ai.md]
---

# Clanker Slop / ขยะจากหุ่นยนต์

**Clanker Slop** เป็นคำแสลง (Slang) ที่ใช้เรียกเนื้อหา, โค้ด, หรือ Pull Request ที่สร้างโดย AI ปริมาณมหาศาลซึ่งมักจะมีคุณภาพต่ำ, ผิดพลาด หรือไม่ผ่านการตรวจสอบจากมนุษย์ (มักถูกใช้โดย [[mario-zechner]])

## ปัญหาใน Open Source

ในยุคที่ใครก็สั่งให้ AI เขียน code ได้ (เช่น ผ่าน OpenClaw หรือ [[claude-code]]), เจ้าของโปรเจกต์ Open Source ต้องเผชิญกับ:
- **PR Flooding**: การมีคนส่ง PR ที่ AI เขียนมาให้ตรวจวันละเป็นร้อยตัว
- **Vibe-coding Error**: โค้ดที่ดูเหมือนจะรันได้ (Vibe ดี) แต่ซ่อน bug หรือความซับซ้อนที่ไม่มีความจำเป็นไว้
- **Maintenance Burden**: ภาระในการตรวจงานที่ AI "พ่น" ออกมากลายเป็นภาระหนักของมนุษย์ที่เป็นเจ้าของโปรเจกต์
- **Attention Drain**: maintainer ต้องเสียเวลาคัดแยกว่า issue/PR ไหนมาจากคนจริงที่เข้าใจปัญหา และอันไหนเป็น output ที่ agent ยิงมาเฉยๆ

## วิธีแก้ (Human Verification)

เพื่อป้องกัน **Clanker Slop**, นักพัฒนาเริ่มใช้มาตรการรุนแรงขึ้น เช่น:
- **Whitelist/Vouch**: การอนุญาตเฉพาะคนที่เคยคุยกันในฐานะ "มนุษย์" ก่อนเท่านั้นถึงจะส่ง PR ได้
- **Auto-closing**: การปิด PR ทันทีถ้าตรวจสอบพบว่ามาจากเครื่องมือ AI โดยไม่ผ่านการตรวจสอบเบื้องต้น
- **Human Voice Gate**: ขอให้ผู้ส่งเขียน issue สั้นๆ ด้วยเสียงของตัวเองก่อน ถ้าดูเป็นมนุษย์จริงจึงค่อย vouch รอบถัดไป
- **OSS Vacation**: ปิด tracker ชั่วคราวเมื่อภาระเกินรับไหว เป็น social protocol เพื่อรักษา attention ของ maintainer ไม่ใช่แค่ technical filter

## Pi intake protocol

ใน [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]], [[mario-zechner|Mario]] ให้ตัวเลขจาก [[pi-agent|pi]]: จากยุคก่อน agent ที่โปรเจกต์ open source ใหญ่อาจได้ PR หนึ่งถึงสองอันต่อสัปดาห์ ตอนนี้เขาเจอ PR จาก clanker วันละ 50-60 อัน. หลาย PR มีคำอธิบายยาวมากและแก้ไฟล์ตั้งแต่ 10 ถึง 1,000 ไฟล์.

วิธีที่เขาใช้คือปิด PR โดยปริยาย แล้วให้คนเขียน issue สั้น ๆ ด้วยเสียงของตัวเองก่อน: ต้องบอกว่าจะทำอะไร ทำไปทำไม และเข้าใจ solution อย่างไร. ถ้าผ่าน เขาจะตอบว่า looks good และ workflow จะ whitelist account นั้นให้ส่ง PR ได้โดยไม่โดนปิดอัตโนมัติ.

เขายัง auto-close issue เพื่อคุม noise แล้วกลับมาอ่านจาก marker `last read` เปิดเฉพาะ issue ที่มีค่า. จาก 50 issue ล่าสุดที่เล่า มีแค่ 2 issue ที่รอดกลับมาเปิด.

**ผลคือ:** defense ที่ได้ผลไม่ใช่จับว่า text เขียนโดย AI หรือไม่ แต่คือพิสูจน์ว่ามีมนุษย์เข้าใจปัญหาอยู่หลัง diff.

## ดูเพิ่ม

- [[vibecoded-slop]] — แนวคิดเดียวกันในฝั่งซอฟต์แวร์
- [[vouch-oss]]
- [[alignment-bottleneck]]
- [[code-isnt-free-mario-zechner-hard-truths-coding-ai]]
