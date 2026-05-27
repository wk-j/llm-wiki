---
title: Can Bölük
type: entity
tags: [person, ai, harness, open-source]
created: 2026-05-27
updated: 2026-05-27
sources: [improved-15-llms-harness-changed.md]
---

# Can Bölük / คาน บอลึค

**Can Bölük** (@_can1357) เป็น engineer ที่เขียนเรื่อง harness กับ game security บทความ [[improved-15-llms-harness-changed|I Improved 15 LLMs at Coding in One Afternoon]] (ก.พ. 2026) ของเขาเสนอประเด็นหลักว่า **เวลาถก benchmark coding กันเรื่อง model วงการมักมองข้าม harness** โดยเฉพาะ edit tool ที่อยู่ตรง tool boundary

เขาดูแล [[oh-my-pi|oh-my-pi]] — fork ของ [[pi-agent|pi]] จาก [[mario-zechner|Mario Zechner]] — เป็น hobby harness แบบ model-agnostic (~1,300 commits ตอนที่เขียน) ใช้ลอง tool schema, subagent output format, และเทคนิคแบบ [[hashline|Hashline]]

## สิ่งที่ wiki หยิบมาเล่า

- **Hashline / react-edit-benchmark** — แท็กบรรทัดด้วย content hash สั้น ๆ แทนที่จะให้ model reproduce old text; วัด 16 model × 3 edit formats; โค้ดเปิดที่ GitHub `can1357/oh-my-pi`
- **มุม vendor policy** — มอง Anthropic บล็อก [[opencode|OpenCode]] และ Google ปิดบัญชี Gemini ระหว่าง benchmark ว่าเป็นสัญญาณ anti–third-party harness

## See also

- [[oh-my-pi]]
- [[improved-15-llms-harness-changed]]
- [[hashline]]
- [[mario-zechner]]
- [[coding-harness]]
