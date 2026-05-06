---
title: AI Slop
type: concept
tags: [ai, quality, design, critique]
created: 2026-04-28
updated: 2026-04-28
sources: [chase-ai-claude-code-impeccable.md, mario-zechner-pi-agent.md, maggies-appleton-collaborative-ai-engineering.md, ai-language-crisis-phenomenon.md]
---

# AI Slop / ขยะ AI

**AI Slop** เป็นคำที่ใช้เรียกผลลัพธ์จาก AI (ไม่ว่าจะเป็น ข้อความ, รูปภาพ, หรือ โค้ด) ที่มีคุณภาพต่ำ, ดูจืดชืด, มีความผิดพลาดแฝงอยู่ หรือดูเป็น "ผลงานสำเร็จรูป" ที่ขาดรสนิยมและความคิดสร้างสรรค์ของมนุษย์ มักเกิดจากการสั่งงาน (prompting) ที่กว้างเกินไปหรือไม่ใช้คำศัพท์เฉพาะทางที่ถูกต้อง

## ประเภทของ AI Slop

- **Text/Language Slop:** งานเขียนที่ใช้คำฟุ่มเฟือย, โครงสร้างประโยคซ้ำซาก (เช่น "ไม่ใช่แค่... แต่คือ..."), หรือคำศัพท์ยอดฮิตที่ AI ชอบใช้ (delve, unlock) จนทำให้ภาษาดูจืดชืดและขาดอารมณ์ความรู้สึกของมนุษย์ (ดูเพิ่มที่ [[ai-language-crisis-phenomenon]])
- **Visual/Design Slop:** งานออกแบบ UI ที่ดูเป็นแพทเทิร์นซ้ำๆ (เช่น bento box แบบเดิมๆ หรือสีที่ดูตุ่นๆ) ขาดความเข้าใจในเรื่อง hierarchy, typography และ spatial design ที่ดี
- **Code Slop (Clanker Slop):** โค้ดที่ AI เขียนออกมาแบบขอไปที มีความซับซ้อนเกินจำเป็น หรือดูเหมือนจะทำงานได้แต่แฝงไปด้วย bug (ดูเพิ่มที่ [[clanker-slop]])
- **Vibecoded Slop:** ผลงานที่เน้น "ความรู้สึก" ว่าใช่ แต่เชิงเทคนิคแล้วใช้งานจริงไม่ได้หรือไม่เสถียร (ดูเพิ่มที่ [[vibecoded-slop]])

## สาเหตุและวิธีแก้

1. **Lack of Vocabulary:** [[chase-ai]] ชี้ให้เห็นว่าสาเหตุที่งาน UI ออกมาเป็น slop เพราะผู้สั่งงานไม่ใช้ภาษาของ designer (nomenclature) วิธีแก้คือการใช้เครื่องมืออย่าง [[impeccable]] เพื่อสอน "รสนิยม" และมาตรฐานให้ AI
2. **Laziness (No Human in the Loop):** การปล่อยให้ AI ทำงานโดยไม่มีมนุษย์คอยคัดกรองหรือปรับแต่ง (curation)
3. **Prompt Mediocrity:** การใช้ prompt ที่ธรรมดาเกินไป จะได้ผลลัพธ์ที่เป็นค่าเฉลี่ยของข้อมูลที่ AI ถูก train มา (ซึ่งมักจะจืดชืด)

## payoff
การตระหนักถึง AI Slop ช่วยให้นักพัฒนาและนักออกแบบไม่หยุดเพียงแค่ผลลัพธ์แรกที่ AI มอบให้ แต่พยายามขัดเกลาและใช้เครื่องมือเสริมเพื่อสร้างงานที่โดดเด่นและมีคุณภาพจริง

## See also

- [[clanker-slop]]
- [[vibecoded-slop]]
- [[impeccable]]
- [[chase-ai]]
