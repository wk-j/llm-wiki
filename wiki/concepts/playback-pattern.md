---
title: Playback Pattern
type: concept
tags: [agent-design, alignment, communication]
created: 2026-04-29
updated: 2026-04-29
sources: [compound-engineering-v3-3-0.md]
---

# Playback Pattern / รูปแบบการทวนความเข้าใจ

Playback Pattern เป็นเทคนิคการสื่อสารระหว่าง AI agent และมนุษย์ เพื่อตรวจสอบความเข้าใจให้ตรงกันก่อนที่ agent จะเริ่มลงมือทำงานที่ซับซ้อนหรือใช้เวลานาน เทคนิคนี้ถูกนำมาใช้อย่างชัดเจนใน [[compound-engineering]] v3.3.0 โดย [[trevin]]

## แก่นความคิด

ปัญหาที่พบบ่อยใน AI agent คือการที่ agent รับคำสั่งแล้วรีบไปทำงานทันทีโดยมีสมมติฐานที่ผิด (incorrect assumptions) พองานเสร็จออกมา (ซึ่งอาจใช้เวลาหลายนาที) ผลลัพธ์กลับไม่ใช่สิ่งที่ผู้ใช้ต้องการ การแก้ไขในภายหลังจึงทำได้ยากและเสียเวลา

**Playback Pattern แก้ปัญหานี้ด้วยการ "ทวนความ" (playback) สิ่งที่เข้าใจออกมาเป็น 3 ส่วนหลัก:**

1.  **Stated (สิ่งที่ระบุชัด):** สรุปสิ่งที่ผู้ใช้สั่งโดยตรง (User's literal prompt)
2.  **Inferred (สิ่งที่คาดเดาเพิ่ม):** สมมติฐานที่ agent คิดเอาเองว่าผู้ใช้น่าจะต้องการ หรือสิ่งที่ต้องทำเพื่อให้งานสำเร็จแต่ไม่ได้ถูกระบุไว้ (Contextual assumptions)
3.  **Out-of-scope (สิ่งที่อยู่นอกขอบเขต):** สิ่งที่ agent จะไม่แตะต้อง หรือสิ่งที่จงใจเว้นไว้เพื่อไม่ให้ขอบเขตงานบานปลาย (Deliberate exclusions)

## ตัวอย่างการใช้งาน

เมื่อสั่งให้ agent "เพิ่มระบบ OAuth login ในแอปมือถือ"

*   **Stated:** เพิ่มปุ่ม login ด้วย OAuth
*   **Inferred:** จะใช้ Google และ GitHub เป็น provider, ต้องเขียน callback handler, และแก้ไข schema ตาราง User
*   **Out-of-scope:** จะไม่ยุ่งกับระบบ Email login เดิม และยังไม่ทำ Two-factor authentication (2FA) ในรอบนี้

## ประโยชน์ที่ได้รับ (The Payoff)

- **Cheaper to correct:** การแก้ bullet point ที่เข้าใจผิดในหน้า chat นั้น "ราคาถูก" กว่าการต้องมารื้อโค้ดที่ agent เขียนเสร็จไปแล้ว 10 นาทีมาก
- **Faster to trust:** เมื่อผู้ใช้เห็นว่า agent เข้าใจบริบท (Inferred) และขอบเขต (Out-of-scope) ได้ถูกต้อง ความไว้ใจในการปล่อยให้ agent ทำงานยาว ๆ ก็จะเพิ่มขึ้น
- **Reduced Hallucination:** การบังคับให้ agent ต้องแจกแจงสิ่งที่เข้าใจออกมา ช่วยลดการ "มโน" ไปเองเงียบ ๆ

## See also

- [[compound-engineering]]
- [[alignment-bottleneck]]
- [[graduated-autonomy]]
