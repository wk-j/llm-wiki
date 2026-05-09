---
title: "Accelerating Gemma 4: Multi-Token Prediction Drafters"
type: source
tags: [gemma, google, inference, speculative-decoding, multi-token-prediction, latency, agents]
url: "https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/"
created: 2026-05-07
updated: 2026-05-07
sources: [multi-token-prediction-gemma-4.md]
---

# Accelerating Gemma 4: Multi-Token Prediction Drafters / เร่ง Gemma 4 ด้วย MTP Drafters

บทความบล็อก Google โดย Olivier Lacombe (Director, PM) และ Maarten Grootendorst (DevRel) ประกาศปล่อย **Multi-Token Prediction (MTP) drafter** สำหรับตระกูล [[gemma|Gemma 4]] โดยอ้างว่าเร่งความเร็ว inference ได้ **สูงสุด 3 เท่า** โดยคุณภาพ output ไม่ลดลงเลย

## ปัญหาที่แก้

Inference ของ LLM ตอนนี้ติด **memory bandwidth** ไม่ใช่ compute — กล่าวคือ GPU/CPU เสียเวลาส่วนใหญ่ไปกับการลาก parameter หลายพันล้านตัวจาก VRAM เข้ามายัง compute unit เพื่อสร้างเพียง token เดียว ทำให้ compute เหลือว่างและ latency สูง

## วิธีแก้: Speculative Decoding

จับคู่ target model ตัวใหญ่ (เช่น Gemma 4 31B) กับ **drafter** ตัวเล็กๆ ที่เบากว่ามาก

- drafter เดาหลาย token ล่วงหน้าในขณะที่ target ทำงาน 1 token
- จากนั้น target ตรวจคำเดาทั้งหมด **พร้อมกันใน batch เดียว** — ถ้าตรงก็ accept, ถ้าไม่ตรงก็ rollback
- ผลคือเอา compute ที่เหลือว่างมาใช้ให้คุ้ม โดย output ออกมาเหมือนเดิมเป๊ะๆ (lossless)

ดูเพิ่มที่ [[speculative-decoding]] และ [[multi-token-prediction]]

## รายละเอียดสถาปัตยกรรม

- Draft model **ใช้ activations ของ target ร่วมกัน** และ **share KV cache** กับ target — ตรงนี้คือเหตุผลที่ overhead ของ drafter เหลือน้อยมาก
- สำหรับ edge model **E2B / E4B** ใช้ efficient clustering ใน embedders
- บน **Apple Silicon** ได้ ~2.2x ที่ batch size 4–8
- บน **Nvidia A100** ได้ผลใกล้เคียงเมื่อ batch size สูงขึ้น

## รองรับ framework / runtime

Hugging Face Transformers, MLX, vLLM, SGLang, [[ollama]], LiteRT-LM, Google AI Edge Gallery (Android/iOS)

## ใครได้ประโยชน์

> "Drastically reduce latency for near real-time chat, immersive voice applications and agentic workflows"
> while maintaining "identical frontier-class reasoning and accuracy."

ตรงนี้ตรงกับ pain point ของ [[agentic-engineering|งาน agentic]] ที่ต้องเรียก model หลายรอบใน loop เดียว — latency ทุก ms มีผล

## License และที่มา

Apache 2.0 — model weights และเอกสารอยู่บน Hugging Face และ Kaggle

## See also

- [[gemma]]
- [[speculative-decoding]]
- [[multi-token-prediction]]
- [[google-cloud]]
