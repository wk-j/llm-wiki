---
title: Leo Robinovitch
type: entity
tags: [developer, tui, go, terminal]
created: 2026-04-16
updated: 2026-04-23
sources: [leo-robinovitch-terminal-pager.md]
---

# Leo Robinovitch

นักพัฒนาอิสระที่เป็นที่รู้จักจากการสร้างแอปพลิเคชันและเครื่องมือ [[tui|TUI]] ด้วยภาษา Go. เขียนบล็อกที่ [theleo.zone](https://theleo.zone).

## โปรเจกต์

| โปรเจกต์ | คำอธิบาย |
|---|---|
| [viewport](https://github.com/robinovitch61/viewport) | Go component ที่ใช้ซ้ำได้: เป็น viewport สำหรับแสดงข้อความที่สามารถ scroll, search, และรองรับ ANSI/Unicode ได้ สำหรับ Bubble Tea TUIs |
| [lore](https://github.com/robinovitch61/lore/) | [[terminal-pager]] ที่สร้างขึ้นบน viewport component; เป็นโปรแกรมที่ Leo ใช้แทน `less` ในชีวิตประจำวัน |
| [kl](https://github.com/robinovitch61/kl) | TUI สำหรับดู log ของ Kubernetes: รองรับ multi-cluster, multi-namespace, search, และ JSON prettification |
| [wander](https://github.com/robinovitch61/wander/) | TUI สำหรับ HashiCorp Nomad |

viewport component เป็น core ที่ใช้ร่วมกันในแอปพลิเคชันเหล่านี้ ซึ่งถูกแยกออกมาเป็น library ที่ใช้ซ้ำได้แบบ standalone

## ดูเพิ่ม

- [[tui]]
- [[terminal-pager]]
- [[leo-robinovitch-terminal-pager]]
