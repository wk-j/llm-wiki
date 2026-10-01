---
title: OpenCode Reloaded
type: source
author: Kit Langton
url: https://anoma.ly/notes/opencode-reloaded/
date_published: 2026-09-21
date_ingested: 2026-09-22
tags: [ai, coding-harness, hot-reload, opencode, plugins, state-management]
created: 2026-09-22
updated: 2026-09-22
sources: ["https://anoma.ly/notes/opencode-reloaded/"]
---

# OpenCode Reloaded / เปลี่ยนสภาพแวดล้อมโดยไม่หยุด Agent

[[kit-langton|Kit Langton]] (ผู้เขียน opencode notes) อธิบายว่า [[opencode|OpenCode 2]] เปลี่ยน config เชื่อม MCP server หรือเขียน plugin ระหว่างที่กำลังทำงานได้ แล้วทุก session เห็นผลทันที Agent จึงสร้าง tool ให้ตัวเองและเรียกใช้ใน turn เดียวกันได้ ไม่ต้องปิดโปรแกรม พิมพ์ `/reload` หรือเริ่ม session ใหม่

เรื่องยากไม่ใช่แค่เฝ้าดูว่าไฟล์เปลี่ยนเมื่อไร แต่คือทำอย่างไรให้ plugin หลายตัวแก้ environment ชุดเดียวกันโดยไม่ทับกัน OpenCode แก้ด้วย [[replayable-state-transformations|Replayable State Transformations]]: plugin แต่ละตัวลงทะเบียน transformation ของตัวเอง ส่วน host สร้าง state ใหม่จากค่าว่างแล้วรัน transformation ทุกตัวตามลำดับ

## ปัญหาของ shared mutable catalog

ตัวอย่างในบทความเริ่มจาก model catalog ที่ plugin หลายตัวแก้โดยตรง:

- `models-dev.ts` ดึงรายชื่อ provider จาก `models.dev` ตอนเริ่ม แล้ว refresh ทุกชั่วโมง
- `provider-policy.ts` ปิด model จาก provider ที่นโยบายองค์กรไม่อนุญาต
- `limits.ts` ลด output limit ของทุก model ลงครึ่งหนึ่ง
- `local-model.ts` เพิ่ม model ที่รันในเครื่อง

แบบแรกดูตรงไปตรงมา เพราะทุก plugin เข้าถึง `ctx.catalog` แล้วแก้ค่าได้เลย แต่ state สุดท้ายขึ้นกับว่าแต่ละตัวรันกี่ครั้งและรันก่อนหลังอย่างไร

เมื่อ `models-dev.ts` refresh แล้วเขียน provider record ชุดใหม่ policy ที่ปิด model ไว้จะหายไป ถ้า `models.dev` ลบ provider ตัวหนึ่ง provider นั้นกลับค้างอยู่ใน catalog เพราะไม่มีใครลบของเก่า ส่วน `halveLimits` ยิ่งเห็นปัญหาชัด พอรันซ้ำเพื่อรองรับ model ที่เพิ่งเพิ่ม limit ของ model เดิมจะลดจากครึ่งหนึ่งเหลือหนึ่งในสี่

ถ้าให้ policy plugin subscribe event แล้วรันซ้ำหลัง refresh วิธีนี้จะช่วยได้เฉพาะ operation ที่ idempotent เช่นปิด model ที่ปิดอยู่แล้ว ยังต้องคุมไม่ให้ session ใดอ่าน catalog ในช่วงที่ refresh เสร็จแต่ policy ยังไม่ตามมา และใช้ไม่ได้กับ transformation ที่ผลเปลี่ยนทุกครั้งเมื่อรันซ้ำ

**ได้อะไร:** ถ้า plugin แก้ shared state โดยตรง เจ้าของ plugin ต้องจำทั้งประวัติของ state และสิ่งที่ plugin ตัวอื่นเคยทำ ระบบจึงซับซ้อนขึ้นทุกครั้งที่เพิ่ม contributor ใหม่

## ให้ plugin ประกาศ transformation แทนการแก้ค่ากลาง

OpenCode เปลี่ยน `ctx.catalog` จากตัว catalog เป็น handle สำหรับลงทะเบียน transformation แต่ละ plugin บอกแค่ว่าตัวเองต้องเปลี่ยน catalog อย่างไร แล้ว host เป็นคนเก็บลำดับและประกอบผล:

1. เริ่มจาก catalog ว่าง
2. `models-dev.ts` ใส่ provider ที่เพิ่งดึงมา
3. `local-model.ts` เพิ่ม model ในเครื่อง
4. `provider-policy.ts` ปิด provider ที่ไม่อนุญาต
5. `limits.ts` ลด output limit ครั้งเดียว
6. publish catalog ก้อนใหม่ให้ทุก session

ลำดับยังมีผล แต่ OpenCode เป็นเจ้าของลำดับนั้นเพียงจุดเดียว Plugin ไม่ต้อง subscribe การเปลี่ยนของกันเองหรือเก็บว่าเคยแก้ record ไหนแล้ว

บทความใช้คำทาง functional programming ว่า transformation เหล่านี้เป็น endomorphism คือรับค่าและคืนค่าชนิดเดิม เมื่อนำหลายตัวมาเรียงกันก็ยังได้ transformation ของชนิดเดิม จึงประกอบและ replay ได้เป็นชุด

**ผลคือ:** bug ที่เกิดจากประวัติการแก้ state หายไป เพราะ rebuild ทุกครั้งเริ่มจากฐานเดียวและรัน contribution แต่ละตัวหนึ่งครั้ง

## Refresh ข้อมูลโดยไม่เปลี่ยน transformation

`models-dev.ts` ยังต้องดึงข้อมูลใหม่ทุกชั่วโมง Plugin จึงเก็บ provider ชุดล่าสุดไว้ในตัวแปร แล้วลงทะเบียน transformation ที่อ่านตัวแปรนั้นตอนทำงาน พอ fetch รอบใหม่เสร็จ plugin ก็แทนค่าตัวแปรแล้วเรียก `ctx.catalog.reload()`

`reload()` สร้าง catalog ว่าง รัน transformation ทุกตัวใหม่ แล้ว publish ผลพร้อมกัน Transformation ของ `models-dev.ts` ไม่ต้องลงทะเบียนใหม่ แต่รอบ rebuild ถัดไปจะอ่านข้อมูลล่าสุดที่ closure ถืออยู่

วิธีนี้แก้ตัวอย่างก่อนหน้าได้ครบ:

- provider ที่หายจาก `models.dev` จะหายจาก catalog รอบใหม่
- policy รันหลังข้อมูลต้นทางทุกครั้ง จึงไม่ถูก refresh เขียนทับ
- `halveLimits` รันครั้งเดียวต่อ rebuild จึงลด 128K เป็น 64K ไม่ไหลลงเป็น 32K

**ได้อะไร:** refresh เปลี่ยน input ล่าสุด ไม่ได้สะสม mutation ไว้บนผลรอบก่อน

## `State` ใช้กับ environment ทุกส่วน

Model catalog เป็นเพียงตัวอย่าง OpenCode ใช้ abstraction ชื่อ `State` กับ registry ของ skill, command, agent, tool, MCP server และ formatter ด้วย `State` มี operation หลักสองตัว:

- `transform` ลงทะเบียน transformation
- `reload` สร้างค่าปัจจุบันใหม่จาก contribution ที่ยัง active

เมื่อมีไฟล์ plugin ใหม่ built-in file-watcher plugin จะรันไฟล์นั้นและผูก transformation ที่ลงทะเบียนไว้กับเจ้าของไฟล์ ถ้าลบไฟล์ OpenCode จะถอด contribution ของไฟล์นั้นแล้ว rebuild `State` ที่เกี่ยวข้อง ส่วนการแก้ไฟล์เท่ากับถอดของเก่า รันไฟล์ใหม่ แล้ว rebuild

ทุก session อ้าง state ที่ publish ล่าสุดอยู่แล้ว จึงเห็น plugin, tool หรือ MCP server ชุดใหม่พร้อมกัน โดยไม่ต้อง restart session ทีละตัว

## ขอบเขตของคำอธิบาย

บทความอธิบาย pattern และมี code ตัวอย่างครบเส้นทาง แต่ไม่ได้ให้ benchmark ว่า reload ใช้เวลาหรือ memory เท่าไรเมื่อมี plugin จำนวนมาก ยังไม่บอกด้วยว่าถ้า transformation ตัวหนึ่ง throw error ระบบจะ rollback เก็บ state ก้อนเดิม หรือ publish บางส่วนอย่างไร

คำว่า deterministic ในบทความมีเงื่อนไขว่า starting state, data และลำดับ transformation ต้องเหมือนเดิม ข้อมูลจาก network ยังเปลี่ยนได้ และ transformation ที่มี side effect ก็อาจทำให้ผลไม่เหมือนเดิม Pattern นี้จึงลด history-dependent mutation แต่ไม่ได้ทำให้ external input หรือ plugin code ปลอดความไม่แน่นอนเอง

ไฟล์ plugin ก็เป็น executable code บทความพูดถึง lifecycle และ composition แต่ไม่ได้อธิบาย permission, sandbox, signature, trust policy หรือวิธีแยก plugin ที่ไม่น่าไว้ใจ เรื่อง hot reload จึงไม่ใช่ security boundary

## See also

- [[opencode]]
- [[kit-langton]]
- [[replayable-state-transformations]]
- [[coding-harness]]
- [[plugin-manager]]
- [[model-context-protocol]]
