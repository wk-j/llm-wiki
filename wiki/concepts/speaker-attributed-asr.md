---
title: Speaker-Attributed ASR
type: concept
tags: [asr, speech, diarization, transcription, audio]
created: 2026-05-09
updated: 2026-05-09
sources: [granite-4-1-fastest-asr.md]
---

# Speaker-Attributed ASR / ถอดเสียงพร้อมบอกว่าใครพูด

Speaker-attributed ASR คือ ASR ที่ไม่ได้ออกแค่ข้อความ แต่ใส่ label ว่า speaker ไหนพูดช่วงไหนด้วย มักเรียกใกล้กับคำว่า **diarization**

ตัวอย่าง output ที่มีประโยชน์:

- Speaker 1: ...
- Speaker 2: ...
- Speaker 1: ...

ใน [[granite-4-1-fastest-asr|Granite 4.1 - The Fastest ASR?]], [[granite-speech|Granite Speech]] 4.1 2B Plus ถูกวางเป็นรุ่นสำหรับงานนี้

## ทำไม transcript ธรรมดาไม่พอ

ถ้าเป็นเสียงคนเดียว transcript ดิบอาจพอใช้ แต่ podcast, interview, meeting, court transcript, customer call มักมีหลายคน

พอไม่รู้ว่าใครพูด ประโยคเดียวกันอาจตีความผิด เช่น:

- ลูกค้าพูดหรือพนักงานพูด
- host ถามหรือ guest ตอบ
- คนหนึ่งเสนอ อีกคน reject หรือเปล่า

ได้อะไร: speaker attribution ทำให้ transcript กลายเป็น record ของบทสนทนา ไม่ใช่แค่กองข้อความ

## ใน Granite Speech 4.1 Plus

รุ่น Plus ให้ speaker label เช่น speaker 1 / speaker 2 แต่ไม่ได้รู้ชื่อจริงเสมอไป ขั้นต่อไปคือ map speaker label เป็นชื่อคนจริงใน pipeline

Plus ยังมี word-level timestamps และ incremental decoding ซึ่งช่วยงาน long-form audio:

- ตัดเสียงเป็น chunk แล้วต่อ transcript ได้
- รักษา speaker numbering ให้คงที่ขึ้น
- ใช้ timestamp ทำ subtitle หรือ audio navigation ได้

trade-off คือภาษาน้อยลง ไม่มี translation และ WER สูงกว่ารุ่น base

## See also

- [[automatic-speech-recognition]]
- [[granite-speech]]
- [[keyword-biasing]]
- [[word-error-rate]]
- [[granite-4-1-fastest-asr]]
