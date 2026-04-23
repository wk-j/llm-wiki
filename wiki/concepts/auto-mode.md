---
title: Auto Mode
type: concept
tags: [ai, claude-code, permissions, autonomy, coding-harness]
created: 2026-04-20
updated: 2026-04-23
sources: [claude-code-auto-mode]
---

# Auto Mode / โหมดอัตโนมัติของ Claude Code

**Auto Mode** คือ permission mode แบบ "กึ่งกลาง" ของ [[claude-code|Claude Code]] ที่ออกแบบมาเพื่อลดความถี่ในการขออนุญาต (permission prompt) โดยให้ **classifier** ทำหน้าที่คั่นกลางระหว่าง Claude กับการรัน tool call แต่ละครั้ง แทนที่จะต้องถามผู้ใช้ทุกครั้ง หรือข้ามการตรวจสอบทั้งหมดแบบ `--dangerously-skip-permissions`

ฟีเจอร์นี้ประกาศใช้เมื่อวันที่ 24 มีนาคม 2026 ([[claude-code-auto-mode]]) ซึ่งในตอนนั้นยังใช้กับ Sonnet 4.6 และ Opus 4.6 อยู่ก่อนที่ Opus 4.7 จะเปิดตัว และเมื่อ [[claude-opus-4-7|Opus 4.7]] เปิดตัวในเดือนถัดมา, Auto Mode ก็ถูกขยายให้ครอบคลุมผู้ใช้ Claude Code Max ด้วย

## สเปกตรัมของ Permission Mode

เราสามารถมอง permission mode เป็นเส้นสเปกตรัมที่เรียงจาก "ปลอดภัยแต่ช้า" ไปจนถึง "เร็วแต่เสี่ยง":

| Mode | Claude ทำอะไร | ผู้ใช้ถูกถามเมื่อไหร่ | เหมาะกับงานประเภทไหน |
|---|---|---|---|
| **Default** | รอการยืนยันสำหรับทุก file write และ bash command | ทุก tool call | งานสั้นๆ, งานที่ต้องการ interaction สูง |
| **Auto mode** | ทำงานอัตโนมัติ ถ้า classifier ประเมินว่าปลอดภัย | เฉพาะเมื่อ Claude ยืนยันจะทำ action ที่ถูก block ซ้ำๆ | งาน long-running ที่เราไว้ใจได้ในระดับหนึ่ง |
| **`--dangerously-skip-permissions`** | ทำทุกอย่างโดยไม่ถาม | ไม่มีการถาม | ใช้ใน sandbox หรือ isolated environment เท่านั้น |

Auto mode คือตำแหน่งตรงกลางที่ช่วยสร้างสมดุลระหว่างความเร็วและความปลอดภัย

## Classifier ทำงานอย่างไร

ก่อนที่ tool call แต่ละครั้งจะถูกรัน, จะมี classifier เข้ามา**ตรวจสอบ action นั้น** ว่ามีความเสี่ยงที่จะก่อให้เกิดความเสียหาย (destructive) หรือไม่ ตัวอย่างเช่น:

- การลบไฟล์จำนวนมาก
- การดึงข้อมูลที่อาจเป็นความลับออกไป (data exfiltration)
- การรันโค้ดที่ดูน่าสงสัยหรืออาจเป็นอันตราย

หาก classifier ประเมินว่าปลอดภัย → **action จะถูกรันทันที** โดยไม่ต้องถามผู้ใช้

หากประเมินว่ามีความเสี่ยง → **action จะถูก block** และ Claude จะถูก redirect ให้ลองใช้วิธีอื่นแทน

หาก Claude ยังคงดื้อดึงที่จะทำ action ที่ถูก block ซ้ำๆ → สุดท้ายระบบจะ**แสดง prompt เพื่อถามผู้ใช้**โดยตรง

กลไกนี้เปรียบเสมือนการมี reviewer agent เล็กๆ คั่นอยู่ระหว่าง main agent กับ shell ซึ่งคล้ายกับ pattern แบบ pipeline ใน [[subagent-patterns]] แต่เป็น pipeline ที่ตัว harness เป็นผู้กำหนด ไม่ใช่ prompt ที่ผู้ใช้ออกแบบเอง

## ข้อจำกัดที่ควรทราบ

Anthropic ได้ระบุข้อจำกัดไว้อย่างชัดเจน:
- **ไม่ได้ปลอดภัย 100%:** Classifier อาจตัดสินใจผิดพลาดและปล่อย action ที่มีความเสี่ยงผ่านไปได้, โดยเฉพาะถ้า intent ของผู้ใช้ไม่ชัดเจน หรือ Claude ไม่มี context ของ environment มากพอ Anthropic ยังคงแนะนำให้ใช้ใน isolated environment เท่านั้น
- **False Positives:** อาจมีการ block action ที่ไม่อันตรายเกิดขึ้นได้บ้างเป็นครั้งคราว
- **Overhead:** การรัน classifier ทำให้เกิด token และ latency เพิ่มขึ้นเล็กน้อยในแต่ละ tool call

## วิธีเปิดใช้งาน

- **CLI:** พิมพ์ `claude --enable-auto-mode` จากนั้นกด **Shift+Tab** เพื่อสลับ permission mode ไปที่ auto
- **Desktop / VS Code:** เปิด toggle ใน Settings → Claude Code แล้วเลือก `auto` จาก permission-mode dropdown
- **Admin Control:** ผู้ดูแลระบบสามารถปิดฟีเจอร์นี้ทั้งองค์กรได้ผ่าน managed settings โดยตั้งค่า `"disableAutoMode": "disable"`

## ความเชื่อมโยงกับแนวคิดอื่น

- **[[delegation-mindset]]:** Akshay Pachaar แนะนำ Auto Mode เป็นหนึ่งในสามเทคนิคหลักสำหรับ Opus 4.7 เพราะช่วยให้ task ที่ต้องรันนานๆ สามารถจบได้โดยไม่ต้องมีคนคอย check-in (ซึ่งทุกการ check-in หมายถึงการเริ่ม reasoning cycle ใหม่ที่ Opus 4.7 คิดค่าใช้จ่ายเต็มจำนวน)
- **[[coding-harness]]:** Permission mode คือหนึ่งใน control surface ที่สำคัญของ harness และ Auto Mode ก็คือตำแหน่งใหม่บนสเปกตรัมที่สะท้อนการตัดสินใจทางวิศวกรรมของมนุษย์
- **[[claude-code-session-management]]:** สำหรับ session ที่ยาวนาน, การต้องตอบ prompt ทุกครั้งจะขัดจังหวะการทำงาน Auto Mode จึงช่วยให้ session ที่ยาวสามารถรันจนจบได้ในครั้งเดียว
- **[[subagent-patterns]]:** Classifier-gate คือ pipeline pattern ที่ harness ติดตั้งมาให้ฟรี เทียบกับ [[harness-engineering|harness ของ Panutat]] ที่ผู้ใช้ต้องสร้าง reviewer agent ขึ้นมาเอง

## เมื่อไหร่ที่ไม่ควรเปิด

- เมื่อยังไม่แน่ใจว่าจะให้ Claude ทำอะไร และต้องการตรวจสอบการทำงานทีละขั้นตอน
- เมื่อทำงานใน environment ที่**ไม่ได้ isolate** (เช่น บน laptop ที่มี SSH keys, production credentials, หรือ repo ที่สามารถ commit เข้า main ได้โดยตรง)
- สำหรับงานสั้นๆ ที่มีการถามไม่กี่ครั้งอยู่แล้ว การเปิด Auto Mode อาจเป็นการเพิ่ม overhead โดยไม่จำเป็น

## See also

- [[claude-code-auto-mode]]
- [[claude-code]]
- [[claude-opus-4-7]]
- [[delegation-mindset]]
- [[coding-harness]]
- [[subagent-patterns]]
- [[graduated-autonomy]]
- [[agent-runtime-untrusted]]
