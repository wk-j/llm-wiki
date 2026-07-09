---
title: Rust
type: entity
tags: [programming-language, systems, memory-safety]
created: 2026-07-09
updated: 2026-07-09
sources: [bun-in-rust.md]
---

# Rust

**Rust** คือภาษา programming สำหรับ systems software ที่เน้น memory safety ผ่าน ownership, borrow checker และ RAII-style cleanup อย่าง `Drop`. ใน [[bun-in-rust|Bun in Rust]] [[jarred-sumner|Jarred Sumner]] เลือก Rust เป็นภาษาใหม่ของ [[bun|Bun]] เพราะ bug ส่วนใหญ่ที่เจ็บคือ use-after-free, double-free และ forgot-to-free ใน error path.

บทความนี้ไม่ได้บอกว่า Rust ทำให้ทุกอย่างปลอดภัยโดยอัตโนมัติ. Bun ยังต้องใช้ `unsafe` เพราะคุยกับ C/C++ library อย่าง [[javascriptcore|JavaScriptCore]]. แต่ Rust ทำให้ ownership/lifetime หลายจุดต้องถูก encode ชัด และ `Drop` ลดภาระที่ต้องจำ cleanup ทุก call site แบบ manual.

## บทเรียนจาก Bun

Rust rewrite ของ Bun เริ่มจาก mechanical port ที่ยังคล้าย Zig มาก แล้วค่อย refactor ลด `unsafe` ทีหลัง. นี่ทำให้ทีม review ได้ง่าย เพราะคนที่เข้าใจ Zig เดิมยัง mapping behavior ไป Rust ใหม่ได้.

Source บอกว่าหลัง merge มี `unsafe` ราว 4% ของ Rust code block และ 78% ของ block เหล่านั้นเป็นบรรทัดเดียว เช่น pointer จาก C++ หรือ call เข้า C library. ตัวเลขนี้ควรอ่านเป็น claim จาก Bun team.

## See also

- [[bun-in-rust]]
- [[bun]]
- [[zig]]
- [[large-scale-changes]]
