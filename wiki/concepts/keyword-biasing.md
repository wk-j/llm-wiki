---
title: Keyword Biasing
type: concept
tags: [asr, prompting, speech, transcription]
created: 2026-05-09
updated: 2026-05-09
sources: [granite-4-1-fastest-asr.md]
---

# Keyword Biasing / การเอียง model ให้จำคำเฉพาะ

Keyword biasing คือการส่งรายชื่อคำสำคัญให้ ASR model ก่อนหรือระหว่าง transcribe เพื่อให้ model มีโอกาสเลือกคำนั้นมากขึ้น

ตัวอย่างคำที่มักต้อง bias:

- ชื่อคน
- ชื่อบริษัท
- acronym
- product name
- technical term
- spelling พิเศษ

ใน [[granite-4-1-fastest-asr|Granite 4.1 - The Fastest ASR?]], [[sam-witteveen|Sam Witteveen]] บอกว่านี่เป็นจุดที่ [[granite-speech|Granite Speech]] 4.1 2B base น่าสนใจมาก เพราะ transcript งานจริงมักพังตรงคำเฉพาะ ไม่ใช่คำสามัญ

## ทำไมสำคัญ

ASR model อาจฟังประโยคทั่วไปได้ดี แต่พอเจอชื่อเฉพาะ เช่นชื่อ host, library, model, acronym หรือคำใน domain แคบๆ มันเดาผิดได้ง่าย

ถ้า transcript ผิดตรงคำเฉพาะ ต่อให้ WER รวมดูดี ผู้ใช้ก็ยังรู้สึกว่า transcript ใช้ไม่ได้ เพราะคำที่สำคัญที่สุดผิด

ได้อะไร: keyword biasing เปลี่ยน ASR จาก “ฟังทั่วไปได้ดี” เป็น “ฟังงานของเราดีขึ้น”

## Trade-off ใน Granite Speech 4.1

ใน Granite Speech 4.1:

- รุ่น base มี keyword biasing
- รุ่น NAR ไม่มี keyword biasing เพราะเน้น throughput ดิบ
- สำหรับ long-form audio ต้องคิดว่าจะส่ง keyword list อย่างไรในแต่ละ chunk

ตรงนี้ทำให้ keyword biasing เป็นทั้ง model feature และ pipeline design problem ถ้า chunk ยาวหลายชั่วโมง ต้องมีวิธีส่งคำเฉพาะให้ถูกจังหวะ

## See also

- [[automatic-speech-recognition]]
- [[granite-speech]]
- [[non-autoregressive-asr]]
- [[granite-4-1-fastest-asr]]
