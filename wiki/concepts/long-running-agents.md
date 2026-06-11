---
title: Long-running Agents / Agent ที่อยู่ข้ามวัน
type: concept
tags: [ai, agents, long-running, architecture, memory, orchestration]
created: 2026-04-23
updated: 2026-04-23
sources: [google-cloud-long-running-agent-patterns.md]
---

# Long-running Agents / Agent ที่อยู่ข้ามวัน

Agent ส่วนใหญ่ที่เราคุ้นเคย — Claude Code, ChatGPT, Cursor — คือ **agent สั้น ๆ** คุยหนึ่ง session จบ ปิด process ทิ้ง state หาย แต่ workload จริงของบริษัทหลายอย่างไม่จบใน session เดียว เช่น เคลม insurance 5000 ชิ้นที่ต้องไล่สัมภาษณ์ประกัน, sales sequence ที่ส่ง email ต่อเนื่องหนึ่งสัปดาห์, reconcile ยอดเงินข้าม 4 ระบบข้ามคืน — งานพวกนี้ใช้เวลาเป็นชั่วโมง เป็นวัน หรือเป็นสัปดาห์

**Long-running agent** คือ agent ที่ออกแบบมาให้ *อยู่ข้ามวัน* state ไม่หายเวลา idle, resume ต่อได้หลังค้างหยุด, มี memory ข้าม session, ทน failure ได้โดยไม่ต้องเริ่มจากศูนย์

หน้านี้สรุป 5 pattern ที่ [[google-cloud-long-running-agent-patterns|Addy Osmani และ Shubham Saboo เสนอในบล็อก Google Cloud]] (2026-04-22) ประกาศพร้อม Cloud Next '26 ที่ [[gemini-enterprise-agent-platform|Agent Runtime]] ของ [[google-cloud|Google Cloud]] เปิดให้ agent อยู่ได้ถึง **7 วัน** — แต่ pattern เองไม่ขึ้นกับ Google ใช้กับ stack ไหนก็ได้ถ้า platform รองรับ

## ภาพรวม — ทำไมต้องคิดใหม่

Agent สั้น ๆ ถูกเขียนเป็น **request handler** รับ input, คิด, ตอบ, จบ state ตายพร้อม process ถ้าต้องจำอะไรข้าม session ก็เก็บลง DB แล้วโหลดใหม่ตอน turn ถัดไป

ปัญหาคือพอ workflow ยาว หลายชั่วโมง หลายวัน ทุกครั้งที่ reload จาก DB เรา **เสีย reasoning chain** (สายเหตุผลที่ agent สร้างไว้), **soft signal** (ข้อสังเกตระหว่างทางที่ไม่ได้บันทึกเป็นข้อมูล), กับ **confidence gradient** (ระดับความมั่นใจที่ทำให้การตัดสินใจก่อนหน้าดูสมเหตุสมผล) reload มาได้แค่ข้อเท็จจริงดิบ แต่ "ทำไมถึงเลือกแบบนี้" หายไปหมด

แก้ด้วยการเปลี่ยนมุม — **ปฏิบัติกับ agent เหมือน long-running server process** ไม่ใช่ request handler checkpoint ความคืบหน้า, จัดการ failure บางส่วน, ทำให้ idempotent — เหมือนตอนเขียน data pipeline ที่ต้อง process ล้าน record ไม่ได้ต่างจาก engineering pattern ที่เราใช้อยู่แล้ว เปลี่ยนแค่ subject จาก `data row` เป็น `agent decision`

มุมนี้ตรงกับสิ่งที่ [[cursor|Cursor]] เจอจริงตอนทำ [[cloud-agents|cloud agent]] — agent loop ที่อยู่ยาว ๆ คือ distributed-system workload ตัวหนึ่ง. Cursor เลยย้ายไปใช้ [[temporal|Temporal]] เพื่อ [[durable-execution|durable execution]] แทนการสร้าง durability primitive เอง ดู [[what-weve-learned-building-cloud-agents]]

## Pattern 1: Checkpoint-and-Resume

**เหมาะกับงานประเภทไหน** — งานที่เป็นชุดยาว ๆ เช่น process document 500 ไฟล์, ส่ง email 2000 ฉบับ, reconcile transaction 50000 record

**กลไก** — agent เขียนความคืบหน้าลง sandbox filesystem เป็นระยะ พอ crash หรือ error ระหว่างทาง resume ได้จากจุดเดิม ไม่ใช่เริ่มใหม่ทั้งหมด

Addy ให้ตัวอย่างโค้ด ADK — batch ละ 50 document ถึง save checkpoint ครั้งหนึ่ง ประกอบด้วย `last_processed` index, `partial_results`, และ timestamp จุดสำคัญคือ **เลือก granularity (ความถี่) ให้พอดี** — save ทุก document เปลือง I/O, save แค่ตอนจบเสี่ยงเสียงานเยอะถ้าพัง เลข 50 ไม่ใช่เลขมหัศจรรย์ ขึ้นกับว่างานหนึ่งชิ้นแพงแค่ไหน

**ได้อะไร** — ทนต่อ failure, คืน progress ได้โดยไม่เสียงาน และ (สำคัญไม่แพ้กัน) **audit trail** เพราะ checkpoint ที่เก็บไว้คือหลักฐานว่า agent ทำอะไรถึงไหน

## Pattern 2: Delegated Approval (Human-in-the-Loop)

**เหมาะกับงานประเภทไหน** — workflow ที่มี approval gate เช่น "agent ร่าง contract เสร็จ รอมนุษย์ review ก่อนส่ง" "agent เสนอ bid รอ manager อนุมัติก่อน commit"

**ปัญหาของ HITL แบบเดิม** — ตอน agent ขอ approval ส่วนใหญ่ทำแบบนี้: serialize state เป็น JSON → webhook ไปหา human → รอ → สักพัก human ตอบกลับ → agent deserialize → พยายาม rehydrate context เดิม

ปัญหา:
- JSON เก็บ **reasoning context ที่ implicit ไม่ได้** (pattern, hesitation, confidence) — พอ serialize เหลือแต่ข้อมูลดิบ
- notification ไปปะปนกับ alert 50 อย่างใน Slack/email — คนไม่เห็น
- กว่ามนุษย์จะตอบ ผ่านไป 8 ชั่วโมง context ใน agent พังไปหมดแล้ว

**กลไกของ long-running** — agent **หยุดในที่** (pause in place) reasoning chain, working memory, tool call history, pending action ยังอยู่ครบใน process ไม่ได้ถูก serialize ออก ช่วงรอ human agent ใช้ compute เป็น 0 (ไม่มี token cost) พอ human ตอบ agent resume แบบ sub-second ต่องานเดิมทันที

ทีม Google เสริม **Mission Control** เป็น inbox ที่จัด notification เป็น 3 กล่อง ("Needs your input" / "Errors" / "Completed") ใช้กับ fleet หลายสิบ agent พร้อมกันได้โดยไม่หลงว่าตัวไหนต้องการอะไร

**ได้อะไร** — HITL ที่ไม่เสีย context ระหว่างรอ + operational UX ที่ scale ได้เกิน 1 agent

## Pattern 3: Memory-Layered Context

**ภาพรวม** — agent ที่อยู่ 7 วันต้องจำได้มากกว่าแค่ session ปัจจุบัน ต้องจำ preference ของ user เมื่อสัปดาห์ก่อน, จำ context ระดับองค์กรที่คุย session เดียวไม่ครอบคลุม

Google เสนอสองชั้น:

- **Memory Bank** — ความจำระยะยาว สร้างจาก conversation อัตโนมัติ จัดเป็นหัวข้อ (topic-organized) เหมือนห้องสมุด
- **Memory Profiles** — working memory ความเร็วสูง สำหรับ detail ที่ต้องเอามาใช้บ่อย ๆ ด้วย accuracy สูง เหมือน cache

เทียบกับความจำของมนุษย์ง่าย ๆ — Memory Bank = ความทรงจำระยะยาว, Memory Profiles = สิ่งที่อยู่ในหัวตอนนี้

### ปัญหาใหม่ที่คนไม่คิดถึง — Memory Drift

พอ agent สะสม memory จาก interaction ต่อเนื่อง **พฤติกรรมของมันจะเริ่มถูก shape โดย experience ไม่ใช่แค่ prompt กับ code เท่านั้น**

ตัวอย่างปัญหาที่ Addy ชี้ — สมมติ user 3–4 คนทำ shortcut แปลก ๆ (ข้าม approval step) agent เห็นว่า "อ๋อ shortcut นี้ยอมรับได้" แล้วเริ่มแนะนำ shortcut กับ user คนอื่นที่ไม่ควรใช้ — เกิด **drift** ที่ไม่ได้อยู่ใน prompt ไม่ได้อยู่ใน code แต่อยู่ใน memory layer

ยิ่งถ้า agent หลายตัวเขียน/อ่าน memory pool เดียวกัน ก็เกิด **cross-agent data leakage** — workflow A เห็นข้อมูล workflow B โดยไม่ตั้งใจ

### ทางแก้ — ใช้ governance แบบ microservice

Google เสนอ triad:
- **Agent Identity** — agent แต่ละตัวมี identity แบบ cryptographic เหมือน service account scope ได้ว่าแตะ memory bank ไหน tool อะไรได้บ้าง
- **Agent Registry** — service discovery agent ไหน active, รัน prompt/code version อะไร, state ปัจจุบันเป็นยังไง
- **Agent Gateway** — API gateway ตรงกลางระหว่าง agent กับ memory + tool ถ้า agent พยายามเขียน PII ลง long-term memory → Gateway block

หลักคิด: **อย่าให้ agent write memory ได้ตามใจ** governance memory เหมือน governance microservice

**ได้อะไร** — audit ได้ว่า agent จำอะไร, drift ตรวจจับได้, เปลี่ยน policy ได้โดยไม่ต้อง redeploy agent ทุกตัว

> คำถามที่ต้องตั้งตั้งแต่ day one ไม่ใช่แค่ "agent ทำอะไรอยู่" แต่คือ **"agent จำอะไร แล้ว memory นั้นเปลี่ยน behavior ยังไง"**

จุดนี้ตรงกับ [[agent-runtime-untrusted|หลักคิด agent-runtime-untrusted ของ OWASP APTS]] — policy ต้องอยู่**นอก** model ถึงจะ audit/test/change ได้ การฝัง policy ใน prompt หรือฝังใน code agent คือ anti-pattern ทั้งคู่

## Pattern 4: Ambient Processing

**เหมาะกับงานประเภทไหน** — งานที่**ไม่มี** human interaction เป็นหลัก เช่น content moderation, fraud detection, log anomaly detection — เฝ้า event stream แล้วทำงานในเบื้องหลัง

**กลไก** — agent เสียบตรงเข้ากับ BigQuery table / Pub/Sub stream รันต่อเนื่องเป็นวัน ๆ process event ตามมา maintain state ของตัวเอง (เช่น "trend ของ content violation 24 ชม.ล่าสุด"), escalate เมื่อเจอ edge case

**Decision หลักทาง architecture** — อย่า hardcode policy ลงในตัว agent ให้ **externalize ผ่าน Agent Gateway** พอ policy เปลี่ยน update Gateway ที่เดียว fleet ทั้งหมดเห็นกฎใหม่ทันที ไม่ต้อง redeploy agent ทุกตัว

ตรงนี้คือจุดเดียวกับที่ [[auto-mode|Auto mode ของ Claude Code]] ทำกับ tool call — classifier ที่อยู่นอก model ตัดสินใจ approve/reject ไม่ฝังใน prompt

**ได้อะไร** — ambient agent ทำงาน 24/7 ได้โดยไม่ต้องรอมนุษย์ และ policy change ไม่ต้อง touch code

## Pattern 5: Fleet Orchestration

**เหมาะกับงานประเภทไหน** — workload ที่ต้องการ agent หลายตัวเชี่ยวชาญคนละอย่าง เช่น sales prospecting = Lead Research Agent → Outreach Agent → Scoring Agent → Follow-up Agent

**กลไก** — coordinator agent ดูภาพรวม, delegate ให้ specialist agent แต่ละตัวรันแยก process แยก container แต่ละ specialist มี:
- Agent Identity เฉพาะตัว (scope ว่าเข้า memory/tool ไหนได้บ้าง)
- policy ผ่าน Agent Gateway (Outreach Agent เข้า data การเงินที่ Scoring Agent ใช้ไม่ได้)
- entry ใน Agent Registry (track version ต่างหาก)

Coordinator ดูแล global state + handoff เป็น classic **coordinator/worker pattern** ที่ระบบกระจายใช้มาหลายสิบปี ใหม่ตรงที่ ADK มี graph-based declarative workflow ให้เขียน coordination logic แบบ declarative แทน imperative

**ได้อะไร** — update specialist ได้อิสระ deploy Scoring Agent version ใหม่โดยไม่ touch Outreach Agent ถ้า deploy พัง ก็พังเฉพาะตัวนั้น ไม่ cascade เพราะอยู่คนละ container

### เทียบกับ subagent ที่เล็กกว่า

Pattern นี้คือรูปแบบขยายของ [[subagent-patterns|subagent patterns]]:
- **Parallel fan-out** ใน Claude Code = ลูกที่อยู่ใน session เดียว รันขนานสั้น ๆ
- **Fleet orchestration** = ลูกที่อยู่คนละ process คนละ container รันแยกกันวันต่อวัน

ต่างกันเรื่อง scope ของ lifetime กับ isolation — pattern เดียวกันจุดยืนต่างกัน

ขยายขึ้นไปเป็น [[agent-swarm]] (Kimi K2.6 scale 100–300 agent) ก็อยู่ในสายเดียวกัน — scale-out มากกว่า scale-up

## เทียบ 5 pattern

| Pattern | ปัญหาที่แก้ | กลไกหลัก |
|---|---|---|
| Checkpoint-and-Resume | งานยาวเกิน session เดียว, ทน failure | save state เป็น batch ลง filesystem |
| Delegated Approval | HITL ที่เสีย context ระหว่างรอ | pause in place, zero compute ขณะรอ |
| Memory-Layered Context | จำข้าม session + กัน memory drift | Memory Bank + Profiles + governance triad |
| Ambient Processing | งานไม่มี human-trigger | BigQuery/Pub/Sub connector + policy-from-Gateway |
| Fleet Orchestration | หลาย specialist agent ทำงานร่วมกัน | coordinator + container per specialist |

## เริ่มตรงไหนดี

Addy ให้คำถามตัดสินใจง่าย ๆ:

> **งานยาวที่สุดแบบที่ agent ต้องทำต่อเนื่องไม่ขาดคือนานแค่ไหน?** เป็นนาที → ไม่ต้องใช้ long-running. เป็นชั่วโมงหรือเป็นวัน → pattern พวกนี้คือจุดเริ่ม

**Compose กันได้** ระบบ compliance ตัวหนึ่งอาจใช้ครบทั้ง 5 — Checkpoint-and-Resume สำหรับ process document, Delegated Approval ตอน review gate, Memory-Layered Context สำหรับความรู้ข้าม case, Fleet Orchestration ประสาน specialist — pattern ไม่ได้แทนกัน แต่ stack ต่อกัน

## See also

- [[google-cloud-long-running-agent-patterns]]
- [[gemini-enterprise-agent-platform]]
- [[google-cloud]]
- [[cloud-agents]]
- [[durable-execution]]
- [[temporal]]
- [[what-weve-learned-building-cloud-agents]]
- [[orchestration-tax]]
- [[subagent-patterns]]
- [[agent-runtime-untrusted]]
- [[auto-mode]]
- [[agent-swarm]]
- [[advisor-strategy]]
- [[claude-code-session-management]]
- [[loop-engineering]]
