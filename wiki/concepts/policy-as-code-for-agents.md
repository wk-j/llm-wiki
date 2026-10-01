---
title: Policy as Code for Agents
type: concept
tags: [ai, agents, governance, security, enterprise, compliance, sdlc]
created: 2026-09-14
updated: 2026-09-30
sources: [ai-native-sdlc-playbook.md, engineering-the-harness-thoughtworks.md]
---

# Policy as Code for Agents / วางนโยบายองค์กรเป็นชั้นควบคุม agent

เวลาองค์กรจะให้ agent ทำงานจริง คำถามแรกไม่ใช่ "model เก่งพอไหม" แต่คือ "ถ้า agent ทำผิด อะไรจะหยุดได้" [[ai-native-sdlc-playbook|AI-Native SDLC Playbook]] ของ [[anthropic|Anthropic]] ตอบด้วยชั้นควบคุมสามระดับที่แข็งขึ้นเรื่อย ๆ แต่ละระดับใช้กับนโยบายคนละแบบ

หลักคือ **ใส่ policy ตั้งแต่ตอนสร้างงาน ไม่ใช่รอให้เจอปัญหาตอน review** เพราะถึงตอนนั้นมีคนรออยู่แล้ว และงานก็แก้ยากกว่าเดิม

## สามชั้น ไล่จากหลวมไปแข็ง

| ชั้น | กลไก | บังคับได้แค่ไหน | เหมาะกับ |
| --- | --- | --- | --- |
| Skills | โฟลเดอร์ instruction ที่ model อ่านแล้วทำตาม | แนะนำเฉย ๆ model อาจพลาดหรือข้ามได้ | ความรู้เชิงนโยบายที่ต้องตีความ เช่น "endpoint ต้องผ่าน gateway JWT ห้ามมี anonymous route" |
| Hooks | script ที่รันคร่อม action ตอบได้ allow / ask / block | แน่นอน ตรวจได้ ไม่ขึ้นกับ model | กฎเชิงกล เช่นห้ามแตะ path ที่ freeze, กัน credential เข้า diff, หยุดรอคนอนุมัติ |
| Managed settings | config ที่ push ผ่าน MDM | ปลายทางแก้ไม่ได้ | สิ่งที่ต่อรองไม่ได้ เช่น sandbox, domain ที่ออกเน็ตได้, การปิดการอ่าน credential |

ตัวอย่างที่ทำให้เห็นภาพ: กฎว่า "API ใหม่ต้องมี audit log" อยู่ใน skill ได้ เพราะต้องอ่านบริบทว่าอะไรนับเป็น audit log ในระบบนี้ ส่วนกฎว่า "ห้ามอ่าน `~/.aws/credentials`" ไม่ควรอยู่ใน skill เลย เพราะมันตรวจได้ตรง ๆ และผลของการพลาดหนักเกินกว่าจะฝากไว้กับการเชื่อฟัง

**ได้อะไร:** เลือกชั้นตามว่ากฎนั้นต้องตีความไหม และพลาดแล้วเจ็บแค่ไหน ไม่ใช่ยัดทุกอย่างลง prompt

## ทำไมชั้นแข็งสุดต้องอยู่ที่ OS ไม่ใช่ที่ prompt

Managed settings ในตัวอย่างมีหลายข้อ แต่ทั้งหมดใช้หลักเดียวกัน คือ **ตัดความสามารถออก แทนที่จะสั่งไม่ให้ทำ**

- ปิดทางอ่าน `.env*` และ `secrets/**` แล้วเปิดเฉพาะ inner loop ที่ปลอดภัย (`git`, `make build/test/lint`) ไว้ล่วงหน้า
- บังคับ sandbox ระดับ OS และตั้งให้ **ไม่ยอมรันเลยถ้า sandbox ใช้ไม่ได้** แทนที่จะ fallback ไปโหมดหลวม
- ออกเน็ตได้เฉพาะ domain ที่ระบุ
- ให้ OS ปฏิเสธการอ่าน `~/.ssh`, `~/.aws/credentials` และถอด token ออกจาก environment variable
- บังคับว่า skill, hook และ MCP server ต้องมาจาก marketplace ขององค์กร ปิด flag ที่ sideload ของนอกเข้ามาได้
- ปิดไม่ให้ engineer ขยาย permission เอง และไม่ให้สตาร์ทบน version ที่ยังไม่ได้ประเมิน

เหตุผลตรงไปตรงมา: prompt injection, tool ที่หลอก และความผิดพลาดของ model ล้วนอยู่ในชั้นที่ "การสั่งไม่ให้ทำ" เอาไม่อยู่ แต่ถ้ากระบวนการอ่านไฟล์นั้นไม่ได้ตั้งแต่แรก ก็ไม่มีอะไรให้ฝ่า นี่คือหลักเดียวกับ [[agent-runtime-untrusted|การถือว่า runtime ของ agent เป็นของที่ไว้ใจไม่ได้]]

**ผลคือ:** ความปลอดภัยไม่ได้ขึ้นกับว่า model วันนี้เชื่อฟังแค่ไหน

### ตัวอย่างเล็กกว่า: tool แบบ least-privilege

[[engineering-the-harness-thoughtworks|บทความของ Thoughtworks]] ใช้หลักเดียวกันในระดับ agent แต่ละตัว การเขียนใน prompt ว่า "อย่า push code" หรือ "อย่าแก้ config" เปราะเกินไป ให้เปลี่ยนเป็นข้อบังคับเชิงโครงสร้างแทน ตัวอย่างคือ agent ที่ตอบคำถามหรือตรวจโค้ด ได้แค่ tool อ่านอย่างเดียว ไม่มีความสามารถเขียนไฟล์ตั้งแต่ต้น

**ได้อะไร:** ไม่ต้องใช้ managed settings ทั้งองค์กรก็เริ่มได้ แค่เลือก tool ให้ agent ตามบทบาท

## ยังต้องแยกหน้าที่เหมือนเดิม

ชั้นควบคุมไม่ได้ยกเลิกกฎเก่าของ audit เรื่อง separation of duties สิ่งที่ playbook ยืนยันไว้:

- agent ที่เขียน code อนุมัติ code ตัวเองไม่ได้ บังคับที่ branch protection ไม่ใช่ที่ instruction
- hook ที่ประตู production บล็อกจนกว่า release manager ที่ระบุชื่อจะอนุมัติ
- ทุกครั้งที่รันแบบ non-interactive ต้องแยก log ว่าเป็น identity ของ agent หรือของคน
- การ block ต้องบอกเหตุผลและบอกทางไปขออนุมัติ ไม่ใช่แค่ปฏิเสธเงียบ ๆ

ถ้า block แล้วไม่บอกทางขออนุมัติ คนอาจหาทางอ้อมนอกระบบ และ audit trail จะขาดตรงจุดนั้น

## ทำ policy ให้มี regression test

ชั้นควบคุมพวกนี้เป็น code จึงพังได้ และ **การแก้ skill หนึ่งบรรทัดเปลี่ยนพฤติกรรมของทุก session พร้อมกัน** playbook จึงให้รันชุด eval ทุกครั้งที่แก้ `CLAUDE.md`, skill หรือ hook แล้ว gate การ merge ไว้ที่ pass rate

พูดอีกแบบคือ policy ขององค์กรได้ CI เหมือน code ทั่วไป ถ้าไม่มีชั้นนี้ การ "ปรับ prompt นิดหน่อย" จะกลายเป็นการเปลี่ยน production behavior ที่ไม่มีใครเห็น ดู [[evals-and-error-analysis]] และ [[prompt-ablation]]

## จุดที่ควรระวัง

- **ชั้นหลวมเกินก็ไม่บังคับ ชั้นแข็งเกินก็ขวางงาน:** ถ้า managed settings ปิดจนงานปกติทำไม่ได้ คนจะกลับไปทำงานนอกระบบ ซึ่งแย่กว่าเดิม
- **skill ยาวเกินกิน context:** ทุก skill ที่โหลดทุกครั้งคือต้นทุนคงที่ต่อ session ดู [[instruction-budget]]
- **marketplace ขององค์กรต้องมีคนดูแลจริง:** ไม่งั้นจะกลายเป็นคิวที่ทุกคนรอ แล้ว [[open-source-governance|ปัญหาเรื่องใครมีสิทธิ์อนุมัติอะไร]] ก็ย้ายมาอยู่ตรงนี้แทน
- **hook ตัดสินแทนคนไม่ได้:** ตอบได้แค่ว่ากฎเชิงกลผ่านไหม แต่บอกไม่ได้ว่า requirement นี้ยังแก้ปัญหาจริงหรือเปล่า

## See also

- [[ai-native-sdlc-playbook]]
- [[control-bands]]
- [[agent-runtime-untrusted]]
- [[graduated-autonomy]]
- [[claude-md]]
- [[instruction-budget]]
- [[evals-and-error-analysis]]
- [[agentic-code-review]]
- [[ai-driven-sdlc]]
- [[agent-observability]]
- [[model-context-protocol]]
- [[engineering-the-harness-thoughtworks]]
