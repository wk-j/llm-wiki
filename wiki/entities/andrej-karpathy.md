---
title: Andrej Karpathy
type: entity
tags: [person, ai, llm]
created: 2026-04-12
updated: 2026-04-23
sources: [LLM Knowledge Bases Thread by @karpathy.md, forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls..md, "Karpathy's LLM Wiki The Complete Guide to His Idea File.md"]
---

# Andrej Karpathy

นักวิจัยและผู้สอนด้าน AI อดีต Director of AI ที่ Tesla และผู้ร่วมก่อตั้ง OpenAI เป็นผู้บัญญัติศัพท์ "vibe coding" เป็นที่รู้จักจากการทำให้ deep learning เข้าใจง่าย (คอร์ส CS231n ที่ Stanford, วิดีโอบรรยายบน YouTube) มีความเคลื่อนไหวบน Twitter (@karpathy)

## ความเกี่ยวข้องกับ wiki นี้

เป็นผู้ริเริ่มหลายรูปแบบที่ wiki นี้กล่าวถึง:

- **[[llm-knowledge-bases]]** — personal wiki ที่รวบรวมโดย LLM (กระทู้ X วันที่ 2 เม.ย. 2026) ซึ่งเป็นรูปแบบที่ wiki นี้ใช้งาน
- **[[idea-file]]** — การแบ่งปันรูปแบบที่เป็นนามธรรมเพื่อให้ LLM agents นำไปสร้างเป็นรูปธรรม แทนที่จะแบ่งปันโค้ด (gist ที่เผยแพร่ตามมาในวันที่ 4 เม.ย. 2026)
- **[[llm-coding-pitfalls]]** — ข้อสังเกตสาธารณะเกี่ยวกับโหมดความล้มเหลวของการแก้ไขโค้ดด้วย LLM ([tweet](https://x.com/karpathy/status/2015883857489522876)) ซึ่งต่อมาถูก [[forrestchang]] นำไปทำเป็น skill ของ Claude Code ชื่อ [[karpathy-guidelines]]

ทั้งสามแนวทางนี้ล้วนแนะนำให้ใช้ไฟล์คำสั่ง Markdown ที่มีน้ำหนักเบา (`AGENTS.md`, `CLAUDE.md`, `SKILL.md`) แทนที่จะใช้ tooling ที่ซับซ้อน

## The idea file gist

หลังจากที่ทวีตเรื่อง LLM Knowledge Bases ของเขาไวรัล ("Wow, this tweet went very viral!") Karpathy ได้เผยแพร่ GitHub gist ชื่อ "LLM Wiki" — ซึ่งไม่ใช่โค้ด ไม่ใช่แอป แต่เป็น [[idea-file]]: คำอธิบายเชิงโครงสร้าง, ปรัชญา, และเครื่องมือ จุดประสงค์ที่ระบุไว้คือ: "หน้าที่เดียวของเอกสารนี้คือการสื่อสารรูปแบบ ที่เหลือ LLM ของคุณสามารถคิดต่อได้เอง"

เขาเชื่อมโยงรูปแบบนี้อย่างชัดเจนกับแนวคิด [[memex]] ของ [[vannevar-bush]] ในปี 1945 — คือเส้นทางความรู้ (associative trails) ที่เป็นส่วนตัวและผ่านการคัดสรร "ส่วนที่เขาแก้ไม่ได้คือใครจะเป็นคนดูแลรักษา ซึ่ง LLM จะจัดการเรื่องนั้น"

## แนวปฏิบัติที่สำคัญ

- ใช้ Obsidian เป็น IDE สำหรับงานด้านความรู้; โดยให้ LLM เขียนด้านหนึ่ง และเปิด graph view ของ Obsidian ไว้อีกด้านหนึ่ง
- เก็บ schema ไว้ใน `AGENTS.md` (ในที่นี้เราใช้ `CLAUDE.md`)
- ชอบโครงสร้าง directory ที่เรียบง่ายและแบน มากกว่า tooling ที่ซับซ้อน
- มีส่วนร่วมในช่วง ingest แรกๆ และลดการมีส่วนร่วมลงเมื่อ LLM เรียนรู้รูปแบบแล้ว
- "Vibe-codes" เครื่องมือที่สร้างขึ้นเอง (เช่น search engines, data processing) ตามความต้องการที่เกิดขึ้น
- Wiki งานวิจัยของเขา: มีบทความประมาณ 100 บทความ, ราว 400K คำ ในหัวข้อวิจัย ML เพียงหัวข้อเดียว

## ดูเพิ่ม

- [[karpathy-llm-knowledge-bases]]
- [[karpathy-llm-wiki-idea-file]]
- [[karpathy-guidelines]]
- [[llm-knowledge-bases]]
- [[llm-coding-pitfalls]]
- [[idea-file]]
- [[memex]]
