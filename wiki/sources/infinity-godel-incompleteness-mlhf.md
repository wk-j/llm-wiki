---
title: เมื่อ Infinity เขย่าวงการคณิตศาสตร์ | Gödel's Incompleteness Theorems
type: source
tags: [mathematics, infinity, set-theory, logic, foundations]
created: 2026-07-03
updated: 2026-07-03
sources: []
---

# เมื่อ Infinity เขย่าวงการคณิตศาสตร์ / Gödel's Incompleteness Theorems

สรุปวิดีโอภาษาไทยของ [[mlhf|แมทเล่าให้ฟัง / MLHF]] ว่าด้วย [[infinity|infinity]], [[cardinality|cardinality]], [[cantor-diagonal-argument|Cantor's diagonal argument]], [[continuum-hypothesis|Continuum Hypothesis]], และ [[godel-incompleteness-theorems|Gödel's incompleteness theorems]]

- URL: https://www.youtube.com/watch?v=HWVbY9MdJ4w
- Author: [[mlhf|แมทเล่าให้ฟัง / MLHF]]
- รูปแบบ: YouTube transcript ภาษาไทย
- แกนเรื่อง: พอศึกษาขนาดของ infinity อย่างจริงจัง เราจะเจอคำถามที่ระบบคณิตศาสตร์ตอบไม่ได้จาก axiom ที่มีอยู่ ภาพ “คณิตศาสตร์พิสูจน์ได้ทุกอย่าง” เลยสั่นคลอน

## ภาพรวม

วิดีโอเริ่มจาก intuition ง่าย ๆ: จำนวนนับกับเลขคู่ดูเหมือนควรมีจำนวนไม่เท่ากัน เพราะเลขคู่เป็นแค่ครึ่งหนึ่งของจำนวนนับ. แต่พอใช้การจับคู่แบบ 1:1 ทั้งสองเซตกลับมีขนาดเท่ากันในความหมายของ [[cardinality|cardinality]]

จากนั้นเรื่องค่อย ๆ ไต่ขึ้น:

- infinity แบบนับได้ เช่น จำนวนนับ เลขคู่ จำนวนเต็ม จำนวนเฉพาะ และเศษส่วน
- infinity แบบนับไม่ได้ เช่น จำนวนจริง
- [[cantor-diagonal-argument|Cantor's diagonal argument]] ที่พิสูจน์ว่าจำนวนจริงใหญ่กว่าจำนวนนับ
- [[beth-numbers|Beth numbers]] และ [[aleph-numbers|Aleph numbers]] สำหรับจัดลำดับขนาด infinity
- [[continuum-hypothesis|Continuum Hypothesis]] ว่ามี infinity อื่นแทรกระหว่างจำนวนนับกับจำนวนจริงไหม
- [[zfc-set-theory|ZFC set theory]] และข้อจำกัดของระบบ axiom
- [[godel-incompleteness-theorems|Gödel's incompleteness theorems]] ที่บอกว่าระบบคณิตศาสตร์ที่แรงพอจะมี statement จริงบางอย่างที่พิสูจน์ไม่ได้ในระบบนั้น

ได้อะไร: infinity ไม่ใช่แค่ “ใหญ่แบบไม่มีที่สิ้นสุด” แต่มีชั้น มีขนาด และบางคำถามเกี่ยวกับมันแตะขอบเขตของสิ่งที่ระบบคณิตศาสตร์พิสูจน์ได้

## Cardinality: ขนาดของเซตแบบไม่พึ่งสามัญสำนึก

คำว่า “จำนวนสมาชิก” ใช้กับเซตจำกัดได้ตรง ๆ แต่พอเป็นเซตอนันต์ intuition จะหลอกเราได้ง่าย. วิธีที่วิดีโอใช้คือดูว่าเซตสองเซตจับคู่กันแบบ 1:1 ได้ไหม

ตัวอย่าง:

- จำนวนนับ `1, 2, 3, ...`
- เลขคู่ `2, 4, 6, ...`

จับคู่ได้ด้วยสูตร `n -> 2n`. ไม่มีตัวไหนตกหล่น และไม่มีตัวไหนถูกจับคู่ซ้ำ. ดังนั้นสองเซตนี้มี cardinality เท่ากัน แม้เลขคู่จะดูเหมือน “ครึ่งหนึ่ง” ของจำนวนนับก็ตาม

ผลคือ: ในโลกของ infinite sets คำว่า “ส่วนหนึ่งของเซต” ไม่ได้แปลว่าต้องเล็กกว่าเสมอไป

## Countable infinity และ uncountable infinity

Infinity ที่จับคู่กับจำนวนนับได้เรียกว่า [[countable-infinity|countable infinity]]. วิดีโอยกตัวอย่างว่าเซตเหล่านี้มีขนาดแบบเดียวกัน:

- จำนวนนับ
- เลขคู่
- จำนวนเต็ม
- จำนวนเฉพาะ
- จำนวนตรรกยะ / เศษส่วน

แต่จำนวนจริงไม่อยู่กลุ่มนี้. [[georg-cantor|Georg Cantor]] ใช้ [[cantor-diagonal-argument|diagonal argument]] พิสูจน์ว่าไม่ว่าจะพยายาม list จำนวนจริงอย่างฉลาดแค่ไหน เราสร้างจำนวนจริงใหม่ที่ต่างจากทุกตัวใน list ได้เสมอ

พูดง่าย ๆ: ถ้าบอกว่าจำนวนจริงทั้งหมดถูก list ไว้แล้ว Cantor จะสร้างตัวเลขที่หลุดจาก list นั้นได้หนึ่งตัวเสมอ. นี่ทำให้จำนวนจริงเป็น [[uncountable-infinity|uncountable infinity]]

## Beth numbers และ Aleph numbers

วิดีโอใช้ [[beth-numbers|Beth numbers]] เพื่อเล่าแนวทางสร้าง infinity ที่ใหญ่ขึ้น:

- `beth_0` คือ cardinality ของจำนวนนับ
- `beth_1` คือ cardinality ของจำนวนจริง หรือ power set ของจำนวนนับ
- `beth_2` คือ power set ของเซตที่มีขนาด `beth_1`

ส่วน [[aleph-numbers|Aleph numbers]] ใช้เรียง cardinality ของ infinite sets จากเล็กไปใหญ่:

- `aleph_0` คือ infinity ที่เล็กที่สุด เท่ากับขนาดของจำนวนนับ
- `aleph_1` คือ cardinality ถัดไปที่ใหญ่กว่า `aleph_0`

คำถามใหญ่จึงกลายเป็น: `aleph_1` เท่ากับ `beth_1` ไหม

## Continuum Hypothesis

[[continuum-hypothesis|Continuum Hypothesis]] คือคำถามว่ามีขนาด infinity ที่แทรกอยู่ระหว่างจำนวนนับ (`aleph_0`) กับจำนวนจริง (`beth_1`) หรือไม่

ถ้าไม่มี แปลว่า `aleph_1 = beth_1`. ถ้ามี แปลว่าจำนวนจริงไม่ใช่ infinity ถัดจากจำนวนนับทันที

วิดีโอบอกว่านี่เป็นหนึ่งใน 23 ปัญหาของ [[david-hilbert|David Hilbert]] ในปี 1900 และเป็นโจทย์ที่ต้องรอหลายสิบปีถึงจะเข้าใจคำตอบที่แปลกมาก: ไม่ใช่ว่ามันจริงหรือเท็จใน ZFC แต่ ZFC ตัดสินมันไม่ได้

## ZFC และ undecidable statement

[[zfc-set-theory|ZFC]] คือระบบ axiom ของ set theory ที่มักใช้เป็นรากฐานของคณิตศาสตร์สมัยใหม่. วิดีโออธิบาย axiom แบบเข้าใจง่ายว่าเป็นข้อเริ่มต้นที่เรายอมรับไว้ก่อน แล้วใช้พิสูจน์ข้ออื่นต่อ

ในกรณี Continuum Hypothesis:

- [[kurt-godel|Kurt Gödel]] แสดงว่า ถ้า ZFC ไม่ขัดแย้งในตัวเอง ก็หักล้าง Continuum Hypothesis จาก ZFC ไม่ได้
- [[paul-cohen|Paul Cohen]] แสดงว่า ถ้า ZFC ไม่ขัดแย้งในตัวเอง ก็พิสูจน์ Continuum Hypothesis จาก ZFC ไม่ได้

ดังนั้น Continuum Hypothesis เป็น [[undecidable-propositions|undecidable]] จาก ZFC: จะเพิ่มเป็น axiom ว่าจริงก็ได้ หรือเพิ่มว่าเท็จก็ได้ โดยไม่ทำให้ระบบเดิมพัง ถ้าระบบเดิมไม่ขัดแย้งในตัวเอง

## Gödel's incompleteness theorems

วิดีโอขยายจาก Continuum Hypothesis ไปสู่ [[godel-incompleteness-theorems|Gödel's incompleteness theorems]]. ใจความคือ ต่อให้เราออกแบบระบบ axiom ฉลาดแค่ไหน ถ้าระบบนั้นแรงพอจะทำ arithmetic ได้และไม่ขัดแย้งในตัวเอง ก็จะมี statement บางอย่างที่จริงแต่พิสูจน์ไม่ได้ในระบบนั้น

ผลกระทบทางใจของเรื่องนี้ใหญ่: นักคณิตศาสตร์อาจใช้เวลาหลายปีหรือทั้งชีวิตแก้โจทย์หนึ่ง โดยไม่รู้ว่าโจทย์นั้นอาจเป็นชนิดที่ระบบ axiom ที่ใช้อยู่ตอบไม่ได้

ได้อะไร: ปัญหาไม่ได้อยู่ที่ ZFC “ห่วย” แต่เป็นข้อจำกัดเชิงโครงสร้างของระบบ formal ที่แรงพอ

## Caveats จาก transcript

- Transcript เรียกคำว่า undecidable เพี้ยนเป็น “undesirable” ช่วง Continuum Hypothesis; สรุปนี้ใช้คำว่า undecidable
- Transcript รวม timeline ของ Gödel/Cohen ไว้เหมือนตีพิมพ์พร้อมกันในปี 1963. สรุปนี้แยกใจความมาตรฐานไว้ว่า Gödel ให้ผลฝั่ง consistency/ไม่อาจหักล้างก่อน และ Cohen ให้ผล independence ฝั่งไม่อาจพิสูจน์ในปี 1963. ควรเก็บ transcript wording เป็นความย่อของวิดีโอ ไม่ใช่ timeline ละเอียด
- วิดีโอใช้คำว่า Beth/Beth number และ Aleph/Aleph number หลายจุดผ่าน auto-caption ที่เพี้ยน เช่น “Bed”, “B Zero”, “alf” จึง normalize ชื่อคณิตศาสตร์ให้เป็นรูปมาตรฐาน

## See also

- [[infinity]]
- [[cardinality]]
- [[countable-infinity]]
- [[uncountable-infinity]]
- [[cantor-diagonal-argument]]
- [[continuum-hypothesis]]
- [[zfc-set-theory]]
- [[godel-incompleteness-theorems]]
- [[undecidable-propositions]]
