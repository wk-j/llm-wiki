---
title: Speculative Decoding
type: concept
tags: [inference, latency, llm, optimization]
created: 2026-05-07
updated: 2026-07-03
sources: [multi-token-prediction-gemma-4.md, chinas-models-no-longer-need-western-hardware.md]
---

# Speculative Decoding / สเปคคูเลทีฟดีโคดดิง

เทคนิคเร่ง inference ของ LLM ที่ **ไม่เปลี่ยน output** เลย — ใช้ model ตัวเล็ก (drafter) เดา token ล่วงหน้าหลายตัว แล้วให้ model ตัวใหญ่ (target) ตรวจคำเดาเหล่านั้นพร้อมกันใน batch เดียว

## ทำไมถึงเร่งได้

Inference ของ LLM ติด **memory bandwidth** — เวลาส่วนใหญ่หมดไปกับการดึง weight หลายพันล้านตัวจาก VRAM เข้ามาทุกครั้งที่จะ generate 1 token ส่วน compute จริงๆ เหลือว่างเยอะ

speculative decoding ใช้ compute ที่เหลือว่างนี้ให้คุ้ม โดย:

1. drafter (model เล็ก) generate ไป k token ติดๆ กันอย่างรวดเร็ว
2. target (model ใหญ่) เอา k token นั้นมาตรวจ **พร้อมกันใน 1 forward pass** — ค่าใช้จ่ายเทียบเท่ากับ generate 1 token ปกติ เพราะ bottleneck คือการลาก weight ไม่ใช่ compute
3. ตรงไหน drafter ทายถูก ก็ accept ตรงไหนผิด ก็ rollback ตั้งแต่จุดที่ผิด

ผลคือถ้า drafter เดาถูก k–1 จาก k ตัว ก็ได้ throughput เกือบ k เท่า ตัว target ยังเป็นคน "ตัดสินใจสุดท้าย" ทุกครั้ง — output จึงเหมือนกับใช้ target ตัวเดียวเป๊ะๆ (lossless)

## ข้อจำกัด

- ต้องมี drafter ที่ **distribution ใกล้กับ target** ไม่งั้นเดาผิดบ่อย accept rate ต่ำ ก็ไม่ได้เร่งจริง
- กิน VRAM เพิ่ม (ต้องโหลด drafter ด้วย)
- เร่งดีที่สุดที่ batch size เล็ก — batch ใหญ่มาก compute เริ่มเป็น bottleneck แทน memory bandwidth จุดเด่นก็จาง

## ความสัมพันธ์กับ Multi-Token Prediction

[[multi-token-prediction]] (MTP) เป็น **วิธีหนึ่งในการสร้าง drafter** ที่ดี — แทนที่จะเทรน drafter แยก ก็ให้ target เองทำนายหลาย token ล่วงหน้าในการ forward เดียว ใน [[gemma|Gemma 4]] ของ Google ใช้ MTP drafter ที่ share activations และ KV cache กับ target จึงเบามาก

## ใช้ที่ไหนแล้วบ้าง

- vLLM, SGLang, MLX, Hugging Face Transformers, Ollama, LiteRT-LM รองรับเป็นมาตรฐานในปี 2026
- [[gemma|Gemma 4]] + MTP drafter — Google อ้างเร่งได้สูงสุด 3 เท่า
- [[longcat-2-0|LongCat 2.0]] — วิดีโอของ [[prompt-engineering|Prompt Engineering]] บอกว่าใช้ picker / draft network ที่เบากว่าเพื่อเพิ่ม throughput บน hardware ที่ memory bandwidth จำกัดกว่า NVIDIA stack

## ทำไมเรื่องนี้สำคัญกับ agentic workflow

[[agentic-engineering|Agent loops]] เรียก model หลายรอบต่อ task เดียว — latency ทุก ms ทบกันใน loop ภายนอก speculative decoding จึงเป็น **เครื่องมือเร่ง agent โดยไม่ต้องลด quality** ที่หาได้ยาก

ในมุม hardware เรื่องนี้ยิ่งสำคัญกว่าเดิม. ถ้า decode ติด memory bandwidth การให้ model ใหญ่ตรวจหลาย token พร้อมกันช่วยใช้ compute ที่เหลือว่างให้คุ้มขึ้น โดยไม่ต้องเปลี่ยนคำตอบสุดท้ายของ target model

## See also

- [[multi-token-prediction]]
- [[gemma]]
- [[token-optimization]]
- [[longcat-2-0]]
