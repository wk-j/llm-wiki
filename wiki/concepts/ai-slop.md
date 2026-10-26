---
title: AI Slop
type: concept
tags: [ai, quality, design, critique]
created: 2026-04-28
updated: 2026-10-23
sources: [chase-ai-claude-code-impeccable.md, mario-zechner-pi-agent.md, maggies-appleton-collaborative-ai-engineering.md, ai-language-crisis-phenomenon.md, eternal-sloptember.md, never-been-better-time-to-go-into-math-3blue1brown.md]
---

# AI Slop / ขยะ AI

**AI Slop** เป็นคำที่ใช้เรียกผลลัพธ์จาก AI (ไม่ว่าจะเป็น ข้อความ, รูปภาพ, หรือ โค้ด) ที่มีคุณภาพต่ำ, ดูจืดชืด, มีความผิดพลาดแฝงอยู่ หรือดูเป็น "ผลงานสำเร็จรูป" ที่ขาดรสนิยมและความคิดสร้างสรรค์ของมนุษย์ มักเกิดจากการสั่งงาน (prompting) ที่กว้างเกินไปหรือไม่ใช้คำศัพท์เฉพาะทางที่ถูกต้อง

## ประเภทของ AI Slop

- **Text/Language Slop:** งานเขียนที่ใช้คำฟุ่มเฟือย, โครงสร้างประโยคซ้ำซาก (เช่น "ไม่ใช่แค่... แต่คือ..."), หรือคำศัพท์ยอดฮิตที่ AI ชอบใช้ (delve, unlock) จนทำให้ภาษาดูจืดชืดและขาดอารมณ์ความรู้สึกของมนุษย์ (ดูเพิ่มที่ [[ai-language-crisis-phenomenon]])
- **Visual/Design Slop:** งานออกแบบ UI ที่ดูเป็นแพทเทิร์นซ้ำๆ (เช่น bento box แบบเดิมๆ หรือสีที่ดูตุ่นๆ) ขาดความเข้าใจในเรื่อง hierarchy, typography และ spatial design ที่ดี
- **Code Slop (Clanker Slop):** โค้ดที่ AI เขียนออกมาแบบขอไปที มีความซับซ้อนเกินจำเป็น หรือดูเหมือนจะทำงานได้แต่แฝงไปด้วย bug (ดูเพิ่มที่ [[clanker-slop]])
- **Vibecoded Slop:** ผลงานที่เน้น "ความรู้สึก" ว่าใช่ แต่เชิงเทคนิคแล้วใช้งานจริงไม่ได้หรือไม่เสถียร (ดูเพิ่มที่ [[vibecoded-slop]])
- **Polished Slop:** ใน [[eternal-sloptember|The Eternal Sloptember]] slop ที่น่ากลัวที่สุดไม่ใช่งานพังชัด ๆ แต่คืองานที่ดูถูก syntax ดี structure ดี แต่ process ข้างหลังไม่ได้เข้าใจระบบจริง จึงทำให้ [[quality-proxy-collapse|quality proxy collapse]]

## สาเหตุและวิธีแก้

1. **Lack of Vocabulary:** [[chase-ai]] ชี้ให้เห็นว่าสาเหตุที่งาน UI ออกมาเป็น slop เพราะผู้สั่งงานไม่ใช้ภาษาของ designer (nomenclature) วิธีแก้คือการใช้เครื่องมืออย่าง [[impeccable]] เพื่อสอน "รสนิยม" และมาตรฐานให้ AI
2. **Laziness (No Human in the Loop):** การปล่อยให้ AI ทำงานโดยไม่มีมนุษย์คอยคัดกรองหรือปรับแต่ง (curation)
3. **Prompt Mediocrity:** การใช้ prompt ที่ธรรมดาเกินไป จะได้ผลลัพธ์ที่เป็นค่าเฉลี่ยของข้อมูลที่ AI ถูก train มา (ซึ่งมักจะจืดชืด)

## payoff
การตระหนักถึง AI Slop ช่วยให้นักพัฒนาและนักออกแบบไม่หยุดเพียงแค่ผลลัพธ์แรกที่ AI มอบให้ แต่พยายามขัดเกลาและใช้เครื่องมือเสริมเพื่อสร้างงานที่โดดเด่นและมีคุณภาพจริง

## คำถามเปิด: slop เป็นแค่ช่วงชั่วคราวไหม

แหล่งใน wiki ยังเห็นไม่ตรงกันว่า slop จะหายไปเองเมื่อ model เก่งขึ้นหรือไม่ wiki เก็บไว้ทั้งสองฝั่ง

- **ฝั่งที่คิดว่าชั่วคราว** [[3blue1brown|3Blue1Brown]] (ช่อง YouTube สอนคณิตศาสตร์) บอกใน [[never-been-better-time-to-go-into-math-3blue1brown|วิดีโอเรื่องอนาคตของคณิตศาสตร์]] ว่า proof จาก model ตอนนี้อ่านยาก แต่น่าจะดีขึ้น เพราะบริษัททำ model มีแรงจูงใจให้ model อธิบายเก่ง เขาเทียบกับ code จาก model ที่เขาเห็นว่าช่วงแรกทำงานได้แต่ยังรก แล้วเดินไปทางสะอาดขึ้น เขายอมรับเองว่ามีคนเถียง และ model ยัง comment เยอะเกิน
- **ฝั่งที่เห็นว่ายังไม่หาย** [[dhh|DHH]] ใน [[make-it-simpler|Make It Simpler]] เล่าว่า agent ยังเขียน code ซับซ้อนเกินจำเป็นบ่อย และ agent ที่ review ก็ปล่อยผ่าน ส่วน [[eternal-sloptember|The Eternal Sloptember]] เถียงว่าปัญหาอาจอยู่ที่ชนิดของ model ไม่ใช่ความเรียบร้อย ถ้าเป็นแบบนั้น output ที่ดูสะอาดขึ้นอาจกลายเป็น polished slop แทน

สองฝั่งพูดถึงคนละอย่างอยู่บางส่วน 3B1B พูดถึงความอ่านง่ายของคำอธิบาย อีกฝั่งพูดถึงความซับซ้อนและความเข้าใจข้างหลังงาน ยังไม่มีแหล่งไหนวัดว่า output จาก model สะอาดขึ้นจริงตามเวลาหรือไม่

## See also

- [[clanker-slop]]
- [[vibecoded-slop]]
- [[quality-proxy-collapse]]
- [[impeccable]]
- [[chase-ai]]
- [[make-it-simpler]]
- [[eternal-sloptember]]
- [[never-been-better-time-to-go-into-math-3blue1brown]]
