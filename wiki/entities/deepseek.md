---
title: DeepSeek
type: entity
tags: [ai-lab, china, llm, deepseek]
created: 2026-04-27
updated: 2026-04-27
sources: [deepseek-wikipedia.md]
---

# DeepSeek / ดีพซีค

บริษัทวิจัย AI สัญชาติจีน (Hangzhou DeepSeek Artificial Intelligence Basic Technology Research Co., Ltd.) ที่สร้างความสั่นสะเทือนไปทั่วโลกในช่วงต้นปี 2025 ด้วยการปล่อย model ที่ประสิทธิภาพสูงในราคาที่ถูกอย่างไม่น่าเชื่อ

## ภาพรวม

DeepSeek เป็นบริษัทที่แยกตัว (spinoff) ออกมาจากกองทุน Quant Hedge Fund ชื่อ **[[high-flyer|High-Flyer]]** ในช่วงกลางปี 2023 โดยมีเป้าหมายหลักคือการวิจัย AGI (Artificial General Intelligence) ภายใต้การนำของ **[[liang-wenfeng|Liang Wenfeng]]** (CEO)

สิ่งที่ทำให้ DeepSeek ต่างจาก Lab ใน Silicon Valley คือความสามารถในการรีดประสิทธิภาพจาก hardware ที่จำกัด (เช่น การใช้ Nvidia A100 ในช่วงที่ถูกแบนชิปใหม่) และการใช้เงินทุนในการ train model ที่น้อยกว่า OpenAI หรือ Google มากถึง 10-20 เท่า แต่ได้ผลลัพธ์ที่ใกล้เคียงกัน

## ผลงานและ Model สำคัญ

- **DeepSeek-V3:** Model ตัวแรงที่ใช้เงิน train เพียง $6M แต่ประสิทธิภาพชนกับ GPT-4o ได้
- **DeepSeek-R1:** Reasoning model ที่ใช้เทคนิค **[[grpo|GRPO]]** ในการฝึก ทำให้มีความสามารถในการคิดวิเคราะห์ (reasoning) สูงมากจนกลายเป็น app ที่มียอด download สูงสุดใน US App Store ช่วงต้นปี 2025
- **DeepSeek Coder:** ตระกูล model ที่เน้นด้านการเขียน code โดยเฉพาะ

## จุดเด่นด้านกลยุทธ์

- **Efficiency First:** เน้นการปรับแต่ง algorithm (เช่น **[[mla-attention|MLA]]**) เพื่อลดการกิน memory และเพิ่มความเร็วในการประมวลผล
- **Open-weight:** ปล่อยน้ำหนัก (weights) ของ model ให้คนทั่วไปนำไปใช้งานได้ฟรี (แต่ไม่เปิดเผยชุดข้อมูลที่ใช้ train ทั้งหมด) ซึ่งต่างจาก closed-source model ของ OpenAI
- **Hiring Strategy:** ไม่เน้นจ้างแค่สาย Computer Science แต่รับคนจากหลากหลายสาขา เช่น นักคณิตศาสตร์ หรือแม้แต่นักกวี เพื่อเพิ่มความลุ่มลึกให้กับ model

## See also

- [[high-flyer]]
- [[liang-wenfeng]]
- [[mla-attention]]
- [[grpo]]
- [[open-weight-models]]
