---
title: Entity Framework Core
type: entity
tags: [dotnet, database, orm, persistence, ef-core]
created: 2026-07-02
updated: 2026-07-02
sources: [zoran-horvat-domain-model-persistence.md]
---

# Entity Framework Core / EF Core

**Entity Framework Core (EF Core)** คือ ORM ของฝั่ง .NET ที่ช่วย map object ใน application กับข้อมูลใน relational database. ใน source นี้ [[zoran-horvat|Zoran Horvat]] ใช้ EF Core เป็นตัวอย่างว่า persistence tooling ไม่จำเป็นต้องบังคับให้ [[domain-modeling|domain model]] แบนลงเป็น primitive เสมอไป.

## บทบาทใน source นี้

Horvat อ้างว่า EF Core 10 รองรับการเก็บ nested [[value-objects|value objects]] ด้วย complex properties ลงตารางเดียว. แนวคิดคือ object graph อยู่ใน model ได้ แต่ leaf scalar ถูก map ลงเป็น columns แยกใน table.

เขายังพูดถึง value conversions สำหรับ wrapper type ที่ถือค่าเดียว เช่น identifier หรือ timestamp. Converter unwrap ค่าเวลา write และ rebuild type เวลา read. ตรงนี้เป็น persistence boundary ที่ใช้ enforce invariant ซ้ำได้.

## ข้อควรระวัง

หน้านี้ยังไม่ใช่คู่มือ EF Core. Claim เรื่อง EF Core 10 มาจากโพสต์ X ที่ ingested เท่านั้น. ถ้าจะนำไปใช้จริง ต้องตรวจ version, provider support, migration output, และ SQL translation จากเอกสาร/โปรเจกต์จริง.

## See also

- [[zoran-horvat-domain-model-persistence]]
- [[object-relational-mapping]]
- [[domain-model-persistence-separation]]
- [[value-objects]]
