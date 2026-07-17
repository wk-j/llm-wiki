---
title: "Migel Tissera on X: Android App Behavioral Fingerprinting SDKs"
type: source
tags: [android, privacy, security, behavioral-biometrics, anti-fraud, reverse-engineering]
created: 2026-07-16
updated: 2026-07-16
sources: ["https://x.com/migtissera/status/2077079252864991717"]
---

# Migel Tissera on X: Android App Behavioral Fingerprinting SDKs / SDK เก็บพฤติกรรมในแอป X บน Android

[[migel-tissera|Migel Tissera]] (ผู้เผยแพร่ field report จากการวิเคราะห์แอป Android) บอกว่าเขาพบ SDK สองตัวอยู่ใน APK ของ [[x-twitter|X หรือ Twitter]] SDK ทั้งคู่ยังไม่ทำงานใน session ที่เขาตรวจ แต่ code ที่พบรองรับการเก็บสัญญาณกว้างทั้งแอปเมื่อถูกเปิดใช้ เช่น จังหวะพิมพ์ การแตะหน้าจอ event ของ clipboard รูปใหม่ใน gallery motion sensor และ identifier ของเครื่อง

ใจความสำคัญไม่ใช่ “X กำลังอ่านข้อความทุกตัวที่พิมพ์” เพราะ thread ยังไม่แสดงหลักฐานถึงขั้นนั้น ผู้เขียนระบุชัดเฉพาะ clipboard ว่าเก็บ event type, timing และ length แต่ไม่เก็บ text content. ส่วนคำว่า `character deltas per field` ในฝั่ง keyboard ยังไม่ได้อธิบายละเอียดว่าบันทึกอะไรและย้อนสร้างข้อความได้หรือไม่ Claim ที่แข็งแรงกว่าคือ APK มี infrastructure สำหรับ [[behavioral-biometrics|behavioral biometrics]] และ session ของผู้เขียนเห็นว่ามันยัง gated/inactive. การโยงไป fraud ของ X Money/X Pay หรือ ID verification ยังเป็นสมมติฐาน ไม่ใช่คำยืนยันจาก X

## ผู้เขียนรายงานว่าระบบเก็บอะไรได้

รายการนี้มาจาก thread และ session log ที่ผู้เขียนแนบมา Wiki ยังไม่ได้ตรวจ APK, SDK หรือ network traffic ซ้ำเอง

| กลุ่มสัญญาณ | สิ่งที่ thread ระบุ | สิ่งที่ยังสรุปไม่ได้ |
| --- | --- | --- |
| การพิมพ์ | inter-keystroke timing และ character delta แยกตาม field | thread ไม่ได้นิยาม `character delta` จึงยังสรุปไม่ได้ว่าเห็นหรือย้อนสร้างข้อความได้แค่ไหน |
| Clipboard | ประเภท event, เวลา และความยาวของ paste/copy/cut | ผู้เขียนบอกว่าไม่เก็บ text content |
| Touch/gesture | event การแตะและ gesture ทุกหน้าจอเมื่อ SDK ถูกเปิด | ยังไม่รู้ว่า sample/ส่งออกมากแค่ไหน |
| รูปในเครื่อง | `ContentObserver` เฝ้า `MediaStore.Images` เพื่อรู้ว่ามีภาพหรือ screenshot ใหม่ | การเห็น event ว่ามีไฟล์ใหม่ไม่เท่ากับอ่านหรือ upload ภาพนั้น |
| Motion/device | accelerometer และ sensor อื่น, `ANDROID_ID`, advertising ID, carrier, root/emulator flags | ยังไม่รู้ retention, ปลายทาง หรือ policy ที่ใช้ผูกข้อมูล |
| Device token | token ถาวรที่ผู้เขียนบอกว่า XOR-obfuscated | XOR เป็นการทำให้อ่านยาก ไม่ใช่หลักฐานว่า token ปลอดภัยหรือถูกใช้ติดตามจริง |

สัญญาณแต่ละตัวอาจดูไม่รุนแรงเมื่อแยกกัน แต่พอรวมจังหวะพิมพ์ รูปแบบการแตะ sensor และ identifier ก็สร้างลายนิ้วมือเชิงพฤติกรรมที่แยกคนหรือ session ออกจากกันได้

**ได้อะไร:** ความเสี่ยงอยู่ที่การรวมสัญญาณหลายชั้น ไม่ได้อยู่ที่ event ตัวเดียว

## “มี code” ยังไม่เท่ากับ “กำลังเก็บข้อมูล”

thread ย้ำหลายครั้งว่า SDK ยัง inactive อย่างน้อยบนเครื่องของผู้เขียน นี่ทำให้ต้องแยกหลักฐานสามระดับ:

1. **Capability** — APK มี class, hook หรือ observer ที่รองรับการเก็บข้อมูล
2. **Activation** — runtime เปิด path นั้นจริงใน account, region หรือ feature ใด
3. **Collection/use** — app ส่ง เก็บ รวม และใช้ข้อมูลอย่างไรหลังเปิด

หลักฐานในโพสต์แตะระดับแรกและมี runtime observation จากเครื่องเดียวเพื่อบอกว่าระดับสองยังไม่เกิดใน session นั้น แต่ยังไม่พอพิสูจน์ rollout, server-side flag, network destination, retention หรือการใช้จริงใน production

**ผลคือ:** dormant SDK เป็นเหตุให้ถามต่อและตรวจซ้ำ ไม่ใช่หลักฐานว่า surveillance กำลังเกิดกับทุกคนแล้ว

## สมมติฐาน X Money / X Pay

Tissera คาดว่า infrastructure นี้น่าจะใช้ทำ anti-fraud เช่นจับ bot, account takeover หรือบัตรที่ขโมยมาในบริการการเงินของ X เขาตอบใน conversation เพิ่มว่า feature อาจถูกเปิดเมื่อใช้ X Money/X Pay หรือทำ ID verification

เหตุผลนี้เป็นไปได้ในเชิงเทคนิค เพราะระบบการเงินใช้ [[behavioral-biometrics|รูปแบบพฤติกรรม]] ประกอบ risk score ได้โดยไม่ต้องอ่านข้อความ แต่ thread ไม่ได้มีเอกสาร SDK, config, endpoint หรือคำยืนยันจาก X ที่ผูก code กับผลิตภัณฑ์นั้นโดยตรง จึงต้องเก็บเป็น hypothesis

อีกด้าน ต่อให้จุดประสงค์คือ anti-fraud ก็ยังมีคำถามเรื่อง scope. การ register hook แบบ process-wide ทำให้ระบบมองเห็น event นอกหน้าจอจ่ายเงินได้ ถ้าไม่จำกัดช่วงเวลา field และ retention ให้ชัด ขอบเขตกว้างกว่าที่ผู้ใช้คาดจากฟีเจอร์การเงิน

**ได้อะไร:** จุดประสงค์ที่ชอบธรรมไม่ได้ตอบคำถามเรื่องสัดส่วน ความยินยอม และขอบเขตโดยอัตโนมัติ

## คำว่า keylogger ยังสรุปเกินหลักฐาน

มีผู้ตอบ thread เรียกระบบนี้ว่า keylogger แต่คำนี้พาให้คนเข้าใจว่า app เก็บ raw text ครบทุกตัว ขณะที่หลักฐานในข้อความระบุ inter-keystroke timing กับ `character deltas per field` โดยไม่อธิบายรูปแบบ delta. เราจึงยังบอกไม่ได้ทั้งว่าเป็นเพียง metadata หรือว่าย้อนสร้างข้อความบางส่วนได้

ตรงนี้สำคัญเพราะการอธิบายเกินหลักฐานทำให้ประเด็น privacy ที่ตรวจได้อ่อนลง คำที่แม่นกว่า ณ ตอนนี้คือ app-wide behavioral telemetry หรือ behavioral biometrics infrastructure แล้วเก็บความหมายของ `character delta` เป็นคำถามเปิด

## วิธีตรวจและข้อจำกัดของแหล่ง

ผู้เขียนแนบ session log และชวนผู้อ่านใช้ `apksaw` ซึ่งเขาอธิบายว่าเป็น MCP server สำหรับ [[mobile-app-reverse-engineering|reverse engineer แอป Android]] ผ่าน coding agent กับโทรศัพท์ที่ต่ออยู่ นี่ช่วยให้ claim ตรวจซ้ำได้ในหลักการ แต่ source ที่ wiki ได้รับมีลิงก์ย่อและไม่ได้มี APK version, SDK name, hash, decompiled path หรือ packet capture ครบในตัวข้อความ

โพสต์จึงเป็น field report จากผู้วิเคราะห์คนเดียวและเป็นการโปรโมตเครื่องมือของผู้เขียนไปพร้อมกัน การยืนยันที่แข็งแรงกว่าต้องมีอย่างน้อย app version, code path, activation condition, runtime trace, network destination และผลจากเครื่อง/account มากกว่าหนึ่งชุด

## เสียงจาก conversation

conversation มีทั้งคนที่มองว่า data collection แบบนี้ “ปกติ” เมื่อเทียบกับ TikTok และคนที่มองว่าเป็นเครื่องมือสอดส่อง แต่ไม่มีฝั่งไหนเพิ่มหลักฐานทางเทคนิคเกี่ยวกับ X Android ในข้อความที่ให้มา Tissera เองบอกว่า location, camera, microphone, contacts และ permission อื่นพบได้ใน social app ทั่วไป แล้วแยก SDK สองตัวนี้ออกมาเพราะ reach แบบ app-wide

คำว่า “Meta และ TikTok น่าจะทำทั้งหมดเหมือนกัน” เป็นการคาดของผู้เขียน ไม่ใช่ผลวิเคราะห์ที่แสดงใน thread นี้ Wiki จึงไม่ใช้โพสต์นี้ไปแก้ claim ของบริษัทอื่น

## คำถามที่ยังเปิดอยู่

- SDK สองตัวชื่ออะไร มาจาก vendor ไหน และอยู่ใน X Android version ใด
- เงื่อนไขเปิดใช้มาจาก remote config, account state, region, X Money/X Pay หรือ ID verification จริงหรือไม่
- ตอน active ระบบเก็บแค่ local risk score หรือส่ง raw event ออก network
- hook แบบ process-wide ยกเว้น password, direct message และ field อ่อนไหวหรือไม่
- `MediaStore.Images` observer รู้แค่ว่ามีไฟล์ใหม่ หรือเปิดอ่าน metadata/content ต่อ
- identifier และ device token ถูกเก็บนานแค่ไหน reset ได้อย่างไร และผูกข้าม account หรือ app install หรือไม่
- ผู้ใช้ได้รับ notice/consent ที่เจาะจงพอหรือไม่ และปิด feature ได้ไหม
- นักวิจัยคนอื่นทำซ้ำบน APK version และ account state เดียวกันได้ผลเหมือนกันหรือไม่

## ดูเพิ่ม

- [[migel-tissera]]
- [[x-twitter]]
- [[behavioral-biometrics]]
- [[mobile-app-reverse-engineering]]
- [[learning-from-users]]
