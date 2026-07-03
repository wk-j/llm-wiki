---
title: The Eternal Sloptember
type: source
tags: [ai, coding-agents, slop, software-quality, critique]
created: 2026-07-03
updated: 2026-07-03
sources: []
---

# The Eternal Sloptember / Sloptember ที่ไม่จบ

บทความของ [[the-singularity-is-nearer|the singularity is nearer]] บน `geohot.github.io` (2026-05-24) โจมตีการเอา AI agents มาใช้ใน software development อย่างแรง. จุดยืนหลักคือ coding agents ยัง “program” ไม่ได้จริง แค่เลียน distribution ของงาน programming ได้แนบเนียนขึ้นเรื่อย ๆ

- URL: https://geohot.github.io//blog/jekyll/update/2026/05/24/the-eternal-sloptember.html
- Author: [[the-singularity-is-nearer|the singularity is nearer]]
- วันที่ใน URL: 2026-05-24
- แกนเรื่อง: agents สร้าง output ที่ดูเหมือน code ดีขึ้น แต่ broken แบบตรวจยากขึ้น ทำให้องค์กรใหญ่เสี่ยงสะสม [[vibecoded-slop|vibecoded slop]] และ [[cognitive-debt|cognitive debt]]

## Thesis หลัก

ผู้เขียนเปิดด้วย claim แรงว่า “Agents cannot program.” เหตุผลคือ LLM เป็น statistical model ที่ mimic distribution ของ programming ได้เก่งขึ้น แต่ไม่ได้ผ่าน process แบบมนุษย์ที่เข้าใจระบบจริง

ประเด็นนี้ต่างจากคำวิจารณ์แบบ “model ยังไม่เก่งพอวันนี้”. ผู้เขียนกำลังบอกว่า process ผิดชนิด. ถ้า model แค่ทำนาย pattern ของ code ได้แนบเนียนขึ้น output จะดูถูกต้องขึ้น แต่ bug จะยิ่งซ่อนลึกขึ้น

ได้อะไร: slop ในบทนี้ไม่ใช่แค่ output ห่วยชัด ๆ แต่คือ output ที่หน้าตาดีขึ้นเรื่อย ๆ จน proxy เดิมอย่าง syntax, grammar, และ test ผ่านบางส่วนเริ่มหลอกเราได้

## ทดลองจริงแล้วแต่ยังไม่ไว้ใจ

ผู้เขียนบอกว่าเคยพยายามใช้ agents จริงประมาณ 6 เดือน ไม่ใช่ปฏิเสธเพราะกลัวเสีย status. ตัวอย่างที่ยกมา:

- เขียนบางส่วนของ [[tinygrad|tinygrad]] ด้วย agents
- reverse chip USB <-> PCIe ด้วย agents
- ลองหลาย model, harness, และ prompt

แต่ผลที่รู้สึกซ้ำ ๆ คือ agent ทำ progress ช่วงต้นเร็วมาก แล้วติดช่วง polish. หลังจากนั้น workflow กลายเป็นการดึง lever แบบ slot machine หวังว่ารอบหน้าจะ polish จนจบได้

ผู้เขียนไม่ได้บอกว่า AI ไม่มีประโยชน์. เขายอมรับว่า AI เป็น search ที่ดีกว่า Google สำหรับหลายงาน และทำ prototype ที่ไม่ต้อง polish ได้เร็วมาก. แต่เขาไม่เห็นว่า agent อยู่ใกล้ bar ของ software engineer ที่บริษัทดี ๆ ควรรับ

## ไม่ใช่แค่ status anxiety

บทความตอบข้อกล่าวหาว่า programmer ต่อต้าน AI เพราะกลัวเสียสถานะ. ผู้เขียนบอกว่าถ้าเครื่องมือทำงานได้จริง คนเขียนโปรแกรมไม่ได้กลัวอยู่แล้ว:

- [[afl|AFL]] หา bug ได้มากกว่า LLMs แต่ไม่มีใครรู้สึกว่ามันมาแย่ง status
- Chess และ Go ไม่ได้ตายหลัง AI เก่งกว่ามนุษย์
- ผู้เขียนอยากมี robot associates ที่ไว้ใจได้มาช่วย clean up code

ดังนั้นปัญหาไม่ใช่ “กลัวถูกแทนที่”. ปัญหาคือยังไม่ trust ว่า agent เหล่านี้ทำงานระดับ software engineer ได้จริง

## ทำไมองค์กรใหญ่เสี่ยงกว่าคนเก่งหรือทีมเล็ก

บทความแยกผลกระทบของ agents ตามชนิดขององค์กร. High-performing individuals และทีมเล็กยังพอรับมือได้ เพราะ feedback loop สั้น และคนเก่งมีนิสัย error correction: เห็น slop แล้วรู้ว่าเป็น slop

องค์กรใหญ่เจอเงื่อนไขตรงข้าม:

- feedback loop ช้ากว่า
- alignment น้อยกว่า
- bottom performers ไม่มี self-check เท่าคนเก่ง
- คนกลุ่มนี้อาจเป็นคนที่ผลิต “10x output” ด้วย agents มากที่สุด

ผลคือ average output ขององค์กรอาจแย่ลงแม้จำนวน code, app, และ feature เพิ่มขึ้น. ผู้เขียนเรียกยุคนี้ว่า golden era for buckets of slop และ dark age for gems of quality

ตรงนี้เชื่อมกับ [[orchestration-tax|orchestration tax]] และ [[cognitive-surrender|cognitive surrender]]: ถ้า output เร็วกว่า review capacity มากพอ มาตรฐานองค์กรจะลดลงแบบเงียบ ๆ

## Artifact ไม่ได้บอก process อีกต่อไป

แก่นที่ลึกที่สุดของบทความอยู่ตรงนี้. เวลาคนเห็น artifact ที่ syntax ดี grammar ดี หรือหน้าตาเหมือนงานมนุษย์ เราเคยเดาได้ว่ามี human process อยู่ข้างหลัง: มีคนเข้าใจ เจอปัญหา ตัดสินใจ และรับผิดชอบ

พอมี LLM assumption นี้ก็ไม่จริงเสมอไปแล้ว. Artifact อาจออกมาจาก process ที่ไม่ได้เข้าใจระบบเหมือนมนุษย์ แต่หน้าตาเหมือนงานมนุษย์มากพอให้ proxy เดิมใช้ไม่ได้

นี่คือ [[quality-proxy-collapse|quality proxy collapse]]: สิ่งที่เคยเป็นสัญญาณคุณภาพ เช่น syntax, grammar, structure, หรือ confidence เริ่มวัดไม่ได้ว่างานนั้น build ต่อได้จริงไหม

## LeCun/Marcus camp และ world models

ผู้เขียนบอกว่าตอนนี้ย้ายมาอยู่ฝั่ง [[yann-lecun|Yann LeCun]] / [[gary-marcus|Gary Marcus]] ในเรื่อง LLMs แบบไม่ endorse ทุกอย่าง. มุมที่เห็นด้วยคือ LLM ล้วน ๆ ไม่น่าพอสำหรับ programming agents จริง

คำสำคัญคือ [[programming-process-matters|process matters]]. Programming ไม่ใช่แค่สร้างข้อความ code ที่ดูเหมือน code. มันต้องมี model ของโลกหรือระบบที่ code ไปกระทบ. ผู้เขียนเชื่อว่า deep learning ยังเป็นทางออก แต่ agent ที่ program ได้จริงต้องมี world models มากกว่าแค่ RLVR ที่หาทางผ่าน test โดย comment out failing test

## Open questions

- claim “agents cannot program” เป็นข้อจำกัดของ LLM-style agent ปัจจุบัน หรือเป็นข้อจำกัดถาวรของแนวทางนี้
- world model ที่พอสำหรับ programming ควรหน้าตาเป็นอย่างไร และต่างจาก memory/context/harness อย่างไร
- ทีมเล็กที่มี review discipline จะได้ประโยชน์สุทธิจาก agents มากกว่าหรือแค่เสียหายน้อยกว่าองค์กรใหญ่
- benchmark ที่วัด polish, maintainability, และ process understanding ควรต่างจาก coding benchmark ปัจจุบันอย่างไร
- ถ้า agent มี deterministic verifier แข็งพอ เช่น fuzzing, property test, formal spec, หรือ behavioral verifier ข้อวิจารณ์นี้ลดลงแค่ไหน

## See also

- [[ai-slop]]
- [[vibecoded-slop]]
- [[cognitive-debt]]
- [[cognitive-surrender]]
- [[agentic-coding-trap]]
- [[building-pi-world-of-slop]]
- [[quality-proxy-collapse]]
- [[programming-process-matters]]
- [[tinygrad]]
- [[afl]]
