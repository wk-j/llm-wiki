---
title: Introducing GeneBench-Pro
type: source
tags: [ai, benchmarks, biology, science, openai, agents]
created: 2026-07-01
updated: 2026-07-01
url: https://openai.com/index/introducing-genebench-pro/
date_ingested: 2026-07-01
sources: [https://openai.com/index/introducing-genebench-pro/]
---

# Introducing GeneBench-Pro / เปิดตัว GeneBench-Pro

บทความ Research/Publication ของ [[openai|OpenAI]] เผยแพร่วันที่ 30 มิถุนายน 2026 เปิดตัว [[genebench-pro|GeneBench-Pro]] benchmark สำหรับวัดว่า AI agent รับมือกับงาน computational biology ที่ต้องใช้ judgement หนัก ๆ ได้แค่ไหน

โจทย์ตั้งต้นของบทความคือ data ทางวิทยาศาสตร์ไม่ได้บอกวิธีใช้มาให้ นักวิจัยต้องตัดสินเองว่า pattern เป็น biology หรือ noise, data ตอบคำถามได้จริงไหม, และผลที่เจอควรเปลี่ยนแผนวิจัยยังไง ตรงนี้คือส่วนที่ benchmark แบบถามความรู้หรือทำ workflow สำเร็จรูปวัดไม่ค่อยได้

## แก่นของบทความ

GeneBench-Pro ขยายจาก GeneBench เดิมไปสู่โจทย์ที่ยากและเหมือนงานวิจัยจริงกว่าเดิม ครอบคลุม genomics, quantitative biology, และ translational medicine

OpenAI ใช้คำว่า [[research-taste|research taste]] เพื่อเรียกชุด judgement ที่นักวิจัยใช้ระหว่างวิเคราะห์ เช่น:

- data ชุดนี้รองรับคำถามอะไรได้บ้าง
- diagnostics แรก ๆ ควรทำให้เปลี่ยน model หรือ estimand ไหม
- เมื่อไรควรยอมรับว่าแผนแรกผิด แล้ววนกลับไปแก้แนวทาง
- เมื่อไรผลลัพธ์พร้อมใช้ตัดสิน downstream decision

ได้อะไร: benchmark นี้พยายามวัด "รสนิยมการวิจัย" ในความหมายเชิงปฏิบัติ ไม่ใช่รสนิยมสวยงาม แต่คือความสามารถในการเลือกทางวิเคราะห์ที่ data รองรับจริง

## โครงสร้างชุดโจทย์

GeneBench-Pro มี **129 คำถาม** ใน **10 domains** และ **21 sub-domains** ของ computational biology ตัวอย่าง domain ได้แก่ statistical genetics, population genetics, regulatory omics, proteomics, clinical genetics, cancer genomics, microbial genomics, และ forensic genetics

แต่ละโจทย์ให้ agent เข้า workspace แยก มี prompt สั้น ๆ, data files, และ bioinformatics stack มาตรฐาน เช่น Python, scientific computing libraries, และ PLINK 2.0 แม้โจทย์ไม่ได้บังคับให้ใช้ tool เฉพาะทางเสมอไป

รูปแบบโจทย์สำคัญคือให้ data ที่ messy พร้อม experimental context สั้น ๆ และ target estimand ที่ผูกกับ downstream decision เช่นตัวอย่าง tumor therapy benefit-risk decision ที่ต้องประเมิน benefit, toxicity risk, net clinical utility, แล้วตอบเป็น JSON ตาม schema ที่กำหนด

ผลคือ: agent ต้องทำ exploratory data analysis, เลือก causal/statistical method, ตรวจ data quality, ปรับแผน และปิดท้ายด้วยคำตอบเชิงปริมาณ ไม่ใช่แค่จำ textbook biology

## ทำไมสร้างแบบ synthetic

OpenAI บอกว่า benchmark ชีววิทยาแบบ long-horizon มักพังได้สองทาง:

- ถ้าใช้ historical dataset ที่ messy จริงเกินไป อาจไม่มี path เดียวที่ถูกชัด ๆ agent สองตัวอาจเลือก cutoff คนละแบบแต่ต่างก็ defensible
- ถ้าโจทย์ numerical insensitive เกินไป agent อาจวิเคราะห์ผิดหลักแต่ยังได้เลขผ่าน

GeneBench-Pro เลยสร้างโจทย์แบบ **synthetic** โดย OpenAI รู้ causal structure และ data-generating process เต็ม ทำให้ tune ความยากได้, ยอมรับความต่างเล็ก ๆ จาก choice ที่สมเหตุผลได้, และใช้ ablation ตรวจว่า analysis ที่ดู plausible แต่ผิดจริง ๆ จะ fail

อีกชั้นคือ audit trace เพื่อหา information leakage และ shortcut ที่ไม่ตั้งใจ ตรงนี้เชื่อมกับ [[benchmark-contamination|benchmark contamination]] และ [[reward-hacking|reward hacking]] โดยตรง: benchmark ที่ดีต้องทำให้คะแนนมาจากการเลือก analytic pathway ถูก ไม่ใช่จากการเจอทางลัด

## Expert review

OpenAI ส่ง **82 จาก 129 คำถาม** ให้ external domain experts รีวิว กลุ่ม reviewer มีตั้งแต่ graduate students, postdoctoral researchers, industry scientists, จนถึง professors

Reviewer ประเมินสามเรื่อง:

- โจทย์เหมือนงานจริงไหม
- target answer identifiable หรือไม่
- method และ estimator ที่คาดหวังเหมาะสมไหม

ตัวอย่าง feedback ชี้ว่าโจทย์มี technical issue และ quality-control issue ที่ต้องคิดจริง ไม่ใช่แค่เอาวิธีสำเร็จรูปไปใช้กับ clean data ส่วนอีกมุมหนึ่งบอกว่าถ้า model ทำได้ดี อาจช่วย researcher เลือก workflow และสำรวจ data ได้เร็วและ reproducible ขึ้น

ได้อะไร: expert review ทำหน้าที่เป็น reality check ว่าโจทย์ไม่ได้แค่ยากในแบบ puzzle แต่ยากในแบบที่นักวิจัยชีววิทยาเจอจริง

## การให้คะแนน

เพราะ OpenAI คุม data-generating process เอง จึงให้คะแนนได้แบบ deterministic เทียบกับ target ที่รู้ล่วงหน้า ลดปัญหา rubric-based grading ที่คะแนนแกว่งตาม verbosity หรือความชอบของ evaluator

แต่ละโจทย์มี metadata เพิ่ม เช่น intended analysis structure, data files, case study หลายหน้า, และผล expert review

OpenAI เปิดชุดตัวอย่าง **10 คำถาม** บน [[hugging-face|Hugging Face]] พร้อม web interface สำหรับ browse case studies และจะส่ง subset **50 คำถาม** ให้ [[artificial-analysis|Artificial Analysis]] ทำ third-party benchmarking ต่อ

ผลคือ: benchmark นี้ไม่ได้เปิดทั้งหมด แต่เปิดตัวอย่างพอให้ inspect ได้ และตั้งใจให้มีการวัดอิสระบางส่วนภายนอก OpenAI

## ผลลัพธ์ model

ผลที่ OpenAI รายงาน:

| Model / mode | Pass rate |
|---|---:|
| [[gpt-5-6-sol\|GPT-5.6 Sol]] max/highest reasoning | 28.7% |
| [[gpt-5-6-sol\|GPT-5.6 Sol]] Pro mode | 31.5% |
| GPT-5.6 Terra max | 23.3% |
| GPT-5.6 Luna max | 16.5% |
| [[gpt-5-5\|GPT-5.5]] xhigh | 12.0% |
| GPT-5.2 xhigh | 4.9% |
| Opus 4.8 | 16.0% |
| GLM 5.2 | 4.6% |
| DeepSeek V4 Pro | 2.4% |

OpenAI บอกว่า GPT-5.6 Sol ที่ highest reasoning แก้ได้เกือบ 6 เท่าของ GPT-5.2 และใช้ token ประมาณสองในสามของ GPT-5.2 ในระดับสูงสุด

บทความยังชี้ว่าช่องว่างระหว่าง GPT-5.6/GPT-5.5 กับ open-source models อย่าง GLM 5.2 ใหญ่กว่าที่คาดจาก coding benchmark เช่น [[deepswe|DeepSWE]] จึงตีความว่า open-source models อาจ specialize กับ coding มากกว่าความสามารถ reasoning กว้าง ๆ

## ต้นทุนมนุษย์กับ automation บางส่วน

Reviewer ประเมินว่าโจทย์ GeneBench-Pro ทั่วไปใช้ human expert ประมาณ **20-40 ชั่วโมง** ถ้าคิด $200 ต่อชั่วโมง ต้นทุนมนุษย์ต่อโจทย์อยู่ระดับหลายพันดอลลาร์ ขณะที่ inference cost อยู่แค่หลายดอลลาร์ต่อโจทย์

OpenAI ไม่ได้บอกว่า agent แทน expert ได้แล้ว เพราะดีที่สุดยังต่ำกว่าหนึ่งในสาม แต่ช่องว่างต้นทุนทำให้ partial automation มีมูลค่า เช่นช่วย triage hypothesis, เลือก workflow, หรือสำรวจ data ให้ researcher ตรวจต่อ

ได้อะไร: ความคุ้มค่าที่บทความเสนอไม่ใช่ "แทนนักวิทยาศาสตร์" แต่คือทำให้ judgement loop บางส่วนเร็วขึ้นพอจะเปลี่ยน economics ของ research ได้

## Failure pattern ที่เห็น

OpenAI ยกตัวอย่าง pharmacogenomic time-to-event response:

- GPT-5.5 ใช้ conventional Cox model กับ time-varying exposure แต่ไม่จัดการ treatment-confounder feedback
- GPT-5.6 Sol ใช้ new-user marginal structural Cox model, exclude prevalent users, ใช้ stabilized inverse-probability weights, และใส่ 90-day efficacy lag

ตรงนี้เป็นภาพที่ดีของ [[research-taste|research taste]]: model ที่อ่อนกว่าเห็น timing ของ treatment แต่ยังไม่ปิด inferential loop ส่วน model ที่แข็งกว่ารู้ว่าต้องเปลี่ยน causal method เพราะ treatment กับ biomarker feedback กัน

## Key takeaways

- GeneBench-Pro วัด scientific judgement ใน computational biology: ambiguity, QC, causal/statistical choice, iterative analysis, และ decision-readiness
- Synthetic data generation ช่วยลดทั้ง arbitrary author preference และโจทย์ที่เลข insensitive จนวิเคราะห์ผิดแล้วยังผ่าน
- Expert review ทำให้ benchmark ผูกกับความยากแบบงานวิจัยจริง ไม่ใช่ puzzle ที่แต่งขึ้นลอย ๆ
- GPT-5.6 Sol ทำได้ดีที่สุดที่ 28.7% หรือ 31.5% ใน Pro mode แต่ยังต่ำกว่าหนึ่งในสาม แปลว่ายังมีช่องว่างใหญ่ก่อน agent จะทำงานนี้แทน expert ได้
- ผลลัพธ์ชี้ว่า coding strength กับ scientific reasoning ภายใต้ uncertainty ไม่ใช่ axis เดียวกันเสมอไป

## See also

- [[genebench-pro]]
- [[research-taste]]
- [[openai]]
- [[gpt-5-6-sol]]
- [[benchmark-contamination]]
- [[behavioral-verifier]]
- [[reward-hacking]]
- [[deepswe]]
- [[long-horizon-coding]]
