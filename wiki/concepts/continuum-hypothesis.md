---
title: Continuum Hypothesis
type: concept
tags: [mathematics, set-theory, logic, foundations]
created: 2026-07-03
updated: 2026-07-03
sources: [infinity-godel-incompleteness-mlhf.md]
---

# Continuum Hypothesis / สมมติฐานคอนตินิวอัม

Continuum Hypothesis คือคำถามว่ามี cardinality ใดอยู่ระหว่างขนาดของจำนวนนับกับขนาดของจำนวนจริงหรือไม่

พูดด้วย [[aleph-numbers|Aleph numbers]] และ [[beth-numbers|Beth numbers]] คือถามว่า:

`aleph_1 = beth_1` หรือเปล่า

## ทำไมสำคัญ

ถ้า `aleph_1 = beth_1` แปลว่าไม่มี infinity ขนาดอื่นแทรกระหว่างจำนวนนับกับจำนวนจริง. ถ้าไม่เท่ากัน แปลว่ายังมี infinity อีกชั้นหนึ่งตรงกลาง

ปัญหานี้อยู่ในรายการ Hilbert's problems ของ [[david-hilbert|David Hilbert]] และกลายเป็นตัวอย่างคลาสสิกของ [[undecidable-propositions|undecidable proposition]] ใน [[zfc-set-theory|ZFC]]

## คำตอบจาก Gödel และ Cohen

ถ้า ZFC ไม่ขัดแย้งในตัวเอง:

- [[kurt-godel|Gödel]] แสดงว่า ZFC หักล้าง Continuum Hypothesis ไม่ได้
- [[paul-cohen|Cohen]] แสดงว่า ZFC พิสูจน์ Continuum Hypothesis ไม่ได้

ผลคือ Continuum Hypothesis independent จาก ZFC. พูดแบบไม่ technical คือ ZFC ตัดสินคำถามนี้เองไม่ได้

## See also

- [[zfc-set-theory]]
- [[undecidable-propositions]]
- [[godel-incompleteness-theorems]]
