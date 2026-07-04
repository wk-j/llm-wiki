---
title: Mario Zechner
type: entity
tags: [developer, open-source, gamedev, pi]
created: 2026-04-28
updated: 2026-07-04
sources: [mario-zechner-pi-agent.md, building-pi-world-of-slop.md, code-isnt-free-mario-zechner-hard-truths-coding-ai.md]
---

# Mario Zechner / มาริโอ เซคเนอร์

**Mario Zechner** เป็นวิศวกรซอฟต์แวร์และนักพัฒนา Open Source มายาวนานกว่า 17 ปี เขาเป็นที่รู้จักในฐานะผู้สร้าง **libGDX** (Java game development framework) และล่าสุดคือผู้พัฒนา [[pi-agent|pi]] ซึ่งเป็น coding agent ใน terminal

## แนวคิดและจุดยืน

- **Minimalist & Pragmatic**: มาริโอเน้นการสร้างเครื่องมือที่เรียบง่ายแต่ทรงพลัง เขาคัดค้าน "Feature Bloat" และการซ่อนกลไกการทำงานไว้หลังฉาก (Hidden injection)
- **Extensibility First**: เขาเชื่อว่า Developer แต่ละคนมี workflow ต่างกัน เครื่องมือที่ดีจึงควรเป็น "Scaffolding" ที่ผู้ใช้ขยายความสามารถเองได้ง่าย
- **OSS Defense**: เขาเป็นผู้เสนอวิธีรับมือกับ AI spam ในโปรเจกต์ Open Source โดยใช้ระบบ Human Verification ([[vouch-oss]])
- **Slow Down Discipline**: ใน talk [[building-pi-world-of-slop|Building pi in a World of Slop]] เขาเตือนว่าการปล่อย agent เขียน code เร็วกว่าที่มนุษย์จะอ่านทัน ทำให้ความซับซ้อนสะสมแบบ compound error งาน critical จึงยังต้องอ่าน code และตัดสินใจเอง
- **Code isn't free**: ในบทสัมภาษณ์ [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]] เขาแยก "implementation ถูกลง" ออกจาก "โค้ดไม่มีต้นทุน". ถ้าไม่มีใครเข้าใจและ maintain ได้ โค้ดที่ agent สร้างเร็ว ๆ แค่เลื่อนโทษไปข้างหน้า
- **Agent เป็นคู่คิด ไม่ใช่กองทัพเสมอไป**: Mario ใช้ agent ทำ analysis, เสนอทางเลือก, เขียนตัวอย่าง, และ implement หลังมี guardrail ชัด แต่เขาไม่ชอบ workflow แบบเปิด agent จำนวนมากจนตัวเองหลุดจากการคิดปัญหา

## ผลงานสำคัญ

- **libGDX**: เฟรมเวิร์กสร้างเกมที่ได้รับความนิยมสูงในวงการ Java
- **pi (pi.dev)**: Coding agent ที่เน้นความ malleability และความเร็วในการทำงาน
- **Earendil**: ทีม/บริษัทที่เขาเข้าร่วมเพื่อทำ [[pi-agent|pi]] และทดลอง application layer / local inference ต่อ

## ดูเพิ่ม

- [[pi-agent]]
- [[clanker-slop]]
- [[code-isnt-free-mario-zechner-hard-truths-coding-ai]]
- [[earendil]]
