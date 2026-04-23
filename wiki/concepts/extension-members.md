---
title: Extension Members (C#)
type: concept
tags: [csharp, language-features, extensions]
created: 2026-04-15
updated: 2026-04-23
sources: [csharp-14-whats-new.md]
---

# Extension Members

Extension members, ที่ถูกนำมาใช้ใน [[csharp|C#]] 14, เป็นการขยายฟีเจอร์ *extension method* ที่มีมานานนับทศวรรษ บล็อก `extension<T>(Receiver)` ใหม่สามารถมีได้ทั้ง extension **methods**, **properties**, **static members**, และ **operators** — ทั้งหมดนี้เขียนใน static class แต่สามารถเรียกใช้ได้ราวกับว่าเป็นของ type ที่ถูกขยาย

## ทำไมถึงสำคัญ

Extension methods (C# 3.0) ช่วยให้คุณสามารถเพิ่ม instance-style method เข้าไปใน type ที่คุณไม่ได้เป็นผู้สร้างได้ แต่ฟีเจอร์นี้จำกัดอยู่แค่ method เท่านั้น ไม่มีวิธีที่จะเพิ่ม computed property, static factory, หรือ operator เข้าไปใน type ของคนอื่นได้โดยไม่ต้องใช้ inheritance หรือ wrapper type C# 14 ได้ปิดช่องว่างนั้นแล้ว

## Syntax

Extension block จะอยู่ภายใน `static class` มีสองรูปแบบ:

```csharp
public static class Enumerable
{
    // Instance-receiver block: member จะทำงานเหมือน instance member
    extension<TSource>(IEnumerable<TSource> source)
    {
        public bool IsEmpty => !source.Any();
        public IEnumerable<TSource> Where(Func<TSource, bool> predicate) { ... }
    }

    // Type-receiver block: member จะทำงานเหมือน static member ของ receiver
    extension<TSource>(IEnumerable<TSource>)
    {
        public static IEnumerable<TSource> Combine(IEnumerable<TSource> a, IEnumerable<TSource> b) { ... }
        public static IEnumerable<TSource> Identity => Enumerable.Empty<TSource>();
        public static IEnumerable<TSource> operator +(IEnumerable<TSource> a, IEnumerable<TSource> b) => a.Concat(b);
    }
}
```

## ประเภทของ Member

| ประเภท | Instance-receiver | Type-receiver |
|---|---|---|
| Method | `sequence.Where(...)` | `IEnumerable<int>.Combine(a, b)` |
| Property | `sequence.IsEmpty` | `IEnumerable<int>.Identity` |
| Operator | — | `a + b` บน `IEnumerable<T>` |

## Call sites

- Instance-receiver member จะดูเหมือนการเรียก instance: `sequence.IsEmpty`
- Type-receiver member จะดูเหมือนการเรียก static บน type ที่ถูกขยาย: `IEnumerable<int>.Identity`
- User-defined extension operator จะผูกเหมือน operator ปกติที่ call site

## ความสัมพันธ์กับ extension methods

Extension method แบบดั้งเดิมที่ใช้ `this`-parameter (C# 3.0) ยังคงใช้งานได้ syntax ใหม่เป็นการเพิ่มเติมและมีความสามารถในการแสดงออกมากกว่า — รูปแบบเก่าสามารถแสดงออกในรูปแบบใหม่ได้ทางกลไก แต่รูปแบบใหม่จำเป็นสำหรับ properties, static members, และ operators

## ดูเพิ่ม

- [[csharp]]
- [[csharp-14-whats-new]]
- [[field-keyword]]
