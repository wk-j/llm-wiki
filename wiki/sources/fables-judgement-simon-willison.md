---
title: Fable's judgement — Simon Willison
type: source
tags: [ai, claude-code, agents, prompting, cost-optimization, subagents, models]
created: 2026-07-05
updated: 2026-07-05
sources: [fables-judgement-simon-willison.md]
url: https://simonwillison.net/2026/Jul/3/judgement/
---

# Fable's judgement — Simon Willison

โพสต์สั้นของ [[simon-willison|Simon Willison]] (2026-07-03) รวมเคล็ดสามชั้นที่มีธีมเดียวกัน: **ปล่อยให้ model ใช้ดุลพินิจของตัวเอง แทนที่จะสั่งกฎตายตัวว่าให้ทำงานยังไง**. ธีมนี้ใช้กับ [[fable|Fable]] เป็นหลัก และใช้กับ Opus ได้บางส่วน. Simon เจอไอเดียนี้ตอนเป็นพิธีกร Fireside Chat แล้วต่อยอดด้วยเคล็ดของ [[jesse-vincent|Jesse Vincent]] จนกลายเป็นวิธีประหยัด token ที่เขาลงมือทำจริง.

## เคล็ดจาก Fireside Chat: ให้ model ตัดสินใจเรื่องวิธีทำงานเอง

Simon เป็นพิธีกร Fireside Chat กับ [[cat-wu|Cat Wu]] และ [[thariq-shihipar|Thariq Shihipar]] จากทีม [[claude-code|Claude Code]] ที่งาน [[ai-engineer-worlds-fair|AI Engineer World's Fair]] (วันพุธ). เคล็ดที่เขาบอกว่าน่าสนใจที่สุดคือ ให้ Fable (และ Opus ในระดับหนึ่ง) **ใช้ดุลพินิจของมันเอง** แทนที่จะไปกำหนดขั้นตอนการทำงานให้มันละเอียด.

ตัวอย่างที่ทีมยกคือเรื่อง **testing**. คุณเขียนกฎแบบนี้ก็ได้:

> "only use automated testing for larger features, don't update and run tests for small copy or design changes"
> (ให้เขียน automated test เฉพาะฟีเจอร์ใหญ่ ๆ อย่าไปแก้หรือรัน test กับการเปลี่ยน copy หรือ design เล็กน้อย)

แต่ทีมบอกว่า ดีกว่านั้นคือแค่บอก Fable ว่า **"ให้ใช้ดุลพินิจเองว่าเมื่อไหร่ควรเขียน test"**. เพราะกฎตายตัวเดาทุกกรณีไม่ได้ ส่วน model ที่แรงพอจะชั่งบริบทตรงหน้าได้เองว่างานนี้ควรมี test ไหม. ดูแนวคิดนี้แบบเต็มที่ [[judgement-based-prompting]].

## เคล็ดของ Jesse Vincent: ให้ Fable เลือก model ที่ถูกลงเอง

[[jesse-vincent|Jesse Vincent]] ต่อยอดไอเดียเดียวกันในเชิงประหยัดต้นทุน. บริบทคือ Fable กำลังจะขึ้นราคาในอีกไม่กี่วัน Simon เลยอยากใช้ token ที่มีอยู่ให้คุ้มก่อนหมดโควตา. เคล็ดของ Jesse คือ **บอก Fable ให้ไปใช้ model ตัวอื่นทำงานเล็ก ๆ โดยให้ Fable ใช้ดุลพินิจเองว่าจะเลือก model ไหน**.

จุดสำคัญคือ ดุลพินิจเรื่อง "งานนี้ต้องใช้ model แรงแค่ไหน" ก็ถูกยกให้ model ตัดสินเองเหมือนกัน ไม่ใช่ให้คนมานั่งแยกงานทีละชิ้น. นี่คือรุ่นที่คนสั่งด้วย prompt ของ [[advisor-strategy|advisor strategy]] และเชื่อมกับ [[model-choice-by-expertise]] แต่ย้ายคนตัดสินใจจากมนุษย์ไปเป็นตัว model เอง.

## Simon ลงมือ: prompt เดียว + memory file

Simon สั่ง Claude Code ไปตรง ๆ ว่า:

> "For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent"
> (งาน coding ทุกอย่าง ให้ใช้ดุลพินิจเลือก model ที่ power ต่ำลงตามความเหมาะสม แล้วรันใน subagent)

Claude เซฟสิ่งนี้เป็น **memory file** แบบ `feedback` ไว้ที่ `~/.claude/projects/name-of-project/memory/delegate-coding-to-subagents.md` โดยมีโครงเดียวกับที่ wiki นี้ใช้เก็บ memory (frontmatter + Why + How to apply):

- **Why:** เรื่อง cost/efficiency — งาน implementation ส่วนใหญ่ไม่ต้องใช้ model ระดับบนสุด; ส่วนที่เป็น judgment, review, และ synthesis ให้อยู่ที่ main loop.
- **How to apply:** พองานเป็นการเขียน/แก้ code เป็นหลัก ให้ spawn subagent พร้อม model override — `sonnet` สำหรับงาน implementation จริงจัง, `haiku` สำหรับงานจิ๊บ ๆ เชิงกลไก — แล้วเขียน prompt ให้ครบในตัว; เสร็จแล้วค่อยรีวิวผลใน main loop ก่อน commit. งาน design, audit, data synthesis และอะไรก็ตามที่ต้องใช้ judgment เยอะ ให้อยู่กับ model หลัก.

โครงนี้สอดกับ [[delegation-mindset|delegation mindset]] และ [[subagent-patterns]]: main loop ถือ judgment/review ไว้ ส่วน worker ที่ถูกลงลงมือเขียน code.

## ผลลัพธ์ (ตามที่ Simon เล่า)

Simon บอกว่าจนถึงตอนนี้ได้ผลดี:

> "I'm getting a *ton* of work done and my Fable allowance is shrinking less quickly than before."
> (ทำงานได้เยอะขึ้นมาก และโควตา Fable ก็ลดช้าลงกว่าเดิม)

เป็นหลักฐานเชิงประสบการณ์จากคนเดียว ไม่ใช่ตัวเลข benchmark — เก็บไว้เป็น field report.

## เชื่อมกับ wiki

- [[judgement-based-prompting]] — แก่นของ source: สั่งด้วยดุลพินิจ ไม่ใช่กฎตายตัว
- [[advisor-strategy]] / [[model-choice-by-expertise]] — การเลือก model ให้พอดีกับงาน; source นี้ย้ายคนเลือกไปเป็น model
- [[delegation-mindset]] / [[subagent-patterns]] — main loop ถือ judgment, subagent ที่ถูกลงลงมือ
- [[value-maxing]] / [[ai-token-economics]] — รีดคุณค่าต่อ token; ที่นี่คือฝั่งผู้ใช้ที่ยืด allowance ก่อนราคาขึ้น
- [[orchestration-tax]] / [[cognitive-surrender]] — ข้อควรระวัง: ยกดุลพินิจให้ model มากไปโดยไม่รีวิว ก็เสี่ยงเช่นกัน

## See also

- [[simon-willison]]
- [[judgement-based-prompting]]
- [[jesse-vincent]]
- [[cat-wu]]
- [[thariq-shihipar]]
- [[ai-engineer-worlds-fair]]
- [[fable]]
- [[advisor-strategy]]
- [[delegation-mindset]]
