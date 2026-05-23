---
title: Personalized Development Environment
type: concept
tags: [developer-tools, productivity, ai, customization]
created: 2026-05-23
updated: 2026-05-23
sources: [software-writing-software-gone-right.md]
---

# Personalized Development Environment / สภาพแวดล้อมเขียนโค้ดแบบส่วนตัว

**Personalized Development Environment** หรือ **PDE** คือแนวคิดของ [[tj-devries|TJ DeVries]] ว่า developer environment ไม่ควรจบที่ editor หรือ IDE แต่รวมทั้งเครื่องมือ config, shell, OS, shortcuts, plugins, และ automation ที่คนคนนั้นเข้าใจและปรับเองได้

พูดง่าย ๆ: เครื่องไม่ใช่ของกลางที่ต้องทนใช้ตาม vendor ตั้งมา แต่เป็น workshop ส่วนตัวที่ค่อย ๆ ลด friction ของเจ้าของมัน

## แก่นความคิด

PDE อยู่ระหว่าง editor เปล่า ๆ กับ IDE สำเร็จรูป มันมี "assembly required" แบบ Neovim หรือ Emacs แต่ไม่ได้จำกัดเฉพาะ editor. สิ่งสำคัญคือผู้ใช้รู้ว่าระบบทำงานอย่างไร และเปลี่ยนมันได้โดยไม่ต้องเข้าเมนูซ้อนหลายชั้น

ใน [[software-writing-software-gone-right|Software Writing Software (gone right!)]], TJ ใช้ [[neovim|Neovim]] เป็นศูนย์กลาง แต่เดโมลามไปถึงธีมของ desktop, terminal, SSH, และ config ของเครื่อง Linux. จุดนี้ทำให้ PDE ใกล้กับ [[malleable-tools|malleable tools]] มากกว่า "IDE setup" ธรรมดา

**ได้อะไร:** environment กลายเป็นของที่พัฒนาได้เหมือน software ไม่ใช่แค่ preference panel

## AI ทำให้ cost ของ personalization ต่ำลง

ก่อนมี LLM การเขียน automation เล็ก ๆ มักติด cost แอบแฝง: ต้องหา API, อ่าน doc, เขียน code, debug edge case. งานอาจใช้เวลาไม่นาน แต่แรงเสียดทานพอให้คนผัดไปหลายวัน

LLM ลด cost ตรงนี้ โดยเฉพาะงานที่ขอบเขตเล็กและตรวจผลได้ทันที เช่น:

- เขียน Lua function ให้ [[neovim|Neovim]]
- เปิด floating terminal พร้อม command เฉพาะ
- เรียก plugin อย่าง Telescope เพื่อ search config
- เปลี่ยน theme หรือ background ของ desktop

ตรงนี้ไม่ใช่ [[specs-to-code|specs-to-code]] ระดับระบบใหญ่ เพราะ blast radius เล็กกว่า และ feedback loop สั้นกว่า เจ้าของเครื่องเห็นผลทันทีว่ามันทำงานไหม

**ผลคือ:** personalization ที่เคย "ไม่คุ้มทำ" เริ่มคุ้ม เพราะ cost ของการลองต่ำลง

## Dot Prompts

TJ เสนอไอเดีย `dot prompts` แบบกึ่งเล่นกึ่งจริง: แทนที่จะเก็บทุกอย่างเป็น dotfiles อาจเก็บรายการ preference หรือสิ่งที่ไม่ชอบเป็น prompt แล้วให้ agent apply กับเครื่องใหม่

ตัวอย่างไม่ใช่ "นี่คือ config ทั้งหมดของฉัน" แต่เป็น "ฉันไม่ชอบค่า default เหล่านี้ของ Omarchy ช่วยเปลี่ยนให้เป็นแบบนี้". วิธีนี้ทำให้ config เป็น intent มากขึ้น แต่ก็เสี่ยงถ้าไม่มี verification เพราะ prompt อาจ apply ต่างกันในแต่ละรอบ

**ได้อะไร:** dot prompts ชี้ว่าการตั้งค่าอาจย้ายจาก file snapshot ไปเป็น reusable intent แต่ต้องมี harness ที่ตรวจผลลัพธ์ได้

## ความต่างจาก coding harness

[[coding-harness|Coding harness]] คือชั้น software ที่ครอบ LLM แล้วให้มันใช้ tools, context, sandbox, และ feedback loop. PDE คือ environment ของมนุษย์ทั้งหมด

สองอย่างนี้ทับกันเมื่อ PDE เริ่มมี AI เป็น primitive เช่น `luai.nvim` ที่ให้ function missing → generate → cache → improve. ในจุดนั้น editor plugin เริ่มทำตัวเหมือน harness เล็ก ๆ สำหรับ personal automation

## See also

- [[software-writing-software-gone-right]]
- [[tj-devries]]
- [[luaai-nvim]]
- [[neovim]]
- [[malleable-tools]]
- [[just-in-time-software]]
- [[coding-harness]]
