---
title: Typesafe AI
type: entity
tags: [ai, company, classification, inference, reinforcement-learning]
created: 2026-09-19
updated: 2026-09-19
sources: [jev-the-ultimate-classification-model.md]
---

# Typesafe AI

Typesafe AI คือบริษัทผู้สร้าง [[jev|Jev]] ตามวิดีโอของ [[sam-witteveen|Sam Witteveen]] บริษัทออกจาก stealth พร้อมเสนอ model ที่เน้นคำตัดสินเร็วและ typed output แทนการ chat

Sam ระบุว่าผู้ก่อตั้งคือ Diogo Almeida อดีตนักวิจัย OpenAI และผู้เขียนลำดับต้นของ paper InstructGPT ทีมใช้เวลาสองปีพัฒนา Jev ใน stealth ข้อมูลทั้งหมดในหน้านี้มาจากวิดีโอที่ได้รับมา ยังไม่ได้ตรวจกับประวัติบริษัทหรือ paper ต้นทาง

## แนวทางของบริษัท

Typesafe AI ใช้คำว่า [[system-one-models|System One Models]] กับ model ที่รับ `state` และ typed questions แล้วคืนค่าให้ software ใช้ต่อได้ทันที แนวทางนี้ตั้งต้นจากโจทย์ว่า software มักต้องการ class, score หรือ boolean probability มากกว่าย่อหน้าจาก chatbot

บริษัทระบุองค์ประกอบสามอย่างผ่านสื่อที่ Sam นำมาเล่า:

- model architecture แบบใหม่
- parallel sampler
- RLCD หรือ Reinforcement Learning for Calibrated Decisions

แหล่งนี้ไม่มี paper, architecture diagram หรือรายละเอียด RLCD จึงยังบอกไม่ได้ว่าต่างจาก transformer classifier เดิมตรงไหน และยังไม่มีหลักฐานพอจะยืนยันว่า probability calibrated ดีเพียงใด

## See also

- [[jev]]
- [[system-one-models]]
- [[jev-the-ultimate-classification-model]]
- [[sam-witteveen]]
