---
title: Just-in-Time Software
type: concept
tags: [ai, software-engineering, developer-tools, automation]
created: 2026-05-23
updated: 2026-05-23
sources: [software-writing-software-gone-right.md]
---

# Just-in-Time Software / ซอฟต์แวร์ที่เกิดตอนต้องใช้

**Just-in-time software** คือการสร้าง software ชิ้นเล็ก ๆ ตอนที่ต้องใช้จริง แล้วเก็บไว้ถ้ามันมีประโยชน์ เสนอใน talk ของ [[tj-devries|TJ DeVries]] ผ่านเดโม [[luaai-nvim|luai.nvim]]

ต่างจาก agentic coding ที่ให้ AI ทำ feature ใหญ่ ๆ แนวคิดนี้เล็กกว่า: เราอยากได้ function หรือ command หนึ่งตัว พิมพ์คำอธิบายสั้น ๆ แล้วให้ LLM เขียน implementation ให้ตรงนั้น

## Pattern

รูปแบบพื้นฐานมีสี่ขั้น:

1. ผู้ใช้เรียกชื่อ function หรือคำอธิบายของสิ่งที่อยากได้
2. ระบบตรวจว่า implementation มีอยู่แล้วไหม
3. ถ้าไม่มี ระบบเรียก LLM ให้ generate code แล้ว save เป็น module
4. รอบต่อไปโหลด code ที่ cache ไว้โดยไม่ต้องเรียก LLM

ใน `luai.nvim`, ขั้นที่ 2 ใช้ Lua `require` และ Neovim `runtimepath`. ขั้นที่ 3 ใช้ agent เขียน Lua code. ขั้นที่ 4 ทำให้ function กลายเป็นส่วนหนึ่งของ environment จริง ไม่ใช่คำตอบชั่วคราวใน chat

**ได้อะไร:** AI กลายเป็น lazy compiler ของ intent ขนาดเล็ก

## ตัวอย่างจากเดโม

ตัวอย่างที่เล็กที่สุดคือ `print all odd values in the table`. มันไม่ใช่งานยาก แต่เป็นงานที่ไม่จำเป็นต้องให้มนุษย์เสียสมาธิ

ตัวอย่างที่มีค่ากว่า คือ command ที่ผูกกับ environment ส่วนตัว:

- ลบ whitespace ซ้ำใน string
- สร้าง floating window ใน [[neovim|Neovim]]
- search Neovim config ด้วย Telescope
- เปลี่ยน theme ของ desktop
- เปิด floating terminal แล้ว SSH ไป `terminal.shop`

ของพวกนี้ไม่จำเป็นต้องเป็น product. มันมีค่าถ้าแก้ papercut ของคนใช้จริงใน [[personalized-development-environment|personalized development environment]] ของเขา

## สำคัญตรง cache และ improve

ถ้า generate ทุกครั้ง แนวคิดนี้จะช้าและไม่น่าเชื่อถือ แต่ TJ ทำให้ code ถูก save เป็น module. เมื่อใช้ซ้ำ ระบบโหลด code เหมือน function ปกติ

อีกส่วนที่สำคัญคือ metadata. Generated function เก็บ prompt history และ response เล็ก ๆ ไว้ด้วย เมื่อ function พังเพราะ API เปลี่ยน เช่น `win highlight` deprecated ผู้ใช้สั่งเพิ่มสั้น ๆ ว่าอย่าใช้ key นี้ แล้วให้ระบบแก้จาก context เดิม

**ผลคือ:** just-in-time software ไม่ใช่ของใช้แล้วทิ้งเสมอไป มันเป็น scratch implementation ที่ค่อย ๆ แข็งแรงขึ้นได้

## ขอบเขตที่ควรใช้

แนวคิดนี้เหมาะกับงานที่:

- ขอบเขตเล็ก
- ตรวจผลได้ทันที
- พังแล้วไม่กระทบระบบใหญ่
- ผูกกับ preference ส่วนตัว
- คุ้มค่าถ้าใช้ซ้ำมากกว่าหนึ่งครั้ง

มันไม่เหมาะกับ core business logic ที่ต้องมี design, test, review, และ ownership ชัดเจน ตรงนั้นยังต้องใช้ [[agentic-engineering|agentic engineering]] หรือ [[harness-engineering|harness engineering]] ที่หนักกว่า

## ความต่างจาก Just-in-Time Context

[[just-in-time-context|Just-in-Time Context]] คือการส่ง context ให้ agent ตอนจำเป็น เพื่อลด token และ attention load.

Just-in-time software คือการสร้าง code ตอนจำเป็น เพื่อลด friction ใน environment ของมนุษย์.

สองอย่างคล้ายกันตรงที่ไม่ front-load ทุกอย่าง แต่สิ่งที่ lazy-load คนละชนิด: อันหนึ่ง lazy-load context, อีกอัน lazy-generate capability

## See also

- [[software-writing-software-gone-right]]
- [[luaai-nvim]]
- [[personalized-development-environment]]
- [[malleable-tools]]
- [[coding-harness]]
- [[just-in-time-context]]
