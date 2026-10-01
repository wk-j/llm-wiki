---
title: System One Models
type: concept
tags: [ai, classification, inference, latency, decision-systems]
created: 2026-09-19
updated: 2026-09-19
sources: [jev-the-ultimate-classification-model.md]
---

# System One Models / Model สำหรับคำตัดสินเร็ว

System One Model คือชื่อที่ [[typesafe-ai|Typesafe AI]] ใช้กับ model ที่ตอบคำถามจำกัดรูปแบบอย่าง class, score หรือ yes-probability โดยไม่เขียนเหตุผลยาว แนวคิดยืมภาพ System 1 จาก Daniel Kahneman มาอธิบายการตัดสินใจที่เร็วและไม่ไตร่ตรองหลายขั้น

คำนี้ยังเป็น positioning ของบริษัทจากแหล่งเดียว ไม่ใช่หมวดสถาปัตยกรรมที่มีนิยามกลางในงานวิจัย วิกิจึงใช้เพื่อเรียก design goal ของ [[jev|Jev]] ไม่ได้สรุปว่า model ทำงานเหมือนการรู้คิดของมนุษย์จริง

## แยกงานตัดสินใจออกจากงาน reasoning

LLM แบบ reasoning มักใช้ [[chain-of-thought|chain-of-thought]] หรือ test-time compute เพิ่ม เพื่อแก้โจทย์ที่ต้องเชื่อมเหตุผลหลายขั้น แต่ software decision จำนวนมากมี output แคบอยู่แล้ว เช่น:

- support ticket นี้ควรเข้าทีมไหน
- ข้อความนี้เร่งด่วนหรือไม่
- agent output ผิดกฎหรือเปล่า
- code change นี้เสี่ยงระดับใด

ถ้าใช้ reasoning model กับงานเหล่านี้ ระบบต้องรอ token หลายตัวก่อนถึง label สุดท้าย และบางครั้งยังต้อง parse JSON อีก System One Model ตัดส่วนสร้างข้อความออก แล้วคืน typed value โดยตรง

| มิติ | Reasoning LLM | System One Model ตามแนวคิดของ Typesafe AI |
| --- | --- | --- |
| output | ข้อความ เหตุผล หรือ tool call | choice, score หรือ yes-probability |
| inference | มัก generate หลาย token ต่อกัน | ตั้งใจให้คืนผลใน pass เดียว |
| จุดแข็ง | โจทย์เปิดและ reasoning หลายขั้น | routing, ranking และ semantic gate ที่ยิงถี่ |
| สิ่งที่ต้องคุม | token cost, latency, parsing, reasoning error | class definition, threshold, calibration, wrong decision |

**ได้อะไร:** เลือก model ตามรูปทรงของคำตอบ ไม่ใช้ chatbot เป็นค่าเริ่มต้นกับทุก decision

## แตกคำถามใหญ่เป็นคำถามเล็ก

[[sam-witteveen|Sam Witteveen]] เสนอใน [[jev-the-ultimate-classification-model|วิดีโอทดลอง Jev]] ว่าอย่าถามคำถามกว้างอย่าง "startup นี้ดีไหม" ให้แตกเป็น feasibility, market type และเกณฑ์ย่อย แล้วกำหนดตัวเลือกหรือช่วงคะแนนไว้ล่วงหน้า

code ปกติค่อยนำผลแต่ละข้อมารวมกัน เช่น route ไปคิว A เมื่อ class เป็น `billing` และ refund probability เกิน threshold หรือส่งให้คนตรวจเมื่อ probability กระจายจนไม่มี class ชัด วิธีนี้ทำให้ business rule อยู่ใน code ส่วน model รับเฉพาะงานตีความภาษา

**ผลคือ:** ทีมปรับ threshold และ flow ได้โดยไม่ต้องซ่อน policy ทั้งหมดไว้ใน prompt เดียว

## Probability ไม่เท่ากับ calibration

Jev คืน probability ของแต่ละตัวเลือก ต่างจากการขอให้ chatbot พิมพ์ตัวเลข `0.9` เป็นข้อความ แต่การมี field ชื่อ probability ยังไม่พิสูจน์ว่าเลขนั้น calibrated

ต้องทดสอบกับข้อมูลจริง เช่น กลุ่มที่ model ให้ 80% ถูกใกล้ 80% หรือไม่ แยกตามภาษา domain class imbalance และ input ที่เปลี่ยน distribution ด้วย วิดีโอแสดงว่า Jev มี stochastic variation และมั่นใจน้อยลงเมื่อข้อความกำกวม แต่ไม่มี calibration curve หรือ benchmark เทียบ classifier อื่น

**ได้อะไร:** ใช้ probability ช่วย route ความไม่แน่ใจได้ แต่ต้องวัดก่อนตั้ง threshold ที่กระทบผู้ใช้หรือความปลอดภัย

## ตำแหน่งใน harness

ในกรอบ [[harness-guides-sensors|Harness Guides & Sensors]] System One Model ยังเป็น inferential sensor เพราะตีความความหมายด้วย model และให้ผลเปลี่ยนได้ จุดขายคือทำ sensor ชนิดนี้ให้เร็วและถูกลงจนรันถี่กว่า LLM judge ตัวใหญ่

แต่ความเร็วไม่ได้เปลี่ยนให้กลายเป็น computational sensor ถ้าตัดสินผิดแล้วมีผลเสียสูง ต้องมี deterministic validation, human review หรือ boundary ภายนอกตามระดับความเสี่ยง โดยเฉพาะงานอนุมัติ tool call และ prompt-injection detection ที่ควรอ่านคู่กับ [[agent-runtime-untrusted|Agent Runtime as Untrusted Component]]

## เรื่องที่ยังตอบไม่ได้

- RLCD ทำงานอย่างไร และดีกว่าวิธี train classifier เดิมตรงไหน
- typed question ทั้งสามแบบครอบคลุม decision จริงได้แค่ไหน
- งานไหนคุ้มกว่าการ fine-tune model เฉพาะทางอย่าง BERT
- probability เสถียรและ calibrated ข้ามภาษา domain กับเวลาเพียงใด
- architecture ใหม่ทำให้เร็วขึ้นจริงส่วนไหน เมื่อเทียบกับการเปลี่ยน output head ของ transformer เดิม

## See also

- [[jev]]
- [[typesafe-ai]]
- [[jev-the-ultimate-classification-model]]
- [[chain-of-thought]]
- [[harness-guides-sensors]]
- [[agent-runtime-untrusted]]
