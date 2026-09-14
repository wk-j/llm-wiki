---
title: Plan Mode as Prompting
type: concept
tags: [ai, planning, coding-agents, harness, judgment]
created: 2026-07-02
updated: 2026-09-14
sources: [zoran-horvat-claude-no-planning-engine.md, planning-mode-dangerous-illusion.md, claude-codes-new-intent-md-rob-shocks.md, ai-native-sdlc-playbook.md]
---

# Plan Mode as Prompting / Plan mode คือ prompt scaffold

**Plan Mode as Prompting** คือมุมมองว่า plan ที่ agent เขียนออกมาเป็นผลของ prompt strategy และ harness constraint มากกว่าจะเป็น proof ว่ามี planning engine แบบ symbolic อยู่ข้างใน. หน้านี้มาจากโพสต์ของ [[zoran-horvat|Zoran Horvat]] เรื่อง [[zoran-horvat-claude-no-planning-engine|Claude has no planning engine]] และวิดีโอ breakdown [[planning-mode-dangerous-illusion]].

## Plan ที่ดูดีไม่เท่ากับเข้าใจจริง

Plan mode มักผลิต numbered steps ที่อ่านดี. มันอาจพูดถึง risk, obstacle, และ implementation order ได้. แต่ Horvat เตือนว่า output แบบนี้อาจเป็นแค่ pattern ของ "แผนที่ดีควรหน้าตาเป็นอย่างไร" ไม่ใช่ความเข้าใจเชิงวิศวกรรม.

ตัวอย่างคือ model วาง plan ที่ดูเป็นระบบ แต่ไม่ถามว่าควรทิ้ง user data หรือไม่. นั่นเป็นคำถามสำคัญกว่า implementation step เพราะมันแตะ product semantics และความรับผิดชอบต่อผู้ใช้.

**ผลคือ:** plan อ่านดีได้ แม้ยังข้ามคำถามที่ senior engineer ต้องถาม.

## Demo: directory upload feature

ในวิดีโอ [[planning-mode-dangerous-illusion]] Horvat ใช้ prompt เดียวกันกับ Sonnet 4.6 และ [[claude-opus-4-7|Opus 4.7]]. โจทย์คือ web app ให้ user upload source-code directory, ignore directories เช่น binaries หรือ `node_modules`, เก็บผลเป็น JSON บน server, แล้ว render ตาราง path/name/line count.

Sonnet 4.6 วางแผน server-side filtering แต่ไม่วาง client-side filtering. ผลคือ frontend upload directory ดิบขึ้น server ก่อน แล้ว server ค่อยโยนไฟล์ที่ไม่ต้องการทิ้ง. สำหรับ Horvat นี่เสี่ยงทั้ง waste และ server crash ถ้า user upload directory ใหญ่. Sonnet ยัง implement bug ที่ทำให้ file path หายหลัง refresh เพราะใส่ filename ลงทั้ง path และ name field.

Opus 4.7 วางแผนดีขึ้น: เห็น client-side filtering, repopulate file paths ที่ browser strip ออก, และ output ถูกต้องกว่า. แต่ Horvat ยังบอกว่านี่คือ prompt/iteration strategy ที่แพงและ refined กว่า ไม่ใช่ proof ว่ามี symbolic planner.

**ได้อะไร:** model/harness ที่ดีกว่าลด blind spot ได้ แต่ไม่ได้แทนการถามคำถามเชิง design.

## Plan mode อยู่ที่ harness layer

ในกรอบ [[coding-harness]] Plan mode คือ behavior ของเครื่องมือรอบ model: จำกัดไม่ให้แก้ไฟล์, ให้สำรวจ context, แล้ว prompt ให้เขียนขั้นตอนก่อน implement. ถ้าเปลี่ยน prompt, model, effort level, หรือรอบ iteration คุณภาพ plan ก็เปลี่ยน.

นี่ไม่ได้ทำให้ Plan mode ไร้ค่า. ตรงข้าม มันทำให้เราเห็นว่าควร improve ตรงไหน: prompt, grounding, evidence requirement, checklist, reviewer, หรือ deterministic gate.

**ได้อะไร:** อย่าถามว่า "model มี planner ไหม" อย่างเดียว ให้ถามว่า "harness บังคับให้ plan มีหลักฐานและถูกตรวจอย่างไร".

## วิธีใช้ให้ปลอดภัยกว่า

แนวปฏิบัติที่เข้ากับโพสต์นี้:

- ให้ plan ระบุ assumption และ decision ที่เสี่ยง
- ให้ link กลับไป code evidence หรือ docs ที่ใช้
- ใช้ [[grounding|external prior art]] หรือ web search เมื่อเรื่องมี best practice ภายนอก
- แยก find กับ filter ในงาน review เหมือน [[find-vs-filter]]
- ให้คนตัดสินใจจุดที่กระทบ data, architecture, security, และ user-facing behavior

**ผลคือ:** plan กลายเป็น first draft ที่ตรวจง่าย ไม่ใช่คำตัดสินแทนคน.

## Senior moves ที่ plan mode ยังพลาด

Horvat ชี้ว่าแม้ Opus ทำงานผ่าน มันยังพลาดสิ่งที่ senior engineer ควรถาม:

- จะทิ้ง user data ทั้งหมดจริงหรือ ทั้งที่ feature ถัดไปอาจต้องใช้
- ทำไม ignore list ต้องซ้ำทั้ง client และ server
- risk ฝั่ง server load ถูกปิดตั้งแต่ client หรือยัง

สามเรื่องนี้ไม่ใช่ syntax. มันเป็น product semantics, data design, และ operational safety. Plan mode อาจทำตาม requirement ได้ดี แต่ยังไม่รู้ว่า requirement นั้นควรถูกทักกลับตรงไหน.

**ผลคือ:** แผนที่ดีต้องมีช่องให้คนตรวจ assumption ไม่ใช่แค่ checklist ว่าจะ implement อะไร.

## ประเด็นที่ยังไม่ลงตัว

Playbook ของ Anthropic ใน [[claude-codes-new-intent-md-rob-shocks|คลิป Rob Shocks]] วาง plan mode เป็นช่วง Build ของ [[artifact-chain|artifact chain]] วิศวกรส่ง `intent.md` กับ `spec.md` ให้ agent แล้วซักต่อว่าอะไรอาจพัง ทางเลือกไหนถูกตัด และ test อะไรพิสูจน์ผลได้ จนคนที่ไม่เห็นบทสนทนาเดิม implement จาก `plan.md` ได้

นี่ไม่ได้ลบคำวิจารณ์ของ Horvat กลับทำให้เส้นแบ่งชัดขึ้น Playbook ใช้ plan เป็น artifact ที่วิศวกรต้องตรวจและอนุมัติ ไม่ได้อ้างว่า numbered steps เป็น proof ว่า model เข้าใจ product semantics แล้ว ถ้าคนไม่ถาม assumption สำคัญ แผนที่อ่านครบก็ยังพลาดได้

**ผลคือ:** plan mode มีค่าตอนใช้เป็นพื้นที่ให้คนทัก risk ก่อนแก้ code ไม่ใช่เครื่องประทับว่า design ถูก

หน้า [[dynamic-workflows]] บันทึก claim ว่า Claude Code สามารถ self-plan และ dispatch subagents ได้. หน้าใหม่นี้ไม่ได้บอกว่าความสามารถนั้นไม่มี utility. มันบอกว่าคำว่า "self-plan" อาจหมายถึง harness-guided prompting ไม่ใช่ planner แบบ symbolic.

คำถามที่ควรเปิดไว้คือ งานชนิดไหนพอใช้ plan draft + verification gate ได้ และงานชนิดไหนต้องให้มนุษย์ออกแบบแผนเองก่อน.

## `plan.md` เป็น artifact ที่ commit ไม่ใช่แค่ขั้นตอนในหัว

[[ai-native-sdlc-playbook|Playbook ของ Anthropic]] ให้ plan mode เป็นจุดเริ่มปกติของช่วง Build แต่ไม่ได้หยุดแค่สั่งให้ agent วางแผนก่อน ยังมีเกณฑ์รับแผนและกฎกัน drift ตามมาด้วย

**เกณฑ์รับแผน** คือคนที่ไม่เคยเห็นบทสนทนานี้ต้องอ่านแล้วทำตามได้ ก่อนอนุมัติ engineer ต้องซักแผนว่าเสี่ยงตรงไหน มีทางอื่นไหม และจะพิสูจน์อย่างไร แผนที่ผ่านจะ commit เป็น `plan.md` พร้อมไฟล์ที่ต้องเปลี่ยน ลำดับงาน risk และหลักฐานที่ใช้ตัดสิน

**กฎกัน drift** ระบุว่าถ้างานจริงเบนจากแผน ต้องแก้ `plan.md` ใน commit เดียวกับ code ไม่ใช่ปล่อยให้แผนค้างอยู่ที่ version แรก ตัววัดที่เสนอคือความถี่ที่ diff หลัง merge ยังตรงกับ `plan.md` ค่านี้ช่วยบอกว่า [[artifact-chain|artifact chain]] ยังตามงานจริงอยู่หรือกลายเป็นเพียงพิธีกรรม

ข้อจำกัดเดิมยังอยู่: แผนที่อ่านแล้วครบไม่ได้แปลว่าครบจริง `plan.md` ที่ commit แล้วก็ยังเป็น prose ที่ตกสมมติฐานสำคัญได้

**ผลคือ:** reviewer เห็นทั้งทางที่เลือกและ diff ไม่ใช่เห็นแต่ผลลัพธ์สุดท้าย

## See also

- [[zoran-horvat-claude-no-planning-engine]]
- [[planning-mode-dangerous-illusion]]
- [[coding-harness]]
- [[dynamic-workflows]]
- [[judgement-vs-automation]]
- [[grounding]]
- [[agentic-code-review]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[intent-md]]
- [[artifact-chain]]
- [[ai-native-sdlc-playbook]]
