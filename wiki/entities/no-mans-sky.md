---
title: No Man's Sky
type: entity
tags: [game, procedural-generation, game-dev]
created: 2026-10-26
updated: 2026-10-26
sources: [math-of-procedural-generation-dekwit.md]
---

# No Man's Sky

No Man's Sky คือเกมสำรวจอวกาศที่มีดาวให้ไปเยือนราว 2^64 ดวง (18,446,744,073,709,551,616) ทุกดวงเกมสร้างจาก seed ไม่ได้มีใครวาดไว้ ใน wiki นี้มันเป็นตัวอย่างที่ชัดที่สุดว่าโลกในเกมเป็น "ฟังก์ชัน ไม่ใช่ข้อมูล" จากคลิปของ [[dekwit|DekWit]]

## เรื่องที่ wiki เก็บไว้

- **ดาวเยอะกว่าที่ไฟล์จะจุได้:** คลิปบอกว่าไฟล์เกมบน PC ตอนเปิดตัวมีขนาดไม่กี่ GB ถ้าเก็บข้อมูลทุกดวงจริง ฮาร์ดดิสก์ทั้งโลกรวมกันก็ไม่พอ (ขนาดไฟล์ยังไม่ได้ตรวจ)
- **seed 64 bit:** จำนวนดาวมาจากจำนวนค่าที่ตัวแปร 64 bit แทนได้ [Wikipedia](https://en.wikipedia.org/wiki/No_Man%27s_Sky) ก็อธิบายตัวเลข "over 18 quintillion" ด้วย seed 64 bit เช่นกัน
- **seed ซ้อนชั้น:** seed ของจักรวาล → galaxy → ระบบสุริยะ → ดาวเคราะห์ → ภูเขา ทะเล ต้นไม้ ดู [[procedural-generation]]
- **ดาวทรงกลม:** คลิปอธิบายด้วยภาพก้านเม่นที่ยืดหดตาม noise แล้วต่อด้วย density แบบทรงกลมเพื่อให้มีถ้ำ ดู [[density-function-terrain]]
- **domain warping:** คลิปเล่าเทคนิคนี้ในช่วงดาวของ No Man's Sky เพื่อให้ภูเขาไม่เหมือนก้อนดินน้ำมัน ดู [[domain-warping]]
- **ตอนต่อไป:** ท้ายคลิปทิ้งคำถามไว้ว่าสมการที่สร้างเอเลี่ยนในเกมนี้หน้าตาเป็นยังไง

## ข้อสังเกต

- คลิปพูดว่า "18 ล้านล้านดวง" แต่ 2^64 ในภาษาไทยคือราว 18 ล้านล้านล้าน (18 quintillion) หน้านี้ใช้ 2^64
- วิธีปั้นดาวในหน้านี้เป็นคำอธิบายของคลิป ไม่ได้อ้างเอกสารของผู้พัฒนา

## See also

- [[procedural-generation]]
- [[density-function-terrain]]
- [[domain-warping]]
- [[pseudorandom-number-generator]]
- [[minecraft]]
- [[math-of-procedural-generation-dekwit]]
