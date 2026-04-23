---
title: Helix
type: entity
tags: [text-editors, modal-editing, rust, lsp, tree-sitter]
created: 2026-04-14
updated: 2026-04-23
sources: [Helix - Release 25.07 Highlights.md]
---

# Helix

Modal text editor ยุค post-modern ที่เขียนด้วยภาษา Rust มีฟีเจอร์ในตัวสำหรับ multiple selections, [[tree-sitter]], Language Server Protocol (LSP), และ Debug Adapter Protocol (DAP) ที่ยังเป็นรุ่นทดลอง

## การตัดสินใจเชิงออกแบบที่สำคัญ

- **ไม่มีระบบ plugin** — ฟีเจอร์ต่างๆ จะถูกสร้างขึ้นมาในตัว แทนที่จะต้องพึ่งพา plugin (ตรงข้ามกับ [[neovim|Neovim]]/Vim และ [[plugin-manager|plugin managers]] อย่าง [[vim-pack]])
- **Multiple selections** เป็น primitive หลักในการแก้ไข (ได้แรงบันดาลใจจาก [[kakoune]])
- **Tree-sitter native** — syntax highlighting, การจัดย่อหน้า, textobjects ทั้งหมดขับเคลื่อนด้วย query ของ [[tree-sitter]]
- **LSP native** — code actions, completions, diagnostics, document colors ทั้งหมดมีมาให้ในตัว
- **Pickers** — UI component ที่คล้าย telescope ถูกนำมาใช้ทั่วทั้งโปรแกรม (file picker, file explorer, symbol picker, ฯลฯ)

## การผนวกรวม Tree-sitter

การผนวกรวม tree-sitter ของ Helix ได้ผ่านการพัฒนามาหลายขั้นตอน:

1.  **ดั้งเดิม**: ใช้ Rust crates `tree-sitter` และ `tree-sitter-highlight` อย่างเป็นทางการ
2.  **Forked highlighter**: Custom fork ที่แยก parsed trees ออกจาก queries โดยได้รับแรงบันดาลใจจาก Atom editor
3.  **[[tree-house]]** (25.07): เขียนขึ้นมาใหม่ทั้งหมดเป็น crate แยกต่างหาก พร้อมด้วย injection tree ที่เหมาะสม, incremental re-parsing, และแก้ปัญหา locals scoping

## ลิงก์

- [GitHub](https://github.com/helix-editor/helix/)
- [Matrix community](https://matrix.to/#/#helix-community:matrix.org)
- [Website](https://helix-editor.com)

## ดูเพิ่ม

- [[tui]]
- [[tree-sitter]]
- [[tree-house]]
- [[helix-release-25-07]]
- [[neovim]] — modal editor ที่เน้นการขยายความสามารถผ่าน plugin ซึ่งตรงข้ามกัน
