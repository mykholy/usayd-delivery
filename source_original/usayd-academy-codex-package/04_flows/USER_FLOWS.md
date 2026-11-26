# Clickable user journeys

Open the canvas Screen map (`Main.dc.html`) and press **Start journey**, or open `01_design/html/ar/index.html`. Each step is a separate artboard joined by real links. Prototype links never imply backend behavior.

## F01 · Market & price → checkout quote
*اختيار السوق والسعر حتى عرض الدفع* · requirements: FR-GEO-002, FR-GEO-005

```mermaid
flowchart LR
  UX_GLOB_001["UX-GLOB-001<br/>Country & Currency Selector"] --> UX_GLOB_002["UX-GLOB-002<br/>Localized Pricing Comparison"]
  UX_GLOB_002["UX-GLOB-002<br/>Localized Pricing Comparison"] --> UX_AUTH_001["UX-AUTH-001<br/>Unified Signup"]
  UX_AUTH_001["UX-AUTH-001<br/>Unified Signup"] --> UX_AUTH_005["UX-AUTH-005<br/>Welcome Onboarding"]
  UX_AUTH_005["UX-AUTH-005<br/>Welcome Onboarding"] --> UX_GLOB_006["UX-GLOB-006<br/>Regional Checkout Quote"]
```

## F02 · Change language independently of country & timezone
*تغيير اللغة باستقلال عن البلد والتوقيت* · requirements: FR-I18N-006

```mermaid
flowchart LR
  UX_LEARNER_001["UX-LEARNER-001<br/>Learner Home"] --> UX_GLOB_004["UX-GLOB-004<br/>Language & Regional Preferences"]
  UX_GLOB_004["UX-GLOB-004<br/>Language & Regional Preferences"] --> UX_LEARNER_001["UX-LEARNER-001<br/>Learner Home"]
```

## F03 · Guest assessment booking (incl. minor gate)
*حجز تقييم مستوى لزائر (ومسار القاصر)* · requirements: FR-BOOK-002, FR-IAM-007

```mermaid
flowchart LR
  UX_PUBLIC_001["UX-PUBLIC-001<br/>Marketing Home"] --> UX_PUBLIC_009["UX-PUBLIC-009<br/>Free Assessment Booking"]
  UX_PUBLIC_009["UX-PUBLIC-009<br/>Free Assessment Booking"] --> UX_AUTH_001["UX-AUTH-001<br/>Unified Signup"]
  UX_AUTH_001["UX-AUTH-001<br/>Unified Signup"] --> UX_AUTH_002["UX-AUTH-002<br/>Guardian Consent Step"]
  UX_AUTH_002["UX-AUTH-002<br/>Guardian Consent Step"] --> UX_AUTH_005["UX-AUTH-005<br/>Welcome Onboarding"]
  UX_AUTH_005["UX-AUTH-005<br/>Welcome Onboarding"] --> UX_LEARNER_004["UX-LEARNER-004<br/>Initial Assessment"]
```

## F04 · Regional immutable payment quote
*عرض دفع إقليمي ثابت* · requirements: FR-PAY-003, FR-GEO-007

```mermaid
flowchart LR
  UX_GLOB_002["UX-GLOB-002<br/>Localized Pricing Comparison"] --> UX_GLOB_006["UX-GLOB-006<br/>Regional Checkout Quote"]
  UX_GLOB_006["UX-GLOB-006<br/>Regional Checkout Quote"] --> UX_LEARNER_029["UX-LEARNER-029<br/>Subscription & Billing"]
```

## F05 · Booking with an ambiguous DST time
*حجز حصة مع وقت ملتبس بسبب التوقيت الصيفي* · requirements: FR-TIME-004, FR-TIME-005

```mermaid
flowchart LR
  UX_LEARNER_008["UX-LEARNER-008<br/>Booking Wizard"] --> UX_GLOB_005["UX-GLOB-005<br/>Timezone Preview & DST Warning"]
  UX_GLOB_005["UX-GLOB-005<br/>Timezone Preview & DST Warning"] --> UX_LEARNER_009["UX-LEARNER-009<br/>Lesson Detail"]
```

## F06 · Teacher schedule collision across markets
*تعارض جدول المعلم عبر الأسواق* · requirements: FR-TIME-006

```mermaid
flowchart LR
  UX_TEACHER_003["UX-TEACHER-003<br/>Availability"] --> UX_GLOB_008["UX-GLOB-008<br/>Timezone Availability Editor"]
  UX_GLOB_008["UX-GLOB-008<br/>Timezone Availability Editor"] --> UX_TEACHER_004["UX-TEACHER-004<br/>Teaching Calendar"]
```

## F07 · Video provider switch with dual approval
*تبديل مزود الفيديو باعتماد مزدوج* · requirements: FR-VPC-005, FR-VPC-006

```mermaid
flowchart LR
  UX_VPC_001["UX-VPC-001<br/>Video Providers Overview"] --> UX_VPC_003["UX-VPC-003<br/>Video Provider Capabilities"]
  UX_VPC_003["UX-VPC-003<br/>Video Provider Capabilities"] --> UX_VPC_004["UX-VPC-004<br/>Video Routing Rules"]
  UX_VPC_004["UX-VPC-004<br/>Video Routing Rules"] --> UX_VPC_005["UX-VPC-005<br/>Video Switch Impact & Dry-run"]
  UX_VPC_005["UX-VPC-005<br/>Video Switch Impact & Dry-run"] --> UX_VPC_006["UX-VPC-006<br/>Video Routing Approval"]
```

## F08 · Join via external meeting, then report
*الدخول للحصة عبر رابط خارجي ثم التقرير* · requirements: FR-VIDEO-004, FR-VPC-011

```mermaid
flowchart LR
  UX_LEARNER_009["UX-LEARNER-009<br/>Lesson Detail"] --> UX_VPC_009["UX-VPC-009<br/>Embedded vs External Prejoin"]
  UX_VPC_009["UX-VPC-009<br/>Embedded vs External Prejoin"] --> UX_LEARNER_010["UX-LEARNER-010<br/>Classroom"]
  UX_LEARNER_010["UX-LEARNER-010<br/>Classroom"] --> UX_LEARNER_011["UX-LEARNER-011<br/>Post-Lesson Report"]
```

## F09 · Consent-based AI analysis with teacher approval
*تحليل ذكي بموافقة واعتماد المعلم* · requirements: FR-AI-003, FR-IAM-006

```mermaid
flowchart LR
  UX_LEARNER_032["UX-LEARNER-032<br/>Account Settings"] --> UX_LEARNER_027["UX-LEARNER-027<br/>AI Study Assistant"]
  UX_LEARNER_027["UX-LEARNER-027<br/>AI Study Assistant"] --> UX_TEACHER_011["UX-TEACHER-011<br/>Plan Review Queue"]
```

## F10 · Competition through appeal
*المسابقة حتى التظلم* · requirements: FR-CONTEST-011

```mermaid
flowchart LR
  UX_LEARNER_020["UX-LEARNER-020<br/>Competitions Discover"] --> UX_LEARNER_021["UX-LEARNER-021<br/>Competition Detail"]
  UX_LEARNER_021["UX-LEARNER-021<br/>Competition Detail"] --> UX_LEARNER_022["UX-LEARNER-022<br/>Competition Preparation"]
  UX_LEARNER_022["UX-LEARNER-022<br/>Competition Preparation"] --> UX_LEARNER_023["UX-LEARNER-023<br/>Competition Round"]
  UX_LEARNER_023["UX-LEARNER-023<br/>Competition Round"] --> UX_LEARNER_025["UX-LEARNER-025<br/>Competition Result & Appeal"]
  UX_LEARNER_025["UX-LEARNER-025<br/>Competition Result & Appeal"] --> UX_TEACHER_015["UX-TEACHER-015<br/>Appeals Academic Review"]
  UX_TEACHER_015["UX-TEACHER-015<br/>Appeals Academic Review"] --> UX_ADMIN_031["UX-ADMIN-031<br/>Contest Appeals"]
```

## F11 · Supervisor approval with scope denial
*اعتماد المشرف مع رفض النطاق* · requirements: FR-SUP-002, FR-SUP-008

```mermaid
flowchart LR
  UX_SUP_001["UX-SUP-001<br/>Supervisor Home"] --> UX_SUP_002["UX-SUP-002<br/>Academic Plans Approval"]
  UX_SUP_002["UX-SUP-002<br/>Academic Plans Approval"] --> UX_SUP_004["UX-SUP-004<br/>Safeguarding Case Console"]
```

## F12 · Mobile offline draft & reconnect
*الموبايل: مسودة دون اتصال ثم العودة للحصة* · requirements: FR-MOB-002, FR-MOB-004

```mermaid
flowchart LR
  UX_MOBILE_002["UX-MOBILE-002<br/>Flutter Today"] --> UX_MOBILE_003["UX-MOBILE-003<br/>Flutter Classroom"]
  UX_MOBILE_003["UX-MOBILE-003<br/>Flutter Classroom"] --> UX_MOBILE_007["UX-MOBILE-007<br/>Flutter Exam"]
```

## F13 · Teacher lesson lifecycle
*دورة الحصة للمعلم* · requirements: FR-ATT-003

```mermaid
flowchart LR
  UX_TEACHER_002["UX-TEACHER-002<br/>Teacher Home"] --> UX_TEACHER_005["UX-TEACHER-005<br/>Lesson Briefing"]
  UX_TEACHER_005["UX-TEACHER-005<br/>Lesson Briefing"] --> UX_VPC_010["UX-VPC-010<br/>Teacher Provider Join Health"]
  UX_VPC_010["UX-VPC-010<br/>Teacher Provider Join Health"] --> UX_TEACHER_006["UX-TEACHER-006<br/>Teacher Classroom"]
  UX_TEACHER_006["UX-TEACHER-006<br/>Teacher Classroom"] --> UX_TEACHER_007["UX-TEACHER-007<br/>Lesson Report Editor"]
```

## F14 · Daily learning loop
*حلقة التعلم اليومية* · requirements: FR-PLAN-003, FR-PLAN-004

```mermaid
flowchart LR
  UX_LEARNER_001["UX-LEARNER-001<br/>Learner Home"] --> UX_LEARNER_013["UX-LEARNER-013<br/>Daily Study"]
  UX_LEARNER_013["UX-LEARNER-013<br/>Daily Study"] --> UX_LEARNER_014["UX-LEARNER-014<br/>Revision Queue"]
  UX_LEARNER_014["UX-LEARNER-014<br/>Revision Queue"] --> UX_LEARNER_015["UX-LEARNER-015<br/>Memory Map"]
  UX_LEARNER_015["UX-LEARNER-015<br/>Memory Map"] --> UX_ENG_003["UX-ENG-003<br/>Gentle Progress & Streak Recovery"]
```

## F15 · Payroll: accrual to approval
*الرواتب: من الاستحقاق للاعتماد* · requirements: FR-PAYROLL-008, FR-SUP-006

```mermaid
flowchart LR
  UX_TEACHER_016["UX-TEACHER-016<br/>Teacher Pay Statements"] --> UX_ADMIN_021["UX-ADMIN-021<br/>Payroll Calculations"]
  UX_ADMIN_021["UX-ADMIN-021<br/>Payroll Calculations"] --> UX_ADMIN_022["UX-ADMIN-022<br/>Payroll Approval"]
```

## F16 · Launch a market and price it
*إطلاق سوق جديد وتسعيره* · requirements: FR-GEO-010, FR-SUP-013

```mermaid
flowchart LR
  UX_GLOB_010["UX-GLOB-010<br/>Markets Overview"] --> UX_GLOB_011["UX-GLOB-011<br/>Market Launch Wizard"]
  UX_GLOB_011["UX-GLOB-011<br/>Market Launch Wizard"] --> UX_GLOB_012["UX-GLOB-012<br/>Country Pricing Matrix"]
  UX_GLOB_012["UX-GLOB-012<br/>Country Pricing Matrix"] --> UX_GLOB_013["UX-GLOB-013<br/>Price Approval & Version Diff"]
```

## F17 · Child safeguarding case
*حالة حماية طفل* · requirements: FR-SUP-004

```mermaid
flowchart LR
  UX_ADMIN_036["UX-ADMIN-036<br/>Safeguarding Incident Queue"] --> UX_SUP_004["UX-SUP-004<br/>Safeguarding Case Console"]
```

## F18 · Adaptive exam
*الاختبار التكيفي* · requirements: FR-ASMT-003

```mermaid
flowchart LR
  UX_LEARNER_017["UX-LEARNER-017<br/>Exam Catalog"] --> UX_LEARNER_018["UX-LEARNER-018<br/>Exam Taking"]
  UX_LEARNER_018["UX-LEARNER-018<br/>Exam Taking"] --> UX_LEARNER_019["UX-LEARNER-019<br/>Exam Results"]
```

## F19 · App launch: splash to today
*تشغيل التطبيق: من الشاشة الافتتاحية إلى اليوم* · requirements: FR-MOB-001

```mermaid
flowchart LR
  UX_MOBILE_000["UX-MOBILE-000<br/>Flutter Splash (added)"] --> UX_MOBILE_001["UX-MOBILE-001<br/>Flutter Login"]
  UX_MOBILE_001["UX-MOBILE-001<br/>Flutter Login"] --> UX_MOBILE_002["UX-MOBILE-002<br/>Flutter Today"]
```
