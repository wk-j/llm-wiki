---
title: Claude Mythos Preview
type: entity
tags: [ai, models, anthropic, claude, mythos, cybersecurity]
created: 2026-04-22
updated: 2026-04-23
sources: [Claude Mythos Preview.md]
---

# Claude Mythos Preview

ตระกูลโมเดลรุ่นพรีวิว (frontier-preview) ของ [[anthropic|Anthropic]] ซึ่งประกาศเปิดตัวครั้งแรกพร้อมกับ [[project-glasswing|Project Glasswing]] เป็นโมเดลที่มีความสามารถโดยรวมสูงสุดของ Anthropic แต่**ไม่ได้เปิดให้ใช้งานเป็นการทั่วไปอย่างจงใจ** เนื่องจากมีความสามารถด้านความปลอดภัยทางไซเบอร์ที่สูงมาก

## เหตุผลที่จำกัดการเข้าถึง

Mythos Preview สามารถค้นหาและใช้ประโยชน์จากช่องโหว่ zero-day ในระบบปฏิบัติการและเบราว์เซอร์หลักๆ ทุกตัวได้โดยอัตโนมัติ [[anthropic|Anthropic]] ตัดสินว่าช่วงเปลี่ยนผ่าน—ก่อนที่ระบบนิเวศด้านความปลอดภัยจะเข้าสู่สมดุลใหม่ด้วยการป้องกันที่ใช้ ML ช่วย—มีความเสี่ยงเกินไปที่จะเปิดตัวในวงกว้าง การเข้าถึงจึงทำผ่าน [[project-glasswing|Project Glasswing]] สำหรับพาร์ทเนอร์ที่สำคัญในอุตสาหกรรมและนักพัฒนาโอเพนซอร์สที่ผ่านการตรวจสอบแล้วเท่านั้น

## โปรไฟล์ความสามารถ

| ความสามารถ | รายละเอียด |
|---|---|
| **การค้นหา Zero-day** | ทำงานอัตโนมัติครอบคลุม OS kernels, เบราว์เซอร์, crypto libs, เว็บแอป, VMMs |
| **การพัฒนา Exploit** | ทำงานอัตโนมัติทั้งหมด: ROP chains, JIT heap sprays, KASLR bypass, sandbox escapes |
| **การเชื่อมโยงช่องโหว่ (Vuln chaining)** | เชื่อมโยงช่องโหว่อิสระ 2–4 ตัวเพื่อสร้าง exploit เพียงตัวเดียว (เช่น read primitive + UAF + heap spray → root) |
| **วิศวกรรมย้อนกลับ (Reverse engineering)** | สร้างซอร์สโค้ดขึ้นมาใหม่จาก binary ที่ถูก stripped แล้วค้นหาช่องโหว่ในซอร์สโค้ดต้นฉบับที่เป็น closed-source |
| **การใช้ประโยชน์จาก N-day** | เมื่อได้รับ CVE + git hash จะเขียน exploit ที่ใช้งานได้โดยอัตโนมัติในเวลาไม่กี่ชั่วโมง ด้วยต้นทุน <$1000 |

## ไฮไลท์จาก Benchmark (เทียบกับ Opus 4.6)

- **Exploits ใน JS engine ของ Firefox 147**: Opus 4.6 → สำเร็จ 2/200+ ครั้ง; Mythos Preview → สำเร็จ 181/200+ ครั้ง (พร้อม register controls อีก 29 ครั้ง)
- **OSS-Fuzz tier-5 (control flow hijack)**: Opus 4.6 → 0; Mythos Preview → 10 บนเป้าหมายที่แพตช์สมบูรณ์แล้ว
- **OSS-Fuzz tier 1–2 crashes**: Opus 4.6 → 150–175; Mythos Preview → 595

## ความสามารถด้านไซเบอร์เกิดขึ้นได้อย่างไร

ไม่ได้มาจากการฝึกด้านความปลอดภัยโดยตรง แต่เป็นความสามารถที่เกิดขึ้นเองซึ่งเป็นผลพลอยได้จากการปรับปรุงความสามารถทั่วไปในด้านโค้ด, การให้เหตุผล, และความเป็นอิสระ (autonomy) การปรับปรุงที่ทำให้ Mythos Preview *แก้ไข*ช่องโหว่ได้ดีขึ้น ก็ทำให้มัน*ใช้ประโยชน์*จากช่องโหว่ได้ดีขึ้นเช่นกัน

## การค้นพบที่น่าสนใจ

- ช่องโหว่ OpenBSD SACK NULL-pointer deref (DoS) ที่มีอายุ 27 ปี
- ช่องโหว่ FFmpeg H.264 sentinel collision (OOB write) ที่มีอายุ 16 ปี
- ช่องโหว่ FreeBSD NFS RCE → root (CVE-2026-4747) ที่มีอายุ 17 ปี
- Guest-to-host memory corruption ใน VMM ที่เป็น memory-safe (ยังไม่ถูกแพตช์)
- การทำ privilege escalation chain ใน Linux kernel หลายครั้ง (เชื่อม 2–4 ช่องโหว่)
- Browser JIT heap sprays + sandbox escapes (ในเบราว์เซอร์หลักทุกตัว, ยังไม่ถูกแพตช์)
- จุดอ่อนในไลบรารี Crypto (TLS, AES-GCM, SSH; รวมถึงการ bypass certificate ของ Botan)
- อีกหลายพันรายการอยู่ระหว่างกระบวนการเปิดเผยข้อมูลอย่างมีการประสานงาน

## ต้นทุนในการค้นพบ

- OpenBSD bug: <$50 สำหรับการรันที่สำเร็จ, <$20K สำหรับการรัน scaffold ทั้งหมด 1000 ครั้ง
- N-day exploits: <$1000 ต่อรายการ, ใช้เวลา <1 วัน
- โดยรวม: "ไม่ถึงหนึ่งวัน" สำหรับการสร้าง exploit ที่ซับซ้อนที่สุด

## ความสัมพันธ์กับ Opus 4.7

- Opus 4.7 เป็น **flagship ที่เปิดให้ใช้ทั่วไป** (เปิดตัว 16 เม.ย. 2026); ความสามารถด้านไซเบอร์ถูกลดทอนลงระหว่างการฝึก + มีการเพิ่มระบบป้องกันอัตโนมัติเข้าไป
- Mythos Preview อยู่ในระดับที่**สูงกว่า** Opus 4.7 ในแง่ของความสามารถดิบ แต่ต่ำกว่าในแง่ของความปลอดภัย
- [[anthropic|Anthropic]] วางแผนที่จะเปิดตัวระบบป้องกันใหม่พร้อมกับ "Claude Opus model ที่กำลังจะมาถึง" ก่อนที่จะเปิดให้ใช้โมเดลระดับ Mythos-class ในวงกว้างขึ้น
- มี **Cyber Verification Program** สำหรับผู้เชี่ยวชาญด้านความปลอดภัยที่ต้องการใช้ความสามารถด้านไซเบอร์เต็มรูปแบบ

## ดูเพิ่ม

- [[anthropic]]
- [[claude]]
- [[claude-opus-4-7]]
- [[project-glasswing]]
- [[model-cyber-capability-emergence]]
