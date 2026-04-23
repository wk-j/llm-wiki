---
title: Holographic UI
type: concept
tags: [ui, design, sci-fi, holographic, glassmorphism, diegetic]
created: 2026-04-14
updated: 2026-04-23
sources: [Holographic UI.md]
---

# Holographic UI / UI โฮโลแกรม

ภาษาการออกแบบ UI ที่จำลอง interface ที่เปล่งแสงและฉายภาพในอวกาศ — กึ่งโปร่งใส, เรืองแสง, และไร้น้ำหนัก ภาพลวงตาหลักคือ: **interface ทำจากแสง ไม่ใช่วัตถุ**

Holographic UI อยู่ตรงกลางระหว่าง [[glassmorphism]] (ซึ่งใช้เทคนิคความโปร่งใสและ backdrop-blur ร่วมกัน) และ [[diegetic-ui]] (ในสไตล์ย่อย "Holographic Projection") แต่เป็นระบบที่แตกต่างและมีข้อจำกัดและคำศัพท์เป็นของตัวเอง

## UI โฮโลแกรม vs. UI บนจอภาพปกติ

| คุณสมบัติ | จอภาพปกติ | โฮโลแกรม |
|---|---|---|
| พื้นหลัง | ทึบ / opaque | โปร่งใส / see-through |
| ขอบ | เส้นทึบ | ขอบเรืองแสง, halo อ่อนๆ |
| ความลึก | แบน | ระนาบ Z-planes เป็นชั้นๆ, parallax |
| สี | Full RGB gamut | เรืองแสงสีเดียวหรือสองสี |
| การโต้ตอบ | Click/tap | Gesture, proximity, hover |
| การเปลี่ยนสถานะ | ทันที | Fade / dematerialize (สลายไป) |

## ห้าเวอร์ชันย่อย

แต่ละเวอร์ชันมีเรื่องราวของสีและมีต้นแบบทางวัฒนธรรมที่แตกต่างกัน:

- **Pure Holo** — สีเดียว Cyan/blue. ต้นแบบ: Minority Report, แล็บของ Iron Man. โปร่งแสงสูงสุด, ขอบเรืองแสงบางๆ, panel ซ้อนกันเป็นชั้นๆ
- **Bio-Holo** — สีฟ้า-เขียวแบบเรืองแสงในสิ่งมีชีวิต. ต้นแบบ: Avatar / เครือข่าย Na'vi. รูปทรงออร์แกนิก, ขอบโค้ง, เส้นอนุภาค, การเชื่อมต่อคล้ายใยแมงมุม
- **Military Holo** — สีเหลืองอำพัน/ส้มบนพื้นเกือบดำ. ต้นแบบ: ห้องสงครามใน The Expanse. ข้อมูลหนาแน่น, ตารางข้อความแน่นๆ, tactical overlays, กรอบวงเล็บเชิงมุม
- **Ghost Holo** — สีม่วง/ชมพูมาเจนต้าบนพื้นน้ำเงิน-ดำมืด. ต้นแบบ: Ghost in the Shell, Cyberpunk. มี scan-line artifacts, glitch distortion, เอฟเฟกต์ข้อความที่เสียหาย
- **Clean Holo** — สีขาว/เงินบนพื้นมืด. ต้นแบบ: Apple Vision, โลกอนาคตอันใกล้. panel กระจกฝ้า, ขอบที่บอบบางมาก, เน้น typography, มีพื้นที่ว่าง

## Primitive หลักในการเรนเดอร์

### The Glass Panel

เป็น building block พื้นฐาน ทุก interface โฮโลแกรมประกอบด้วย glass panel:

- พื้นหลัง `rgba()` (ไม่เคยเป็นสีทึบ)
- ขอบ 1px พร้อมสีเรืองแสงที่เข้ากัน
- box-shadow สามชั้น: แสงฟุ้งด้านนอก + แสงเติมด้านใน + เส้นขอบสว่าง
- `backdrop-filter: blur()` สำหรับความลึก
- Scan-line overlay ผ่าน `::before` pseudo-element ด้วย repeating-linear-gradient

### Depth layering (การซ้อนชั้นความลึก)

ระนาบ Z-planes สามชั้นจำลองระยะการฉาย — ด้านหน้า (opacity เต็ม, เงาเข้ม), กลาง (opacity 0.9), หลัง (opacity 0.7, เงาน้อยที่สุด)

### Corner accents (การเน้นที่มุม)

รูปทรงขอบบางส่วนเฉพาะที่มุม (โดยใช้ pseudo-elements) แทนที่จะเป็นขอบเต็ม — เสริมความรู้สึกเหมือนแสงที่ถูกฉาย

### Glow text (ข้อความเรืองแสง)

Text-shadow ที่เข้ากับสีเน้นของ panel. Letter-spacing กว้าง (≥0.08em). Font weight บาง. มีสไตล์ที่แตกต่างกันสำหรับข้อความหลัก, ป้ายกำกับสีจาง, และค่าข้อมูล

## คำศัพท์เกี่ยวกับ Animation

Animation บังคับสี่อย่างที่สร้างภาพลวงตา "แสงที่มีชีวิต":

1.  **Materialize** — panel fade-in พร้อม scale-up เล็กน้อยและ blur ที่ชัดขึ้น (ตอน mount)
2.  **Breathe** — การกระพริบของแสงอย่างนุ่มนวลบน panel ที่ไม่ได้ใช้งานทั้งหมด (รอบ 3–5 วินาที, staggered delays)
3.  **Scan** — องค์ประกอบที่เคลื่อนไหวซึ่งแสดงถึงการประมวลผลที่กำลังทำงาน (อย่างน้อยหนึ่งอย่างต่อหน้าจอ)
4.  **Ring spin** — การหมุนอย่างต่อเนื่องบนมิเตอร์วงกลมหรือ loader

Optional: glitch distortion (เวอร์ชัน Ghost), particle float (บรรยากาศรอบข้าง), vanish/dematerialize (animation ตอนออก)

## รูปแบบ Layout

- **Command Deck** — layout 3-panel ที่เน้นตรงกลาง พร้อม panel สถานะ/ข้อมูลด้านข้าง และ ticker ด้านล่าง
- **Floating Cards** — ตารางกระจัดกระจายพร้อมการหมุนเล็กน้อยและความลึกที่แตกต่างกัน
- **Cockpit** — แถบข้อมูลแนวนอน (navigation / ภาพหลัก + เครื่องมือ / การแจ้งเตือน)

## ข้อจำกัดในการออกแบบ

- พื้นหลังต้องมืด (#000000–#0d0d20) — โฮโลแกรมไม่ฉายในเวลากลางวัน
- panel ทั้งหมดต้องกึ่งโปร่งใส — `rgba()` เท่านั้น, ห้ามใช้สีทึบ
- ทุกขอบต้องเรืองแสงผ่าน box-shadow
- ห้ามใช้ข้อความสีขาวล้วน — ให้ใช้สีเกือบขาวที่ย้อมสีตาม palette
- ห้ามมีมุมแหลม > border-radius 2px
- ไม่มีองค์ประกอบที่เป็นภาพถ่าย — UI โฮโลแกรมเป็นสิ่งก่อสร้างจากแสงล้วนๆ
- Typography: Google Fonts — Exo 2, Rajdhani, Orbitron, หรือ Share Tech Mono

## ความสัมพันธ์กับสไตล์อื่น

Holographic UI ทับซ้อนกับแต่แตกต่างจาก:

- **[[glassmorphism]]** — ใช้ backdrop-blur และความโปร่งใสร่วมกัน, แต่ glassmorphism ใช้พื้นหลังที่สว่าง/มีสีสัน ในขณะที่ holographic ต้องการพื้นหลังที่มืด
- **[[diegetic-ui]]** — holographic projection เป็นหนึ่งในห้าสไตล์ย่อยของ diegetic; holographic UI เป็นระบบการออกแบบที่กว้างกว่าซึ่งทำงานนอกบริบทเกม/เรื่องเล่าได้ด้วย
- **[[retro-futurism]]** — เวอร์ชัน Military Holo และ Ghost Holo มี DNA ทางสายตาร่วมกับ [[cassette-futurism]] และ [[soviet-cosmism]] ตามลำดับ, แต่ holographic UI มุ่งเป้าไปที่ "อนาคต" มากกว่า "อนาคตในมุมมองของอดีต"
- **[[cyberpunk-neon]]** — เวอร์ชัน Ghost Holo ทับซ้อนกับสุนทรียศาสตร์แบบ cyberpunk (สีม่วง/มาเจนต้า, เอฟเฟกต์ glitch)

## ดูเพิ่ม

- [[diegetic-ui]]
- [[glassmorphism]]
- [[retro-futurism]]
- [[ui-style-categories]]
- [[cassette-futurism]]
- [[soviet-cosmism]]
