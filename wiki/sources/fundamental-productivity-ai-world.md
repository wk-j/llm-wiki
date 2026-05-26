---
title: Fundamental of productivity in AI world
type: source
tags: [ai, productivity, management, workflow]
created: 2026-05-25
updated: 2026-05-25
author: "[[chrisza-stuff|ChrisZa Stuff]]"
url: "https://www.youtube.com/watch?v=aPb18hv5wBY"
published: 2026-05-24
sources: []
---

# Fundamental of productivity in AI world / รากฐาน productivity ในโลก AI

วิดีโอนี้ของ [[chrisza-stuff|ChrisZa Stuff]] (ผู้ทำคอนเทนต์ไทยเรื่องเทคโนโลยีและการทำงาน) ชวนมองคำว่า productivity ใหม่ในยุคที่ AI ทำให้การผลิตเอกสาร โค้ด หรือ artifact เร็วขึ้นมาก แก่นของคลิปคือ productivity ไม่ใช่การที่คนหนึ่งคนผลิตของได้เยอะขึ้น แต่คือจังหวะที่งานถูกส่งต่อและอีกฝ่ายยอมรับเอาไปใช้ต่อได้จริง

## Key takeaways

### 1. Productivity ไม่ใช่ efficiency หรือ effectiveness

ChrisZa แยก productivity ออกจาก efficiency และ effectiveness อย่างชัดเจน Efficiency คือทำสิ่งหนึ่งด้วยต้นทุนน้อยลง ส่วน effectiveness คือทำสิ่งที่ควรทำได้ผล แต่ productivity ในคลิปนี้หมายถึงมูลค่าที่เกิดจากการแลกเปลี่ยนระหว่างคนอย่างน้อยสองฝ่าย

เขาเริ่มจากเลนส์เศรษฐศาสตร์ คนหนึ่งส่งสินค้า อีกคนส่งเงินกลับมา ถ้าทั้งสองฝ่าย consent และ win-win ก็เกิด productivity gain ในระบบ ถ้าผลิตของไว้เต็มโกดังแต่ไม่มีใครเอาไปใช้ นั่นไม่ใช่ productivity แต่เป็น waste

ได้อะไร: เวลาใช้ AI ต้องไม่ถามแค่ว่า "เราผลิตได้เร็วขึ้นไหม" แต่ต้องถามว่า "คนถัดไปเอาไปใช้ได้ดีขึ้นไหม"

### 2. Productivity อยู่ที่เส้น ไม่ใช่ที่คน

ประโยคหลักของคลิปคือ productivity ต้องมี human interaction อย่างน้อยสองคน งานจึงควรถูกวัดที่ "เส้น" ระหว่าง producer กับ consumer ไม่ใช่ดูแต่ output ของ producer

ตัวอย่างในทีมซอฟต์แวร์คือ คนหนึ่งส่ง intent หรือ requirement อีกคนทำ design แล้วอีกคนเขียน code ถ้า requirement ถูกสร้างไว้เฉย ๆ แต่คนถัดไปใช้ไม่ได้ งานนั้นยังไม่เกิด productivity ต่อให้มันดูสมบูรณ์ตามฟอร์มก็ตาม

นี่คือฐานของ [[interaction-productivity|Interaction Productivity]]: productivity จริงเกิดตอนงานข้ามมือสำเร็จ ไม่ใช่ตอน artifact ถูกผลิต

ได้อะไร: การเพิ่ม productivity ต้องปรับ interface ระหว่างคน ไม่ใช่เร่งคนใดคนหนึ่งแยกจากระบบ

### 3. AI ทำให้ producer เร็วขึ้น แต่ consumer ไม่ได้เร็วตาม

ในโลกก่อน AI หลายองค์กรวัด individual productivity ได้พอประมาณ เพราะมี standard กลาง เช่น document template, UML diagram, coding convention หรือ requirement format คนที่ส่งงานและคนที่รับงานต่างรู้กติกาเดียวกัน

แต่ AI ทำให้ producer conform to standard ได้ง่ายมาก ถ้า requirement ต้องมี 4 หัวข้อ เราสั่ง AI ให้สร้าง requirement ตามฟอร์มได้วันละพันชิ้น ปัญหาคือ consumer ยังอ่าน ยอมรับ และรับผิดชอบงานได้เท่าเดิม

ตรงนี้เชื่อมกับ [[local-optimization-trap|Local Optimization Trap]] และ [[theory-of-constraints|Theory of Constraints]]: การเร่งจุดที่ไม่ใช่คอขวด ทำให้งานไปกองที่จุดรับงาน

ได้อะไร: AI อาจเพิ่ม output แต่ไม่ได้เพิ่ม throughput ถ้าจุด acceptance ยังเป็นคอขวดเดิม

### 4. Acceptance automate ไม่ได้แบบตรง ๆ

ChrisZa เน้นว่า acceptance ระหว่างคนสองคนไม่ใช่แค่การตรวจ syntax หรือเช็ก checklist แต่คือการที่คนรับงานยอมรับว่า "ฉันโอเคที่จะรับงานนี้ไปทำต่อ" พร้อมความรับผิดชอบต่อผลลัพธ์

AI ช่วย review หรือช่วยอ่านได้ แต่ถ้าองค์กรพยายาม automate acceptance จนคนรับงานแค่กดรับโดยไม่ตรวจ ระบบจะสร้าง culture of irresponsibility: ทุกคนรับเร็ว ปล่อยผ่านเร็ว แล้วโยนความเสียหายให้คนถัดไป

นี่คือฐานของ [[acceptance-bottleneck|Acceptance Bottleneck]]: จุดยอมรับงานเป็นทั้งคอขวดทางเวลาและคอขวดทางความรับผิดชอบ

ได้อะไร: ต้องเร่งการทำความเข้าใจและการตัดสินใจของคนรับงาน ไม่ใช่บังคับให้คนรับเร็วขึ้นโดยไม่เข้าใจ

### 5. Standard เดิมอาจไม่ fair balance ในยุค AI

ก่อน AI standard ที่ดีควร balance workload ระหว่าง producer กับ consumer ไม่ให้คนเขียนสบายเกินไปจนคนอ่านต้องเดาเอง และไม่ให้คนเขียนต้องอธิบายทุกอย่างจนเกินจำเป็น

หลัง AI balance นี้เปลี่ยน Producer มีต้นทุนการสร้าง artifact ต่ำลงมาก แต่ consumer ยังมีต้นทุนการอ่าน ตรวจ และรับผิดชอบสูงเหมือนเดิม คำถามของคลิปคือ standard เดิมยัง fair อยู่ไหม ถ้าไม่ ควรมี standard ใหม่ที่ช่วยเร่งเส้นการส่งต่อ ไม่ใช่เร่ง output ของคนหนึ่งคน

นี่คือ [[ai-era-standard-balance|AI-era Standard Balance]]: standard ที่ดีในยุค AI ต้องลดภาระคนรับงานด้วย ไม่ใช่แค่ทำให้คนส่งงานผลิตง่ายขึ้น

ได้อะไร: template, doc format, design spec และ review process ควรถูกออกแบบใหม่จากมุม consumer

## ความสัมพันธ์กับ source อื่น

คลิปนี้เข้ากับ [[jeeraphan-lairat-ai-coding-speed|บทความของ Jeeraphan Lairat]] เรื่อง AI เขียนโค้ดเร็วขึ้น 10 เท่าแต่ lead time ยังไม่ลด ทั้งสองแหล่งบอกว่า productivity รวมไม่ได้ขึ้นจากการเร่ง coding เฉย ๆ

แต่ ChrisZa เพิ่มเลนส์ human interaction เข้าไป: คอขวดไม่ใช่แค่ stage ใน process แต่คือการยอมรับงานระหว่างคน งานจึงต้องถูกออกแบบให้ผ่านมือคนถัดไปได้จริง

คลิปยังเชื่อมกับ [[html-artifacts|HTML Artifacts]] เพราะตัวอย่างต้นคลิปพูดถึงเอกสาร HTML interactive ที่ทำให้คนเขียนกับคนอ่านเข้าใจกันเร็วขึ้น นี่เป็นตัวอย่างของการปรับ artifact ให้ช่วยเส้นการส่งต่อ ไม่ใช่แค่ทำเอกสารให้ดูเยอะขึ้น

## See also

- [[interaction-productivity]]
- [[acceptance-bottleneck]]
- [[ai-era-standard-balance]]
- [[local-optimization-trap]]
- [[lead-time]]
- [[theory-of-constraints]]
- [[html-artifacts]]
