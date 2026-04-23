---
title: Cassette Futurism
type: concept
tags: [ui, design, retro-futurism, sci-fi]
created: 2026-04-13
updated: 2026-04-23
sources: [retro-futuristic-ui-design, imetomi-retro-futuristic-ui]
---

# Cassette Futurism

**Cassette Futurism** คือ subgenre ของ [[retro-futurism]] ที่มีรากฐานจากยุค 1970s–80s — ยุคของคอมพิวเตอร์เทอร์มินัลที่ดูเทอะทะ, สัญญาณรบกวนแบบ VHS, และคอมพิวเตอร์ยุคเทปคาสเซ็ท เป็นภาพอนาคตในจินตนาการของคนที่เพิ่งเคยเห็นคอมพิวเตอร์อย่าง BBC Micro แล้วคิดว่า *"นี่แหละคือทิศทางที่โลกกำลังจะไป"*

## ลักษณะทางภาพ (Visual Characteristics)

- **พื้นหลัง:** สีเกือบดำ (`#050508`)
- **สีหลัก:** สีเขียว Matrix (`#00ff41`), ตัดด้วยสีม่วงแดง (magenta) และใช้สีเหลืองสำหรับการแจ้งเตือน (alerts)
- **เอฟเฟกต์:** เส้นสแกนของจอ CRT และแสงฟอสเฟอร์เรืองรอง
- **ฟอนต์:** ฟอนต์ Monospace เช่น `VT323` หรือ `Share Tech Mono`
- **องค์ประกอบ:** Progress bar แบบ ASCII, เคอร์เซอร์กระพริบ, และการเรนเดอร์ข้อความสไตล์เทอร์มินัล

## ตัวอย่างอ้างอิง (Key References)

- **MUTHUR:** อินเทอร์เฟซคอมพิวเตอร์ในภาพยนตร์เรื่อง *Alien*
- **WarGames (1983):** ภาพยนตร์ปี 1983
- **BBC Micro:** และคอมพิวเตอร์ตามบ้านในยุคแรกๆ
- **VHS-era recording equipment:** อุปกรณ์บันทึกวิดีโอในยุค VHS

## การนำไปใช้ (Implementation)

หัวใจหลักคือการทำให้อินเทอร์เฟซดูเหมือนหน้าจอคอมพิวเตอร์เทอร์มินัลยุคเก่า โดยใช้ pattern ที่เรียกว่า **Terminal / Phosphor Screen**: ข้อความสีเขียวฟอสเฟอร์บนพื้นกระจกสีเข้ม, มีเส้นสแกน, และเคอร์เซอร์กระพริบ องค์ประกอบสำคัญได้แก่ `TerminalWindow`, `PhosphorText`, `CommandLine`, และ `ASCII ProgressBar`

## เทคนิคการสร้างเอฟเฟกต์ CRT ด้วย CSS

[[imetomi-retro-futuristic-ui|React component ของ Imetomi]] พิสูจน์ให้เห็นว่าเราสามารถสร้างเอฟเฟกต์จอ CRT ที่สมจริงได้ด้วย **การซ้อน CSS layer เพียงอย่างเดียว** โดยไม่ต้องใช้ WebGL หรือ canvas เลย สูตรคือการซ้อน layer โปร่งแสง 5-7 ชั้น (เช่น เส้นสแกนที่สร้างจาก `repeating-gradient`, ขอบมืด (vignette) จาก `radial-gradient`, แสงสะท้อน, โอเวอร์เลย์กระจก, และเงาขอบ) แต่ละ layer นั้นเรียบง่าย แต่เมื่อรวมกันแล้วให้ผลลัพธ์ที่น่าทึ่ง

รายละเอียดสำคัญ:
- ใช้ `border-radius` แบบวงรี (elliptical) เพื่อจำลองความโค้งของหน้าจอ
- ซ้อน `text-shadow` หลายๆ ชั้นเพื่อสร้างเอฟเฟกต์แสงฟอสเฟอร์เรืองรอง (สีอำพัน `#ff6a00` หรือสีเขียว `#00ff41`)
- ใช้ `perspective` ของ CSS บน wrapper เพื่อสร้างมิติความลึกเล็กน้อย
- ใช้ `hue-rotate` และ `position` ที่สั่นเล็กน้อย (jitter) เพื่อสร้างเอฟเฟกต์ภาพสั่น (glitch)

## See also

- [[retro-futurism]]
- [[atompunk]]
- [[raygun-gothic]]
- [[imetomi-retro-futuristic-ui]]
- [[nathan-david-jones]]
