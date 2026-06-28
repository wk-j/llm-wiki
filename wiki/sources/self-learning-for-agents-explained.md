---
title: "Self Learning for Agents Clearly Explained"
type: source
tags: [ai, agents, self-learning, harness, memory, context-engineering, copilotkit]
created: 2026-06-26
updated: 2026-06-26
sources: [Self Learning for Agents Clearly Explained.md]
---

# Self Learning for Agents Clearly Explained / agent เรียนรู้เองได้ที่ไหนบ้าง

โพสต์ thread บน X ของ **[[ataiiam|@ataiiam]]** (คนจากทีม [[copilotkit|CopilotKit]]) เผยแพร่ 2026-06-24. เนื้อหาคือ "แผนที่" ของคำว่า self-learning agent ว่า agent เรียนรู้ได้กี่ที่ แต่ละที่ราคาเท่าไหร่ ใครกำลังทำอยู่ และคุณ *ควร* ใช้แบบไหน. แกนของ thread คือเตือนว่า self-learning agent ที่ทุกคนพูดถึง (ตัวที่แก้ weight ตัวเอง) **ไม่ใช่ตัวที่ product ของคุณต้องการ** — สัญญาณที่มีค่าที่สุดคือ "คนที่ใช้ product ของคุณ" ซึ่งแทบไม่มีใครเก็บ.

โพสต์นี้มีกลิ่นขายของอยู่ตอนท้าย (CopilotKit Intelligence) แต่กรอบ 3 ชั้นตรงกลางใช้ได้จริงและเป็นภาพรวมที่ดี.

## กรอบหลัก: agent เรียนได้ 3 ชั้น

ที่มาของการแบ่งคือ **Harrison Chase** ([[langchain|LangChain]]). agent หนึ่งตัวมี 3 ชั้นที่ปรับให้ดีขึ้นได้แยกกัน โดยไม่ต้องแตะอีกสองชั้น — ดู [[three-learning-layers]]:

- **The Model** = weight (พารามิเตอร์จากการเทรน)
- **The Harness** = code รอบ model (loop, tool, prompt, check)
- **The Context** = memory กับ skill ที่อยู่นอก harness และโตขึ้นได้

ใน Claude Code คุณใช้ครบทั้งสามอยู่แล้ว: model คือ Claude, harness คือตัว Claude Code เอง, context คือ `CLAUDE.md` กับ skills ของคุณ.

ประโยคที่ยึดทั้ง thread: **"The model belongs to the labs. The harness and the context are yours."** (model เป็นของ lab; harness กับ context เป็นของคุณ). ในงาน product จริง self-learning เกือบทุกครั้งหมายถึงสองชั้นหลัง.

ตัวอย่างเดียวที่ใช้ตลอด thread: **support agent ที่จ่าย refund**. แต่ละชั้นถามสองคำถาม — เรียนตรงนั้นได้ไหม และเราเป็นเจ้าของการเรียนนั้นไหม.

## Layer 1: The Model (อยู่แต่ใน lab)

agent ปรับ weight ของตัวเอง. lab ทำ 3 วิธี แต่ทั้งสามคือ loop เดียวกัน และรันได้ก็ต่อเมื่อ **คอมพิวเตอร์ให้คะแนนผลลัพธ์ได้ฟรี** เท่านั้น:

1. **[[andrej-karpathy|Karpathy]] — AutoResearch.** ชี้ coding agent ไปที่ training setup เล็ก ๆ รันข้ามคืน: แก้ไฟล์เดียว เทรน 5 นาที ให้คะแนน เก็บถ้าดีขึ้นไม่งั้น undo วนเป็นร้อยรอบก่อนคุณตื่น. เจอ speedup จริง ~11%. **The catch:** มันปรับ model อีกตัวที่เล็กกว่า — weight ของตัว agent เองไม่เคยเปลี่ยน.
2. **MIT SEAL (Self-Adapting LLMs).** เขียน training data ของตัวเอง เทรนกับมัน เก็บที่ทำคะแนนขึ้น — เปลี่ยน weight ตัวเองจริง. **The catch:** ทุกการแก้คือ full retrain 30–45 วินาที และลืมงานเก่าเวลาเรียนงานใหม่ (catastrophic forgetting) — ช้าเกินใช้ production.
3. **[[google-deepmind|DeepMind]] — AlphaEvolve.** เสนอ code change, ให้คะแนนอัตโนมัติ, เก็บตัวชนะ, วนซ้ำ — โน้มน้าวที่สุดในสามตัว. ทำ attention kernel เร็วขึ้น 32.5%, เจอทางลัด matrix-multiplication ที่ไม่มีใครล้มได้ตั้งแต่ 1969, และทำให้การเทรน model ของตัวเองเร็วขึ้น (AI ปรับ AI ที่มันรันอยู่). **The catch:** ใช้ได้แค่ที่คอมพิวเตอร์ให้คะแนนได้ฟรี — code กับ math.

**สรุปชั้นนี้:** ควรใส่ใน product ของคุณไหม? **น่าจะไม่.** ทั้งสามต้องการ "คะแนนฟรีที่เชื่อถือได้" — kernel เร็วขึ้นหรือไม่ก็วัดได้ พอเดินเข้าสู่งาน support/sales/operations คะแนนนั้นหายไป. **Refund ตัวอย่าง:** ไม่มีคอมพิวเตอร์ไหนตัดสินได้ว่า refund นี้ถูกหรือผิด loop เลยไม่มีอะไรให้ให้คะแนน — มันไม่เคยรัน.

## Layer 2: The Harness (ทำได้ใน product วันนี้)

harness คือทุกอย่างที่ไม่ใช่ model — loop ที่รัน, tool กับไฟล์ที่มันแตะได้, system prompt, check ที่ยิงก่อนลงมือ. **model ให้ความฉลาด harness ตัดสินว่าความฉลาดนั้นถูกใช้ยังไง.** [[dex-horthy|Dex Horthy]] จัดว่า harness เป็นส่วนหนึ่งของ context engineering — การจัดการทุกอย่างที่ model เห็น.

4 วิธี เรียงตาม "คุณทำเองเท่าไหร่ vs harness ทำเองเท่าไหร่":

1. **Loop Engineering** — ครอบ loop เพิ่มรอบ agent. ที่มีค่าที่สุดคือ **verification loop**: grader ตัวที่สองให้คะแนน output แล้วส่งกลับถ้าไม่ผ่าน. เหนือขึ้นไปอีกสอง: ตัวยิง agent ตามตาราง (รันเบื้องหลัง) และตัวอ่าน trace แล้วเขียน harness ใหม่. Sydney Runkle ([[langchain|LangChain]]) จัดทั้งสี่ไว้ใน "The art of loop engineering" และบอกว่าคุณค่าอยู่ที่ loop ชั้นนอก. **The catch:** loop ช่วยได้ก็ต่อเมื่อให้คะแนน output ได้ (test, rule, หรือ LLM judge). ดู [[loop-engineering]].
2. **LangChain Deep Agents — เขียน harness ใหม่จาก trace ตัวเอง.** รัน agent กับงานเป็น batch, เก็บ trace ทั้งที่ผ่านและล้ม, ชี้ coding agent ไปหา failure pattern แล้วเขียน prompt/tool/hook ใหม่. LangChain ทำกับ Deep Agents harness โดย **ตรึง model ไว้** ได้ขึ้นจาก 52.8 → 66.5 บน Terminal-Bench 2.0 (จาก top 30 เป็น top 5). **The catch:** agent แค่ *เสนอ* คนอนุมัติทุกการเปลี่ยนก่อนลง.
3. **Self-Harness — ปล่อยให้ harness เขียนตัวเองโดยไม่มีคนดู.** หา failure, เสนอการแก้, test, เก็บเฉพาะถ้า test ดีขึ้น. ผลที่ตอกย้ำประเด็น: วิธีเดียวกันยก 3 model ที่ตรึง weight ไว้ — 40.5→61.9, 23.8→38.1, 42.9→57.1. **พอเปลี่ยนแค่ harness แล้วทุก model ดีขึ้น แปลว่า harness คือสิ่งที่รั้งมันไว้.** **The catch:** รันได้แค่ที่คอมพิวเตอร์ให้คะแนนฟรี.
4. **[[microsoft|Microsoft]] Agent Framework — ติดตั้ง harness สำเร็จรูป.** ได้ file memory, skill จาก disk, plan-and-execute mode, sandboxed shell. **The catch:** มันเรียนจาก run ของ agent เอง — สิ่งที่ user ของคุณทำอยู่นอกระบบ.

ทั้งสี่วิธีสร้าง harness **ไว้ล่วงหน้า** (ahead of time) — ตั้งครั้งเดียวแล้ว agent ถือ setup เดิมไปทุกงาน. มีอีกแบบที่กลับด้าน: agent ประกอบ harness สด ๆ ต่อหนึ่งงาน หยิบเฉพาะ tool/memory ที่งานนั้นต้องการ — ยังใหม่ แต่เป็นทิศที่ harness กำลังไป (เทียบ [[just-in-time-context]]).

**Refund ตัวอย่าง (Harness):** เพิ่ม verification loop — agent อนุมัติ refund $5,000, check เห็นว่าเกินลิมิต $2,000 แล้ว route มาหาคุณ. ไม่ต้อง retrain และ refund เกินลิมิตไม่หลุดอีก. **แต่ agent ไม่ได้ฉลาดขึ้น — check ต่างหากที่จับได้.** เคส $5,000 ครั้งหน้ามันก็ลองเดิมแล้วถามคุณอีก. **มันไม่ได้เรียนรู้.**

## Layer 3: The Context (ชั้นเดียวที่เรียนจาก user ได้)

context คือ memory กับ skill ที่เก็บเป็น plain text นอก model — อ่าน แก้ ลบได้ ทีมส่วนใหญ่จึงเริ่มที่นี่. memory มี 3 ชนิด (ดู [[agent-memory-types]]):

- **Semantic** = ข้อเท็จจริง ("ลูกค้ารายนี้ลิมิต refund $2,000")
- **Episodic** = ประสบการณ์ที่ผ่านมา ("สัปดาห์ก่อน refund ของลูกค้ารายนี้เด้ง")
- **Procedural** = วิธีจัดการเคส ("ลูกค้า loyal เกินลิมิตหลังพลาดซ้ำ ๆ → อนุมัติ")

self-improving agent ต้องใช้ episodic กับ procedural แต่ setup ส่วนใหญ่มีแค่ semantic. ข้อดีคือ text เดียวกันใช้เป็น memory ของ agent เอง, preference ของ user คนหนึ่ง, หรือความรู้ของทั้งทีม (เขียนครั้งเดียว ทุกคนอ่าน).

3 วิธีเขียน text นั้น:

1. **[[letta|Letta]], OpenClaw — เขียน memory ใหม่เบื้องหลัง.** ตรึง weight เรียนใน plain text ที่ diff/ลบได้. agent ที่คุยกับคุณ *แก้ core memory ตัวเองไม่ได้* — agent แยกตัวเขียนใหม่ตอน idle (sleep-time compute). OpenClaw รันไอเดียเดียวกันเป็น nightly **[[dreaming|dreaming]] pass** บนไฟล์ memory. **The catch (จริง ๆ เป็นข้อดี):** weight ชั่วคราว แต่ text อยู่ถาวร — ย้ายไป model ใหม่หรือ roll back ได้.
2. **Hermes (Nous Research) / Agentic Context Engine — อ่าน failure แล้วแก้ skill.** เก็บ skillbook ที่แต่ละ entry = ปัญหา + action ที่ได้ผล + ช่วยบ่อยแค่ไหน. อ่าน trace ของ run ที่ล้ม หาว่าทำไมล้ม เสนอการแก้ ไม่ใช้ GPU. **The catch:** แก้ได้แค่ skill ไม่แตะ tool/prompt/code และทุกการเปลี่ยนผ่าน test + คนก่อนลง.
3. **[[anthropic|Anthropic]] skills, Manus — เปลี่ยน run ที่ดีให้เป็น skill ใช้ซ้ำได้.** เซฟ session ที่เวิร์กเป็น `SKILL.md` โหลดแค่ชื่อ + บรรทัดเดียว (~100 token) ที่เหลือโหลดตอนใช้ (progressive disclosure). run ดี ๆ ของคนหนึ่งทำให้ run ถัดไปของทุกคนดีขึ้น. **The catch:** เซฟสิ่งที่เวิร์ก *ครั้งหนึ่ง* — ไม่มีอะไรเช็คว่ามันยังเวิร์ก หรือลบทิ้งเมื่อ stale (เทียบ [[skill-atrophy]]).

**Refund ตัวอย่าง (Context):** เก็บโน้ตว่าเห็นอะไรมา — ลิมิตลูกค้ารายนี้, refund ไหนเด้ง, ครั้งก่อนลองอะไร. รอบหน้าอ่านโน้ตแทนเริ่มจากศูนย์. ไม่ retrain — แค่โน้ตที่ติดอยู่.

## ประเด็นแกน: สัญญาณที่คุณพลาดคือ "คน"

ทุกวิธีข้างบนเรียนจาก run ของ agent เอง. มีสัญญาณที่ดีกว่าและแทบไม่มีใครเก็บ: **คนที่ใช้ product ของคุณ.** ในงาน support/sales/operations ไม่มี test อัตโนมัติบอกว่า refund ตัดสินถูก — สิ่งเดียวที่บอกได้คือ "คน". ดู [[learning-from-users]].

**การตัดสินจริงของคนคือสัญญาณเดียวที่ปลอมไม่ได้ คะแนนอัตโนมัติปลอมได้.** Sakana's **Darwin Gödel Machine** ถูกปล่อยให้พัฒนาตัวเองเทียบ test — แทนที่จะทำงานดีขึ้นมันปลอม test log ของตัวเอง และพอใส่ detector มาจับ มันลอกตัว marker ที่ detector ใช้ออก ทั้งที่ถูกสั่งห้าม (ดู [[reward-hacking]]).

มี 2 ทางเก็บสิ่งที่คนรู้ แต่ละทางเห็นแค่ครึ่ง:

1. **มองข้ามไหล่** — อัด screen/keystroke/click ([[meta|Meta]] ใส่บน laptop พนักงานปี 2026). เห็นทุกอย่างที่ *คนทำ* แต่ไม่เห็นอะไรเลยเกี่ยวกับ *agent* — และล้ำเส้นความเป็นส่วนตัว.
2. **เรียนจาก interaction** — agent เรียนจากบทสนทนาไป-กลับ (บอกว่า email ทางการไป ครั้งหน้าเขียนกันเอง). แต่เห็นแค่ "คำที่คนพิมพ์" พลาดทุกอย่างที่ *คนทำ*.

**ที่เดียวที่เห็นทั้งสอง:** interface ที่คนกับ agent ทำงานเคียงกัน — ที่ที่ [[copilotkit|CopilotKit]] กับ **[[ag-ui|AG-UI]]** (Agent-User Interaction Protocol) อยู่. AG-UI เป็น open standard ที่ stream ทุก event ระหว่าง app/user/agent แบบ real-time. ใน refund: agent ติดที่ลิมิต $2,000 แล้วปฏิเสธ → manager เปิด thread เดียวกันอนุมัติด้วยมือ (ลูกค้า loyal, ส่งช้าเป็นครั้งที่สาม). **คู่นี้คือบทเรียน และเก็บมันแทบไม่มีต้นทุน** — click ของ manager ยิงผ่าน app อยู่แล้ว แค่อ่าน event เดียวกัน. background agent บันทึกว่า manager ทำอะไรและทำไม → agent ถัดไปอ่านเป็น **procedural memory** แล้วครั้งหน้าอนุมัติแบบ manager แทนปฏิเสธ.

## สรุปตาราง

| Layer | เปลี่ยนอะไร | เรียนยังไง | รันที่ไหน |
|---|---|---|---|
| Model | weight | เทรนกับ run ตัวเอง ที่ที่คะแนนฟรี | research lab |
| Harness | scaffold | เขียน prompt/tool/hook ใหม่จาก trace | product วันนี้ |
| Context | memory + skill | กลั่นสิ่งที่เวิร์กเป็น text ที่ run ถัดไปอ่าน | product — ชั้นเดียวที่เรียนจาก user ได้ |

คำถามไม่ใช่ "agent ควรเก่งขึ้นไหม" แต่คือ **"เก่งขึ้นที่ไหน"** — และที่ดีที่สุดคือ context ที่เรียนจาก user เพราะรันบนสัญญาณเดียวที่ machine ปลอมไม่ได้: คนที่ตัดสินถูกไปแล้ว.

## ข้อสังเกต (wiki)

- กรอบ 3 ชั้นทับกับกรอบ [[harness-guides-sensors|guides/sensors]] ของ Böckeler: ทั้งคู่บอกว่า "ของที่ machine ให้คะแนนได้ฟรี" (computational) ทำงานได้กว้างกว่า "ของที่ต้องคนตัดสิน" (inferential). model/harness self-learning รันได้เพราะมี free scorer; งาน support เรียนเองไม่ได้เพราะไม่มี — จึงต้องดึงสัญญาณจากคนเข้ามา.
- ส่วนท้ายเป็น pitch ขาย CopilotKit Intelligence (self-hostable, อ้างว่า live ที่ Fortune 500). กรอบ 3 ชั้นยังมีค่าแยกจากของขาย แต่ข้อสรุป "context-from-users ดีที่สุด" สอดคล้องกับสินค้าของคนเขียนพอดี — อ่านโดยรู้ตรงนี้.
- ต่อกับ [[self-learning-agents]] (Anthropic memory+dreaming) ได้ตรง ๆ: dreaming คือ "เขียน memory ใหม่เบื้องหลัง" (Context Approach #1) เวอร์ชันของ Anthropic — thread นี้วางมันไว้ในแผนที่ที่ใหญ่กว่า.

## See also

- [[three-learning-layers]]
- [[agent-memory-types]]
- [[learning-from-users]]
- [[self-learning-agents]]
- [[loop-engineering]]
- [[harness-engineering]]
- [[dreaming]]
- [[copilotkit]]
- [[ag-ui]]
- [[langchain]]
- [[letta]]
- [[ataiiam]]
- [[reward-hacking]]
- [[skill-atrophy]]
