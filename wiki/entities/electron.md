---
title: Electron
type: entity
tags: [desktop-apps, javascript, node, frameworks, tooling]
created: 2026-04-18
updated: 2026-04-23
sources: [opencode-tauri-to-electron.md, opencode-desktop-electron-brendonovich.md]
---

# Electron

เฟรมเวิร์กสำหรับสร้างแอปพลิเคชันเดสก์ท็อป โดยรวมเอา **Chromium** สำหรับ frontend และ **Node.js** สำหรับ main process เข้าไว้ด้วยกัน เป็นเฟรมเวิร์กที่ครองตลาดอยู่ — แอปอย่าง Slack, VS Code, Discord, Figma desktop ล้วนใช้ Electron มักถูกวิจารณ์เรื่องขนาดของ bundle และการใช้หน่วยความจำเมื่อเทียบกับ [[tauri|Tauri]]

## จุดที่ได้เปรียบ (ตาม @brendonovich, 18 เม.ย. 2026)

เมื่อ logic หลักที่หนักๆ ของแอปเป็น **JS/Node/Bun อยู่แล้ว**, main process ที่เป็น Node.js ของ Electron จะสามารถ host logic นั้น **ใน process เดียวกันได้** — ไม่ต้องมี sidecar, ไม่ต้องมี IPC hop นี่คือเหตุผลที่ [[opencode|OpenCode]] ย้ายมาจาก Tauri: server `opencode serve` ของพวกเขา (ซึ่งย้ายจาก Bun มาเป็น Node ในการย้ายครั้งเดียวกัน) สามารถรันโดยตรงภายใน main process ของ Electron ได้เลย ซึ่งช่วยลด overhead ตอนเริ่มต้นและกำจัด bug ด้านความเสถียรข้าม platform ไปได้ประเภทหนึ่ง นอกจากนี้ **Chromium** ยังให้การเรนเดอร์ frontend ที่สอดคล้องกันข้าม OS ได้ดีกว่า platform-native webview — ซึ่งเป็นประเด็นสำคัญเพราะ [[tauri|Tauri]] ใช้ **WebKit** บน macOS/Linux ซึ่งมีประสิทธิภาพการเรนเดอร์และความเท่าเทียมกันของสไตล์ที่แย่กว่าอย่างเห็นได้ชัดสำหรับ UI ที่ซับซ้อน เป็นข้อแลกเปลี่ยนที่ยอมรับอย่างชัดเจน: ขนาด bundle ที่ใหญ่ขึ้น

ดูเหตุผลฉบับเต็มจากแหล่งข้อมูลหลักได้ที่: [[opencode-desktop-electron-brendonovich]]

## ดูเพิ่ม

- [[tauri]]
- [[opencode]]
- [[opencode-desktop-electron-brendonovich]]
- [[opencode-tauri-to-electron]]
