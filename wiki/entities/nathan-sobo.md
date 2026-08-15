---
title: Nathan Sobo
type: entity
tags: [people, zed, editors, collaboration, version-control]
created: 2026-08-15
updated: 2026-08-15
sources: [software-is-made-between-commits.md]
---

# Nathan Sobo / เนธาน โซโบ

**Nathan Sobo** คือผู้ร่วมก่อตั้ง [[zed-industries|Zed Industries]] และผู้เขียน [[software-is-made-between-commits|Software Is Made Between Commits]] ในบทความเขาเล่าว่าทีมก่อตั้ง Zed ในปี 2021 เพราะอยากสร้าง editor สำหรับ developer ระดับสูง แล้วค่อยวางวิธีร่วมมือที่ไม่ถูกจำกัดด้วย commit

## มุมมองเรื่องการสร้าง software

Sobo ไม่ชอบ Pull Request ในฐานะพื้นที่หลักของ collaboration เพราะทีม Zed มักทำงานใน worktree เดียวกันและคุยเรื่อง code ระหว่างที่กำลังเขียน เขามองว่าพอ commit กับ push แล้ว บทสนทนาที่สำคัญที่สุดมักจบไปก่อน

เมื่อ coding agent เข้ามา มุมนี้ยิ่งสำคัญขึ้น บทสนทนาไม่ใช่แค่คำอธิบายประกอบ แต่เป็นสิ่งที่ทำให้ code เกิด ดังนั้นเขาจึงเสนอให้เก็บ conversation กับ evolution ของ worktree เป็น artifact ร่วมกันผ่าน [[deltadb|DeltaDB]]

**ได้อะไร:** มุมของ Sobo ย้าย collaboration จากการคอมเมนต์ snapshot ย้อนหลัง ไปสู่การคุยกับ code และ agent ขณะที่งานยังเปลี่ยนอยู่

## ขอบเขตของมุมมองนี้

นี่เป็น thesis จากผู้สร้าง product ที่กำลังเปิดตัว จึงอธิบาย design intent ได้ แต่ยังไม่ใช่ผลเปรียบเทียบว่าทีมทั่วไปทำงานดีกว่า PR workflow แค่ไหน คำถามเรื่อง governance, audit, privacy, performance และการเชื่อมกับ Git ecosystem ยังเปิดอยู่ใน source นี้

## See also

- [[zed-industries]]
- [[zed]]
- [[deltadb]]
- [[conversation-code-provenance]]
- [[software-is-made-between-commits]]
