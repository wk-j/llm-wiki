---
title: luai.nvim
type: entity
tags: [neovim, lua, ai, developer-tools]
created: 2026-05-23
updated: 2026-05-23
sources: [software-writing-software-gone-right.md]
---

# luai.nvim

**luai.nvim** คือ experimental [[neovim|Neovim]] plugin ของ [[tj-devries|TJ DeVries]] ที่ให้ผู้ใช้เรียก function จากคำอธิบาย แล้วให้ LLM generate Lua implementation ให้ถ้า function นั้นยังไม่มี

Repo ที่ source ให้ไว้คือ `https://github.com/tjdevries/luai.nvim/tree/master`.

## มันทำงานอย่างไร

แกนหลักคือ Lua module loading:

- ถ้า function มี implementation อยู่แล้ว ระบบ `require` แล้วคืน function นั้น
- ถ้ายังไม่มี ระบบเรียก agent ให้เขียน Lua code
- code ที่ได้ถูก save เป็น module ใน runtime path
- generated object เก็บ metadata/history และใช้ `__call` เพื่อเรียกเหมือน function

ตรงนี้ทำให้ `luai.nvim` เป็นตัวอย่างของ [[just-in-time-software|just-in-time software]]: software เกิดตอนต้องใช้ แต่ไม่หายไปหลังใช้เสร็จ

## ทำไมมันน่าสนใจ

plugin นี้เล็กกว่า coding agent เต็มตัว แต่น่าสนใจเพราะผูก AI เข้ากับ mechanic ของ editor โดยตรง. ผู้ใช้ไม่ได้ copy code จาก chat แล้ว paste เอง แต่เรียก function missing แล้วระบบจัดการ generate/cache/load ให้

ถ้า function พัง เช่น Neovim API เปลี่ยน ผู้ใช้ prompt เพิ่มได้ว่าอะไรใช้ไม่ได้ แล้วให้ระบบ improve จาก history เดิม

**ได้อะไร:** editor กลายเป็นพื้นผิวที่สร้าง tool เฉพาะตัวได้ทันที ไม่ใช่แค่ที่พิมพ์ code

## See also

- [[software-writing-software-gone-right]]
- [[tj-devries]]
- [[neovim]]
- [[just-in-time-software]]
- [[personalized-development-environment]]
- [[malleable-tools]]
