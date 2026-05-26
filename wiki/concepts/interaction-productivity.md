---
title: Interaction Productivity
type: concept
tags: [productivity, ai, workflow, management]
created: 2026-05-25
updated: 2026-05-25
sources: [fundamental-productivity-ai-world.md]
---

# Interaction Productivity / productivity ที่เกิดตรงการส่งต่อ

Interaction Productivity คือมุมมองว่า productivity จริงเกิดตรงที่งานถูกส่งต่อจากคนหนึ่งไปสู่อีกคนหนึ่ง แล้วคนรับเอาไปใช้ต่อได้ ไม่ใช่เกิดแค่ตอน producer ผลิต artifact ออกมา

แนวคิดนี้มาจาก [[chrisza-stuff|ChrisZa Stuff]] (ผู้ทำคอนเทนต์ไทยเรื่อง AI และการทำงาน) ในวิดีโอ [[fundamental-productivity-ai-world|Fundamental of productivity in AI world]] เขาบอกให้มอง productivity ที่ "เส้น" ระหว่างคน ไม่ใช่ที่ตัวคน

## แก่นความคิด

ถ้าคนหนึ่งเขียน requirement ได้เร็วขึ้น 10 เท่า แต่คนถัดไปอ่านแล้วใช้ไม่ได้ งานนั้นไม่ได้เพิ่ม productivity รวม มันแค่เพิ่มของค้างในระบบ

ในภาพนี้ artifact มีค่าเมื่อมันผ่านมือได้:

- intent ถูกส่งให้ designer แล้ว designer เข้าใจ
- design ถูกส่งให้ engineer แล้ว engineer ทำต่อได้
- code ถูกส่งให้ reviewer แล้ว reviewer ยอมรับได้
- product ถูกส่งให้ customer แล้ว customer จ่ายเงินหรือยืนยันว่าใช้ได้

ผลคือ: productivity ไม่ใช่ output count แต่คือ accepted transfer

## ทำไม AI ทำให้เรื่องนี้สำคัญขึ้น

AI ลดต้นทุนการผลิต artifact อย่างแรง คนหนึ่งคนจึงปั่น spec, doc, code, mockup หรือ analysis ได้มากกว่าเดิมหลายเท่า แต่คนรับงานยังมีข้อจำกัดเดิม คือเวลา ความเข้าใจ trust และความรับผิดชอบ

ถ้าองค์กรยังวัดรายคนเหมือนเดิม จะเห็นตัวเลข producer ดีขึ้น แต่ไม่เห็นว่าคนถัดไปกำลังจมกับงานที่ต้องอ่าน ต้องเช็ก และต้องรับผิดชอบ นี่คือญาติใกล้กับ [[local-optimization-trap|Local Optimization Trap]]

ได้อะไร: การใช้ AI ให้คุ้มต้องถามว่า AI ลด friction ในการส่งต่อหรือเปล่า ไม่ใช่แค่ผลิตของได้มากขึ้นหรือเปล่า

## วิธีออกแบบจากเลนส์นี้

ให้เริ่มจาก consumer ของงานก่อน คนถัดไปต้องตัดสินใจอะไร ต้องเชื่ออะไร ต้องเห็น evidence อะไร และต้องรับผิดชอบส่วนไหน จากนั้นค่อยออกแบบ artifact ให้ตอบโจทย์นั้น

ตัวอย่างเช่น [[html-artifacts|HTML Artifacts]] ไม่ได้ดีเพราะเป็น HTML เฉย ๆ แต่ดีเมื่อมันช่วยให้คนอ่านเห็นกราฟ คลิกดูส่วนสำคัญ และตัดสินใจได้เร็วกว่า Markdown ยาว ๆ

ผลคือ: format ที่ดีคือ format ที่ช่วย acceptance ไม่ใช่ format ที่ทำให้ producer เขียนง่ายอย่างเดียว

## See also

- [[acceptance-bottleneck]]
- [[ai-era-standard-balance]]
- [[lead-time]]
- [[theory-of-constraints]]
- [[html-artifacts]]
