---
title: Terminal Pager
type: concept
tags: [terminal, tui, text-navigation, tools]
created: 2026-04-16
updated: 2026-04-23
sources: [leo-robinovitch-terminal-pager.md]
---

# Terminal Pager

โปรแกรมสำหรับดูข้อความหลายหน้าใน terminal แบบ interactive ใช้เมื่อ output ยาวเกินกว่าจะอ่านได้ในครั้งเดียว: git diffs, man pages, logs, ผลลัพธ์จากฐานข้อมูล, output ของเครื่องมือ AI

## โปรแกรมเรียกใช้ pager อย่างไร

โปรแกรมจะตรวจสอบ environment variable `$PAGER` หากมีการตั้งค่าไว้และ stdout เป็น TTY (interactive session), โปรแกรมจะสร้าง pager เป็น child process และ pipe output ของตัวเองไปยัง stdin ของ pager หาก stdout ไม่ใช่ TTY (เช่น `git diff | grep ...`), pager จะถูกข้ามไป

มีการ override เฉพาะทางด้วย: `$GIT_PAGER` สำหรับ git, `$BAT_PAGER` สำหรับ pager ภายในของ bat, ฯลฯ

## Pager ทั่วไป

| Pager | หมายเหตุ |
|---|---|
| `less` | เป็น default fallback ในระบบส่วนใหญ่; ตั้งค่าได้สูง; output จะหายไปเมื่อออกเป็นค่าเริ่มต้น (ใช้ `-X` เพื่อให้คงอยู่) |
| `bat` | มี syntax highlighting + line numbers; เรียกใช้ pager อื่นภายใน |
| `most` | มีหลายหน้าต่าง, splits |
| `delta` | เชี่ยวชาญสำหรับ git diffs; side-by-side, syntax highlighting |
| `lore` | pager ที่เขียนด้วย Go ของ [[leo-robinovitch|Leo Robinovitch]], สร้างขึ้นบน `viewport` component ของเขา |
| `cat` | ตั้งค่า `PAGER=cat` เพื่อปิดการใช้งาน paging ทั้งหมด |

## option ของ `less` ที่มีประโยชน์

- `-X` / `--no-init` — คง output ไว้ใน terminal หลังจากออก
- `-i` / `--ignore-case` — ค้นหาแบบไม่สนใจ case-sensitive
- `-R` — ส่งผ่าน ANSI escape codes (สำหรับ output ที่มีสี)

## Pagers vs TUIs

Pager โดยทั่วไปจะแสดงข้อความ stream เดียวใน alt screen (หรือ inline) ส่วน [[tui|TUIs]] จะประกอบด้วย component ที่คล้าย pager หลายตัวควบคู่ไปกับองค์ประกอบ UI อื่นๆ `viewport` component ของ Leo Robinovitch เป็น mini-pager ที่ใช้ซ้ำได้ซึ่งมีไว้สำหรับฝังใน TUI

## ดูเพิ่ม

- [[tui]]
- [[leo-robinovitch-terminal-pager]]
- [[leo-robinovitch]]
