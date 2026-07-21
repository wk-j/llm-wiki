---
title: Skill Stacking
type: concept
tags: [ai, skills, generalist, domain-expertise, taste]
created: 2026-07-21
updated: 2026-07-21
sources: [teepagorn-ten-lessons-building-with-ai.md, llm-era-computer-engineering-ep3-nattee.md]
---

# Skill Stacking / การต่อทักษะหลายด้านเข้าด้วยกัน

**Skill stacking** คือการมีทักษะหลายด้านในระดับที่พอมองโครงสร้างออก แล้วเอามาต่อกันเพื่อทำงานที่คนถนัดด้านเดียวอาจมองไม่เห็น เช่น คนที่พอรู้ code, design, marketing และ psychology สามารถออกแบบ product หนึ่งชิ้นให้ครบวงจรขึ้น แล้วใช้ AI ช่วยลงรายละเอียดแต่ละด้าน

ใน [[teepagorn-ten-lessons-building-with-ai|10 บทเรียนจากการสร้างของด้วย AI]] ผู้เขียนใช้ภาพว่าไม่ต้องเก่งสุดทุกด้าน แค่รู้ราว 70% ก็ “เปิด map” ของทักษะนั้นได้ รู้ว่าควรถามอะไร หาของที่ไหน และเอาอะไรต่อกับอะไร ตัวเลขนี้เป็น heuristic ส่วนตัว ไม่ใช่ระดับมาตรฐานที่วัดได้

## AI เปลี่ยนประโยชน์ของคนรู้กว้างอย่างไร

ก่อนมี AI คนรู้กว้างอาจติดที่ไม่มีเวลาลงรายละเอียดทุกแขนง พอมี AI เขาช่วยร่าง code, เสนอ variation, อธิบาย jargon หรือค้นวิธีเฉพาะด้านได้เร็วขึ้น Breadth จึงทำหน้าที่เลือกทิศและเชื่อมชิ้นส่วน ส่วน AI ช่วยเพิ่ม throughput ในแต่ละแขนง

แต่ AI ไม่ได้ทำให้ความรู้ตื้นกลายเป็น expertise โดยอัตโนมัติ ถ้าคนไม่รู้ว่า output ที่ดีหน้าตาเป็นอย่างไร ก็จะจับ hallucination, tradeoff หรือ edge case ไม่ได้

**ได้อะไร:** skill stack ให้ leverage ตอน “เลือกและเชื่อม” ส่วนความลึกให้ safety ตอน “ตัดสินและตรวจ”

## ความตึงกับ Generalist Moat ที่กำลังหด

หน้า [[engineering-role-shift|Engineering Role Shift]] เก็บข้อสังเกตของ [[nattee-niparnan|Nattee Niparnan]] ว่าความรู้กว้างระดับพอทำได้อาจเสีย moat เพราะ AI ทำงานผิวกว้างได้เหมือนกัน คนจึงต้องลึกบางด้านเพื่อสร้าง [[eh-gland|ต่อมเอ๊ะ]]

สองมุมนี้ไม่จำเป็นต้องหักล้างกันทันที เพราะกำลังพูดถึงคุณค่าคนละชนิด:

| มุม | สิ่งที่ breadth ช่วย | สิ่งที่ depth ช่วย |
| --- | --- | --- |
| Skill stacking | เห็น combination ใหม่และสั่งงานข้ามโดเมน | ตรวจว่าชิ้นส่วนที่ AI เติมมาถูกจริง |
| Generalist moat | ความรู้กว้างทั่วไปอาจไม่ใช่จุดขายแล้ว | ความลึกเป็นฐานของ judgement ที่ AI ชดเชยยาก |

คำถามจริงจึงไม่ใช่ “กว้างหรือลึก” แต่คือ **ต้องลึกตรงไหนพอเป็น anchor และกว้างแค่ไหนพอเชื่อมโลกหลายใบเข้าด้วยกัน**

## รูปแบบที่ใช้ได้จริง

1. เลือก anchor domain อย่างน้อยหนึ่งด้านที่ทำเองและ debug เองได้
2. เรียนด้านข้างให้ถึงระดับที่ตั้งคำถามและรู้ vocabulary สำคัญ
3. ใช้ AI ช่วยสำรวจและทำ draft แต่ขอ evidence หรือ verifier ทุกครั้งที่ผลมีความเสี่ยง
4. พอเจอ pattern ซ้ำ ค่อยเก็บเป็น skill, checklist หรือ [[coding-harness|harness]]
5. กลับมาลงมือเองเป็นระยะเพื่อไม่ให้เกิด [[skill-atrophy]]

**ผลคือ:** breadth ไม่กลายเป็นการสะสม buzzword และ depth ไม่กลายเป็นกำแพงที่ทำงานข้ามทีมไม่ได้

## คำถามที่ยังเปิดอยู่

- ระดับ “รู้พอถาม” วัดจากอะไร: vocabulary, ทำ prototype ได้, debug ได้ หรือ review ได้
- งาน safety-critical ต้องการ depth ในทุกจุดสำคัญหรือใช้ expert/harness มาชดเชยได้แค่ไหน
- junior จะสร้าง anchor domain ได้อย่างไร ถ้า AI ทำให้ข้ามช่วงฝึกมือที่สร้าง [[taste-paradox|taste]]
- skill stack แบบไหนสร้าง combination ใหม่จริง และแบบไหนเป็นเพียงความรู้ผิวที่ AI ทำแทนได้อยู่แล้ว

## ดูเพิ่ม

- [[teepagorn-ten-lessons-building-with-ai]]
- [[engineering-role-shift]]
- [[taste-paradox]]
- [[knowledge-skills-wisdom]]
- [[model-choice-by-expertise]]
- [[skill-atrophy]]
- [[domain-to-ai-translator]]
