---
title: Meituan
type: entity
tags: [china, company, ai, llm, hardware]
created: 2026-07-03
updated: 2026-07-03
sources: [chinas-models-no-longer-need-western-hardware.md]
---

# Meituan / เหม่ยถวน

Meituan คือบริษัทเทคโนโลยีจีนที่คนมักรู้จักจากบริการ food delivery และ grocery delivery. ในวิดีโอ [[chinas-models-no-longer-need-western-hardware|China's Models No Longer Need Western Hardware]] บริษัทนี้ถูกยกเป็นตัวอย่างว่าองค์กรจีนที่ไม่ใช่ frontier AI lab แบบดั้งเดิมก็เริ่มสร้าง model ใหญ่ระดับ trillion-parameter ได้

## บทบาทในแหล่งนี้

แหล่งนี้บอกว่า Meituan เปิดตัว [[longcat-2-0|LongCat 2.0]] ซึ่งเป็น 1.6T-parameter [[mixture-of-experts|MoE]] model และ train บน custom AI chips โดยไม่พึ่ง NVIDIA GPUs หรือ Google TPUs.

ประเด็นสำคัญจึงไม่ใช่แค่ Meituan มี model ใหม่ แต่คือบริษัทที่ core business อยู่ใน consumer services สามารถลงทุนทำ stack AI ของตัวเองได้ลึกถึง model architecture, long-context attention, inference optimization, และ hardware/runtime.

## ทำไมสำคัญ

ถ้าคำกล่าวในคลิปถูกต้อง Meituan เป็นสัญญาณว่า AI capability ในจีนอาจกระจายออกจาก lab เฉพาะทางไปยังบริษัท internet ขนาดใหญ่ที่มีเงิน, data, infra, และแรงจูงใจทางยุทธศาสตร์

ตรงนี้ต่อจาก [[deepseek|DeepSeek]] ในอีกมุมหนึ่ง: DeepSeek ทำให้โลกเห็น efficiency-first model; Meituan ในแหล่งนี้ทำให้เห็นการเลี่ยง hardware/software stack ตะวันตก.

## See also

- [[longcat-2-0]]
- [[chinas-models-no-longer-need-western-hardware]]
- [[sputnik-moment-ai]]
- [[deepseek]]
