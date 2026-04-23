---
title: Plugin Manager
type: concept
tags: [tooling, editors, package-management]
created: 2026-04-17
updated: 2026-04-23
sources: [vim-pack-guide.md]
---

# Plugin Manager / ตัวจัดการ Plugin

Plugin manager ทำหน้าที่ติดตั้ง, โหลด, อัปเดต, และลบ extension ที่ผู้ใช้สร้างขึ้นสำหรับโปรแกรม host — โดยทั่วไปคือ text editor ในโลกของ Vim/Neovim, มันยังตัดสินใจด้วยว่า plugin จะโหลด *เมื่อไหร่* (ตอนเริ่มต้น หรือแบบ lazy) และจัดการ lockfile เพื่อให้สามารถทำซ้ำสภาพแวดล้อมได้

## ความรับผิดชอบหลัก

1.  **Fetch** — clone repository (โดยปกติคือ Git) มาไว้ในตำแหน่งที่รู้จัก
2.  **Load** — ทำให้ plugin ปรากฏบน `runtimepath` เพื่อให้ editor สามารถหาไฟล์ `plugin/`, `lua/`, `ftplugin/` ของมันเจอ
3.  **Update** — fetch commit ใหม่ๆ, แสดง diff, และให้ผู้ใช้ยอมรับหรือปฏิเสธ
4.  **Pin** — บันทึกเวอร์ชันที่ติดตั้ง (lockfile) เพื่อให้เครื่องใหม่สามารถสร้างสภาพแวดล้อมที่เหมือนกันทุกประการได้
5.  **Hook** — รันโค้ดของผู้ใช้ก่อน/หลังการ install/update/delete (เช่น `TSUpdate` หลังจากติดตั้ง `nvim-treesitter`)

Manager ขั้นสูงจะเพิ่ม:
- **Lazy loading** — เลื่อนการโหลด plugin ออกไปจนกว่าจะมี event, command, filetype, หรือการกดปุ่มเกิดขึ้น
- **Dependency resolution** — รับประกันว่า plugin A จะโหลดก่อน plugin B หาก B ต้องการ A
- **Declarative specs** — DSL สำหรับ lazy trigger และการตั้งค่าใน table เดียว

## ภูมิทัศน์ของ Neovim

| Manager | สไตล์ | หมายเหตุ |
|---|---|---|
| [[vim-pack]] | Minimal, built-in (Neovim 0.12+) | มีสามฟังก์ชัน, lockfile, hook ที่ใช้ autocmd. ไม่มี declarative lazy DSL |
| lazy.nvim | Rich declarative | เป็น third-party ที่โดดเด่น `cmd`/`event`/`ft`/`keys` lazy triggers, `opts`, `dependencies` |
| mini.deps | Minimal, Lua | ต้นแบบของ [[vim-pack]] โดย [[evgeni-chasnovski\|Chasnovski]] |
| packer.nvim | Legacy | Archived ในปี 2023; ผู้ใช้ย้ายไป lazy.nvim หรือ vim.pack |
| pathogen / vim-plug | ยุคก่อน Lua | Vimscript; ยังคงใช้กันอย่างแพร่หลายใน Vim ธรรมดา |

## ข้อแลกเปลี่ยนหลัก

Plugin manager มีสเปกตรัมตั้งแต่ **โปร่งใสเชิงกลไก** (คุณเขียน Lua ที่โหลด plugin แบบ imperative) ไปจนถึง **สะดวกแบบ declarative** (คุณเขียน spec table แล้ว manager จะคิดเองว่าเมื่อไหร่และอย่างไร)

- **ข้อดีของ Transparent:** config คือ source of truth, ลำดับของ hook ชัดเจน, ไม่มี magic
- **ข้อดีของ Declarative:** startup speed ผ่าน lazy loading ที่จริงจัง, boilerplate น้อยลง, รูปแบบที่สอดคล้องกัน

[[vim-pack]] อยู่ฝั่ง transparent โดยการออกแบบ. `lazy.nvim` อยู่ฝั่ง declarative. ทั้งสองแบบต่างก็มีเหตุผลที่ดี.

## Lockfiles

Lockfile บันทึก commit ที่แน่นอนของแต่ละ plugin ที่ติดตั้งไว้ มัน:
- ช่วยให้เครื่องใหม่สามารถสร้างสภาพแวดล้อมปัจจุบันซ้ำได้
- ทำให้สามารถทำ workflow "revert latest update" ได้
- ควรถูกเช็คอินเข้า version control
- ไม่ควรแก้ไขด้วยมือเด็ดขาด

[[vim-pack]] เขียน `nvim-pack-lock.json`; lazy.nvim เขียน `lazy-lock.json`.

## ดูเพิ่ม

- [[vim-pack]]
- [[neovim]]
- [[helix]] — ทางเลือก: a batteries-included editor that ships features as built-ins rather than plugins
