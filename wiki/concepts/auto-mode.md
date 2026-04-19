---
title: Auto Mode
type: concept
tags: [ai, claude-code, permissions, autonomy, coding-harness]
created: 2026-04-20
updated: 2026-04-20
sources: [claude-code-auto-mode.md]
---

# Auto Mode / โหมดอัตโนมัติของ Claude Code

**Permission mode แบบกลาง** ของ [[claude-code|Claude Code]] ที่ให้ classifier คั่นกลางระหว่าง Claude กับการกด "อนุญาต" แต่ละ tool call — แทนที่จะถามคนทุกครั้ง หรือปล่อยผ่านหมดแบบ `--dangerously-skip-permissions`

ประกาศเมื่อ 2026-03-24 ([[claude-code-auto-mode]]) ตอนนั้นยังใช้กับ Sonnet 4.6 / Opus 4.6 ก่อน 4.7 จะออกด้วยซ้ำ พอ [[claude-opus-4-7|Opus 4.7]] ออกในเดือนถัดมา auto mode ก็ขยายไปถึง Claude Code Max users

## สเปกตรัมของ permission mode

ลองนึกภาพเป็นเส้นต่อเนื่องระหว่าง "ปลอดภัยแต่ช้า" กับ "เร็วแต่เสี่ยง":

| Mode | Claude ทำอะไร | คนถูกถามเมื่อไหร่ | เหมาะกับ |
|---|---|---|---|
| **Default** | รอยืนยันทุก file write / bash command | ทุก tool call | งานสั้น งาน interactive |
| **Auto mode** | ทำเอง ถ้า classifier บอกว่าปลอดภัย | เฉพาะตอน Claude ยืนยันจะทำ action ที่ถูก block ซ้ำ ๆ | งาน long-running ที่ไว้ใจได้ส่วนใหญ่ |
| **`--dangerously-skip-permissions`** | ทำทุกอย่างโดยไม่ถาม | ไม่มี | เฉพาะใน sandbox / isolated env |

Auto mode = ตำแหน่งกลางที่เพิ่งถูกเพิ่มเข้ามา ไม่ใช่แค่ปุ่มเปิด/ปิด

## classifier ทำอะไร

ก่อน tool call แต่ละครั้งถูก run มี classifier ตัวหนึ่งมา **review action นั้น** ว่ามีโอกาสเป็น destructive หรือเปล่า เช่น:

- ลบไฟล์จำนวนมาก
- ดึงข้อมูล sensitive ออกไปข้างนอก (data exfiltration)
- run โค้ดที่ดูเป็นอันตราย

ถ้าดูปลอดภัย → **ผ่านเลย** ไม่ต้องถามคน

ถ้าเสี่ยง → **block** แล้ว redirect ให้ Claude ลองท่าอื่น

ถ้า Claude ดื้อ พยายามทำ action ที่ถูก block ซ้ำ ๆ → สุดท้าย **ขึ้น prompt ถามคน**

กลไกนี้เหมือนใส่ reviewer agent เล็ก ๆ คั่นระหว่าง main agent กับ shell — คล้าย pipeline ใน [[subagent-patterns]] แต่เป็น pipeline ที่ harness บังคับ ไม่ใช่ prompt แบบที่ผู้ใช้ออกแบบเอง

## ข้อจำกัดที่ Anthropic บอกตรง ๆ

- **ไม่ได้ปลอดภัย 100%** — classifier อาจปล่อย action เสี่ยงผ่าน ถ้า intent ของ user กำกวม หรือ Claude ไม่รู้บริบทของ environment มากพอ Anthropic ยังแนะนำให้ใช้ใน isolated environment อยู่ดี
- อาจ **block action ที่ไม่อันตราย** บ้างเป็นครั้งคราว
- **เสีย token + latency เพิ่มเล็กน้อย** ต่อ tool call เพราะต้อง run classifier

## วิธีเปิด

- **CLI:** `claude --enable-auto-mode` ก่อน แล้วกด **Shift+Tab** เพื่อ cycle permission mode มาถึง auto
- **Desktop / VS Code:** เปิด toggle ใน Settings → Claude Code ก่อน แล้วเลือกจาก permission-mode dropdown
- **Admin ปิดทั้ง org ได้** ผ่าน managed settings: `"disableAutoMode": "disable"`

## ความเชื่อมโยงกับแนวคิดอื่น

- **[[delegation-mindset]]** — Akshay Pachaar แนะนำ auto mode เป็นหนึ่งใน 3 ท่าหลักของ 4.7: ช่วยให้ long-running task จบได้โดยไม่ต้อง check-in เป็นระยะ ๆ (ซึ่งทุก check-in = reasoning รอบใหม่ที่ 4.7 เก็บเงินเต็ม)
- **[[coding-harness]]** — permission mode คือหนึ่งใน control surface หลักของ harness; auto mode = ตำแหน่งใหม่บน spectrum ที่ Alex Ker มองว่า harness เป็นที่อยู่ของ human engineering judgment
- **[[claude-code-session-management]]** — พอ session ยาว ๆ การถูกถามทุก tool call จะตัดจังหวะงานและกินเวลาคน — auto mode ช่วยให้ session ยาวจบในรวดเดียว
- **[[subagent-patterns]]** — classifier-gate คือ pipeline pattern ที่ harness ใส่ให้ฟรี เทียบกับ [[harness-engineering|harness ของ Panutat]] ที่ผู้ใช้ประกอบ reviewer agent เอง

## เมื่อไหร่ไม่ควรเปิด

- งานที่ยังไม่รู้ตัวเองว่าจะให้ Claude ทำอะไร — อยาก review ทีละก้าวก่อน
- งาน production บน environment ที่ **ไม่ได้ isolate** (เช่น laptop ที่มี SSH key, prod credentials, repo ที่ commit เข้า main ได้ตรง) — Anthropic ย้ำว่าถึงจะเบากว่า `--dangerously-skip-permissions` แต่ก็ยังไม่ใช่ safe-by-default
- งานสั้นที่ถูกถามไม่กี่ครั้งอยู่แล้ว — เปิด auto mode เสีย classifier overhead เปล่า ๆ

## See also

- [[claude-code-auto-mode]]
- [[claude-code]]
- [[claude-opus-4-7]]
- [[delegation-mindset]]
- [[coding-harness]]
- [[subagent-patterns]]
