---
title: Automatic Speech Recognition (ASR)
type: concept
tags: [speech, ai, transcription, audio, models]
created: 2026-05-09
updated: 2026-09-07
sources: [granite-4-1-fastest-asr.md, dhh-strategies-programming-with-ai-agents-lex-clips.md]
---

# Automatic Speech Recognition (ASR) / การแปลงเสียงพูดเป็นข้อความ

Automatic Speech Recognition หรือ **ASR** คืองานให้ model ฟังเสียงพูดแล้วสร้างข้อความออกมา เช่น transcript ประชุม, podcast, lecture, call center, subtitle

ใน source [[granite-4-1-fastest-asr|Granite 4.1 - The Fastest ASR?]] ตัวอย่างหลักคือ [[granite-speech|Granite Speech]] 4.1 จาก [[ibm|IBM]] ซึ่งแยก ASR ออกเป็นหลาย variant ตามสิ่งที่งานต้องการจริง

## สิ่งที่ต้องวัด

ASR ไม่ได้วัดแค่ “ฟังถูกไหม” อย่างเดียว งานจริงมีหลายแกน:

- **[[word-error-rate|WER]]** — คำผิดกี่เปอร์เซ็นต์ ยิ่งต่ำยิ่งดี
- **RTFX / Real-Time Factor** — compute 1 วินาทีประมวลผลเสียงได้กี่วินาที
- **language support** — รองรับภาษาอะไรบ้าง
- **translation** — แปลเสียงจากภาษาออกไปอีกภาษาด้วยไหม
- **punctuation / true casing** — เติมจุด comma ตัวพิมพ์ใหญ่เล็กให้ใช้อ่านต่อได้ไหม
- **[[keyword-biasing|keyword biasing]]** — บอกชื่อเฉพาะ acronym หรือศัพท์เฉพาะให้ model เอียงไปทางคำเหล่านั้นได้ไหม
- **[[speaker-attributed-asr|speaker attribution]]** — รู้ไหมว่า speaker ไหนพูดคำไหน
- **word-level timestamp** — แต่ละคำจบที่เวลาไหน

ได้อะไร: การเลือก ASR model ต้องเริ่มจาก downstream workflow ไม่ใช่ดู benchmark ตัวเดียว

## Autoregressive กับ non-autoregressive

ASR transformer จำนวนมากทำงานแบบ autoregressive คือ generate token ทีละตัว token ถัดไปขึ้นกับ token ก่อนหน้า วิธีนี้แม่น แต่ decoding เป็นลำดับ ทำให้ speed ติดเพดาน

[[non-autoregressive-asr|Non-autoregressive ASR]] พยายามแก้ด้วยการทำงานขนานมากขึ้น ใน Granite Speech 4.1 2B NAR, IBM ใช้วิธี draft transcript ก่อน แล้วให้ model แก้ transcript นั้นแทนที่จะเขียนใหม่จากศูนย์

ผลคือ throughput สูงมาก แต่แลกกับ feature บางอย่าง เช่น keyword biasing, speaker attribution, timestamp

## แก้คำเฉพาะทีหลังก็ได้ ไม่จำเป็นต้องแก้ที่ model

ตารางข้างบนมอง keyword biasing เป็น feature ของ model แต่ workflow ของ [[lex-fridman|Lex Fridman]] ใน [[dhh-strategies-programming-with-ai-agents-lex-clips|บทสัมภาษณ์กับ DHH]] แสดงอีกทาง คือทำเป็นชั้นแยกหลังการถอดเสียง

เขาถอดเสียงด้วย [[elevenlabs|ElevenLabs]] แล้วบอกเองว่ายังมีคำผิด จากนั้นให้ LLM ทำความสะอาด transcript โดยมี dictionary คำเฉพาะของเขา และมี agent ที่กวาด code base เพื่อดึงชื่อไฟล์กับชื่อ function ที่เขาพูดถึงบ่อยมาเป็นรายการอ้างอิง เวลาคุยเรื่องข้อความก็ให้รู้จักชื่อคนใน Gmail กับ WhatsApp

**ได้อะไร:** ถ้า ASR ที่เลือกไม่มี keyword biasing ก็ยังแก้ที่ pipeline ได้ ข้อดีคือเปลี่ยน dictionary ได้ทันทีและใช้กับ model ตัวไหนก็ได้ ข้อเสียคือเพิ่ม latency และยังพลาดได้เมื่อคำที่ถอดผิดกลายเป็นคำอื่นที่ฟังดูเข้าท่าจนไม่มีอะไรสะกิดให้แก้ Lex บอกว่าเขายอมรอ 5–10 วินาทีเพื่อแลกกับความถูก ดู [[voice-first-prompting]]

## See also

- [[granite-speech]]
- [[ibm]]
- [[non-autoregressive-asr]]
- [[speaker-attributed-asr]]
- [[keyword-biasing]]
- [[word-error-rate]]
- [[granite-4-1-fastest-asr]]
- [[voice-first-prompting]]
- [[elevenlabs]]
- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
