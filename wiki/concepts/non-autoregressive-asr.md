---
title: Non-Autoregressive ASR
type: concept
tags: [asr, speech, inference, throughput, models]
created: 2026-05-09
updated: 2026-05-09
sources: [granite-4-1-fastest-asr.md]
---

# Non-Autoregressive ASR / ASR ที่ไม่ถอดเสียงทีละ token

Non-autoregressive ASR คือวิธีทำ transcript ที่ไม่ generate token ทีละตัวตามลำดับแบบ autoregressive ปกติ เป้าหมายคือทำให้ decoding ขนานขึ้นและเร็วขึ้นมาก

ใน [[granite-4-1-fastest-asr|Granite 4.1 - The Fastest ASR?]], [[granite-speech|Granite Speech]] 4.1 2B NAR ใช้แนวคิดนี้เพื่อเร่ง throughput สำหรับงานถอดเสียงจำนวนมาก

## ปัญหาของ autoregressive ASR

ASR model อย่าง Whisper, Parakeet, Canary และ transformer ASR หลายตัว generate transcript ทีละ token:

1. model ทำนาย token ถัดไป
2. token นั้นกลายเป็น context ของ token ถัดไป
3. GPU ต้องรอ step ก่อนหน้าเสร็จก่อนทำ step ต่อไป

วิธีนี้ช่วย accuracy เพราะ model เห็นสิ่งที่ตัวเองเพิ่งเขียน แต่ทำให้ decoding เป็น sequential workload ขนาดเล็กจำนวนมาก

ได้อะไร: ถ้าต้อง transcribe หลายร้อยชั่วโมง sequential decoding จะกลายเป็นคอขวด

## NLE: Transcript Editing

IBM ใช้แนวทาง **NLE: Non-autoregressive LLM-based ASR by Transcript Editing** แทนการทำนายทั้ง transcript จากศูนย์

กลไกคือ:

1. **frozen CTC encoder** ฟังเสียงแล้วสร้าง draft transcript อย่างเร็ว
2. draft มักถูกเป็นส่วนใหญ่ แต่ยังมีคำผิด/ขาด/เกิน
3. LLM-based editor ใช้ bidirectional attention เพื่อ **copy, insert, delete, replace**
4. output สุดท้ายคือ transcript ที่แก้จาก draft

การแก้ draft ง่ายกว่าการเขียน transcript ทั้งหมดในช็อตเดียว เพราะ model มีโครงให้ยึดอยู่แล้ว

ได้อะไร: ได้ speed แบบ non-autoregressive แต่ไม่เสีย accuracy หนักเท่าการ predict ทั้ง sequence จากศูนย์

## Trade-off

Granite Speech 4.1 2B NAR ถูกวางเป็น model สำหรับ raw transcript throughput:

- เร็วมากเมื่อ batch บน hardware อย่าง H100
- เหมาะกับเสียงจำนวนมากที่ต้องการข้อความดิบ
- แต่ไม่มี [[keyword-biasing|keyword biasing]]
- ไม่มี [[speaker-attributed-asr|speaker attribution]]
- ไม่มี timestamp
- ไม่มี translation

ผลคือ NAR ไม่ใช่ตัวแทนรุ่น Plus หรือ base ทุกงาน แต่เป็นตัวเลือกเมื่อ bottleneck คือ throughput

## See also

- [[automatic-speech-recognition]]
- [[granite-speech]]
- [[word-error-rate]]
- [[granite-4-1-fastest-asr]]
