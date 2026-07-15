---
title: Frontier AI Standards Body
type: concept
tags: [ai, governance, standards, safety, evaluation, policy]
created: 2026-07-15
updated: 2026-07-15
sources: [framework-frontier-ai-dawning-new-age.md]
---

# Frontier AI Standards Body / หน่วยมาตรฐานสำหรับ Frontier AI

Frontier AI Standards Body คือสถาบันกำกับ model แนวหน้าที่ [[demis-hassabis|Demis Hassabis]] เสนอใน [[framework-frontier-ai-dawning-new-age|A Framework for Frontier AI and the Dawning of a New Age]]. หน่วยนี้ **ยังเป็นข้อเสนอ** ไม่ใช่องค์กรที่ตั้งแล้ว

แกนคือกำกับตาม capability และ risk ไม่ใช่กำกับ AI ทุกตัวเหมือนกัน Model ที่ผ่าน threshold จะเป็น `Frontier-class`; องค์กรเจ้าของ model นั้นเป็น `Frontier Lab`. Model เล็กจาก startup/academia ที่ยังไม่ถึง threshold ได้รับการยกเว้น

## โครงสร้างสถาบัน

Hassabis เสนอให้สหรัฐฯ เริ่มก่อนในรูป federally overseen public-private partnership หรือ self-regulatory organisation คล้าย FINRA. Board ควรมีผู้เชี่ยวชาญเทคนิคอิสระกับตัวแทน open source. เงินทุนส่วนใหญ่น่าจะมาจากอุตสาหกรรม เพราะงานต้องใช้ทั้งคนเก่งและ compute สูง

หน่วยนี้ทำ protocol ร่วมกับหน่วยงานรัฐบาลและ US National Labs โดยเฉพาะการทดสอบที่แตะ national security. ระยะยาวต้องสร้างความสามารถทดสอบเอง ไม่พึ่ง Lab ที่ถูกตรวจ

**ได้อะไร:** เป้าหมายคือสร้างผู้ตรวจที่เข้าใจ model ลึกพอและมีทรัพยากรเทียบกับผู้สร้าง ไม่ใช่ regulator ที่อ่านแค่เอกสาร

## เส้นทางกำกับ

| ระยะ | สิ่งที่เกิดขึ้น |
|---|---|
| 1. Define | ตั้ง benchmark/threshold ว่าอะไรคือ Frontier-class |
| 2. Voluntary review | Frontier Lab ส่ง model ให้ตรวจล่วงหน้าสูงสุด 30 วัน |
| 3. Validate protocol | ดูว่า test จับ capability/risk ได้จริงและไม่ถูกเล่นเกมง่าย |
| 4. Formalise | บังคับ Frontier Model ผ่าน gate ก่อน deploy ในตลาดสหรัฐฯ |
| 5. Post-release | Lab กับ Standards Body แก้ critical vulnerability ที่พบหลังปล่อย |
| 6. Ratchet | เพิ่มความเข้ม หรือประสาน slowdown ถ้า risk ร้ายแรงขึ้น |

ความแข็งของกรอบนี้คือเพิ่มระดับได้ตามหลักฐาน. จุดที่ยังขาดคือ legal authority, due process, appeal, liability และนิยามว่าใครกดปุ่ม slowdown ได้

## สิ่งที่ Frontier Lab ควรทำ

- เผยแพร่ model card พร้อมรายละเอียดเทคนิค
- รักษา internal cybersecurity ให้แข็ง
- vet บุคลากรสำคัญ
- ลงทุน safety/security research ให้พอ
- ส่ง model เข้ารับการประเมินก่อนปล่อย
- ร่วมแก้ critical vulnerability หลัง release

Hassabis ต้องการให้สถานะ Frontier Lab มี prestige. วิธีนี้พยายามเปลี่ยน compliance จากต้นทุนล้วนให้เป็นสัญญาณว่าองค์กรรับผิดชอบและมี capability สูงจริง

## Evaluation ที่ต้องหมุนตลอด

การทดสอบควรครอบคลุม cyber, biological threats และ high-risk domain อื่น. Agentic test ควรหา guardrail bypass กับ deception. ผู้เขียนยังยก watermark สำหรับภาพ AI และ human-readable output token เพื่อช่วยตรวจ reasoning

benchmark อาจ refresh ทุกไตรมาส ชุดที่อิ่มตัวต้องเลิกใช้. ช่วงแรก Lab ช่วยออกแบบได้ แต่สุดท้าย Standards Body ต้องมี held-out test ของตัวเอง และส่งเสริม third-party auditor เพื่อกัน overfitting, [[benchmark-contamination|contamination]] และ [[reward-hacking|reward hacking]].

**ผลคือ:** evaluation เป็นระบบมี lifecycle ไม่ใช่ leaderboard ชุดเดียวที่ใช้ตลอดไป

## Open, closed และขอบเขตตลาด

กรอบนี้ใช้กับ Frontier-class model จากทุกประเทศและทั้ง open/closed. ข้อดีคือไม่เปิดช่องให้เลี่ยงกติกาด้วย license หรือประเทศต้นทาง. แต่ enforcement ต่างกันมาก: closed API มีเจ้าของคุม deployment; open-weight model ถูก copy, fine-tune และรันนอกเขตอำนาจได้

การยกเว้น non-frontier model ช่วย startup และ academia แต่ threshold อาจสร้าง cliff: พอ model ข้ามเส้น compliance cost กระโดดขึ้นทันที. วิธีวัด capability จึงมีผลต่อการแข่งขันและการเปิดเผย model โดยตรง

## ความตึงที่ต้องเก็บไว้

- **Expertise vs capture:** รับเงินอุตสาหกรรมช่วยให้มีคน/compute พอ แต่ผู้ถูกกำกับอาจมีอิทธิพลเหนือผู้กำกับ
- **Dynamic tests vs predictability:** หมุน test กัน overfit แต่ Lab ต้องรู้กติกาพอจะวางแผน release และอุทธรณ์ได้
- **Prestige vs gatekeeping:** สถานะ Frontier Lab สร้างแรงจูงใจ แต่ก็อาจรวมอำนาจไว้กับองค์กรใหญ่
- **Open access vs enforceability:** ใช้เกณฑ์เดียวกับ open/closed ดูเท่าเทียม แต่ความสามารถบังคับใช้ไม่เท่ากัน
- **National start vs global risk:** สหรัฐฯ เริ่มได้เร็ว แต่ model และผลกระทบข้ามพรมแดน
- **Visible reasoning vs faithful reasoning:** output ที่อ่านได้อาจช่วย audit แต่ยังต้องพิสูจน์ว่าตรงกับเหตุผลภายในจริง

## Open questions

- ใครเลือก board และถอดสมาชิกที่มี conflict of interest อย่างไร
- threshold วัด capability, compute, deployment scale หรือผลกระทบรวมกัน
- test ลับแค่ไหนจึงกัน overfitได้โดยยังตรวจสอบความชอบธรรมได้
- จะรับรอง third-party auditor และ audit ตัว Standards Body เองอย่างไร
- open-weight model ต้องผ่าน gate ตอน release weights, ตอน deploy หรือทั้งสองจุด
- ตลาดสหรัฐฯ จะบังคับ model จากต่างประเทศอย่างไรโดยไม่ผลัก deployment ไปใต้ดิน
- slowdown ใช้เกณฑ์อะไร ใครเข้าร่วม และมีวิธีตรวจการปฏิบัติตามอย่างไร

## See also

- [[framework-frontier-ai-dawning-new-age]]
- [[demis-hassabis]]
- [[artificial-general-intelligence]]
- [[benchmark-contamination]]
- [[reward-hacking]]
- [[open-weight-models]]
- [[model-cyber-capability-emergence]]
- [[agent-runtime-untrusted]]
- [[graduated-autonomy]]
