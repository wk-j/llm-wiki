---
title: X (Twitter)
type: entity
tags: [social-media, mobile, android, privacy, fintech]
created: 2026-07-16
updated: 2026-07-16
sources: [migel-tissera-x-android-behavioral-fingerprinting.md]
---

# X (Twitter) / เอ็กซ์

X คือ social platform ที่เดิมชื่อ Twitter. ใน [[migel-tissera-x-android-behavioral-fingerprinting|field report ของ Migel Tissera]] ประเด็นอยู่ที่แอป Android ไม่ใช่ตัวเว็บไซต์หรือ platform ทุก client

Tissera รายงานว่า APK มี SDK สองตัวสำหรับเก็บจังหวะพิมพ์ clipboard event การแตะหน้าจอ event รูปใหม่ใน gallery motion sensor และ device identifier. เขาบอกว่าชุดนี้ยัง inactive บนเครื่องที่ตรวจ จึงพิสูจน์ได้เพียง capability ที่มีอยู่กับ observation จาก session เดียว ไม่ใช่ rollout ต่อผู้ใช้ทั้งหมด

ผู้เขียนคาดว่า X อาจเตรียมระบบไว้ทำ anti-fraud ของ X Money/X Pay หรือ ID verification. Wiki เก็บการโยงนี้เป็นสมมติฐาน เพราะข้อความที่ได้รับไม่มีเอกสารหรือคำยืนยันจาก X

**ผลคือ:** เวลาพูดถึง X ในเรื่องนี้ ต้องระบุทั้ง platform (`Android app`), สถานะ (`inactive ใน session ของผู้เขียน`) และระดับหลักฐาน (`reverse-engineering field report`)

## ดูเพิ่ม

- [[migel-tissera]]
- [[behavioral-biometrics]]
- [[mobile-app-reverse-engineering]]

