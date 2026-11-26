# Scenario flowbook: 24 Mermaid models (23 journeys + 1 architecture diagram)

## 01. Market Selection
**Source:** `04_flows/01_market_selection.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Guest loads localized site → Use selected market → Show coarse IP hint or country selector → User selects country → Load active price book and programs → Waitlist or unavailable notice.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 02. Locale Independence
**Source:** `04_flows/02_locale_independence.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Student settings → Change UI language AR or EN → Update user locale → Re-render RTL or LTR → Keep selected market currency and timezone unchanged.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 03. Payment Quote
**Source:** `04_flows/03_payment_quote.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** (1) Student → API: Select package and billing country → (2) API → Pricing: Market eligibility + active price book → (3) Pricing → API: Immutable quote amount_minor currency tax expiry → (4) API → Student: Quote and charge currency → (5) Student → API: Confirm checkout with idempotency key → (6) API → PSP: Create intent with merchant profile and amount → (7) PSP → API: Webhook signed event → (8) API → API: Verify dedup and reconcile ledger → (9) API → Student: Paid entitlement or pending status *(derived 1:1 from `03_payment_quote.mmd`; diagram unchanged)*
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 04. Time Zone Booking
**Source:** `04_flows/04_time_zone_booking.mmd`
**User story domains:** TIME.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** (1) Learner → BookingAPI: Request local slot with IANA zone → (2) BookingAPI → BookingAPI: Detect DST gap or overlap → (3) BookingAPI → Learner: UTC slot plus local offset choices → (4) Learner → BookingAPI: Pick confirmed UTC slot → (5) BookingAPI → BookingAPI: Teacher UTC overlap lock → (6) BookingAPI → Teacher: Booked UTC and teacher local display → (7) BookingAPI → Learner: Booked UTC and learner local display *(derived 1:1 from `04_time_zone_booking.mmd`; diagram unchanged)*
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 05. Dst Ambiguity
**Source:** `04_flows/05_dst_ambiguity.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** User selects local wall time → Show valid alternatives → Show both offsets and instants → Convert to UTC → User selects one offset → Persist UTC and timezone snapshot.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 06. Video Provider Switch
**Source:** `04_flows/06_video_provider_switch.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** (1) Admin → PolicyAPI: Draft default provider and market rules → (2) PolicyAPI → PolicyAPI: Credentials health capabilities and legal preflight → (3) PolicyAPI → Admin: Impact preview and dry-run → (4) Admin → OpsApprover: Request second approval and MFA → (5) OpsApprover → PolicyAPI: Approve effective-at version → (6) PolicyAPI → Lesson: New unprovisioned lessons use new provider → (7) Lesson → Admin: Existing bound lessons unchanged *(derived 1:1 from `06_video_provider_switch.mmd`; diagram unchanged)*
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 07. Video Failover
**Source:** `04_flows/07_video_failover.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Classroom join requested → Route approved eligible provider → Use bound provider → Issue authorized join → Recovery incident and manual replacement → Authorized migration or fallback with audit.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 08. Minor Guardian Consent
**Source:** `04_flows/08_minor_guardian_consent.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Unified learner sign up → Continue placement → Collect guardian minimal contact and consent version → Restricted pending state → Enroll and schedule.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 09. Teacher Shift
**Source:** `04_flows/09_teacher_shift.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Teacher sets recurrence in IANA timezone → Project future local occurrences → Convert each occurrence to UTC → Show corrections and alternate slots → Publish availability.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 10. Academic Plan Approval
**Source:** `04_flows/10_academic_plan_approval.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** (1) Learner → Teacher: Baseline evaluation → (2) Teacher → AI: Verified rubric evidence → (3) AI → Teacher: Draft plan with provenance → (4) Teacher → Supervisor: Propose version for review → (5) Supervisor → Teacher: Approve or request change → (6) Teacher → Learner: Published verified plan *(derived 1:1 from `10_academic_plan_approval.mmd`; diagram unchanged)*
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 11. Supervisor Abac
**Source:** `04_flows/11_supervisor_abac.mmd`
**User story domains:** SUP.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Supervisor calls sensitive endpoint → 403 deny and audit → Return minimal allowed data.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 12. Competition
**Source:** `04_flows/12_competition.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Student sees competition → Explain reason and alternatives → Register and practice → Timed round using UTC deadline → Submit answers → Judging with conflicts check.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 13. Assessment Adaptive
**Source:** `04_flows/13_assessment_adaptive.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Teacher verified weaknesses → AI proposes adaptive exam blueprint → Academic reviewer checks question bank and difficulty → Student attempt with autosave and offline recovery → Teacher grades sensitive recitation answers → Update mastery and spaced reviews.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 14. Payroll
**Source:** `04_flows/14_payroll.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** (1) Attendance → Payroll: Approved lesson minutes and attendance → (2) Payroll → Payroll: Snapshot effective contract rules → (3) Payroll → Teacher: Preview statement → (4) Teacher → Payroll: Dispute if needed → (5) Payroll → Finance: Maker creates pay run → (6) Finance → Payroll: Independent approval → (7) Payroll → Teacher: Posted immutable statement *(derived 1:1 from `14_payroll.mmd`; diagram unchanged)*
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 15. Localized Notifications
**Source:** `04_flows/15_localized_notifications.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Booking UTC event → User timezone and locale preference → Quiet hours check in local zone → Schedule unique UTC notification → Localized AR or EN template → Email SMS push subject to opt in.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 16. Provider Capability Matrix
**Source:** `04_flows/16_provider_capability_matrix.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Request classroom AI or recording → Disable safely with explanation → Enable required capability.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 17. Support Incident
**Source:** `04_flows/17_support_incident.mmd`
**User story domains:** SUP.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Student reports issue → Support queue under region → Safeguarding restricted case → Operational incident → Authorized human triage and review → Resolution and optional class credit.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 18. Config Approval
**Source:** `04_flows/18_config_approval.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Admin edits settings draft → Schema and scope validation → Impact diff preview → Independent reviewer and MFA → Authorized publish → Versioned effective change.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 19. Mobile Offline
**Source:** `04_flows/19_mobile_offline.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Mobile offline → Read cached approved study data → Enter local practice draft → Encrypt local draft and queue sync → Submit idempotent versioned sync → Show merge/review with no silent overwrite.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 20. Learning Retention
**Source:** `04_flows/20_learning_retention.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Lesson approved → Mastery and revision schedule updated → Daily due practice reminder → Student attempts self review → Teacher or qualified evaluator validates → Adaptive next-week recommendation.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 21. Platform Architecture
**Source:** `04_flows/21_platform_architecture.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Web AR RTL and EN LTR → Laravel API v1 → Flutter Mobile → Admin and Supervisor → (MySQL database) → (Redis queues and cache).
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 22. Supervisor Case
**Source:** `04_flows/22_supervisor_case.mmd`
**User story domains:** SUP.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** (1) Learner → Support: Submit sensitive report → (2) Support → Safety: Scoped safeguarding case minimal details → (3) Safety → Safety: Verify purpose and evidence access → (4) Safety → Academic: Request permissible academic context → (5) Academic → Safety: Minimal authorized context → (6) Safety → Learner: Appropriate resolution notification *(derived 1:1 from `22_supervisor_case.mmd`; diagram unchanged)*
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 23. Teacher Selection
**Source:** `04_flows/23_teacher_selection.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** Learner evaluation and preferences → Available teachers with qualifications and timezones → Match level language schedule consent → Offer bookable slots and price → Reserve slot with lock → Confirm paid booking.
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.

## 24. Country Activation
**Source:** `04_flows/24_country_activation.mmd`
**User story domains:** Core + linked v1.1.
**Preconditions:** authenticated role where needed; approved market/config/payment/consent where relevant.
**Happy path:** (1) Regional → Platform: Country draft and offerings → (2) Compliance → Platform: Approve legal and privacy scope → (3) Finance → Platform: Verify PSP quote tax and merchant → (4) Platform → Platform: Sandbox e2e and dual approval → (5) Platform → Regional: Activate future effective date and audit *(derived 1:1 from `24_country_activation.mmd`; diagram unchanged)*
**Alternative/failure:** strict validation, idempotency, scope and consent fail-closed, recover with preserved transaction and clear localized UI.
**Test expectations:** AR/EN, correct currency/timezone, wrong-role authorization, replay/duplicate/concurrent requests, web/Flutter where relevant.
