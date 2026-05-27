---
title: oh-my-pi
type: entity
tags: [product, tool, agents, open-source, harness]
created: 2026-05-27
updated: 2026-05-27
sources: [improved-15-llms-harness-changed.md]
---

# oh-my-pi

**oh-my-pi** เป็น open-source coding agent harness ที่ [[can-boluk|Can Bölük]] fork จาก [[pi-agent|pi]] ([pi-mono](https://github.com/badlogic/pi-mono) โดย [[mario-zechner|Mario Zechner]]) ออกแบบให้ **model-agnostic** — ตัว model เป็นแค่พารามิเตอร์ ส่วน harness เป็นที่ที่ทดลองและคุมได้เต็มมือ

Repo: [github.com/can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)

## จุดที่ Can ปรับเป็นพิเศษ

- **Subagent output** — แทนที่จะปล่อย raw JSONL leak เข้า parent context แบบ [[claude-code|Claude Code]] (กิน token มหาศาล) ให้ subagent ส่ง structured data กลับมาแทน
- **[[hashline|Hashline]] edit tool** — บรรทัดที่ read/grep ทุกบรรทัดติด tag `line:hash|` มาด้วย; edit อ้าง tag แทนการ reproduce whitespace
- **react-edit-benchmark** — benchmark แก้ bug ในไฟล์ React; 16 model, Patch vs Replace vs Hashline; รายงานต่อ run อยู่ใน `packages/react-edit-benchmark`

## ความสัมพันธ์กับ pi

oh-my-pi รับปรัชญา pi มาเต็ม ๆ — core เล็ก, โปร่งใส, ปรับได้ — แต่ Can ใช้เป็น **สนามทดลอง harness** มากกว่าจะเป็น distribution หลักของ pi ดู [[pi-agent]] และ [[building-pi-world-of-slop]]

## See also

- [[can-boluk]]
- [[improved-15-llms-harness-changed]]
- [[hashline]]
- [[edit-tool-formats]]
- [[pi-agent]]
- [[coding-harness]]
