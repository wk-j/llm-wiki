---
title: Cloud Agents
type: concept
tags: [ai, agents, cloud-agents, infrastructure, harness, durable-execution, orchestration]
created: 2026-06-05
updated: 2026-06-05
sources: [What we’ve learned building cloud agents.md]
---

# Cloud Agents / Agent ที่รันบนคลาวด์

**Cloud agent** คือ coding agent ที่รันบน VM ในคลาวด์ ไม่ใช่บน laptop ของ user. agent แต่ละตัวมี environment, dependency, network access ของตัวเอง, ทำงานขนานกันได้ทีละหลายตัว, รันแบบไม่มีคนเฝ้า (unattended), และรับงานยาวเป็นชั่วโมงหรือเป็นวันได้.

หน้านี้สรุปจากบทเรียนหนึ่งปีของ [[cursor|Cursor]] ในบล็อก [[what-weve-learned-building-cloud-agents|What We've Learned Building Cloud Agents]] (โดย [[josh-ma|Josh Ma]], 2026-06-02).

## แก่นความคิด — ไม่ใช่ "local agent บน server"

ความเข้าใจผิดตอนแรกคือคิดว่า cloud agent เป็นแค่การเอา local agent ไปวางบน server. ความจริงคือมันกลายเป็นการ **สร้าง operating layer รอบตัว agent** — ทุกอย่างที่ local agent ได้ฟรีจาก laptop ต้องประกอบขึ้นใหม่บนคลาวด์.

> "the work increasingly looks less like porting a local agent to a server and more like building an operating layer around it."

local agent ยืม environment, network, credential ที่ทำงานอยู่แล้วบนเครื่อง user. cloud agent ไม่มีอะไรให้ยืม — ต้องสร้าง environment, จัดการ durability เอง, และดูแล conversation state ข้ามหลายเครื่องเอง.

## เสาหลัก 4 อย่างของ cloud agent

### 1. Environment คือตัวสินค้า

ปัจจัยใหญ่สุดที่กำหนดคุณภาพงานคือการมี [[agent-development-environment|development environment ครบเหมือน developer จริง]]. อาการพังไม่ใช่ crash แต่เป็นคุณภาพงานตกแบบเงียบ ๆ — แล้วคนไปโทษ model. พอ model ฉลาดขึ้น environment กลายเป็นตัวตัดสินว่า model จะทำงานได้เต็มศักยภาพไหม. สุดท้ายต้องสร้าง "enterprise IT สำหรับ agent" — secret redaction, network policy, credential management.

### 2. Durable execution

cloud agent รันใน VM ที่อาจเจอ inference ล่ม, pod ถูกแทนที่, node ดับ. Cursor ย้ายจาก work-stealing ที่เปราะ ("one 9") ไปใช้ [[temporal|Temporal]] เพื่อ [[durable-execution|durable execution]] — ดัน reliability เกิน "two 9s", รองรับ 50M+ action/วัน. **40%+ ของ PR ใน Cursor มาจาก cloud agent.** เกี่ยวพันกับ [[long-running-agents|long-running agent]] โดยตรง.

### 3. แยก agent / machine / conversation state ออกจากกัน

cloud agent ไม่ใช่ loop เดียวบนเครื่องเดียวอีกแล้ว — มันอาจ spawn subagent กระจายหลายเครื่อง, subagent อาจอยู่นานกว่า parent. วิธีรับมือคือ decouple สามอย่าง: **agent loop** (อยู่ใน Temporal ไม่ใช่บน VM → จัดการ pod อิสระ, ใช้ readonly/prewarmed VM ได้), **machine state**, และ **conversation state** (storage แบบ append-only ที่ stream + rewind ได้เวลา retry).

### 4. รู้จักหลบให้ agent ทำงาน

harness ต้องตัดสินตลอดว่าอะไรควร deterministic อะไรควรยกให้ agent. แนวโน้มคือ **ย้าย logic จาก harness ไปเป็น tool ที่ agent คุมเอง** เมื่อ model ฉลาดขึ้น (เช่น CI Autofix เปลี่ยนจาก harness ดึง log → ให้ GitHub CLI ไปเลย). harness ไม่หาย แต่เนื้อในเปลี่ยน. และ cloud agent ต้อง prompt ให้ **autonomous กว่า local** เพราะ cost ของการบล็อกสูง — agent อาจนั่งรอ permission เป็นชั่วโมงโดยไม่มีใครเห็น. ดู [[coding-harness]] และ [[orchestration-tax]].

## ทิศทางถัดไป: self-healing

เป้าหมายคือก้าวพ้นทางเลือก binary ระหว่าง "จูงมือ" กับ "หลบให้ทำเอง" — ให้ agent มี tool เข้าใจระบบรอบตัวมัน รายงานเองเมื่อ secret หาย/network บล็อก แล้วแก้เอง. ดู [[self-healing-environments]].

## เทียบกับ pattern อื่นในวิกิ

- **[[long-running-agents]]** — 5 pattern ของ Google Cloud (checkpoint-and-resume, delegated approval ฯลฯ) เป็นมุม "ออกแบบ agent ให้อยู่ข้ามวัน"; cloud agent ของ Cursor เป็นมุม "สร้าง infra จริงให้ pattern พวกนั้นรันได้"
- **[[orchestration-tax]]** — คนคือคอขวด serial ในระบบ agent ขนาน; cloud agent ยิ่งทำให้ agent ขนานเยอะ คอขวดที่ review/merge ยิ่งชัด
- **[[subagent-patterns]]** / **[[agent-swarm]]** — cloud ทำให้ subagent กระจายข้ามเครื่อง/ข้าม pod ได้จริง

## See also

- [[what-weve-learned-building-cloud-agents]]
- [[cursor]]
- [[josh-ma]]
- [[temporal]]
- [[agent-development-environment]]
- [[durable-execution]]
- [[self-healing-environments]]
- [[long-running-agents]]
- [[coding-harness]]
- [[orchestration-tax]]
- [[subagent-patterns]]
