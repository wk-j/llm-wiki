---
title: Gemma
type: entity
tags: [google, model, open-weight, llm]
created: 2026-05-07
updated: 2026-05-07
sources: [multi-token-prediction-gemma-4.md]
---

# Gemma

ตระกูล **open-weight model** ของ Google ปล่อยภายใต้ Apache 2.0 — เป็นคู่หู open-source ของ Gemini ที่เป็น proprietary

## Gemma 4 (2026)

รุ่นปัจจุบัน ณ ปี 2026 มีหลายขนาดตั้งแต่ edge model ขนาดเล็กไปจนถึง model ใหญ่ระดับ 31B

ขนาดที่ปรากฏในเอกสารของ Google:

- **E2B / E4B** — รุ่น edge สำหรับ Android/iOS (ผ่าน Google AI Edge Gallery) และ LiteRT-LM
- **Gemma 4 31B** — รุ่นใหญ่ที่ใช้เป็น target ใน MTP drafter blog post

## MTP Drafters (พ.ค. 2026)

Google ปล่อย [[multi-token-prediction|MTP]] drafter สำหรับ Gemma 4 ทุกขนาด ทำงานคู่กับ target model ผ่านวิธี [[speculative-decoding]] อ้างว่าเร่ง inference ได้ **สูงสุด 3 เท่า** โดย output เหมือนเดิม drafter share activations และ KV cache กับ target จึงเบามาก ดูที่ [[multi-token-prediction-gemma-4]]

## Runtime ที่รองรับ

Hugging Face Transformers, MLX, vLLM, SGLang, [[ollama|Ollama]], LiteRT-LM, Google AI Edge Gallery

## See also

- [[multi-token-prediction]]
- [[speculative-decoding]]
- [[google-cloud]]
- [[multi-token-prediction-gemma-4]]
