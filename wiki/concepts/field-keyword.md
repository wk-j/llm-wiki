---
title: The `field` Keyword (C#)
type: concept
tags: [csharp, language-features, properties]
created: 2026-04-15
updated: 2026-04-23
sources: [csharp-14-whats-new.md]
---

# The `field` Keyword / keyword `field` ของ C#

`field` เป็น contextual keyword ที่ถูกนำมาใช้ใน [[csharp|C#]] 14 สามารถใช้ได้ภายใน body ของ property accessor มันอ้างอิงถึง **compiler-synthesized backing field** สำหรับ property นั้นๆ ซึ่งช่วยลดความจำเป็นในการประกาศ `private` backing field ด้วยตนเองทุกครั้งที่ต้องการ custom accessor logic

## ปัญหาที่แก้ไข

ก่อน C# 14, property ใดๆ ที่ต้องการ custom get/set logic (เช่น validation, lazy initialization, change notification) จำเป็นต้องประกาศ backing field อย่างชัดเจน:

```csharp
private string _msg;
public string Message
{
    get => _msg;
    set => _msg = value ?? throw new ArgumentNullException(nameof(value));
}
```

field `_msg` เพิ่มความยุ่งยากในการตั้งชื่อ, ต้องคอยให้สอดคล้องกับ property, และทำให้ member list ของ type ดูรก

## ด้วย `field`

```csharp
public string Message
{
    get;
    set => field = value ?? throw new ArgumentNullException(nameof(value));
}
```

Compiler จะสร้าง backing field ให้โดยอัตโนมัติ คุณสามารถเขียน custom body สำหรับ accessor **ตัวใดตัวหนึ่งหรือทั้งสองตัว** ก็ได้ — ในที่นี้ `get` จะถูก auto-implement ในขณะที่ `set` มีการ validate

## การแก้ความกำกวม (Disambiguation)

`field` เป็น contextual keyword ดังนั้น identifier ที่มีอยู่ก่อนแล้วชื่อ `field` ใน scope อาจทำให้เกิดความสับสนหรือ breaking change ได้ มีทางออกสองทาง:

- ใช้ `@field` เพื่อบังคับให้ตีความว่าเป็น identifier
- ใช้ `this.field` เมื่ออ้างถึง member ที่ชื่อ `field`
- หรือแค่เปลี่ยนชื่อ symbol ที่ชนกัน

## เกี่ยวข้องกับ

- เป็นส่วนเสริมของ auto-property init ของ C# 9+ และ required members ของ C# 11
- เข้ากันได้ดีกับ nullability annotations และ validation patterns

## ดูเพิ่ม

- [[csharp]]
- [[csharp-14-whats-new]]
- [[extension-members]]
