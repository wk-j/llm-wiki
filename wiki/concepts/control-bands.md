---
title: Control Bands
type: concept
tags: [ai, agents, monitoring, sre, governance, sdlc, automation]
created: 2026-09-14
updated: 2026-09-14
sources: [ai-native-sdlc-playbook.md]
---

# Control Bands / ระดับความผิดปกติที่กำหนดสิทธิ์ของ agent

**Control band** คือวิธีผูกสิทธิ์ของ agent เข้ากับความรุนแรงของสิ่งที่ตรวจเจอ ยิ่งค่าเบี่ยงจากปกติมาก agent ยิ่งทำได้มาก แนวคิดนี้มาจาก [[ai-native-sdlc-playbook|AI-Native SDLC Playbook]] ของ [[anthropic|Anthropic]] ในช่วง Maintain

วิธีนี้ **แยกชั้นตรวจจับออกจากชั้นตอบสนอง** การตัดสินว่า "ผิดปกติหรือยัง" ไม่ใช้ model ส่วน model เข้ามาทำงานตอนตัดสินว่าจะทำอะไรต่อ

## ชั้นตรวจจับ: ห้ามมี model

ชั้นนี้เป็น script ธรรมดาที่เฝ้า metric เทียบกับ baseline แบบ rolling เช่น 30 วันย้อนหลัง แล้วใช้กฎสถิติจับความเบี่ยง playbook อ้าง Western Electric rules ที่เป็นชุดกฎจากงาน statistical process control ในโรงงาน พูดง่าย ๆ คือกฎที่บอกว่าจุดแบบไหนถือว่าหลุดจากความผันผวนปกติ

Metric ที่ยกตัวอย่างเป็นของฝั่ง delivery ไม่ใช่แค่ระบบ: อัตรา test พังใน CI, 5xx หลัง deploy, PR cycle time

เหตุผลที่ต้อง deterministic มีสองข้อ หนึ่งคือผลต้องเหมือนเดิมทุกครั้งและอธิบายให้ auditor ฟังได้ สองคือถ้าให้ model เป็นคนตัดสินว่ามีปัญหาไหม ก็เท่ากับเอา [[llm-nondeterminism|ความไม่แน่นอน]] ไปวางไว้ที่ชั้นล่างสุดของระบบเตือนภัย

**ได้อะไร:** เกณฑ์ที่ใช้เรียกระบบอัตโนมัติตรวจซ้ำแล้วให้ผลเดิม แม้ชั้นตอบสนองจะใช้ model

## ชั้นตอบสนอง: ไล่ระดับตามความเบี่ยง

สิทธิ์ของ agent เขียนไว้ในไฟล์ที่ versioned (playbook ใช้ชื่อ `bands.yaml`) โครงที่เสนอคือสามชั้น

| ระดับ | agent ทำอะไรได้ |
| --- | --- |
| 1σ | บันทึกอย่างเดียว ไม่เรียก agent |
| 2σ | เรียก agent มาวินิจฉัย แบบอ่านอย่างเดียว โดยจำกัด tool ไว้ เช่น `Read`, `Grep`, `Bash(gh run view *)` |
| 3σ | ลงมือได้ แต่เฉพาะทางที่เปิดไว้ คือเปิด PR หรือเรียก runbook ที่อนุมัติแล้ว |

สองคำที่ต้องแยกให้ออกคือ **action** กับ **route** action บอกว่าทำอะไรได้ (log / diagnose / propose) ส่วน route บอกว่าออกทางไหนได้บ้าง ต่อให้ถึง 3σ agent ก็ยัง merge เองไม่ได้ ทำได้เพียงเปิด PR เข้าคิวให้คนตรวจ

ผลการวินิจฉัยไม่ได้จบเป็นรายงาน แต่เขียนออกมาเป็น [[intent-md|`intent.md`]] แล้วไหลกลับเข้าต้นวงจร กลายเป็น [[artifact-chain|artifact chain]] เส้นเดียวกับงานที่มาจากไอเดียของคน

**ผลคือ:** ระบบเตรียม diagnosis กับข้อเสนอไว้ก่อนที่คนจะเปิดคอมพ์ แต่การตัดสินใจที่ย้อนยากยังรอคน

## ทำไมไม่ตั้งเป็น threshold เดียวไปเลย

เพราะ threshold เดียวบังคับให้เลือกอย่างใดอย่างหนึ่ง ตั้งไวไปก็ได้ alert ท่วมจนคนเลิกอ่าน ตั้งช้าไปก็จับของไม่ทัน การไล่ระดับทำให้ค่าเบี่ยงเล็กน้อยมีที่ไปโดยไม่ต้องรบกวนใคร แล้วสงวนทั้งค่า token และความสนใจของคนไว้ให้เคสที่หนักจริง

หลักนี้เหมือน [[graduated-autonomy|graduated autonomy]] แต่เปลี่ยนตัวแปรจาก "งานนี้เสี่ยงแค่ไหน" เป็น "ตอนนี้ระบบเบี่ยงแค่ไหน"

## ปรับ band จากผลที่เจอจริง

ระบบต้องรับ feedback กลับมาสองทาง

- **คน dismiss เคสไหน ให้นำผลไปปรับ band:** ถ้า on-call ปัดตกซ้ำ ๆ แปลว่า band ไวเกินไปสำหรับ metric นั้น การแก้ band ต้องผ่านเจ้าของ policy
- **พอแก้จริง ให้เพิ่ม eval ของ incident class นั้น:** CI รอบหน้าจะได้จับปัญหาเดิมเอง ไม่ต้องรอ band ลั่นซ้ำ ต่อกับ [[evals-and-error-analysis]]

**ได้อะไร:** ระบบเรียนรู้จาก incident โดยความรู้ไปลงที่ชุดทดสอบ ไม่ได้ไปลงที่หัวของ on-call คนใดคนหนึ่ง

## จุดที่ควรระวัง

- **กฎจากโรงงานกับ metric ของซอฟต์แวร์ไม่เหมือนกัน:** Western Electric rules ตั้งอยู่บนสมมติฐานว่า process ค่อนข้างนิ่ง ส่วน delivery metric มี seasonality (ศุกร์บ่าย ปลาย sprint) และ regime change (เปลี่ยน CI runner เปลี่ยน model) ที่ทำให้ baseline เก่าใช้ไม่ได้ทันที
- **เลือก metric ผิดแล้วทุกอย่างข้างบนพลอยผิด:** ถ้าเฝ้าแต่ตัวที่ขยับง่าย ระบบจะไวกับเรื่องที่ไม่สำคัญ
- **band เป็นสิทธิ์ ไม่ใช่แค่ตัวเลข:** ใครแก้ `bands.yaml` ได้ก็ขยายสิทธิ์ agent ได้ ไฟล์นี้จึงควรอยู่ใต้ review เดียวกับ permission ดู [[policy-as-code-for-agents]]
- **3σ ที่เปิด PR เยอะ ๆ ก็สร้างคิว:** ถ้าคน triage ไม่ทัน ระบบก็แค่ย้ายกองงานไปอีกที่ ดู [[acceptance-bottleneck]]

## See also

- [[ai-native-sdlc-playbook]]
- [[policy-as-code-for-agents]]
- [[graduated-autonomy]]
- [[intent-md]]
- [[artifact-chain]]
- [[ai-driven-sdlc]]
- [[evals-and-error-analysis]]
- [[agent-observability]]
- [[self-healing-environments]]
- [[acceptance-bottleneck]]
