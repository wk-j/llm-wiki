---
title: Research Taste
type: concept
tags: [ai, science, research, benchmarks, judgment]
created: 2026-07-01
updated: 2026-07-01
sources: [https://openai.com/index/introducing-genebench-pro/]
---

# Research Taste / รสนิยมการวิจัย

**Research taste** ในบทความ [[introducing-genebench-pro|Introducing GeneBench-Pro]] ของ [[openai|OpenAI]] หมายถึง chain ของ judgement ที่ทำให้นักวิจัยเลือกทางวิเคราะห์ได้ดี ไม่ใช่แค่รู้ทฤษฎีหรือกด pipeline ถูก

คำว่า taste ตรงนี้ไม่ได้หมายถึง "ชอบแบบไหน" แบบสวยงาม แต่หมายถึง sense จากประสบการณ์ว่า data ชุดนี้ควรถามอะไร, ควรเชื่อผลไหน, และเมื่อไรต้องเปลี่ยนแผน

## หน้าตาในงานจริง

ใน computational biology data มักมาพร้อม noise, batch effect, artifact, missingness, confounding, และ measurement issue นักวิจัยที่มี research taste จะถามต่อทันที:

- pattern นี้เป็น biology หรือ artifact
- data รองรับ estimand ที่อยากตอบจริงไหม
- covariate หรือ quality-control issue ตัวไหนเปลี่ยนคำตอบได้
- analysis แรกที่วางไว้ยังใช้ได้ไหมหลังเห็น diagnostics
- result พร้อมใช้ตัดสิน downstream decision หรือยัง

ได้อะไร: research taste คือสิ่งที่ทำให้การวิเคราะห์ไม่ไหลตาม script จนได้คำตอบที่ดูดีแต่ผิดฐาน

## ต่างจากความรู้และ workflow

model อาจรู้ว่า Cox model คืออะไร หรือรู้ว่า PLINK ใช้ทำอะไร แต่นั่นยังไม่พอ ถ้าโจทย์มี treatment-confounder feedback, prevalent-user bias, หรือ delayed treatment effect การเลือก model ตามสูตรง่าย ๆ อาจผิด

ตัวอย่างใน GeneBench-Pro:

- GPT-5.5 เห็น treatment timing และใช้ Cox model แบบ time-varying exposure
- [[gpt-5-6-sol|GPT-5.6 Sol]] เปลี่ยนไปใช้ new-user marginal structural Cox model เพราะโจทย์มี feedback ระหว่าง treatment กับ confounder

ความต่างไม่ได้อยู่ที่จำชื่อ method ได้ แต่อยู่ที่รู้ว่า assumption ของ method ไหนถูกทำลายโดย data structure แบบไหน

## ทำไมวัดยาก

research taste ยากต่อ benchmark เพราะหลาย decision เป็นเรื่อง judgement:

- cutoff บางอย่างอาจมีหลายค่าที่ defensible
- historical dataset จริงอาจไม่มี ground truth เดียว
- ถ้า verifier หยาบไป analysis ที่ผิดอาจยังได้เลขใกล้พอผ่าน

[[genebench-pro|GeneBench-Pro]] แก้ด้วย synthetic data ที่รู้ causal structure และ data-generating process ทำให้แยกได้ว่า choice ไหนยืดหยุ่นได้ และ choice ไหนผิดหลักจนควร fail

## เชื่อมกับ harness และ verifier

ใน coding เราใช้ [[behavioral-verifier|behavioral verifier]] ตรวจว่า software ทำพฤติกรรมถูกไหม ใน science งานยากกว่า เพราะพฤติกรรมที่ถูกคือ "เลือก inference path ถูก" ไม่ใช่แค่ output ผ่าน test

research taste จึงต้องการ verifier ที่ดูทั้ง numerical answer และ reasoning/QC trace ในระดับหนึ่ง ไม่งั้น agent อาจได้เลขถูกจากทางที่ไม่ควรเชื่อ หรือทำ [[reward-hacking|reward hacking]] กับรูปแบบคำตอบ

## ผลคือ

ถ้า agent มี research taste สูง มันจะไม่ใช่แค่ช่วยรัน analysis เร็วขึ้น แต่มันจะช่วย researcher ตัดสินใจว่า analysis ไหนควรทำตั้งแต่แรก และผลไหนควรหยุดเพื่อเช็คใหม่ก่อนนำไปใช้

## See also

- [[genebench-pro]]
- [[introducing-genebench-pro]]
- [[behavioral-verifier]]
- [[benchmark-contamination]]
- [[reward-hacking]]
- [[verifiability]]
