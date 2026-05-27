---
title: Edit Tool Formats
type: concept
tags: [ai, harness, coding, tools, benchmarks]
created: 2026-05-27
updated: 2026-05-27
sources: [improved-15-llms-harness-changed.md]
---

# Edit Tool Formats / รูปแบบเครื่องมือแก้ไฟล์

เวลา coding agent จะแก้ไฟล์ **รูปแบบที่ harness บังคับให้ model ใช้ส่ง edit** มีผลต่อ success rate พอ ๆ กับความฉลาดของ model — ไม่ใช่แค่ implementation detail

[[can-boluk|Can Bölük]] กับ benchmark ภายนอก (Diff-XYZ, EDIT-Bench, Aider) ชี้ตรงกันว่า failure หลายครั้งเกิดที่ **tool boundary**: model รู้ว่าจะแก้อะไร แต่ส่ง edit ออกมาในรูปที่ harness parse/apply ไม่ได้

## แนวหลักในตลาด

### apply_patch (OpenAI-style diff string)

- ใช้ใน [[openai-codex|Codex]] — input เป็น string ที่ต้องเขียนตาม diff format ของ OpenAI
- น่าจะถูก bias ที่ gateway ให้ Codex variants (คล้าย JSON schema / required tool)
- model อื่นที่ไม่คุ้น format จะล้มเยอะมาก (เช่น Grok 4 ~50.7%, GLM-4.7 ~46.2% ใน benchmark ของ Can)

### str_replace (exact find-and-replace)

- ใช้ใน [[claude-code|Claude Code]] กับ harness ส่วนใหญ่ — หา old string **ตรงทุกตัวอักษร** แล้วแทน
- ข้อดี: คิดง่าย เห็นภาพชัด
- ข้อเสีย: whitespace/indent พลาดนิดเดียวก็ล้ม; เจอหลาย match ก็ reject; error "String to replace not found" ดังจน community มี megathread บน GitHub
- Gemini ทำคล้ายกัน แต่อนุโลม whitespace ได้บ้าง

### Unified diff / Aider format

- Aider benchmark: format เดียวกันดัน GPT-4 Turbo จาก 26% → 59%
- GPT-3.5 ได้แค่ 19% ด้วย format เดียวกัน — **model ต้องเขียน valid diff ได้เองก่อน**

### Fine-tuned merge model

- Cursor ฝึก model ~70B แยกตัวมา merge draft edit เข้าไฟล์ ([Instant Apply blog](https://cursor.com/blog/instant-apply))
- ตัว harness ยอมรับเองว่าไฟล์ <400 บรรทัด **rewrite ทั้งไฟล์** ยังชนะ aider-like diff — แปลว่าปัญหายังไม่ "จบ"

### Hashline

- แนวของ Can ใน [[oh-my-pi]] — อ้าง `line:hash` แทนการ reproduce content; ดู [[hashline]]
- ใน benchmark 16 model: Patch แย่ที่สุดเกือบทุกตัว; Hashline ชนะหรือเสมอ Replace ส่วนใหญ่

## ปัญหาร่วม (ตาม Can)

ทุกแนวข้างบน (ยกเว้น Hashline บางส่วน) ต้องให้ model **จำ content ที่เคยเห็นแล้วพิมพ์กลับออกมา** — ไม่มี stable identifier ที่บอกว่าจะแก้บรรทัดไหนโดยไม่กิน context เพิ่ม พอ mechanical edit ล้ม ผู้ใช้ก็โทษ model

Benchmark สรุปตรงกันว่า **ไม่มี format ไหนชนะทุก model ทุก use case** (Diff-XYZ, JetBrains)

## สรุปสำหรับทีม

1. **วัดแยก** — แยก "เข้าใจงาน" กับ "ส่ง edit ผ่าน" ก่อนจะสรุปว่า model แย่
2. **เลือก format ตาม model ที่ใช้จริง** — อย่าไป copy Codex patch มาใส่ harness อื่นแล้วหวังผล
3. **ลอง anchor แบบ hash/line id** — คุ้มสุดตอน str_replace ติด retry loop
4. **อย่ารอ vendor** — open harness ปรับให้ทุก model; vendor จะปรับให้แค่ ecosystem ตัวเอง

**ได้อะไร:** ปรับแค่ edit format อาจได้ +5–14pp success และลด output token ~20% โดยไม่ต้องเทรน model ใหม่

## See also

- [[hashline]]
- [[improved-15-llms-harness-changed]]
- [[coding-harness]]
- [[llm-coding-pitfalls]]
- [[openai-codex]]
- [[claude-code]]
- [[oh-my-pi]]
