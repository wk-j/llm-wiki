---
title: Omarchy
type: entity
tags: [linux, developer-tools, ai, agents, terminal]
created: 2026-09-07
updated: 2026-09-07
sources: [dhh-strategies-programming-with-ai-agents-lex-clips.md, dhh-ai-programming-setup-lex-clips.md, "https://omarchy.org"]
---

# Omarchy / Linux distribution ของ DHH

Omarchy เป็น Linux distribution ที่ [[dhh|DHH]] ผู้สร้าง Ruby on Rails ทำขึ้นเอง ชื่อมาจากคำว่า **omakase** ที่แปลว่าให้เชฟเลือกให้ ตัวระบบวางอยู่บน Arch ตามที่ผู้พูดอ้างถึง package จาก repo ของ Arch ในบทสัมภาษณ์ เว็บของโครงการอยู่ที่ [omarchy.org](https://omarchy.org)

หน้านี้รวบรวมจากสิ่งที่ DHH เล่าในคลิป Lex Clips สองตอน คือ [[dhh-strategies-programming-with-ai-agents-lex-clips|ตอนเรื่องวิธีทำงานกับ agent]] และ [[dhh-ai-programming-setup-lex-clips|ตอนเรื่องชุดเครื่องมือ]] ไม่ใช่จากเอกสารของโครงการ

## จุดยืน: เลือกของให้ครบ

Omarchy ลงโปรแกรมมาให้พร้อมใช้ ไม่ใช่ระบบเปล่าที่ผู้ใช้ต้องประกอบเอง ของที่ DHH ยกตัวอย่างมี OBS สำหรับอัดหน้าจอ, Kdenlive ซึ่งเป็น video editor แบบ timeline, Omacut ที่เขาเขียนเองสำหรับตัดคลิปสั้นด้วยคีย์บอร์ด, Neovim, [[herdr|Herdr]], tmux, terminal, ธีมและภาพพื้นหลังชุดที่เขาคัดเอง

เรื่องนี้เป็นจุดที่เขาเถียงกับสาย Linux ดั้งเดิมที่ถือว่าการลงของมาให้เป็น bloat ดู [[omakase-software|Omakase Software]] สำหรับข้อโต้แย้งทั้งสองด้าน

การตั้งค่าส่วน Linux configuration เขียนด้วย bash เป็นหลัก เพราะ bash ถูกทำมาสำหรับงาน system administration และเขามีไฟล์ `AGENTS.md` กำกับสไตล์ให้ agent เช่น ข้อห้ามเรื่อง early exit

## เรื่องขนาดและความเร็วของ installer

ในคลิปเรื่องวิธีทำงานกับ agent DHH เล่าว่าไล่รีดขนาด ISO จากราว 7.5 GB เหลือราว 5.85 GB เพราะเวลาติดตั้งส่วนใหญ่หมดไปกับการคลาย package ที่บีบอัดไว้ ขนาดที่ลดลงจึงแปลเป็นเวลาที่ลดลงเกือบเป็นสัดส่วนเดียวกัน วิธีที่ใช้คือทำ package รุ่น slim ของ JetBrains font (200 MB → ราว 16 MB), บีบอัด Nvidia driver ด้วย zstd ระดับแรงสุด และตัดของที่ไม่ได้ใช้ออกทีละชิ้น

agent ยังเสนอวิธีที่เขาไม่ได้คิดถึง คือให้ installer เริ่มโหลดของเบื้องหลังระหว่างที่ยังรอคนตอบคำถามตอนตั้งค่า

font ที่ใช้เป็น JetBrains font รุ่น monospace แบบ nerd font patched เพราะเป็น font เดียวที่เรนเดอร์สวยใน Ghostty ซึ่งเป็น terminal ของ Mitchell Hashimoto

ตัวเลขทั้งหมดเป็นการเล่าจากความจำในบทสัมภาษณ์ ไม่ใช่ release note

## เกี่ยวกับ agent

DHH มองว่า Linux เอื้อต่อ agent เพราะสั่งผ่าน CLI และแก้ config file ได้ตรง ๆ ไม่ต้องคลิก GUI ดู [[agent-experience|Agent Experience (AX)]]

รุ่นที่เขาเรียกในคลิปว่า **Omarchy Quattro** เขาบอกว่าดีในฐานะระบบที่ดัดแปลงได้ เพราะเพิ่มความสามารถได้ด้วยการคุยกับ agent ภาพต่อไปที่เขาอยากเห็นคือรวมเรื่องเสียงเข้ามา คือพูดขอให้เครื่องทำ panel ดูราคาหุ้นแล้วมันทำมาให้ ดู [[malleable-tools|Malleable Tools]] และ [[just-in-time-software|Just-in-Time Software]] ชื่อรุ่นนี้บันทึกตามที่ผู้พูดออกเสียง ยังไม่ได้ตรวจกับ release ของโครงการ

ระบบมี [[voxtype|VoxType]] เป็นตัวเลือกสำหรับถอดเสียงเป็นข้อความ แต่ไม่ได้ลงมาให้ตั้งแต่แรกเพราะ package มี model ราว 150 MB

## See also

- [[dhh]]
- [[omakase-software]]
- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
- [[dhh-ai-programming-setup-lex-clips]]
- [[herdr]]
- [[voxtype]]
- [[malleable-tools]]
- [[agent-experience]]
