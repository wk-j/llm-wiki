---
title: Nattee Niparnan
type: entity
tags: [person, thai, education, ai, software-engineering]
created: 2026-04-18
updated: 2026-04-28
sources: [llm-era-computer-engineering-nattee.md, llm-era-computer-engineering-ep3-nattee.md]
---

# Nattee Niparnan / ณัฐที นิภาชน์

อาจารย์ประจำภาควิชาวิศวกรรมคอมพิวเตอร์ (CEDT) จุฬาลงกรณ์มหาวิทยาลัย ผู้เขียนซีรีส์บน Facebook *"วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง"* ซึ่งกลายเป็นบันทึกสำคัญเกี่ยวกับแนวทางการปรับตัวของวิศวกรและภาคการศึกษาในยุค Agent

## ประเด็นสำคัญจากซีรีส์

| ตอนที่ | วันที่ | หัวข้อหลัก | คีย์เวิร์ดสำคัญ |
|---|---|---|---|
| **Ep. 1** | 10 เม.ย. 2026 | LLM ในห้องเรียนและห้องสอบ | Prompt-as-exam, -10 pts hint cost |
| **Ep. 2** | ~17 เม.ย. 2026 | Coding Agent ในงานจริง | [[taste-paradox]], $140 PoC |
| **Ep. 3** | 28 เม.ย. 2026 | การรู้จักตัวเองและการเลือกทางลึก | [[eh-gland|ต่อมเอ๊ะ]], [[horror-vacui]], เป็ดไม่รอด |

## ส่วนร่วมและแนวคิดหลัก

### 1. [[eh-gland|ต่อมเอ๊ะ (Eh Gland)]]
แนวคิดที่ขยายต่อจาก [[taste-paradox]] ใน Ep. 3: คือสัญชาตญาณในการตรวจพบความผิดปกติที่ AI มองข้าม (เช่น domain logic) ซึ่งจะ "ฝ่อ" ลงถ้าเรา outsource งานให้ AI ทั้งหมดโดยไม่ฝึกมือเอง

### 2. การล่มสลายของ "เป็ด" (Shrinking Generalist Moat)
Nattee สังเกตว่าความรู้กว้างๆ แบบพอทำได้ (generalist) ในด้าน Network, Infra หรือ Ops ที่เคยเป็นจุดแข็ง กลับถูก AI เข้ามาแทนที่ได้ง่ายมาก (เช่น การ config switch หรือเซ็ต Proxmox) ทำให้ค่าตัวของความเป็น "เป็ด" ลดลง และผลักดันให้คนต้องเลือก "ลึก" ในบางด้านเพื่อรักษาความสามารถในการคุม AI

### 3. การใช้ AI ปิดจุดอ่อน (Gap Closing)
- **Testing**: ใช้ Claude Code เขียน test suite (225 tests) เพื่อปิดจุดอ่อนที่เจ้าตัวไม่ชอบเขียน test
- **UI/UX**: ใช้ Gemini ช่วยแก้ปัญหา [[horror-vacui|Horror Vacui]] (โรคกลัวที่ว่าง) ซึ่งเป็นจุดอ่อนที่ทำให้ดีไซน์ของเขาเป็น "Wall of Text" มาตลอด

## การดูแล cafe-grader
ปัจจุบันเป็นผู้ดูแล [`cafe-grader`](https://github.com/nattee/cafe-grader-web) ระบบตรวจงานอัตโนมัติของภาควิชาที่ริเริ่มโดย อ. มะนาว (Jittat Fakcharoenphol) และ อ. โป้ง (Pramook Khungurn)

## เพื่อนร่วมงานที่กล่าวถึง
- **Noppakorn Jiravaranun (อ. มีน)** — Super TA ผู้เชี่ยวชาญด้าน Proxmox, Grafana, และ Network Infrastructure ที่ช่วยวางระบบให้ภาควิชา (Ep. 3)

## ดูเพิ่ม

- [[llm-era-computer-engineering-nattee]]
- [[llm-era-computer-engineering-ep3-nattee]]
- [[eh-gland]]
- [[taste-paradox]]
- [[horror-vacui]]

