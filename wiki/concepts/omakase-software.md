---
title: Omakase Software
type: concept
tags: [software-engineering, philosophy, developer-tools, linux, defaults]
created: 2026-09-07
updated: 2026-09-07
sources: [dhh-strategies-programming-with-ai-agents-lex-clips.md]
---

# Omakase Software / ซอฟต์แวร์แบบเชฟเลือกให้

**Omakase software** คือการแจกซอฟต์แวร์ที่ผู้สร้างเลือกของให้ครบมาแล้ว แทนที่จะให้ผู้ใช้ประกอบเอง คำว่า omakase มาจากร้านอาหารญี่ปุ่น แปลว่าให้เชฟเลือกให้ [[dhh|DHH]] ตั้งชื่อ [[omarchy|Omarchy]] จากคำนี้ และอธิบายจุดยืนไว้ใน [[dhh-strategies-programming-with-ai-agents-lex-clips|บทสัมภาษณ์กับ Lex Fridman]]

## ข้อโต้แย้งที่มีมาก่อน

ในวงการ Linux มีมุมที่ถือว่าการลงโปรแกรมมาให้ล่วงหน้าเป็น bloat หรือของเกินความจำเป็น เหตุผลคือไม่ใช่หน้าที่ของคนทำ distribution ที่จะตัดสินว่าคนอื่นควรใช้โปรแกรมอะไร ผู้ใช้ควรเลือกเองทั้งหมด

DHH ไม่เถียงว่ามีของเกิน เขาเถียงว่าการเลือกให้เป็น feature ไม่ใช่ bug

> "I'm the chef. I'm making the choices. And this is the collection of applications I think is awesome."

ของที่ Omarchy ลงมาให้มี OBS สำหรับอัดหน้าจอ, Kdenlive ซึ่งเป็น video editor, Omacut ที่เขาเขียนเองสำหรับตัดคลิปสั้น, Neovim, [[herdr|Herdr]], tmux, terminal, ธีมและภาพพื้นหลังที่คัดแล้ว

> "This is supposed to be a productive system the minute you unpack it."

**ได้อะไร:** เกณฑ์ตัดสินเปลี่ยนจาก "เล็กที่สุด" เป็น "พร้อมทำงานเร็วที่สุดหลังเปิดเครื่อง"

## เล็กกับพร้อมใช้ ไม่ใช่คนละทาง

จุดที่คนมักเข้าใจผิดคือคิดว่า omakase หมายถึงยอมให้ระบบอ้วน เรื่องที่ DHH เล่าในคลิปเดียวกันสวนกับความคิดนั้น เขาไล่รีดขนาด ISO จากราว 7.5 GB เหลือราว 5.85 GB ด้วยการทำ package รุ่น slim ของ font, บีบอัด driver แรงขึ้น และตัด variant ที่ไม่ได้ใช้ออก

สิ่งที่เขาไม่ตัดคือ **โปรแกรมที่คนได้ใช้จริง** สิ่งที่เขาตัดคือ **น้ำหนักที่ไม่ได้แลกมาด้วยประโยชน์** เช่น font variant ที่ไม่มีใครเปิด หรือ archive ที่บีบอัดไม่สุด กรณี [[voxtype|VoxType]] ชัดที่สุด เขาไม่ลง package นี้มาให้ในเครื่องเพราะมี model ราว 150 MB แต่เตรียมทางให้ติดตั้งง่ายตอนออนไลน์แทน

**ผลคือ:** omakase ไม่ใช่การเลิกสนใจขนาด มันคือการย้ายคำถามจาก "อันนี้กินพื้นที่เท่าไร" เป็น "พื้นที่ที่กินไปแลกมาด้วยอะไร"

## เกี่ยวกับ agent อย่างไร

สองเรื่องที่ต่อกับงาน agent โดยตรง

หนึ่ง ค่าเริ่มต้นที่มีความเห็นชัดเจนคือ context ให้ agent ด้วย เครื่องที่มีชุดเครื่องมือแน่นอนทำให้คำสั่งซ้ำ ๆ ทำงานเหมือนกันทุกเครื่อง ต่างจากเครื่องที่ทุกคนประกอบเองซึ่ง agent ต้องเดาก่อนว่ามีอะไรอยู่ ตรงนี้เป็น [[agent-experience|AX]] ระดับเครื่อง

สอง ต้นทุนของการเลือกให้ต่ำลงเมื่อการแก้ถูกลง เมื่อก่อนเชฟที่เลือกของให้ต้องรับภาระดูแลของทุกชิ้น พอเขียนเครื่องมือเล็ก ๆ ของตัวเองได้เร็วขึ้น เชฟก็เสิร์ฟของที่ทำเองได้มากขึ้น เช่น Omacut ที่มีอยู่เพราะเปิด timeline editor ทั้งตัวเพื่อตัดคลิปเดียวมันน่ารำคาญ ดู [[personalized-development-environment|Personalized Development Environment]] และ [[just-in-time-software|Just-in-Time Software]]

## ข้อแลกเปลี่ยนที่ยังอยู่

- ผู้ใช้ที่ไม่ชอบของที่เชฟเลือกต้องรื้อออกเอง ซึ่งบางทีเหนื่อยกว่าลงเพิ่มเอง
- ยิ่งลงมาให้เยอะ ผิวสัมผัสด้านความปลอดภัยและภาระการอัปเดตยิ่งกว้าง คลิปไม่ได้พูดถึงเรื่องนี้
- คำว่า "เชฟเลือกให้" ใช้ได้เมื่อเชฟกับลูกค้ามีรสนิยมใกล้กัน distribution ที่โตขึ้นจะเจอแรงกดให้ทำทุกอย่างให้ทุกคน ซึ่งขัดกับแนวคิดตั้งต้น

## See also

- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
- [[omarchy]]
- [[dhh]]
- [[personalized-development-environment]]
- [[malleable-tools]]
- [[just-in-time-software]]
- [[agent-experience]]
- [[papercut-features]]
- [[local-optimization-trap]]
