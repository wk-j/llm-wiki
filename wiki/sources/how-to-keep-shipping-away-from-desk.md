---
title: How to Keep Shipping When You Walk Away from Your Desk
type: source
tags: [ai, agents, developer-experience, attention, burnout, harness, claude-code]
created: 2026-06-11
updated: 2026-06-11
sources: [How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md]
url: https://www.youtube.com/watch?v=so9l_MwS2yg
author: Zack Proser
published: 2026-06-11
---

# How to Keep Shipping When You Walk Away from Your Desk / ทำงานต่อได้แม้ลุกจากโต๊ะ

Talk ของ [[zack-proser|Zack Proser]] (วิศวกรทีม Applied AI ที่ [[workos|WorkOS]]) เสนอวิธีใช้ coding agent ให้ทำงานต่อได้โดยไม่ต้องนั่งเฝ้าหน้าจอทั้งวัน. แก่นของ talk ไม่ใช่ "ทำยังไงให้ agent ผลิตงานมากขึ้น" แต่คือ **ทำยังไงให้คนยังรักษาสมาธิ สุขภาพ และ judgement ได้ ตอน agent ผลิตงานเร็วกว่าที่คนจะตามทัน**.

ประโยคสรุปของ Zack คือ:

> "The tools are nuclear now. Our nervous systems are still ancient."

เครื่องมือ scale ได้ แต่ระบบประสาทของคนไม่ scale ตาม. ถ้าปล่อยให้จำนวนงานโตตามกำลัง agent ตรง ๆ ทางปกติจะจบที่ burnout เร็วขึ้น. ดู concept หลักที่ [[developer-balance|Developer Balance]].

## ปัญหา: Agent ไม่ใช่คอขวดแล้ว คนต่างหาก

Zack เริ่มจากประสบการณ์ที่หลายคนเจอเหมือนกัน: ใช้ agent แล้วทำงานได้มากกว่าเดิม แต่หมดแรงตั้งแต่ 11 โมง เพราะต้องสลับ context และคอยตรวจงานหลายเส้นพร้อมกัน. เขายกคำพูดของ [[simon-willison|Simon Willison]] ว่าเปิด agent ขนานสี่ตัวแล้วหมดแรงก่อนเที่ยง.

จุดสำคัญคือ agent อาจวนทำงานจนผ่านเกณฑ์ได้แทบไม่จำกัด แต่คนยังต้องรับผิดชอบเรื่องที่ขนานไม่ได้:

- ตัดสินว่าโจทย์ธุรกิจถูกแก้จริงหรือยัง
- ใช้ taste และ judgement กับทางเลือกที่ไม่มี test ตัดสินให้
- review คุณภาพก่อน ship
- รักษา mental model ของระบบ

ตรงนี้คือปัญหาเดียวกับ [[orchestration-tax|Orchestration Tax]]: การเปิด agent ถูก แต่การปิด loop ด้วย judgement ของคนแพง.

**ผลคือ:** เป้าหมายไม่ควรเป็นการเปิด agent ให้มากที่สุด แต่เป็นการออกแบบวันทำงานให้ agent รับงานที่ตรวจเองได้ และเก็บ attention ของคนไว้กับ judgement.

## ตัวอย่าง loop ที่ปิดได้เอง

Zack เล่า bug ใน Slack bot ของ WorkOS ที่แปลงข้อความเป็น blog post. ตัว sentence-case enforcer ทำ acronym อย่าง `SCIM` และ `SSO` พัง. เขาให้ [[claude-code|Claude Code]] เข้าถึงทั้ง Slack และ Linear ผ่าน [[model-context-protocol|MCP]] แล้วสั่งให้:

1. แก้ bug
2. ส่ง input เข้า Slack channel จริง
3. ปล่อย blog bot รัน workflow จริง
4. ตรวจ output ว่า acronym ไม่พัง
5. ห้ามหยุดจนกว่าจะ verify ได้

พอกลับมาดู เขาไม่ได้เจอแค่ patch แต่เจอ **loop ที่ปิดแล้ว**: agent แก้และพิสูจน์ผลในระบบจริงเรียบร้อย.

> "Speed requires safety."

ความเร็วจะมีประโยชน์ก็ต่อเมื่อ agent มีเครื่องมือและเกณฑ์พิสูจน์งานของตัวเอง. ประโยคนี้ต่อกับ [[harness-guides-sensors|guides and sensors]], [[behavioral-verifier]], และ [[facts-first|facts-first]] โดยตรง.

## Stack สี่ชั้นสำหรับรักษาสมาธิ

Zack แบ่งวิธีทำงานเป็นสี่ชั้น. แต่ละชั้นลดเวลาที่คนต้องนั่งเฝ้าหรือสลับ context.

### 1. Signal layer: ให้ agent กรองสิ่งรบกวน

แทนที่จะเปิด Slack เองแล้วโดน thread อื่นดึงออกนอกงาน เขาให้ Claude Code อ่าน Slack เป็น loop เพื่อหา `@mention`, DM, และเรื่องสำคัญ แล้วเทียบกับ Linear เพื่อ deduplicate ว่าอะไรเป็น ticket จริง.

Signal layer ไม่ได้เอาคนออกจากวง. มันสร้าง facade บาง ๆ ที่กัน noise ออก แล้วส่งเฉพาะสัญญาณที่ต้องใช้ judgement ของคน.

**ได้อะไร:** คนไม่ต้องจ่าย context-switch cost เพื่อเปิดทุก inbox เอง.

### 2. Voice-first flow: ส่ง brief ให้เร็วขึ้น

Zack ใช้เสียงสั่งงานประมาณ **184 คำต่อนาที** เทียบกับพิมพ์เร็วสุดของตัวเองราว 90 คำต่อนาที. ประโยชน์ไม่ใช่แค่ prompt หนึ่งอันเร็วขึ้น แต่คือพูด brief ให้ agent หลายตัวแล้วปล่อยให้มันรันขนานได้.

ข้อควรระวังคือ ช่องทางส่งงานที่เร็วขึ้นยิ่งทำให้ [[orchestration-tax]] แรงขึ้น ถ้า review rate ไม่เพิ่มตาม.

**ได้อะไร:** ลดแรงเสียดทานตอนเริ่มงาน แต่ต้องคุมจำนวนงานให้เท่ากับกำลัง review.

### 3. Remote Control: เปลี่ยนจอ ไม่ได้ย้าย session

เขาเริ่ม session ที่โต๊ะบนเครื่องตัวเอง แล้วใช้ [[claude-code-remote-surfaces|Claude Code Remote Control]] คุยกับ session เดิมผ่านมือถือ แม้อยู่นอกบ้านและใช้ LTE. Agent ยังเห็น filesystem, tool, และ MCP บนเครื่องเดิม.

Zack ผูกวิธีนี้กับ **shower principle**: ตอนโฟกัสหนัก เราเก่งเรื่องดันงานให้เสร็จ แต่พอลุกเดินหรืออาบน้ำ สมองเข้า diffuse mode แล้วเห็นทางเลือกใหม่. แต่ก่อนการลุกจากโต๊ะหมายถึงหยุดงาน. Remote Control ทำให้ agent เดินงานต่อ ส่วนคนเปลี่ยนโหมดคิดและส่ง insight กลับได้ทันที.

**ได้อะไร:** ลดเวลานั่งโต๊ะและลดอาการบาดเจ็บจากการใช้งานซ้ำ ๆ โดยยัง steer งานได้.

### 4. System improvement: ใช้ประวัติการทำงานปรับ harness

Claude Code เก็บ conversation เป็นไฟล์ JSONL. Zack เสนอให้รัน agent ทุกสัปดาห์เพื่อหา session ที่:

- ใช้ thinking token เยอะผิดปกติ
- คนกับ agent ต้องถามกลับไปกลับมาเพราะโจทย์กำกวม
- เจอ churn หรือความผิดพลาดซ้ำ

จากนั้นให้เสนอ skill, MCP server, hook, หรือเครื่องมือที่ขาด เพื่อให้สัปดาห์ถัดไปทำงานลื่นขึ้น. ถ้า JSONL ดิบรกเกินไป ให้ hook สรุปจุดติดขัดตอนจบ session ลง Markdown ก่อน แล้วค่อยวิเคราะห์รวม.

นี่คือ [[harness-ratchet|Harness Ratchet]] จากข้อมูลการใช้งานจริง: อย่าทิ้ง conversation history เป็นขยะ ให้ใช้มันเป็นหลักฐานว่าระบบควรปรับตรงไหน.

**ได้อะไร:** การทำงานปกติกลายเป็นข้อมูลสำหรับลดปัญหาซ้ำในอนาคต.

## Verification gate สามระดับ

การเดินออกจากโต๊ะจะปลอดภัยขึ้นได้เมื่อ agent พิสูจน์งานเองก่อนเรียกคนกลับมา. Zack แบ่ง gate แบบง่าย:

| Gate | Agent ต้องพิสูจน์อะไร |
|---|---|
| **1. Code-level** | lint, build, unit test ผ่านทุกครั้งผ่าน hook |
| **2. Browser-level** | เปิด browser คลิก flow จริง เช่น login แล้วยืนยันว่าไม่พัง |
| **3. Critic-level** | agent อีกตัวตรวจตาม constitution หรือเกณฑ์ที่กำหนด แล้วส่ง feedback กลับให้แก้ |

ลำดับนี้ตรงกับ [[harness-guides-sensors]]: gate แรกเป็น computational sensor ที่เร็วและ deterministic; gate หลัง ๆ ใช้ browser และ inferential critic กับพฤติกรรมที่เช็คยากขึ้น.

**ผลคือ:** คนกลับมารับงานที่มีหลักฐานประกอบ ไม่ใช่ claim ว่า "เสร็จแล้ว".

## วันทำงานที่ Zack เสนอ

1. เริ่มวันด้วย deep-focus session เพื่อเลือกงานสำคัญ วางทิศ และเปิด work track
2. ส่งงานแยกอิสระให้ agent ผ่าน Codex, Claude Code, หรือ tool อื่น
3. ใช้ [[git-worktrees|git worktree]] เมื่อต้องรันหลายเส้นไม่ให้ชนไฟล์กัน
4. ลุกจากโต๊ะ เดิน หรือทำกิจกรรมอื่น แล้ว steer ผ่านมือถือเมื่อจำเป็น
5. review PR เป็น batch และใช้ comment บนมือถือส่งงานกลับไปแก้
6. ปลายสัปดาห์ให้ agent วิเคราะห์ประวัติ session แล้วปรับ harness

นี่ไม่ใช่การออกจาก loop. คนยังรับผิดชอบคุณภาพและการ ship อยู่ เพียงย้ายจากการเฝ้าทุก tool call ไปเป็นการกำหนดทิศ วาง gate และตรวจจุดสำคัญ.

## สุขภาพเป็น input ของระบบ

Zack เชื่อม Oura Ring ผ่าน MCP ให้ Claude เห็นข้อมูลการนอน. บางครั้ง Claude เตือนว่าเมื่อคืนไม่ได้นอน ควรทำแค่งานส่วนแรกแล้วพัก. เขายอมรับว่ายังฝืนคำเตือนอยู่ แต่ประเด็นคือเริ่มมองงานแบบองค์รวม: ticket, conversation, skill, เวลาโฟกัส, การนอน และสภาพร่างกายเป็น input ของระบบเดียวกัน.

มุมนี้ต่างจากการ optimize productivity ปกติ เพราะไม่ได้ถามแค่ว่า "ผลิตได้เท่าไร" แต่ถามว่า **ระบบนี้ทำให้คนกลับมาทำงานดีได้อีกในวันพรุ่งนี้ไหม**.

## ขอบเขตและคำเตือน

- วิธีนี้เหมาะที่สุดกับงานแยกชิ้นชัดและมี verification gate. งานใหญ่ที่แตะทั้ง stack ยังต้องใช้ worktree, agent team, spec/test ที่ชัด และ judgement ของคนมากขึ้น.
- Voice-first และ remote control ลดแรงเสียดทาน แต่ก็ทำให้สั่งงานเพิ่มง่ายขึ้น. ถ้าไม่คุม WIP อาจเร่ง burnout แทน.
- Conversation-history analysis เป็นข้อเสนอจากประสบการณ์ส่วนตัว ยังไม่มีข้อมูลว่าลดเวลาหรือข้อผิดพลาดได้เท่าไร.
- การให้ agent แตะ Slack, Linear, health data, และ local machine เพิ่มพื้นที่เสี่ยงด้าน permission, privacy, และ security.
- คำแนะนำสำหรับคนต้นอาชีพคือ **อย่า delegate งานที่ยังทำเองไม่เป็น**. ใช้ AI ช่วยถามและเรียนให้ลึกขึ้น แต่ยังต้องลงมือสร้าง mental model เพื่อกัน [[skill-atrophy|skill atrophy]].

## See also

- [[developer-balance]]
- [[zack-proser]]
- [[workos]]
- [[orchestration-tax]]
- [[harness-ratchet]]
- [[harness-guides-sensors]]
- [[claude-code]]
- [[claude-code-remote-surfaces]]
- [[git-worktrees]]
- [[skill-atrophy]]
- [[simon-willison]]
