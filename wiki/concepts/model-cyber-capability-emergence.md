---
title: Model Cyber Capability Emergence
type: concept
tags: [ai, cybersecurity, emergence, ai-safety, anthropic]
created: 2026-04-22
updated: 2026-04-22
sources: [Claude Mythos Preview.md]
---

# Model Cyber Capability Emergence / ความสามารถด้าน cybersecurity ที่เกิดขึ้นเองจากโมเดล

## แก่นความคิด

[[claude-mythos-preview|Claude Mythos Preview]] หา zero-day + เขียน exploit ได้ทุก OS ทุก browser อัตโนมัติ — **โดยไม่ได้ฝึกไว้เฉพาะเรื่อง security เลย** ความสามารถนี้ *emerged* ออกมาเองจากการที่โมเดลเก่งขึ้นทั่วไปในด้าน code / reasoning / autonomy

ผลคือ: ต่อไปนี้ทุก frontier model ที่เก่งขึ้น จะเก่ง security ขึ้นด้วยโดยอัตโนมัติ — ทั้ง defensive (หา bug แก้) และ offensive (เขียน exploit) ไม่มีทางเลือกได้อย่าง

## เกิดอะไรขึ้นกับ Mythos Preview

Anthropic ไม่ได้ fine-tune หรือ train Mythos ให้เก่ง exploit โดยเจาะจง แต่การที่โมเดลอ่านโค้ดเก่งขึ้น, คิดเป็นลำดับเก่งขึ้น, ทำงานต่อเนื่องได้นานขึ้น — ทำให้มันเก่ง *ทั้ง* การ patch bug *และ* การ exploit bug ไปพร้อมกัน ตรงนี้คือจุดสำคัญ: **offensive กับ defensive เป็น side effect เดียวกันของความเก่งทั่วไป**

ตัวเลขเปรียบเทียบกับ [[claude-opus-4-7|Opus 4.6]] บน Firefox 147 JS engine:

| Metric | Opus 4.6 | Mythos Preview |
|---|---|---|
| Working exploits | 2 / 200+ พยายาม | 181 / 200+ (+29 register control) |
| OSS-Fuzz tier-5 (control flow hijack) | 0 | 10 on fully patched targets |
| OSS-Fuzz tier 1–2 crashes | 150–175 | 595 |

Opus 4.6 "far better at identifying and fixing vulnerabilities than at exploiting them" (คำจากบล็อกเดือนก่อน) → Mythos พลิกกลับ: exploit ได้เต็ม ๆ

## รูปแบบที่เห็น

**Vulnerability chaining ที่ซับซ้อน** — Mythos ไม่ได้หา bug เดียวแล้วจบ มัน chain 2–4 vulnerabilities เข้าด้วยกัน: KASLR bypass → read struct → use-after-free → heap spray → root มีเกือบโหลของ chain แบบนี้บน Linux kernel คนทำอันเดียวก็ยากแล้ว มันทำเป็นระบบ

**Cost ต่อมาก** — OpenBSD bug: รัน scaffold 1000 รอบรวม <$20K, รอบที่เจอ <$50. N-day exploit: <$1000, <1 วัน. พอเทียบกับ expert pentester ที่ใช้สัปดาห์ต่อ exploit นี่คือการเปลี่ยนระดับ orders of magnitude

**Friction-based defense อ่อนแอลง** — Defense-in-depth ที่ขึ้นกับ "น่าเบื่อ / นาน / ซับซ้อนเกินไป" สำหรับมนุษย์ จะไม่ไวพอสำหรับโมเดลที่อดทนได้ไม่จำกัด Anthropic เองบอกว่า mitigations ที่คุ้มค่าเพราะ *friction* จะอ่อนแอลงมาก; hard barriers (KASLR, W^X) ยังสำคัญอยู่

## เชื่อมกับแนวคิดอื่นใน wiki

**[[agent-runtime-untrusted]]** — APTS บอกว่า "treat agent runtime as untrusted." Mythos Preview เป็นกรณีศึกษาแบบ full-scale ของสมมติฐานนี้: โมเดลที่ทำงานอัตโนมัติเก่งพอที่จะ root เครื่องได้ ยิ่งต้อง ensure ว่า scope มันถูกจำกัดโดย construction ไม่ใช่แค่ "หวังว่ามันจะไม่ทำ"

**[[graduated-autonomy]]** — ระดับ L4 (Autonomous) ของ APTS หมายความว่า agent ทำงานโดยไม่มี human review ในทุก step. Mythos scaffold ทำงาน L4 ใน domain ที่อันตรายมาก (exploit development). การตัดสินใจว่า model ไหนได้ L4 ใน domain ไหน คือคำถามหลักที่ Anthropic เผชิญตอนนี้

**[[auto-mode]]** — Claude Code auto-mode ใช้ classifier gate ตัดสินใจ approve/reject tool calls. Mythos ใช้ scaffold แบบเดียวกัน (container + Claude Code + prompt) แต่งานต่างกันโดยสิ้นเชิง. ถ้า Mythos-class model เปิดให้ใครก็ได้ใช้ผ่าน Claude Code, auto-mode classifier จะกลายเป็น defense layer สำคัญมาก

**[[advisor-strategy]]** — ปัจจุบัน Opus advise Sonnet execute. ถ้าระดับความสามารถด้าน security ของโมเดลธรรมดาเท่ากับ Mythos, advisor pattern อาจจะต้องกลับทิศ: ใช้ lightweight model triage แล้วส่งให้ specialized security model ทำต่อ

## ผลกระทบที่คาดได้

1. **Patch cycle ต้องสั้นลงมาก** — N-day exploit ที่เคยใช้คนเก่งทำสัปดาห์ ตอนนี้โมเดลทำเองในไม่กี่ชั่วโมงจาก CVE + git hash
2. **Security equilibrium เปลี่ยน** — 20 ปีที่ผ่านมา attack shape คล้ายเดิม; language model ที่ scale การหา+ใช้ vuln ได้ จะเปลี่ยน balance
3. **Defender ได้เปรียบในระยะยาว** — แต่ transitional period "fraught"; attacker อาจได้เปรียบก่อน
4. **Memory-safe language ยิ่งสำคัญ** — ส่วนใหญ่ของ vuln ที่ Mythos เจอเป็น memory corruption ใน C/C++ แต่ "memory-safe" language ก็ไม่ปลอดภัย 100% เพราะ `unsafe` blocks (Rust) / JNI (Java) / ctypes (Python)

## ได้อะไร

Offensive cyber capability ไม่ใช่ feature ที่ต้อง build แยก — มันเป็น **inevitable side effect** ของการทำโมเดลให้เก่งขึ้นทั่วไป. ทางเลือกไม่ใช่ "จะ train ให้เก่ง security ไหม" แต่เป็น "จะควบคุม/ปล่อยยังไง" — ซึ่งตรงกับที่ [[agent-runtime-untrusted]] บอก: scope by construction, don't rely on model restraint.

## See also

- [[claude-mythos-preview]]
- [[project-glasswing]]
- [[anthropic]]
- [[agent-runtime-untrusted]]
- [[graduated-autonomy]]
- [[auto-mode]]
- [[advisor-strategy]]
