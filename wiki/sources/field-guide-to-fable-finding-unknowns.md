---
title: "A Field Guide to Fable: Finding Your Unknowns"
type: source
tags: [ai, agents, claude, fable, prompting, workflow, unknowns, html]
url: https://x.com/trq212/status/2073100352921215386
author: "[[thariq-shihipar|Thariq Shihipar (@trq212)]]"
date_ingested: 2026-07-04
created: 2026-07-04
updated: 2026-07-04
sources: [a-field-guide-to-fable-finding-your-unknowns.md]
---

# A Field Guide to Fable: Finding Your Unknowns / คู่มือภาคสนามสำหรับ Fable: หา unknowns ของตัวเองให้เจอ

บทความยาวบน X ของ [[thariq-shihipar|Thariq Shihipar (@trq212)]] (Member of Technical Staff ทีม [[claude-code|Claude Code]] คนเดียวกับที่เขียนเรื่อง [[thariq-html-effectiveness|HTML effectiveness]]) เล่าวิธีทำงานกับ **Claude Fable 5** — model รุ่นใหม่ของ [[anthropic|Anthropic]] ในตระกูล [[claude|Claude]] แก่นของบทความคือ พอ model เก่งขึ้นถึงระดับนี้ คอขวดของคุณภาพงานย้ายจากตัว model มาอยู่ที่ตัวเรา: เราจะเคลียร์ "unknowns" — ช่องว่างระหว่างสิ่งที่เราบอก Claude กับสภาพจริงของงาน — ได้เร็วแค่ไหน

> "Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns."
> — Fable เป็น model ตัวแรกที่เขารู้สึกว่าคุณภาพงานถูกจำกัดด้วยความสามารถของ *ตัวเขาเอง* ในการเคลียร์ unknowns ไม่ใช่ความสามารถของ model

## แผนที่ไม่ใช่พื้นที่จริง / Map vs Territory

Thariq เปิดด้วยบทเรียนเก่าจากปรัชญา: [[map-vs-territory|the map is not the territory]] (แผนที่ไม่ใช่พื้นที่จริง)

> "The map, a representation of the work to be done, is my prompts and skills and context, it's what I give Claude. The territory is where the work needs to happen, the codebase, the real world, its actual constraints."
> — แผนที่ = prompt + skills + context ที่เราส่งให้ Claude ส่วนพื้นที่จริง = codebase, โลกจริง, และข้อจำกัดจริงของงาน

ช่องว่างระหว่างสองอย่างนี้คือสิ่งที่เขาเรียกว่า **unknowns** พอ Claude เจอ unknown มันต้องเดาว่าเราต้องการอะไรจาก best guess ยิ่งปริมาณงานเยอะ ยิ่งเจอ unknowns บ่อย

จุดสำคัญ: วางแผนล่วงหน้าอย่างเดียวไม่พอ เพราะ unknowns โผล่ได้ลึกกลางทาง implementation หรือบางทีก็ชี้ว่าเราควรแก้ปัญหาด้วยวิธีอื่นไปเลย การทำงานกับ Fable จึงเป็น loop วนซ้ำของการหา unknowns **ก่อน / ระหว่าง / หลัง** ลงมือ

**ผลคือ:** โจทย์ไม่ใช่ "เขียน prompt ให้เป๊ะขึ้น" แต่คือ "รู้ให้เร็วขึ้นว่าตัวเองยังไม่รู้อะไร"

## Unknowns 4 แบบ

Thariq แตกปัญหาออกเป็น 4 ช่อง (ดู [[unknowns-matrix|Unknowns Matrix]]):

- **Known Knowns** — สิ่งที่เรารู้และบอกไปแล้ว = เนื้อหาใน prompt
- **Known Unknowns** — สิ่งที่ยังคิดไม่จบ แต่อย่างน้อยรู้ตัวว่ายังไม่รู้
- **Unknown Knowns** — สิ่งที่ชัดกับเราจนไม่คิดจะเขียนลงไป แต่พอเห็นของจริงจะจำได้ทันทีว่า "ใช่/ไม่ใช่อันนี้"
- **Unknown Unknowns** — สิ่งที่ไม่เคยนึกถึงเลย รวมถึงไม่รู้ด้วยซ้ำว่า "ของดี" หน้าตาเป็นยังไง

เขายกตัวอย่างนักเขียน prompt ที่เก่งที่สุดที่เขาเคยเห็น เช่น [[boris-cherny|Boris Cherny]] (ผู้สร้าง Claude Code) กับ Jarred Sumner (ผู้สร้าง Bun) ว่าคนพวกนี้มี unknowns น้อยมาก เพราะ in-sync ทั้งกับ codebase และพฤติกรรมของ model — แต่ก็ยัง *เผื่อใจ* ว่ามี unknowns อยู่เสมอ

> "In many ways, reducing and planning for your unknowns is the **skill** of agentic coding."
> — การลดและเผื่อแผนสำหรับ unknowns นี่แหละคือ "ทักษะ" ของ agentic coding และฝึกได้โดยทำงานกับ Claude นั่นเอง

## Help Claude help you

สั่ง Claude คือการเดินบนเส้นบาง ๆ: สั่งละเอียดเกินไป Claude จะเดินตามคำสั่งแม้ตอนที่ควร pivot; สั่งกว้างเกินไป Claude จะเดาโดยอิง industry best practices ที่อาจไม่เข้ากับงานเรา ถ้าไม่จัดการ unknowns เราจะพลาดทั้งสองทาง

ข่าวดีคือ Claude ช่วยหา unknowns ของเราได้เอง: มันค้น codebase กับ internet เร็วกว่าเรามาก รู้เรื่องทั่วไปเยอะกว่าเรา และเรียนจาก failure ได้เร็วกว่า สิ่งสำคัญที่สุดคือ **บอกจุดตั้งต้นของเราให้ Claude รู้** — เราคิดมาถึงไหนแล้ว มีประสบการณ์กับปัญหา/codebase แค่ไหน แล้วให้มันทำงานแบบ thought partner

เกือบทุก pattern ในบทความ Thariq บอกว่า [[html-artifacts|HTML artifact]] คือสื่อที่ดีที่สุดในการ visualize (เขาทำ [example artifacts](https://thariqs.github.io/html-effectiveness/unknowns/) ไว้ให้ดูด้วย)

## เทคนิคก่อนลงมือ (Pre-implementation)

### Blind Spot Pass — จัดการ unknown unknowns

เหมาะกับตอนเข้าไปทำงานในพื้นที่ที่ไม่คุ้น เช่น feature ใน codebase ส่วนที่ไม่เคยแตะ หรืองาน domain ใหม่อย่าง design เพราะเราไม่รู้แม้แต่ว่าควรถามอะไร อะไรคือของดี มีงานเก่าอะไรอยู่แล้ว หรือหลุมไหนต้องเลี่ยง

วิธีคือสั่ง Claude ตรง ๆ ให้ช่วยหา unknown unknowns แล้วอธิบายให้ฟัง — Thariq ใช้คำว่า "blindspot pass" กับ "unknown unknowns" ตรง ๆ ในคำสั่งเลย และบอกด้วยว่าเราเป็นใคร รู้อะไรมาแล้วบ้าง

ตัวอย่าง prompt (verbatim): "I'm working on adding a new auth provider but I know nothing about the auth modules in this codebase. Can you do a blindspot pass to help me figure out my relevant unknown unknowns and help me prompt you better."

### Brainstorms และ prototypes — จัดการ unknown knowns

เหมาะกับงานที่เกณฑ์ตัดสิน "รู้ต่อเมื่อเห็น" เช่น visual design การเจอ unknown knowns ตอน prototype ถูกกว่าไปเจอตอน implementation มาก เพราะ spec ขยับนิดเดียว code เปลี่ยนโครงได้เยอะ และให้ agent revert ของเก่าก็ยาก เช่น อยากเห็นว่าปุ่มใหม่บน frame หน้าตาเป็นยังไง ไม่ต้องต่อ backend route จริง

Thariq เริ่มแทบทุก session ด้วย exploration/brainstorm ก่อน — Claude มักเจอทางเลือกดี ๆ ที่เขาคิดไม่ถึง (และบางทีก็หลงรายละเอียดจนพลาดภาพรวม) การ brainstorm ช่วยกัน scope ไม่ให้แคบหรือกว้างเกิน ตัวอย่าง prompt: ขอ HTML หน้าเดียวที่มี "4 wildly different design directions" ให้เลือก react หรือให้ค้น codebase แล้วเสนอ 10 จุด intervene เรียงจากถูกสุดไปทะเยอทะยานสุด

ตรงนี้คือแนวเดียวกับ [[throwaway-prototyping|Throwaway Prototyping]] ของ Matt Pocock

### Interviews — จัดการ known unknowns ที่เหลือ

brainstorm จบแล้วมักยังมีเรื่องคาใจ ให้ Claude สัมภาษณ์เรากลับ โดยให้ context ของปัญหาไว้นำคำถาม

ตัวอย่าง prompt (verbatim): "Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture."

pattern นี้คือ [[grill-me|Grill Me]] ของ Matt Pocock ในเวอร์ชันคนทีม Claude Code — สองแหล่งอิสระเสนอวิธีเดียวกัน

### References — ตอนบรรยายไม่ถูก

บางอย่างเราอธิบายเป็นคำพูดไม่ได้ (ไม่มีศัพท์ หรือซับซ้อนเกินจะพิมพ์) คำตอบที่ดีที่สุดคือ reference และ reference ที่ดีที่สุดคือ **source code** — ชี้ Fable ไปที่ folder ของ library ที่ทำสิ่งที่เราต้องการ แล้วบอกว่าให้ดูอะไร ต่อให้เป็นคนละภาษา programming ก็ได้ เช่น "Rust crate ใน vendor/rate-limiter ทำ backoff แบบที่ต้องการ ให้อ่านแล้ว reimplement semantics เดียวกันใน TypeScript API client"

Claude Design ก็ทำงานแบบนี้: ชี้ไปที่ module บนเว็บที่ชอบ มันจะอ่าน code ข้างใต้ ไม่ใช่แค่ดู screenshot — ได้รายละเอียด markup/โครงสร้างจริงของ component

### Implementation Plans — เรียงตามโอกาสที่จะแก้

พอคิดว่าพร้อมลงมือ ให้ Claude เขียน implementation plan ที่ **เอาส่วนที่มีโอกาสเปลี่ยนมากที่สุดขึ้นก่อน** — data model, type interface, UX flow — ส่วน mechanical refactoring ที่ไว้ใจได้ให้ฝังท้ายเอกสาร แบบนี้ Claude จะดันของที่เราอาจต้องแก้ขึ้นมาให้เห็นเอง แทนที่จะให้เราไล่อ่าน plan ยาวเท่ากันทุกส่วน

## เทคนิคระหว่างลงมือ (During implementation)

### Implementation notes

พอใจ plan แล้ว Thariq จะเปิด session ใหม่ แล้วส่ง artifacts (spec, prototype) เข้า prompt — แต่ต่อให้วางแผนดีแค่ไหน unknown unknowns ก็ยังซุ่มอยู่ agent อาจเจอ edge case ใน code ที่บังคับให้เปลี่ยนทาง

วิธีของเขา: สั่งให้ Claude Code เก็บไฟล์ `implementation-notes.md` (หรือ .html) ชั่วคราว บันทึกการตัดสินใจระหว่างทาง ตัวอย่าง prompt (verbatim): "Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate from the plan, pick the conservative option, log it under 'Deviations', and keep going."

**ได้อะไร:** deviation ไม่หายไปเงียบ ๆ ใน transcript — มันกลายเป็นบทเรียนสำหรับรอบถัดไป (ใกล้เคียงแนวคิด [[agent-handoff-documents|handoff documents]])

## เทคนิคหลังลงมือ (Post implementation)

### Pitches และ explainers

การ ship ต้องได้ buy-in กับ approval คนอ่าน (reviewer) มักเริ่มด้วย unknowns ชุดเดียวกับที่เราเคยมี — pitch/explainer artifact ที่ดีช่วยเร่งความเข้าใจ และช่วยให้ expert เห็นว่าเรา account for จุดพลาดที่พวกเขาจะถามถึงแล้ว เช่น รวม prototype + spec + implementation notes เป็นเอกสารเดียวไว้วางใน Slack

### Quizzes

หลัง session ยาว Claude อาจทำไปเยอะกว่าที่เรารู้ตัว อ่าน diff อย่างเดียวเข้าใจได้ตื้น เพราะ behavior จริงขึ้นกับ code path เดิมด้วย Thariq เลยสั่งให้ Claude ทำ HTML report อธิบาย context + intuition + สิ่งที่ทำ แล้วปิดท้ายด้วย **quiz** ที่เขาต้องตอบให้ผ่าน

> "I only merge after I pass the quiz perfectly."
> — เขาจะ merge ก็ต่อเมื่อทำ quiz ผ่านเต็มเท่านั้น

**ได้อะไร:** เป็นเกราะกัน [[comprehension-debt|comprehension debt]] และ [[cognitive-surrender|cognitive surrender]] แบบวัดผลได้ — ถ้าตอบ quiz ไม่ผ่าน แปลว่ายังไม่เข้าใจของที่กำลังจะ merge

## เคสจริง: ตัดต่อ launch video ของ Fable

วิดีโอเปิดตัว Fable ตัดต่อด้วย [[claude-code|Claude Code]] ทั้งหมด ทั้งที่ video editing เป็น domain ใหม่ของ Thariq ลำดับที่เขาใช้คือตัวอย่างของทุก pattern รวมกัน:

1. เริ่มจาก known knowns: รู้ว่า Claude ใช้ code ตัดวิดีโอ/ถอดเสียงได้ แต่ไม่แน่ใจเรื่องความแม่น → ให้ Claude **อธิบาย** ว่า transcription แบบ Whisper ทำงานยังไง และตัด "อืม" กับ pause ยาว ๆ ด้วย ffmpeg ได้แม่นแค่ไหน
2. อยากได้ UI ที่ sync กับคำพูด แต่ไม่แน่ใจว่าทำได้ → ให้ Claude สร้าง **prototype** ด้วย Remotion + transcript ก่อน
3. ภาพดู muted ซึ่งรู้ว่าเกี่ยวกับ color grading แต่ไม่รู้ว่า color grading คืออะไร → ลองให้ทำหลาย variation ให้เลือกก่อน แล้วพบว่าตัวเองไม่รู้ว่า "ดี" หน้าตาเป็นยังไง (unknown unknown) → เปลี่ยนเป็นให้ Claude **สอน** เรื่อง color grading เพื่อหา unknowns ก่อน

## Matching the Map and Territory

ยิ่ง model เก่งขึ้น approach ที่ถูกยิ่งพาไปได้ไกล ถ้างาน long-horizon กลับมาผิด สาเหตุน่าจะเป็นว่าเรายังนิยาม unknowns ไม่พอ หรือ plan ไม่เผื่อที่ให้ Claude improvise ผ่าน unknowns ได้

> "Every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out what you didn't know before it gets expensive to fix."
> — explainer, brainstorm, interview, prototype, reference ทุกอันคือวิธี "จ่ายถูก" เพื่อรู้ว่าเราไม่รู้อะไร ก่อนที่มันจะแพงตอนต้องตามแก้

## ความสัมพันธ์กับหน้าอื่นใน wiki

- มุมนี้กลับด้านกับ [[eternal-sloptember]] และ [[plan-mode-as-prompting]]: ฝั่งวิจารณ์บอกว่า agent ไม่เข้าใจงานจริง ฝั่ง Thariq บอกว่า gap ที่เหลือส่วนใหญ่คือ unknowns ของ *ผู้ใช้* ที่ยังไม่ถูกเคลียร์ — เก็บไว้เป็น tension สองด้าน ไม่ได้ตัดสินว่าใครถูก
- [[intent-gap]] คือปัญหาเดียวกันมองจากฝั่ง verification (โค้ด plausible แต่ไม่ correct) ส่วน unknowns คือมุมมองฝั่ง prompting ว่าช่องว่างนั้นมาจากไหน
- เสริม [[grill-me]], [[throwaway-prototyping]], [[html-artifacts]] ด้วยหลักฐานอิสระจากคนในทีม Claude Code
- quiz pattern เป็นคำตอบเชิงปฏิบัติต่อ [[comprehension-debt]] และ [[orchestration-tax|orchestration tax]] ฝั่ง review

## Caveats

- เป็น workflow ส่วนตัวของ engineer หนึ่งคนใน Anthropic ไม่ใช่ official docs — claim เรื่อง "Fable เป็น model ตัวแรกที่ bottleneck อยู่ที่ผู้ใช้" เป็นความเห็นส่วนตัว เก็บแบบ source-attributed
- บทความยืนยันว่า **Claude Fable 5** เป็น model ในตระกูล Claude และมี launch video จาก ClaudeDevs — ช่วยเคลียร์คำถามเปิดในหน้า [[fable]] (ที่ก่อนหน้านี้ไม่แน่ใจว่า Fable เป็น model หรือ harness) แต่รายละเอียด spec/pricing/tier ของ Fable 5 ยังไม่อยู่ใน wiki
- "Claude Design" ถูกพูดถึงผ่าน ๆ ในบทความ ยังไม่มีรายละเอียดพอจะสร้างหน้า

## See also

- [[map-vs-territory]]
- [[unknowns-matrix]]
- [[thariq-shihipar]]
- [[fable]]
- [[boris-cherny]]
- [[html-artifacts]]
- [[grill-me]]
- [[throwaway-prototyping]]
- [[intent-gap]]
- [[thariq-html-effectiveness]]
- [[claude-code-session-management]]
