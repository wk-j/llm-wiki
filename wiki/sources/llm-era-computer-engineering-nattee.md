---
title: LLM Era Computer Engineering — Nattee Niparnan
type: source
tags: [ai, software-engineering, education, curriculum, thai-source, pedagogy, coding-agent]
author: Nattee Niparnan
date_ingested: 2026-04-18
sources: ["LLM Era Computer Engineering - Nattee Niparnan.md"]
---

# วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง — Nattee Niparnan

ซีรีส์ Facebook สองตอนโดย [[nattee-niparnan|Nattee Niparnan]] อาจารย์ภาควิชาวิศวกรรมคอมพิวเตอร์ จุฬาฯ — Ep. 1 เล่ามุม "ห้องเรียนกับห้องสอบ" (2026-04-10); Ep. 2 เล่ามุม "งานจริงกับ Coding Agent" (~2026-04-17) และสรุปคำถามกลางที่ยังตอบไม่ได้ว่า **นิสิตวิศวฯคอมควรฝึกมือลึกแค่ไหนในยุคที่ LLM ทำแทนได้จริง** เข้าชุดกับข้อเสนอ [[harness-engineering|Harness Engineering]] ของ [[panutat-tejasen|Panutat Tejasen]] แต่มองจากคนละจุด

## Ep. 1 — LLM ในห้องเรียน และห้องสอบ (2026-04-10)

### เปิดด้วยฉาก hail mary

นิสิตคนหนึ่งในวิชา Data Structure เหลือ 20 นาทีสุดท้าย คะแนน 10% กด "ขอ hint จาก LLM" ใน grader — LLM ถามกลับแบบ Socratic ว่า *"แยกแยะ array index กับค่าใน array ให้ออก"* — นิสิตแก้จุดนั้นแล้วคะแนนพุ่งไป 100%. ฉากนี้เป็นตัวอย่างจริงของการทดลองที่เริ่มสะสมมาเกือบปี

### Pattern การสอน/วัดผลที่ทดลองแล้ว (แจงเป็นรายการได้)

อันนี้คือคุณค่าหลักของ Ep. 1 — รายการ design choice ที่ทำจริงในภาคฯ ไม่ใช่แค่บทนำของ Ep. 2:

| Pattern | รายละเอียด |
|---|---|
| **LLM-in-grader (Socratic-only)** | ฝัง LLM เข้าไปในระบบ `cafe-grader` (maintainer ปัจจุบันคือ Nattee, เริ่มโดย อ. มะนาว Jittat Fakcharoenphol และ อ. โป้ง Pramook Khungurn); แต่ control prompt ให้ถามกลับเฉพาะจุดที่ผิด ไม่ให้เฉลย |
| **Help-cost ในห้องสอบ** | กดขอ hint 1 ครั้ง **คะแนนเต็มลด 10 แต้ม** กด 3 ครั้งเหลือ 70 — นิสิตต้องตัดสินใจเองว่าคุ้มไหม (เป็น economics ของ help-asking) |
| **Chat-log-as-submission** | งานที่วัดด้วยรายงานต้องส่ง chat log ที่คุยกับ LLM มาด้วย; ให้คะแนนตาม "ความพยายามในการสร้างผลงานที่ดีผ่าน LLM" ไม่ใช่แค่ผลลัพธ์ — rubric ยังยาก แต่ดีกว่าดูแต่ output |
| **Prompt-as-exam (อ. สมชาย, Intro to Com Prog)** | นิสิตเขียน *prompt* แทนเขียน code; เอา prompt ไปสร้าง code แล้ว code ต้องทำงานถูกต้อง (อ้างอิงจากโพสต์ของ อ. Ekapol Chuangsuwanich) |
| **Find-the-bug / flip classroom** | ในวิชา Data Structure และ Algorithm Design เพิ่มน้ำหนักของโจทย์ "หาว่า code นี้ผิดตรงไหน" ทั้งในห้องและในข้อสอบ — ตั้งใจเทรน "ต่อมเอ๊ะ" |
| **Workshop guided-learning / NotebookLM** | สนับสนุนการใช้ LLM ช่วยเรียนอย่างเปิดเผย มี workshop (บรรยายโดย อ. ม๊อค Mock Suwannatat) |
| **Claude Code skill สำหรับเฉลย/presentation** | อ. ชิน Nuttapong Chentanez รับอาสาเขียน skill ให้ Claude Code ช่วยเขียนเฉลย, review เฉลย, และทำ presentation แบบมี animation อธิบายข้อ |

### Feedback จริงจาก pattern เหล่านี้

- LLM-in-grader บางครั้ง "ตอบตรงจุดผิดเป๊ะ แก้แล้วผ่าน" บางครั้ง "focus ไม่ครบ แก้แล้วยังผิด" — ไม่ได้สมบูรณ์ แต่ hail-mary log ที่เห็นเยอะแสดงว่ามีผล
- Chat-log submission ทำให้เห็นว่านิสิตคุยกับ LLM ยังไง — มีประโยชน์แม้ rubric ยังไม่ครบ

### คำถามที่ยังตอบไม่ได้ — Dijkstra

คำถามแบบ *"นิสิตต้องรู้ไหมว่าเมื่อไรจะใช้ Dijkstra Algorithm (หรือ algo อื่น)"* — Nattee คิดมาเป็นปียังไม่ตก: ถ้าไม่สอน แล้ว LLM เลือก algorithm ผิด นิสิตที่ไม่เคยเรียนจะรู้ได้ยังไงว่ามันผิด; แต่จะให้เรียนลึกทุกเรื่องเหมือนเดิมก็ดูไม่ make sense เมื่อ LLM ทำแทนได้จริง — **ปมนี้คือต้นทางของ taste paradox ใน Ep. 2**

## Ep. 2 — Coding Agent ในงานจริง และ taste paradox (~2026-04-17)

### เคสเริ่มต้น — PoC Web App

- งานที่ปรึกษา ปกติใช้เวลา **1–2 เดือน**; requirement นิ่งช้าจนเหลือเวลา **ไม่ถึง 1 สัปดาห์**
- ใช้ stack: **Claude Code + Antigravity + Figma Make**
- ค่า tool รวม **$140**; ไม่จ้าง RA เลย (ปกติต้องจ้าง 3–4 คน)
- Nattee ทำหน้าที่ *review + ตัดสินใจ* เป็นหลัก

### "งานลิง" และการขยับขึ้น loop ถัดไป

- *ChatGPT แบบปกติ* = ยังต้อง "ก็อป code ไปแปะ, รัน, เอา error กลับมาถาม" — "งานลิง" ที่ใช้มือแต่ไม่ใช้สมอง กินเวลาในทุก loop
- *Coding Agent* = สร้างไฟล์ / รันคำสั่ง / อ่านผล / แก้เอง — เอาคนออกจาก loop งานลิง แล้วดันคนขึ้นไปอยู่ใน loop ที่ต้อง "ตัดสินใจ" จริง ๆ

### War story — authorization bug

- แต่ละ endpoint ผ่าน unit test; ดูดี
- พอทำ integration test พบว่า **Buyer ลบ resource ของ Seller ได้** — เพราะ Nattee ไม่ได้สั่งให้ Agent คิด authorization ในภาพรวม
- Agent แก้ครบทั้งระบบใน commit เดียวได้สบาย — แต่ **"Agent ไม่รู้หรอกว่าต้องแก้ ถ้าเราไม่สั่ง"**
- บทเรียน: เวลาที่ Agent คืนมา ถ้าเอาไป "ปั่นฟีเจอร์" อย่างเดียวได้แค่ "เร็วขึ้น"; ถ้าเอามา "ถอย-มองภาพรวม-audit" นั่นแหละคือจุดชี้วัด

### ทรัพยากรในสมการ compromise เปลี่ยนไป

หัวใจของวิศวกรคือการ compromise — แต่ *ทรัพยากรที่ต้องชั่ง* เปลี่ยน:

| เดิม (ก่อน Agent) | ใหม่ (มี Agent) |
|---|---|
| "ทีมถนัด framework ไหน" | "Agent เขียน framework ไหนได้เสถียรกว่า" |
| "อะไรเขียนเร็วกว่า" | "framework ไหนกิน token น้อยกว่า" |

> "คำถามที่เมื่อ 2 ปีที่แล้วไม่มีในสมองเลย" — Nattee

### Taste paradox (ใจกลางของ Ep. นี้)

- "ใช้ Agent เป็น" — สอนไม่ยาก ยัดใน 1–2 วิชาก็พอ
- "ใช้เมื่อไร ขนาดไหน และ **review อย่างไรให้มีต่อมเอ๊ะ**" — นี่คือของยาก
- ปมที่ซ้อนอยู่: review ได้ดี ต้องเคย "ทำ" มาก่อน — Nattee จับ bug authorization ได้เพราะเคยเขียน auth เอง; คนที่ไม่เคยเขียน เคยแต่สั่ง Agent ทำ จะรู้ได้ยังไงว่าตรงไหนควรเอ๊ะ
- **"Agent ทำให้เราข้ามขั้นตอนฝึกมือได้ แต่ขั้นตอนฝึกมือนั่นแหละที่สร้าง judgment ให้เราคุม Agent ได้"** — loop ที่วนอยู่นี้คือสิ่งที่ Nattee เรียกว่าปัญหา "taste"
- ดู [[taste-paradox]] สำหรับการเก็บประเด็นนี้เป็น concept แยก

### High-level Design Choice ขยับลงมาหา junior

- ตัดสินใจ *"ทำไม framework นี้ / ทำไม lib นี้ถึงเหมาะ"* — เมื่อก่อนเป็นงาน Senior
- วันนี้ Agent รับงาน implementation ไปแล้ว — **นิสิตจบใหม่ถูกบังคับให้ต้องคิดภาพใหญ่แทน**
- เป็นการขยับ scope ของ [[ai-orchestrator]] ลงไปอีกระดับ

### Core engineering สำคัญมากขึ้น ไม่ใช่น้อยลง

- วิชายาขมอย่าง **Data Structure, Algorithm, Discrete Math** — ไม่ใช่แค่ทฤษฎีบนกระดาน แต่คือพื้นฐานในการเข้าใจระบบและ **ตรวจสอบงานของ AI** ได้
- "ยิ่งมี Agent ยิ่งต้องแม่นเรื่องพวกนี้ **มากขึ้น ไม่ใช่น้อยลง**" — ตรงข้ามกับคำทำนายที่ว่าทฤษฎีจะกลายเป็นไม่จำเป็น
- ต่อยอดใน [[engineering-role-shift]]

### Dark Side — ทุนของ RA หายไป

- งานสเกลเดิมเคย **จ้าง RA 3–4 คน** — รอบนี้ **จ้าง 0**
- $140 ค่า tool ถูกกว่าจ้างคนหลายเท่า
- มุม corporate อาจปลอบใจว่า "ยังไงก็ต้องจ้างเด็กจบใหม่เพื่อโตไปเป็น Senior" — แต่ *"ในมุมคนจ่ายเงิน แรงจูงใจที่จะจ้างคนน้อยลงชัดขึ้นทุกวัน"*
- เชื่อมโยงกับ [[judgement-vs-automation]] ในเรื่อง entry-level hiring

### คำถามที่ Nattee ยังตอบไม่ได้

- *"นิสิตต้องฝึกมือลึกแค่ไหนถึงจะพอ?"* — ฝึกทุกเรื่องเหมือนเดิมไม่ make sense; ไม่ฝึกเลยก็ไม่มี taste
- จังหวะเวลา: "Agent วันนี้ยังไม่เก่งเรื่องมองภาพรวม แต่พรุ่งนี้ model เทพกว่ามาเมื่อไหร่ก็ไม่รู้ (ตามอ่าน อ. อ๋า Piyalitt Ittichaiwong)"
- *"ยิ่งเป็นเหตุผลที่ต้องรีบสร้าง skill พวกนี้ตอนที่มันยังมีค่าอยู่"*

### ปล. — อุปสรรคจริงในห้องเรียน

ค่าใช้จ่ายรายเดือนของ tools ระดับ top — อ. Ekapol Chuangsuwanich และ อ. Dittaya Wanvarie กำลังประสานหาทางแก้ให้นิสิต

## ใจความรวมของซีรีส์

1. **การสอนปรับไปแล้วเยอะ** (Ep. 1) แต่ outcome ของวิชาหลักยัง *"ยังไม่ได้ปรับอย่างชัดเจน"* — design ไปก่อน theory ตามหลัง
2. **Coding Agent ย้ายคนขึ้น loop ตัดสินใจ** (Ep. 2) — งาน review / architectural choice กลายเป็นจุดชี้วัดผลงาน
3. **Taste paradox** — ฝึกมือคือสิ่งที่สร้าง judgment ที่ใช้คุม Agent ได้; จะสอนให้ "ข้าม" ฝึกมือแต่ยังมี judgment ไม่รู้ทำยังไง
4. **Core theory สำคัญมากขึ้น** — DS/Algo/Discrete Math เลิกเป็นวิชาบนกระดาน กลายเป็นเครื่องมือตรวจงาน AI
5. **High-level design choice ตกลงมาหา junior** — seniors เคยเป็นคนเลือก framework; วันนี้ agent เขียน implement เอง นิสิตจบใหม่ต้องคิดภาพใหญ่ตั้งแต่แรก
6. **Dark side** — $140 tool vs 3–4 RA เงินเดือน — แรงจูงใจในการ "จ้างคนน้อยลง" ชัดขึ้นทุกวัน

## การเทียบกับข้อเสนอของ Panutat

Panutat (ใน [[harness-engineering-panutat]]) บอกว่า **มนุษย์ตรวจงาน AI ตามไม่ทันแล้ว** → ต้องให้ agent ตัวอื่นมาตรวจ (harness)

Nattee ย้อนหนึ่งชั้น: **ต่อให้จะออกแบบ harness ก็ยังต้องเคยทำมือเองถึงจะรู้ว่า harness ตัวไหนควรมี และควรตรวจอะไร** → นี่คือ taste paradox

ทั้งสองคนพูดถึงจุดเดียวกัน (review / audit งาน AI) แต่มองจากคนละจุด:

- **Panutat** = *scope of reviewability*: ทำไมคนตรวจ library choice ไม่ไหว — ตอบด้วย agent harness
- **Nattee** = *origin of the reviewer*: taste มาจากไหน ถ้า junior ไม่เคยฝึกมือเอง

ไม่ได้ขัดแย้งกัน — เป็นสองปัญหาคนละ layer ในเรื่องเดียวกัน ดู [[taste-paradox]]

## See also

- [[nattee-niparnan]]
- [[taste-paradox]]
- [[harness-engineering]]
- [[harness-engineering-panutat]]
- [[panutat-tejasen]]
- [[engineering-role-shift]]
- [[ai-orchestrator]]
- [[judgement-vs-automation]]
- [[llm-coding-pitfalls]]
- [[advisor-strategy]]
