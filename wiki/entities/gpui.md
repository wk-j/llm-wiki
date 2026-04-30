---
title: GPUI
type: entity
tags: [framework, rust, gpu, ui]
created: 2026-04-29
updated: 2026-04-29
sources: [zed-is-1-0.md]
---

# GPUI

**GPUI** คือ UI Framework ที่เขียนด้วยภาษา [[rust]] พัฒนาโดยทีม [[zed-industries]] เพื่อเป็นรากฐานให้กับ [[zed]] editor โดยเฉพาะ

## จุดเด่น (Key Features)

- **GPU-Accelerated**: ออกแบบมาให้ทำงานเหมือน Engine ของวิดีโอเกม โดยการส่งข้อมูล UI ไปประมวลผลบน GPU ผ่าน Shaders แทนที่จะใช้ CPU วาดภาพแบบดั้งเดิม
- **Rust-Native**: ใช้ประโยชน์จาก ownership model ของ Rust เพื่อจัดการหน่วยความจำและ concurrency อย่างมีประสิทธิภาพ
- **Low Latency**: มุ่งเน้นการตอบสนองที่เร็วที่สุด (sub-millisecond input latency)
- **Custom Built**: เป็นการสร้างใหม่ทั้งหมดโดยไม่พึ่งพา Web technology หรือ library UI ทั่วไป เพื่อให้สามารถควบคุม stack ได้ทุกระดับ (Deep Ownership)

## ความสำคัญ
การมี Framework ของตัวเองทำให้ Zed สามารถทำสิ่งที่ Editor ที่ใช้ Electron (เช่น [[vscode]]) ทำไม่ได้ เช่น การเรนเดอร์ข้อความและ UI ที่ซับซ้อนด้วยความเร็วสูงมาก และการสร้างระบบ AI interaction ที่ฝังลึกอยู่ในระดับ primitive ของ UI

## ดูเพิ่ม
- [[zed]] — Application หลักที่ใช้ GPUI
- [[rust]] — ภาษาที่ใช้พัฒนา
