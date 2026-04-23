---
title: Neovim
type: entity
tags: [editors, vim, neovim, tooling]
created: 2026-04-17
updated: 2026-04-23
sources: [vim-pack-guide.md]
---

# Neovim

Neovim เป็น fork ของ Vim ที่สามารถขยายความสามารถได้อย่างยิ่งยวด (hyperextensible) และฝัง Lua ไว้ในตัว เดิมที fork มาในปี 2014 เพื่อ refactor codebase ที่เป็นภาษา C ของ Vim และเพิ่ม scripting runtime เข้าไป สำหรับผู้ใช้ส่วนใหญ่ที่ต้องการ async, การตั้งค่าด้วย Lua, LSP และ tree-sitter ในตัว Neovim ถือเป็น Vim ยุคใหม่โดยพฤตินัย

## สิ่งที่แตกต่างจาก Vim

- **Embedded Lua runtime** — `init.lua` เข้ามาแทนที่ `.vimrc` เป็นไฟล์ config ที่เป็นที่ยอมรับ
- **Built-in LSP client** — `vim.lsp` มาพร้อมกับ core; ตั้งค่า server ผ่าน `vim.lsp.enable()` และ `nvim-lspconfig`
- **Built-in [[tree-sitter]]** — parsers, highlights, text objects
- **`vim.loader`** — bytecode cache; `vim.loader.enable()` ช่วยให้ startup เร็วขึ้น 20-30%
- **`runtimepath` conventions** — layout แบบ `lua/`, `plugin/`, `ftplugin/`, `after/` สำหรับการค้นหา module

## ระบบนิเวศของ Plugin

Plugins คือ Git repository ที่จัดวางอยู่ภายใต้ `pack/<package>/{start,opt}/<plugin>/` ในอดีตถูกจัดการโดยเครื่องมือ third-party (pathogen → vim-plug → packer.nvim → lazy.nvim) ตั้งแต่ Neovim 0.12 เป็นต้นมา, module [[vim-pack]] ที่มาพร้อมกับโปรแกรมได้ให้ความสามารถในการ install/load/update มาในตัว

## เวอร์ชัน 0.12

มาพร้อมกับ [[vim-pack]] เป็นส่วนหนึ่งของ core นี่เป็น release แรกที่มี [[plugin-manager]] ที่มีความสามารถมาในตัว Neovim เอง — เวอร์ชันก่อนหน้ามี `:packadd` และมาตรฐานของ package แต่ไม่มี UX สำหรับ install/update

## ตำแหน่งเมื่อเทียบกับ editor อื่นๆ

- **Vim** — สำหรับการใช้งานจริงส่วนใหญ่ Neovim ถือเป็น superset ของ Vim; Vim 9 ได้เพิ่ม Vim9script เข้ามาเพื่อตอบโต้ ทำให้สายเลือดของ Vim ยังคงอยู่
- **[[helix]]** — modal editor ยุค post-modern ที่ไม่มีระบบ plugin เลย; มาพร้อม LSP/tree-sitter ในตัว เป็นขั้วตรงข้ามทางปรัชญากับจุดยืนของ Neovim ที่ "ขยายความสามารถได้เป็นค่าเริ่มต้น"
- **VS Code / Zed** — GUI editor ที่มีโมเดล extension แตกต่างกัน (Node.js/WASM); Neovim มักถูกฝังเข้าไปข้างในเพื่อใช้เป็น modal layer

## ดูเพิ่ม

- [[vim-pack]]
- [[plugin-manager]]
- [[evgeni-chasnovski]]
- [[helix]]
- [[tree-sitter]]
