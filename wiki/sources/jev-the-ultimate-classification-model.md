---
title: Jev - The Ultimate Classification Model?
type: source
author: Sam Witteveen
url: https://www.youtube.com/watch?v=X117w2Rark8
date_ingested: 2026-09-19
tags: [ai, classification, inference, latency, system-one-models, typesafe-ai]
created: 2026-09-19
updated: 2026-09-19
sources: ["https://www.youtube.com/watch?v=X117w2Rark8"]
---

# Jev - The Ultimate Classification Model? / Model ตัดสินใจเร็วแทน Chatbot ได้ไหม

[[sam-witteveen|Sam Witteveen]] (creator ที่ทดลอง AI model ผ่าน demo ใช้งานจริง) พาไปรู้จัก [[jev|Jev]] ของ [[typesafe-ai|Typesafe AI]] ตัว model ไม่ได้เขียนคำตอบยาวแบบ chatbot แต่รับข้อมูลหนึ่งก้อน แล้วตอบคำถามจำกัดรูปแบบ เช่น เลือกหมวด ให้คะแนน หรือคืน probability ว่าคำตอบเป็น yes

Sam เรียกแนวนี้ว่า [[system-one-models|System One Model]] ตามกรอบ System 1 และ System 2 จาก Daniel Kahneman งานอย่างแยก support ticket หรือเช็กว่า agent ผิดกฎหรือไม่ มักต้องการคำตัดสินเร็ว ไม่ได้ต้องการ [[chain-of-thought|chain-of-thought]] ยาวหลายนาที

## Contract มีแค่ state กับ typed questions

ผู้ใช้ส่งข้อมูลเข้า Jev สองส่วน:

1. `state` คือข้อความหรือข้อมูลดิบ เช่น support ticket, agent trace หรือ log
2. typed questions คือคำถามที่กำหนดชนิดผลลัพธ์ไว้แล้ว

วิดีโอแบ่งคำถามเป็นสามชนิด:

| ชนิด | สิ่งที่ส่งเข้า | สิ่งที่ได้กลับ |
| --- | --- | --- |
| `choice` | รายการตัวเลือก | ตัวเลือกที่ model เลือก พร้อม probability ของแต่ละตัวเลือก |
| `score` | ช่วงคะแนนที่กำหนด | คะแนนและ probability ที่เกี่ยวข้อง |
| `noul` | คำถาม yes/no | probability ว่าคำตอบเป็น yes |

คำว่า `noul` สะกดตาม transcript ที่ผู้ใช้ส่งมา การ ingest ครั้งนี้ยังไม่ได้ตรวจชื่อ field กับเอกสาร API ของ Typesafe AI

ผลลัพธ์ไม่มีข้อความอิสระให้ parse และ model เลือกได้เฉพาะค่าที่ schema อนุญาต Sam จึงเสนอให้มอง Jev เป็น "smart if statement" มากกว่า chatbot งานหนึ่งควรแตกเป็นคำถามเล็กหลายข้อ แล้วใช้ code ปกติประกอบคำตอบและ business rule ต่อ

**ได้อะไร:** software ได้ค่าที่นำไป branch ต่อได้ทันที โดยไม่ต้องรอ model เขียนเหตุผลหรือ JSON ยาวก่อนถึงคำตอบ

## Demo จากภาษาและ sentiment ไปถึงงาน routing

Sam ลอง `choice` กับ language identification ทั้งภาษาฝรั่งเศสและภาษาไทยที่เขียนด้วยอักษรโรมัน Jev เลือกหมวดได้ตรงในตัวอย่างที่แสดง ส่วน `score` ใช้ให้คะแนน sentiment ตั้งแต่ 0 ถึง 2 และขยับคะแนนตามข้อความที่ positive, negative หรือ mixed

ตัวอย่าง `noul` ถามว่าข้อความกำลังตั้งคำถามหรือไม่ Jev ยังแยกประโยคคำถามที่ไม่มีเครื่องหมาย `?` ได้ แต่ผลเปลี่ยนเล็กน้อยในแต่ละครั้ง Sam ชี้ว่าผลยังเป็น stochastic และสังเกตเองว่าข้อความยาวกว่าดูเหมือนทำให้ model มั่นใจขึ้น ข้อนี้เป็นข้อสังเกตจาก demo ไม่ใช่ผลทดลองที่ควบคุมตัวแปร

ใน demo ที่ใกล้งานจริง เขาใช้ Jev ทำหลายอย่างกับข้อความเดียว:

- route support ticket ไป billing, sales หรือ technical
- ตรวจว่าผู้ใช้ขอ refund หรือไม่
- ประเมินความเร่งด่วน
- แยก prompt injection, sarcasm, PII และ spam
- ช่วยเลือก tool ให้ agent
- เช็ก code แบบ yes/no ว่าปลอดภัยหรือไม่

Jev ช่วยเลือกชื่อ tool ได้ แต่ไม่สร้าง argument สำหรับเรียก tool ต่อ ตรงนี้ยังต่างจาก function-calling model ที่ extract parameter แล้วประกอบ request ให้ครบ

**ผลคือ:** Jev เหมาะเป็น semantic gate หรือ router มากกว่าเป็นตัวลงมือทำงานปลายทาง

## หลายคำตัดสินเล็กประกอบเป็น workflow

จุดที่ Sam สนใจที่สุดคือการรัน classification หลายข้อเรียงกัน เขา demo 20 งานต่อเนื่องกับ input เดียว แล้วนำผลแต่ละข้อไปประกอบเป็น workflow ผ่าน code ธรรมดา บางข้อทำขนานกันได้เพราะไม่พึ่งผลก่อนหน้า

วิธีนี้ต่างจากการถาม model คำถามกว้างข้อเดียวอย่าง "ให้คะแนน pitch นี้" ผู้ใช้ต้องแยกเกณฑ์ก่อน เช่น feasibility, market type และความเสี่ยง แล้วกำหนด option หรือ scale ให้แต่ละข้อ ผลลัพธ์จึงแก้ด้วย code และ threshold ได้ตรง ๆ ไม่ต้องไล่ปรับ prose prompt ทุกครั้ง

ตรงนี้เชื่อมกับ [[harness-guides-sensors|Harness Guides & Sensors]] Jev อาจทำ inferential sensor ให้เบาและเร็วพอจะรันถี่ขึ้น แต่ยังเป็น model ที่ให้ผลเปลี่ยนได้ ไม่กลายเป็น deterministic test หรือ policy gate เพียงเพราะ output เป็น typed value

## Speed กับราคาที่วิดีโอรายงาน

Sam เรียก Jev ผ่าน OpenRouter และรายงานราคาขณะอัดวิดีโอว่า input อยู่ที่ 4.20 เซนต์ต่อหนึ่งล้าน token ส่วน output token ฟรี ตัวอย่างแต่ละครั้งแสดงค่าใช้จ่ายราว 0.0014 เซนต์ และชุด 20 งานรวมกันเกิน 1/20 เซนต์เล็กน้อย

Typesafe AI อ้าง latency ฝั่ง model ราว 70 ถึง 500 มิลลิวินาที ก่อนรวม network round trip Sam ยังประมาณว่าถ้ารัน 10 query ต่อวินาทีต่อเนื่องจะเสียราว 7 ดอลลาร์ต่อชั่วโมง ตัวเลขทั้งหมดเป็นภาพจากวิดีโอ ณ เวลานั้น ไม่ใช่ราคาหรือ SLA ที่วิกิยืนยันว่าใช้ได้ในปัจจุบัน

เหตุผลที่ output token ฟรีตามคำอธิบายในคลิปคือ Jev ไม่ได้ autoregressive decode ข้อความทีละ token ผลลัพธ์ออกมาใน pass เดียว จึงไม่จ่ายต้นทุนตามความยาวคำตอบแบบ LLM ทั่วไป

## สิ่งที่รู้และสิ่งที่ยังไม่รู้เรื่องตัว model

ข้อมูลสถาปัตยกรรมยังน้อย Typesafe AI ระบุเพียงสามส่วนตามที่ Sam ถ่ายทอด:

- model architecture แบบใหม่
- parallel sampler
- วิธี train ชื่อ RLCD หรือ Reinforcement Learning for Calibrated Decisions

ไม่มี paper หรือ architecture diagram ในแหล่งนี้ และไม่ได้อธิบายว่า RLCD ทำงานอย่างไร Sam เดาว่าอาจยังเป็น transformer ที่ใช้ช่วง prefill สร้าง representation แล้วส่งเข้า classification หรือ regression head แต่เขาระบุชัดว่าเป็นการคาดเดา ไม่ใช่ข้อมูลจาก Typesafe AI

คำว่า probability ใน response ก็ยังไม่พอจะพิสูจน์ว่า model calibrated จริง ต้องวัดเพิ่มว่ากลุ่มคำตอบที่ให้ 80% ถูกใกล้ 80% หรือไม่ และต้องแยกตามภาษา domain class imbalance กับ distribution shift วิดีโอมี demo รายกรณี แต่ไม่มี benchmark หรือ calibration curve ให้ตรวจ

## "ไม่ hallucinate" หมายถึงไม่หลุด schema ไม่ใช่ตอบถูกเสมอ

Typesafe AI อ้างว่า Jev hallucinate ไม่ได้ Sam ตีความ claim นี้อย่างระวังว่า model สร้าง JSON พัง ชื่อ tool ปลอม หรือข้อความนอกตัวเลือกไม่ได้ เพราะไม่มีช่องให้ generate ค่าเหล่านั้น

Jev ยังเลือก class ผิด ให้ score ผิด หรือมั่นใจผิดได้ วิดีโอเองแสดงว่าผลแต่ละรอบขยับ และตัวอย่างที่กำกวมทำให้ probability กระจายมากขึ้น ดังนั้น typed output แก้ปัญหา schema validity แต่ไม่ได้รับรอง semantic correctness

ข้อจำกัดนี้สำคัญกับงาน security ตัวอย่างตรวจ prompt injection ในคลิปดูทำได้ดี แต่ยังไม่มี attack suite, false-negative rate หรือผลบน input นอก distribution มาให้ดู ถ้าใช้คุม action ของ agent ต้องมี sandbox, allowlist และ audit boundary อยู่ข้างนอก model ตามหลัก [[agent-runtime-untrusted|Agent Runtime as Untrusted Component]]

**ได้อะไร:** Jev อาจลด latency และ parsing failure ของ semantic decision แต่ความเสียหายจากคำตัดสินผิดยังต้องคุมด้วย architecture

## คำถามที่ยังตอบไม่ได้

- RLCD ทำให้ probability calibrated ดีขึ้นจริงแค่ไหน เมื่อเทียบกับ classifier ที่ train แบบเดิม
- ภาษาไหน domain แบบไหน และ class distribution แบบใดที่ Jev ทำได้ไม่ดี
- latency กับ throughput เปลี่ยนอย่างไรเมื่อ `state` ยาวหรือถามหลายข้อพร้อมกัน
- Jev คุ้มกว่าการ fine-tune BERT หรือ model เล็กเฉพาะงานตรงจุดไหน เมื่อรวมข้อมูล train, hosting และ monitoring
- model ใช้สถาปัตยกรรมใหม่จริง หรือเป็น transformer เดิมที่เปลี่ยน head กับวิธี train
- `noul` ใน transcript ตรงกับชื่อชนิดข้อมูลใน API จริงหรือเป็นความคลาดเคลื่อนจากการถอดเสียง

## Quotes

> "Software doesn't want a paragraph. It wants a value that it can basically use straight away."

> "You could think of this as being a smart if statement."

## See also

- [[jev]]
- [[typesafe-ai]]
- [[sam-witteveen]]
- [[system-one-models]]
- [[chain-of-thought]]
- [[harness-guides-sensors]]
- [[agent-runtime-untrusted]]
