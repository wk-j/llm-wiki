---
title: Residual Stream
type: concept
tags: [ai, llm, transformer, architecture, interpretability]
created: 2026-07-03
updated: 2026-07-03
sources: [llm-loops-instead-of-chain-of-thought.md]
---

# Residual Stream / ช่องทาง state หลักของ Transformer

Residual stream คือช่องทาง hidden state หลักที่ข้อมูลไหลผ่าน transformer layer. แต่ละ layer อ่านจาก stream นี้ แล้วเขียน update กลับเข้าไป

ในคลิป [[llm-loops-instead-of-chain-of-thought|LLM that loops instead of Doing Chain-of-Thought]] bycloud ใช้ residual stream เพื่ออธิบายว่า [[looped-transformers|looped transformer]] เป็น dynamical system: hidden state เดิมถูก update ซ้ำทุก recurrence ไม่ได้ถูกคำนวณใหม่จากศูนย์

## ทำไมเกี่ยวกับ loop

ถ้า transformer block ถูกวนซ้ำ output ของรอบก่อนจะกลับมาเป็น input ของ block เดิม. Residual stream จึงเป็น state ที่สะสมข้อมูลข้าม loop

ถ้า update stable representation จะค่อย ๆ refine. ถ้า update unstable hidden state norm อาจโต, direction อาจ drift, และ loss อาจ spike

**ผลคือ:** การออกแบบ looped transformer ต้องคุม residual stream ไม่ให้สะสม error หรือพลังงานของ activation แบบไร้ทิศทาง

## See also

- [[looped-transformers]]
- [[latent-reasoning]]
- [[kv-cache]]
