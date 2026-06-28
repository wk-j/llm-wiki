---
title: Dreaming
type: concept
tags: [agent-memory, anthropic, multi-agent, batch-process, self-learning]
created: 2026-05-09
updated: 2026-06-26
sources: [memory-and-dreaming-self-learning-agents, Self Learning for Agents Clearly Explained.md]
---

# Dreaming / การฝัน (กระบวนการจัด memory นอก session)

**Dreaming** คือ batch process ที่ [[anthropic|Anthropic]] เปิด research preview ใน [[claude-managed-agents|Claude Managed Agents API]] วันที่ 2026-05-09 หน้าที่ของมันคืออ่าน transcript ของ agent หลายตัวจากช่วงที่ผ่านมา แล้วอัปเดต **memory store** ให้สด — ทำงาน **นอก hot path** ของ agent ตัวจริง ไม่เพิ่ม latency

ชื่อ "dreaming" สื่อถึงการที่มนุษย์นอนหลับแล้วสมอง consolidate ความจำ — ระหว่างที่ agent "ตื่น" ทำงาน memory ก็ถูก dreaming "ฝัน" ทบทวนในเบื้องหลัง

## ทำไมถึงต้องมี

[[agent-memory-filesystem|Memory แบบ file system]] ที่ Claude อ่าน/เขียนเองในเซสชัน ไปได้ถึงระดับหนึ่ง แต่พอมี agent หลายตัว (multi-agent swarm) มาแชร์ memory เดียวกัน เริ่มเจอปัญหา 3 ข้อ:

1. agent ตัวใหม่ไม่เห็นสิ่งที่ตัวอื่นเรียนรู้ไปแล้ว
2. agent หลายตัวทำผิดเหมือนๆ กันโดยไม่รู้ว่าเป็น pattern (ต่างคนต่างมุม)
3. memory store ใหญ่ขึ้นเรื่อยๆ ไม่มีใคร curate

agent เดี่ยวมองจาก context ตัวเอง — เห็นไม่หมด

## กลไก

Dreaming เป็น **batch async** Trigger ได้ 2 รูปแบบ:

- **Cron** — ตั้งให้รันเป็นรอบในคอนโซล/API
- **Event** — เช่น agent finish task แล้วก่อน spin down ก็เรียก dreaming เพื่อ commit สิ่งที่เรียนรู้

ขั้นตอนภายใน:

1. รับ memory store + ช่วงเวลา (เช่น 7 วันย้อนหลัง)
2. ดึง transcript ของ session ทั้งหมดที่แตะ memory store นั้น
3. spawn sub-agent หลายตัวอ่าน transcript หา pattern, mistake, strategy ที่ใช้ได้
4. ผลิต **diff** บน memory store
5. apply ทันที หรือให้คน review ผ่าน API ก่อนก็ได้

ประเภทการเปลี่ยน memory ที่ dreaming ทำ:
- **Pattern discovery** — เห็น pattern ข้าม agent เช่น "alert ลั่นทุก 60 วินาทีหลัง CPU spike" สรุปว่ามี retry logic ผิด
- **Deduplication** — รวม entry ซ้ำ
- **Pruning** — ลบ entry ที่ stale
- **Verification** — ติด tag ว่า entry นี้ verified ณ เวลาไหน ให้ agent วันถัดไปไว้ใจได้

## ทำไมต้องเป็น process แยก ไม่ให้ agent ทำเอง

Mahes ([[anthropic|Anthropic]] PM) ให้เหตุผล 4 ข้อ:

1. **Out of band** — ไม่อยู่ใน hot path ของ task ใดๆ ไม่เพิ่ม latency
2. **Cross-agent perspective** — agent เดี่ยวเห็นแค่มุมตัวเอง dreaming อ่าน transcript หลายตัวพร้อมกันได้
3. **Discrete objective** — agent ทำงานดีที่สุดเมื่อ objective ชัด แยก "memory quality" ออกจาก "task completion" — ไม่ให้สอง objective กลืนกัน
4. **Scale ผ่าน compute** — เหมือน test-time compute ของ thinking model: ใส่ token จัด memory ครั้งเดียวล่วงหน้า amortize ค่าจัดข้าม agent ปลายน้ำทุกตัวที่อ่าน

อีก analogy ที่ใช้อธิบาย: dreaming = **search index pipeline** ที่ปั่น index ไว้ล่วงหน้า ทำให้ retrieval ตอน serve ราคาถูก

## ผลลัพธ์เบื้องต้น

ลูกค้า early access ที่ Anthropic ยกตัวอย่าง:

- **[[harvey-ai|Harvey]]** (legal AI) — เปิด dreaming ใน legal benchmark ของตัวเอง task completion rate ของ scenario หนึ่งเพิ่มขึ้น **6 เท่า**

## ตำแหน่งใน Frontier Memory System

| | [[agent-memory-filesystem\|Memory API]] | Dreaming |
|---|---|---|
| โหมด | real-time, in-session | batch, out-of-band |
| มุมมอง | per-agent | cross-agent |
| เป้าหมาย | task completion | memory quality |
| Trigger | inline tool call | cron / event |
| ผลลัพธ์ | อ่าน/เขียนทันที | diff บน memory store |

Memory คือ primitive ระดับล่าง ส่วน dreaming เป็นชั้น **process** ที่ครอบบนอีกที — Mahes ใช้คำว่า dreaming คือ "สะพาน" ระหว่าง memory ระดับ session กับ knowledge base ขนาดใหญ่ระดับองค์กร

## เปรียบเทียบกับแนวทางอื่น

- **[[mercury|Mercury]]** ของ [[ctrl-alt-zaid]] เน้น [[hybrid-memory|Hybrid Architecture]] ที่แยก machine substrate กับ Markdown ของมนุษย์ — ไม่มี process แยกแบบ dreaming ระบุชัด แต่ใช้ [[memory-scoring]] + [[memory-decay]] ให้ memory ค่อยๆ ตกตะกอน
- **[[compaction]]** ใน [[claude-code|Claude Code]] เป็นการสรุป context ใน session เดียว ไม่ใช่ข้าม session/agent

ความต่างคือ dreaming ทำ **คน-ละ session** กับ agent ที่ทำงานจริง และมองข้าม session

## dreaming ในแผนที่ self-learning ที่ใหญ่กว่า

[[self-learning-for-agents-explained]] วาง dreaming ลงในกลุ่ม **"เขียน memory ใหม่เบื้องหลัง"** (Context Approach #1 ของชั้น Context ใน [[three-learning-layers]]) — ที่ที่ idea เดียวกันโผล่หลายเจ้า:

- **[[letta|Letta]]** — ตรึง weight เรียนใน plain text; agent ที่คุยกับ user แก้ core memory ตัวเองไม่ได้ มี agent แยกเขียนใหม่ตอน idle (เรียก *sleep-time compute*)
- **OpenClaw** — รันไอเดียเดียวกันเป็น **nightly dreaming pass** บนไฟล์ memory (ใช้คำว่า "dreaming" ตรง ๆ เหมือนกัน)
- **[[anthropic|Anthropic]] dreaming** (หน้านี้) — เวอร์ชันที่เด่นเรื่อง **cross-agent**: อ่าน transcript หลาย agent พร้อมกัน ไม่ใช่แค่ memory ของ agent เดียว

แก่นร่วมที่ thread สรุปได้คม: **weight ชั่วคราว แต่ text อยู่ถาวร** — memory ที่ dreaming จัดเป็น text จึงย้ายข้าม model ได้และ roll back ได้ ต่างจาก fine-tune ที่ฝังความรู้ลง weight

## See also

- [[agent-memory-filesystem]]
- [[claude-managed-agents]]
- [[self-learning-agents]]
- [[memory-and-dreaming-self-learning-agents]]
- [[memory-decay]]
- [[memory-drift]]
- [[hybrid-memory]]
- [[harvey-ai]]
- [[three-learning-layers]]
- [[self-learning-for-agents-explained]]
- [[letta]]
- [[agent-memory-types]]
