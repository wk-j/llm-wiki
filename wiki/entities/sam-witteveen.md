---
title: Sam Witteveen
type: entity
tags: [creator, ai, local-ai, agents, youtube]
created: 2026-05-09
updated: 2026-05-09
sources: [granite-4-1-fastest-asr.md]
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

## See also

- [[granite-4-1-fastest-asr]]
- [[granite-speech]]
- [[automatic-speech-recognition]]
- [[harness-engineering]]
