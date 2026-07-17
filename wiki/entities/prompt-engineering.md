---
title: Prompt Engineering
type: entity
tags: [youtube, ai, education, source]
created: 2026-07-03
updated: 2026-07-17
sources: [chinas-models-no-longer-need-western-hardware.md, stop-building-ai-agents-old-way.md, gpt-5-6-sol-fable-killer-prompt-engineering.md, kimi-k3-explained-prompt-engineering.md]
---

# Prompt Engineering / พรอมป์เอ็นจิเนียริง

Prompt Engineering คือช่อง YouTube / แหล่งอธิบายงาน AI engineering ที่เป็นผู้ทำวิดีโอ [[chinas-models-no-longer-need-western-hardware|China's Models No Longer Need Western Hardware]] และ [[stop-building-ai-agents-old-way|Stop Building AI Agents the Old Way]].

## บทบาทใน wiki

ในแหล่งนี้ Prompt Engineering ทำหน้าที่เป็นผู้เล่าและตีความ LongCat 2.0 ของ [[meituan|Meituan]] โดยเน้นมุม hardware independence, CUDA dependency, MoE limits, [[n-gram-embeddings|n-gram embeddings]], [[sparse-attention|sparse attention]], และ [[speculative-decoding|speculative decoding]].

เนื้อหาควรอ่านเป็น third-party explainer ไม่ใช่ primary source จาก Meituan. ตัวเลข model, chip count, token count, และ benchmark จึงควรโยงกลับไปที่คลิปหรือ blog ของ LongCat ก่อนใช้เป็นข้อเท็จจริงแข็ง

ใน [[stop-building-ai-agents-old-way|Stop Building AI Agents the Old Way]] ช่องนี้ย้ายจากเรื่อง model/hardware ไปสู่การออกแบบ [[long-running-agents|long-running agents]]: goal เป็น contract, evaluator แยกจาก executor, verifier เป็น proof, outer loop คุมการวน, role orchestration คุม cost/quality, [[agent-observability|agent observability]] ทำให้เห็น run ที่ยาว, และ [[session-mining|session mining]] เปลี่ยน failure เก่าเป็น rule.

คลิปนี้มีช่วง sponsor ของ [[latitude|Latitude]] จึงควรแยก claim เกี่ยวกับ product ออกจากกรอบคิดทั่วไปเรื่อง agent reliability.

ใน [[gpt-5-6-sol-fable-killer-prompt-engineering|GPT 5.6 Sol: Fable Killer?]] ช่องนี้กลับมาเทียบ model โดยวาง [[gpt-5-6-sol|GPT-5.6 Sol]] กับ [[fable|Claude Fable 5]] ผ่าน cost, coding benchmark, งาน UI, long-horizon demo และ automated research. ผู้เล่าตั้งข้อสงสัยกับ benchmark ที่ effort ไม่เท่ากันเอง และยอมรับว่ายังเข้าใช้ Sol ไม่ได้ตอนอัดคลิป. ข้อสรุปจึงเป็น “สูสีหรือชนะบางงานในราคาต่ำกว่า” ไม่ใช่ “Sol ชนะ Fable แล้ว”.

ใน [[kimi-k3-explained-prompt-engineering|Kimi K3 Explained!]] ช่องนี้ใช้กรอบ specialist vs generalist เพื่ออธิบาย [[kimi-k3|Kimi K3]]. ผู้พูดมองว่า K3 ขึ้น frontier ด้าน agentic coding แต่ยังตามหลังด้าน general chat, HLE และ hallucination บางตัว. คลิปยังโยง Kimi กับการเป็น base สำหรับ post-training และ token efficiency ทว่า transcript มีชื่อรุ่น/บริษัทเพี้ยน และยังไม่ได้ตรวจ Kimi blog กับ evaluator report ต้นทาง.

**ผลคือ:** เวลาใช้คลิปของช่องนี้ ต้องแยกกรอบคิดที่นำกลับมาใช้ได้ออกจากตัวเลขหรือ product claim ที่เล่าต่อจากแหล่งอื่น.

## See also

- [[chinas-models-no-longer-need-western-hardware]]
- [[stop-building-ai-agents-old-way]]
- [[longcat-2-0]]
- [[meituan]]
- [[latitude]]
- [[gpt-5-6-sol-fable-killer-prompt-engineering]]
- [[gpt-5-6-sol]]
- [[fable]]
- [[kimi-k3-explained-prompt-engineering]]
- [[kimi-k3]]
