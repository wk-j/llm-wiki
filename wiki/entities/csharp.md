---
title: C#
type: entity
tags: [csharp, dotnet, programming-languages, microsoft]
created: 2026-04-15
updated: 2026-04-23
sources: [csharp-14-whats-new.md]
---

# C#

C# (ซีชาร์ป) เป็นภาษาโปรแกรมแบบ statically-typed, object-oriented ของ Microsoft สำหรับแพลตฟอร์ม .NET มีรอบการออกเวอร์ชันใหม่ทุกปี โดยแต่ละเวอร์ชันจะผูกกับ .NET release ที่สอดคล้องกัน

## เวอร์ชันปัจจุบัน

**C# 14** — เวอร์ชันล่าสุด มาพร้อมกับ **.NET 10**, รองรับใน Visual Studio 2026 และ .NET 10 SDK ดูรายการฟีเจอร์ทั้งหมดได้ที่ [[csharp-14-whats-new]]

## ฟีเจอร์เด่นใน C# 14

- [[extension-members]] — generalized extensions: properties, static members, operators
- [[field-keyword]] — `field` keyword ภายใน property accessor สำหรับ backing field ที่สร้างขึ้นโดยอัตโนมัติ
- Null-conditional assignment (`customer?.Order = ...`)
- First-class implicit conversions สำหรับ `Span<T>` / `ReadOnlySpan<T>`
- Lambda parameter modifiers (`ref`, `out`, `scoped`...) โดยไม่ต้องระบุ type อย่างชัดเจน
- `partial` constructors และ events
- User-defined compound assignment operators
- `nameof` กับ unbound generics (`nameof(List<>)`)

## หมายเหตุเรื่องเวอร์ชัน

C# แต่ละเวอร์ชันจะ target .NET base class library ที่เฉพาะเจาะจง C# 14 ต้องการ .NET 10; framework ที่เก่ากว่าจะยังคงใช้ภาษาเวอร์ชันก่อนหน้า สามารถตั้งค่าได้ผ่าน `<LangVersion>` ในไฟล์โปรเจกต์

## ดูเพิ่ม

- [[csharp-14-whats-new]]
- [[extension-members]]
- [[field-keyword]]
