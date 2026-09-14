---
title: "cafkafk on NixOS, Omarchy, and Respect for Maintainers"
type: source
tags: [linux, nixos, nixpkgs, omarchy, open-source, governance, maintenance]
created: 2026-09-10
updated: 2026-09-10
url: https://x.com/cafkafk/status/2097574059584143577
author: "@cafkafk"
published: 2026-09-09
date_ingested: 2026-09-10
sources: []
---

# cafkafk on NixOS, Omarchy, and Respect for Maintainers / ใช้ผลงานของชุมชนก็ต้องให้เกียรติคนดูแล

โพสต์บน [[x-twitter|X]] ของ [[cafkafk|cafkafk]] โต้กลับ [[dhh|David Heinemeier Hansson (DHH)]] หลังเจ้าของโพสต์บอกว่า DHH ใช้คำดูถูกคนในชุมชน Nix และ Linux แต่ต่อมากลับวางแผนให้ [[omarchy|Omarchy]] ใช้ [[nixos|NixOS]] เป็นฐาน

ใจความไม่ได้ห้ามวิจารณ์ NixOS เจ้าของโพสต์แย้งว่าคนทำ distribution พึ่งแรงงานของ maintainer จำนวนมาก ทั้ง package, security, infrastructure, release engineering และ review ถ้าจะเอางานเหล่านั้นมาเป็นฐาน ก็ควรวิจารณ์ด้วยความเคารพ ไม่ใช่ชมเทคโนโลยีพร้อมเหยียดคนที่ทำให้เทคโนโลยีนั้นใช้ได้จริง

หน้านี้สรุปข้อความที่ผู้ใช้ส่งมา ไม่ได้มีโพสต์ต้นทางของ DHH วิดีโอในโพสต์ หรือประกาศแผนย้ายจาก Omarchy จึงแยกคำกล่าวของ cafkafk ออกจากข้อเท็จจริงที่ยืนยันได้

## จุดที่ cafkafk โต้แย้ง

cafkafk เล่าว่าเมื่อราวสองสัปดาห์ก่อน DHH เรียกคนใน Nix และ Linux ecosystem ด้วยคำว่า "Goddamn maniacs", "Clowns", "Goblins" และ "Cancer" แต่ในบทสนทนาเดียวกันกลับเรียก Nix ว่า "amazing technology" สองวันก่อนโพสต์นี้ cafkafk บอกว่าเห็นแผนจะสร้าง distribution บน NixOS

สำหรับ cafkafk ปัญหาไม่ใช่การวิจารณ์ NixOS แต่เป็นท่าทีของคนนอกที่เข้ามาล้อคนทำงาน แล้วหยิบงานของชุมชนนั้นไปเป็นฐานของโปรเจกต์ตัวเอง คำว่า “tourist” ในโพสต์จึงหมายถึงคนที่ยังรู้จักชุมชนไม่พอ แต่พูดราวกับตัดสินชุมชนทั้งก้อนได้แล้ว

**ได้อะไร:** คำชมเทคโนโลยีไม่ชดเชยการดูถูกคนดูแล เพราะตัวเทคโนโลยีอยู่ต่อได้จากงานของคนเหล่านั้น

## Distribution ไม่ได้มีแค่ชั้น config กับ installer

โพสต์ย้ำว่าสิ่งที่ Omarchy มีในตอนนี้คือชั้น configuration และ installer ที่วางบนงานหลายปีจาก Arch, Linux, Rust และในอนาคตอาจรวม NixOS กับ [[nixpkgs|Nixpkgs]] ด้วย การใช้ Claude เขียนส่วนเชื่อมไม่ได้ทำให้ package, security, infrastructure, technical knowledge, release engineering, review และ maintenance ข้างล่างหายไป

> "You are not replacing those people. You are depending on them."

ความหมายคือ agent อาจช่วยสร้างชั้นบนได้เร็วขึ้น แต่คนทำโปรเจกต์ยังพึ่งชุมชนที่ดูแลชั้นล่างอยู่ กรณีนี้จึงอ่านคู่กับ [[software-ecology|Software Ecology]] ได้ เพราะ software ไม่ได้เกิดจาก code ชิ้นเดียว มันอยู่ใน ecosystem ที่คน เครื่องมือ และงานดูแลเชื่อมกัน

**ผลคือ:** จะประเมินว่า distribution ใหม่สร้างอะไรเอง ต้องแยกชั้นที่โปรเจกต์ทำเพิ่มออกจากฐานที่รับมาจาก upstream

## Governance เป็นส่วนหนึ่งของงาน

cafkafk มองว่า DHH อยากให้เทคโนโลยี “apolitical” แต่กลับพูดเรื่อง politics, culture, code of conduct และ community governance อยู่มาก เขาวิจารณ์ code of conduct แต่ก็ตั้งกติกาว่าคนในชุมชนของตัวเองควรทำตัวอย่างไร

> "Communities require governance."

ในโพสต์นี้ governance หมายถึงงานตัดสินใจและดูแลชุมชนที่ทำให้โปรเจกต์เดินต่อได้ ไม่ใช่สิ่งรบกวนงานเทคนิค ส่วนเรื่อง land acknowledgement นั้น cafkafk บอกว่าไม่ใช่ข้อถกเถียงหลักที่นิยามชุมชน NixOS และมองว่า DHH ดึง culture war บน X มาครอบชุมชนที่ยังรู้จักไม่พอ ตรงนี้เป็นคำประเมินของผู้เขียน ไม่ใช่ผลสำรวจสมาชิก NixOS

**ได้อะไร:** [[open-source-governance|Open Source Governance]] ไม่ได้มีแค่คำถามว่าใครอนุมัติ feature แต่รวมถึงกติกา review, security, release และการอยู่ร่วมกันของ contributor ด้วย

## ความสามารถไม่ได้เริ่มที่คนทำชั้นบน

โพสต์โต้คำชวนของ DHH เรื่องสร้างบ้านให้ “competent people” ว่าคนเก่งมีอยู่ใน ecosystem แล้ว และเป็นกลุ่มเดียวกับที่โปรเจกต์ของเขาต้องพึ่ง การวาง layer ใหม่บนงานเดิมจึงไม่ทำให้เจ้าของ layer กลายเป็นผู้ใหญ่ด้านเทคนิคเพียงคนเดียวในห้อง

cafkafk ปิดด้วยการต้อนรับ DHH สู่ NixOS แต่ขอให้ลด culture-war posturing แล้วเพิ่มความเคารพกับความถ่อมตัวต่อคนที่ทำฐานเหล่านี้

**ผลคือ:** ข้อโต้แย้งนี้วัดความชอบธรรมจากวิธีปฏิบัติต่อ upstream ไม่ได้วัดจากว่า layer ใหม่เขียนได้เร็วหรือดูเรียบง่ายแค่ไหน

## ขอบเขตหลักฐานและเรื่องที่ยังตอบไม่ได้

- คำดูถูกและคำชม Nix ข้างต้นมาจากการเล่าของ cafkafk เพราะข้อความที่ได้รับไม่มีบทสนทนาต้นทางของ DHH ให้เทียบบริบท
- โพสต์หลักเขียนว่า DHH “planning to build” บน NixOS ส่วน quote-post ใช้คำว่า “Seems Omarchy is going to switch to NixOS?” จึงเป็นรายงานเรื่องแผน ไม่ใช่หลักฐานว่า Omarchy ย้ายฐานเสร็จแล้ว
- หน้า [[omarchy|Omarchy]] เดิมบันทึกว่าใช้ Arch จากบทสัมภาษณ์ของ DHH เก็บข้อมูลนั้นไว้เป็นฐานที่รายงานก่อนหน้า และเก็บแผน NixOS จากโพสต์นี้ไว้คู่กันจนกว่าจะมีประกาศหรือ code จากโครงการ
- โพสต์ไม่ได้เทียบข้อดีข้อเสียทางเทคนิคของ Arch กับ NixOS และไม่ได้ตรวจโครงสร้าง governance ของ NixOS แบบเป็นระบบ
- คำว่า “สองสัปดาห์ก่อน” กับ “สองวันก่อน” เป็นเวลาคร่าว ๆ ที่นับจากโพสต์วันที่ 9 กันยายน 2026 ยังไม่มี permalink ของเหตุการณ์สองช่วงนั้นในข้อความที่ได้รับ

## See also

- [[cafkafk]]
- [[dhh]]
- [[omarchy]]
- [[nixos]]
- [[nixpkgs]]
- [[open-source-governance]]
- [[software-ecology]]
- [[socio-technical-system]]
