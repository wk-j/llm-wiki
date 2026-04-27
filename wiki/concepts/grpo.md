---
title: Group Relative Policy Optimization
type: concept
tags: [ai, deepseek, reinforcement-learning, reasoning]
created: 2026-04-27
updated: 2026-04-27
sources: [deepseek-wikipedia.md]
---

# Group Relative Policy Optimization (GRPO) / กรุ๊ป เรลลาทีฟ พอลิซี ออปติไมเซชัน

เทคนิค Reinforcement Learning (RL) ที่ **[[deepseek|DeepSeek]]** ใช้ฝึก model สายเหตุผล (Reasoning) อย่าง DeepSeek-R1 โดยไม่ต้องพึ่งพาตัวให้คะแนน (Reward Model) แยกต่างหาก

## แก่นความคิด

โดยปกติการทำ RL ให้ AI (เช่น PPO) จะต้องมี "Reward Model" อีกตัวหนึ่งมาคอยบอกว่าคำตอบที่ AI ตอบมานั้นดีแค่ไหน ซึ่งการสร้าง Reward Model ให้แม่นยำนั้นทำยากและกินทรัพยากรสูง

GRPO เปลี่ยนวิธีใหม่โดยการให้ AI ลองตอบคำถามเดียวกันออกมา **"เป็นกลุ่ม" (Group)** หลายๆ แบบ แล้วเอาคำตอบในกลุ่มนั้นมาเปรียบเทียบกันเอง (Relative) เพื่อหาว่าอันไหนดีที่สุดตามเกณฑ์ที่กำหนด (เช่น คำตอบในรูปแบบ XML ที่ถูกต้อง หรือผลลัพธ์การคำนวณที่ตรงเป้า)

## Why this helps / ผลคือ

- **ตัดความยุ่งยากของ Reward Model:** ไม่ต้องเสียเวลา train model ตัวที่สองมาคอยคุม
- **Efficiency สูง:** ใช้ทรัพยากรในการฝึกน้อยกว่าวิธีดั้งเดิมมาก
- **เหมาะกับงาน Reasoning:** ช่วยให้ AI ฝึกกระบวนการคิด (Chain of Thought) ได้อย่างเป็นธรรมชาติผ่านการลองผิดลองถูกและเปรียบเทียบตัวเอง

## See also

- [[deepseek]]
- [[adaptive-thinking]]
