---
title: Stacked Pull Requests
type: concept
tags: [git, pull-requests, code-review, workflow, ci, agents]
created: 2026-08-04
updated: 2026-08-15
sources: [about-stacked-pull-requests-github-docs.md, software-is-made-between-commits.md]
---

# Stacked Pull Requests / Pull Request แบบต่อกันเป็นชั้น

**Stacked pull requests** คือการแตก change ใหญ่เป็น PR เล็กหลายตัวที่ต่อกันเป็นสาย PR ล่างสุดวางฐาน ส่วน PR ด้านบนพึ่ง code จากชั้นข้างล่าง แต่ละตัวมี branch, diff, review และสถานะของตัวเอง

ตัวอย่างเช่น งานหนึ่งต้องเพิ่ม schema, API แล้วค่อยทำ UI แทนที่จะยัดทุกอย่างลง PR เดียว ทีมแยกเป็น `schema → API → UI` ได้ คนทำ UI เริ่มต่อจาก API ที่ยังไม่ merge เข้า `main` ส่วน reviewer อ่านทีละ concern

## กติกาแกนกลาง

ให้ dependency ไหลจากล่างขึ้นบนเสมอ ถ้า code ใน PR หนึ่งต้องใช้ของจากอีก PR ของที่ถูกพึ่งต้องอยู่ branch เดียวกันหรือชั้นต่ำกว่า

```text
trunk ← foundation ← service ← interface
```

แต่ละ PR จึงควรตอบคำถามเดียวที่ review ได้ เช่น “schema ถูกไหม” หรือ “endpoint ใช้ schema นี้ถูกไหม” ไม่ใช่แบ่งตามจำนวนไฟล์เฉย ๆ

**ได้อะไร:** คนทำงานเดินหน้าต่อได้ทั้งที่ฐานยังรอ review ขณะเดียวกัน reviewer ยังเห็น diff เล็กและมีขอบเขต

## Stack ต่างจาก PR Dependency DAG อย่างไร

Stack เป็น dependency **เส้นเดียว** ทุกชั้นมีตัวก่อนหน้าหนึ่งตัว ส่วน [[pr-dependency-dag|PR Dependency DAG]] (กราฟที่บอกว่า PR ไหนพึ่ง PR ไหน) กว้างกว่า เพราะแตกแขนงได้ เช่น backend กับ mobile อาจพึ่ง schema ตัวเดียวกันแต่ไม่พึ่งกันเอง

ดังนั้น stack หนึ่งสายคือกรณีพิเศษของ DAG ถ้างานแตกหลายแขนง อาจต้องมีหลาย stack หรือใช้ coordinator คุมกราฟรวมอีกชั้น

**ผลคือ:** stacked PR ช่วยงานต่อเนื่องตาม dependency แต่ไม่ได้แทน orchestration ของงานขนานทุกแบบ

## ทำไม diff เล็กอย่างเดียวยังไม่พอ

การแตก PR สร้างต้นทุนเพิ่มถ้าเครื่องมือไม่รู้ว่ามันต่อกัน:

- branch ชั้นบนต้องขยับตามฐานเมื่อชั้นล่างแก้
- CI และ branch protection อาจรันไม่ครบกับ PR ที่ไม่ได้ชี้ `main`
- reviewer อาจเห็น diff เล็ก แต่ไม่รู้ว่ามันอยู่ตรงไหนของ change ใหญ่
- merge ผิดลำดับแล้วทำให้ dependency ขาด

ฟีเจอร์ native ของ [[github|GitHub]] ใน [[about-stacked-pull-requests-github-docs|เอกสาร Stacked Pull Requests]] แก้จุดเหล่านี้ด้วย cascading rebase, stack map, quality gate ทุกชั้น และ merge แบบเข้าใจทั้งสาย ฟีเจอร์นี้ยังเป็น public preview ณ 4 ส.ค. 2026

**ได้อะไร:** เครื่องมือเก็บทั้งความเล็กของแต่ละ PR และ context ของชุดงาน ไม่บังคับให้ทีมเลือกอย่างใดอย่างหนึ่ง

## เหมาะเมื่อไร

Stack เหมาะกับ change ที่มีลำดับพึ่งพาชัด เช่น schema → service → UI, refactor → behavior change → test หรือ task ของ agent ที่ต่อยอดกันทีละก้อน มันช่วยมากเมื่อ PR แรกยังรอ review แต่คนหรือ agent ต้องเริ่มขั้นถัดไปแล้ว

ไม่ควรฝืนใช้เมื่อ change แยกจากกันจริง เพราะ branch อิสระ review และ merge ง่ายกว่า และไม่ควรสร้างชั้นเล็กจนแต่ละ PR ไม่มีความหมายในตัวเอง เพราะ reviewer จะเสียเวลาไล่ context มากกว่าที่ได้จาก diff เล็ก

## จุดเสี่ยงที่ยังต้องคุม

- **ฐานแกว่ง:** ถ้า interface ชั้นล่างเปลี่ยนบ่อย งานทุกชั้นด้านบนต้องตามแก้
- **review order:** reviewer ควรเริ่มจากล่างขึ้นบน ไม่อย่างนั้นอาจวิจารณ์ code ที่ตั้งอยู่บนสมมติฐานซึ่งยังไม่ผ่าน
- **CI multiplication:** quality gate ครบทุกชั้นเพิ่มความมั่นใจ แต่ก็เพิ่มจำนวน run และเวลารอ
- **rollback:** การรวมหลายชั้นพร้อมกันทำให้ต้องรู้ว่า revert ทั้งชุดหรือเฉพาะ commit ไหนจึงจะไม่ตัด dependency กลางสาย
- **human throughput:** agent สร้าง PR ได้เร็วขึ้น แต่คนยังต้องเข้าใจและยอมรับทีละชั้น จึงยังติด [[orchestration-tax|คอขวดการ review]] ได้

## Tension: review หลัง snapshot หรือร่วมมือก่อน commit

[[nathan-sobo|Nathan Sobo]] เสนออีกมุมใน [[software-is-made-between-commits|Software Is Made Between Commits]] เขามองว่า PR comment พยายามเอาบทสนทนากลับมาผูกกับ code หลัง commit/push ทั้งที่ decision สำคัญเกิดตอนกำลังเขียน จึงอยากให้ทีมคุยกับ agent และ annotate shared worktree ได้ก่อน commit ผ่าน [[deltadb|DeltaDB]]

มุมนี้ไม่ได้ลบเหตุผลของ stacked PR ซึ่งยังแบ่ง integration change ให้ review และรัน quality gate ทีละชั้นได้ ความเป็นไปได้หนึ่งคือ DeltaDB ดูแล continuous collaboration ก่อน commit แล้ว stacked PR ดูแล approval กับ merge หลัง change เริ่มนิ่ง แต่ source ของทั้งสองฝ่ายยังไม่อธิบาย handoff ระหว่างกัน เช่น provenance ใดต้องติดไปกับ PR และ approval ใดต้องย้อนกลับเข้า conversation history

**คำถามเปิด:** ทีมได้ review คุณภาพดีกว่าจากการเข้าร่วมตั้งแต่งานยังเคลื่อน หรือเสีย audit boundary ที่ PR ให้มา? คำตอบน่าจะขึ้นกับชนิดงาน กฎ compliance และความสามารถในการ export evidence ระหว่างสองระบบ

## เช็กลิสต์ก่อนใช้

1. แต่ละ PR มี concern เดียวและ review แยกได้หรือไม่?
2. dependency เรียงจากฐานขึ้นบนโดยไม่มีวงกลมหรือไม่?
3. CI และ approval รันกับทุกชั้นจริงหรือไม่?
4. ทีมรู้ว่าจะ merge, rebase และ rollback จากล่างขึ้นบนอย่างไรหรือไม่?
5. stack สั้นพอให้คนเห็นภาพรวมจากแผนที่เดียวหรือไม่?

## See also

- [[about-stacked-pull-requests-github-docs]]
- [[pr-dependency-dag]]
- [[github]]
- [[git-worktrees]]
- [[agentic-engineering]]
- [[orchestration-tax]]
- [[conversation-code-provenance]]
- [[software-is-made-between-commits]]
