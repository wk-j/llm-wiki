---
title: World Models
type: concept
tags: [ai, reasoning, agents, cognition]
created: 2026-07-03
updated: 2026-09-07
sources: [eternal-sloptember.md, dhh-strategies-programming-with-ai-agents-lex-clips.md]
---

# World Models / โมเดลของโลก

World models คือ model ภายในที่ทำให้ระบบเข้าใจว่า action หนึ่งจะเปลี่ยนโลกหรือ environment อย่างไร. ในงาน software โลกนั้นอาจไม่ใช่โลกกายภาพ แต่เป็นระบบ code, state, invariant, tests, users, และ failure modes ที่ change หนึ่งไปกระทบ

## ทำไมเกี่ยวกับ programming agents

ใน [[eternal-sloptember|The Eternal Sloptember]] ผู้เขียนบอกว่า real programming agents ต้องมี world models มากกว่าแค่ทำนาย token หรือหาเส้นทางผ่าน test. เพราะ programming ต้องเข้าใจผลกระทบ ไม่ใช่แค่ผลิตข้อความ code ที่ดูเหมือนถูก

ตัวอย่างง่าย ๆ: agent ที่ไม่มี world model อาจ comment out failing test แล้วบอกว่าทุกอย่างผ่าน. มัน optimize สัญญาณภายนอก แต่ไม่ได้เข้าใจ behavior ที่ test เคยปกป้อง

## ความสัมพันธ์กับ harness

[[coding-harness|Coding harness]] และ verifier ช่วยบังคับ agent ให้เจอกับโลกจริงมากขึ้น เช่น run test, browser flow, fuzzing, typecheck, logs. แต่คำถามเปิดคือ world model ควรอยู่ใน model เอง, อยู่ใน memory/context, เกิดจาก tool interaction, หรือมาจากทั้งหมดรวมกัน

ได้อะไร: world model เป็นชื่อของสิ่งที่ขาดเมื่อ output ดูถูก แต่ process ข้างในยังไม่เข้าใจระบบจริง

## คำเดียวกัน แต่คนละความหมาย: live gaming model

ต้องระวังคำนี้ เพราะมีสองความหมายที่ปนกันง่าย

ความหมายที่หน้านี้พูดถึงข้างบนคือ **ความเข้าใจผลกระทบ** คือ agent รู้ว่าการแก้ตรงนี้ไปกระทบ state, invariant และ user อย่างไร

ความหมายที่สองคือ **model ที่ generate โลกออกมาเลย** [[dhh|DHH]] พูดถึงแบบนี้ใน [[dhh-strategies-programming-with-ai-agents-lex-clips|บทสัมภาษณ์กับ Lex Fridman]] คือ AI สาย live gaming ที่คิดเฟรมถัดไปของเกมขึ้นมาสด ๆ แล้วคนเล่นได้จริง เขาเอามาตั้งคำถามว่าถ้าทำกับเกมได้ ทำไมทำกับระบบปฏิบัติการไม่ได้ พูดกับเครื่องแล้วให้มันเปลี่ยนรูปตามที่สั่ง ([[malleable-tools]])

สองความหมายนี้เกี่ยวกันตรงที่ model ต้องเดาผลของ action ได้ แต่เป้าต่างกัน อันหนึ่งใช้เพื่อ **ตัดสินใจ** ในระบบที่มีอยู่จริง อีกอันใช้เพื่อ **สร้าง** สิ่งที่ยังไม่มี งานเกมยอมให้เพี้ยนได้ในระดับที่ระบบปฏิบัติการหรือ production code ยอมไม่ได้ ดังนั้นการอ้างความสำเร็จของฝั่งเกมมาสนับสนุนฝั่ง software จริงยังต้องมีข้อพิสูจน์เพิ่ม

## See also

- [[programming-process-matters]]
- [[quality-proxy-collapse]]
- [[behavioral-verifier]]
- [[coding-harness]]
- [[malleable-tools]]
- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
