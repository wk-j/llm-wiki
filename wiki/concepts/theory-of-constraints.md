---
title: Theory of Constraints
type: concept
tags: [management, productivity, software-engineering, bottleneck]
created: 2026-04-28
updated: 2026-05-25
sources: [jeeraphan-lairat-ai-coding-speed.md, fundamental-productivity-ai-world.md]
---

# Theory of Constraints / ทฤษฎีข้อจำกัด (Bottleneck)

หลักการจัดการที่กล่าวว่า "ความเร็วของกระบวนการทั้งหมด จะเท่ากับความเร็วของส่วนที่ช้าที่สุด (Bottleneck) เท่านั้น"

ในบริบทของการพัฒนาซอฟต์แวร์ยุค AI:
- **Coding is not the bottleneck:** การเขียนโค้ดมักกินเวลาเพียง 10% ของ [[lead-time]] ทั้งหมด
- **The real bottlenecks:** มักอยู่ที่การรอคอย (Wait time) เช่น รอ Code Review, รอ Testing, หรือรอการตัดสินใจ
- **Local vs Global:** การเร่งสปีดที่จุด Coding (ซึ่งไม่ใช่คอขวด) จะไม่ช่วยให้งานถึงมือลูกค้าเร็วขึ้น แต่จะส่งผลให้งานไปกองรวมกันที่จุดถัดไปแทน (ดู [[local-optimization-trap]])
- **Acceptance as bottleneck:** ในเลนส์ของ [[chrisza-stuff|ChrisZa Stuff]] คอขวดสำคัญในยุค AI คือจุดที่คนรับงานต้องเข้าใจและยอมรับงาน ดู [[acceptance-bottleneck]]

## วิธีแก้
1. **ทำให้คอขวดมองเห็นได้:** เก็บข้อมูลระยะเวลาที่งานแช่อยู่ในแต่ละ stage
2. **ทลายคอขวด:** โฟกัสการปรับปรุงที่จุดที่ช้าที่สุดเท่านั้น
3. **[[limit-wip|จำกัดงานในมือ]]:** เพื่อไม่ให้งานไหลเข้า pipeline เร็วกว่าที่คอขวดจะรับไหว

## See also
- [[local-optimization-trap]]
- [[limit-wip]]
- [[alignment-bottleneck]]
- [[interaction-productivity]]
