---
title: TUI (Terminal User Interface)
type: concept
tags: [terminal, tui, ui, software-engineering]
created: 2026-04-16
updated: 2026-04-23
sources: [leo-robinovitch-terminal-pager.md]
---

# TUI (Terminal User Interface) / ส่วนติดต่อผู้ใช้บนเทอร์มินัล

แอปพลิเคชันบน Terminal ที่ทำงานเหมือนแอปพลิเคชันกราฟิกแบบ interactive แต่รันทั้งหมดภายใน terminal TUI ใช้ **alt screen** เพื่อยึดครองการแสดงผลของ terminal ทั้งหมดชั่วคราวและนำเสนอส่วนประกอบต่างๆ: title bars, sidebars, text viewports, lists, input fields

## ลักษณะเด่น

| | Pager / CLI | TUI |
|---|---|---|
| **Screen** | Inline (scrollback) | Alt screen (ยึดทั้งหน้าจอ) |
| **Components** | Text stream เดียว | ส่วนประกอบหลายชิ้นประกอบกัน |
| **Input** | น้อย | การนำทางด้วยคีย์บอร์ดที่หลากหลาย |
| **Smallest unit** | Character / line | Terminal grid cell |

ข้อจำกัดของ grid-cell บังคับให้ TUI ต้องเรียบง่ายและเป็นลำดับชั้น แต่ละหน้าจอจะแสดงเฉพาะสิ่งที่จำเป็น พร้อมด้วย keyboard shortcut เพื่อเจาะลึกหรือเปลี่ยนมุมมอง — แทนที่จะเป็นหน้าเดียวที่เลื่อนได้ยาวๆ

## ส่วนประกอบทั่วไป

- **Viewport** — พื้นที่ข้อความที่เลื่อนและค้นหาได้ (ส่วนประกอบพื้นฐานที่สุดของ TUI)
- **List/picker** — ชุดรายการที่เลือกได้
- **Input field** — การป้อนข้อความ
- **Status bar / help line** — คำใบ้ปุ่มตามบริบท

## Frameworks

- **[Bubble Tea](https://github.com/charmbracelet/bubbletea)** (Go) — สถาปัตยกรรมแบบ model-update-view ที่ได้รับแรงบันดาลใจจาก Elm; [[leo-robinovitch]] ใช้สำหรับ lore, kl, wander
- **Ratatui** (Rust) — ใช้กันอย่างแพร่หลายใน ecosystem ของ Rust; [[helix]] ใช้ในเชิงแนวคิด (Helix มี rendering layer ของตัวเอง)

## ตัวอย่างใน wiki นี้

- [[helix]] — modal text editor, เขียนด้วย Rust
- [[leo-robinovitch-terminal-pager|lore, kl, wander]] — TUI ที่เขียนด้วย Go ของ Leo Robinovitch

## ดูเพิ่ม

- [[terminal-pager]]
- [[helix]]
- [[leo-robinovitch]]
