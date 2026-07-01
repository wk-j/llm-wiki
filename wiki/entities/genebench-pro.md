---
title: GeneBench-Pro
type: entity
tags: [ai, benchmarks, biology, science, openai]
created: 2026-07-01
updated: 2026-07-01
sources: [https://openai.com/index/introducing-genebench-pro/]
---

# GeneBench-Pro

[[openai|OpenAI]] benchmark สำหรับวัด AI agent ในงาน computational biology ที่ต้องใช้ judgement หนัก ๆ เปิดตัววันที่ 30 มิถุนายน 2026 ผ่านบทความ [[introducing-genebench-pro|Introducing GeneBench-Pro]]

จุดต่างจาก benchmark ที่ถามความรู้คือ GeneBench-Pro ให้ agent เจอ data ที่ messy, context สั้น ๆ, target estimand, และ downstream decision แล้วต้องเลือกวิธีวิเคราะห์เอง วนตรวจ data เอง และสรุปคำตอบเชิงปริมาณเอง

## วัดอะไร

GeneBench-Pro วัดสิ่งที่ OpenAI เรียกว่า [[research-taste|research taste]] หรือ chain ของ judgement ในงานวิจัย:

- data รองรับคำถามนี้ไหม
- noise/artifact แยกจาก biology ยังไง
- diagnostics ควรทำให้เปลี่ยน model, estimand, หรือ inclusion criteria ไหม
- result พร้อมใช้ตัดสิน clinical/academic/business decision หรือยัง

ได้อะไร: benchmark นี้ไม่ได้วัดว่า model รู้ศัพท์ genomics แค่ไหน แต่วัดว่า model ทำตัวเหมือนนักวิเคราะห์วิทยาศาสตร์ที่ระวัง data issue ได้ไหม

## ขนาดและ domain

- 129 problems
- 10 domains
- 21 sub-domains
- ครอบคลุม statistical genetics, population genetics, quantitative genetics, regulatory omics, functional genomics, proteomics, clinical genetics/pharmacogenomics/diagnostics, cancer genomics, microbial genomics, และ forensic genetics

OpenAI เปิดตัวอย่าง 10 คำถามบน [[hugging-face|Hugging Face]] และ case-study browser ส่วน 50-question subset จะถูกส่งให้ [[artificial-analysis|Artificial Analysis]] ทำ third-party benchmarking

## วิธีสร้างโจทย์

โจทย์สร้างแบบ synthetic เพราะ OpenAI รู้ causal structure และ data-generating process เต็ม วิธีนี้แก้ปัญหาสองอย่าง:

- historical dataset จริงอาจมีหลายทางที่ defensible จนคะแนนสะท้อน preference ของคนแต่งโจทย์
- dataset ที่เลขไม่ sensitive พออาจปล่อยให้ analysis ผิดหลักแต่ยังผ่าน

GeneBench-Pro จึง tune complexity ได้, ตรวจด้วย ablation ว่า analysis ที่ผิดจะ fail, และ audit trace เพื่อหา leakage หรือ shortcut

ตรงนี้เชื่อมกับ [[benchmark-contamination]] และ [[behavioral-verifier]]: benchmark ที่ดีต้องทำให้ "ทางวิเคราะห์ถูก" เป็นเหตุผลหลักของคะแนน ไม่ใช่การจำเฉลยหรือชน verifier แบบบังเอิญ

## ผลที่รายงาน

| Model / mode | Pass rate |
|---|---:|
| [[gpt-5-6-sol\|GPT-5.6 Sol]] max/highest reasoning | 28.7% |
| [[gpt-5-6-sol\|GPT-5.6 Sol]] Pro mode | 31.5% |
| GPT-5.6 Terra max | 23.3% |
| GPT-5.6 Luna max | 16.5% |
| [[gpt-5-5\|GPT-5.5]] xhigh | 12.0% |
| Opus 4.8 | 16.0% |
| GLM 5.2 | 4.6% |
| DeepSeek V4 Pro | 2.4% |

จุดสำคัญคือ model ที่ดีที่สุดยังต่ำกว่าหนึ่งในสาม แปลว่า agent เริ่มช่วยได้ แต่ยังไม่พอแทนนักวิจัยที่ต้องรับผิดชอบ inference สุดท้าย

## ความหมายต่อ wiki

GeneBench-Pro เป็นญาติฝั่ง science ของ [[deepswe|DeepSWE]]:

- DeepSWE ทำให้ coding benchmark ใกล้งานจริงขึ้น โดยตัด contamination และตรวจพฤติกรรม
- GeneBench-Pro ทำแบบคล้ายกันกับ computational biology แต่โจทย์หนักกว่าเรื่อง uncertainty, causal inference, QC, และ decision-readiness

ผลคือ wiki ควรแยก "เก่ง coding" ออกจาก "เก่ง scientific reasoning" ให้ชัดขึ้น เพราะ OpenAI รายงานว่า open-source models บางตัวดู competitive ใน coding มากกว่าใน GeneBench-Pro

## See also

- [[introducing-genebench-pro]]
- [[research-taste]]
- [[openai]]
- [[gpt-5-6-sol]]
- [[deepswe]]
- [[benchmark-contamination]]
- [[behavioral-verifier]]
- [[reward-hacking]]
