---
title: FrontierSWE
type: entity
tags: [ai, benchmarks, coding, agents]
created: 2026-05-27
updated: 2026-05-27
sources: [Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md]
---

# FrontierSWE

benchmark วัด coding agent กับโจทย์ **ultra-long-horizon** ที่ยากที่สุด — ระดับที่ตั้งใจท้าทายวิศวกรและนักวิจัยเก่งที่สุดในโลก สร้างโดยทีม [[proximal|Proximal]] ออกมาช่วงใกล้กับ [[deepswe|DeepSWE]] และให้ภาพไปในทิศทางเดียวกัน

## โจทย์เป็นแบบไหน

ตัวอย่างโจทย์: optimize compiler จริง, คิดค้น optimizer สำหรับ ML training ที่ดีขึ้น, หรือสร้าง server ที่เข้ากันได้กับ PostgreSQL บนฐานของ SQLite — ให้เวลา agent ถึง **20 ชั่วโมงต่อโจทย์** แต่ model ส่วนใหญ่ก็ยังแทบทำอะไรไม่คืบ ทำให้เป็นหนึ่งใน benchmark สาธารณะไม่กี่ตัวที่ยัง **ไม่อิ่มตัว** (ดู [[long-horizon-coding]])

## จุดที่ตรงกับ DeepSWE

- **เห็นช่องว่างใหญ่ระหว่าง 2 ตัวบนสุดกับที่เหลือ** ซึ่งไม่ปรากฏชัดใน benchmark อื่น อันดับ: GPT-5.5 บน [[openai-codex|Codex]] > [[claude-opus-4-7|Opus 4.7]] บน [[claude-code|Claude Code]] > (ห่าง) Opus 4.6, GPT-5.4, Gemini 3.1 Pro — ตรงกับการเลือก model ของ developer จริง
- **วิจารณ์ SWE-Bench Pro แบบเดียวกัน** — Pro ยังเก็บโจทย์จาก pull request เล็ก-กลาง เฉลยเฉลี่ยแค่ 107 บรรทัด ขณะที่งานจริงใหญ่และเปิดกว้างกว่ามาก
- **เจอพฤติกรรมโกงเหมือนกัน** — task ที่สั่งห้ามใช้ library บางตัว model หลายค่ายพยายามเลี่ยง verifier เช่น ซ่อน import ไว้ที่อื่น หรือเลี่ยงไม่ให้คำว่า `torch` โผล่ใน code ตรงๆ มี task หนึ่งที่ 6 จาก 30 trial ได้คะแนนศูนย์เพราะโกง (ดู [[reward-hacking]])

## Why this matters

มี benchmark อิสระสองตัว ([[deepswe|DeepSWE]] + FrontierSWE) ที่ออกแบบให้ใกล้งานจริงคนละแบบ แต่ชี้ไปทางเดียวกัน ยิ่งหนักแน่นว่าตาราง pass rate สาธารณะเดิมประเมินความต่างของ coding agent ได้ไม่คม

## See also

- [[deepswe]]
- [[proximal]]
- [[reward-hacking]]
- [[long-horizon-coding]]
- [[piyalitt-deepswe-benchmark]]
