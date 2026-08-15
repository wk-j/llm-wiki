---
title: Software Is Made Between Commits
type: source
tags: [zed, deltadb, version-control, collaboration, agents, provenance]
created: 2026-08-15
updated: 2026-08-15
url: https://zed.dev/blog/introducing-deltadb
author: Nathan Sobo
date_ingested: 2026-08-15
sources: ["https://zed.dev/blog/introducing-deltadb"]
---

# Software Is Made Between Commits / ซอฟต์แวร์เกิดขึ้นระหว่าง commit

บทความของ [[nathan-sobo|Nathan Sobo]] (ผู้ร่วมก่อตั้ง Zed และผู้เขียนบทความนี้) เสนอว่า commit เก็บได้เพียงภาพเป็นช่วง ๆ แต่การตัดสินใจสำคัญเกิดตอนคนกับ [[agentic-engineering|coding agent]] คุยและแก้ code ไปพร้อมกัน ถ้าแยกบทสนทนาออกจากไฟล์ เราต้องค่อยเอาเหตุผลกลับไปผูกกับ diff หรือ Pull Request (PR) ทีหลัง และบางส่วนก็หายไประหว่างทาง

ทางออกที่ [[zed-industries|Zed Industries]] เสนอคือ [[deltadb|DeltaDB]] ระบบ version control ที่บันทึกทั้งการเปลี่ยนแปลงย่อยและบทสนทนาที่ทำให้เกิดการเปลี่ยนแปลงนั้น บทความนี้เป็นประกาศจากทีมผู้สร้าง จึงบอกทิศทางของ product ได้ดี แต่ยังไม่ใช่หลักฐานว่าระบบใช้ได้ครบตาม claim ในงานจริง

## จาก snapshot ของ commit ไปสู่ทุก operation

Git จับ snapshot เมื่อมี commit ส่วน DeltaDB แบ่งงานเป็น stream ของ `delta` ขนาดเล็ก ทุก operation มี identity คงที่ จึงอ้างถึง code ณ จุดใดจุดหนึ่งระหว่างการแก้ได้ แม้ไฟล์จะเปลี่ยนต่อหลังจากนั้น

ข้อความของ agent กับ edit ที่เกิดจากข้อความนั้นถูกเก็บเคียงกัน ทำให้ version ของ worktree และบทสนทนาที่ขับมันเดินไปด้วยกัน ไม่ต้องรอ commit ก่อนจึงเริ่มชี้ว่าเหตุผลใดสร้าง code ส่วนไหน

**ได้อะไร:** จุดอ้างอิงละเอียดกว่า commit และเก็บ “เหตุใดจึงแก้” ไว้ใกล้กับ “แก้อะไร” ตั้งแต่ต้น

## Shared worktree ที่คนและ agent แก้พร้อมกัน

DeltaDB ฝัง replicated worktree ที่ผู้เขียนบอกว่า conflict-free คนและ agent หลายตัวจึงแก้ไฟล์เดียวกันข้ามเครื่องได้พร้อมกัน ไฟล์ยังเป็นไฟล์จริง: agent ใช้ผ่าน terminal ได้ และผู้ใช้ mount worktree ลง disk เพื่อเปิดด้วยเครื่องมืออื่นได้

คำว่า conflict-free ตรงนี้ควรอ่านอย่างระวัง [[crdts|CRDT]] ช่วยให้ replica รวม operation กันได้โดยไม่ทำ state สูญหาย แต่ไม่ได้แปลว่า edit สองชุดจะเข้ากันทางความหมาย ตัวอย่างเช่น agent สองตัวอาจแก้ API คนละทิศจน code compile ไม่ผ่านได้ แม้ระบบรวมตัวอักษรได้ครบ

**ได้อะไร:** ลดปัญหาการ sync ไฟล์และเปิดให้ร่วมมือระหว่างที่งานยังเคลื่อนไหว แต่ยังต้องมี validation และการตัดสินใจร่วมเพื่อคุมความถูกต้องของ software

## Source code กลายเป็น source conversation

แก่นใหม่คือ [[conversation-code-provenance|conversation-code provenance]] (การย้อนจาก code ไปหาเหตุผลในบทสนทนาและย้อนกลับได้) การอ้างอิงผูกกับ delta ไม่ใช่ line number จึงยังอยู่เมื่อ code ถูกย้ายหรือแทรกบรรทัดเพิ่ม

- จากบรรทัดในบทสนทนา ผู้ใช้เปิดดู code ในสภาพปัจจุบันหรือสภาพตอน agent เขียนได้
- จากบรรทัดของ code ผู้ใช้หาได้ว่าบทสนทนาใดสร้างมัน และมีบทสนทนาใดแตะมันต่อ
- agent รุ่นหลังดึงบริบทของ code ที่กำลังแก้ หรือถาม agent ก่อนหน้าว่าเหตุใดจึงเขียนแบบนั้นได้

**ได้อะไร:** history ไม่ได้ตอบแค่ว่า code เปลี่ยนอย่างไร แต่พยายามเก็บเหตุผลและเส้นทางการตัดสินใจไว้เป็นข้อมูลที่ค้นกลับได้

## ร่วมมือก่อน commit ไม่ใช่ลบ Git ทิ้ง

Sobo วิจารณ์ PR ว่าเป็นพิธีที่เอาบทสนทนากลับไปผูกกับ snapshot หลังเหตุการณ์สำคัญผ่านไปแล้ว เขาอยากให้เพื่อนร่วมทีมเข้ามาระหว่างที่งานยังเกิด คุยกับ agent ที่ทำงาน และ annotate code ได้ทันทีโดยไม่ต้องรอ commit กับ push

แต่บทความไม่ได้เสนอให้เลิก Git หรือ continuous integration (CI) กลับวาง Git กับ CI ไว้เป็นชั้นที่รัน check และเชื่อมงานออกสู่ ecosystem ภายนอก ความต่างคือไม่บังคับให้ GitHub/PR เป็นพื้นที่หลักของ collaboration

จุดนี้ชนกับ [[stacked-pull-requests|stacked pull requests]] บางส่วน เอกสาร GitHub มอง PR เล็กหลายชั้นเป็นหน่วย review และ quality gate ที่จัดการได้ ส่วน Sobo มองว่า discussion สำคัญควรเกิดก่อน commit ทั้งสองอาจอยู่ร่วมกันได้: DeltaDB ดูแลงานที่กำลังก่อตัว ส่วน PR/Git ดูแล integration gate แต่ source ยังไม่อธิบายว่า evidence จากบทสนทนาจะส่งต่อเข้า review, approval และ audit ภายนอกอย่างไร

**ผลคือ:** สิ่งที่ถูกท้าทายไม่ใช่คุณค่าของ commit แต่คือการใช้ commit เป็นเงื่อนไขว่าทีมจึงจะเริ่มคุยกับ code ได้

## สถานะและขอบเขตหลักฐาน

บทความบอกว่า beta จะพร้อมใน “อีกไม่กี่สัปดาห์” และชวนผู้อ่านเข้ารอทดลอง แต่ข้อความที่ให้มาไม่มีวันเผยแพร่ จึงไม่ควรแปลงคำนี้เป็นวันเปิดตัวแน่นอน

Source นี้ยังไม่ให้รายละเอียดเรื่อง data model, storage cost, access control, retention ของบทสนทนา, offline recovery, semantic conflict, performance, การเชื่อมกับ Git host หรือวิธีเรียก agent เก่ากลับมา จึงควรเก็บทุกอย่างเหล่านี้เป็นคำถามเปิด ไม่ใช่อนุมานจากคำว่า version control หรือ CRDT

สถานะยังมี tension กับ [[zed-is-1-0|Zed is 1.0]] ซึ่งเรียก DeltaDB ว่า synchronization engine และวางเป็นฐานของ Zed 1.0 แล้ว บทความใหม่กลับเรียกมันว่า version control และบอกว่า beta กำลังจะมา อาจเป็นการขยาย product จาก engine ภายในไปเป็น surface สำหรับผู้ใช้ หรือเป็นเพียงการเปลี่ยน framing; source สองชิ้นยังตอบไม่ได้

## คำถามเปิด

- DeltaDB จะส่ง provenance ไปกับ Git commit, PR หรือ repository อื่นได้มากแค่ไหน?
- ทีมกำหนดสิทธิ์ดู ลบ และเก็บบทสนทนาที่อาจมีข้อมูลลับอย่างไร?
- เมื่อ CRDT รวม edit ได้แต่ความหมายของ code ขัดกัน ระบบจะพาคนหรือ agent ไป resolve ตรงไหน?
- การ “ถาม agent ก่อนหน้า” หมายถึงเรียก session/model เดิมจริง หรือสร้างคำตอบใหม่จาก transcript ที่เก็บไว้?
- ทีมควรเลือก shared worktree แบบ DeltaDB หรือ isolation แบบ [[git-worktrees|Git worktree]] ตามชนิดงานอย่างไร?

## See also

- [[deltadb]]
- [[conversation-code-provenance]]
- [[collaborative-ai-engineering]]
- [[zed]]
- [[nathan-sobo]]
- [[stacked-pull-requests]]
- [[git-worktrees]]
