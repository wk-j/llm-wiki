---
title: How a Cloudflare Engineer Ships Production Code He Didn't Write - Dillon Mulroy
type: source
author: Jan-Niklas Wortmann
url: https://www.youtube.com/watch?v=sYNOgpDKTvE
date_ingested: 2026-09-12
tags: [ai, coding-agents, software-engineering, code-review, developer-experience, cloudflare]
created: 2026-09-12
updated: 2026-09-12
sources: ["https://www.youtube.com/watch?v=sYNOgpDKTvE"]
---

# How a Cloudflare Engineer Ships Production Code He Didn't Write / เมื่อ Agent เขียนโค้ด แต่คนยังรับผิดชอบงาน Production

[[jan-niklas-wortmann|Jan-Niklas Wortmann]] (ผู้สัมภาษณ์ด้าน software engineering และ AI coding) คุยกับ [[dillon-mulroy|Dillon Mulroy]] (Principal Engineer ที่ [[cloudflare|Cloudflare]]) เรื่องชีวิตหลังเลิกเขียนโค้ดเองเกือบทั้งหมด Dillon บอกว่าหลังใช้ Claude Opus 4.5 มาราวหกเดือน เขา ship ได้มากกว่าที่เคย แต่สนุกกับงานน้อยลงและเหนื่อยกว่าเดิม

แกนของบทสนทนาไม่ใช่แค่ "AI เขียนโค้ดแทนได้แล้ว" Dillon ยังอ่านทุกบรรทัด ถือ accountability ไว้กับคน และวางกรอบงานก่อนให้ model ลงมือ จุดเปลี่ยนจริงอยู่ที่เนื้องานของมนุษย์ จากเดิมสลับระหว่าง design ยากกับ implementation ย่อย ๆ กลายเป็นต้องตัดสินปัญหาใหญ่ต่อเนื่องแทบทั้งวัน

## Productivity สูงขึ้น แต่ flow หายไป

Dillon แยกความยากของงานเป็นสองระดับ ตอนเริ่ม feature คนต้องออกแบบภาพใหญ่ เช่น data flow, API, storage, abstraction และ failure path หลังจากนั้นการลงมือเขียนเปิดช่วงพักทางความคิด มีโจทย์เล็กให้แก้ทีละข้อและได้ความรู้สึกสำเร็จต่อเนื่อง ช่วงนี้เคยพาเขาเข้า flow state

พอ agent รับ implementation ไป งานส่วนเล็กจำนวนมากหายไป แต่โจทย์ภาพใหญ่ยังอยู่ คนจึงขยับจาก macro problem หนึ่งไปอีก macro problem หนึ่งโดยแทบไม่มีช่วงผ่อน Dillon บอกว่าไม่ค่อยได้เข้า flow state ในหกเดือนที่ผ่านมา แม้ output สูงขึ้นมาก

เรื่องนี้เพิ่มกรณีที่สามให้ [[creative-ownership|Creative Ownership]] เดิม Typecraft กับ Phoomparin Mano เล่าความรู้สึกห่างจากงาน ส่วน DHH เล่าว่าหลาย agent ทำให้ flow กลับมา Dillon อยู่กึ่งกลาง เขายังควบคุม design และอ่านงานทั้งหมด แต่เสีย micro-decision ที่เคยให้ความสุข

**ผลคือ:** throughput, quality, flow และความสุขจาก craft เป็นคนละตัววัด งานอาจดีขึ้นในตัวหนึ่งพร้อมแย่ลงในอีกตัวได้

## คนยังต้องเป็นเจ้าของผลลัพธ์

Dillon ไม่ปล่อย cloud agent วิ่ง loop แล้ว commit เข้า codebase เอง เขาบอกว่าอ่าน code ทุกบรรทัด และใส่ principle ประสบการณ์ ความผิดพลาดเก่า และ judgement ของตัวเองลงในผลลัพธ์ คนที่ขับ LLM ยังต้องรับผิดชอบสิ่งที่ ship เหมือนเดิม เพียงแต่การตัดสินใจของคนหนึ่งส่งผลได้กว้างขึ้นในเวลาสั้นลง

เขาจำกัด change ให้เล็กและเป็นหน่วย งานหนึ่งหรือ PR หนึ่งมักอยู่ราว 300 ถึง 800 บรรทัด แล้วต่อกันเป็น [[stacked-pull-requests|stacked PR]] เมื่อมี dependency เป้าหมายไม่ใช่ตัวเลขตายตัว แต่คือขนาดที่เขายังอ่านครบ เข้าใจ scope และ ship แยกได้

สำหรับ review ก่อน push เขาใช้ [[plannotator|Plannotator]] เปิด diff ใน local web app หน้าตาคล้าย GitHub PR review ใส่ comment ทีละไฟล์ แล้วส่ง feedback กลับเข้า agent session จังหวะนี้ช่วยให้ AI-generated change ผ่านการอ่านของเจ้าของงานก่อนทีมเห็น PR

**ได้อะไร:** การอ่านทุกบรรทัดยังพอทำได้เมื่อ diff เล็กและ review loop อยู่ใกล้ implementation ถ้า agent สร้าง change ใหญ่กว่านั้นเร็วเกินไป วิธีนี้จะชน [[orchestration-tax|Orchestration Tax]] ทันที

## Spec ที่ใกล้ code มากกว่า PRD

Dillon ไม่เริ่มจาก PRD ยาวแล้วโยนให้ model implement รอบเดียว เขาคุยกับ agent จนมี shared understanding แล้วค่อยเก็บเป็น tech spec เนื้อหาใน spec ใกล้ code มาก:

- TypeScript types และ interfaces
- boundary ของระบบ รวมถึง adapter และ implementation ที่ต้องมี
- call stack เดิมที่จะแก้หรือ code path ใหม่ที่จะเพิ่ม
- input, output และ error ของแต่ละขั้น
- test ที่จะเขียนตามแนว red-green-refactor/TDD

เขามองว่า model ทำ function ที่กำหนดขอบเขตชัดได้ค่อนข้างดี ส่วนที่ยังต้องใช้แรงคนคือ design และการประกอบ abstraction หลายตัวให้เข้ากัน วิธีนี้จึงไม่ได้ลด spec เป็น prose instruction แต่ใช้ type, call path และ test บังคับ shape ของ solution

นี่เป็น counterexample ต่อ [[specs-to-code|Specs-to-Code]] แบบ "เขียนสเปกแล้วไม่ดูไส้ใน" เพราะ Dillon อ่านทั้ง spec และ code เอง ขณะเดียวกันก็ยังไม่หักล้าง [[facts-first|Facts-First]] เพราะ type กับ call stack ไม่ได้พิสูจน์ behavior ทั้งหมด ส่วน test ใน spec ต่างหากที่กลายเป็น executable fact ได้เมื่อเขียนและรันจริง

**ผลคือ:** spec ทำหน้าที่เป็น design boundary ให้คนกับ model เห็นภาพเดียวกัน ไม่ใช่ใบรับรองว่า implementation ถูกแล้ว

## `/tree` แทน subagent ที่สรุปให้เอง

[[pi-agent|pi]] ไม่มี subagent ติดมาเป็นแกนหลัก แต่มี `/tree` ให้ย้อนกลับไปจุดก่อนหน้าใน conversation โดยไม่ย้อน Git state ผู้ใช้เลือกได้ว่าจะกลับเฉย ๆ ให้ระบบสรุป หรือกำหนด prompt สำหรับสรุป

Dillon ใช้กิ่งย่อยสำรวจเรื่องหนึ่งทีละกิ่ง เช่น framework, storage API หรือ test setup เขามักถามคำถามที่ตัวเองรู้คำตอบอยู่แล้วเพื่อเช็กว่า agent เข้าใจ tech stack ตรงกัน จากนั้นคัดข้อความสุดท้ายด้วย `/copy` หรือให้เขียนลงไฟล์ Markdown แล้วกลับไปที่รากเพื่อสำรวจเรื่องถัดไป สุดท้ายเขานำเฉพาะ context ที่เห็นว่าจำเป็นกลับเข้าสายหลัก

เขาชอบวิธีนี้มากกว่า subagent เพราะ summary ของ subagent ถูกเลือกด้วย judgement ของ core agent และอาจทิ้งสิ่งที่เขาสนใจ การคุมกิ่งเองทำให้มนุษย์เป็นคนเลือกว่า context ใดควรมีผลต่อ implementation ข้อแลกเปลี่ยนคือ workflow ใช้แรงและความชำนาญสูง

**ได้อะไร:** tree session ไม่ได้ทำงานขนานแบบ agent fleet แต่มันให้ผู้ใช้ควบคุมการย่อ context และลด noise ก่อน model ออกแบบงาน

## Loop จาก AI lab ไม่ใช่ค่าเริ่มต้นของทุกทีม

Dillon ไม่ปฏิเสธว่า long-running loop หรือ dynamic workflow อาจใช้ได้ในอนาคต แต่เขามองว่า ณ วันที่สัมภาษณ์ 25 June 2026 วิธีนี้ยังไม่ practical สำหรับ median developer ต้นทุน token สูง คุณภาพเปลี่ยนตาม release และทีมทั่วไปไม่มีทรัพยากรเหมือน AI lab เขาต้องการหลักฐานเรื่องผลลัพธ์ ต้นทุน และความสม่ำเสมอมากกว่าคำบอกเล่า

ปลายทางที่เขาอยากได้กลับเป็นคิวที่มองเห็น งานในคิวค่อยพาเขาผ่าน research, spec, implementation และ review โดยเรียนรู้ว่าเขาชอบ type, call stack, interface และ test แบบไหน นี่ใกล้ [[queues-over-loops|Queues over Loops]] แต่ยังมีคนคุมแต่ละช่วง ไม่ใช่ queue ที่ agent หยิบไป ship เองทั้งหมด

เขายก Fable เป็นตัวอย่างข้อจำกัดของ production use โดยอ้างว่าไม่มี zero data retention และ auto-mode อาจ downgrade ไป Opus 4.8 จนเสีย prompt-cache economics กับ control ของผู้ใช้ ข้อมูลนี้เป็นคำกล่าวในบทสัมภาษณ์ ไม่ได้ตรวจเทียบ product terms หรือเอกสารของ Anthropic ในการ ingest ครั้งนี้

**ผลคือ:** คำว่า autonomous ต้องแยก capability ออกจาก economics, data policy, consistency และ review capacity ของทีม

## บทบาทกว้างขึ้น แต่ specialization ยังไม่หาย

Dillon มองว่า engineer ที่ดีควรเข้าใจ product และผู้ใช้ลึกขึ้น AI ช่วยให้ engineer ทำ QA หรือสำรวจ codebase ของทีมอื่นได้เร็ว ขณะเดียวกัน product manager ก็สร้าง MVP หรือ prototype เพื่อสื่อสารกับ engineer ได้ตรงกว่า PRD อย่างเดียว

เขาไม่ได้สรุปว่าทุกตำแหน่งควรถูกรวมเป็น product engineer คนเดียว ผู้ร่วมสนทนาทั้งสองเห็นตรงกันว่าเส้นแบ่งงานพร่าขึ้น แต่ความเชี่ยวชาญเฉพาะยังมีค่า ประเด็นที่ยังตอบไม่ได้คือจะฝึก developer รุ่นใหม่อย่างไร ถ้า agent ตัดช่วงดิ้นรน ลองผิด และเห็น architecture พังออกไปก่อนจะได้สร้าง intuition

ในเรื่องการลดคน Dillon เล่าว่า Cloudflare ลดพนักงานราว 20% หรือประมาณ 1,100 คนใน May 2026 และบอกว่า AI เป็นเหตุหลัก เขามองว่าคำอธิบายนี้จริงในระดับหนึ่ง เพราะบริษัทเปิดรับตำแหน่งชนิดอื่นจำนวนมากต่อทันที แต่ก็คิดว่า overhiring ในปีก่อนมีส่วนด้วย ข้อนี้เป็นมุมจากพนักงานคนหนึ่ง Transcript ที่ให้มาไม่มีประกาศบริษัท ตัวเลข staffing รายละเอียดตำแหน่ง หรือหลักฐานที่แยกสองเหตุออกจากกัน

**ได้อะไร:** role compression อาจเปลี่ยนส่วนผสมของงานและตำแหน่งจริง แต่ source เดียวไม่พอใช้พิสูจน์ว่า AI เป็นเหตุของ layoff ทั้งหมด

## ขอบเขตของหลักฐาน

- Transcript ระบุว่าบทสนทนาเกิดวันที่ 25 June 2026 แต่ข้อมูลที่ให้มาไม่ได้ยืนยันวันเผยแพร่วิดีโอ
- Productivity, ความเหนื่อย คุณภาพ และสัดส่วน code ที่ไม่ได้เขียนเองเป็น self-report ของ Dillon ไม่มี telemetry เรื่อง defect, cycle time, cost หรือเวลาที่ใช้ review
- คำอธิบาย Cloudflare layoff และตำแหน่งงานที่เปิดใหม่เป็นมุมจากภายในของ Dillon ยังไม่ได้ตรวจเทียบประกาศบริษัทหรือข้อมูล workforce
- ข้ออ้างเรื่องราคา ความสม่ำเสมอ zero data retention และ model downgrade ของ Fable ผูกกับ product state ตอนสัมภาษณ์และยังไม่ได้ตรวจจากเอกสารทางการ
- Transcript ถอดชื่อบางคำคลาดเคลื่อน หน้านี้ใช้ `Ghostty`, `Herdr`, `pi` และ `Plannotator` ตามชื่อใน description ที่ผู้ใช้ส่งมา

## See also

- [[dillon-mulroy]]
- [[jan-niklas-wortmann]]
- [[cloudflare]]
- [[pi-agent]]
- [[herdr]]
- [[plannotator]]
- [[creative-ownership]]
- [[ai-work-intensification]]
- [[developer-balance]]
- [[agentic-code-review]]
- [[tree-structured-sessions]]
- [[stacked-pull-requests]]
- [[subagent-patterns]]
- [[queues-over-loops]]
- [[specs-to-code]]
- [[engineering-role-shift]]
- [[fable]]
