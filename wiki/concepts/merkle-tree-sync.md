---
title: Merkle Tree-based Sync
type: concept
tags: [sync, hashing, performance, infrastructure]
created: 2026-05-08
updated: 2026-05-08
sources: [why-im-against-claude-codes-grep-only-retrieval.md]
---

# Merkle Tree-based Sync / การซิงก์ข้อมูลด้วยโครงสร้าง Merkle Tree

Merkle Tree-based Sync เป็นวิธีการตรวจสอบความเปลี่ยนแปลงของข้อมูลในระบบไฟล์ขนาดใหญ่ โดยใช้โครงสร้างต้นไม้ที่มีการเก็บค่า hash (ลายนิ้วมือดิจิทัล) ต่อกันเป็นทอดๆ เพื่อให้รู้ว่ามีจุดไหนเปลี่ยนไปบ้างโดยไม่ต้องไล่ตรวจทุกไฟล์

## วิธีการทำงานใน Codebase
1. **File Hashing:** ทุกไฟล์จะถูก hash เก็บไว้
2. **Directory Hashing:** ค่า hash ของไฟล์ใน folder จะถูกนำมารวมกันเป็น hash ของ folder นั้น
3. **Root Hash:** ทำซ้ำไปเรื่อยๆ จนได้ hash ก้อนเดียวที่คุมทั้งโปรเจกต์
4. **Fast Comparison:** เมื่อมีการแก้โค้ด ระบบแค่เช็ก Root Hash ถ้าเปลี่ยน ก็ไล่ลงไปตามกิ่งก้าน (branch) ที่ hash เปลี่ยน เพื่อหาไฟล์ที่ต้องอัปเดต index ใหม่

## ประโยชน์สำหรับ AI Agents
ในเครื่องมืออย่าง [[claude-context]], เทคนิคนี้ช่วยให้:
- **Incremental Indexing:** อัปเดต vector database เฉพาะส่วนที่แก้โค้ดจริงๆ ไม่ต้อง scan ใหม่ทั้งโปรเจกต์ทุกครั้ง
- **ความเร็วสูง:** ตรวจสอบ codebase ขนาดใหญ่ได้ในระดับมิลลิวินาที
- **ประหยัดทรัพยากร:** ลดภาระของ CPU และ IO ในการเตรียม context ให้ Agent

## See also
- [[claude-context]]
- [[semantic-retrieval]]
