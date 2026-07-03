---
title: Cantor's Diagonal Argument
type: concept
tags: [mathematics, proof, set-theory, infinity]
created: 2026-07-03
updated: 2026-07-03
sources: [infinity-godel-incompleteness-mlhf.md]
---

# Cantor's Diagonal Argument / วิธีทแยงมุมของ Cantor

Cantor's diagonal argument คือบทพิสูจน์ของ [[georg-cantor|Georg Cantor]] ว่าเซตของจำนวนจริงนับไม่ได้ จึงมี cardinality ใหญ่กว่าจำนวนนับ

## วิธีคิด

สมมุติว่าเราสามารถ list จำนวนจริงทั้งหมดได้ แล้วจับคู่กับจำนวนนับครบทุกตัว. Cantor สร้างจำนวนจริงตัวใหม่โดยเลือกหลักทศนิยมที่ `n` ให้ต่างจากหลักทศนิยมที่ `n` ของจำนวนจริงตัวที่ `n` ใน list

ตัวเลขใหม่นี้จะต่างจากทุกตัวใน list อย่างน้อยหนึ่งหลัก:

- ต่างจากตัวที่ 1 ที่หลักที่ 1
- ต่างจากตัวที่ 2 ที่หลักที่ 2
- ต่างจากตัวที่ 3 ที่หลักที่ 3

ดังนั้นมันไม่อยู่ใน list ทั้งที่สมมุติว่า list ครบแล้ว. เกิด contradiction

## See also

- [[uncountable-infinity]]
- [[cardinality]]
- [[continuum-hypothesis]]
