---
title: Dissatisfaction Rate
type: concept
tags: [metric, user-experience, llm, arena-ai]
created: 2026-04-28
updated: 2026-04-28
sources: [peter-gostev-what-models-suck-at.md]
---

# Dissatisfaction Rate / อัตราความไม่พอใจ

**Dissatisfaction Rate** เป็นตัวชี้วัดที่ใช้ใน [[arena-ai|Chatbot Arena]] เพื่อระบุจำนวนครั้งที่ผู้ใช้เลือกโหวต "แย่ทั้งคู่" (Both models are bad) เมื่อเปรียบเทียบคำตอบจากโมเดลชั้นนำสองตัว

## ความสำคัญ

ในขณะที่คะแนน Elo บอกว่าใคร "เก่งกว่าใคร" แต่ **Dissatisfaction Rate** บอกเราว่า "เรามาถึงจุดที่ AI แก้ไขปัญหาได้จริงหรือยัง" 
- ถ้า Elo สูงแต่ Dissatisfaction Rate ยังสูง แปลว่าโมเดลตัวนั้นแค่ "ห่วยน้อยกว่า" ตัวอื่นในงานประเภทนั้นๆ

## เทรนด์ที่น่าสนใจ (2023-2026)

1. **Overall Progress**: อัตราความไม่พอใจลดลงจาก ~17% (ยุค GPT-4 แรกเริ่ม) เหลือประมาณ 9% ในปัจจุบัน
2. **Category Variance**:
    - **Math**: ลดลงอย่างมาก แสดงว่า AI เริ่มเก่งเรื่องตัวเลขจริงๆ
    - **Creative Writing/Gaming**: แทบไม่ลดลงเลย สะท้อนว่า AI ยังขาด "วิญญาณ" หรือความเข้าใจในบริบทที่ต้องอาศัยรสนิยม
3. **The Expert Wall**: ในหมวดหมู่ผู้เชี่ยวชาญ (Expert) อัตราความไม่พอใจมักจะสูงกว่าปกติ (ประมาณ 13%+) เพราะงานมีความซับซ้อนเกินกว่าที่โมเดลจะทำได้ในขั้นตอนเดียว

## ดูเพิ่ม

- [[arena-ai]]
- [[peter-gostev]]
