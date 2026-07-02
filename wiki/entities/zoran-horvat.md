---
title: Zoran Horvat
type: entity
tags: [software-engineering, dotnet, ddd, ef-core, education]
created: 2026-07-02
updated: 2026-07-02
sources: [zoran-horvat-domain-model-persistence.md]
---

# Zoran Horvat

[[zoran-horvat-domain-model-persistence|โพสต์ X ที่ ingested]] วาง [[zoran-horvat|Zoran Horvat]] เป็น software educator / .NET practitioner ที่สอนเรื่อง domain modeling, C#/.NET, และ [[entity-framework-core|EF Core]] persistence.

หน้านี้บันทึกเฉพาะสิ่งที่มาจาก source นี้: Horvat ย้ำว่า [[domain-modeling|domain model]] ไม่ควรงอเข้าหา database แค่เพราะ ORM ทำให้ persistence ยาก. เขาเสนอให้ใช้ [[value-objects|value objects]], complex properties, value conversions, private constructor, และ query translation เพื่อเก็บ model ที่ expressive ไว้ได้.

## มุมมองที่ source นี้เพิ่ม

- [[domain-model-persistence-separation]]: แยกงานออกแบบ domain ออกจากงานเก็บข้อมูล
- [[primitive-obsession]]: เลี่ยงการแทน concept สำคัญด้วย `string`, `decimal`, หรือ raw GUID
- [[value-objects]]: ให้ concept ที่มีกฎของตัวเองเป็น type ของตัวเอง
- [[object-relational-mapping]]: ORM ไม่ควรเป็นเหตุผลให้ model แบนลงโดยไม่จำเป็น

## Open questions

- claim เฉพาะของ EF Core 10 ในโพสต์ยังไม่ได้ตรวจจาก Microsoft docs โดยตรง
- ยังไม่ได้ ingest วิดีโอ "EF Core Mapping: Dark Magic (Here Is Why)" ที่โพสต์อ้างถึง

## See also

- [[zoran-horvat-domain-model-persistence]]
- [[entity-framework-core]]
- [[domain-model-persistence-separation]]
- [[domain-modeling]]
- [[value-objects]]
