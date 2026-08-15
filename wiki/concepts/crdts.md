---
title: Conflict-Free Replicated Data Types
type: concept
tags: [distributed-systems, synchronization, collaboration, data-structures]
created: 2026-08-15
updated: 2026-08-15
sources: [zed-is-1-0.md, software-is-made-between-commits.md]
---

# Conflict-Free Replicated Data Types / CRDT

**Conflict-Free Replicated Data Type (CRDT)** คือโครงสร้างข้อมูลสำหรับระบบกระจายที่ยอมให้ replica หลายชุดรับการแก้ไขพร้อมกัน แล้วค่อยรวม state หรือ operation กลับมาโดยได้ผลลัพธ์ที่สอดคล้องกัน ไม่ต้องมี server กลางตัดสินทุก edit ตามลำดับเดียวตั้งแต่ต้น

ใน wiki นี้ CRDT ปรากฏเป็นฐานของ [[deltadb|DeltaDB]] ระบบที่ [[zed-industries|Zed Industries]] ใช้ทำ replicated worktree ให้คนกับ agent หลายตัวแก้ไฟล์เดียวกันข้ามเครื่องได้

## Conflict-free แปลว่าอะไร

คำว่า conflict-free พูดถึงการรวมข้อมูลระดับระบบ ตัวอย่างเช่น replica สองเครื่องรับ operation คนละชุดแล้วระบบยังมีวิธี merge โดยไม่ทิ้ง edit ฝั่งใดเงียบ ๆ เมื่อทุก replica ได้ operation ครบ สุดท้ายควรเห็น state ที่ตรงกัน

มันไม่ได้แปลว่าเจตนาของคนสองคนจะไม่ชนกัน คนหนึ่งอาจเปลี่ยนชื่อ field ส่วนอีกคนเขียน consumer ที่ยังใช้ชื่อเก่า CRDT รวม operation ได้ครบ แต่ผลลัพธ์ยัง compile พังหรือทำ behavior ผิดได้

**ได้อะไร:** แยก conflict สองชั้นออกจากกัน — data convergence เป็นงานของ CRDT ส่วน semantic correctness ยังเป็นงานของทีม test และ review

## ทำไมเหมาะกับ collaborative editing

Editor แบบ real-time ต้องรับ edit จากหลายเครื่องและยังตอบสนองเร็ว ถ้ารอ lock กลางทุก keystroke งานจะสะดุด CRDT เปิดให้แต่ละ replica รับ operation ในพื้นที่ของตัวเองก่อน แล้ว sync ภายหลัง

[[software-is-made-between-commits|Software Is Made Between Commits]] ขยายการใช้แนวคิดนี้จากข้อความใน editor ไปทั้ง worktree พร้อมให้แต่ละ delta มี identity คงที่ จึงใช้เป็นฐานของ [[conversation-code-provenance|conversation-code provenance]] ได้

**ผลคือ:** ระบบไม่ได้แค่ทำให้ทุกคนเห็นไฟล์เดียวกัน แต่ยังอ้างถึง operation เดิมได้เมื่อ code เคลื่อนต่อ

## ขอบเขตที่ source ยังไม่บอก

บทความของ Zed ไม่ให้ algorithm, data model, ordering rule, garbage collection, storage cost หรือ recovery protocol ของ DeltaDB จึงยังบอกไม่ได้ว่าใช้ CRDT ชนิดใดและมี tradeoff เชิง performance แบบไหน หน้า wiki นี้อธิบายหลักทั่วไปและเก็บรายละเอียด implementation เป็นคำถามเปิด

## See also

- [[deltadb]]
- [[conversation-code-provenance]]
- [[collaborative-ai-engineering]]
- [[software-is-made-between-commits]]

