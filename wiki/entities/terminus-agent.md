---
title: Terminus
type: entity
tags: [agent, benchmark, minimalism, tmux]
created: 2026-04-28
updated: 2026-04-28
sources: [mario-zechner-pi-agent.md]
---

# Terminus / เทอร์มินัส

**Terminus** เป็น coding agent รุ่นบุกเบิกที่มีความเรียบง่ายที่สุด แต่กลับมีประสิทธิภาพสูงมากในการทดสอบ [[terminalbench]]

## กลไกการทำงาน

Terminus ให้สิทธิ์ LLM ในการเข้าถึงเพียงแค่:
1. **tmux session**: สภาพแวดล้อม terminal ที่รันอยู่
2. **Raw Keystrokes**: การส่งปุ่มกด (เหมือนมนุษย์พิมพ์)
3. **Screen Output**: การอ่านค่าตัวอักษรและรหัสควบคุม (VT sequences) ที่ปรากฏบนหน้าจอ

โดยที่ Terminus **ไม่มี** เครื่องมือจัดการไฟล์ (File tools), ไม่มีระบบค้นหาเว็บ และไม่มีการทำ AST indexing ใดๆ

## ความสำคัญ

ความสำเร็จของ Terminus เป็นหลักฐานเชิงประจักษ์ว่า "ความสามารถของตัวโมเดล" (Frontier model intelligence) นั้นสำคัญกว่า "ความเยอะของฟีเจอร์" ในตัว agent (Harness features) และเป็นแรงบันดาลใจสำคัญให้ [[mario-zechner]] สร้าง [[pi-agent|pi]] ขึ้นมา

## ดูเพิ่ม

- [[terminalbench]]
- [[pi-agent]]
