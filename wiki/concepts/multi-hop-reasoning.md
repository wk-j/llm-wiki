---
title: Multi-hop Reasoning
type: concept
tags: [ai, llm, reasoning, benchmarks]
created: 2026-07-03
updated: 2026-07-03
sources: [llm-loops-instead-of-chain-of-thought.md]
---

# Multi-hop Reasoning / การให้เหตุผลหลาย hop

Multi-hop reasoning คือโจทย์ที่ต้องหาคำตอบผ่านข้อมูลหลายขั้น โดยคำตอบของขั้นหนึ่งกลายเป็น input ของขั้นถัดไป

ใน [[llm-loops-instead-of-chain-of-thought|LLM that loops instead of Doing Chain-of-Thought]] bycloud ยกตัวอย่าง "ภรรยาของประธานาธิบดีสหรัฐคนที่ 44 คือใคร" model ต้องรู้ก่อนว่าคนที่ 44 คือ Barack Obama แล้วค่อยโยงไป Michelle Obama

## ทำไมไม่ใช่แค่จำ

โจทย์หนึ่งขั้นมักตอบได้ด้วย pattern matching หรือ memorization. แต่โจทย์หลาย hop ต้อง track state ระหว่างทาง:

- ดึง fact แรก
- ใช้ fact นั้นเลือก relation ถัดไป
- รวมผลลัพธ์จนได้ answer

ยิ่งจำนวน hop เพิ่ม model ต้อง simulate computation ที่ลึกขึ้น ถ้าเป็น vanilla transformer ที่ทำครั้งเดียวใน forward pass อาจไม่มีพื้นที่พอให้ iterate

## ทำไมเกี่ยวกับ looped transformer

[[looped-transformers|Looped transformer]] ให้ model วน hidden state หลายรอบ. ถ้าแต่ละ loop ทำหน้าที่เหมือน step ของการ infer ความสัมพันธ์ จำนวน loop ก็เป็นตัวแทนของ depth ได้

คลิปบอกว่า paper **Loop, Think, & Generalize** พบว่าเมื่อเพิ่ม recurrent iterations ตอน inference model ทำ hop ได้มากกว่าที่ train ไว้ในบาง setting นี่ทำให้ multi-hop reasoning เป็น benchmark แรก ๆ ที่ใช้ดูว่า recurrence ช่วย reasoning จริงไหม

**ผลคือ:** multi-hop reasoning เป็นสนามทดลองที่วัดง่ายกว่า reasoning โลกจริง แต่ยังเป็นแค่ proxy ไม่ใช่ proof ว่า model เข้าใจทุกงาน

## See also

- [[looped-transformers]]
- [[latent-reasoning]]
- [[chain-of-thought]]
- [[behavioral-verifier]]
- [[research-taste]]
