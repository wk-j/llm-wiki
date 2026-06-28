---
title: Andrej Karpathy
type: entity
tags: [person, ai, llm]
created: 2026-04-12
updated: 2026-04-30
sources: [LLM Knowledge Bases Thread by @karpathy.md, forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls..md, "Karpathy's LLM Wiki The Complete Guide to His Idea File.md", Andrej Karpathy From Vibe Coding to Agentic Engineering.md, Self Learning for Agents Clearly Explained.md]
---

# Andrej Karpathy / อันเดรจ คาร์พาธี

นักวิจัยและผู้สอนด้าน AI อดีต Director of AI ที่ Tesla และผู้ร่วมก่อตั้ง OpenAI เป็นผู้บัญญัติศัพท์ "vibe coding" เป็นที่รู้จักจากการทำให้ deep learning เข้าใจง่าย (คอร์ส CS231n ที่ Stanford, วิดีโอบรรยายบน YouTube) ปัจจุบันเป็นผู้ก่อตั้ง Eureka Labs และมุ่งเน้นการสร้าง [[ai-native-education]]

## ความเกี่ยวข้องกับ wiki นี้

เป็นผู้ริเริ่มหลายรูปแบบที่ wiki นี้กล่าวถึง:

- **[[llm-knowledge-bases]]** — personal wiki ที่รวบรวมโดย LLM ซึ่งเป็นรูปแบบหลักที่ wiki นี้ใช้งาน
- **[[idea-file]]** — การแบ่งปันรูปแบบ (schema) เพื่อให้ LLM agents นำไปสร้างเป็นรูปธรรม แทนที่จะแบ่งปันโค้ด
- **[[vibe-coding]]** — การเขียนโปรแกรมด้วย "vibe" (ความรู้สึกและทิศทาง) โดยให้ LLM จัดการ implementation ทั้งหมด

## วิวัฒนาการสู่ Agentic Engineering (2026)

ในงาน Sequoia AI Ascent 2026, Karpathy ได้ขยายความแนวคิดจากปีที่ผ่านมา:

- **[[agentic-engineering]]** — คือก้าวต่อไปของ [[vibe-coding]] ที่เน้นการรักษาคุณภาพระดับ professional (engineering discipline) ในขณะที่ gain speed 10x-100x ผ่านการประสานงาน [[agent-swarm|agent]] หลายตัว
- **[[software-3-0]]** — นิยามใหม่ของการเขียนโปรแกรม คือการใช้ context window เป็น lever ในการสั่งการ LLM interpreter
- **[[jagged-intelligence]]** — มุมมองต่อ LLM ว่าเป็น "ghosts" (statistical simulation) ที่มีความเก่งแบบฟันปลา (jagged) คือเก่งงานยากอย่างการ refactor code มหาศาล แต่พลาดเรื่องง่ายๆ อย่างการนับจำนวนตัวอักษรหรือตรรกะพื้นฐาน

## AutoResearch — model ที่ปรับ model

ใน [[self-learning-for-agents-explained]] Karpathy ปรากฏผ่านโปรเจกต์ **AutoResearch**: ชี้ coding agent ไปที่ training setup เล็ก ๆ แล้วปล่อยรันข้ามคืน — แก้ไฟล์เดียว, เทรน 5 นาที, ให้คะแนนผล, เก็บถ้าดีขึ้นไม่งั้น undo, วนเป็นร้อยรอบก่อนคุณตื่น. เจอ speedup จริง ~11%. เป็นตัวอย่างของ self-learning **ชั้น Model** (ดู [[three-learning-layers]]).

**ข้อจำกัดที่น่าสนใจ:** agent ปรับ model *อีกตัวที่เล็กกว่า* — weight ของตัว agent เองไม่เคยเปลี่ยน. และเหมือนทุกวิธีในชั้น Model มันรันได้แค่ที่คอมพิวเตอร์ให้คะแนนได้ฟรี ซึ่งเข้ากับธีม [[llm-coding-pitfalls]] ที่ Karpathy ชูเอง: ที่ที่วัดผลได้ชัด AI ทำได้ดี ที่ที่วัดยากต้องมีคน.

## แนวปฏิบัติและปรัชญา

- **Outsource thinking, not understanding**: เราสามารถให้ AI ช่วยคิด (process/implement) ได้ แต่ความเข้าใจ (understanding) และทิศทาง (direction) ต้องอยู่ที่มนุษย์
- **Human as Director**: หน้าที่ของมนุษย์เปลี่ยนจาก "คนเขียนโค้ด" เป็น "ผู้กำกับ" (Director of Taste & Judgment)
- **Agent-Native Infrastructure**: สนับสนุนให้สร้าง infra ที่เอื้อต่อ agent (เช่น docs ที่เขียนให้ agent อ่าน) ไม่ใช่ออกแบบมาเพื่อมนุษย์อย่างเดียว

## The idea file gist

หลังจากที่ทวีตเรื่อง LLM Knowledge Bases ของเขาไวรัล Karpathy ได้เผยแพร่ GitHub gist ชื่อ "LLM Wiki" — ซึ่งไม่ใช่โค้ด ไม่ใช่แอป แต่เป็น [[idea-file]]: คำอธิบายเชิงโครงสร้าง, ปรัชญา, และเครื่องมือ จุดประสงค์คือ: "หน้าที่เดียวของเอกสารนี้คือการสื่อสารรูปแบบ ที่เหลือ LLM ของคุณสามารถคิดต่อได้เอง"

เขเชื่อมโยงรูปแบบนี้อย่างชัดเจนกับแนวคิด [[memex]] ของ [[vannevar-bush]] ในปี 1945 — คือเส้นทางความรู้ (associative trails) ที่เป็นส่วนตัวและผ่านการคัดสรร

## ดูเพิ่ม

- [[vibe-coding]]
- [[agentic-engineering]]
- [[software-3-0]]
- [[jagged-intelligence]]
- [[llm-knowledge-bases]]
- [[idea-file]]
- [[memex]]
- [[three-learning-layers]]
- [[self-learning-for-agents-explained]]
