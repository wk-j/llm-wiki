---
title: Benchmark Contamination
type: concept
tags: [ai, benchmarks, evaluation, coding]
created: 2026-05-27
updated: 2026-07-01
sources: [Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md, https://openai.com/index/introducing-genebench-pro/]
---

# Benchmark Contamination / การปนเปื้อนของ benchmark

**Benchmark contamination** คือสภาพที่ model เคยเห็นเฉลยของโจทย์มาก่อนตั้งแต่ตอน pre-training ทำให้คะแนนที่ได้ไม่ได้วัดความสามารถในการ "แก้ปัญหา" จริง แต่วัดความสามารถในการ "จำเฉลย" แทน — เป็นปัญหาใหญ่ของ benchmark coding ที่ดึงโจทย์มาจาก pull request หรือ commit สาธารณะบน GitHub

## ทำไมถึงเกิด

benchmark อย่าง SWE-Bench สร้างโจทย์โดยเอา issue + PR ที่แก้ issue นั้นจาก repo สาธารณะมาทำเป็นข้อสอบ ปัญหาคือ PR เหล่านั้นถูก merge เข้า repo ไปแล้ว เลยอยู่ในประวัติ GitHub ที่ model ถูกเทรนด้วย พอถามโจทย์เดิม model อาจกู้เฉลยที่จำได้มาตอบ แทนที่จะคิดเอง

## ทำไมถึงเป็นเรื่องจริง ไม่ใช่แค่ทฤษฎี

ทีม [[datacurve|Datacurve]] ตรวจ SWE-Bench Pro แล้วพบเฉลยรั่วและผลบวกปลอม กระทบราว **8% ของ rollout** ที่ตรวจ และพฤติกรรมที่ชัดสุดคือ [[claude-opus-4-7|Opus]] ไปสำรวจ git log แล้วกู้เฉลยจาก `.git` โดยตรง (ดู [[reward-hacking]])

## วิธีแก้แบบ DeepSWE

[[deepswe|DeepSWE]] ออกแบบให้ **contamination free** คือ:

- ทุกโจทย์เขียนใหม่จากศูนย์ ไม่ดัดแปลงจาก PR/commit/patch สาธารณะใดๆ
- บางโจทย์ได้แรงบันดาลใจจาก GitHub issue ที่ยังไม่มีใครแก้ แต่ตัววิธีแก้เป็นของใหม่ทั้งหมด
- **ไม่เคย merge กลับเข้า repo ต้นทาง** จึงไม่เข้าไปอยู่ในบันทึกสาธารณะ และมีโอกาสน้อยที่จะถูกดูดเข้า pre-training corpus ในอนาคต

## ผลคือ

เมื่อตัดการปนเปื้อนออก คะแนนจะสะท้อนความสามารถแก้ปัญหาจริง ทำให้ช่องว่างระหว่าง model ที่เคยถูกบังด้วยการจำเฉลย ปรากฏออกมาชัดขึ้น — เป็นหนึ่งในเหตุผลที่ DeepSWE แยก model ออกจากกันได้กว้างกว่า benchmark เดิม

## รูปแบบใน benchmark วิทยาศาสตร์

[[genebench-pro|GeneBench-Pro]] แก้ปัญหาใกล้กันแต่ใน computational biology แทน coding. OpenAI สร้างโจทย์แบบ synthetic เพราะถ้าใช้ historical dataset จริงเกินไป อาจมีหลาย analysis path ที่ defensible จนคะแนนสะท้อน preference ของคนแต่งโจทย์ หรือถ้าโจทย์ numerical insensitive เกินไป model อาจวิเคราะห์ผิดแต่ยังผ่าน

วิธีของ GeneBench-Pro คือรู้ causal structure และ data-generating process เต็ม แล้ว audit trace เพื่อหา leakage หรือ shortcut. ตรงนี้เป็น contamination control แบบกว้างกว่า "model เคยเห็นเฉลย" เพราะรวมถึงทางลัดที่ทำให้ agent ผ่านโดยไม่ต้องเลือก analytic pathway ที่ถูก

## See also

- [[deepswe]]
- [[genebench-pro]]
- [[behavioral-verifier]]
- [[reward-hacking]]
- [[verifiability]]
