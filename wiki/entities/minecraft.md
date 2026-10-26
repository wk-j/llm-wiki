---
title: Minecraft
type: entity
tags: [game, procedural-generation, game-dev]
created: 2026-10-26
updated: 2026-10-26
sources: [math-of-procedural-generation-dekwit.md]
---

# Minecraft

Minecraft คือเกม sandbox ที่โลกทั้งใบประกอบจากบล็อก ผู้เล่นขุด สร้าง และสำรวจโลกที่เกมสร้างจาก seed ใน wiki นี้ Minecraft เป็นตัวอย่างหลักของ [[procedural-generation|procedural generation]] แบบ "โลกเป็นฟังก์ชัน" จากคลิปของ [[dekwit|DekWit]]

## เรื่องที่ wiki เก็บไว้

- **seed เดียวกัน โลกเดียวกัน:** พิมพ์ seed แล้วกด Create World ส่ง seed เดียวกันให้เพื่อน เพื่อนก็ได้ภูเขา ต้นไม้ และเพชรที่พิกัดเดิม ถ้า seed เป็นตัวอักษร เกมแปลงเป็นตัวเลขก่อน ดู [[pseudorandom-number-generator]]
- **LCG:** คลิปบอกว่า Minecraft รุ่นคลาสสิกใช้ LCG ที่ `m = 2^48` ซึ่งตรงกับ `java.util.Random` ตามเอกสารของ Oracle (ยังไม่ได้ตรวจว่าเวอร์ชันปัจจุบันยังใช้อยู่ไหม)
- **slime chunk:** เกมโยน seed กับพิกัด chunk เข้าสูตรเพื่อตัดสินว่า chunk ไหนมี slime แผนที่หา slime chunk ก็แค่รันสูตรเดียวกัน
- **เวอร์ชัน 1.18:** เปลี่ยนวิธีสร้างภูเขาและถ้ำ ถ้ำเกิดจาก noise 3 มิติที่ให้คะแนนทุกบล็อก ดู [[density-function-terrain]]
- **โลกไม่มีขอบ:** ตามทฤษฎีสร้าง chunk ใหม่ได้เรื่อย ๆ แต่เกมตั้งขีดจำกัดไว้ คลิปบอกว่านี่คือเหตุผลที่ Minecraft ต้องสร้างโลกเป็นฟังก์ชัน และถามพิกัดไหนก็ตอบได้ทันที ต่างจาก [[terraria|Terraria]]
- **ราคาที่จ่าย:** ในมุมของคลิป โลกมหาศาลแลกมากับพื้นที่ที่หน้าตาคล้ายกันไปหมด

## เรื่องที่ยังเปิด

คลิปเล่าว่าก่อน 1.18 Minecraft ใช้ heightmap ที่ทำโพรงไม่ได้ แต่ blog ของ Notch ปี 2011 เล่าว่าเปลี่ยนไปใช้ 3D noise แบบ density ตั้งแต่ช่วงแรกเพื่อให้มีหน้าผายื่น wiki เก็บทั้งสองด้านไว้ที่ [[density-function-terrain]]

## See also

- [[procedural-generation]]
- [[density-function-terrain]]
- [[pseudorandom-number-generator]]
- [[terraria]]
- [[no-mans-sky]]
- [[math-of-procedural-generation-dekwit]]
