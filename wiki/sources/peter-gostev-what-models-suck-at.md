---
title: "What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench"
type: source
tags: [llm, benchmarks, arena-ai, bullshitbench, reasoning]
created: 2026-04-28
updated: 2026-04-28
sources: [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench.md]
---

# What Do Models Still Suck At? / สิ่งที่ LLM ยังคง "กาก" อยู่

Peter Gostev จาก [[arena-ai|Arena.ai]] (ผู้สร้าง LMSYS Chatbot Arena) นำเสนอมุมมองที่ขัดแย้งกับกระแส "กราฟพุ่งขึ้น" ของ benchmark ทั่วไป โดยชี้ให้เห็นว่ายังมีงานหลายอย่างที่โมเดลระดับโลกยังทำได้ไม่ดี และบางครั้งการ "คิด" (Reasoning) นานขึ้นกลับทำให้ผลลัพธ์แย่ลง

## Key Takeaways

- **BullshitBench**: Benchmark ที่ Peter สร้างขึ้นเพื่อทดสอบว่าโมเดลจะ "ผลักกลับ" (Push back) คำถามที่เป็นเรื่องไร้สาระ (Nonsense) หรือไม่
    - พบว่าโมเดลส่วนใหญ่พยายามจะ "ตอบให้ได้" แม้คำถามจะไม่มีความหมาย (เช่น ถามเรื่องความสัมพันธ์ระหว่างการย่อหน้า code กับความเร็วในการ deploy)
    - [[anthropic|Anthropic]] (Claude 4.5/Sonnet) ทำได้ดีที่สุดในการปฏิเสธคำถามไร้สาระ ในขณะที่ GPT และ Gemini ยังมีอาการ "ไหลตาม" (Accommodating) อยู่ประมาณ 50%
- **Reasoning Regression**: การเพิ่มขั้นตอนการคิด (Thinking/Reasoning) ไม่ได้ช่วยแก้ปัญหา BullshitBench เสมอไป บางครั้งโมเดลที่คิดเยอะกลับพยายามหาเหตุผลมาสนับสนุนเรื่องไร้สาระจนยาวเหยียด (เช่น GPT-5.4 ที่คิด 20 ย่อหน้าเพื่อแก้ปัญหาที่ไม่มีอยู่จริง)
- **Dissatisfaction Rate (อัตราความไม่พอใจ)**: ข้อมูลจาก Arena ที่เก็บมาตั้งแต่ปี 2023 ชี้ให้เห็นว่าแม้โมเดลจะเก่งขึ้น แต่อัตราที่ผู้ใช้ "ไม่ชอบทั้งสองรุ่น" (Dislike both) ยังสูงถึง 9% ในภาพรวม และสูงกว่านั้นมากในงานระดับผู้เชี่ยวชาญ (Expert)
- **Expert Category Gaps**:
    - **Math/Quantitative**: พัฒนาขึ้นอย่างก้าวกระโดด (อัตราไม่พอใจลดลงมาก)
    - **Creative Writing/Gaming**: พัฒนาช้ามาก โดยเฉพาะเรื่อง Game Mechanics ที่โมเดลยังไม่เข้าใจ "ความสนุก" หรือความซับซ้อนของเกมจริงๆ
    - **Finance/Law**: อัตราความไม่พอใจยังคงที่ ไม่ได้ลดลงตามความเก่งของโมเดลรุ่นใหม่ๆ
- **Expectation Shift**: กราฟ benchmark ที่พุ่งขึ้นอาจไม่ได้แปลว่าโมเดลฉลาดขึ้นอย่างเดียว แต่ผู้ใช้เองก็ตั้งความหวังสูงขึ้นและถามคำถามที่ยากขึ้นเรื่อยๆ ทำให้เกิดการต่อสู้ระหว่างความสามารถของโมเดลและความคาดหวังของมนุษย์

## Key Entities

- [[peter-gostev]]: ผู้เชี่ยวชาญด้าน AI และ Data จาก Arena.ai
- [[arena-ai]]: แพลตฟอร์มเปรียบเทียบโมเดล (LMSYS Chatbot Arena)
- [[bullshitbench]]: ชุดคำถามทดสอบการรับมือกับเรื่องไร้สาระ

## Key Concepts

- [[dissatisfaction-rate]]: ตัววัดว่าโมเดล "สอบตก" ทั้งคู่ในสายตาผู้ใช้
- [[reasoning-regression]]: สภาวะที่โมเดลยิ่งคิดเยอะยิ่งหลงทาง (Over-thinking nonsense)
- [[bullshit-detection]]: ความสามารถในการแยกแยะและปฏิเสธคำถามที่ผิดหลักการหรือไร้สาระ

## See also

- [[llm-coding-pitfalls]] — ปัญหาของ LLM ในงานเฉพาะทาง (Karpathy)
- [[taste-paradox]] — ความคาดหวังที่เพิ่มขึ้นตามความเก่งของ AI
