---
title: Bun
type: entity
tags: [runtime, javascript, tooling, software-engineering]
created: 2026-07-09
updated: 2026-07-09
sources: [bun-in-rust.md]
---

# Bun

**Bun** คือ JavaScript runtime และ toolchain ที่รวม runtime, transpiler, bundler, package manager และ test runner ไว้ในตัวเดียว. ใน [[bun-in-rust|Bun in Rust]] [[jarred-sumner|Jarred Sumner]] เล่าว่า Bun เริ่มจากการ port transpiler ของ esbuild จาก Go มา [[zig|Zig]] แล้วขยาย scope จนครอบคลุม Node-compatible APIs หลายสิบตัว.

บทความนี้ทำให้ Bun เป็นเคสใหญ่ใน wiki เพราะมันไม่ใช่แค่ product JavaScript. มันเป็นตัวอย่างของ runtime ที่ memory safety ยากมาก: JavaScript เป็น garbage-collected language แต่ implementation ต้องคุยกับ memory ที่จัดการเองใน Zig/C/C++ และ embed library อย่าง [[javascriptcore|JavaScriptCore]].

## Rust rewrite

Bun v1.3.14 เป็น version สุดท้ายที่เขียนด้วย Zig. Bun v1.4.0 จะเป็น version แรกที่เขียนด้วย [[rust|Rust]]. เหตุผลหลักคือ stability: ลด bug กลุ่ม use-after-free, double-free, memory leak และ cleanup ใน error path.

การ rewrite ใช้ [[claude-code|Claude Code]] กับ [[fable|Claude Fable 5]] ผ่าน [[dynamic-workflows|dynamic workflows]] ราว 50 workflow, peak ประมาณ 64 Claudes พร้อมกัน, 11 วันจน test suite ผ่านทุก platform. Source บอกว่า rewrite แก้ bug ที่ reproduce ได้ 128 ตัวใน v1.3.14 และทำให้ binary size/stack usage/performance ดีขึ้นหลายจุด.

## ทำไมอยู่ใน wiki นี้

Bun กลายเป็นหลักฐานภาคสนามของหลายแนวคิด:

- [[large-scale-changes]] — rewrite ข้ามภาษาระดับล้านบรรทัด
- [[adversarial-review-loops]] — maker/checker/fixer pattern ที่ใช้จริง
- [[behavioral-verifier]] — test suite ภาษา TypeScript เป็น oracle ข้าม implementation language
- [[orchestration-tax]] — agent เยอะช่วยผลิต แต่คนยังต้อง monitor, review และ merge

## See also

- [[bun-in-rust]]
- [[jarred-sumner]]
- [[rust]]
- [[zig]]
- [[claude-code]]
- [[dynamic-workflows]]
