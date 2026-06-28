---
title: Google DeepMind
type: entity
tags: [org, ai, lab, research]
created: 2026-06-26
updated: 2026-06-26
sources: [Self Learning for Agents Clearly Explained.md]
---

# Google DeepMind

ห้องวิจัย AI ของ Google. ในวิกินี้ปรากฏใน [[self-learning-for-agents-explained]] ผ่าน **AlphaEvolve** — coding agent ที่เป็นตัวอย่างโน้มน้าวที่สุดของ self-learning ชั้น Model (ดู [[three-learning-layers]]).

AlphaEvolve ทำงานเป็น loop: เสนอ code change → ให้คะแนนอัตโนมัติ → เก็บตัวชนะ → วนซ้ำ. ผลที่อ้าง:

- ทำ attention kernel เร็วขึ้น **32.5%**
- เจอทางลัด matrix-multiplication ที่ไม่มีใครล้มได้ตั้งแต่ **1969**
- ทำให้การเทรน model ของตัวเองเร็วขึ้น — **AI ปรับ AI ที่มันรันอยู่**

**ข้อจำกัด:** รันได้แค่ที่คอมพิวเตอร์ให้คะแนนได้ฟรี — code กับ math. พอเป็นงาน support/sales ที่ไม่มี free scorer วิธีนี้ใช้ไม่ได้ ซึ่งเป็นเหตุผลที่ self-learning ชั้น Model อยู่แต่ใน lab.

## See also

- [[three-learning-layers]]
- [[self-learning-for-agents-explained]]
- [[reward-hacking]]
