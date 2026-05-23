---
title: Granite Speech
type: entity
tags: [ibm, speech, asr, open-models, local-ai]
created: 2026-05-09
updated: 2026-05-09
sources: [granite-4-1-fastest-asr.md]
---

# Granite Speech

Granite Speech คือสาย speech model ในตระกูล Granite ของ [[ibm|IBM]] สำหรับงานเสียง เช่น [[automatic-speech-recognition|Automatic Speech Recognition]] หรือ ASR

ใน Granite Speech 4.1, IBM ปล่อย model 2B ประมาณ 3 แบบ ไม่ได้บังคับให้ใช้ model เดียวกับทุกงาน แนวคิดคือเลือกตาม bottleneck:

- **Granite Speech 4.1 2B** — เน้น WER ต่ำและมี [[keyword-biasing|keyword biasing]]
- **Granite Speech 4.1 2B Plus** — เพิ่ม [[speaker-attributed-asr|speaker attribution]], word-level timestamp, incremental decoding
- **Granite Speech 4.1 2B NAR** — ใช้ [[non-autoregressive-asr|non-autoregressive ASR]] เพื่อ throughput สูงมาก

## Positioning

Granite Speech ไม่ได้แทน Whisper แบบตรงๆ ทุกด้าน แต่เปิดทางเลือกที่ Whisper และ model อย่าง Parakeet/Canary อาจไม่ตอบหมดพร้อมกัน:

- ต้องการเร็วมาก → NAR
- ต้องการชื่อเฉพาะหรือ acronym ถูก → base + keyword biasing
- ต้องการ transcript ที่รู้ speaker และ timing → Plus
- ต้องการรัน local / edge → ทุกตัวอยู่ระดับประมาณ 2B

## Long-form audio

สำหรับ audio ยาว เช่น podcast 4 ชั่วโมง ปัญหาไม่ได้จบที่ model ดี ต้องมี workflow:

- chunking และ overlap
- prefix หรือ previous transcript สำหรับ incremental decoding
- keyword list ต่อ chunk
- speaker numbering ที่คงที่ข้าม chunk

ตรงนี้ทำให้ Granite Speech เป็นทั้ง model release และโจทย์ harness/pipeline สำหรับงานเสียง

## See also

- [[ibm]]
- [[automatic-speech-recognition]]
- [[non-autoregressive-asr]]
- [[speaker-attributed-asr]]
- [[keyword-biasing]]
- [[word-error-rate]]
- [[granite-4-1-fastest-asr]]
