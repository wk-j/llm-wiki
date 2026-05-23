---
title: TJ DeVries
type: entity
tags: [developer-tools, neovim, lua, ai]
created: 2026-05-23
updated: 2026-05-23
sources: [software-writing-software-gone-right.md]
---

# TJ DeVries

**TJ DeVries** เป็น developer ใน ecosystem ของ [[neovim|Neovim]] และผู้ทำคอนเทนต์สาย editor/tooling. ใน source นี้เขาพูดเรื่อง [[personalized-development-environment|personalized development environment]] และโชว์ [[luaai-nvim|luai.nvim]] เป็นตัวอย่าง software ที่ AI เขียน software ชิ้นเล็ก ๆ ให้ในจังหวะที่ต้องใช้

## มุมที่สำคัญใน wiki นี้

TJ ไม่ได้วาง AI เป็นคนเขียนโปรเจกต์แทนทั้งหมด แต่ใช้ AI เป็นตัวลด friction ใน environment ส่วนตัว. ถ้า function เล็ก ๆ ไม่มีอยู่ ระบบ generate ให้ แล้ว cache ไว้เป็น Lua module

ตรงนี้เชื่อมกับ [[malleable-tools|malleable tools]] เพราะเครื่องมือไม่แข็งตัวตาม vendor. ผู้ใช้สามารถสร้าง command เฉพาะตัวจากภาษาธรรมดา แล้วปรับต่อได้จาก error หรือ preference ของตัวเอง

## See also

- [[software-writing-software-gone-right]]
- [[luaai-nvim]]
- [[neovim]]
- [[personalized-development-environment]]
- [[just-in-time-software]]
