---
title: AI Data Center Bottlenecks
type: concept
tags: [ai, data-center, infrastructure, hardware, networking]
created: 2026-07-03
updated: 2026-07-03
sources: [review-lite-cohr-nok-aaoi.md, how-ai-became-more-expensive-than-workers-it-replaced.md]
---

# AI Data Center Bottlenecks / คอขวดของ AI data center

AI data center bottlenecks คือคอขวดที่ทำให้ระบบ AI ทั้งศูนย์ไม่เร็วตามชิ้นส่วนที่แพงที่สุด. ในวิดีโอ [[review-lite-cohr-nok-aaoi|Review LITE COHR NOK AAOI]] ผู้พูดเสนอว่า หลังจากตลาดคุยเรื่อง GPU, memory, และ CPU แล้ว คอขวดถัดไปที่ถูกเล่ามากขึ้นคือ [[photonic-interconnects|photonic interconnects]] หรือการส่งข้อมูลผ่านแสง

## ทำไมคอขวดขยับได้

พอ GPU แรงขึ้นและ memory bandwidth สูงขึ้น งาน AI ก็ไม่ได้ติดแค่ compute. Model ต้องย้าย activation, weights, gradients, request, response, และ intermediate data ข้ามเครื่องและข้าม rack ถ้า network ช้า hardware แพง ๆ จะรอกันเอง

ตรงนี้ทำให้ optical module, switch, fiber, DSP, และ data-center network fabric กลายเป็นส่วนหนึ่งของ AI scaling story

**ได้อะไร:** การลงทุน AI infrastructure ต้องดูทั้งระบบ ไม่ใช่ดูเฉพาะ GPU หรือ model benchmark

## บทเรียนจากคลิป photonics

คลิปให้บทเรียนสำคัญ: คอขวดทางเทคนิคไม่เท่ากับกำไรสูงเสมอไป

ผู้พูดเทียบ photonics กับ memory. Memory เช่น DRAM เคยมีช่วง margin สูงมากเมื่อของขาด แต่ photonics ในอดีตไม่ได้ทำกำไรสูงเท่านั้นเสมอ. ดังนั้นต้องถามต่อว่า:

- บริษัทคุมต้นน้ำไหม เช่น [[indium-phosphide-wafer|Indium Phosphide wafer]]
- capacity พร้อมหรือยัง
- ลูกค้า qualify แล้วหรือยัง
- ราคาขายขึ้นเร็วกว่าต้นทุนไหม
- บริษัทอยู่ในส่วนที่ได้กำไรก่อน หรือแค่มีชื่ออยู่ใน theme

## ความเชื่อมโยงกับ wiki AI hardware

ก่อนหน้านี้ wiki มีเรื่อง [[longcat-2-0|LongCat 2.0]] และคำถามว่า AI model ต้องพึ่ง NVIDIA/CUDA แค่ไหน. หน้านี้เพิ่มอีกชั้น: ต่อให้มี compute stack แล้ว ระบบก็ยังติด network, power, memory, cooling, และ supply chain ของชิ้นส่วน data center ได้

**ผลคือ:** AI scaling เป็นปัญหา systems engineering ทั้งก้อน ไม่ใช่แค่ model architecture หรือ GPU procurement

## จากคอขวดกายภาพสู่ราคา token

วิดีโอ [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] เพิ่มด้านราคาเข้าไป: ถ้า data center, power, GPU, networking, cooling, และชิ้นส่วนอิเล็กทรอนิกส์สร้างไม่ทัน demand ต้นทุนที่องค์กรเห็นปลายทางคือ [[ai-token-economics|token price]] ที่สูงขึ้น

แหล่งนี้ยังตั้งคำถามว่า demand ที่ hyperscaler เห็นเป็น demand ใช้งานจริงทั้งหมดหรือมี [[tokenmaxxing|tokenmaxxing]] / leaderboard gaming ปนอยู่. ถ้า demand บางส่วนเป็นสัญญาณเทียม การวางแผน data center จากตัวเลขนั้นก็เสี่ยงอ่านตลาดผิด

**ผลคือ:** คอขวด data center ไม่ใช่แค่ทำให้ AI ช้าหรือ capacity ไม่พอ แต่มันทำให้ ROI ของ enterprise AI เปลี่ยนได้ด้วย

## See also

- [[review-lite-cohr-nok-aaoi]]
- [[photonic-interconnects]]
- [[optical-transceivers]]
- [[indium-phosphide-wafer]]
- [[nvidia]]
- [[longcat-2-0]]
- [[ai-token-economics]]
- [[enterprise-ai-roi]]
- [[tokenmaxxing]]
