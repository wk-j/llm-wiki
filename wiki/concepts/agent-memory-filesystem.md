---
title: Agent Memory as File System
type: concept
tags: [agent-memory, anthropic, primitive, design-pattern]
created: 2026-05-09
updated: 2026-05-09
sources: [memory-and-dreaming-self-learning-agents]
---

# Agent Memory as File System / Memory ในรูปแบบ file system

แนวทางที่ [[anthropic|Anthropic]] เลือกสำหรับ memory ใน [[claude-managed-agents|Claude Managed Agents API]] (public beta, 2026-04 — 2026-05): **มอง memory เป็นลำดับชั้นของไฟล์** ที่ Claude อ่าน/เขียนเองด้วย `bash` กับ `grep` ไม่ใช่ vector store ไม่ใช่ DB schema ตายตัว ไม่ใช่ tool call ที่กำหนด parameter แน่น

## ที่มา: ถอย "harness" ออก ปล่อยให้ model จัดการเอง

Anthropic ลองมาแล้วหลายแบบ:

| รุ่น | รูปแบบ | ปัญหา |
|---|---|---|
| `CLAUDE.md` ใน [[claude-code\|Claude Code]] (~2024) | ไฟล์ markdown ไฟล์เดียว agent ทิ้ง note ให้ตัวเอง บางทีคนก็แก้ | จำกัดมาก เป็น early version |
| `memory tool` ใน SDK | tool call ที่ระบุ parameter + output format | constrain Claude เกินไป |
| **Memory ใน Managed Agents** (2026) | file system ที่ Claude จัดการเอง | — |

หลักการคือเดียวกับ skills: ให้ Claude เป็นคนตัดสินใจ structure เอง แทนที่ harness จะกำหนดให้

> เรารู้ว่า agent จัดการ virtual environment + file system ของตัวเองได้ ทำไมจะทำแบบเดียวกันกับ memory ไม่ได้?
> — Mahes, Anthropic Platform PM

## ทำไมเพิ่งจะทำได้ตอนนี้

[[claude-opus-4-7|Claude Opus 4.7]] (เปิดตัว เม.ย. 2026) เป็น state-of-the-art ใน file-system-based memory ในจุด 3 จุดที่จำเป็น:

1. **เลือก content** — ตัดสินได้ดีว่าอะไรควรจดลง memory
2. **เลือก granularity** — ควรแตกเป็นกี่ไฟล์
3. **เลือก structure** — จัด tree ใน file system ให้ตัวเองหรือ agent อื่นใช้ต่อได้

ทั้งหมดนี้ใช้ tool พื้นฐานที่ Claude เก่งอยู่แล้วจาก agentic coding คือ `bash` + `grep`

## คุณสมบัติสำคัญสำหรับ enterprise

ใน Managed Agents API มี property ที่ออกแบบมาเพื่อ multi-agent + production:

### Permission scopes

agent ตัวเดียวถือ memory store หลายอันได้ แต่ permission ต่างกัน เช่น SRE agent ใน demo ของ talk:
- **org-wide knowledge** — read-only (runbook, SLO guideline)
- **team SRE memory** — read-write (working memory)
- **codebase memory** — แล้วแต่งาน

### Optimistic concurrency

ถ้ามี agent หลายร้อยตัวเขียน memory store เดียวกันพร้อมกัน จะไม่ clobber กันเอง — แต่ละการเขียนแนบ **content hash** ของ state ตอนอ่าน ก่อน apply ระบบเช็คว่า hash ยังตรงไหม ถ้ามีคนเขียนแทรกไปก่อนจะ reject

### Version history + attribution

audit log ทุก write — agent ตัวไหน, session ไหน, เวลาไหน, แก้อะไร เปิดให้ทั้งคนและ agent ดูในอนาคต — กลายเป็น context เพิ่ม

### Standalone API

ลูกค้าหลายเจ้ามี pipeline ของตัวเอง เช่น scan PII ก่อนเขียน หรือ clone memory ออกระบบอื่น — Anthropic ไม่ขัง memory ไว้ใน managed agents เท่านั้น เปิด API ให้ทำของพวกนี้ได้นอก runtime

## 3 layer ของ frontier memory system

Mahes แบ่งระบบ memory เป็น 3 ชั้น:

| Layer | คืออะไร | Anthropic ใช้อะไร |
|---|---|---|
| Storage | ที่เก็บข้อมูล + metadata | managed cloud storage + audit log |
| Structure & content | format ของ memory | file system + skills (procedural memory) |
| Process | trigger/source ของ update | [[dreaming]] — เพิ่งเปิด preview 2026-05-09 |

Memory-as-filesystem ครอบ 2 layer แรก ส่วน [[dreaming]] เติม layer ที่ 3

## ผลที่ลูกค้ารายงาน

- **Rocketin** (knowledge agent ภายใน) — first-pass mistake ลด **90%** เพราะ agent ตัวใหม่ catch ความผิดของตัวก่อนหน้าได้ ตามมาด้วย token efficiency + latency ที่ดีขึ้น

## เปรียบเทียบกับแนวทางอื่น

- **[[hybrid-memory|Mercury Hybrid Memory]]** ([[ctrl-alt-zaid]]) — แยก Markdown สำหรับมนุษย์ ออกจาก structured substrate สำหรับเครื่อง
- **[[claude-code|Claude Code]] CLAUDE.md** — รุ่นแรกของแนวคิดนี้แต่ flat — ไม่มี permission scope, concurrency, audit log
- **[[google-cloud-long-running-agent-patterns|Google Memory-Layered Context]]** — ใน Gemini Enterprise Agent Platform แบ่ง Memory Bank + Profiles เป็น layer

## See also

- [[dreaming]]
- [[claude-managed-agents]]
- [[self-learning-agents]]
- [[claude-opus-4-7]]
- [[anthropic]]
- [[hybrid-memory]]
- [[mercury]]
- [[memory-and-dreaming-self-learning-agents]]
