---
title: Alignment Bottleneck
type: concept
tags: [management, engineering, ai, productivity]
created: 2026-04-28
updated: 2026-04-28
sources: [maggie-appleton-collaborative-ai-engineering.md]
---

# Alignment Bottleneck / คอขวดด้านความสอดประสาน

**Alignment Bottleneck** คือสภาวะที่การสร้างซอฟต์แวร์ถูกจำกัดด้วย "ความไม่เข้าใจที่ตรงกันของคนในทีม" มากกว่า "ความเร็วในการเขียน code" ปัญหานี้รุนแรงขึ้นอย่างมากเมื่อมีการนำ AI Agent มาใช้

## ทำไม Alignment ถึงกลายเป็นคอขวด?

1. **Cheap Implementation**: เมื่อการเขียน code แทบจะฟรีและทำได้ทันที ความยากจึงย้ายไปอยู่ที่การตัดสินใจว่า "เรากำลังเดินไปถูกทางไหม?"
2. **Collapse of Time**: ในอดีต กระบวนการที่ช้า (เช่น การรอ Review) ให้เวลาคนในทีมได้คิดและปรับจูนความเข้าใจ เมื่อช่วงเวลานี้หายไป (Implementation Window Collapsed) ทุกคนจะวิ่งไปคนละทิศละทางด้วยความเร็วสูง
3. **High Opportunity Cost**: เพราะเราทำได้ทุกอย่าง ค่าเสียโอกาส (Opportunity Cost) จึงเป็นต้นทุนที่แท้จริง การเลือกทำสิ่งที่ "ไม่ใช่" แม้จะทำได้เร็ว ก็คือการเสียทรัพยากรไปเปล่าๆ

## สัญญาณของปัญหา

- มี Pull Request (PR) กองเป็นตั้งที่ไม่มีใครกล้าตรวจ เพราะไม่รู้ที่มาที่ไป
- มี feature ใหม่ๆ โผล่มาในระบบที่ไม่มีใครสั่งให้ทำ
- เกิด merge conflict รุนแรงเพราะ Agent หลายตัวรุมแก้ไขไฟล์เดียวกัน

## วิธีแก้

ต้องเปลี่ยนจากการเน้น "Output" (ปริมาณ code) ไปเน้น "Outcome" (ผลลัพธ์ที่ต้องการ) และนำกระบวนการวางแผน (Planning) กลับมาเป็นหัวใจสำคัญ โดยใช้เครื่องมือที่รองรับการทำงานแบบ [[collaborative-ai-engineering|Collaborative AI Engineering]]

## ดูเพิ่ม

- [[collaborative-ai-engineering]]
- [[ace]]
- [[vibecoded-slop]]
- [[theory-of-constraints]]
- [[lead-time]]
