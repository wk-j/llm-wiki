---
title: Density Function Terrain
type: concept
tags: [procedural-generation, terrain-generation, noise, game-dev]
created: 2026-10-26
updated: 2026-10-26
sources: [math-of-procedural-generation-dekwit.md]
---

# Density Function Terrain / ภูมิประเทศแบบถามทุกจุด

แทนที่จะถามว่า "พื้นตรงนี้สูงเท่าไหร่" (heightmap) วิธีนี้ถามทุกจุดในพื้นที่ 3 มิติว่า "ตรงนี้เป็นของแข็งหรืออากาศ" โดยคำนวณคะแนน (density) ของแต่ละจุด บวกเป็นหิน ลบเป็นอากาศ ถ้ำ หน้าผายื่น และภูเขาที่ข้างในกลวงเลยเกิดได้ ซึ่ง heightmap ทำไม่ได้ ในคลิป [[math-of-procedural-generation-dekwit|คณิตศาสตร์สร้างโลกได้ยังไง]] วิธีนี้โผล่สองรอบ ทั้งใน [[minecraft|Minecraft]] และดาวของ [[no-mans-sky|No Man's Sky]]

## Heightmap ติดตรงไหน

heightmap รับพิกัด XZ บนพื้น แล้วคืนความสูงกลับมา 1 ค่า ใต้เส้นเป็นหิน เหนือเส้นเป็นอากาศ หนึ่งคอลัมน์มีผิวได้ผิวเดียว เลยไม่มีโพรงหรือส่วนที่ยื่นออกมา

ถ้าอยากได้ถ้ำ ต้องไปเจาะเพิ่มทีหลัง คลิปเล่าว่า Minecraft แบบเดิมปั้นภูเขาตัน ๆ ก่อน แล้วปล่อยโปรแกรมชื่อ carver ที่ทำงานคล้ายหนอนลงไปแทะหินแบบสุ่ม ได้อุโมงค์แคบที่หน้าตาซ้ำและไม่เกี่ยวกับภูมิประเทศรอบ ๆ

**ผลคือ:** ตราบใดที่คำถามคือ "สูงเท่าไหร่" ถ้ำจะเป็นของแปะทีหลังเสมอ

## วิธีคิดแบบคะแนน

```
density(x, y, z) = base(y) + noise(x, y, z)
```

- `base(y)` ยิ่งลึกยิ่งเป็นบวก ยิ่งสูงยิ่งติดลบ
- `noise` เป็น noise 3 มิติที่มีทั้งค่าบวกและลบ บวกทับลงไปทุกบล็อก
- density ตั้งแต่ 0 ขึ้นไปเป็นหิน ต่ำกว่า 0 เป็นอากาศ

ใต้ดินลึก ๆ ปกติควรเป็นหินตัน แต่ถ้า noise ตรงนั้นติดลบมากพอจะหักล้าง base คะแนนรวมก็ติดลบ จุดนั้นกลายเป็นอากาศ ช่องอากาศกลางชั้นหินพวกนี้คือถ้ำ

**ผลคือ:** ถ้ำ หน้าผา และภูเขามาจากสมการเดียวกัน ถ้ำเลยกลมกลืนกับภูมิประเทศรอบตัว

## ใช้กับดาวทรงกลม

ดาวที่เดินวนรอบได้เจอปัญหาเดียวกันในอีกรูป คลิปเล่าเป็นสองขั้น

1. **ก้านเม่น (heightmap แบบรัศมี):** นึกภาพแกนกลางดาวที่มีก้านพุ่งออกทุกทิศ ส่งทิศของก้านไปถาม noise ว่าควรยืดหรือหด ได้ `r(d) = R + f(d)` เช่น `R` = 3,000 เมตร ยืดเป็นภูเขา หดเป็นเหว แต่หนึ่งทิศได้รัศมีค่าเดียว ถ้าผิวอยู่ที่ 3,200 เมตร ตั้งแต่ใจกลางถึง 3,200 เมตรต้องตันหมด ทำถ้ำไม่ได้
2. **density แบบทรงกลม:** ไล่ถามทุกจุดในดาว เอาระยะจากใจกลางมาลบ `density(p) = R + f(p) − |p|` บวกแปลว่าอยู่ในเนื้อดาว ลบแปลว่าอยู่ในอากาศ

**ผลคือ:** พื้นราบหรือทรงกลมก็แก้ด้วยการเปลี่ยนคำถามแบบเดียวกัน จาก "ผิวอยู่ตรงไหน" เป็น "จุดนี้คืออะไร"

## ประวัติใน Minecraft: ยังมีสองเรื่องเล่า

เรื่องนี้แหล่งข้อมูลยังไม่ลงรอยกัน wiki เก็บไว้ทั้งสองด้าน

- **คลิปของ [[dekwit|DekWit]]:** Minecraft ก่อนเวอร์ชัน 1.18 ใช้ heightmap ที่ให้ความสูงค่าเดียวต่อพิกัด XZ แล้วพึ่ง carver ทำถ้ำ เวอร์ชัน 1.18 เปลี่ยนมาใช้สมการ 3 มิติที่สแกนทุกบล็อก
- **blog ของ Notch ปี 2011** ("Terrain generation, Part 1" ยกมาใน [Stack Overflow](https://stackoverflow.com/questions/6091468/how-is-a-3d-perlin-noise-function-used-to-generate-terrain)): Notch (ผู้สร้าง Minecraft) เล่าว่าเคยใช้ 2D heightmap แต่ "there's no way for this method to generate any overhangs" จึงเปลี่ยนไปใช้ 3D Perlin noise และ "treated the noise value as the 'density', where anything lower than 0 would be air"
- **ฝั่ง Minecraft เอง:** [snapshot 21w06a](https://www.minecraft.net/en-us/article/minecraft-snapshot-21w06a) ในช่วงพัฒนา 1.18 เรียก noise caves (cheese, spaghetti) ว่า "a new way of generating caves" ส่วน [Minecraft Wiki](https://minecraft.wiki/w/Cave) บอกว่าทุกวันนี้ยังมี carver caves ทำงานคู่กับ noise caves และ [noise router](https://minecraft.wiki/w/Noise_router) คือชุด density function ที่คำนวณค่าให้ทุกตำแหน่งบล็อก

wiki อ่านว่า รูปทรงพื้นแบบ density มีมาตั้งแต่ก่อน 1.18 สิ่งที่ 1.18 เพิ่มคือถ้ำที่เกิดจาก noise ใน density เดียวกัน แทนที่จะพึ่ง carver อย่างเดียว คลิปน่าจะย่อสองเรื่องนี้รวมกัน แต่ wiki ยังไม่ได้ตรวจ source code ของแต่ละเวอร์ชัน ข้อนี้จึงยังเป็นคำถามเปิด

## See also

- [[perlin-noise]]
- [[fractal-noise]]
- [[domain-warping]]
- [[procedural-generation]]
- [[minecraft]]
- [[no-mans-sky]]
- [[math-of-procedural-generation-dekwit]]
