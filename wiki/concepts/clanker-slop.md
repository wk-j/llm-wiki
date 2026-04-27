---
title: Clanker Slop
type: concept
tags: [ai, spam, open-source, critique]
created: 2026-04-28
updated: 2026-04-28
sources: [mario-zechner-pi-agent.md]
---

# Clanker Slop / ขยะจากหุ่นยนต์

**Clanker Slop** เป็นคำแสลง (Slang) ที่ใช้เรียกเนื้อหา, โค้ด, หรือ Pull Request ที่สร้างโดย AI ปริมาณมหาศาลซึ่งมักจะมีคุณภาพต่ำ, ผิดพลาด หรือไม่ผ่านการตรวจสอบจากมนุษย์ (มักถูกใช้โดย [[mario-zechner]])

## ปัญหาใน Open Source

ในยุคที่ใครก็สั่งให้ AI เขียน code ได้ (เช่น ผ่าน OpenClaw หรือ [[claude-code]]), เจ้าของโปรเจกต์ Open Source ต้องเผชิญกับ:
- **PR Flooding**: การมีคนส่ง PR ที่ AI เขียนมาให้ตรวจวันละเป็นร้อยตัว
- **Vibe-coding Error**: โค้ดที่ดูเหมือนจะรันได้ (Vibe ดี) แต่ซ่อน bug หรือความซับซ้อนที่ไม่มีความจำเป็นไว้
- **Maintenance Burden**: ภาระในการตรวจงานที่ AI "พ่น" ออกมากลายเป็นภาระหนักของมนุษย์ที่เป็นเจ้าของโปรเจกต์

## วิธีแก้ (Human Verification)

เพื่อป้องกัน **Clanker Slop**, นักพัฒนาเริ่มใช้มาตรการรุนแรงขึ้น เช่น:
- **Whitelist/Vouch**: การอนุญาตเฉพาะคนที่เคยคุยกันในฐานะ "มนุษย์" ก่อนเท่านั้นถึงจะส่ง PR ได้
- **Auto-closing**: การปิด PR ทันทีถ้าตรวจสอบพบว่ามาจากเครื่องมือ AI โดยไม่ผ่านการตรวจสอบเบื้องต้น

## ดูเพิ่ม

- [[vibecoded-slop]] — แนวคิดเดียวกันในฝั่งซอฟต์แวร์
- [[vouch-oss]]
- [[alignment-bottleneck]]
