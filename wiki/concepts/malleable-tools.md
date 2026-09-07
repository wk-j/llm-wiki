---
title: Malleable Tools
type: concept
tags: [ux, development, flexibility, philosophy]
created: 2026-04-28
updated: 2026-09-07
sources: [dhh-strategies-programming-with-ai-agents-lex-clips.md, mario-zechner-pi-agent.md, building-pi-world-of-slop.md, software-writing-software-gone-right.md]
---

# Malleable Tools / เครื่องมือที่ดัดแปลงได้

**Malleable Tools** คือแนวคิดในการสร้างซอฟต์แวร์หรือเครื่องมือที่ไม่ได้มีสถานะ "คงที่" (Rigid) แต่เปิดโอกาสให้ผู้ใช้สามารถแก้ไขโครงสร้างภายใน วิธีการทำงาน หรือหน้าตาของมันได้โดยตรงและรวดเร็วในขณะที่ใช้งานอยู่

## ในบริบทของ AI Agent

[[mario-zechner]] เสนอว่าในยุค AI ที่เรายังไม่รู้ว่า "workflow ที่ดีที่สุด" คืออะไร เครื่องมือไม่ควรจะตีกรอบให้เรา แต่ควรจะ:
- **Expose Internals**: เปิดให้เห็นว่า system prompt และกลไกของ tool ทำงานอย่างไร
- **Hot-reloading**: แก้ไขการทำงานของเครื่องมือ (เช่น สั่งให้ bash tool ทำงานผ่าน SSH) แล้วเห็นผลทันที
- **User-defined Primitives**: ให้ผู้ใช้สร้าง "เครื่องมือพื้นฐาน" ชุดใหม่ขึ้นมาได้เองตามความถัดของโปรเจกต์
- **Self-modification by Agent**: ให้ agent อ่าน documentation/examples ของ harness แล้วเขียน extension ให้ตัวเอง เช่น custom tool, slash command, event listener, provider, compaction, หรือ UI

## Payoff / ผลคือ
ช่วยให้ Developer สามารถสร้าง workflow ส่วนตัวที่ทรงพลังกว่าเครื่องมือสำเร็จรูปทั่วไป และลดการพึ่งพิง vendor ที่อาจเปลี่ยนพฤติกรรมของ AI ภายหลัง ([[alignment-bottleneck]])

ในมุมของ [[mario-zechner|Mario Zechner]], ความ malleable ไม่ใช่ของเล่น มันคือทางรอดในช่วงที่วงการยังไม่รู้ว่า coding agent form ที่ดีที่สุดคืออะไร ถ้า core ใหญ่เกินไป ผู้ใช้ต้องรอ vendor ตัดสินใจแทน ถ้า core เล็กแต่ extension แรง ผู้ใช้ลอง workflow ใหม่ได้เอง

## ตัวอย่างขนาดเล็ก: luai.nvim

[[tj-devries|TJ DeVries]] โชว์อีกมุมหนึ่งใน [[software-writing-software-gone-right|Software Writing Software (gone right!)]]. แทนที่จะสร้าง coding agent ทั้งตัว เขาทำ [[luaai-nvim|luai.nvim]] ให้ [[neovim|Neovim]] generate Lua function เมื่อเรียก function ที่ยังไม่มี แล้ว cache implementation ไว้ใช้ครั้งต่อไป

ตรงนี้คือ malleable tool แบบ micro. ผู้ใช้ไม่ได้รอ plugin author เพิ่ม feature ให้ แต่บอก environment ว่า "อยากได้ command แบบนี้" แล้วให้ AI เขียน glue code เฉพาะตัว เช่น floating window, search config, หรือ switch desktop theme

**ได้อะไร:** malleability ไม่จำเป็นต้องเริ่มจากระบบใหญ่เสมอไป แค่ function เล็ก ๆ ที่ generate/cache/improve ได้ ก็ลด friction รายวันได้แล้ว

## ระดับระบบปฏิบัติการ: ภาพที่ DHH อยากเห็น

[[dhh|DHH]] ขยายแนวคิดนี้ขึ้นไปอีกชั้นใน [[dhh-strategies-programming-with-ai-agents-lex-clips|บทสัมภาษณ์กับ Lex Fridman]] เขาบอกว่า [[omarchy|Omarchy]] รุ่นที่สี่ดีในฐานะ **malleable operating system** เพราะเพิ่มความสามารถได้ด้วยการคุยกับ agent ไม่ใช่รอ upstream ปล่อย feature

ขั้นต่อไปที่เขาอยากเห็นคือรวมเสียงเข้ามาทั้ง input และ output คือพูดว่าอยากได้ panel ดูราคาหุ้น ขอ Apple กับ Dell แล้ว agent ไปทำมาให้ หน้าตาของเครื่องเปลี่ยนตามที่สั่ง เขาเทียบกับภาพ Jarvis ใน Iron Man และกับ AI สาย live gaming model ที่สร้างเฟรมถัดไปขึ้นมาสด ๆ แล้วเล่นได้จริง ([[world-models]])

**ได้อะไร:** malleability ไต่จาก function เดียว ([[luaai-nvim|luai.nvim]]) ขึ้นไปถึง harness แล้วไปถึงทั้งเครื่อง ข้อควรระวังคือคลิปไม่ได้พูดถึง permission, ความปลอดภัย, การย้อนกลับเมื่อ agent แก้เครื่องพลาด หรือความคงเส้นคงวาของ UI ที่เปลี่ยนได้ทุกวัน ซึ่งเป็นคำถามที่ยิ่งใหญ่ขึ้นตามขอบเขตที่ยอมให้ agent แก้

## ดูเพิ่ม

- [[pi-agent]]
- [[harness-engineering]]
- [[luaai-nvim]]
- [[just-in-time-software]]
- [[omarchy]]
- [[omakase-software]]
- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
