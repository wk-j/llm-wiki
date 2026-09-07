---
title: David Heinemeier Hansson (DHH)
type: entity
tags: [people, programming, ai, linux]
created: 2026-09-06
updated: 2026-09-07
sources: [dhh-ai-programming-setup-lex-clips.md, dhh-strategies-programming-with-ai-agents-lex-clips.md, i-was-replaced-by-ai-typecraft.md]
---

# David Heinemeier Hansson (DHH) / ผู้สร้าง Ruby on Rails

David Heinemeier Hansson หรือ DHH เป็นโปรแกรมเมอร์ผู้สร้าง Ruby on Rails ซึ่งเป็น framework สำหรับเว็บ และ [[omarchy|Omarchy]] ซึ่งเป็นระบบ Linux คำแนะนำแขกรับเชิญใน [[dhh-ai-programming-setup-lex-clips|บทสัมภาษณ์เรื่องชุดเครื่องมือ AI]] ระบุว่าเขาเป็น CTO ของ 37signals และเป็นนักแข่งรถด้วย

## การทำงานกับ agent ที่เขาเล่า

DHH ย้ายจาก TextMate ที่ใช้เกือบ 20 ปีมาทำงานบน Linux และคุม agent หลายตัวใน terminal เขาใช้ [[herdr|Herdr]] จัด session และแจ้งเตือน ใช้ [[tailscale|Tailscale]] เชื่อมเครื่องที่อยู่คนละสถานที่ และยังใช้ Neovim เปิดดู code รอบส่วนที่ agent แก้

เขากะว่าตามงานได้ประมาณ 16 งานพร้อมกัน ก่อนชนขีดจำกัดของตัวเอง ยิ่ง agent เร็ว จำนวนงานที่ตามไหวก็ยิ่งลดลง ตัวเลขนี้เป็นประสบการณ์ส่วนตัว ไม่ใช่สูตรเพิ่ม productivity

## สิ่งที่เขาบอกว่าคนยังต้องทำเอง

ใน [[dhh-strategies-programming-with-ai-agents-lex-clips|คลิปอีกตอนของบทสัมภาษณ์เดียวกัน]] DHH เล่าสิ่งที่ agent ยังไม่ทำเองคือลดความซับซ้อน เขาเจอซ้ำ ๆ ว่า agent ทำเสร็จบอกว่าเสร็จ agent อีกตัว review ก็บอกว่าผ่าน แต่พอเขาทักว่าดูซับซ้อนเกินไป มันตัดเหลือครึ่งเดียวทันที

> "But you actually do have to tell them, 'Make it simpler.'"

เขาเทียบว่าตัวเองเป็น editor หรือเป็น Da Vinci ที่มีลูกศิษย์ช่วยสกัดหิน ส่วนเขาบอกได้ว่าสัดส่วนยังไม่สมกับปัญหา ดู [[make-it-simpler|Make It Simpler]]

## จุดยืนเรื่องเขียน bash เองที่เปลี่ยนไป

คลิปแรกเขาเล่าว่าเคยขอ bash จาก agent แล้วพิมพ์เองใหม่ เพราะไม่อยากให้ความสามารถไหลออกจากนิ้ว ถึงขั้นตั้งใจไปเรียน bash ให้เขียนได้จริง คลิปที่สองเขาบอกว่าไม่ได้เขียน bash เองมาสองเดือนกว่าแล้ว เพราะ agent เก่งขึ้นมาก

เก็บทั้งสองข้างไว้เทียบใน [[skill-atrophy|Skill Atrophy]] จุดที่ต่างจากคนทั่วไปคือเขาเรียนไปก่อนแล้วจึงเลิกเขียน ไม่ใช่ไม่เคยเขียนเองมาก่อน

สิ่งที่เขายังต้องทำซ้ำคือเตือน agent ให้กลับไปอ่าน `AGENTS.md` เพราะมีข้อห้ามเรื่อง early exit อยู่ในนั้น แต่ agent ยังชอบเขียนเป็น precondition ต่อกันเป็นชั้น ๆ

## Omarchy กับแนวคิด omakase

ชื่อ [[omarchy|Omarchy]] มาจากคำว่า omakase ที่แปลว่าให้เชฟเลือกให้ เขาจึงลงโปรแกรมมาให้ครบตั้งแต่แรก และเถียงกับสาย Linux ที่ถือว่านี่คือ bloat ดู [[omakase-software|Omakase Software]]

ในคลิปเดียวกันเขาเล่าการรีดขนาด ISO จากราว 7.5 GB เหลือราว 5.85 GB ทีละ package แล้วบอกว่ารู้สึกเหมือนวิศวกร McLaren ที่โกนน้ำหนักรถทีละกรัม

## ความสนุกของคนเขียนโปรแกรม

[[i-was-replaced-by-ai-typecraft|Typecraft]] ผู้ทำวิดีโอสอน programming เล่าว่าเคยเรียนจากสื่อของ DHH และภายหลังรู้สึกสูญเสียลายมือของตัวเองเมื่องานกลายเป็นการรับ output จาก AI ส่วน DHH เล่าว่าความสนุกกลับมาเมื่อมีหลายงานให้ตัดสินใจต่อเนื่อง

สองเรื่องนี้ช่วยให้ [[creative-ownership|Creative Ownership]] เก็บได้ทั้งความหมายจากการเขียนเองและจากการกำหนดทิศให้ agent ยังตอบไม่ได้ว่าความต่างมาจากตัวงาน อิสระของคนทำ หรือจังหวะของ workflow มากกว่ากัน

## See also

- [[dhh-ai-programming-setup-lex-clips]]
- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
- [[omarchy]]
- [[make-it-simpler]]
- [[omakase-software]]
- [[lex-fridman]]
- [[skill-atrophy]]
- [[herdr]]
- [[tailscale]]
- [[creative-ownership]]
- [[attention-bottleneck]]
