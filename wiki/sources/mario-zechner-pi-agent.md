---
title: "I Hated Every Coding Agent, So I Built My Own — Mario Zechner (Pi)"
type: source
tags: [coding-agents, pi, terminal, open-source, minimalism]
created: 2026-04-28
updated: 2026-04-28
sources: [I Hated Every Coding Agent, So I Built My Own — Mario Zechner (Pi).md]
---

# I Hated Every Coding Agent, So I Built My Own / เมื่อผมเกลียด Coding Agent ทุกตัวที่มีอยู่ เลยสร้างขึ้นมาเอง

Mario Zechner (ผู้สร้าง libGDX) เล่าถึงที่มาของ [[pi-agent|pi]] ซึ่งเป็น coding agent ใน terminal ที่เน้นความเรียบง่าย (Minimalism) และความสามารถในการดัดแปลง (Extensibility) เพื่อแก้ปัญหา "Feature Bloat" และ "Hidden Context" ที่พบในเครื่องมือกระแสหลักอย่าง [[claude-code]]

## Key Takeaways

- **The Spaceship Trap**: ปัญหาของ coding agent ส่วนใหญ่อย่าง Claude Code คือการพยายามใส่ฟีเจอร์ทุกอย่างเข้าไปจนกลายเป็น "ยานอวกาศ" ที่ผู้ใช้ใช้จริงเพียง 5% แต่ต้องแบกรับความซับซ้อนและอาการ "Flicker" ของ UI ที่ไม่จำเป็น
- **Minimalism is Enough**: จากการดู [[terminalbench]] พบว่า [[terminus-agent]] ซึ่งเป็น agent ที่มีแค่ tmux และ keystrokes (ไม่มีเครื่องมือซับซ้อน) กลับทำคะแนนได้สูงสุด สะท้อนว่า agent ไม่ได้ต้องการฟีเจอร์เยอะเพื่อทำงานให้เก่ง
- **Malleable Tools / เครื่องมือที่ดัดแปลงได้**: Mario เชื่อว่าเรายังอยู่ในช่วง "ลองผิดลองถูก" (Messing around) ดังนั้นเครื่องมือควรจะดัดแปลงได้ง่าย (Malleable) เพื่อให้ Developer ทดลอง workflow ใหม่ๆ ได้เร็ว
- **Pi Core Design**:
    - **Four Tools Only**: มีแค่ read, write, edit, และ bash
    - **Tree-structured Sessions**: จัดเก็บประวัติเป็นแบบต้นไม้ (Branching) ช่วยให้ทำ sub-tasks หรือสรุปข้อมูลแล้วกลับมาที่รากได้ง่าย
    - **Hot-reloading Extensions**: เขียนเครื่องมือเสริม (Tools) หรือ UI ใหม่ด้วย TypeScript และโหลดใหม่ได้ทันทีโดยไม่ต้องรีสตาร์ท
- **Context Management Problems**: วิพากษ์วิจารณ์การจัดการ context ใน [[opencode]] เช่น การทำ compaction ที่ทำให้ prompt cache พัง หรือการใช้ LSP feedback ระหว่างที่ agent ยังแก้ไข code ไม่เสร็จ (ทำให้ agent สับสน)
- **Clanker Slop & Human Verification**: ในยุค AI-generated spam (Clanker Slop), Mario ใช้ระบบ Whitelist และเครื่องมืออย่าง [[vouch-oss]] เพื่อให้มั่นใจว่าคนที่มาเปิด PR ใน Open Source เป็นมนุษย์จริงๆ

## Key Entities

- [[mario-zechner]]: ผู้สร้าง libGDX และ pi
- [[pi-agent]]: Coding agent ที่เน้นความเรียบง่ายและขยายความสามารถได้สูง
- [[terminus-agent]]: Agent ต้นแบบที่ใช้แค่ tmux และ keystrokes
- [[terminalbench]]: ระบบประเมินประสิทธิภาพของ coding agents

## Key Concepts

- [[tree-structured-sessions]]: การเก็บประวัติ session แบบกิ่งก้านแทนที่จะเป็นรายการแนวตั้ง
- [[clanker-slop]]: คำเรียกขยะหรือ spam ที่สร้างโดย AI ปริมาณมาก
- [[malleable-tools]]: แนวคิดเครื่องมือที่ผู้ใช้สามารถปรับแต่งโครงสร้างภายในได้เองอย่างรวดเร็ว

## See also

- [[claude-code]] — จุดเริ่มต้นและคู่เทียบของ pi
- [[harness-engineering]] — แนวคิดการสร้าง "นั่งร้าน" สำหรับ agent
- [[vibecoded-slop]] — แนวคิดใกล้เคียงกับ Clanker Slop
