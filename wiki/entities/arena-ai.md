---
title: Arena.ai
type: entity
tags: [organization, benchmark, lmsys, chatbot-arena]
created: 2026-04-28
updated: 2026-04-28
sources: [peter-gostev-what-models-suck-at.md]
---

# Arena.ai (Chatbot Arena) / อารีนา เอไอ

**Arena.ai** (หรือรู้จักกันในนาม LMSYS Chatbot Arena) เป็นแพลตฟอร์มมาตรฐานสำหรับการวัดประสิทธิภาพของ LLM ผ่านการทำ "Blind Test" โดยให้ผู้ใช้เปรียบเทียบคำตอบจากโมเดลสองตัวที่ไม่เปิดเผยชื่อแล้วโหวตเลือกตัวที่ชอบมากกว่า

## กลไกการทำงาน

1. **Battle Mode**: ผู้ใช้ใส่ Prompt และได้รับคำตอบจากโมเดล A และ B
2. **Voting**: ผู้ใช้เลือกว่า A ดีกว่า, B ดีกว่า, เสมอกัน หรือ "แย่ทั้งคู่" ([[dissatisfaction-rate]])
3. **Elo Rating**: ระบบจะคำนวณคะแนน Elo เพื่อจัดอันดับ Leaderboard ของโมเดลทั่วโลก

## ความสำคัญ

ในยุคที่ benchmark แบบเดิมๆ (เช่น MMLU) เริ่มถูก "ปนเปื้อน" (Contamination) ข้อมูลจาก Arena.ai ถือว่าเป็นแหล่งข้อมูลที่น่าเชื่อถือที่สุด เพราะเป็นการวัดผลจาก Prompt ของผู้ใช้จริงๆ ในสถานการณ์จริง และไม่สามารถเตรียมตัวมาเพื่อโกงคะแนนล่วงหน้าได้

## ข้อมูลสถิติ (ณ เมษายน 2026)

- มีผลโหวตมากกว่า 5.5 ล้านโหวต
- ติดตามโมเดลมากกว่า 700 รุ่น ทั้งแบบ Open-source และ Closed-source
- มีการแบ่งหมวดหมู่การทดสอบที่ละเอียด เช่น Coding, Hard Prompts, และ Expert Categories

## ดูเพิ่ม

- [[peter-gostev]]
- [[dissatisfaction-rate]]
