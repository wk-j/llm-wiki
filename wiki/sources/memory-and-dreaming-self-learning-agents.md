---
title: "Memory and dreaming for self-learning agents"
type: source
tags: [anthropic, agent-memory, dreaming, managed-agents, multi-agent, self-learning]
created: 2026-05-09
updated: 2026-05-09
sources: [Memory and dreaming for self-learning agents.md]
---

# Memory and dreaming for self-learning agents / Memory กับ Dreaming สำหรับ agent ที่เรียนรู้ตัวเอง

Talk จาก **Mahes** (Product Manager ทีม Platform ของ [[anthropic|Anthropic]]) เปิดตัว 2 อย่างพร้อมกันใน Claude Managed Agents API:

1. **Memory** — ระบบ "ความจำ" ที่เปิด public beta ก่อนหน้านี้ไม่กี่สัปดาห์ มอง memory เป็น **file system** ที่ Claude จัดการเองด้วย bash/grep
2. **Dreaming** — ของใหม่ที่เพิ่งปล่อย research preview วันนี้ (2026-05-09): batch process ที่รัน "นอก session" คอยอ่าน transcript แล้วอัปเดต memory store ให้สด

แก่นของ talk คือคำว่า **self-learning agents** — agent ที่เก่งขึ้นเองจากงานที่ผ่านมา ไม่ใช่แค่จากการ retrain โมเดล

## ทำไม Anthropic ลงทุนกับ memory เป็น primitive ตัวต่อไป

Mahes ไล่ลำดับ primitive ที่ Anthropic ปล่อยมาแล้ว:

- **[[model-context-protocol|MCP]]** — เปิดให้ agent ต่อ tool/data ภายนอก
- **Harness** — Claude Code, Agent SDK
- **Skills** (ต.ค. 2025) — ให้ agent หยิบความสามารถใหม่จาก agent อื่น/มนุษย์ มาใช้ได้

ทุกตัวข้างบนช่วยให้ agent ทำงานยาวขึ้นและกว้างขึ้น แต่ยังเหลือเรื่องที่ยังแก้ไม่ตก คือ **continuous self-learning** กับ **context management ในงานยาวๆ** — ตรงนี้คือที่ memory เข้ามา

agent ที่มี memory จะเรียนได้ 3 อย่าง:

1. **เรื่อง task ที่ทำ** — success criteria, ความผิดที่เคยเกิด, กลยุทธ์ที่ใช้ได้/ใช้ไม่ได้
2. **เรื่องสภาพแวดล้อม** — codebase, ไฟล์ที่ต้อง keep up to date
3. **เรื่อง agent ตัวอื่น** — เห็นว่า agent ตัวอื่นในระบบเดียวกันเจออะไร เอามารวมในความจำตัวเอง

ข้อ 3 คือสิ่งที่ Mahes บอกว่าตื่นเต้นที่สุด เพราะ multi-agent system ขนาดใหญ่ (swarm) จะค่อยๆ สร้าง "world model" ของตัวเองได้

## Requirement ที่ตกผลึกจากการคุยกับลูกค้า

### 1. Memory ต้อง "maximize intelligence by default"

ตอนทำ [[claude-code|Claude Code]] ปีกว่าก่อน Anthropic ปล่อย CLAUDE.md เป็น memory เวอร์ชันแรก — agent ทิ้ง note ให้ตัวเอง บางทีผู้ใช้ก็เขียนใส่ด้วย ต่อมามี `memory tool` ใน SDK ที่เป็น tool call แบบ well-specified

แต่พอ agent เก่งขึ้น Anthropic เลือกถอย — ปล่อยให้ Claude ตัดสินใจเอง อย่าออกแบบ harness แน่นเกินไป ใช้แนวเดียวกับ skills:

> เรารู้ว่า agent จัดการ virtual environment + file system ของตัวเองได้ ทำไมจะทำแบบเดียวกันกับ memory ไม่ได้?

ผลคือ Memory ใน Managed Agents = **ลำดับชั้นของไฟล์** ที่ Claude อ่าน/เขียนผ่าน `bash` + `grep` — ไม่ใช่ DB หรือ vector store ดู [[agent-memory-filesystem]]

ที่ทำได้ก็เพราะ [[claude-opus-4-7|Opus 4.7]] เป็น state-of-the-art ใน file-system-based memory:
- ตัดสินได้ดีว่าอะไรควรจดลง memory
- แตกไฟล์เป็นกี่ไฟล์ดี
- จัด structure ใน file system ยังไงให้ใช้ต่อได้

### 2. ต้องสเกลกับ multi-agent system

ใน Anthropic เองมี agent หลักร้อยถึงหลักพันรันพร้อมกันใน environment เดียว แชร์ memory state เดียวกัน คุณสมบัติที่ตามมา:

- **Permission scopes** — agent หนึ่งตัวอ่าน/เขียน memory store ได้ไม่เท่ากัน เช่น org-wide knowledge เป็น **read-only** (runbook, SLO guideline) ส่วน working memory เฉพาะทีมเป็น **read-write**
- **Concurrency** — Anthropic ใช้ **optimistic concurrency** ผ่าน content hash: ก่อน agent จะเขียนทับ memory ก็เช็ค hash ก่อนว่า state ตรงกับที่อ่านมาไหม ถ้าไม่ตรงแปลว่ามี agent อื่นเพิ่งเขียน — กัน clobber กันเอง

### 3. Developer/enterprise control

จากการคุยกับลูกค้า สิ่งที่ถูกขอมากที่สุดคือ **version history**:
- Audit log ครบทุกครั้งที่ memory อัปเดต
- Attribution: agent ตัวไหน เซสชันไหน เวลาไหน เปลี่ยนอะไร
- ให้ agent เองก็มองเห็น audit log ได้ในอนาคต

อีกข้อคือ **standalone API** ที่ portable — ลูกค้าหลายเจ้ามี pipeline ของตัวเองอยู่แล้ว เช่น scan PII ก่อนเขียน memory หรือ clone memory ออกไประบบอื่น Anthropic เลยไม่ขัง memory ไว้ใน managed agents เท่านั้น

## 3 layer ของ frontier memory system

Mahes สรุปว่าระบบ memory แบ่งเป็น 3 ชั้น:

| Layer | คืออะไร |
|---|---|
| **Storage** | ข้อมูลถูกเก็บที่ไหน metadata อะไรบ้าง |
| **Structure & content** | format ของ memory (เลือก file system + skills เป็น procedural memory) |
| **Process** | อัปเดตเมื่อไหร่ อะไร trigger source อะไร |

Memory API ครอบ 2 ชั้นแรก แต่ชั้น **process** ยังขาด — agent แต่ละตัวมอง memory จากมุมตัวเอง ไม่เห็น pattern ข้าม session ทำให้:

- session ใหม่พลาดสิ่งที่ session อื่นเคยเรียนแล้ว
- agent ต่างตัวทำผิดเหมือนๆ กันโดยไม่รู้ว่าเป็น pattern
- memory store ใหญ่ไม่มีใคร curate ให้สด

ตรงนี้คือที่ **[[dreaming|Dreaming]]** เข้ามา

## Dreaming คืออะไร

> **Dreaming** = batch async process ที่อ่าน transcript ของ agent หลายตัวจากช่วงเวลาที่ผ่านมา แล้วผลิต memory state ใหม่ที่จัดระเบียบและ verified

เปิด research preview วันนี้ใน Managed Agents API trigger ได้ 2 แบบ:

1. **Cron-based** — ตั้งให้รันเป็นรอบใน console/API
2. **Event-based** — เช่น พอ agent ทำ task เสร็จและกำลัง spin down ก็เรียก dreaming เพื่อ commit สิ่งที่เรียนรู้กลับเข้า memory

Output ของ dreaming คือ **diff** บน memory store จะ apply ทันทีหรือให้คน review ก่อนก็ได้

ผลที่ลูกค้าทดสอบ: **Harvey** (legal AI) เปิด dreaming บน legal benchmark ของตัวเอง task completion rate ขึ้น **6x** ในหนึ่ง scenario

### ทำไม dreaming ดีกว่าให้ agent อัปเดต memory เอง

1. **Out of band** — ไม่อยู่ใน hot path ของ session ใดๆ ไม่เพิ่ม latency
2. **เห็นภาพรวมข้าม agent** — agent เดี่ยวเห็นแค่ context ตัวเอง dreaming อ่าน transcript หลายตัวพร้อมกันได้ จับ pattern ที่ตัวเดียวมองไม่เห็น
3. **Discrete objective** — Mahes ย้ำว่า agent ทำงานดีที่สุดเมื่อ objective ชัด แยก "memory quality" ออกจาก "task completion" ทำให้ทั้งสอง objective ไม่กลืนกัน
4. **Scale ผ่าน compute** — เปรียบเหมือน test-time compute ของ thinking model: ใส่ token เพิ่มเข้าไปจัด memory เลย amortize ค่าจัดข้ามทุก agent ที่อ่าน

อีกมุมที่ใช้อธิบาย: dreaming = **search index** ที่จ่ายต้นทุนจัด index ครั้งเดียวล่วงหน้า แล้ว agent ปลายน้ำทุกตัวก็ใช้ index นั้นได้ถูกๆ

## Demo: SRE agent

Demo ที่ Mahes โชว์เป็น SRE agent (site reliability):

- มี alert เข้ามา → spin up agent → agent มี memory store 3 อัน
  - **org-wide knowledge** (read-only, runbook + SLO)
  - **SRE memory** (read-write, working memory ทีม)
  - **codebase memory**
- alert P1 จาก dispatch service เข้ามา → agent ตัวที่ 1 ไป investigate CPU, traffic, recent PRs แล้วเขียน note ลง SRE memory
- ไม่กี่นาทีต่อมา alert เด้งซ้ำ → agent ตัวที่ 2 spin up เห็น note ของตัวที่ 1 ทันที — short-circuit การ investigate ที่ซ้ำซ้อน
- ใน UI มี version history ครบ ดูได้ว่า agent ตัวไหนเขียนเมื่อไหร่ พร้อม precondition hash

จากนั้นกด **Dreaming job** บนหน้า console:
- เลือก memory store + ช่วงเวลา (เช่น 7 วัน)
- ระบบ spawn dreaming session ที่มี sub-agent หลายตัวอ่าน transcript ทั้งหมด
- ผลลัพธ์เป็น diff หลายไฟล์:
  - **อัปเดต** dispatch latency note: เห็น pattern ว่า alert ลั่น "ทุก 60 วินาที" หลัง CPU spike → สรุปว่ามี retry logic ผิดที่ agent เดี่ยวๆ ไม่เคยเห็น pattern นี้
  - **Dedup** entry ซ้ำ 5 entry → รวมเหลือ 1
  - **ลบ** entry ที่ stale แล้ว
  - **Verify** entry ที่ยังถูกต้อง — ติด tag verification + เวลา ให้ agent วันถัดไปไว้ใจได้

## ภาพสุดท้าย: memory + dreaming = frontier memory system

| | Memory API | Dreaming |
|---|---|---|
| โหมด | real-time, in-session | batch, out-of-band |
| มุมมอง | per-agent | cross-agent |
| เป้าหมาย | task completion | memory quality |
| Trigger | inline tool call | cron / event |
| ผลลัพธ์ | อ่าน/เขียนทันที | diff ที่ apply กับ memory store |

Mahes ปิดท้ายว่า ปีหน้า agent จะรันยาวเป็นวันๆ — memory คือสิ่งที่ทำให้สิ่งนั้นเป็นไปได้

## Quotes

> "Why can't we go the same direction with memory? Memory in Cloud Managed Agents models memory as a file system to Claude — a series of files with a specific hierarchy and format that Claude can manage and update on its own."

> "Dreaming is a process that looks for patterns and mistakes across your recent agent sessions and their transcripts and automatically produces organized and up-to-date memory content."

> "The ultimate goal of dreaming is continuous self-learning and self-improvement where the next day's agents automatically get better based on the learnings and the work of the previous day's experience."

## See also

- [[dreaming]]
- [[agent-memory-filesystem]]
- [[self-learning-agents]]
- [[claude-managed-agents]]
- [[harvey-ai]]
- [[anthropic]]
- [[claude-opus-4-7]]
- [[hybrid-memory]] — Mercury's parallel approach
- [[mercury]]
- [[memory-decay]]
- [[memory-drift]]
- [[selective-injection]]
- [[model-context-protocol]]
