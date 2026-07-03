---
title: AI Brain Fry
type: concept
tags: [ai, productivity, workplace, attention, burnout]
created: 2026-06-30
updated: 2026-06-30
sources: [techsauce-ai-brain-fry.md]
---

# AI Brain Fry / ภาวะสมองล้าจากการใช้ AI

**AI Brain Fry** คือภาวะสมองล้าจากการใช้หรือกำกับดูแล AI เกินกว่าที่สมองคนรับไหว. [[techsauce|Techsauce]] สรุปคำนี้จากงานที่อ้างถึง [[harvard-business-review|Harvard Business Review]] ในโพสต์ [[techsauce-ai-brain-fry|Techsauce - AI Brain Fry]].

พูดง่าย ๆ คือ AI ช่วยทำงานได้ แต่คนยังต้องคุมมัน. พอคนต้องคุมหลายเครื่องมือพร้อมกัน ตรวจคำตอบซ้ำ เปรียบเทียบผลลัพธ์ และตัดสินใจว่าจะเชื่ออะไร สมองก็ไม่ได้พัก. แค่งานเปลี่ยนจาก "ทำเอง" เป็น "คุมคนทำงานที่อาจมั่วได้".

## อาการ

อาการที่ Techsauce ยกมาคือสมองเหมือนมีหมอก โฟกัสยาก ตัดสินใจช้าลง และต้องหยุดพักเพื่อรีเซ็ตความคิด.

ภาวะนี้ไม่ได้แปลว่า AI ทำให้สมองเสียถาวร. ใน context ของโพสต์ มันหมายถึง mental fatigue จากการใช้ attention, working memory, และ judgement เกินกำลังในช่วงทำงาน.

**ได้อะไร:** คำนี้ช่วยตั้งชื่อความเหนื่อยที่คนใช้ AI บางกลุ่มรู้สึก แต่ก่อนอธิบายยาก เพราะภายนอกเหมือนงานถูก automate ไปแล้ว.

## สาเหตุหลักคือ oversight

สาเหตุที่สำคัญไม่ใช่แค่ "ใช้ AI เยอะ" แต่คือ **ต้องกำกับ AI เยอะ**. งาน oversight มีหลายชั้น:

- ตรวจว่าคำตอบถูกไหม
- เทียบ output จากหลายเครื่องมือ
- สลับ context ระหว่าง tool
- จำว่า tool ไหนทำอะไรไปแล้ว
- รับผิดชอบผลสุดท้ายแม้ AI เป็นคนสร้าง

ตรงนี้เชื่อมกับ [[orchestration-tax|Orchestration Tax]] โดยตรง. Orchestration Tax อธิบายว่า agent ผลิตขนานได้ แต่คน review และ merge ยังเป็น serial bottleneck. AI Brain Fry คืออาการในหัวของคนเมื่อ bottleneck นั้นถูกใช้งานเต็มเกินไป.

**ผลคือ:** ยิ่งเพิ่ม AI tool โดยไม่ลดงานตรวจ คนยิ่งเหนื่อย แม้ dashboard จะดู productive ขึ้น.

## ไม่ใช่ข้อห้ามใช้ AI

Techsauce ย้ำว่า AI ยังช่วยลด burnout ได้เมื่อใช้แทน routine tasks เช่น สรุปข้อมูลหรือจัดการเอกสาร. งานแบบนี้ดีเพราะผลลัพธ์มักชัดและไม่ต้องให้คนตัดสินใจซับซ้อนทุกนาที.

ปัญหาเกิดเมื่อ AI ถูกใช้กับงานที่ต้องคุมหลายทางพร้อมกัน. productivity อาจเพิ่มตอนใช้ 1-2 tool แต่พอเกิน 3 tool พร้อมกัน ภาระสลับงานและตรวจงานเริ่มกินกำไรคืน.

**ได้อะไร:** คำถามที่ดีไม่ใช่ "ใช้ AI มากแค่ไหน" แต่คือ "AI ลดงานคิด หรือเพิ่มงานคุม".

## ความสัมพันธ์กับ Cognitive Surrender

[[cognitive-surrender|Cognitive Surrender]] คือการยอมรับงาน AI โดยยังไม่ได้ตั้งความเห็นเอง เพราะ attention หมด. AI Brain Fry คือภาวะล้าก่อนถึงจุดนั้น.

เส้นทางหนึ่งคือ:

1. ใช้ AI หลาย tool
2. ต้องตรวจและเทียบ output มากขึ้น
3. attention หมด
4. เริ่มรับ output เพราะไม่มีแรงคิดเอง
5. สะสม [[cognitive-debt|Cognitive Debt]]

ไม่ใช่ทุก AI Brain Fry จะจบที่ cognitive surrender. ถ้า workflow มี gate ที่ดี พักเป็นรอบ และจำกัด WIP ได้ ภาวะล้าอาจถูกจัดการก่อน.

**ผลคือ:** AI Brain Fry เป็น warning sign. เห็นแล้วควรลด WIP หรือปรับ workflow ก่อนคุณภาพ judgement ตก.

## หลักออกแบบ workflow

- **จำกัดจำนวน tool ที่ต้องคุมพร้อมกัน** — ถ้าเกิน 3 tool แล้ว productivity เริ่มตกตาม claim ของ Techsauce นั่นคือสัญญาณให้รวมขั้นตอนหรือปิดบาง tool
- **ให้ AI ทำ routine tasks ก่อน** — งานซ้ำ ตรวจง่าย และมีรูปแบบชัดช่วยคืนพลังให้คน
- **แยก maker กับ checker** — ให้ระบบมี test, checklist, หรือ verifier แทนการโยนทุกอย่างให้คนอ่านเอง
- **batch review** — ลด context switch จากการเช็ค AI ทีละตัว
- **วัด mental load ด้วย** — ถ้าทีมวัดแค่ output แต่ไม่วัด fatigue จะเห็น productivity ปลอม

ตรงนี้เป็นด้าน workplace ของ [[developer-balance|Developer Balance]]: ความเร็วที่ดีต้องไม่เผาความสามารถในการตัดสินใจของคน.

## See also

- [[techsauce-ai-brain-fry]]
- [[orchestration-tax]]
- [[developer-balance]]
- [[acceptance-bottleneck]]
- [[cognitive-surrender]]
- [[cognitive-debt]]
- [[care-allocation]]
- [[enterprise-ai-roi]]
- [[tokenmaxxing]]
