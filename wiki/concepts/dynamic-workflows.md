---
title: Dynamic Workflows
type: concept
tags: [ai, claude-code, agents, subagents, orchestration, large-scale-changes]
created: 2026-05-29
updated: 2026-05-29
sources: [Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md]
---

# Dynamic Workflows / เวิร์กโฟลว์แบบไดนามิก

ฟีเจอร์ใหม่ใน [[claude-code|Claude Code]] (สถานะ research preview) ที่เปิดตัวพร้อม [[claude-opus-4-8|Opus 4.8]] เมื่อ 28 พฤษภาคม 2026 ไอเดียคือ ปล่อยให้ Claude **รับงานก้อนใหญ่กว่าเดิมมากๆ** โดยไม่ต้องให้คนคอยซอยงานทีละขั้น

## มันทำงานยังไง

พอได้รับงานใหญ่ Claude จะ:

1. **วางแผนงานเอง** — แตกงานก้อนใหญ่ออกเป็นชิ้นย่อยๆ
2. **สั่ง subagents ทำงานคู่ขนานเป็นร้อยตัวในเซสชันเดียว** — แต่ละตัวรับงานชิ้นของมันไป
3. **ตรวจสอบผลลัพธ์ของตัวเอง** ก่อน
4. แล้วค่อย **รายงานกลับ**

ต่างจากการเรียก [[subagent-patterns|subagent]] แบบเดิมตรงที่ Claude เป็นคนคิดโครงงานและจำนวน agent เองตามขนาดงาน ไม่ใช่เรากำหนดให้ล่วงหน้า — เลยเรียกว่า "dynamic"

## ตัวอย่างที่ Anthropic ยกมา

Claude Code + Opus 4.8 **migrate codebase ที่มี code หลายแสนบรรทัด ได้ตั้งแต่เริ่มจนถึงขั้น merge** โดยใช้ **test suite ที่มีอยู่เป็นเกณฑ์ตัดสิน** ว่างานถูกต้องไหม

ตรงนี้คือจุดที่น่าสนใจ: งาน migrate ทั้ง codebase คือตัวอย่างคลาสสิกของ [[large-scale-changes|Large-Scale Changes]] ที่ปกติต้องใช้ทีมและเครื่องมือ automation เฉพาะทาง — dynamic workflows พยายามทำให้ agent ตัวเดียว (ที่กระจายเป็นร้อย subagent) ทำได้ end-to-end โดยมี test suite เป็น oracle ตัดสินถูก/ผิด

## ทำไมต้องมาคู่กับ Opus 4.8

งานแบบนี้จะใช้ได้จริงต่อเมื่อโมเดล **ไม่เนียนว่าทำเสร็จทั้งที่ยังไม่ผ่าน** — ถ้า subagent ร้อยตัวต่างก็ overclaim ว่างานของตัวเองเรียบร้อย ผล merge จะพังเงียบๆ จุดขายเรื่อง [[model-honesty|ความซื่อสัตย์]] ของ Opus 4.8 (ปล่อย bug ตัวเองผ่านน้อยลง ~4 เท่า, ตรวจงานตัวเองก่อนรายงาน) เลยเป็นเงื่อนไขที่ทำให้ dynamic workflows น่าไว้ใจพอจะปล่อยรันยาว

## ใครใช้ได้

เปิดให้แพ็กเกจ **Enterprise, Team, และ Max** (research preview)

## เทียบกับแนวคิดอื่นในวิกินี้

- **[[subagent-patterns]]** — fan-out / pipeline ของ subagent; dynamic workflows คือการให้โมเดลเลือกแพทเทิร์นและสเกลเอง
- **[[agent-swarm]]** — แนวคิดสเกล subagent เป็นร้อย (Kimi K2.6 ทำ 300 ตัว); dynamic workflows คือเวอร์ชันของ Anthropic ที่ผูกกับ test suite เป็นเกณฑ์
- **[[large-scale-changes]]** — superpower ของ Google ที่ให้คนเดียวแก้ code ข้ามล้านบรรทัด; dynamic workflows ดันความสามารถนี้เข้ามาในตัว agent
- **[[long-running-agents]]** — แพทเทิร์น agent ที่รันยาวข้ามวัน; dynamic workflows คือการรันยาวที่ self-plan + self-verify
- **[[orchestration-tax]]** — น้ำหนักถ่วงฝั่งบริโภค: ปล่อย subagent ร้อยตัวง่าย แต่คน review/merge มีคนเดียว การที่ dynamic workflows ผูก test suite เป็น oracle และ Opus 4.8 [[model-honesty|ไม่เนียนว่าทำเสร็จ]] คือสิ่งที่ช่วย "ลดภาษี" ฝั่งมนุษย์ — agent พิสูจน์งานตัวเองได้ คนเลยใช้ attention เฉพาะกับการตัดสินใจ architecture จริง ๆ

## ดูเพิ่ม

- [[claude-opus-4-8]]
- [[claude-code]]
- [[subagent-patterns]]
- [[agent-swarm]]
- [[large-scale-changes]]
- [[model-honesty]]
- [[orchestration-tax]]
- [[piyalitt-opus-4-8-recap]]
