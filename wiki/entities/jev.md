---
title: Jev
type: entity
tags: [ai, classification, inference, system-one-models, typesafe-ai]
created: 2026-09-19
updated: 2026-10-07
sources: [jev-the-ultimate-classification-model.md, what-is-codemode-armin-ronacher.md]
---

# Jev

Jev คือ model ของ [[typesafe-ai|Typesafe AI]] สำหรับงานตัดสินใจแบบมีชนิดผลลัพธ์กำกับ ไม่ได้เปิดให้ chat หรือเขียนข้อความอิสระ ผู้ใช้ส่ง `state` พร้อมคำถามแบบ `choice`, `score` หรือ `noul` แล้วได้ค่ากับ probability กลับมา

[[sam-witteveen|Sam Witteveen]] ทดลอง model ผ่าน OpenRouter ใน [[jev-the-ultimate-classification-model|Jev - The Ultimate Classification Model?]] เขาใช้แยกภาษา ให้คะแนน sentiment, route support ticket, ตรวจ refund กับ urgency, หา PII และ spam รวมถึงเลือก tool ให้ agent

## จุดที่ต่างจาก LLM ทั่วไป

Jev ไม่ autoregressive decode คำตอบทีละ token จึงตอบได้เร็วและไม่มีข้อความยาวให้ parse ตัว model เลือกได้เฉพาะ schema ที่ caller ส่งมา ถ้าโจทย์ต้องการชื่อ tool กับ argument ครบ หรืออยากให้ model อธิบายเหตุผล Jev ยังทำแทน function-calling model ไม่ได้

Typesafe AI เรียก Jev ว่า [[system-one-models|System One Model]] เพราะตั้งใจรับงานจำแนกที่ต้องตอบเร็ว มากกว่างาน reasoning หลายขั้นแบบ [[chain-of-thought|chain-of-thought]]

## ขอบเขตของ claim

วิดีโอรายงาน latency ฝั่ง model ราว 70 ถึง 500 มิลลิวินาที และราคาผ่าน OpenRouter ที่คิดเฉพาะ input token ตัวเลขนี้เป็นค่าตามเวลาที่อัดวิดีโอ ไม่ใช่ข้อมูลปัจจุบันที่ตรวจซ้ำแล้ว

คำว่า "ไม่ hallucinate" หมายถึง output ไม่หลุด schema ไม่ได้แปลว่าคำตอบถูกเสมอ Jev ยังเลือก class ผิดและให้ probability ผิดได้ ผลใน demo ก็เปลี่ยนเล็กน้อยระหว่างรอบ การจะเชื่อ probability ต้องทดสอบ calibration กับข้อมูลจริงของแต่ละงาน

Typesafe AI ระบุชื่อ new architecture, parallel sampler และ RLCD แต่แหล่งนี้ไม่มี paper หรือ diagram Sam จึงแยกการเดาเรื่อง transformer กับ classification head ออกจากข้อมูลที่บริษัทเปิดเผย

## ใช้ใน agent ผ่าน Codemode

[[armin-ronacher|Armin Ronacher]] โชว์ใน [[what-is-codemode-armin-ronacher|What is Codemode]] ว่า agent ใน [[pi-agent|Pi]] เรียก Jev ได้จาก [[codemode|Codemode]] ด้วย `models.getModelOfType("classifier", "typesafe", "jev-latest")` แล้วใช้ `models.classify` ไม่ต้องมี tool เฉพาะ

ตัวอย่างแรกจำแนก GitHub issue 100 ตัวพร้อมกัน ถามสามข้อคือ `sentiment` แบบ `choice`, `frustration` แบบ `score` สี่ระดับ และ `kind` แบบ `choice` แล้วคืนแค่ 12 issue ที่หงุดหงิดสุด ตัวอย่างที่สองให้ Jev เลือก action ในเกมรถถังทีละรอบ 30 รอบ แล้วให้ code ธรรมดาแปลง action เป็นคำสั่งเกม

code ในบทความยืนยันชื่อชนิดคำถาม `choice` กับ `score` และรูปทรงคำตอบ เช่น `r.answers.action.choice` กับ `frustration.score` ที่เป็นตัวเลข ส่วน `noul` ไม่ปรากฏในบทความนี้

**ได้อะไร:** Jev เข้ากับงานที่ agent ต้องตัดสินแคบ ๆ ซ้ำหลายครั้ง โดยให้ code ถือ logic ที่เหลือ

## See also

- [[typesafe-ai]]
- [[system-one-models]]
- [[jev-the-ultimate-classification-model]]
- [[sam-witteveen]]
- [[harness-guides-sensors]]
- [[codemode]]
- [[what-is-codemode-armin-ronacher]]

