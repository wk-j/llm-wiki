---
title: Sam Witteveen
type: entity
tags: [creator, ai, local-ai, agents, youtube]
created: 2026-05-09
updated: 2026-09-19
sources: [granite-4-1-fastest-asr.md, jev-the-ultimate-classification-model.md]
---

# Sam Witteveen

Sam Witteveen เป็น AI creator / practitioner ที่ทำวิดีโออธิบาย model, local AI, และ LLM agent workflow พร้อม demo code

ใน [[granite-4-1-fastest-asr|Granite 4.1 - The Fastest ASR?]] เขาอธิบาย [[granite-speech|Granite Speech]] 4.1 ของ [[ibm|IBM]] ผ่านมุมใช้งานจริง ไม่ใช่แค่อ่าน benchmark:

- รุ่นไหนเหมาะกับ transcript ทั่วไป
- รุ่นไหนเหมาะกับ podcast/meeting ที่ต้องมี speaker label
- รุ่นไหนเหมาะกับ batch transcription ขนาดใหญ่
- deployment local ต้องระวัง PyTorch, CUDA, Flash Attention, chunking, batching ยังไง

## Angle

มุมของ Sam คือ “model release ต้องแปลเป็น workflow ได้” เขาสนใจทั้งความเร็ว, accuracy, prompt control, diarization, timestamp, และการทำให้ agent เรียก transcriber local ได้

ตรงนี้เชื่อมกับ wiki ในสาย [[harness-engineering|Harness Engineering]] เพราะ ASR model จะมีค่าจริงเมื่อถูกห่อด้วย pipeline ที่จัด chunk, keyword biasing, speaker label, และ long-form stitching ได้ดี

## Jev และคำตัดสินที่ไม่ต้องผ่าน chatbot

ใน [[jev-the-ultimate-classification-model|Jev - The Ultimate Classification Model?]] Sam ทดลอง [[jev|Jev]] ของ [[typesafe-ai|Typesafe AI]] ผ่าน OpenRouter จุดสนใจยังเหมือนเดิมคือเอา model มาวางใน workflow จริง แต่ครั้งนี้เปลี่ยนจาก speech model มาเป็น [[system-one-models|System One Model]] ที่คืน class, score หรือ yes-probability โดยตรง

Sam ทดลองทั้ง language identification, sentiment, support routing, PII, spam, prompt injection และ tool selection พร้อมชี้ข้อจำกัดว่า Jev เลือกชื่อ tool ได้แต่ยังสร้าง argument ให้ไม่ได้ เขายังแยกสิ่งที่บริษัทเปิดเผยออกจากสิ่งที่ตัวเองเดา เช่น สมมติฐานว่า model อาจใช้ transformer prefill กับ classification head

มุมนี้ขยายภาพเดิมของ Sam จาก "model release ต้องแปลเป็น workflow ได้" ไปอีกขั้น งานที่ต้องตัดสินใจสั้น ๆ อาจไม่ควรใช้ chatbot หรือ reasoning model เป็นค่าเริ่มต้น แต่ output ที่เร็วและ typed ก็ยังต้องทดสอบ accuracy กับ calibration ในข้อมูลจริง

## See also

- [[granite-4-1-fastest-asr]]
- [[granite-speech]]
- [[automatic-speech-recognition]]
- [[harness-engineering]]
- [[jev-the-ultimate-classification-model]]
- [[jev]]
- [[system-one-models]]
