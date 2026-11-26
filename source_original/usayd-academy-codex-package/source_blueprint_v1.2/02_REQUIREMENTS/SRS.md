# Software Requirements Specification — IEEE-style adapted
**SRS ID:** SRS-001 | **Version:** 1.0 | **Baseline:** 2026-11-21 | **Status:** Draft for architecture/academic/legal approval

## 1. Introduction

### 1.1 Purpose
Specify verifiable behaviors for a multi-role Smart Quran Academy platform serving adults and minors. This SRS supports engineering, QA, Figma/UX, security, educational reviewers, vendor selection and Jira traceability.

### 1.2 Scope
A managed teaching service with learner registration, trial assessments, booking, subscription billing, teacher operations, configurable video conferences, learning plans, revision, tests, contests, content, AI assistance, analytics, mobile clients and administration. Not a teacher marketplace in first release.

### 1.3 Intended readers
Founder/investor, Product Owner, solution architect, Laravel/API engineers, web/Flutter engineers, designers, QA, academic supervisor, finance, legal/privacy.

### 1.4 Definitions
`Learner`: unified student entity regardless of age. `Guardian`: authorized consenting adult for a minor; portal optional. `Lesson`: educational scheduled unit. `Conference`: vendor instance. `Entitlement`: paid right to lesson/asset. `Evidence`: verified teacher rubric/test/attendance/input. `Plan`: approved version of tasks and milestones. `Contest`: organized assessment challenge. `AI suggestion`: nonauthoritative recommendation. `Capability`: provider-specific supported operation. `P0/P1/P2`: delivery sequencing, not product completeness.

## 2. System context

### 2.1 External interfaces
Web/Next.js, Flutter mobile, teacher & admin portals, backend `/api/v1`, MySQL or PostgreSQL, Redis, mail/WhatsApp/SMS, payment gateway, LiveKit/VideoSDK/Daily/Meet/Zoom, Quran content API subject to license, AI workers, metrics/alerts.

### 2.2 User groups
Adult learner, minor learner, teacher, academic supervisor, support, CRM sales, finance, content moderator, system admin, marketing analyst. Least privilege per action.

### 2.3 Constraints
Arabic-first, mixed adult/minor flows, legal consent and cross-border data review, accessible UI, fully externalizable video vendor integration, API first for eventual mobile, reliable billing and accurate religious content.

### 2.4 Operating assumptions
Qualified teacher availability, correct payment vendor enrollment, licensed Quran/recorded media, legal guidance, market pilot confirmation, properly configured vendor API credentials.

## 3. Requirements and functions

**Source of truth:** [requirements catalog](./REQUIREMENTS_CATALOG.md) with **148** unique `FR-*` entries. NFRs in [NFR catalog](./NON_FUNCTIONAL_REQUIREMENTS.md). All implementation work traces to these IDs, tests and screen/UI where applicable.

### 3.1 Identity and consent
Unrestricted all-age student registration UI, role/data policies, adult independence, minors legal approvals without mandatory parental dashboard. Principal FR modules: IAM, PROF.

### 3.2 Teaching supply and booking
Teacher certification, scheduling, substitution, capacity, no-show, lesson grants and attendance: TCHR, BOOK, ATT, VIDEO.

### 3.3 Transactions
Packages, accepted payments, entitlements, refunds, credits, immutable payouts and finance approvals: PAY, PAYROLL.

### 3.4 Academic outcomes
Curriculum, source integrity, approved assessments, plan versioning, memory map and revision engine: CURR, ASMT, PLAN.

### 3.5 Contests and rewards
Level/band eligibility, instructor-approved question banks, rubric, attempts, refereeing, appeals, child privacy, opt-in public recognition, clear prize rules: CONTEST. See dedicated competition SRS.

### 3.6 AI
Recommendation, grounded learning assistant, transcript moderation with informed consent, separate specialist recitation validation and human review: AI. No automatic expulsion or authoritative tajweed verdict.

### 3.7 Platforms and operations
Media, notification, leads, reports, support, privacy, mobile roadmap: MEDIA, NOTIF, CRM, ADMIN, MOB, SEC.

## 4. External interface requirements

- **API:** JSON over HTTPS with OpenAPI 3.1, problem+json consistent errors, Idempotency-Key on payment/booking mutations, cursor pagination, ISO 8601 timestamps, IANA timezone, currency ISO 4217.
- **Authentication:** web SameSite secure cookie/session or chosen secure token flow; short-lived mobile access/rotating refresh with secure storage; password reset and privileged MFA.
- **Video:** `create`, `join`, `get_capabilities`, `close`, `attendance_sync`, `recording_policy`; no assumption every provider embeds or exposes raw audio.
- **Quran:** immutable source edition and ayah reference, content license/attribution, never LLM-generated canonical text.
- **AI:** schema-validated outputs with provenance, latency/cost bounds, human-in-loop and rollback.

## 5. Core data invariants

- Learner is primary person; optional relation to authorized guardian/consent evidence.
- Lesson entitlement consumed exactly once and reversed safely on authorized makeup.
- Every student action is scoped to identity; no reading other student records by changing IDs.
- Published assessment and contest score have provenance and revision history.
- Provider transition changes conference asset, not lesson identity or historic learning records.
- A teacher pay run references immutable contract snapshot and verified eligible work.
- AI may suggest, never silently overwrite teacher-approved Quran grade or plan.

## 6. State machines

See `04_ENGINEERING/STATE_MACHINES.md`: lesson, subscription, assessment, learning plan, contest, prize, payroll and consent. Invalid transitions rejected with 409 or appropriate problem code and Audit Trail.

## 7. Safety and compliance

Documented privacy assessment and country-specific legal review, safeguarding SOP, processing consent, child protection escalation, recording disabled by default, strict retention/deletion, Quran rights, labor/competition rules, accessibility target WCAG 2.2 AA.

## 8. Verification and acceptance

Each FR requires: primary happy-path test; permission/age/consent negative test; empty/error/timeout/mobile/RTL UI where applicable; idempotency/concurrency for mutations; audit and analytics evidence; functional QA sign-off; Academic/Legal/Finance reviews where specified.

## 9. Traceability and open risks

Trace in `06_DELIVERY_JIRA/requirements_traceability.csv`, `test_cases.csv`, `Jira_Import.csv`, screen catalog. Technical POC must validate provider capabilities, cost and international networks before locking the implementation; business pilot validates pricing/retention separately.

## 10. SRS approval sheet

| Role | Approves | Status |
|---|---|---|
| Sponsor/Product | Scope and funding gates | Pending |
| CTO | Architecture and POC feasibility | Pending |
| Academic Lead | Rubrics, contests, Quran accuracy | Pending |
| Legal/Privacy | Children, recordings, law, rewards | Pending |
| Finance | Subscription and teacher pay rules | Pending |
| UX | Information architecture and accessibility | Pending |
| QA | Acceptance and release gates | Pending |
