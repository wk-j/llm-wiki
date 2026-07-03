---
title: Photonic Interconnects
type: concept
tags: [ai, data-center, photonics, networking, semiconductors]
created: 2026-07-03
updated: 2026-07-03
sources: [review-lite-cohr-nok-aaoi.md]
---

# Photonic Interconnects / การส่งข้อมูลผ่านแสง

Photonic interconnects คือการส่งข้อมูลด้วยแสงในระบบคอมพิวเตอร์หรือ data center. ในวิดีโอ [[review-lite-cohr-nok-aaoi|Review LITE COHR NOK AAOI]] คำนี้ถูกใช้เป็น theme ลงทุนรอบ AI data center: พอ GPU และ memory เร็วขึ้นเรื่อย ๆ network ระหว่างเครื่องก็เริ่มเป็นคอขวด

## แก่นความคิด

AI data center ไม่ได้มีแค่ GPU. Model ใหญ่ต้องย้ายข้อมูลระหว่าง GPU, memory, server, switch, storage, และ network fabric ตลอดเวลา ถ้าการส่งข้อมูลช้า เครื่องแพง ๆ ก็รอข้อมูลแทนที่จะคำนวณเต็มที่

Photonic interconnects จึงพยายามใช้แสงช่วยส่งข้อมูลให้เร็วขึ้นและกินพลังงานต่อ bit ต่ำลง โดยเฉพาะใน module ความเร็วสูง เช่น 800G และ 1.6T ที่คลิปพูดถึง

**ได้อะไร:** คอขวดของ AI ไม่ได้อยู่แค่ “มี GPU พอไหม” แต่อยู่ที่ทั้งระบบส่งข้อมูลด้วย

## ห่วงโซ่จากต้นน้ำถึง data center

คลิปเล่า supply chain แบบนี้:

1. substrate / [[indium-phosphide-wafer|Indium Phosphide wafer]]
2. epitaxy / การปลูกวัสดุระดับนาโนเมตรบน wafer
3. fabrication / lithography / etching
4. dicing และทดสอบ die
5. laser + fiber coupling
6. [[optical-transceivers|optical transceiver]] / module ที่รวม laser, DSP, และตัวแปลงสัญญาณ
7. switch / OCS / data center deployment

บริษัทที่อยู่หลายขั้นพร้อมกัน เช่น [[coherent|Coherent]] ในกรอบของคลิป อาจมีอำนาจคุมต้นทุนและเวลาส่งมอบมากกว่าบริษัทที่อยู่ปลายน้ำอย่างเดียว

## ธีมลงทุนกับความจริงทางธุรกิจ

คลิปเปิดด้วยความระวัง: photonics ถูกพูดถึงเยอะ แต่ในอดีต margin ของบางบริษัทต่ำกว่ากลุ่ม memory มาก ผู้พูดจึงไม่ถือว่า “เป็นคอขวด” แปลว่า “กำไรดี” โดยอัตโนมัติ

ตัวแปรที่ต้องดูคือ:

- capacity พร้อมส่งของจริงหรือยัง
- wafer 6 นิ้วผลิตได้ yield ดีไหม
- ลูกค้า qualify แล้วหรือยัง
- บริษัทต้องซื้อวัตถุดิบแพงจากข้างนอกหรือคุมต้นน้ำเอง
- รายได้โตเพราะ photonics จริง หรือ segment อื่นถ่วง/ช่วยอยู่
- module ความเร็วสูงทำ margin ได้จริงแค่ไหนเมื่อแข่งกันมากขึ้น

**ผลคือ:** Photonic interconnects เป็น theme ที่โยงกับ AI infrastructure ได้จริง แต่ต้องอ่านผ่าน supply chain และ margin ไม่ใช่อ่านผ่านคำว่า AI อย่างเดียว

## See also

- [[review-lite-cohr-nok-aaoi]]
- [[indium-phosphide-wafer]]
- [[optical-transceivers]]
- [[ai-data-center-bottlenecks]]
- [[coherent]]
- [[lumentum]]
- [[aaoi]]
- [[nokia]]
- [[axt]]
