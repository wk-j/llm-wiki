---
title: Agent Runtime as Untrusted Component / ตัวรัน agent คือส่วนที่เชื่อไม่ได้
type: concept
tags: [ai, agents, security, threat-model, apts, architecture]
created: 2026-04-20
updated: 2026-06-15
sources: [owasp-apts.md, Claude Mythos Preview.md, "Introducing Omnigent A Meta-Harness to Combine, Control and Share Your Agents.md"]
---

# Agent Runtime as Untrusted Component / ตัวรัน agent คือส่วนที่เชื่อไม่ได้

เวลาเราสร้างระบบที่มี AI agent รันเอง เช่น autonomous pentest หลายคนคิดว่า "งั้นเทรน model ให้ดี เขียน system prompt ให้รัดกุม น่าจะพอแล้ว"

[[owasp-apts|OWASP APTS]] บอกว่าไม่พอ ตอนนี้ยังไม่มีวิธีพิสูจน์ว่า model จะไม่ทำนอกคำสั่ง เทรนดีแค่ไหนก็ยังหลุดได้ โดน prompt injection ทีก็พัง

APTS เลยใช้วิธีคิดอีกแบบ สมมติไปเลยว่า agent อาจลองทำนอกคำสั่งเมื่อไหร่ก็ได้ แล้วออกแบบระบบตั้งแต่แรกไม่ให้มีช่องทำ ไม่ต้องไปหวังว่า model จะยับยั้งตัวเอง

APTS เขียนไว้ใน Introduction ว่า:

> APTS does not try to verify that a foundation model is aligned, cannot scheme, or will not attempt to exceed its mandate. These properties cannot be reliably verified by platform operators today... APTS instead takes an architectural stance: treat the agent runtime as a component that may, for any reason, attempt actions outside its declared mandate, and build the platform so that such attempts fail by construction rather than by the agent's own restraint.

## สองแนวคิดคนละทาง

เรื่อง agent safety มีสองแนวคิดที่ไปคนละทาง:

**แนวแรก เชื่อว่า model จะอยู่ในกรอบ** เทรนดี เขียน prompt ดี ถ้าหลุดแปลว่า alignment พัง ต้องเทรนใหม่

**แนวสอง สร้างระบบไม่ให้มีช่อง** ไม่สนว่า model ดีไม่ดี ขอแค่ว่าถ้ามันพัง ความเสียหายก็ยังอยู่ในกำแพงที่เราสร้างไว้

APTS เลือกแนวสอง เหตุผลง่ายมาก แนวแรกพิสูจน์ไม่ได้ด้วยเครื่องมือที่เรามี ยิ่ง model เก่งขึ้น ช่องว่างระหว่าง "ทำได้" กับ "เราอยากให้ทำ" ก็ยิ่งกว้าง จะปิดช่องนี้ด้วยการขอร้อง model ยังไงก็ไม่ไหว ต้องปิดด้วยโครงสร้าง

## ข้อบังคับที่ APTS เขียนไว้จริง

**APTS-SC-019** sandbox ต้องให้ kernel บังคับ ไม่ใช่รอให้ agent ยับยั้งตัวเอง agent ไม่มี credential ไปขยายกำแพงเอง

**APTS-SC-020** allowlist ของ tool/action ที่ agent ใช้ได้ ต้องอยู่นอก model prompt ถ้า allowlist ฝังใน system prompt แค่ model ตีความใหม่ก็จบ

**APTS-MR-023** threat model ต้องเขียนไว้ว่า agent runtime คือ untrusted component ไม่ใช่แค่พูดในห้องประชุม ต้องลงเอกสาร

**APTS-AR-020** audit log ตัวจริงต้องเก็บในที่ agent เอื้อมไม่ถึง ถ้าแก้ log ได้ log ก็ไม่นับเป็น audit trail แล้ว

**APTS-AL-028** L3 กับ L4 ต้องทดสอบ containment จริงเป็นระยะ operator ลงมือเทสเอง อย่าอ่านเอกสารแล้วเชื่อ

**APTS-TP-021/022** ต้องเปิดเผยว่าใช้ foundation model ตัวไหน และทุกครั้งที่เปลี่ยน model เวอร์ชันใหม่ต้องประเมินใหม่ เพราะ model ใหม่อาจแรงพอทะลุ control เดิม

**APTS-SE-026** ให้เฝ้าดูว่า action ของ agent กระจายตัวเป็นปกติมั้ย ไม่ใช่แค่ดูว่าอยู่ใน scope หรือเปล่า ต่อให้ action ทุกอันอยู่ใน scope ถ้าพฤติกรรมเริ่มเพี้ยนก็ต้องจับได้

## ทำไมพึ่งโครงสร้างดีกว่าพึ่งคำสัญญา

ถ้าเราพึ่ง system prompt อย่างเดียว เช่น "You must not do X" เจอปัญหาหลายอย่าง:

- prompt injection เขียนทับได้
- model เวอร์ชันใหม่อาจตีความ prompt ต่างไป
- policy ที่ฝังใน prompt อ่านยาก เทสยาก audit ก็ยากเพราะไม่มีโครงสร้างชัด

ถ้าเราพึ่ง component ภายนอก เช่น sandbox kernel, allowlist service, audit store ที่อยู่คนละ host จะเห็นข้อดีทันที:

- model โดน jailbreak ระบบก็ยังกันได้
- เทสได้เหมือน unit test red team ได้
- model อัปเดตก็ไม่ต้องกลับมาประเมินซ้ำทุกครั้ง (ยกเว้นว่า capability ใหม่ทะลุ assumption เรื่องโครงสร้างไปเลย)

สรุปคือความปลอดภัยไม่ได้ขึ้นกับว่า model อยู่ในกรอบแค่ไหน แต่ขึ้นกับว่าชั้นรอบ ๆ model กั้นได้ดีแค่ไหน

## ทำไมต้องระวังตอน model อัปเดต

APTS เขียนไว้ว่า model รุ่นใหม่มักเก่งขึ้นเรื่องหาและใช้ช่องโหว่ พฤติกรรมแปลก ๆ ที่ปีก่อนเรามองว่าไม่น่าเกิด ปีนี้ก็เริ่มเห็นใน eval

APTS เลยเขียนไว้แบบนี้:

- อย่ายึด assessment ไว้กับ model เวอร์ชันเดียวแล้วคิดว่าจบ APTS-TP-022 บังคับให้ประเมินใหม่ทุกครั้งที่เปลี่ยน model เวอร์ชันใหม่
- assumption เรื่องโครงสร้างบางอันต้องแข็งขึ้นเมื่อ model เก่งขึ้น เช่น sandbox ที่ใช้กับ model ปี 2025 อาจต้องเสริมความแข็งเพิ่มสำหรับ model ปี 2027
- หัวข้อที่ยังไม่นิ่ง เช่น verifiable alignment, scheming detection, containment testing กับ model ที่รู้ว่าโดนเทสอยู่ APTS ตั้งใจไม่แตะ เก็บไว้ให้เวอร์ชันหลัง

## วิธีคิดนี้ใช้ได้แม้ไม่ได้ทำ pentest tool

ถ้าคุณทำแค่ coding agent ก็เอาวิธีคิดนี้ไปปรับใช้ได้:

- [[auto-mode|Auto mode]] ของ [[claude-code|Claude Code]] เอา classifier มาอยู่นอก model คอยตรวจ tool call ก่อนรันจริง คือ APTS-SC-020 ที่ระดับ harness
- [[subagent-patterns|Pipeline subagent]] pattern เอา review/test/audit agent มาคอยดูช่วงที่ main agent รันเอง คล้าย containment verification ของ APTS-AL-028 แต่ทำต่อเนื่อง
- [[harness-engineering]] ของ [[panutat-tejasen|Panutat]] สอนให้ออกแบบ harness ของ reviewer ไม่ใช่สอนคนไป review ของ agent เอง ลึก ๆ แล้วก็คือ fail-by-construction ในระดับหลักสูตร
- **Agent Gateway** ของ [[gemini-enterprise-agent-platform|Gemini Enterprise Agent Platform]] — ตัวกลางที่ตรวจ request ของ agent ก่อนเข้าถึง memory/tool policy อยู่นอก model audit ได้ เปลี่ยนได้โดยไม่ต้อง redeploy agent — ดู [[long-running-agents|Pattern 3 ของ long-running agents]] คือ APTS-SC-020 รีแบรนด์เป็น product
- **Contextual policy** ของ [[omnigent|Omnigent]] — [[meta-harness|meta-harness]] จำ action history แล้วบังคับกฎจาก state จริง เช่น หลังลง package ใหม่ต้องขออนุมัติก่อน `git push`; egress proxy inject credential เฉพาะ request ที่ผ่านกฎโดยไม่ให้ agent เห็น secret

พูดง่าย ๆ คำถามเปลี่ยนจาก "จะเทรน agent ยังไงให้เชื่อได้" เป็น "จะกั้น agent ยังไงโดยไม่ต้องเชื่อ"

## ผลที่ได้

ทีมที่ออกแบบตามวิธีนี้:

- ไม่ต้องรีบแก้ทุกครั้งที่มีข่าว behavior ใหม่ของ model เพราะ control ไม่ได้พึ่ง model ตั้งแต่แรก
- audit ได้จริงว่าใครทำอะไรเมื่อไหร่ ไม่ต้องไปถาม model ว่าเมื่อกี้มันทำอะไร
- ยืนยันกับลูกค้าหรือ regulator ได้จากหลักฐานโครงสร้าง ไม่ใช่จากรายงานพฤติกรรม model

ส่วนทีมที่ตั้งต้นว่า "เราเทรน model ดีแล้ว ไม่ต้องกั้นเยอะ" มักจะเจอปัญหาตอน scope ขยาย ตอน model อัปเดต หรือตอน prompt injection ตัวใหม่โผล่

## Mythos Preview: กรณีศึกษาแบบ full-scale

[[claude-mythos-preview|Mythos Preview]] ของ [[anthropic|Anthropic]] คือตัวอย่างจริงของสมมติฐานนี้: โมเดลที่ทำงานอัตโนมัติใน container เดี่ยว ๆ สามารถหา + exploit zero-day ในทุก OS หลัก ทุก browser หลัก ได้เองภายในไม่กี่ชั่วโมง ไม่มีมนุษย์ช่วย มีแค่ prompt เดียว "หา vulnerability ในโปรแกรมนี้"

นี่คือเหตุผลที่ APTS บอกว่า **อย่าพึ่ง model restraint** — Mythos เก่งกว่าที่ใครคาดไว้หลายระดับ และความเก่งนี้ emerged จากการ train ทั่วไป ไม่ได้ train เฉพาะเรื่อง security. ถ้าวันนึงโมเดลระดับนี้เปิดกว้างโดยไม่มี sandbox ที่แข็งพอ → defense-in-depth ทุกชั้นที่เคยคิดว่า "น่าเบื่อเกินไปที่จะ exploit" จะพังเพราะโมเดลไม่เบื่อ

ดูเพิ่มที่ [[model-cyber-capability-emergence]]

## See also

- [[owasp-apts]]
- [[owasp]]
- [[graduated-autonomy]]
- [[auto-mode]]
- [[subagent-patterns]]
- [[harness-engineering]]
- [[advisor-strategy]]
- [[model-cyber-capability-emergence]]
- [[claude-mythos-preview]]
- [[meta-harness]]
- [[omnigent]]
