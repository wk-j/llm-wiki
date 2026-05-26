---
title: Acceptance Bottleneck
type: concept
tags: [productivity, ai, workflow, bottleneck]
created: 2026-05-25
updated: 2026-05-25
sources: [fundamental-productivity-ai-world.md]
---

# Acceptance Bottleneck / คอขวดตรงการยอมรับงาน

Acceptance Bottleneck คือคอขวดที่เกิดตอนคนรับงานต้องยอมรับว่า artifact ชิ้นหนึ่งดีพอที่จะเอาไปทำต่อได้ จุดนี้ไม่ได้เป็นแค่ review checklist แต่เป็นการรับผิดชอบต่อสิ่งที่จะเกิดขึ้นหลังจากรับงาน

แนวคิดนี้มาจาก [[chrisza-stuff|ChrisZa Stuff]] ใน [[fundamental-productivity-ai-world|Fundamental of productivity in AI world]] เขาแยก "ผลิต artifact" ออกจาก "accept งาน" อย่างชัดเจน AI ทำอย่างแรกได้เร็วมาก แต่อย่างหลังยังเป็น human interaction

## ทำไม acceptance automate ยาก

AI ช่วยอ่าน ช่วยสรุป ช่วยตรวจ และช่วยเตือน risk ได้ แต่การบอกว่า "ฉันรับงานนี้แล้ว จะเอาไปทำต่อ" ยังผูกกับ judgment และ accountability ของคน

ถ้าองค์กรบังคับให้ acceptance เร็วขึ้นโดยไม่ให้คนเข้าใจงานจริง ๆ คนจะเริ่มรับผ่าน ๆ แล้วโยนปัญหาให้คนถัดไป สุดท้ายจะเกิด culture of irresponsibility: ไม่มีใครเป็นเจ้าของคุณภาพจริง แต่ทุกคนมีหลักฐานว่า "ฉันทำตาม process แล้ว"

ผลคือ: automation ที่ดีควรช่วยให้คน accept ได้มั่นใจขึ้น ไม่ใช่แทนที่การ accept ของคน

## อาการในทีม AI

อาการที่เห็นได้บ่อยคือ producer ใช้ AI สร้าง output ได้เร็วกว่าเดิมมาก แต่ reviewer, QA, designer, PM หรือ customer ยังต้องใช้เวลาทำความเข้าใจเท่าเดิม งานจึงค้างตรงจุดรับงาน

นี่ต่อกับ [[theory-of-constraints|Theory of Constraints]] โดยตรง ความเร็วรวมของระบบไม่เท่ากับความเร็ว producer แต่เท่ากับความเร็วของจุด acceptance ที่ช้าที่สุด

ตัวอย่าง:

- AI เขียน code ได้เร็ว แต่ code review ค้าง
- AI สร้าง requirement ได้เยอะ แต่ designer ไม่รู้ว่า priority ไหนสำคัญ
- AI ทำ report ได้ยาว แต่ executive ไม่มีเวลาตัดสินใจจากมัน

ได้อะไร: ถ้า acceptance เป็นคอขวด การเพิ่ม output ก่อน acceptance จะเพิ่ม waste

## วิธีลดคอขวดนี้

ลดงานของคนรับโดยทำ artifact ให้ตัดสินใจง่ายขึ้น ใส่ context ที่จำเป็น evidence ที่ตรวจได้ และทางเลือกที่ชัด ไม่ใช่เพิ่มรายละเอียดทุกอย่างจนอ่านยากกว่าเดิม

อีกวิธีคือรวม role บางส่วนเข้าด้วยกันเมื่อเหมาะสม เช่น คนเดียวถือทั้ง intent และ design ในงานเล็ก เพื่อลดจังหวะส่งต่อ แต่ต้องแยกเรื่อง productivity ออกจากเรื่อง labor fairness เพราะเป็นคนละคำถาม

ผลคือ: จุดที่ควร optimize คือความเข้าใจและความรับผิดชอบของคนรับ ไม่ใช่จำนวน artifact ที่ส่งเข้า queue

## Ball's counter framing

[[thorsten-ball|Thorsten Ball]] ใน [[software-after-software]] ข้อ 4 พูดเรื่องคอขวดเหมือนกันแต่ในมุมต่างออกไป: "Review will shift from code to decisions" — review ของ code หายไป แต่ review ของ decisions ยังอยู่

ความต่าง:

- ChrisZa: คอขวด acceptance อยู่กับ "consumer เข้าใจและรับผิดชอบงานก่อนเดินต่อ" — ฝั่งคนรับ
- Ball: คอขวดอยู่ที่ "engineering decisions" (priorities, sequencing, tradeoffs) — ฝั่งคนสั่ง

สองมุมเสริมกัน: ถ้า decisions ดี acceptance ก็ง่ายขึ้น แต่ถ้า decisions ไม่ดี acceptance จะยังค้าง แม้ AI จะเร็วแค่ไหน

## See also

- [[interaction-productivity]]
- [[ai-era-standard-balance]]
- [[local-optimization-trap]]
- [[lead-time]]
- [[limit-wip]]
- [[software-after-software]]
- [[process-drag]]
