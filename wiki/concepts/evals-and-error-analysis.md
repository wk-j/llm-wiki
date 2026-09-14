---
title: Evals and Error Analysis
type: concept
tags: [ai, evals, testing, reliability, llm]
created: 2026-08-15
updated: 2026-09-14
sources: [andrew-ng-ai-engineering-skills-map.md, the-new-software-lifecycle.md, claude-codes-new-intent-md-rob-shocks.md, boris-cherny-cut-80-percent-claude-code-prompt.md, ai-native-sdlc-playbook.md]
---

# Evals and Error Analysis / วัดผลกับไล่หาสาเหตุที่ผิด

หน้านี้ว่าด้วยทักษะที่ [[andrew-ng|Andrew Ng]] เรียกว่าเป็น **แกนกลาง** ของการสร้างแอป AI ให้ใช้งานได้จริง:

> "A core skill in doing so is knowing how to drive disciplined evals and error analysis loops."

**Eval** คือชุดการวัดว่าระบบ AI ทำงานได้ดีแค่ไหน — คล้าย test แต่วัดคุณภาพของ output ที่ไม่ตายตัว ไม่ใช่วัด pass/fail ของ logic เดียว **Error analysis** คือการไล่ดูตัวอย่างที่พังจริง ๆ แล้วจัดกลุ่มว่าพังเพราะอะไร เพื่อจะได้รู้ว่าควรไปแก้ตรงไหนก่อน

## ทำไมงาน AI ถึงต้องใช้สองอย่างนี้

จุดตั้งต้นของ Ng คือความต่างข้อเดียวระหว่างแอป AI กับแอปธรรมดา: **output เดาไม่ได้**

พอ prompt ตัว LLM เราไม่รู้ว่าจะได้อะไรกลับมา พอ train deep learning เราไม่รู้ว่ามันจะทำนายอะไรกับข้อมูลใหม่ ส่วน software แบบเดิมพฤติกรรมนิ่งกว่ามาก ([[llm-nondeterminism]] อธิบายกลไกเบื้องหลังไว้ว่าความไม่แน่นอนมาจากชั้น infrastructure ด้วย ไม่ใช่แค่ชั้น prompt)

ทีนี้พอผลไม่นิ่ง วิธีตัดสินแบบเดิม — รันแล้วดูว่าถูกไหม — ใช้ไม่ได้ เพราะ "ถูก" ในรอบนี้ไม่รับประกันรอบหน้า Ng เลยบอกว่าต้องใช้ **เทคนิคเชิงสถิติเพื่อวัด บังคับทิศ และกำกับ (measure, steer, govern)** ระบบ AI ให้พฤติกรรมคาดเดาได้มากขึ้น

**ได้อะไร:** เราไม่ได้ทำให้ AI นิ่งเหมือน software เดิม แต่ทำให้ความไม่นิ่งของมันวัดได้และอยู่ในกรอบที่รับได้

## คำว่า "disciplined" สำคัญตรงไหน

คำนี้เป็นคำแยกระหว่างการทำ eval จริงกับการลองไปเรื่อย ๆ

วิธีที่คนส่วนใหญ่ทำโดยไม่รู้ตัวคือ แก้ prompt แล้วลอง 3-4 เคส รู้สึกว่าดีขึ้น ก็ปล่อย ปัญหาคือ 3-4 เคสนั้นเป็นเคสที่เราจำได้ ซึ่งมักไม่ใช่เคสที่ผู้ใช้จริงเจอ พอเปลี่ยน prompt อีกรอบเพื่อแก้เคสใหม่ ของเก่าก็อาจพังโดยไม่มีใครรู้

วินัยที่ต่างออกไปคือ: มีชุดตัวอย่างคงที่ที่รันซ้ำได้, มีเกณฑ์ตัดสินที่เขียนไว้ก่อนดูผล, และรันทุกครั้งที่เปลี่ยนอะไรก็ตาม ไม่ใช่เฉพาะตอนสงสัย

**ผลคือ:** ความรู้สึกว่า "น่าจะดีขึ้น" ถูกแทนด้วยตัวเลขที่เทียบข้ามรอบได้

## Loop ไม่ใช่ขั้นตอนเดียวจบ

Ng ใช้คำว่า **loop** ไม่ใช่ step วงรอบที่ว่ามีหน้าตาประมาณนี้:

1. รัน eval กับชุดตัวอย่างที่มี แล้วดูว่าคะแนนเท่าไร
2. หยิบเคสที่พังมาอ่านจริง ๆ ทีละอัน
3. จัดกลุ่มความพัง เช่น "retrieval ดึงเอกสารผิด 40%", "ตอบถูกแต่ format เพี้ยน 25%", "ปฏิเสธทั้งที่ควรตอบ 15%"
4. เลือกกลุ่มที่ใหญ่ที่สุดไปแก้ก่อน — ซึ่งอาจไม่ใช่การแก้ prompt เลย อาจต้องไปแก้ retrieval หรือแก้ข้อมูล
5. รัน eval ใหม่ แล้วเพิ่มเคสที่เพิ่งเจอเข้าไปในชุดถาวร

ขั้นที่ 3 คือหัวใจของ error analysis จริง ๆ เพราะมันเปลี่ยนคำถามจาก "คะแนนตกไหม" เป็น "ตกเพราะอะไร และแก้ตรงไหนคุ้มที่สุด"

**ได้อะไร:** เวลาที่ใช้แก้ถูกจัดสรรตามความถี่ของความพังจริง ไม่ใช่ตามเคสที่บังเอิญนึกออก

## Eval ในฐานะเครื่องมือให้ agent ปิด loop เอง

ในแผนที่ทักษะของ Ng ข้อ *using coding agents* พูดถึง eval อีกรอบในบทบาทที่ต่างออกไป: ให้ verifier หรือ eval กับ agent เพื่อให้มัน **ปิด loop ได้เองโดยไม่ต้องรอคน**

ถ้า agent มีเกณฑ์ตัดสินที่รันเองได้ มันจะรู้ว่างานเสร็จหรือยัง แทนที่จะเดาแล้วหยุด นี่เชื่อมตรงกับ [[behavioral-verifier]], [[loop-engineering]] และ [[harness-guides-sensors]] ซึ่งจัดให้ eval/test เป็น **sensor** ที่ป้อน feedback กลับเข้า loop

**ผลคือ:** eval ไม่ได้มีไว้ให้คนอ่านรายงานอย่างเดียว มันเป็นสิ่งที่ทำให้ปล่อย agent ทำงานยาว ๆ ได้อย่างมีเหตุผล

## ตรวจทั้งคำตอบและเส้นทางที่ใช้

[[the-new-software-lifecycle|Addy Osmani]] แยก eval อีกแกนที่ช่วยจับงาน “หน้าตาถูกแต่ทำผิดวิธี”:

- **Output evaluation** ถามว่าผลสุดท้ายตรง rubric หรือไม่
- **Trajectory evaluation** ถามว่า agent เรียก tool, ขอ permission และรัน check ตามขั้นที่ควรหรือไม่

ตัวอย่างเช่น agent แก้ bug แล้ว test ผ่านอาจผ่าน output eval แต่ถ้ามันลบ regression test ทิ้งเพื่อให้เขียว trajectory eval ต้องจับได้ ตรงนี้ต่อกับ [[behavioral-verifier]] และหลัก maker/checker split: อย่าให้ผลลัพธ์สุดท้ายที่ดูดีลบหลักฐานว่าระหว่างทาง agent ข้าม safety gate

อย่างไรก็ดี trajectory eval ไม่ควรกลายเป็นการบังคับ agent ให้เดินเส้นเดียวทุกครั้ง เส้นทางอาจต่างกันแต่ยังปลอดภัยและถูกต้องได้ Rubric จึงควรตรวจ invariant สำคัญ ไม่ใช่ micromanage ทุก tool call

**ได้อะไร:** “ถูก” หมายถึงทั้งได้ของที่ต้องการและมีหลักฐานว่าไม่ได้แลกความถูกต้องหรือความปลอดภัยทิ้งระหว่างทาง

## Regression eval ตอนเปลี่ยน model หรือ skill

[[claude-codes-new-intent-md-rob-shocks|คลิปของ Rob Shocks]] เสนออีก use case: เก็บ issue หรือ task เก่าพร้อม expected outcome แล้วรันใหม่ทุกครั้งที่เปลี่ยน model, skill หรือ workflow หลัก Rob ยกชุดราว 20 เคสเป็นตัวอย่าง ไม่ใช่จำนวนมาตรฐาน

Eval ชุดนี้ไม่ได้วัด product output อย่างเดียว แต่วัดว่า harness ทั้งเส้น regress หรือไม่ เพราะการเปลี่ยน skill อาจทำให้ agent ข้าม policy การเปลี่ยน model อาจทำให้ plan หรือ tool use เปลี่ยน และการเปลี่ยน hook อาจทำให้งานผ่านหรือถูกบล็อกคนละแบบ

**ผลคือ:** model กับ skill upgrade กลายเป็น change ที่ต้องผ่าน regression gate เหมือน code ไม่ใช่อัปเดตแล้วหวังว่าทุกอย่างดีขึ้นเอง

## Eval เองก็หมดอายุได้

[[boris-cherny|Boris Cherny]] เติมอีกด้านใน [[boris-cherny-cut-80-percent-claude-code-prompt|บทสัมภาษณ์กับ Y Combinator]]: eval มักอยู่ได้นานกว่า prompt หรือ harness แต่บางชุดก็อยู่เพียงหนึ่งถึงสาม model generations ก่อนคะแนนอิ่มตัว เมื่อ model ผ่านทุกข้อแล้ว eval นั้นเลิกบอกว่าจุดอ่อนใหม่อยู่ตรงไหน

วิธีไปต่อไม่ใช่เก็บโจทย์เดิมไว้เพราะต้องการกราฟยาวอย่างเดียว แต่ต้องใช้ product จริง ทำ error analysis กับความพลาดของ model รุ่นปัจจุบัน แล้วสร้าง eval ที่ยากและตรงกับ failure ใหม่ ในขณะเดียวกัน eval เดิมอาจยังเก็บไว้เป็น regression set ถ้ามันคุม behavior สำคัญ แม้จะแยกจาก frontier set ที่ใช้หาเพดานใหม่

[[prompt-ablation|Prompt ablation]] ใช้ eval ในทิศกลับด้วย: ไม่ใช่แค่ถามว่าควรเพิ่มกฎอะไร แต่ถามว่าลบกฎไหนแล้ว quality เท่าเดิมหรือดีขึ้น

**ผลคือ:** eval suite ควรมีทั้งส่วนที่เฝ้าของเก่าและส่วนที่ขยับตาม frontier ไม่ใช่ก้อนเดียวที่ใช้ตลอดไป

## ข้อควรระวัง

- eval ที่วัดง่ายไม่ได้แปลว่าวัดตรงกับสิ่งที่ผู้ใช้แคร์ ดู [[quality-proxy-collapse]] เรื่อง proxy คุณภาพที่พังโดยยังดูดีอยู่
- ถ้า agent รู้เกณฑ์ มันอาจเล่นงานกับเกณฑ์แทนที่จะแก้ปัญหาจริง ดู [[reward-hacking]]
- ใช้ model เป็นผู้ตัดสิน (LLM-as-judge) เป็น sensor แบบ inferential ซึ่งเชื่อได้ไม่เต็มร้อยและไม่ควรเป็นด่านเดียว
- ชุด eval ที่ไม่เคยอัปเดตจะค่อย ๆ เลิกสะท้อนงานจริง โดยเฉพาะเมื่อเปลี่ยนรุ่น model

## Continuous evals: เอา eval ไปวางใน CI เพื่อทดสอบตัวที่กำกับ agent

[[ai-native-sdlc-playbook|Playbook ของ Anthropic]] แยก test สองชนิดออกจากกัน test ธรรมดาทดสอบ code ส่วนชุดนี้ทดสอบ **configuration ที่กำกับ agent** ได้แก่ [[claude-md|`CLAUDE.md`]], skills และ hooks

วิธีที่เสนอคือเก็บงานจริงล่าสุดสัก 20-50 เคสพร้อมผลที่ควรได้ แล้วรันชุดนี้ทุกครั้งที่มีคนแก้ config พวกนั้น ถ้า pass rate ตกก็ต้องมีคนดูก่อน merge

Skill เพียงหนึ่งบรรทัดอาจเปลี่ยนพฤติกรรมของทุก session พร้อมกัน ถ้าไม่มีชุดวัด การ "ปรับ prompt นิดหน่อย" ก็เท่ากับเปลี่ยน production behavior โดยไม่รู้ผล จึงต้องมี gate ตรงนี้ ดู [[prompt-ablation]]

อีกกฎหนึ่งคือ **ทุก incident ที่หลุดไป production กลายเป็น eval ถาวรหนึ่งเคส** ชุดวัดจึงโตตามความผิดพลาดที่เคยเจอจริง ไม่ใช่โตตามสิ่งที่คนเขียน eval นึกออก ตัววัดที่ตามมาคือ "incident ซ้ำ class เดิม" ซึ่งควรลดลงเมื่อ eval สะสมขึ้น

ข้อควรระวัง: 20-50 เคสเป็นตัวอย่างในเอกสาร ไม่ใช่ผลจากการวัด ถ้าชุดนั้นไม่แทนงานจริง pass rate ที่สวยก็ไม่ได้แปลว่าอะไร

**ได้อะไร:** policy กับ context ขององค์กรได้ CI เหมือน code ไม่ใช่ของที่แก้แล้วรอดูดวง

## ดูเพิ่ม

- [[andrew-ng-ai-engineering-skills-map]]
- [[ai-engineering-skills-map]]
- [[llm-nondeterminism]]
- [[behavioral-verifier]]
- [[harness-guides-sensors]]
- [[loop-engineering]]
- [[reward-hacking]]
- [[quality-proxy-collapse]]
- [[facts-first]]
- [[property-based-testing]]
- [[the-new-software-lifecycle]]
- [[ai-driven-sdlc]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[artifact-chain]]
- [[boris-cherny-cut-80-percent-claude-code-prompt]]
- [[prompt-ablation]]
- [[ai-native-sdlc-playbook]]
- [[control-bands]]
