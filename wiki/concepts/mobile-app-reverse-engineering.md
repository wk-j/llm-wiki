---
title: Mobile App Reverse Engineering
type: concept
tags: [security, mobile, android, static-analysis, dynamic-analysis]
created: 2026-07-16
updated: 2026-07-16
sources: [migel-tissera-x-android-behavioral-fingerprinting.md]
---

# Mobile App Reverse Engineering / แกะแอปมือถือเพื่อดูพฤติกรรมจริง

Mobile app reverse engineering คือการตรวจแอปที่ build เสร็จแล้วเพื่อดูว่าข้างในมี code, SDK, permission, config และ runtime behavior อะไรบ้าง งาน privacy ใช้วิธีนี้ตรวจช่องว่างระหว่างสิ่งที่ UI/policy บอกกับสิ่งที่ตัว app ทำได้จริง

ใน [[migel-tissera-x-android-behavioral-fingerprinting|thread ของ Migel Tissera]] ผู้เขียนบอกว่าใช้วิธีนี้กับ X Android แล้วพบ SDK สองตัวที่รองรับ [[behavioral-biometrics|behavioral biometrics]] เขายังชวนใช้ `apksaw` ซึ่งอธิบายว่าเป็น MCP server ให้ coding agent ช่วยวิเคราะห์โทรศัพท์ Android ด้วยภาษาธรรมชาติ

## Static บอกว่า “ทำได้” Dynamic บอกว่า “ทำอยู่”

การอ่าน APK/decompiled code เป็น static analysis. มันช่วยหา class, listener, `ContentObserver`, sensor access, identifier และ feature flag แต่ code ที่อยู่ใน binary อาจเป็นของเก่า ถูกปิดด้วย remote config หรือเปิดเฉพาะบาง account/region

Dynamic analysis รัน app จริงแล้วดู log, hook, file access, sensor registration และ network traffic. วิธีนี้ตอบได้ดีขึ้นว่า path ไหน active แต่ผลจากเครื่องเดียวก็ยังไม่ครอบคลุม rollout ทั้งหมด

หลักฐานที่แข็งแรงจึงต่อกันเป็นสาย:

`APK version/hash → code path → activation condition → runtime event → network/storage destination → server-side use`

ถ้าขาดช่วงใด ควรระบุว่าข้อสรุปหยุดอยู่ตรงไหน

**ได้อะไร:** การพบ code ไม่ใช่หลักฐานว่า feature เปิดอยู่ และการไม่เห็น event ใน session เดียวก็ไม่ใช่หลักฐานว่าไม่มีใครได้รับ feature

## Coding agent ช่วยตรงไหน

Agent ช่วยค้น class ข้าม package, สรุป data flow, เขียน hook, เทียบ version และจัด session log ได้เร็วขึ้น แต่ agent ไม่แทน provenance. รายงานที่ตรวจซ้ำได้ยังต้องบอก app version, artifact hash, command/hook, output ดิบ และเงื่อนไข account/device

Natural-language interface ทำให้คนเริ่ม audit ง่ายขึ้น ขณะเดียวกันมันอาจสรุปเกินหลักฐานหรือเรียก API ผิด ถ้าไม่มี trace ที่คนย้อนดูได้ งาน security จึงต้องเก็บ artifact และขั้นตอนจริงไว้ข้างคำอธิบายของ agent

**ผลคือ:** agent ลดแรงแกะ code แต่ความน่าเชื่อถือยังมาจากหลักฐานที่ทำซ้ำได้ ไม่ใช่ความลื่นของบทสรุป

## ข้อจำกัดที่พบบ่อย

- obfuscation ทำให้ชื่อ class/method ไม่บอกเจตนา
- third-party SDK อาจมี capability กว้าง แต่ host app เปิดใช้เพียงบางส่วน
- remote config และ server response เปลี่ยน behavior โดยไม่เปลี่ยน APK
- emulator, root และ instrumentation ทำให้ app เลือก path ต่างจากเครื่องผู้ใช้จริง
- certificate pinning หรือ encrypted payload ทำให้เห็น network destination แต่ไม่เห็นข้อมูลข้างใน
- legal/ethical boundary ต่างกันตาม app, account และเขตอำนาจ ควรทดสอบเฉพาะระบบ/ข้อมูลที่มีสิทธิ์

## คำถามที่ยังเปิดอยู่

- จะเผยแพร่รายละเอียดแค่ไหนให้ตรวจซ้ำได้โดยไม่ช่วย abuse
- จะพิสูจน์ activation condition ที่ขึ้นกับ server โดยไม่เข้าถึง backend อย่างไร
- เมื่อ SDK เป็นของ third party ใครรับผิดชอบอธิบาย data flow: vendor หรือเจ้าของ app
- agent-generated finding ควรผ่าน human review และ independent reproduction ระดับไหนก่อนเผยแพร่

## ดูเพิ่ม

- [[migel-tissera]]
- [[behavioral-biometrics]]
- [[x-twitter]]

