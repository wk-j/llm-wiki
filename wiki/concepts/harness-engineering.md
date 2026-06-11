---
title: Harness Engineering
type: concept
tags: [ai, software-engineering, orchestration, education, curriculum]
created: 2026-04-18
updated: 2026-05-10
sources: [harness-engineering-panutat.md, llm-era-computer-engineering-nattee.md, alex-ker-harnesses-optimize.md, thclaws-announcement-panutat.md, Agent Harness Engineering.md]
---

# Harness Engineering / วิศวกรรม Harness

เมื่อ AI Agent เขียน code ได้ในระดับที่มนุษย์ "ตรวจ" หรือ "แนะนำ" ตามไม่ทัน สิ่งที่มนุษย์ควรสร้างคือ **harness** — ระบบครอบรอบ model หรือ agent หลัก เช่น prompt, tools, sandbox, hooks, memory, context policy, และ agent ตัวอื่นที่ช่วย review, test, audit แบบอัตโนมัติ แนวคิดสายไทยของ [[panutat-tejasen|Panutat Tejasen]] (2026) ใช้ภาพเปรียบเทียบว่า harness คือ "บังเหียน" ที่ช่วยคุมพลังของ LLM

> "เราต้องการเฉพาะส่วนสำคัญที่ทำหน้าที่ Harness คือเป็นบังเหียน ที่จะควบคุมเจ้าม้าป่า คือ LLM" — Panutat Tejasen, 2026

ในแหล่งหลัง ๆ คำว่า **harness engineering** ถูกใช้กว้างขึ้นด้วย [[vtrivedy|Vtrivedy]] และ [[addy-osmani|Addy Osmani]]: ไม่ใช่แค่ pipeline ของ review agent แต่คือ discipline ทั้งหมดของการออกแบบสิ่งรอบ model — prompt, tools, filesystem, sandbox, hooks, memory, context policy, subagent, observability, และ recovery path. สูตรคือ **Agent = Model + Harness**

## หัวใจสำคัญ: ม้าป่ากับบังเหียน

Panutat เปรียบเทียบ LLM เป็น **"ม้าป่า"** ที่มีพลังมหาศาลแต่ควบคุมยาก และ Harness คือ **"บังเหียน"** (Reins) ที่ทำให้เราสามารถสั่งการให้มันทำงานตามที่เราต้องการได้

### จาก LLM Wrapper สู่ Agentic Application (ยุคที่ logic 99% อยู่รอบตัว AI)
วิวัฒนาการของซอฟต์แวร์ AI แบ่งได้เป็นสองยุค:
1.  **LLM Wrapper:** โปรแกรมที่ทำหน้าที่เพียงส่งคำสั่ง (Prompt) ไปยัง API และแสดงผลลัพธ์ (ครอบ API เฉยๆ)
2.  **Agentic Application (Harness):** โปรแกรมซับซ้อนที่ควบคุมกระบวนการทั้งหมด logic ส่วนใหญ่ (99%) ของโปรแกรมประเภทนี้คือระบบ Harness ไม่ใช่ตัว Model (ดูตัวอย่างใน [[thclaws]])

## องค์ประกอบของ Harness (จาก thClaws)
จากการศึกษา [[claude-code]] ผ่านโปรเจกต์ [[thclaws]], Panutat ระบุส่วนประกอบสำคัญของ Harness ไว้ดังนี้:

- **Agentic Loop:** วงจรการทำงานที่ให้ AI คิดและทำซ้ำจนกว่าจะสำเร็จ
- **Tool Routing & Sub-agent Dispatch:** การส่งงานต่อให้เครื่องมือหรือ Agent ตัวรอง
- **Sandbox:** สภาพแวดล้อมที่ปลอดภัยสำหรับการรันโค้ดที่ AI เขียน
- **Context Compaction:** การจัดการหน่วยความจำ (Token) เพื่อให้ Agent ทำงานต่อเนื่องได้ยาวนาน
- **Agent Teams:** การจัดกลุ่ม Agent ให้ทำงานร่วมกันเป็นทีม

## องค์ประกอบของ Harness (จาก Addy Osmani)

Addy ขยายภาพนี้เป็น component taxonomy ที่ออกแบบย้อนจาก behavior:

- **Filesystem + Git** — durable state, workspace, worktree, rollback
- **Bash + Code Execution** — tool ทั่วไปที่ agent ใช้สร้าง action ใหม่เองได้
- **Sandbox + Permission Gate** — ให้รันได้โดยไม่เชื่อใจ runtime ของ agent
- **Memory + Search + MCP** — เติมความรู้ที่ไม่ได้อยู่ใน context หรือ training data
- **Context Management** — [[compaction]], tool-output offloading, [[progressive-disclosure]]
- **Long-Horizon Execution** — loop, planner/executor split, self-verification
- **Hooks + Middleware** — enforcement layer สำหรับ lint, test, destructive-command block
- **Observability** — logs, traces, cost, latency

**ได้อะไร:** harness engineering ในความหมายใหม่นี้คือการออกแบบ runtime ทั้งตัว ไม่ใช่แค่ prompt strategy

## ทิศทางใหม่: บังเหียนคือระบบหลังบ้าน (The Harness is the Backend)

ในปี 2026 เกิดแนวคิดใหม่จาก [[mf-piccolo]] ผู้สร้าง [[iii-triple-i]] ที่มองว่า Harness ไม่ควรเป็นเพียงโครงสร้างชั่วคราว (Scaffolding) ที่ครอบ AI ไว้ แต่ควรเป็นส่วนหนึ่งของสถาปัตยกรรม Backend โดยตรง

- **Collapse of Categories:** แทนที่จะมีระบบแยกสำหรับ Queue, State, และ Agent Orchestration ทุกอย่างถูกยุบรวมเหลือเพียง [[wtf-primitives|WTF Primitives]] (Worker, Trigger, Function)
- **Agent as a Worker:** ในแนวทางนี้ AI Agent คือ "Worker" ประเภทหนึ่งที่สามารถเรียกใช้ Function และจัดการ State ได้ด้วย Primitives เดียวกับโปรแกรมดั้งเดิม
- **Just-in-time Infrastructure:** Agent สามารถสร้าง Worker/Sandbox ใหม่ขึ้นมาใช้งานได้เองตามความต้องการในขณะรันงาน

การเปลี่ยนแปลงนี้ทำให้ Harness เปลี่ยนจาก "สิ่งแปลกปลอม" ที่มาครอบระบบเดิม กลายเป็นเนื้อเดียวกันกับโครงสร้างพื้นฐานของซอฟต์แวร์

## ปัญหาตั้งต้น

ข้อเสนอที่พบบ่อย: สอนนักศึกษาให้ "ตรวจงาน AI Agent" และ "แนะนำให้ AI เลือก Framework ที่ถูก" ฟังดูสมเหตุสมผล แต่ในทางปฏิบัติ:

- Framework / Library ที่ AI Agent เลือกใช้ **เกินความสามารถที่คนจะไปแนะนำ** — "มันรู้มากกว่าเรามาก" (คำของ Panutat)
- ถ้าพยายามแทรกแซงการเลือกของ agent ความเร็วที่ควรได้ **x10 จะกลายเป็น /100** เพราะคอขวดย้ายมาอยู่ที่คน
- งาน "แนะนำ" จึงให้ ROI (ผลตอบแทน) ติดลบ — ยิ่งคนรู้น้อยกว่า agent ยิ่งไม่ควรไปขวาง

## สิ่งที่ควรสอนแทน

ออกแบบและควบคุม AI Agent หลายตัวให้ทำงานประกอบกัน — นั่นคือ **Harness Engineering**:

| บทบาทของ Agent | หน้าที่หลัก |
|---|---|
| Code Review Agent | ตรวจ code quality, naming, architectural fit |
| Inspection / Validation Agent | เทียบ output กับ spec / acceptance criteria |
| Test Case Generator | สร้าง unit test และ integration test |
| E2E Testing Agent | รัน scenario จริงจากมุม user |
| Security Audit Agent | หาช่องโหว่ — OWASP, secret leak, supply-chain risk |

งานของมนุษย์ย้ายไปที่ **การออกแบบ harness** ไม่ใช่การไปแข่งกับ agent ตัวใน:

- เลือก agent ตัวไหนบ้างที่ต้องมีใน pipeline
- ออกแบบ prompt และ criteria (เกณฑ์ตัดสิน) ของแต่ละ agent
- วางลำดับการทำงาน (sequencing) และการส่งต่องาน (handoff)
- ตั้ง quality gate (ด่านตรวจคุณภาพ) และจุดที่ต้องให้คนดูก่อน ship

## Failure ต้องกลายเป็น Harness Ratchet

[[agent-harness-engineering]] เพิ่มหลักที่ทำให้ harness engineering เป็นวินัยระยะยาว: ทุกครั้งที่ agent พลาด ให้ถามว่า failure นี้ควรกลายเป็น rule, hook, test, lint, permission gate, หรือ reviewer subagent ตรงไหน ดู [[harness-ratchet]]

ถ้า agent ลบไฟล์ผิด → เพิ่ม pre-tool hook. ถ้า agent ลืม convention → เพิ่ม rule ที่สั้นและ trace กลับไปหาเหตุการณ์จริง. ถ้า agent ship code ที่ typecheck ไม่ผ่าน → ต่อ typecheck failure กลับเข้า loop

**ผลคือ:** harness ของทีมไม่ใช่ template สำเร็จรูป แต่เป็นประวัติ failure ของทีมที่ถูกทำให้เป็นระบบ

## ทำไมแนวทางนี้เข้าท่า

- **Scale งานตรวจสอบด้วย agent ไม่ใช่คน.** [[engineering-role-shift]] ชี้ว่างาน review / verification คืองานที่ขยายตัวในยุค AI — Harness Engineering คือวิธี scale งานนั้นโดยไม่ติดคอขวดที่คน
- **ตรงกับ pattern agent-verify-agent อื่นๆ.** เทียบได้กับ [[advisor-strategy]] (executor model เรียก advisor ที่จุดตัดสินใจยาก) แต่ harness แผ่ออกเป็น pipeline ถาวรที่มี agent หลายบทบาท ไม่ใช่การเรียกครั้งเดียว
- **แก้ blind spot ที่ [[llm-coding-pitfalls]] อธิบาย.** Karpathy ชี้ว่า AI เขียน code "ดูมั่นใจแต่ผิดเงียบๆ" — harness คือการทำให้การจับ failure mode (รูปแบบความผิดพลาด) เหล่านั้นเป็นระบบ
- **สอดคล้องกับ [[ai-orchestrator]].** วิศวกรยุคใหม่คือคนออกแบบ pipeline ของ agent หลายตัว ไม่ใช่ coder เดี่ยว
- **เคารพ [[judgement-vs-automation]].** ออกแบบ harness คืองานที่ต้องใช้วิจารณญาณและคาดเดาไม่ได้ — ยังเป็นพื้นที่ของคน ในขณะที่ coding ที่คาดเดาได้ถูก automate ไปให้ agent

## นัยทางหลักสูตร

- **อย่าสอนให้นักศึกษา "แข่ง" กับ AI Agent** ในเรื่องเลือก library หรือตรวจ code ด้วยตาเปล่า — ไล่ไม่ทัน และฝึกแล้วไม่ scale
- **สอน design skills ของ harness** — prompt engineering สำหรับ agent แต่ละบทบาท, criteria ของ security audit agent, การต่อ agent หลายตัวเป็น pipeline ที่เชื่อถือได้
- **ย้ายสกิลหลัก** จาก "เขียน code ให้ถูก" ไปที่ "ออกแบบระบบตรวจ-สอบที่ไว้ใจได้"

## ดูควบคู่กับ [[taste-paradox]] — สองปัญหาคนละ layer

Harness Engineering (Panutat) และ [[taste-paradox]] (Nattee) พูดถึงปัญหาเดียวกัน — การ review งาน Agent แบบ manual ทำไม่ไหว — แต่มองจากคนละจุด:

- **Panutat = *scope of reviewability*.** คนรู้น้อยกว่า Agent ไปแล้ว ตรวจ library choice ไม่ทัน → ตอบด้วย agent harness (แทนแรงคนด้วย agent ตัวอื่น)
- **Nattee = *origin of the reviewer*.** ต่อให้มี harness ก็ยังต้องมีคน *ออกแบบ* harness — คนนั้นต้องมี taste — taste มาจากการฝึกมือ — Agent ทำให้ข้ามการฝึกมือได้ จะปิด loop นี้ยังไง?

ไม่ได้ขัดกัน — harness ตอบคำถาม *"ตรวจยังไงให้ scale"* (technology); taste paradox ถามต่อว่า *"แล้วคนที่มี taste พอไปออกแบบ harness จะปั้นขึ้นมาจากไหน"* (pedagogy). ทั้งสองชิ้นต้องตอบไปพร้อมกันในหลักสูตรยุค Agent

## เชื่อมกับ [[subagent-patterns]] ของ Alex Ker

[[alex-ker|Alex Ker]] (2026-04-18) สรุป "pipeline" subagent pattern ไว้ว่า — push งานหนึ่งผ่าน role หลายๆ อันเป็นลำดับ (UX designer → architect → devil's advocate) **pattern นี้คือ pattern เดียวกันที่ Panutat เสนอ** เพียงแต่:

- Alex Ker เสนอในแง่ *เทคนิคการใช้งาน harness รายวัน* (ดูใน [[coding-harness]])
- Panutat เสนอในแง่ *สิ่งที่ curriculum ควรสอนแทนการตรวจ code ด้วยตา*

คนๆ เดียวกันใช้ pattern นี้ได้ทั้งสองบริบท — เครื่องมือในการทำงาน และหัวข้อที่ต้องสอน

## โยงกับกรอบ guides/sensors ของ Böckeler

[[birgitta-bockeler|Birgitta Böckeler]] (Thoughtworks) มองคำเดียวกันนี้จากมุม **ระบบ control**: harness = **guides (feedforward)** + **sensors (feedback)** ดู [[harness-guides-sensors]] ในกรอบนี้ pipeline ของ review agent ที่ Panutat เสนอจัดเป็น **inferential sensor** ตัวหนึ่ง — sensor ที่ใช้ model ตัดสินเชิงความหมาย ช้า/แพง/ไม่ deterministic ต่างจาก computational sensor (test, linter, type checker) ที่เร็วและแน่นอน

นัยที่ได้: harness ของจริงควรผสมทั้งสองชนิด อย่าฝาก quality gate ไว้กับ review agent (inferential) อย่างเดียว เพราะมันแพงและไม่แน่นอน — ของที่จับได้ด้วย computational sensor ควรให้ computational จับ แล้วเก็บ inferential ไว้ตรงที่ต้องใช้วิจารณญาณเชิงความหมายจริง ๆ

## ข้อสังเกตเพิ่มเติม (wiki)

ส่วนนี้เป็นการต่อยอดจากฝั่ง wiki ไม่ได้อยู่ในโพสต์ต้นทางของ Panutat:

- Harness มี cost (ต้นทุน) ของตัวเอง — token, latency, agent-coordination bug ทั้ง pipeline อาจ fail พร้อมกันได้หาก agent base model เหมือนกัน
- ประเด็นเปิด: ควรใช้ model ต่างชนิดใน harness เพื่อ diversity (ความหลากหลาย) ของ failure mode หรือไม่?
- ยังไม่มี tooling มาตรฐานสำหรับ harness orchestration — ยังเป็นพื้นที่ที่กำลังก่อตัว
- แนว [[flue|Flue]] และ Harness-as-a-Service ชี้ว่าตลาดอาจรวมตัวเป็น framework/runtime สำเร็จรูป แต่ domain policy และ failure ratchet ยังต้องเป็นของทีมเอง
- ประเด็นเปิด (จาก taste paradox): ถ้า junior เรียน debugging ผ่าน *output ของ harness* ตลอด จะเกิด taste เองหรือแค่ไว้ใจ harness?

## ดูเพิ่ม (See also)

- [[panutat-tejasen]]
- [[harness-engineering-panutat]]
- [[agent-harness-engineering]]
- [[harness-ratchet]]
- [[taste-paradox]]
- [[nattee-niparnan]]
- [[llm-era-computer-engineering-nattee]]
- [[coding-harness]]
- [[subagent-patterns]]
- [[alex-ker]]
- [[alex-ker-harnesses-optimize]]
- [[ai-orchestrator]]
- [[engineering-role-shift]]
- [[advisor-strategy]]
- [[llm-coding-pitfalls]]
- [[judgement-vs-automation]]
- [[harness-guides-sensors]]
- [[birgitta-bockeler]]
- [[harness-engineering-bockeler]]
