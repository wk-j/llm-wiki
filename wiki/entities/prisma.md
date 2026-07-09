---
title: Prisma
type: entity
tags: [company, database, developer-tools]
created: 2026-07-09
updated: 2026-07-09
sources: [bun-in-rust.md]
---

# Prisma

**Prisma** คือบริษัท/ผลิตภัณฑ์ด้าน database tooling สำหรับนักพัฒนา. ใน [[bun-in-rust|Bun in Rust]] [[jarred-sumner|Jarred Sumner]] บอกว่า Prisma เปิด public beta ของ Prisma Compute บน Rust rewrite ของ [[bun|Bun]].

ตัวอย่างนี้ใช้เป็น production signal: rewrite ไม่ได้อยู่แค่ใน branch ทดลอง แต่ถูก product ภายนอกลองใช้กับ failure mode จริง เช่น memory leaks และ connection pool ที่กู้ตัวเองหลัง VM pause/resume ไม่ได้. คำกล่าวนี้ยังเป็น source-attributed จากบทความ Bun.

## See also

- [[bun]]
- [[bun-in-rust]]
- [[rust]]
