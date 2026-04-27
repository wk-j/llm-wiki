---
title: OpenAI
type: entity
tags: [ai, labs, models, organizations]
created: 2026-04-24
updated: 2026-04-28
sources: [piyalitt-gpt-5-5-launch.md, microsoft-openai-partnership-2026.md, ryan-lopopolo-harness-engineering.md]
---

# OpenAI / โอเพนเอไอ

AI lab ในสหรัฐฯ — สร้าง ChatGPT, ตระกูล GPT, และ [[openai-codex|Codex]] เป็น lab คู่แข่งหลักของ [[anthropic|Anthropic]] และ [[moonshot-ai|Moonshot AI]] ในการแข่งขัน frontier model ช่วงปี 2026

## วัฒนธรรมและแนวทางการพัฒนาภายใน

จากข้อมูลของ [[ryan-lopopolo]] (2026) ทีมวิศวกรภายใน OpenAI ได้เปลี่ยนผ่านไปสู่การทำงานแบบ Agent-exclusively:
- **[[harness-engineering|Harness Engineering]]**: การสร้างระบบควบคุมคุณภาพอัตโนมัติรอบตัว Agent แทนการเขียนโค้ดเอง
- **[[code-is-free|Code is Free]]**: แนวคิดว่าโค้ดไม่มีต้นทุนการผลิต เน้นการผลิตและ refactor ในสเกลใหญ่
- **[[token-billionaire|Token Billionaire]]**: การใช้ output tokens ในระดับพันล้านต่อวันเพื่อผลักดันขีดจำกัดของ Agentic workflow

## บุคลากรสำคัญใน wiki

- [[ryan-lopopolo]] — Member of Technical Staff (Harness Engineering advocate)

## จุดเปลี่ยนความสัมพันธ์กับ Microsoft (เม.ย. 2026)

จากประกาศเมื่อ 2026-04-27 (ดู [[microsoft-openai-partnership-2026]]) OpenAI ได้ขยับจากความสัมพันธ์แบบผูกขาด (exclusive) กับ [[microsoft]] ไปสู่โครงสร้างแบบ "Open Relationship":

- **อิสระในการใช้ Cloud**: OpenAI สามารถนำ model ไปรันและขายบน cloud เจ้าอื่นได้แล้ว (เช่น Google Cloud, AWS) ไม่ได้จำกัดอยู่แค่ Azure
- **Infrastructure Diversification**: มีการดึง partner รายอื่นเข้ามาช่วยเรื่อง compute เพิ่มเติม เช่น Oracle และ SoftBank เพื่อให้รองรับ scale ของโมเดลระดับ frontier ได้ทัน
- **Restructuring**: การปรับความสัมพันธ์นี้สอดคล้องกับการปรับโครงสร้างองค์กร (ปลายปี 2025) ที่พยายามลดข้อจำกัดเรื่อง profit caps เพื่อดึงดูดนักลงทุนในรูปแบบบริษัทมหาชนมากขึ้น

## โมเดลที่อยู่ใน wiki

| โมเดล | ตำแหน่ง | หมายเหตุ |
|---|---|---|
| **[[gpt-5-5]]** | Flagship (เปิดตัว 2026-04-23) | Agentic coding + knowledge work SOTA; 2× ราคา GPT-5.4 |
| GPT-5.5 Pro | Flagship Pro | API $30/$180 per 1M tokens; สำหรับงานที่ต้องการคุณภาพสูงสุด |
| GPT-5.4 | รุ่นก่อน | ยังเป็น baseline สำหรับเปรียบเทียบหลายตัว |

## Surfaces

- **ChatGPT** — consumer/enterprise surface
- **[[openai-codex|Codex]]** — coding harness (CLI + IDE + web); เทียบได้กับ [[claude-code]] ในฝั่ง Anthropic
- **API** — Responses API + Chat Completions API; batch/flex/priority tiers
- **gpt-image-2** — image generation (อ้างโดย Piyalitt ว่าช่วยให้ GPT-5.5 ทำ design system ได้ดีขึ้น)

## การแข่งขันกับ Anthropic (เม.ย. 2026)

จาก [[piyalitt-gpt-5-5-launch]]: **pricing inversion** เกิดขึ้นที่ rung flagship — GPT-5.5 ($5/$30) แพงกว่า [[claude-opus-4-7|Opus 4.7]] ($5/$25) เล็กน้อย ทั้งที่ GPT รุ่นก่อนๆ มักถูกกว่า Opus ประมาณครึ่งหนึ่ง — signal ว่า OpenAI ใช้ compute มากจริงเพื่อให้ทัน [[claude-mythos-preview|Mythos-class]] capability ในตลาด mass

## ประเด็น benchmark

- **SWE-Bench Pro memorization signal** — Anthropic ฟ้องไว้ใน model card ของ GPT-5.5 ว่ามี sign ของการจำ; [[piyalitt-ittichaiwong|Piyalitt]] ตีความว่าเป็นความพลาด ไม่ใช่การ benchmaxx ตั้งใจ — เป็นอีกเคสที่ทำให้ SWE-Bench Pro โดยเดี่ยวๆ เป็น axis ที่ควรระวัง (ดู [[kimi-k2-6]] ด้วย — benchmark table ถูก curate)

## Community presence

- **OpenAI Codex Community** ในไทยโปรโมทโดย [[piyalitt-ittichaiwong|Piyalitt]]
- **Hackathon OpenAI × สมาคมปัญญาประดิษฐ์ประเทศไทย** (2026-04-25, credit รวมเป็นล้าน)

## ดูเพิ่ม

- [[gpt-5-5]]
- [[openai-codex]]
- [[anthropic]]
- [[claude-opus-4-7]]
