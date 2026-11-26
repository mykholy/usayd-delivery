# CLAUDE / FIGMA — MASTER DESIGN BUILD BRIEF (copy/paste)

**Project:** Smart Quran Academy | **Status:** Design production-ready *specification + Figma designs*, not a demand to fabricate operational claims. **Date:** 2026-11-21.

## ROLE AND OBJECTIVE

You are a multidisciplinary Product Design Director, Senior UX Researcher, Arabic RTL UI specialist, Flutter/Responsive UX architect, and Design Systems lead. Build a **real editable Figma design system and complete high-fidelity screen library** for an API-first premium Quran-learning academy for adults and minors. Generate actual Figma frames/components/variables through authorized Figma tooling if available; do not replace editable Figma with static images. If no Figma tool access, output component and page construction instructions plus inspectable HTML prototype explicitly labeled as a fallback; never claim a Figma file was created.

## SOURCE PACK AND AUTHORITY

Read **ALL** files, especially:
- `00_START_HERE/README.md`, `00_START_HERE/DECISIONS_AND_OPEN_ITEMS.md`.
- `01_BUSINESS/BRD.md`, `01_BUSINESS/GO_TO_MARKET.md`.
- `02_REQUIREMENTS/PRD.md`, `02_REQUIREMENTS/SRS.md`, `02_REQUIREMENTS/REQUIREMENTS_CATALOG.md`, `02_REQUIREMENTS/NON_FUNCTIONAL_REQUIREMENTS.md`.
- `03_ACADEMIC_AI/LEARNING_AI_AND_ASSESSMENTS.md`, `03_ACADEMIC_AI/COMPETITIONS_AND_REWARDS.md`.
- `04_ENGINEERING/VIDEO_PROVIDER_RFC.md`, `04_ENGINEERING/API_IMPLEMENTATION_GUIDE.md`.
- `05_UI_UX/SCREEN_CATALOG.md`, `05_UI_UX/SCREEN_DETAILED_SPECS.md`, `05_UI_UX/DESIGN_SYSTEM.md`, `05_UI_UX/UX_COPY_AR_EN.md`, `05_UI_UX/MOBILE_FLUTTER_SPEC.md`.

In conflict, decisions and safety/privacy requirements override visual suggestions. Do not invent accreditation, testimonial, real Quran text, student data, teacher names, or live SDK capabilities. Use synthetic screen data labeled 'Sample' in design; actual product content must be fetched from licensed verified sources.

## CREATIVE NORTH STAR

Premium contemporary trust; Arabic typography and generous whitespace; emerald/teal and subtle warm gold; sophisticated dashboards with restrained charts; Quran reader optimized for diacritics and cognitive comfort. **NOT** a generic LMS template, endless green cards, dark ornamental wallpaper, default Bootstrap, or random gradients. Each persona gets tailored information density and navigation. Reuse shared tokens but differentiate marketing, student learning, teacher workflow, admin operations and Flutter mobile.

## FIRST FIGMA DELIVERABLES

Create these page groups (exact names):
1. `00_Cover_And_Decisions`
2. `01_Foundations_Colors_Type_Grid_RTL`
3. `02_Components_Primitives_Forms_Navigation`
4. `03_Components_Learning_Quran_Classroom`
5. `04_Components_Contest_Assessment_AI`
6. `05_Public_Web`
7. `06_Auth_Onboarding`
8. `07_Learner_Desktop_Tablet`
9. `08_Teacher_Desktop_Tablet`
10. `09_Admin_Desktop`
11. `10_Flutter_Learner_Mobile`
12. `11_Flutter_Teacher_Mobile`
13. `12_Prototype_User_Journeys`
14. `13_States_Errors_Accessibility`
15. `14_Developer_Handoff_Annotations`

## SCREEN COVERAGE CONTRACT

Read the **119 screen IDs in `SCREEN_CATALOG.md`**; every ID must get either a high-fidelity frame (critical/current phase) or an explicitly linked layout/variant design row with component references (later phase). Never mark a missing screen complete. UI states: default, loading, empty, errors, offline, auth-denied, consent-pending, payment-pending, vendor unavailable, AI suggestion unapproved, contest ineligible, contest provisional results, contest score appeal, human-reviewed final result.

Critical high-fidelity screens first: Marketing Home; Unified Signup; Minor Consent Step; Learner Today; Booking Wizard; Live Classroom with both embedded and external meeting; Learning Plan; Memory Map; Revision Queue; Adaptive Exam; Exam Result; Competition Directory/Detail/Round/Private Standings/Appeal/Achievements; Teacher Today/Video/Report/Plan Approval/Judging/Pay Statement; Admin Dashboard/Teacher Contracts/Competition Builder/Control Room/Appeals/AI Policy Review/Billing/Consent Queue; Flutter Home/Classroom/Exam/Competition/Teacher Report.

## RESPONSIVE / RTL REQUIREMENTS

Desktop 1440, tablet 768, mobile 390 (also inspect 360 min); Flutter Android/iOS with safe areas. Arabic right-to-left menus and number/date formatting, English left-to-right variant. Avoid flipping Quran text itself. Arabic UI is not simply mirroring icons. UI text in readable natural Arabic: use examples from `UX_COPY_AR_EN.md`. Design inclusive learner (adult) accounts with guardian consent gate ONLY for legally required cases; do not force 'parent dashboard' on independent adults.

## ESSENTIAL COMPONENTS AND STATES

Use shared Figma Variables/styles from `figma_tokens.json`, tokenized spacing/color/radius/type. Auto Layout across reusable components and variants. Build `QuranReader`, `VerseRangePill`, `StudyTaskCard`, `MemoryMap`, `RevisionDue`, `TutorCard`, `PrejoinDeviceCheck`, `ClassroomVideoStage`, `ConnectionBanner`, `AIRecommendationWithEvidence`, `TeacherReportRubric`, `AssessmentQuestionTypes`, `ContestRegistrationEligibility`, `ContestCountdown`, `JudgeScoringRubric`, `PseudonymLeaderboard`, `AppealTimeline`, `AwardCertificate`, `TeacherCompensationBuilder`, `MoneyLedger`, `AdminAuditTimeline`, `ConsentGate`, `ErrorRecoveryPanel`, `EmptyState`, `Skeleton`.

## FLAGSHIP VIEW: STUDENT DESKTOP

Split desktop into role nav, page header, next live lesson hero, due revision queue with passage ranges, study plan evidence, personal memory map, teacher feedback and contest upcoming card. Don't stack unrelated cards randomly. Show where CTA lives and how learner can get meaningful practice even with no scheduled lesson today.

## FLAGSHIP VIEW: LIVE CLASSROOM

Prejoin test and policies; teacher/student media stage; Quran text workspace; teacher notes and passage selection; mic/camera settings; low-data audio mode; provider badge; reconnection; countdown; explicit recording indicator only when applicable. Render two branches: (a) fully embedded SDK, (b) Google Meet/Zoom Meeting external with separate Quran workspace and return link. UI cannot imply disabled provider API features are available.

## FLAGSHIP VIEW: COMPETITIONS

Competition feed with badges for level/age eligibility; clear timing/rules/prize terms; exam round with attempts; human-judged oral round; provisional results; private default leaderboard; appeal status; certificate. Include alternate student branch for minors and opt-in pseudonyms. Don't create public rankings for minors by default or pay-to-win purchase mechanics.

## FLAGSHIP VIEW: AI TRACKER

Show teacher-approved plan, original assessment evidence, proposed AI amendments with explicit approve/reject by teacher, revision schedules with reason, historical grade trends with shared rubric scale. Do not pretend AI automatically judges Quran correctness.

## TEACHER AND ADMIN

Teacher workload: teach, assess, plan, check reports and contest judging; low typing. Admin: dashboards and powerful forms, safe permissions, date-correct finance, teacher payment models salary/per hour/per lesson/per shift/hybrid with example preview; exception queues for consent/payment/provider incidents. Show multi-step contest setup with academic/legal approvals before publishing.

## FIGMA PROTOTYPE LINKS

Link clickable journeys: Visitor→Signup→Assessment→Subscription→Schedule→Join→Lesson Report→Review; Adult User→AI Proposal→Teacher Approved Plan; Contest→Eligibility→Round→Judge→Provisional Result→Appeal→Final Award; Teacher→Schedule→Classroom→Report→Compensation; Admin→Contest Creation→Judging→Finalize; Outage/Consent Denied/Payment Pending branches.

## DESIGN QUALITY VALIDATION

For each page show at least one clear CTA and realistic content density; no clipped Arabic diacritics, no inaccessible contrast, no lorem ipsum, no invented certification or names, no child portrait in public testimonials. Check keyboard focus, screen reader semantics and touch target sizes. 2 visual options for Public Homepage only; choose one consistent premium direction for all role dashboards. Deliver ready-to-review visual system, annotated flows, component variants and Figma link/file IDs; if Figma access absent state precisely what was produced.

## OUTPUT MANIFEST TO REPORT

`FigmaPages`, `CoreComponents`, `ScreenCoverageByUXId`, `PrototypeJourneys`, `DesignTokens`, `MissingScreens`, `UnresolvedProductQuestions`, `AccessibilityFindings`, `Screenshots/Preview Export`, `NextDeveloperHandoff`. Explicitly count and list gaps; do not claim full coverage until checked against `SCREEN_CATALOG.md`.
