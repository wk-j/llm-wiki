---
title: AI Work Intensification
type: concept
tags: [ai, workplace, productivity, labor, burnout, management]
created: 2026-08-13
updated: 2026-09-24
sources: [i-was-replaced-by-ai-typecraft.md, dillon-mulroy-ships-production-code-he-didnt-write.md, teepagorn-claude-code-adoption-nobody-reading.md]
---

# AI Work Intensification / AI ทำให้งานเข้มขึ้น

**AI Work Intensification** คือภาวะที่ AI ลด effort ต่อชิ้น แต่คนกลับไม่ได้ทำงานน้อยลง. องค์กรเอาความเร็วที่เพิ่มไปยกเป้า เพิ่ม WIP และขยายขอบเขตงาน จน workload รวมหนักกว่าเดิม. [[typecraft|Typecraft]] เล่ากลไกนี้จากประสบการณ์บริษัทเก่าใน [[i-was-replaced-by-ai-typecraft|I Was Replaced by AI]].

พูดง่าย ๆ คือ เมื่อก่อน developer ทำ feature หนึ่งชิ้นด้วยตัวเอง. พอ agent ช่วยให้ทำเร็วขึ้น บริษัทอาจไม่ได้คืนเวลาที่เหลือให้คน แต่คาดหวังสี่ชิ้น เปิด PR ได้ทุกบทบาท และให้ agent เดินตลอดเวลา. งานมือบางส่วนหายไป แต่งานคุม งานตรวจ งานประสาน และแรงกดดันให้ตาม output ใหม่เข้ามาแทน.

## กลไก

ลำดับที่ Typecraft เล่าคือ:

1. AI ทำให้สร้าง code และ PR ง่ายขึ้น
2. คนหลายบทบาทผลิต change ได้มากขึ้น รวมถึง project manager
3. feature volume และการแข่งขันกับทีมอื่นเพิ่ม
4. developer ต้อง review, integrate และรับผิดชอบ output มากขึ้น
5. ความคาดหวังปรับขึ้นตาม capacity ใหม่
6. เวลาทำงานและความเหนื่อยรวมไม่ลด แถมอาจเพิ่ม

จุดสำคัญคือ productivity gain ไม่ได้กำหนดเองว่าจะกลายเป็นเวลาว่างหรือ output เพิ่ม. incentive และ management เป็นคนเลือกว่ากำไรจาก automation ไปอยู่ที่ไหน.

**ได้อะไร:** วัดแค่ “ใช้เวลาต่อ task ลดลง” ไม่พอ. ต้องวัด task volume, WIP, review queue, defect, ชั่วโมงทำงาน และ recovery time พร้อมกัน.

## ต่างจาก AI Brain Fry ยังไง

[[ai-brain-fry|AI Brain Fry]] คืออาการระดับคน: สมองล้าจากการคุม ตรวจ และสลับหลาย AI tool. AI Work Intensification คือกลไกระดับการจัดงาน: เป้าหมายและ workload ขยายตามกำลังผลิตใหม่.

สองอย่างหนุนกันได้. พอบริษัทเพิ่มงาน คนก็ต้อง oversight agent มากขึ้น. พอ attention หมด อาจไหลต่อไปเป็น [[cognitive-surrender|Cognitive Surrender]] คือรับ output โดยยังไม่ได้ตั้งความเห็นเอง.

**ผลคือ:** แก้ด้วยพักอย่างเดียวอาจไม่พอ ถ้าเป้า WIP และ incentive ของทีมยังผลักงานเข้ามาไม่หยุด.

## ต่างจาก Orchestration Tax ยังไง

[[orchestration-tax|Orchestration Tax]] บอกว่าคน review และ merge แบบ serial ขณะที่ agent ผลิตขนานได้. AI Work Intensification อธิบายว่าองค์กรตอบสนองต่อกำลังผลิตนั้นอย่างไร. ถ้าฝ่ายบริหารเห็น output rate สูงขึ้นแล้วเติมงานจนเต็ม capacity ตลอด คอขวดคนจะถูกใช้งานจนล้น.

Orchestration Tax จึงเป็นข้อจำกัดของระบบ. Work intensification คือผลด้านแรงงานเมื่อ incentive ไม่เคารพข้อจำกัดนั้น.

**ได้อะไร:** เพิ่ม verifier ช่วยลด tax ได้ แต่ถ้าทุกเวลาที่ประหยัดถูกเปลี่ยนเป็นเป้าใหม่ คนอาจยังไม่ดีขึ้น.

## ไม่ใช่ผลลัพธ์เดียวของ AI

หน้า [[techsauce-ai-brain-fry|Techsauce - AI Brain Fry]] เก็บอีกด้านไว้: AI อาจลด burnout เมื่อรับ routine tasks ที่ตรวจง่าย. Typecraft เองก็จบคลิปด้วยการยอมรับ AI และตื่นเต้นกับสิ่งที่สร้างได้เร็วขึ้นในบทบาทใหม่ที่ [[planetscale|PlanetScale]].

ดังนั้น concept นี้ไม่ได้บอกว่า AI ทำให้งานหนักขึ้นเสมอ. มันบอกว่า **productivity gain ต้องถูกจัดสรร**. ถ้างาน routine หายและเป้าไม่พุ่งตาม คนได้ capacity คืน. ถ้าความเร็วกลายเป็น baseline ใหม่ทันที งานจะเข้มขึ้น.

**ผลคือ:** ปัญหาอยู่ร่วมกันระหว่างเครื่องมือ, job design, incentive, staffing และสิทธิ์ของคนในการกำหนดวิธีทำงาน.

## ความเป็นเจ้าของก็เป็นต้นทุน

Typecraft เพิ่มมิติที่ตัวเลข throughput มองไม่เห็น. เขารู้สึกว่า programming เคยเป็นงานสร้างสรรค์ที่มีลายมือของตัวเอง แต่ workflow แบบ prompt แล้วรับโค้ดทำให้ creative ownership หายไป.

ตรงนี้เพิ่ม caveat ให้ [[code-is-free|Code is Free]]. ต่อให้ implementation ถูกลง ต้นทุนด้าน comprehension, responsibility และความหมายจากการสร้างงานยังอยู่. ถ้า intensification บังคับให้คนรับ output เร็วจนไม่มีเวลาตั้งความเห็นเอง มันอาจทำให้ทั้งคุณภาพและแรงจูงใจลดลง.

**ได้อะไร:** employee experience และ retention ต้องนับ agency/ownership ด้วย ไม่ใช่ดูแค่ output กับ defect.

## งานเข้มขึ้นได้แม้องค์กรยังไม่ยกเป้า

[[dillon-mulroy|Dillon Mulroy]] เพิ่มกลไกอีกแบบใน [[dillon-mulroy-ships-production-code-he-didnt-write|บทสัมภาษณ์กับ Jan-Niklas Wortmann]] เดิม developer สลับ macro design problem กับ implementation ย่อย ๆ ช่วง implementation มีโจทย์เล็กและความรู้สึกสำเร็จเป็นระยะ จึงช่วยพักจากการตัดสินใจระดับระบบ

พอ agent รับ implementation ไป งานที่เหลือกับคนคือ architecture, abstraction, data flow และ accountability Dillon บอกว่าตัวเอง ship มากขึ้น แต่ต้องย้ายจากปัญหาใหญ่หนึ่งไปอีกปัญหาใหญ่หนึ่งจนเหนื่อยกว่าเดิม และแทบไม่เข้า flow state

กลไกนี้ต่างจากเคส Typecraft ตรงที่ source ไม่ได้บอกว่า management เพิ่ม quota แล้วทำให้ Dillon ล้า ความเข้มเกิดจากส่วนผสมของงานเปลี่ยนเอง งานใช้ judgement เข้มข้นกินสัดส่วนของวันมากขึ้นแม้จำนวนชั่วโมงเท่าเดิม

สองกลไกเกิดพร้อมกันได้:

1. องค์กรเอาความเร็วไปเพิ่ม WIP และเป้าผลงาน
2. automation ตัดงานเบาหรือ rewarding ออก เหลือแต่งาน judgement หนัก

**ได้อะไร:** นอกจากวัดจำนวน task และชั่วโมงทำงาน ต้องดูว่าวันหนึ่งมีช่วงพักทางความคิดและ task mix แบบไหนด้วย

## เคส voxium: 12-13 ชั่วโมงเพื่อกด Enter

โพสต์ [[teepagorn-claude-code-adoption-nobody-reading|ของ @teepagorn]] เล่าต่อจาก [[simon-willison|Simon Willison]] ถึง developer ชื่อ voxium ที่เพิ่งเข้าบริษัทใหญ่ได้ครึ่งเดือน ทีมทำทุกอย่างผ่าน [[claude-code|Claude Code]] ตั้งแต่ spec, code, test ถึง report ทุกระดับ L1 ถึง L7 ทำเหมือนกัน แต่คนถูกกดให้ ship ให้มากที่สุด ทำงานวันละ 12-13 ชั่วโมง "just to press enter" ผู้บริหารยังถามว่าทำไมช้า

เคสนี้ตรงกับกลไกของ Typecraft แทบทุกขั้น เร็วขึ้นก็รับเพิ่ม เร็วขึ้นอีกก็ยกเป้าอีก จุดที่เพิ่มมาคือผลข้างเคียงด้านความเข้าใจ voxium สรุปว่า "Nobody is reading anything." เวลาที่ได้คืนไม่ได้กลับไปที่การอ่านหรือการคิด ดู [[comprehension-debt]]

ผู้เขียนโพสต์เองใช้ Claude Code เยอะและชอบมาก งานส่วนตัวเร็วขึ้นจริง จึงเป็นอีกตัวอย่างว่าเครื่องมือเดียวกันให้ผลต่างกันตามว่าใครกำหนดเป้า

**ได้อะไร:** intensification ไม่ได้กินแค่ชั่วโมงทำงาน มันกินเวลาที่ทีมเคยใช้อ่านและทำความเข้าใจงานด้วย

## วิธีสังเกต

- AI usage เพิ่มแล้วชั่วโมงทำงานไม่ลด
- PR หรือ feature เพิ่มเร็วกว่ากำลัง review
- บทบาทที่ไม่เคยแก้ code เริ่มสร้าง change แต่ ownership หลัง merge ยังอยู่ที่ developer กลุ่มเดิม
- เป้าผลงานปรับขึ้นทุกครั้งที่ tooling เร็วขึ้น
- คนใช้เวลาส่วนใหญ่คุม agent มากกว่าคิดปัญหา
- คนยัง ship ได้ แต่รู้สึกว่าไม่ได้สร้างหรือเข้าใจสิ่งที่ ship

สัญญาณเหล่านี้ยังไม่พิสูจน์ causality. ควรเทียบก่อนและหลัง พร้อมดู staffing, deadline, product pressure และเหตุอื่นที่เกิดพร้อมกัน.

## คำถามเปิด

- productivity gain จาก AI ถูกแบ่งระหว่างเวลาพัก คุณภาพ กำไร และ output ใหม่อย่างไร.
- มี threshold ของ WIP หรือ review load ที่ทำนาย burnout ได้หรือไม่.
- creative ownership วัดอย่างไรโดยไม่ทำให้กลายเป็น survey ตัวเลขผิว ๆ.
- ทีมแบบใดใช้ AI ลด routine work ได้จริงโดยไม่ยกเป้าตามทันที.
- เรื่องเล่าของ Typecraft สอดคล้องกับข้อมูลข้ามองค์กรแค่ไหน. Source นี้เป็น field report จากคนเดียว.
- ถ้า workload ไม่เพิ่ม แต่วันทำงานเหลือแต่ macro judgement ต่อเนื่อง จะออกแบบจังหวะพักหรือเก็บ implementation บางส่วนไว้ได้อย่างไร

## See also

- [[i-was-replaced-by-ai-typecraft]]
- [[ai-brain-fry]]
- [[developer-balance]]
- [[orchestration-tax]]
- [[cognitive-surrender]]
- [[code-is-free]]
- [[acceptance-bottleneck]]
- [[enterprise-ai-roi]]
- [[skill-atrophy]]
- [[creative-ownership]]
- [[dillon-mulroy-ships-production-code-he-didnt-write]]
- [[dillon-mulroy]]
- [[teepagorn-claude-code-adoption-nobody-reading]]
