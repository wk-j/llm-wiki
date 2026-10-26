---
title: Skill Atrophy
type: concept
tags: [psychology, ai, learning]
created: 2026-05-05
updated: 2026-10-23
sources: [dhh-strategies-programming-with-ai-agents-lex-clips.md, agentic-coding-trap.md, How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md, code-isnt-free-mario-zechner-hard-truths-coding-ai.md, teepagorn-claude-code-adoption-nobody-reading.md, never-been-better-time-to-go-into-math-3blue1brown.md]
---

# Skill Atrophy / ภาวะทักษะถดถอย

**Skill Atrophy** ในบริบทของ AI คือภาวะที่ทักษะการเขียนโปรแกรม การคิดเชิงวิพากษ์ (critical thinking) และการแก้ปัญหา (problem-solving) ของนักพัฒนาถดถอยลง เนื่องจากการปล่อยให้ AI Agent เป็นผู้คิดและลงมือทำแทนอยู่เป็นประจำ

นี่คือ **"The Supervision Paradox"** (ความย้อนแย้งของการคุมงาน) ที่บริษัทอย่าง Anthropic เตือนเอาไว้: การจะคุมและใช้งาน AI Agent ให้ได้ผลดีนั้นต้องอาศัยทักษะการเขียนโค้ดและ critical thinking ขั้นสูง แต่ทักษะเหล่านี้กลับเป็นสิ่งที่จะถดถอยลงเมื่อเราใช้งาน AI Agent มากเกินไป

[[lars-faye]] ชี้ให้เห็นว่าการเรียนรู้ของโปรแกรมเมอร์นั้นต้องอาศัย "ความยากลำบาก" (friction) การอ่านรีวิวโค้ดอย่างเดียวให้ผลแค่ 50% ของการเรียนรู้ เมื่อเราตัดความยากในการแก้บั๊กและการเขียนโค้ดด้วยตัวเองออกไป ทักษะการสร้าง mental model และ [[eh-gland]] ก็จะค่อยๆ หายไปตามด้วย ภาวะนี้สามารถเกิดขึ้นได้อย่างรวดเร็วในเวลาเพียงไม่กี่เดือน

## เส้นแบ่งสำหรับคนที่กำลังเรียน

ในช่วงถามตอบของ [[how-to-keep-shipping-away-from-desk|talk ของ Zack Proser]], คนฟังถามตรง ๆ ว่าวิธี delegate งานให้ agent จะทำให้คนต้นอาชีพเสียโอกาสฝึกหรือไม่. คำตอบของ [[zack-proser|Zack Proser]] คือ **อย่าใช้ AI ทำสิ่งที่เรายังทำเองไม่เป็น**.

นี่ไม่ใช่กฎห้ามใช้ AI ตอนเรียน. ใช้ agent ช่วยถามว่า mental model ตรงไหนยังมัว, ให้มัน quiz, หรือช่วยพาเรียนลึกขึ้นได้. แต่เรื่องที่กำลังสร้างพื้นฐานควรยังลงมือเขียน แก้ bug และเจอความเจ็บด้วยตัวเองก่อน. พอมีประสบการณ์พอจะจับ hallucination และ design แย่ได้แล้ว ค่อย delegate เพื่อเพิ่มความเร็ว.

**ได้อะไร:** ใช้ AI เร่งการเรียนโดยไม่ยกการสร้าง judgement ให้ AI ไปด้วย.

## Friction ที่สอน กับ friction ที่ขวาง

[[mario-zechner|Mario Zechner]] แยกเรื่องนี้ชัดใน [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]]. เขาเชื่อว่าการเรียนโปรแกรมต้องมี pain และ friction เพราะมันสร้าง mental model. แต่ friction ทุกชนิดไม่ได้มีค่าเท่ากัน. ตอนเขาเรียน electronics เขาให้ agent เขียน code MCU ส่วนที่เขารู้พื้นฐานดีอยู่แล้ว เพื่อเอาแรงไปเรียนวงจรจริง.

ดังนั้นคำถามที่ดีกว่า "ใช้ AI ตอนเรียนได้ไหม" คือ **friction ตรงนี้กำลังสอน skill ที่เราต้องการอยู่หรือเปล่า**. ถ้าใช่ ควรทำเอง. ถ้าไม่ใช่ และเป็นแค่งานประกอบที่ขวางการเรียนเรื่องหลัก agent อาจช่วยได้.

**ผลคือ:** ป้องกัน skill atrophy ด้วยการเลือก friction ไม่ใช่ด้วยการห้าม AI แบบกว้าง ๆ.

## เรื่องเล่าจากหน้างาน — DHH กลับคำเรื่อง bash (2026-09)

กรณีนี้น่าสนใจเพราะคนคนเดียวเปลี่ยนจุดยืนเองภายในไม่กี่เดือน และเปลี่ยนไปคนละทางกับคำแนะนำข้างบน

ใน [[dhh-ai-programming-setup-lex-clips|บทสัมภาษณ์ตอนก่อน]] [[dhh|DHH]] เล่าว่าเขาเคยขอ bash จาก agent แล้วพิมพ์เองใหม่ทุกครั้ง เหตุผลตรงกับหน้านี้เลย คือไม่อยากให้ความสามารถไหลออกจากนิ้วตัวเอง เขาถึงขั้นไปตั้งใจเรียน bash ให้เขียนเองได้จริง

ใน [[dhh-strategies-programming-with-ai-agents-lex-clips|คลิปถัดมา]] เขาบอกว่า

> "I have not written any bash myself for probably a couple of months because the agents have just gotten so good."

สองประโยคนี้ไม่ขัดกันในความหมาย แต่ขัดกันในการปฏิบัติ หน้านี้เก็บไว้ทั้งคู่ ไม่ตัดข้อใด และแยกสิ่งที่รู้จากสิ่งที่ยังไม่รู้

**สิ่งที่ต่างจากเคสอื่นใน wiki นี้:** DHH ฝึกมือก่อนแล้วจึงเลิกเขียน ซึ่งตรงกับหลัก "อย่าใช้ AI ทำสิ่งที่เรายังทำเองไม่เป็น" ของ [[zack-proser|Zack Proser]] อยู่แล้ว เขายังทักได้ว่า code ที่ agent เขียนซับซ้อนเกินไป ([[make-it-simpler|Make It Simpler]]) และไม่ชอบสไตล์ early exit ที่ agent ชอบใช้ ซึ่งเป็นการทักที่ต้องรู้ bash ก่อน

**สิ่งที่ยังตอบไม่ได้:** ทักษะที่ฝึกไว้แล้วอยู่ได้นานแค่ไหนเมื่อเลิกใช้ สองเดือนยังสั้นเกินจะสรุป และคนที่ไม่เคยเขียน bash เองมาก่อนจะทักแบบเดียวกับเขาได้ไหม คลิปไม่มีข้อมูลตรงนี้

**ผลคือ:** เคสนี้ไม่ได้แปลว่า skill atrophy ไม่จริง มันเตือนว่าต้องแยกสองคำถามออกจากกัน คือ "ยังเขียนเองอยู่ไหม" กับ "ยังตรวจงานเองได้ไหม" คำถามที่สองสำคัญกว่า และเป็นคำถามที่ [[taste-paradox|taste paradox]] กับ [[eh-gland|ต่อมเอ๊ะ]] พูดถึงจริง ๆ

## ถ้าทุก level ทำงานแบบเดียวกัน junior จะเรียนจากใคร

[[teepagorn-claude-code-adoption-nobody-reading|โพสต์ของ @teepagorn]] ขยายเรื่องนี้จากระดับคนไปถึงระดับทีม ในเคสที่เล่า engineer L1 ถึง L7 ทำงานเหมือนกันหมด คือ "Talk to Claude" แล้ว ship

ผู้เขียนมองว่า senior มีค่าเพราะถือบริบท เห็น trade-off ทัก assumption และรู้ว่าเรื่องไหนยังไม่ควรรีบทำ เขาเชื่อว่า judgement กับความ "ดมกลิ่นได้" น่าจะยังอยู่ แต่จะเริ่มไม่ถูกถ่ายทอด junior ไม่เห็นวิธีคิดของ senior แล้ว ส่วน senior ก็ไม่มีเวลาสอนเพราะวิ่งตาม output อยู่ ([[ai-work-intensification]])

**ผลคือ:** skill atrophy ไม่ได้เกิดแค่ในหัวคนเดียว มันเกิดได้ที่ทางส่งต่อทักษะระหว่างรุ่นด้วย ข้อนี้ยังเป็นการคาดการณ์ ยังไม่มีข้อมูลว่า junior ในทีมแบบนี้โตช้าลงจริง

## มุมจากคณิตศาสตร์: เครื่องยกได้หนักกว่า ไม่ได้ทำให้การเข้า gym ไร้ค่า

[[3blue1brown|3Blue1Brown]] (ช่อง YouTube สอนคณิตศาสตร์) ใช้ภาพเปรียบที่ตอบคำถามว่า "ถ้าเครื่องทำได้ดีกว่า จะฝึกเองไปทำไม" ไว้ใน [[never-been-better-time-to-go-into-math-3blue1brown|วิดีโอเรื่องอนาคตของคณิตศาสตร์]]

เขาบอกว่าการฝึกพิสูจน์เหมือนเข้า gym เครื่องยกน้ำหนักได้มากกว่าเรา แต่ประโยชน์ที่เราได้จากการยกเองยังอยู่ครบ คุณค่าชั้นนี้ต้องให้คนลงมือเองเสมอ เลยไม่ขึ้นกับว่าเครื่องเก่งแค่ไหน เขาไล่ดูทุกกรณีตั้งแต่เครื่องเก่งกว่าแค่เรื่องพิสูจน์ ไปจนถึงเก่งกว่าทุกเรื่อง ข้อนี้ไม่เปลี่ยนเลย (ดู [[career-value-stack]])

ส่วนวิธีใช้ AI ตอนเรียน เขาเทียบกับตำราที่มีเฉลยท้ายเล่ม ยังทำโจทย์เองก่อน ติดเมื่อไรค่อยเปิดดู แนวนี้เข้ากับหลักของ Zack Proser ข้างบน

สิ่งที่เขาเห็นว่าต้องเปลี่ยนคือวิธีฝึกและวิธีวัด "assigning and grading problem sets on its own doesn't really make sense right now" และเขาเสนอให้ย้ายไปวัดความเข้าใจจากการนำเสนอด้วยปากมากขึ้น

**ผลคือ:** เหตุผลที่ต้องฝึกเองไม่ใช่เพราะเครื่องยังทำไม่ได้ แต่เพราะผลของการฝึกตกอยู่กับคนที่ฝึกเท่านั้น

## See also

- [[cognitive-debt]]
- [[taste-paradox]]
- [[agentic-engineering]]
- [[developer-balance]]
- [[how-to-keep-shipping-away-from-desk]]
- [[code-isnt-free-mario-zechner-hard-truths-coding-ai]]
- [[dhh]]
- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
- [[make-it-simpler]]
- [[teepagorn-claude-code-adoption-nobody-reading]]
- [[never-been-better-time-to-go-into-math-3blue1brown]]
- [[career-value-stack]]
