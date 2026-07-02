---
title: KV Cache
type: concept
tags: [ai, llm, transformer, inference, memory, attention]
created: 2026-07-03
updated: 2026-07-03
sources: [llm-loops-instead-of-chain-of-thought.md]
---

# KV Cache / แคช Key-Value ของ Transformer

KV cache คือหน่วยความจำที่เก็บ key และ value tensors ของ token ก่อนหน้าไว้ เพื่อให้ transformer decode token ถัดไปโดยไม่ต้องคำนวณ attention ของอดีตซ้ำทั้งหมด

ใน [[llm-loops-instead-of-chain-of-thought|LLM that loops instead of Doing Chain-of-Thought]] bycloud ชี้ว่า KV cache เป็น bottleneck สำคัญของ [[looped-transformers|looped transformer]] และ [[mixture-of-recursions|Mixture of Recursions]]: parameter อาจ shared แล้ว แต่ memory traffic ยังแพงอยู่

## ทำไมสำคัญ

ตอน decode LLM เขียน token ทีละตัว. Token ใหม่ต้อง attend ไปหา token เก่า ถ้าไม่มี cache model ต้อง recompute key/value ของ context เดิมซ้ำทุกครั้ง

KV cache ทำให้ decode เร็วขึ้น แต่กิน GPU memory และ memory bandwidth มาก โดยเฉพาะ:

- context ยาว
- batch ใหญ่
- layer เยอะ
- model ที่มีหลาย recursion depth

**ผลคือ:** inference bottleneck ไม่ได้มีแค่ FLOPs. หลายครั้งช้าหรือแพงเพราะอ่านเขียน memory มากเกินไป

## ปัญหาใน recursive model

ใน recursive/looped model เรา reuse weight เดิมได้ แต่ถ้าเก็บ KV แยกทุก recursion depth แบบ naive ก็ยังใช้ memory หลายชุดอยู่ดี

คลิปสรุปสองวิธี:

- **Recursion-wise caching**: เก็บ KV ของ token ที่ยัง active ในแต่ละ recursion. Token ที่ออกแล้วไม่ต้องถูกลากไปลึกต่อ วิธีนี้ representation สดกว่า แต่กิน memory มากกว่า
- **Recursive KV sharing**: เก็บ KV ครั้งแรก แล้ว reuse ใน recursion ต่อ ๆ ไป วิธีนี้ประหยัดกว่า แต่รอบหลัง attend ไปยัง representation ที่ stale เล็กน้อย

## ความสัมพันธ์กับเทคนิคอื่น

[[mla-attention|Multi-head Latent Attention]] ของ [[deepseek|DeepSeek]] และ [[sparse-attention|sparse attention]] ต่างก็อยู่ในกลุ่มเทคนิคที่ลดราคาของ attention/KV memory. แนวคิดไม่เหมือนกัน แต่แก้คอขวดเดียวกัน: context ยาวทำให้ memory เป็นเพดาน

## See also

- [[looped-transformers]]
- [[mixture-of-recursions]]
- [[mla-attention]]
- [[sparse-attention]]
- [[speculative-decoding]]
