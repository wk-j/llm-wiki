---
title: Harness vs Execution Environment
type: concept
tags: [ai, agents, harness, sandboxing, security, architecture]
created: 2026-10-07
updated: 2026-10-07
sources: [what-is-codemode-armin-ronacher.md]
---

# Harness vs Execution Environment / สมองกับมือของ agent

[[armin-ronacher|Armin Ronacher]] (developer ที่ทำ [[pi-agent|Pi]]) ใช้ภาพ **brains vs hands** ใน [[what-is-codemode-armin-ronacher|What is Codemode]] เพื่อชี้ว่า coding agent หนึ่งตัวมีระบบสองฝั่งที่ควรแยกให้ออก พอแยกได้ ก็ตอบได้ว่า tool แต่ละตัวควรอยู่ฝั่งไหน และ sandbox กั้นอะไรได้จริง

## สองฝั่ง

| ฝั่ง | คืออะไร | ลักษณะ |
| --- | --- | --- |
| **Brain** | ตัว harness ที่คุย LLM ถือ session และ tool definition | รันบนเครื่องหนึ่ง เป็นฝั่งที่เชื่อถือได้ |
| **Hands** | ที่ที่ tool รันจริง Pi เรียกว่า **execution environment** คือเป้าของทุก operation | หลายครั้งเป็นเครื่องเดียวกับ harness แต่ไม่จำเป็น และอาจอยู่ใน sandbox |

สองฝั่งนี้มีระบบไฟล์คนละชุด และระดับความเชื่อถือต่างกัน คำสั่ง `bash` รันฝั่ง hands ส่วนการฉีดรูปเข้า protocol ของ LLM การสั่ง subagent หรือการเรียก model อื่นผ่าน SDK ต้องเกิดฝั่ง brain

**ผลคือ:** "agent รันที่ไหน" มีสองคำตอบเสมอ ต้องถามแยกทั้งสองฝั่ง

## Sandbox ฝั่งหนึ่งไม่ได้กั้นอีกฝั่ง

Armin ยกตัวอย่าง Gondolin (sandbox ที่ลิงก์อยู่ใต้ `earendil-works.github.io`) ถ้าใช้ Gondolin คำสั่ง bash จะถูก sandbox ดี แต่ตัว harness ไม่ได้อยู่ใน sandbox นั้น

นี่สำคัญเวลาประเมินความเสี่ยง ถ้า tool ไหนรันฝั่ง harness มันได้สิทธิ์ของ harness ไม่ใช่สิทธิ์ของ sandbox [[codemode|Codemode]] ของ Pi จึงต้องมี sandbox ของตัวเองแยกต่างหาก คือ QuickJS ใน WASM ที่ไม่มี network ไม่มี file system ไม่มี timer และ RAM จำกัด

ตรงนี้ต่อกับหลัก [[agent-runtime-untrusted|Agent Runtime as Untrusted Component]]: ขอบเขตความเสียหายต้องบังคับจากโครงสร้าง และต้องรู้ว่าแต่ละโครงสร้างคลุมฝั่งไหน การมี sandbox ฝั่ง execution environment ไม่ได้แปลว่า agent ทั้งระบบถูกกั้นแล้ว

**ได้อะไร:** ไล่ทีละ tool ว่ารันฝั่งไหน แล้วเช็กว่ามีอะไรกั้นอยู่ฝั่งนั้นจริงไหม

## เลือกฝั่งให้ tool

- **ทำกับไฟล์และโปรแกรมใน repo** → ฝั่ง hands ผ่าน bash ได้ประโยชน์ที่ model รู้จักระบบไฟล์จากตอน train
- **ต้องแตะ protocol ของ LLM หรือ state ของ harness** (ดูรูป, subagent, model อื่น, state ข้ามรอบ) → ฝั่ง brain เป็น tool ของ harness หรือเรียกผ่าน Codemode
- **งานหลายขั้นที่ต่อ tool ทั้งสองฝั่ง** → Codemode รันฝั่ง brain แล้วเรียก `tools.bash` ไปฝั่ง hands ได้ ข้อมูลที่ `store()` ไว้อยู่ฝั่ง brain ไม่ได้อยู่ใน sandbox

ทางเลือกอื่นคือเขียน CLI ฝั่ง hands ให้คุยกับ harness ผ่าน environment variable กับ Unix socket Armin บอกว่าทำได้ แต่หยาบ และยังทำให้สับสนว่า code รันฝั่งไหน

## เรื่องที่ยังตอบไม่ได้

- บทความไม่ได้ลงรายละเอียดว่า Pi ส่งข้อมูลข้ามสองฝั่งอย่างไรเมื่อ execution environment อยู่คนละเครื่อง
- ยังไม่มีรายละเอียดว่า Gondolin กั้นอะไรบ้าง วิกินี้ยังไม่ได้ ingest แหล่งตรงของ Gondolin

## See also

- [[codemode]]
- [[what-is-codemode-armin-ronacher]]
- [[agent-runtime-untrusted]]
- [[pi-agent]]
- [[coding-harness]]
- [[subagent-patterns]]
- [[cloud-agents]]
