---
title: Unknowns Matrix
type: concept
tags: [ai, agents, prompting, workflow, planning]
created: 2026-07-04
updated: 2026-07-04
sources: [a-field-guide-to-fable-finding-your-unknowns.md]
---

# Unknowns Matrix / ตาราง unknowns 4 ช่อง

frame จาก [[thariq-shihipar|Thariq Shihipar]] ใน [[field-guide-to-fable-finding-unknowns|A Field Guide to Fable]] สำหรับแตกปัญหาก่อนส่งให้ coding agent: ช่องว่างระหว่างสิ่งที่เราบอก agent กับสภาพจริงของงาน (ดู [[map-vs-territory]]) แบ่งได้ 4 ช่อง ตามแนว "known/unknown" ที่คนมักรู้จักจากคำพูดของ Donald Rumsfeld

## 4 ช่อง

| ช่อง | คืออะไร | อาการ |
|---|---|---|
| **Known Knowns** | สิ่งที่รู้และบอกไปแล้ว | เนื้อหาใน prompt ของเรา |
| **Known Unknowns** | สิ่งที่ยังคิดไม่จบ แต่รู้ตัวว่ายังไม่รู้ | "ยังไม่ได้ตัดสินใจว่า auth จะใช้ provider ไหน" |
| **Unknown Knowns** | สิ่งที่ชัดกับเราจนไม่คิดจะเขียน แต่เห็นแล้วจำได้ทันที | taste เรื่อง design — "รู้ต่อเมื่อเห็น" |
| **Unknown Unknowns** | สิ่งที่ไม่เคยนึกถึงเลย ไม่รู้แม้แต่ว่า "ของดี" หน้าตายังไง | เข้า domain/codebase ใหม่ ไม่รู้จะถามอะไร |

ยิ่งเก่ง agentic coding = ยิ่งมี unknowns น้อยและเผื่อแผนสำหรับที่เหลือ Thariq ยก [[boris-cherny|Boris Cherny]] กับ Jarred Sumner (ผู้สร้าง Bun) เป็นตัวอย่างคนที่ in-sync ทั้ง codebase และพฤติกรรม model ในคำของเขา: "reducing and planning for your unknowns is the **skill** of agentic coding" — และเป็นทักษะที่ฝึกได้โดยใช้ Claude ช่วยหานั่นเอง

## เทคนิคต่อช่อง ต่อจังหวะ

Thariq ไม่ได้ใช้ทุกเทคนิคทุกครั้ง แต่เก็บไว้เป็นชุดเครื่องมือ เกือบทุกอันใช้ [[html-artifacts|HTML artifact]] เป็นสื่อ:

**ก่อนลงมือ (pre-implementation)**

- **Blind Spot Pass** → unknown unknowns: สั่งตรง ๆ ด้วยคำว่า "blindspot pass" / "unknown unknowns" ให้ Claude สำรวจแล้วสอนเรา พร้อมบอกว่าเราเป็นใคร รู้อะไรอยู่แล้ว
- **Brainstorms / prototypes** → unknown knowns: ขอหลาย design direction ที่ต่างกันจัด ๆ ให้เรา react; หาให้เจอตอน prototype เพราะเจอตอน implementation แพงกว่ามาก (ดู [[throwaway-prototyping]])
- **Interviews** → known unknowns ที่เหลือ: "Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture." — pattern เดียวกับ [[grill-me]]
- **References** → ตอนบรรยายไม่ถูก: reference ที่ดีที่สุดคือ source code; ชี้ agent ไปที่ folder/library ที่ทำสิ่งที่ต้องการ ต่อให้คนละภาษา
- **Implementation plan** เรียงตามโอกาสแก้: เอา data model / type interface / UX flow ขึ้นก่อน mechanical refactoring ฝังท้าย

**ระหว่างลงมือ**

- **Implementation notes**: ให้ agent เก็บ `implementation-notes.md` บันทึก deviation จาก plan — เจอ edge case ให้เลือกทาง conservative, log ไว้, ทำต่อ; unknown unknowns ที่โผล่กลางทางกลายเป็นบทเรียนรอบหน้า

**หลังลงมือ**

- **Pitches / explainers**: reviewer เริ่มด้วย unknowns ชุดเดียวกับเรา — explainer ที่ดีเร่งทั้งความเข้าใจและ approval
- **Quizzes**: ให้ Claude ทำ report + quiz แล้วต้องตอบผ่านก่อน merge — เกราะกัน [[comprehension-debt]] และ [[cognitive-surrender]] แบบวัดผลได้

**ผลคือ:** ทุกเทคนิคคือการ "จ่ายถูกตอนต้น" เพื่อไม่ต้อง "จ่ายแพงตอนแก้" — "Every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out what you didn't know before it gets expensive to fix."

## ข้อควรระวัง

- สั่งละเอียดเกิน agent จะตามคำสั่งแม้ตอนควร pivot; สั่งกว้างเกิน agent จะเดาด้วย best practices ที่ไม่เข้ากับงาน — matrix ช่วยบอกว่าควรลงทุนเคลียร์ช่องไหนก่อน
- frame นี้มาจาก workflow ส่วนตัวของ engineer หนึ่งคน (แม้จะอยู่ทีม Claude Code) ยังไม่มีหลักฐานเชิงระบบว่าเทคนิคชุดนี้ให้ผลกับทุกคน/ทุกงาน

## See also

- [[field-guide-to-fable-finding-unknowns]]
- [[map-vs-territory]]
- [[grill-me]]
- [[throwaway-prototyping]]
- [[html-artifacts]]
- [[intent-gap]]
- [[comprehension-debt]]
