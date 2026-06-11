---
title: What We've Learned Building Cloud Agents
type: source
tags: [ai, agents, cloud-agents, harness, durable-execution, infrastructure, cursor]
created: 2026-06-05
updated: 2026-06-05
sources: [What we’ve learned building cloud agents.md]
url: https://cursor.com/blog/cloud-agent-lessons
author: Josh Ma
published: 2026-06-02
---

# What We've Learned Building Cloud Agents

บล็อกของ [[cursor|Cursor]] เขียนโดย [[josh-ma|Josh Ma]] (2026-06-02) สรุปบทเรียนหนึ่งปีของการสร้าง **cloud agent** — agent ที่รันบน VM ของตัวเองในคลาวด์ ไม่ใช่บน laptop ของ user. แก่นของบทความคือ พอเอา agent ขึ้นคลาวด์ งานมันไม่ใช่ "เอา local agent ไปแปะบน server" แต่กลายเป็นการ **สร้างชั้น operating layer รอบ ๆ ตัว agent** — environment, durability, orchestration ทั้งหมดต้องประกอบขึ้นใหม่.

ดูหน้า concept หลักที่ [[cloud-agents]], และเรื่องที่เกี่ยวข้อง [[long-running-agents]], [[durable-execution]], [[agent-development-environment]], [[self-healing-environments]].

## บริบท — cloud agent ต่างจาก local agent ตรงไหน

ตอนเปิดตัวปีก่อน Cursor คิดว่า cloud agent เป็นแค่ส่วนต่อขยายของ local agent. ผ่านมาหนึ่งปี ความสามารถขยายไปไกล — ตอนนี้ cloud agent แต่ละตัวรันบน VM ของตัวเอง มี environment, dependency, network access ของตัวเอง, ทำงานขนานกันได้, รันแบบไม่มีคนเฝ้า (unattended), และรับงานยาวกว่าที่ agent บน laptop ทำได้.

ความสามารถพวกนี้มาพร้อมโจทย์ใหม่ที่ตอนรันบน laptop แทบไม่เจอ — การ setup environment, ความน่าเชื่อถือ (reliability), และ orchestration.

## บทเรียน 1: Development environment คือตัวสินค้า

ปัจจัยเดียวที่กระทบคุณภาพงานของ cloud agent มากที่สุด คือการที่มันมี **development environment ครบเหมือน developer จริง** — มี dependency, tool, network ที่ใช้รันและ verify งานได้.

ตอนรัน local เราไม่ต้องคิดเรื่องนี้ เพราะ agent ยืม environment ที่ทำงานอยู่แล้วบน laptop ไปใช้ฟรี. แต่บนคลาวด์ต้องประกอบใหม่ทั้งหมดจากศูนย์ และที่ยากคือ **บอกได้ยากว่าประกอบครบหรือยัง**.

> "Instead of a crash or an error message, often the only indication is a subtle degradation in output quality. You might not notice it at first, or if you do, you might chalk it up to the model."

จุดสำคัญ: อาการพังไม่ใช่ crash แต่เป็น **คุณภาพงานตกแบบเงียบ ๆ** — แล้วคนมักไปโทษ model ทั้งที่ต้นเหตุคือ environment ไม่ครบ. เมื่อปีก่อนเรื่องนี้ยังไม่สำคัญมาก เพราะ model ยังใช้ environment ได้ไม่เต็มที่อยู่แล้ว. แต่พอ model ฉลาดขึ้น **environment กลายเป็นตัวตัดสินว่า model จะทำงานได้เต็มศักยภาพหรือไม่**.

การจะไปถึง "full environment" ต้องสร้าง infra ขึ้นมาเยอะกว่าที่คิด:

- เครื่องมือให้ user สร้าง agent environment ได้ดีขึ้น
- วิธี hibernate และ resume VM ระหว่าง message อย่างมีประสิทธิภาพ
- pipeline สำหรับ checkpoint / restore / fork VM image แบบเร็วและทนทาน
- การเชื่อม harness กับ client ให้แน่น เพื่อให้ทั้ง agent และคน interpret และโต้ตอบกับ environment ได้

พอ cloud agent รับงานมากขึ้น มันต้องการ network access แบบมีการควบคุม — สร้าง PR, ดึง dependency, ทำ research. สุดท้าย Cursor เลยกลายเป็นต้องสร้างสิ่งที่เหมือน **"enterprise IT สำหรับ agent"** — secret redaction (กลบความลับ), network policy, credential management.

## บทเรียน 2: Long-running agent ต้องมี durable execution

cloud agent มีโจทย์ reliability คนละแบบกับ local. แทนที่จะแย่ทรัพยากรบน laptop, cloud agent รันใน VM แยกของตัวเอง. ทำให้รัน agent หลายตัวขนานกันและ delegate งานยาว ๆ (เป็นชั่วโมงแทนที่จะเป็นนาที) ได้ง่าย.

แต่การรันใน VM ก็เปิดความเสี่ยงจากการสะดุด — inference provider ล่ม, pod ต้องถูกแทนที่, EC2 node ดับ.

Cursor เริ่มจาก **work-stealing architecture** — worker node คว้า agent มาแล้ว loop จนจบ. มันคือการย้ายสิ่งที่ทำงานดีตอน local มาวางบน server ตรง ๆ และมันเปราะ — beta ช่วงแรกอยู่ที่ reliability แค่ **"one 9"** (~90%).

พอ cloud agent โตขึ้น Cursor พบว่าตัวเองกำลังจะสร้าง durable execution primitive ขึ้นมาใหม่ทั้งชุด — retry, scheduling งานข้ามเครื่อง, durability ข้าม node failure — ซึ่ง **[[temporal|Temporal]] แก้ไว้หมดแล้ว** เลยย้ายไปใช้ Temporal แทน.

agent loop บน Temporal ตอนนี้ทนต่อ inference สะดุด, pod hibernate/resume, และรันยาวข้ามวันข้ามสัปดาห์ได้. การย้ายครั้งนั้นอย่างเดียวดัน reliability ขึ้นเกิน **"two 9s"** (~99%).

ตัวเลข scale (ณ ตอนเขียน):
- Temporal จัดการ **50 ล้าน+ action ต่อวัน** ข้าม **7 ล้าน+ unique workflow**
- ภายใน Cursor เอง **มากกว่า 40% ของ PR มาจาก cloud agent** และยังเพิ่มขึ้นเรื่อย ๆ

บทเรียนเรื่องการออกแบบ Temporal workflow:
- ย้ายจาก workflow แบบ **"eternal"** (อยู่ตลอด) → หลาย workflow สั้นที่ **exit เมื่อจบงานชิ้นเดียว** — ทำให้ upgrade version ง่ายขึ้น
- แยก activity ออกมาเพื่อจับ timeout และ retry ให้ดีขึ้น เพราะ async tool call, subagent, และ inference provider ล่ม ทำให้สมมติฐานเดิมเปลี่ยนไป

## บทเรียน 3: แยก agent / machine ออกจาก conversation state

cloud agent ไม่ใช่ loop เดียวบนเครื่องเดียวอีกแล้ว. agent หนึ่งตัวอาจรันบนเครื่องหนึ่ง, spawn async subagent กระจายหลายเครื่อง, หรือเริ่มที่ local แล้ว delegate งานไปคลาวด์. subagent อาจ **อยู่นานกว่า parent** หรือรันบน pod คนละชนิดก็ได้.

วิธีรับมือคือเก็บสามอย่างนี้เป็น component ที่ **decouple ออกจากกัน**:

1. **agent loop** — อยู่ใน Temporal ไม่ใช่บน VM. ผลคือจัดการ pod lifecycle ได้อิสระ และรัน agent บน pod หลายชนิด รวมถึง optimization อย่าง readonly VM หรือ prewarmed VM (VM อุ่นเครื่องไว้ล่วงหน้า)
2. **machine state** — VM แยกจาก loop
3. **conversation state** — แยก layer เก็บข้อมูลและ streaming ออกจาก core agent workflow

ฝั่ง conversation Cursor สร้าง storage แบบ **append-only** (เขียนต่อท้ายอย่างเดียว) ที่ stream update ออกไปยัง web และ desktop client. layer นี้เผื่อ retry ไว้ด้วย — ถ้า step หนึ่งของ loop พังหลัง stream output บางส่วนออกไปแล้ว แล้วถูก retry, client จับได้ว่ามี retry, **rewind stream** กลับไป แล้วแสดงข้อมูลใหม่แทนของเก่า.

## บทเรียน 4: รู้จักหลบให้ agent ทำงาน (knowing how to get out of the way)

การสร้าง harness ของ cloud agent คือการตั้งคำถามซ้ำ ๆ ว่า **อะไรควรเป็น deterministic (harness คุม) กับอะไรควรยกให้ agent ตัดสินเอง**.

ช่วงแรก Cursor ยังไม่ไว้ใจ agent มาก — harness เลย double-check งานหลังทุก task, บังคับ commit, แล้ว push. พอ model ฉลาดขึ้น Cursor เริ่ม **ย้าย logic ออกจาก harness ไปเป็น tool ที่ agent คุมเอง**:

- **multi-repo**: เมื่อปีก่อนต้อง hardcode พฤติกรรมไว้ใน harness. ตอนนี้แค่บอก repo layout ให้ agent, เปิด tool สำหรับ branch และ PR, แล้วปล่อยให้ agent ตัดสินใจเองว่าจะทำงานยังไง
- **CI Autofix**: เวอร์ชันเก่า harness มี logic ดึง log งานที่ fail มาเขียนลง VM. ตอนนี้แค่ให้ agent เข้าถึง **GitHub CLI** แล้วเขียน output ก้อนใหญ่ลงไฟล์ให้มัน search เอง. notification ที่ส่งให้ agent ง่ายลงมาก

> "The harness isn't going away so much as what it contains is changing."

harness ไม่ได้หายไป แต่ **เนื้อในมันเปลี่ยน**. ตัวอย่างที่ยังต้องอยู่ใน harness ตอนนี้คือ **computer use** — Cursor มี subagent type เฉพาะสำหรับ computer use มี model routing, prompt, และ screen recording ของตัวเอง. VNC กับ Chrome เป็นของ environment ที่ **share กันระหว่าง parent กับ subagent** ทำให้ parent เรียกใช้ตรง ๆ ได้ (เช่นรัน Playwright script). ที่ต้องมี scaffolding นี้เพราะ model ยังไม่พร้อมทำ computer use เองล้วน ๆ — แต่ตัว agent ยังเป็นคนเลือกเองว่าจะเรียกใช้ตอนไหน. ดู [[subagent-patterns]].

อีกจุด: cloud agent ต้องการ **prompt ที่ต่างจาก local** — Cursor ดัน agent ให้ **autonomous กว่า** เพราะ **ต้นทุนของการบล็อกสูงกว่ามาก**. ตอนรัน local เรารู้ทันทีว่า agent หยุดรอ permission. แต่บนคลาวด์ มันอาจนั่งรอเป็นชั่วโมงกว่าเราจะกลับไปดู. ประเด็นนี้ตรงกับ [[orchestration-tax|orchestration tax]] — ในระบบ agent ขนาน คนคือคอขวด serial.

## บทเรียน 5 (มองไปข้างหน้า): self-healing environment

เป้าหมายถัดไปคือก้าวพ้นทางเลือกแบบ binary ระหว่าง "จูงมือ agent" กับ "หลบให้มันทำเอง". pattern ที่ดีกว่าคือ **ให้ agent มี tool ไว้เข้าใจระบบรอบตัวมันเอง**.

Cursor อยากให้ cloud agent **รายงานได้เองเมื่อติดขัด** — secret หาย, network ถูกบล็อก, หรือ environment กำลังขวางไม่ให้มันคืบหน้า — แล้ว **แก้เองแบบ self-healing**. แนวทางหนึ่งที่ Cursor เล่าในบล็อกวิจัยคือสิ่งที่เรียกว่า **"autoinstall"**. ดู [[self-healing-environments]].

## ข้อสรุป

cloud agent ดีขึ้นมากในไม่กี่เดือนที่ผ่านมา และ Cursor คาดว่าอัตราการเปลี่ยนแปลงจะเร่งขึ้นอีก. จุดขายของ Cursor cloud agent คือให้ทีมใช้ประโยชน์จากพื้นผิวกว้าง ๆ นี้ได้โดยไม่ต้องสร้างหรือดูแล infra ข้างใต้เอง.

## See also

- [[cloud-agents]]
- [[durable-execution]]
- [[agent-development-environment]]
- [[self-healing-environments]]
- [[cursor]]
- [[josh-ma]]
- [[temporal]]
- [[long-running-agents]]
- [[coding-harness]]
- [[orchestration-tax]]
- [[subagent-patterns]]
