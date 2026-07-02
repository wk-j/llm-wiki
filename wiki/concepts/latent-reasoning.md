---
title: Latent Reasoning
type: concept
tags: [ai, llm, reasoning, inference, architecture]
created: 2026-07-03
updated: 2026-07-03
sources: [llm-loops-instead-of-chain-of-thought.md]
---

# Latent Reasoning / การคิดใน latent state

Latent reasoning คือการให้ model ทำ intermediate computation ภายใน hidden state แทนการเขียนขั้นคิดออกมาเป็นภาษาธรรมชาติ

ในคลิป [[llm-loops-instead-of-chain-of-thought|LLM that loops instead of Doing Chain-of-Thought]] bycloud ใช้ [[looped-transformers|looped transformer]] เป็นตัวอย่าง: model วน block เดิมซ้ำ ๆ เพื่อ refine representation โดยไม่ต้องปล่อย chain-of-thought token

## ทำไมคนสนใจ

Chain-of-thought ทำให้ reasoning มองเห็นและ train ได้ง่าย แต่มีต้นทุน:

- ใช้ token เพิ่ม
- เพิ่ม latency
- กิน context window
- reasoning ถูกบีบผ่านภาษาและ sampling

Latent reasoning พยายามย้ายการคิดกลับเข้า computation โดยตรง. แทนที่จะเขียน "คิดทีละขั้น" model ปรับ hidden state หลายรอบแล้วค่อยตอบ

**ได้อะไร:** ถ้าทำได้ดี model อาจคิดนานขึ้นโดยไม่ต้องเปิด reasoning trace เป็นข้อความยาว ๆ

## จุดอ่อน

ข้อเสียใหญ่คือ supervision. Chain-of-thought มี textual trace ให้สอน, distill, filter, หรือให้รางวัลได้. Latent reasoning ไม่มี trace ภาษาธรรมชาติที่บอกว่า step ไหนถูกหรือผิด

ดังนั้น model ต้องค้น process ภายในเองจาก objective ปลายทาง หรือเราต้องมีวิธีช่วยกำกับ latent trajectory แบบอื่น

## ความสัมพันธ์กับ interpretability

งาน mechanistic analysis ที่ bycloud เล่าพยายามดู latent reasoning ด้วย PCA และ attention behavior ข้าม recurrence. ถ้า hidden state ค่อย ๆ เข้า fixed point หรือ cycle ที่เสถียร เราอาจเห็นว่าการวนซ้ำกำลังจัดรูปและ refine ปัญหา ไม่ใช่ drift แบบสุ่ม

แต่การเห็น trajectory ที่ดูดีไม่ได้พิสูจน์ว่างานจริงจะ generalize กว้าง ต้องเทียบกับ benchmark และระบบ production ต่อ

## See also

- [[looped-transformers]]
- [[chain-of-thought]]
- [[multi-hop-reasoning]]
- [[reasoning-regression]]
- [[model-honesty]]
