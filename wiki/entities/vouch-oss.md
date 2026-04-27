---
title: Vouch
type: entity
tags: [tool, open-source, security, ai-defense]
created: 2026-04-28
updated: 2026-04-28
sources: [mario-zechner-pi-agent.md]
---

# Vouch / เวาช์

**Vouch** เป็นเครื่องมือ Open Source ที่พัฒนาโดย Mitchell Hashimoto (ผู้สร้าง Ghostty/HashiCorp) เพื่อช่วยเจ้าของโปรเจกต์ Open Source ป้องกันการรุกรานจาก [[clanker-slop|Clanker Slop]] (AI-generated PRs)

## หน้าที่หลัก

Vouch ทำหน้าที่เป็นด่านหน้าในการทำ **Human Verification**:
- **Whitelist Management**: เก็บรายชื่อบัญชีผู้ใช้ GitHub ที่ได้รับการยืนยันว่าเป็น "มนุษย์" และมีความตั้งใจดีในการช่วยโปรเจกต์
- **Auto-moderation**: ตรวจสอบ PR ที่เข้ามาใหม่ ถ้าผู้ส่งไม่อยู่ในรายชื่อที่ Vouch ไว้ ระบบจะทำการปิด (Close) หรือแจ้งเตือนทันที
- **Friction as a Filter**: บังคับให้ผู้ที่จะช่วยโปรเจกต์ต้อง "แนะนำตัว" หรือสื่อสารผ่านช่องทางที่กำหนดก่อน เพื่อสร้างกำแพงกั้นไม่ให้ agent เข้ามาพ่น code ได้โดยอัตโนมัติ

## ดูเพิ่ม

- [[clanker-slop]]
- [[mario-zechner]]
