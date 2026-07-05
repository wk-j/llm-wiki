---
title: Judgement-Based Prompting
type: concept
tags: [ai, prompting, claude, claude-code, agents, cost-optimization, models]
created: 2026-07-05
updated: 2026-07-05
sources: [fables-judgement-simon-willison.md]
---

# Judgement-Based Prompting / สั่งด้วยดุลพินิจ ไม่ใช่กฎตายตัว

เวลาจะสั่ง coding agent ว่าให้ทำงานยังไง เรามีสองทางเลือก. ทางแรกคือเขียน **กฎตายตัว** ("ทำ X เมื่อ Y, อย่าทำ Z เมื่อ W"). ทางที่สองคือบอกให้ agent **ใช้ดุลพินิจของมันเอง** ในการตัดสินใจนั้น. Judgement-based prompting คือการเลือกทางที่สอง — เชื่อว่า model ที่แรงพอจะชั่งบริบทตรงหน้าได้ดีกว่ากฎ static ที่เดาทุกกรณีไม่ทัน.

ไอเดียนี้มาจากโพสต์ [[fables-judgement-simon-willison|Fable's judgement]] ของ [[simon-willison|Simon Willison]] (2026-07-03) ที่รวมเคล็ดจากทีม [[claude-code|Claude Code]] และ [[jesse-vincent|Jesse Vincent]].

## ตัวอย่างที่หนึ่ง: เมื่อไหร่ควรเขียน test

เคล็ดนี้ [[cat-wu|Cat Wu]] และ [[thariq-shihipar|Thariq Shihipar]] เล่าใน Fireside Chat ที่ [[ai-engineer-worlds-fair|AI Engineer World's Fair]]. คุณจะสั่งแบบมีกฎก็ได้ เช่น "เขียน test เฉพาะฟีเจอร์ใหญ่ อย่าไปแตะ test กับการแก้ copy/design เล็ก ๆ". แต่ทีมบอกว่า ดีกว่าคือแค่สั่งว่า **"ใช้ดุลพินิจเองว่าเมื่อไหร่ควรเขียน test"**.

เหตุผล: กฎแบบนี้มีเคสขอบเยอะเสมอ. "ฟีเจอร์ใหญ่" ใหญ่แค่ไหน? การแก้ copy ที่ดันไปโดน logic ล่ะ? พอเขียนกฎครอบทุกกรณี กฎก็ยาวและเปราะ. ปล่อยให้ [[fable|Fable]] อ่านบริบทของ diff ตรงหน้าแล้วตัดสินเอง มักได้ผลตรงกว่า.

**ได้อะไร:** ไม่ต้องนั่งไล่เขียนกฎครอบทุก edge case; ให้ model ที่เห็นบริบทเป็นคนชั่ง.

## ตัวอย่างที่สอง: งานนี้ควรใช้ model แรงแค่ไหน

Jesse Vincent ต่อยอดไอเดียเดียวกันในเชิงต้นทุน: **บอก Fable ให้ไปใช้ model ตัวอื่นทำงานเล็ก ๆ โดยให้ Fable เลือก model เองว่าจะใช้ตัวไหน**. Simon เอาไปสั่ง Claude Code ตรง ๆ ว่า "งาน coding ทุกอย่าง ให้ใช้ดุลพินิจเลือก model ที่ power ต่ำลงตามเหมาะ แล้วรันใน [[subagent-patterns|subagent]]". ผลคือทำงานได้เยอะขึ้นและโควตา Fable ลดช้าลง.

จุดที่ต่างจาก [[model-choice-by-expertise]] และ [[advisor-strategy]]: สองอันนั้น **คน** เป็นคนเลือก model ให้พอดีกับงาน. ที่นี่ย้ายการเลือกไปเป็น **ตัว model** ตัดสินเอง — คนแค่ตั้งนโยบายว่า "เลือกให้ประหยัดหน่อย".

**ได้อะไร:** ประหยัด token ของ model แพงโดยไม่ต้องแยกงานเองทีละชิ้น.

## เส้นแบ่งกับ judgement-vs-automation

อย่าสับสนกับ [[judgement-vs-automation]]. หน้านั้นถามว่า *งานประเภทไหน* จะถูก automate (งานคาดเดาได้ → automate; งานต้องใช้วิจารณญาณ → เหลือให้คน). ส่วนหน้านี้เป็นเรื่อง **เทคนิคการเขียน prompt**: จะมอบการตัดสินใจย่อย ๆ ระหว่างทำงานให้ดุลพินิจของ model หรือจะล็อกด้วยกฎ. คนละแกน แต่คำว่า "ดุลพินิจ" เชื่อมกัน.

## ขอบเขตและข้อควรระวัง

- **ใช้ได้เมื่อดุลพินิจของ model ในเรื่องนั้นดีพอ.** ถ้าเป็นเรื่องที่ model ยังตัดสินพลาดบ่อย (เช่น data safety, security, architecture) กฎที่ชัดหรือคนตัดสินยังจำเป็น. เทียบ [[zoran-horvat-claude-no-planning-engine|ข้อวิจารณ์ของ Zoran Horvat]] ที่ว่า model วางแผนดูดีแต่ยังพลาดคำถามระดับ senior.
- **ต้องรีวิวผล.** ยกดุลพินิจให้ model โดยไม่ดูผลเลย = เสี่ยง [[cognitive-surrender]] และเพิ่ม [[orchestration-tax]]. Simon เองก็ให้ main loop รีวิวงานของ subagent ก่อน commit.
- **สวนทางกับ CLAUDE.md แบบกฎแน่น.** template อย่าง [[cyril-xbt-claude-md-guide|CLAUDE.md ของ @cyrilXBT]] เน้น section "Never Do This" ที่เป็นกฎตายตัว. Judgement-based prompting ไม่ได้บอกให้ทิ้งกฎทั้งหมด — แต่ให้แยกว่าเรื่องไหนควรล็อกด้วยกฎ (เรื่องที่ผิดไม่ได้) กับเรื่องไหนปล่อยดุลพินิจได้ (เรื่องที่ยืดหยุ่นและกฎครอบไม่ไหว).

## See also

- [[fables-judgement-simon-willison]]
- [[judgement-vs-automation]]
- [[advisor-strategy]]
- [[model-choice-by-expertise]]
- [[delegation-mindset]]
- [[subagent-patterns]]
- [[cognitive-surrender]]
- [[orchestration-tax]]
