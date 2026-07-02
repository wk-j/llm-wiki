---
title: Zoran Horvat
type: entity
tags: [software-engineering, dotnet, ddd, ef-core, education, ai-coding]
created: 2026-07-02
updated: 2026-07-02
sources: [zoran-horvat-domain-model-persistence.md, zoran-horvat-claude-no-planning-engine.md, planning-mode-dangerous-illusion.md]
---

# Zoran Horvat

[[zoran-horvat-domain-model-persistence|โพสต์ X เรื่อง domain model/persistence]] วาง [[zoran-horvat|Zoran Horvat]] เป็น software educator / .NET practitioner ที่สอนเรื่อง domain modeling, C#/.NET, และ [[entity-framework-core|EF Core]] persistence. [[zoran-horvat-claude-no-planning-engine|โพสต์ X เรื่อง Claude planning]] กับวิดีโอ [[planning-mode-dangerous-illusion]] เพิ่มมุมวิจารณ์ AI coding agent โดยเฉพาะ Plan mode ของ [[claude-code|Claude Code]].

หน้านี้บันทึกเฉพาะสิ่งที่มาจาก source นี้: Horvat ย้ำว่า [[domain-modeling|domain model]] ไม่ควรงอเข้าหา database แค่เพราะ ORM ทำให้ persistence ยาก. เขาเสนอให้ใช้ [[value-objects|value objects]], complex properties, value conversions, private constructor, และ query translation เพื่อเก็บ model ที่ expressive ไว้ได้.

## มุมมองที่ source นี้เพิ่ม

- [[domain-model-persistence-separation]]: แยกงานออกแบบ domain ออกจากงานเก็บข้อมูล
- [[primitive-obsession]]: เลี่ยงการแทน concept สำคัญด้วย `string`, `decimal`, หรือ raw GUID
- [[value-objects]]: ให้ concept ที่มีกฎของตัวเองเป็น type ของตัวเอง
- [[object-relational-mapping]]: ORM ไม่ควรเป็นเหตุผลให้ model แบนลงโดยไม่จำเป็น
- [[plan-mode-as-prompting]]: Plan mode เป็น prompt/harness scaffold ที่ให้ model เขียน draft plan ไม่ใช่หลักฐานว่า model มี planning engine หรือ engineering judgment จริง

## มุม Claude planning

ในโพสต์ [[zoran-horvat-claude-no-planning-engine]] และวิดีโอ [[planning-mode-dangerous-illusion]] Horvat บอกว่า plan ของ Claude ควรถูกอ่านเป็น first draft. เขาเทียบ Sonnet 4.6 กับ [[claude-opus-4-7|Opus 4.7]] ด้วยโจทย์ directory upload แล้วเห็นว่า Opus วางแผน performance ดีกว่าและทำงานสำเร็จกว่า แต่เขาตีความว่าเป็นผลจาก prompt iteration / model quality ที่ refined กว่า ไม่ใช่ symbolic understanding.

จุดที่เขาเน้นคือทั้งสอง model ยังพลาด senior moves เช่นการถามว่าควรทิ้ง user data หรือไม่ และการเห็น duplication ระหว่าง server/client. ตรงนี้เชื่อมกับ [[judgement-vs-automation]]: plan text ที่เรียบร้อยยังไม่เท่ากับ engineering judgment.

## Open questions

- claim เฉพาะของ EF Core 10 ในโพสต์ยังไม่ได้ตรวจจาก Microsoft docs โดยตรง
- ยังไม่ได้ ingest วิดีโอ "EF Core Mapping: Dark Magic (Here Is Why)" ที่โพสต์อ้างถึง

## See also

- [[zoran-horvat-domain-model-persistence]]
- [[zoran-horvat-claude-no-planning-engine]]
- [[planning-mode-dangerous-illusion]]
- [[entity-framework-core]]
- [[domain-model-persistence-separation]]
- [[domain-modeling]]
- [[value-objects]]
- [[plan-mode-as-prompting]]
