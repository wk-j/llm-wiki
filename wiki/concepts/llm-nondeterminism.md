---
title: LLM Non-determinism
type: concept
tags: [ai, llm, inference, non-determinism, reliability]
created: 2026-06-11
updated: 2026-06-11
sources: ["Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete..md"]
---

# LLM Non-determinism / ทำไม LLM ให้ผลไม่ซ้ำเดิม แม้ตั้ง temperature 0

หน้านี้เก็บข้อเท็จจริงเชิงกลไกที่หลายหน้าใน wiki พิงอยู่: **LLM ไม่ deterministic แม้ตั้ง temperature 0.0** — prompt เดิมเป๊ะ ๆ ก็ให้ output ต่างกันได้ในแต่ละรอบ และนี่ไม่ใช่ bug ที่รอแก้ แต่เป็นธรรมชาติของวิธีรัน inference ในปัจจุบัน

## สาเหตุเชิงระบบ

ความไม่แน่นอนมาจากชั้น infrastructure ไม่ใช่ชั้น prompt:

- **Floating-point non-associativity** — การบวกเลขทศนิยมให้ผลต่างกันตามลำดับการบวก พอ GPU จัดลำดับ operation ไม่เหมือนเดิมในแต่ละรอบ ผลรวมก็เพี้ยนเล็ก ๆ จนพลิก token ที่ถูกเลือกได้
- **Batch scheduling** — request ของเราถูกจัด batch รวมกับ request อื่นบน server ขนาด batch ที่ต่างกันเปลี่ยนผลคำนวณ
- **Fused-attention kernels** — kernel ที่ optimize มาเพื่อความเร็ว แลกมากับลำดับคำนวณที่ไม่ตายตัว

ทั้งหมดนี้ "แก้ด้วย prose ที่เขียนดีขึ้นไม่ได้" — ต่อให้ spec ชัดแค่ไหน ตัวกลไกการสุ่มก็ยังอยู่

## ตัวเลขที่บทความของ Wasowski รวบรวมไว้

(จาก [[stop-writing-specs-start-writing-facts]] — แต่ละตัวมีเงื่อนไขเฉพาะ อย่าอ่านเป็นกฎสากล)

- งานวิจัยอิสระพบ **80 unique completions จาก 1,000 prompts ที่เหมือนกัน** ใน deterministic mode; variance ระดับไม่กี่จุดถึงสิบกว่าจุดของ accuracy เป็นเรื่องปกติ
- งาน IBM บน RAG workflow สายการเงิน: **model 100B+ ให้ output ซ้ำเดิมแค่ 12.5% ของรอบรัน ขณะที่ model 7–8B ให้ผลตรงกันหมด** — ทิศทางสวนกับความหวัง "รอ model ใหญ่ขึ้นแล้วจะนิ่งเอง" (เป็นผลจาก task เฉพาะ ไม่ใช่กฎทุก workflow)
- Sclar et al. (2023): เปลี่ยน format ของ prompt แบบสุดขั้วบน model รุ่นอ่อน ทำ accuracy แกว่งได้ถึง **76 จุด** — model ใหม่ ๆ ไวต่อ format น้อยลง แต่การขยับโครงสร้าง markdown ก็ยังเปลี่ยนโค้ดที่ generate ได้
- ข้าม vendor: model ของแต่ละเจ้าละเมิด constitution ของเจ้าอื่นบ่อยกว่าของตัวเองหลายเท่า — prompt/spec ที่จูนกับเจ้าหนึ่งเป็น **vendor-shaped** ไม่ใช่ universal

## ผลที่ตามมา

- **Prose instruction ทุกชิ้นคือการสุ่มตัวอย่าง** — model อ่าน spec ครั้งหนึ่งก็ draw จากการแจกแจงของการตีความครั้งหนึ่ง นี่คือฐานของ critique ต่อ [[spec-driven-development]] และเหตุผลที่ [[facts-first]] เลือกฝากความจริงไว้กับ exit code แทน
- **การย้ายรุ่น model = เปลี่ยน interpreter** ไม่ใช่อัปเดตซอฟต์แวร์ — spec เดิมบน model ใหม่คือโปรแกรมเดิมบนตัวแปลภาษาคนละตัว
- ในกรอบ [[harness-guides-sensors]] นี่คือเหตุผลที่ guide/sensor แบบ **inferential** (ให้ model ตัดสิน) เชื่อได้ไม่เต็มร้อยและไม่ควรเป็นด่านเดียว ขณะที่ **computational** (CPU, deterministic) รันกี่รอบก็ได้ผลเดิม
- [[birgitta-bockeler|Böckeler]] เตือนเรื่อง spec-as-source ไว้ว่าอาจได้ "the flaws of both MDD and LLMs: inflexibility and non-determinism"

## See also

- [[stop-writing-specs-start-writing-facts]]
- [[spec-driven-development]]
- [[facts-first]]
- [[intent-gap]]
- [[harness-guides-sensors]]
- [[verifiability]]
