---
title: Tauri
type: entity
tags: [desktop-apps, rust, frameworks, tooling]
created: 2026-04-18
updated: 2026-04-23
sources: [opencode-tauri-to-electron.md, opencode-desktop-electron-brendonovich.md]
---

# Tauri

เฟรมเวิร์กสำหรับสร้างแอปพลิเคชันเดสก์ท็อปที่ใช้ Rust เป็นหลัก ใช้ **native webview** ของ OS (WebKit บน macOS, WebView2 บน Windows, webkitgtk บน Linux) สำหรับ frontend และใช้ Rust สำหรับ main process วางตำแหน่งตัวเองเป็นคู่แข่งกับ [[electron|Electron]] โดยชูจุดเด่นเรื่องขนาด bundle, การใช้หน่วยความจำ, และโมเดลความปลอดภัย

## จุดแข็ง (ตาม @brendonovich, 18 เม.ย. 2026)

- ขนาด bundle เล็ก (ไม่มี Chromium มาด้วย)
- ใช้ Native webviews
- โมเดลความปลอดภัยที่แข็งแกร่ง
- รวดเร็วในกรณีการใช้งานทั่วไป

## กรณีที่ไม่เหมาะสม

เมื่อ logic หลักที่หนักๆ ของแอปทำงานบน **runtime ที่ไม่ใช่ Rust** (เช่น Node, Bun, Python), Tauri จะบังคับให้ runtime นั้นต้องทำงานเป็น **sidecar process** — ทำให้มีต้นทุนตอนเริ่มต้นเพิ่มขึ้น, มี IPC latency, และปัญหาความเสถียรข้าม platform [[opencode|OpenCode]] เจอปัญหานี้และได้ย้ายไปใช้ Electron; ดูเหตุผลจากแหล่งข้อมูลหลักได้ที่ [[opencode-desktop-electron-brendonovich]] (และสรุปก่อนหน้าที่ [[opencode-tauri-to-electron]])

## ข้อควรระวังเกี่ยวกับ WebKit (macOS + Linux)

Tauri ใช้ **native webview ของ OS** — ซึ่งคือ **WebView2** ที่เทียบเท่า Chromium บน Windows, แต่เป็น **WebKit** บน macOS และ webkitgtk บน Linux สำหรับ UI ที่ซับซ้อน, WebKit มีประสิทธิภาพการเรนเดอร์ที่แย่กว่า Chromium อย่างเห็นได้ชัด และมีความไม่สอดคล้องของสไตล์เล็กๆ น้อยๆ ทำให้การทำให้หน้าตาเหมือนกันทุก platform เป็นเรื่องยาก ขณะนี้กำลังมีการพัฒนา **CEF (Chromium Embedded Framework)** backend เพื่อเปลี่ยน webview ไปเป็น Chromium แต่ยังไม่แน่ชัดว่าจะเสถียรเมื่อไหร่ (ตาม @brendonovich, มี.ค. 2026)

## จุดที่เหมาะสมที่สุด: Core ที่เป็น Rust หนักๆ

Tauri เป็น *"อะไรที่มากกว่าไลบรารี Rust สำหรับเปิดและสื่อสารกับ webview เพียงเล็กน้อย"* (@brendonovich) คุณจะเห็นข้อได้เปรียบด้านประสิทธิภาพของมันก็ต่อเมื่องานหนักๆ ของแอปถูกเขียน **ด้วย Rust** — @brendonovich อ้างถึง [[@cap]] ที่ทำการเข้ารหัสและเรนเดอร์วิดีโอแบบ native ใน Rust ว่าเป็นกรณีการใช้งานที่เหมาะสมที่สุด ถ้างานหนักๆ เป็น JS/Python/อื่นๆ, shell ที่เป็น Rust ก็ไม่สามารถช่วยอะไรได้มาก

## ดูเพิ่ม

- [[electron]]
- [[opencode]]
- [[opencode-tauri-to-electron]]
