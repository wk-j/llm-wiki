---
title: Multi-Token Prediction (MTP)
type: concept
tags: [inference, training, llm, optimization, gemma]
created: 2026-05-07
updated: 2026-05-07
sources: [multi-token-prediction-gemma-4.md]
---

# Multi-Token Prediction (MTP) / การทำนายหลาย token พร้อมกัน

เทคนิคที่ให้ model ทำนาย **หลาย token ล่วงหน้าใน forward pass เดียว** แทนที่จะทำนายแค่ token ถัดไปตัวเดียวตามแบบ autoregressive ปกติ ใช้ได้ทั้งตอน train (เป็น auxiliary objective ที่ช่วยให้ model เรียนรู้เร็วขึ้น) และตอน inference (เป็น drafter สำหรับ [[speculative-decoding]])

## MTP ในมุม drafter

ในกรณีของ [[gemma|Gemma 4]] ของ Google ตัว MTP head เป็น **drafter ที่ผูกอยู่กับ target เลย**:

- ใช้ **activations ของ target ร่วมกัน** — ไม่ต้อง forward target ซ้ำเพื่อให้ drafter เดา
- **share KV cache** กับ target — ไม่ต้องเก็บ cache แยก
- overhead จึงน้อยมากเมื่อเทียบกับการมี drafter แยกเป็น model อีกตัวหนึ่ง

ผลคือเอา compute ที่เคยเหลือว่าง (เพราะ inference ติด memory bandwidth) มาใช้เดา token ล่วงหน้าได้เกือบฟรี

## ตัวเลขที่ Google รายงาน

- Gemma 4 + MTP drafter เร่งได้ **สูงสุด 3 เท่า** โดย output เหมือนเดิม
- บน **Apple Silicon** ได้ ~2.2x ที่ batch size 4–8
- บน **Nvidia A100** ได้ผลใกล้เคียงเมื่อ batch size เพิ่ม
- สำหรับ edge model **E2B / E4B** ใช้ efficient clustering ใน embedder ของ MTP head

## ความเชื่อมโยง

- [[speculative-decoding]] — กรอบกว้างกว่า; MTP เป็น "drafter ภายใน" แบบหนึ่ง
- [[gemma]] — ตระกูล model ที่ Google ปล่อย MTP drafter ให้

## See also

- [[speculative-decoding]]
- [[gemma]]
- [[token-optimization]]
