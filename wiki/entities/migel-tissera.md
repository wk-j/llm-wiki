---
title: Migel Tissera
type: entity
tags: [security, android, reverse-engineering, privacy]
created: 2026-07-16
updated: 2026-07-16
sources: [migel-tissera-x-android-behavioral-fingerprinting.md]
---

# Migel Tissera

Migel Tissera หรือ `@migtissera` คือผู้เขียน [[migel-tissera-x-android-behavioral-fingerprinting|thread วิเคราะห์แอป X บน Android]] ใน wiki นี้ เขารายงานว่าพบ SDK สองตัวซึ่งรองรับการเก็บ behavioral signal กว้างทั้ง process แต่ยัง inactive ใน session ที่เขาตรวจ

## สิ่งที่เขาเสนอใน thread

Tissera แยก permission ทั่วไปของ social app ออกจาก infrastructure สำหรับ [[behavioral-biometrics|behavioral biometrics]] เขาคาดว่าชุดหลังอาจเตรียมไว้กัน fraud ของ X Money/X Pay หรือใช้ตอน ID verification แต่ไม่ได้แสดงคำยืนยันจาก [[x-twitter|X]] ในข้อความที่ wiki ได้รับ

เขายังเผยแพร่ session log และชวนคนใช้ `apksaw` ซึ่งเขาอธิบายว่าเป็น MCP server สำหรับ [[mobile-app-reverse-engineering|reverse engineer แอป Android]] ด้วย coding agent. เพราะ thread ทำหน้าที่ทั้งรายงานและโปรโมตเครื่องมือ Claim ทางเทคนิคจึงควรตรวจซ้ำจาก APK/runtime trace อิสระ

**ผลคือ:** ใน wiki นี้ Tissera เป็นแหล่ง field report ไม่ใช่ผู้ยืนยันเจตนาหรือ production behavior ของ X

## ดูเพิ่ม

- [[migel-tissera-x-android-behavioral-fingerprinting]]
- [[behavioral-biometrics]]
- [[mobile-app-reverse-engineering]]
- [[x-twitter]]

