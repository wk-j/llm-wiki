---
title: JavaScriptCore
type: entity
tags: [javascript, runtime, engine, apple]
created: 2026-07-09
updated: 2026-07-09
sources: [bun-in-rust.md]
---

# JavaScriptCore

**JavaScriptCore** คือ JavaScript engine ที่ใช้ใน Safari ของ [[apple|Apple]]. [[bun|Bun]] embed JavaScriptCore เป็น engine หลัก และนี่ทำให้ memory-lifetime ของ Bun ยากขึ้น เพราะ runtime ต้องจัดการทั้งค่า JavaScript ที่ garbage-collected และ resource native ที่ต้อง free เอง.

ใน [[bun-in-rust|Bun in Rust]] JavaScriptCore เป็นหนึ่งในเหตุผลที่ Bun ยังมี `unsafe` แม้ย้ายไป [[rust|Rust]]. Rust ช่วยบังคับ ownership ได้มากขึ้น แต่การเรียกข้าม C/C++ boundary ยังต้องใช้ pointer และ contract จาก library ภายนอก.

## See also

- [[bun]]
- [[bun-in-rust]]
- [[rust]]
