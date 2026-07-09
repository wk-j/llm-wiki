---
title: Zig
type: entity
tags: [programming-language, systems, memory-management]
created: 2026-07-09
updated: 2026-07-09
sources: [bun-in-rust.md]
---

# Zig

**Zig** คือภาษา programming สำหรับ systems software ที่เน้นความเรียบง่าย การควบคุม low-level และ explicit control flow. [[jarred-sumner|Jarred Sumner]] ใช้ Zig สร้าง [[bun|Bun]] รุ่นแรก และย้ำใน [[bun-in-rust|Bun in Rust]] ว่า Zig ทำให้ project scope ใหญ่แบบ Bun เกิดขึ้นได้ในหนึ่งปี.

ข้อจำกัดที่บทความพูดถึงไม่ใช่ "Zig ไม่ดี" แต่คือ fit กับงานเฉพาะของ Bun. Bun ต้องผสม garbage-collected JavaScript values กับ manually-managed memory. Zig ไม่มี constructor/destructor แบบ C++ หรือ `Drop` แบบ [[rust|Rust]], เลยต้องใส่ cleanup ด้วย `defer`/`errdefer` หรือ pattern/style guide ที่คนต้องทำถูกทุกจุด.

## ใน rewrite ของ Bun

Rust code รอบแรกตั้งใจให้ดูเหมือน transpile จาก Zig เพื่อรักษา architecture, performance และ feature set เดิม. ความใกล้เคียงนี้ช่วยให้ reviewer ตรวจ behavior เทียบของเก่าได้ แต่ก็สร้างกับดัก porting mistakes เมื่อ syntax คล้ายกันแต่ semantics ต่างกัน.

## See also

- [[bun-in-rust]]
- [[bun]]
- [[rust]]
