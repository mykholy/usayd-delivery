# Journey walkthroughs (17 required workflows)

Status: **specification**. Screens and operations are validated against `SCREEN_INVENTORY.csv`, `openapi.yaml` and `openapi.proposed.yaml` (operations marked † are PROPOSED, not approved). Nothing here proves backend behaviour.

| # | Journey | Screens | Ops (existing / proposed) | Board | Decisions |
|---|---|---|---|---|---|
| J01 | Guest market selection → browse → level-assessment booking → registration → verified booking | 11 | 5 / 3 | UX-JR-01 | O-01, O-02 (“free” wording) |
| J02 | Minor sign-up → separate guardian session → purpose-level consent, decline, expiry, withdrawal, limited mode | 7 | 3 / 5 | UX-JR-02 | O-04, O-05, O-01 |
| J03 | Teacher application → document verification → approval → availability → learner assignment | 8 | 2 / 7 | — | O-08, O-04 (minor-facing teachers safeguarding standard) |
| J04 | Booking, cancellation and reschedule across time zones (DST gap/overlap, double booking, hold expiry, offline retry) | 8 | 4 / 3 | UX-JR-03 | O-02 (credit/forfeit policy) |
| J05 | Subscription quote → checkout → webhook → entitlement → renew/expire/refund (quote expiry, idempotency) | 5 | 6 / 2 | UX-JR-04 | O-02, O-01 |
| J06 | Classroom prejoin → device checks → in-app/external provider → incident/failover → attendance → teacher report | 10 | 8 / 1 | UX-JR-05 | O-03, O-05 |
| J07 | Teacher report draft/autosave → offline → version conflict → final submission → academic review | 5 | 2 / 2 | UX-JR-06 | — |
| J08 | Learning plan approval → daily learning → oral assessment → evidence-backed revision queue and memory map | 10 | 9 / 1 | — | O-06, O-05 (AI audio) |
| J09 | Exam start/timer → autosave → connection loss → final submit → grading/teacher review → result | 5 | 5 / 1 | — | O-06 |
| J10 | Competition enrollment → eligibility → round → judging → provisional result → appeal (independent session) → final → reward | 13 | 10 / 1 | UX-JR-07 | O-07 |
| J11 | Supervisor scoped request → out-of-scope denial → reassignment/approval with separation of duties | 5 | 6 / 2 | UX-JR-08 | D-39 |
| J12 | Admin price/config/provider change → preview/dry-run → distinct approver → activation → audit/rollback | 7 | 9 / 0 | — | O-02, O-03 |
| J13 | Mobile offline draft → encrypted queue → re-auth → reconnect/batch sync → idempotency and conflict resolution | 5 | 3 / 2 | UX-JR-09 | — |
| J14 | Notifications, quiet hours, support incident and safeguarding escalation | 7 | 4 / 4 | — | O-09, D-39 |
| J15 | Payroll: accrual → calculation → review → dual approval → disbursement/reconciliation (no invented rules) | 4 | 3 / 2 | — | O-08 |
| J16 | Market activation and locale/country/timezone independence | 8 | 6 / 1 | — | O-01, O-02 |
| J17 | Kids / Professional / Simple mode switching (presentation only; permissions unchanged) | 9 | 4 / 0 | — | D-35, D-36, D-37, Guardian PIN storage |

## J01 · Guest market selection → browse → level-assessment booking → registration → verified booking
- **Persona:** Adult guest (18+) in a launched market
- **Actors & session boundaries:** Guest (anonymous session) → same person as new learner (authenticated session). One session boundary at sign-up; the slot hold survives it by hold_id.
- **Entry:** Guest opens the site with no account.
- **Exit:** Booking `confirmed` and visible in the learner calendar, or the guest leaves with a released hold.
- **Screens:** `UX-PUBLIC-001` → `UX-GLOB-001` → `UX-PUBLIC-002` → `UX-PUBLIC-003` → `UX-PUBLIC-005` → `UX-PUBLIC-006` → `UX-PUBLIC-009` → `UX-GLOB-005` → `UX-AUTH-001` → `UX-AUTH-005` → `UX-LEARNER-007`
- **API:** `get__api_v1_public_markets`, `get__programs`, `getPublicTeacher`†, `get__api_v1_booking_available_slots`, `createSlotHold`†, `post__auth_register`, `post_bookings`, `joinMarketWaitlist`†
- **RBAC/ABAC:** Public reads are market-limited (FR-GEO-004); slot hold is anonymous but rate-limited and bound to a device/session; booking requires the authenticated learner who owns the hold.
- **Happy path:**
  1. Guest picks a country (storefront only; IP is a hint, FR-GEO-001) and city when the country has several zones (FR-GEO-012).
  2. Browses programs and published teacher profiles for that market.
  3. Opens free assessment booking; available slots are shown in the guest’s IANA zone with the UTC instant underneath.
  4. Chooses a slot → `createSlotHold` returns hold_id + expires_at (TTL `booking.slot_hold_minutes`).
  5. Signs up (email/phone verification); age band = adult.
  6. Booking is created with hold_id + Idempotency-Key → `confirmed`; confirmation + 24 h/1 h reminders scheduled in the learner’s zone.
- **Alternate paths:**
  - Country not launched → UX-GLOB-003 waitlist (adult contact + marketing consent) or choose another country.
  - Local time ambiguous (DST overlap) → learner picks earlier/later offset before the hold; time in a DST gap → 422 DST_GAP, pick another slot.
- **Denial / error:**
  - Age band under 18 → stop and branch to J02 before any booking is confirmed.
  - Market paused (FR-GEO-011) → no new holds; existing bookings honoured.
- **Timeout / network loss:**
  - Hold request times out → retry with the same Idempotency-Key; never creates two holds.
  - Hold expires during sign-up → booking returns 409 HOLD_EXPIRED; UI re-opens the slot picker with the same filters.
- **Double-click / idempotency:** createSlotHold and post_bookings require Idempotency-Key; double-click on “Confirm” shows one booking.
- **Empty state:** No slots this week → show next available week + waitlist (FR-BOOK-006), never an empty grid without guidance.
- **Recovery:** Abandoned hold auto-expires and releases the teacher slot; guest can resume from the program page.
- **Audit events:** `booking.slot_held`, `auth.registered`, `booking.created`
- **Notifications:** Booking confirmation (email/SMS by consent); Reminders 24 h / 1 h (FR-NOTIF-002)
- **FR:** FR-GEO-001, FR-GEO-002, FR-GEO-004, FR-GEO-012, FR-BOOK-001, FR-BOOK-002, FR-BOOK-007, FR-IAM-001, FR-IAM-002, FR-NOTIF-002
- **Source flows:** F01, F03, 01, 23
- **Owner decisions:** O-01, O-02 (“free” wording)
- **Acceptance:** `acceptance/J01.feature` (3 scenarios)

## J02 · Minor sign-up → separate guardian session → purpose-level consent, decline, expiry, withdrawal, limited mode
- **Persona:** Minor learner (13–17 or under 13) and a guardian
- **Actors & session boundaries:** Minor (own session) · Guardian (separate token session on their own device; never inside the minor’s session) · Safeguarding/admin (consent queue).
- **Entry:** Sign-up yields an age band under 18 (FR-IAM-002).
- **Exit:** Per-purpose consent recorded (granted or declined) with policy versions; account in full or limited mode accordingly.
- **Screens:** `UX-AUTH-001` → `UX-AUTH-002` → `UX-PUBLIC-012` → `UX-AUTH-005` → `UX-LEARNER-001` → `UX-LEARNER-032` → `UX-ADMIN-004`
- **API:** `post__auth_register`, `createGuardianInvitation`†, `getGuardianInvitation`†, `decideGuardianConsent`†, `post__consents`, `post__consents__consentId__withdraw`, `getLegalDocument`†, `listAdminConsents`†
- **RBAC/ABAC:** Minor can only invite; only the token-bound guardian can decide; admins can view the queue in their market but cannot grant on behalf of a guardian.
- **Happy path:**
  1. Minor signs up with minimum data; account starts in **limited mode** (no paid learning, no recording, no competitions, no AI audio).
  2. Minor enters guardian contact → invitation with purposes (lessons, recording, competitions, ai_processing) and expiry.
  3. Guardian opens the link in their own session, reads versioned legal text, completes verification (**method = O-04**).
  4. Guardian grants or declines **each purpose separately**; each creates a consent receipt with policy version.
  5. Minor’s account unlocks only the granted purposes.
- **Alternate paths:**
  - Guardian declines lessons → account stays limited; minor sees a calm explanation and support contact.
  - Guardian grants lessons but not recording → recording toggles stay off and disabled with the reason.
- **Denial / error:**
  - Minor tries to open the guardian link in their own session → token is bound to the guardian flow; decision endpoint rejects learner tokens.
  - Admin attempts to grant → not possible; only view + resend.
- **Timeout / network loss:**
  - Guardian decision request lost → retry with same Idempotency-Key; receipt not duplicated.
  - Invitation expired → 410; minor can resend (rate-limited).
- **Double-click / idempotency:** decideGuardianConsent idempotent per invitation + purpose; regrant after withdrawal creates a **new** receipt (never overwrites).
- **Empty state:** No guardian contact yet → limited mode with one clear action: invite guardian.
- **Recovery:** Withdrawal at any time by the guardian → affected features stop at the next request; scheduled lessons follow the cancellation policy.
- **Audit events:** `guardian_invitation.sent`, `consent.recorded`, `consent.withdrawn`
- **Notifications:** Invitation (guardian channel); Decision outcome to the minor (neutral wording); Expiry reminder before expiry
- **FR:** FR-IAM-002, FR-IAM-006, FR-IAM-007, FR-PROF-005, FR-SEC-005
- **Source flows:** F03, 08
- **Owner decisions:** O-04, O-05, O-01
- **Acceptance:** `acceptance/J02.feature` (4 scenarios)

## J03 · Teacher application → document verification → approval → availability → learner assignment
- **Persona:** Teacher applicant
- **Actors & session boundaries:** Applicant (own session) · Academic supervisor (interview + decision) · Safeguarding lead (check) · Ops supervisor (assignment). Decider ≠ interviewer.
- **Entry:** Authenticated user opens the teacher application.
- **Exit:** Teacher `active` with published availability and at least one assigned learner — or a recorded rejection.
- **Screens:** `UX-TEACHER-001` → `UX-ADMIN-006` → `UX-ADMIN-008` → `UX-ADMIN-009` → `UX-TEACHER-003` → `UX-GLOB-008` → `UX-ADMIN-003` → `UX-TEACHER-008`
- **API:** `createUpload`†, `submitTeacherApplication`†, `listTeacherApplications`†, `decideTeacherApplication`†, `getAdminTeacher`†, `post__admin_teachers__teacherId__contracts`, `put__api_v1_teacher_me_availability_rules`, `assignTeacher`†, `listMyLearners`†
- **RBAC/ABAC:** Applicant sees only their application; documents are private objects with signed URLs; safeguarding check visible only to safeguarding role; contracts need finance role (O-08).
- **Happy path:**
  1. Applicant uploads documents (scan → clean) and submits languages, areas, riwayat.
  2. Credentials review → recitation interview → safeguarding check (cleared).
  3. A different academic supervisor approves → employment state `approved`.
  4. Contract version created (blocked by O-08 for pay terms) → state `active`.
  5. Teacher publishes weekly availability in their IANA zone (RRULE + tzdb version).
  6. Ops assigns learners; teacher sees them in My learners.
- **Alternate paths:**
  - Document removed by malware scan → applicant re-uploads; application stays `submitted`.
  - Supervisor requests changes → application returns to applicant with reasons.
- **Denial / error:**
  - Safeguarding not cleared → approve returns 409 SAFEGUARDING_NOT_CLEARED.
  - Interviewer tries to approve own interview → 403 SELF_DECISION_FORBIDDEN.
- **Timeout / network loss:**
  - Upload interrupted → resumable signed upload; submit disabled until all scans are clean.
- **Double-click / idempotency:** submit and decision require Idempotency-Key; one open application per user (409).
- **Empty state:** No applications → recruitment board shows stages with zero counts and the public careers link (owner content).
- **Recovery:** Suspended teacher (FR-TCHR-005) loses access immediately; future lessons go to reassignment (J04/J06).
- **Audit events:** `teacher_application.submitted`, `teacher_application.decided`, `teacher.contract_created`, `learner.teacher_assigned`
- **Notifications:** Application status changes to applicant; Assignment notice to teacher and learner
- **FR:** FR-TCHR-001, FR-TCHR-002, FR-TCHR-003, FR-TCHR-004, FR-TCHR-005, FR-MEDIA-003, FR-SEC-002
- **Source flows:** 09, 23
- **Owner decisions:** O-08, O-04 (minor-facing teachers safeguarding standard)
- **Acceptance:** `acceptance/J03.feature` (2 scenarios)

## J04 · Booking, cancellation and reschedule across time zones (DST gap/overlap, double booking, hold expiry, offline retry)
- **Persona:** Learner and teacher in different zones
- **Actors & session boundaries:** Learner (own session) · Teacher (own session) · Ops supervisor for conflicts.
- **Entry:** Learner opens booking with an active entitlement.
- **Exit:** Lesson confirmed / rescheduled / cancelled with the credit outcome recorded.
- **Screens:** `UX-LEARNER-008` → `UX-GLOB-005` → `UX-LEARNER-009` → `UX-GLOB-009` → `UX-LEARNER-007` → `UX-TEACHER-004` → `UX-ADMIN-015` → `UX-ADMIN-010`
- **API:** `get__api_v1_booking_available_slots`, `createSlotHold`†, `post_bookings`, `post__bookings__bookingId__reschedule`, `post__api_v1_lessons_lessonId_reschedule_request`, `cancelBooking`†, `listAdminBookings`†
- **RBAC/ABAC:** Only participants or scoped ops may reschedule/cancel; teacher overlap lock is server-side and transactional (FR-BOOK-001).
- **Happy path:**
  1. Learner sees slots in their zone with the teacher’s local time on hover.
  2. Hold → confirm (UTC stored + both IANA zones + tzdb version).
  3. Reschedule inside the window → teacher approval → new slot confirmed, history kept.
  4. Cancel inside the window → credit returned.
- **Alternate paths:**
  - Overlap (clocks go back) → learner must choose earlier/later; both shown with offsets.
  - Gap (clocks go forward) → slot rejected 422 DST_GAP; nearest valid slots suggested. Never auto-shifted.
  - Teacher off-shift clash → ops sees it in the conflict lane (UX-ADMIN-015).
- **Denial / error:**
  - Cancellation outside the window → 409 OUTSIDE_CANCELLATION_WINDOW; outcome per policy (O-02).
  - Non-participant tries to cancel → 404 (non-revealing).
- **Timeout / network loss:**
  - Two learners hold the same slot → second gets 409 SLOT_TAKEN.
  - Offline on mobile → booking actions are disabled (not queued); retry when online.
  - Timeout on confirm → retry with same key; never two lessons.
- **Double-click / idempotency:** All writes keyed; reschedule request is idempotent per lesson + target slot.
- **Empty state:** No availability in range → suggest wider range or waitlist.
- **Recovery:** Expired holds release automatically; failed confirm leaves no partial lesson (transaction + outbox).
- **Audit events:** `booking.slot_held`, `booking.created`, `booking.rescheduled`, `booking.cancelled`
- **Notifications:** Changes to both parties in their own zone and language
- **FR:** FR-BOOK-001, FR-BOOK-003, FR-BOOK-004, FR-BOOK-006, FR-BOOK-007, FR-TIME-004, FR-TIME-005, FR-TIME-006, FR-PROF-003
- **Source flows:** F05, F06, 04, 05
- **Owner decisions:** O-02 (credit/forfeit policy)
- **Acceptance:** `acceptance/J04.feature` (3 scenarios)

## J05 · Subscription quote → checkout → webhook → entitlement → renew/expire/refund (quote expiry, idempotency)
- **Persona:** Adult learner (payer)
- **Actors & session boundaries:** Learner (own session) · PSP (signed webhooks) · Finance (refund approval).
- **Entry:** Learner chooses a package in their market.
- **Exit:** Subscription ACTIVE with entitlement, or PENDING/EXPIRED with a clear next step; refunds recorded in ledger.
- **Screens:** `UX-GLOB-002` → `UX-GLOB-006` → `UX-LEARNER-029` → `UX-GLOB-007` → `UX-ADMIN-019`
- **API:** `get__packages`, `post__api_v1_me_checkout_quotes`, `post__api_v1_me_payment_checkouts`, `post__webhooks_payments__provider`, `get__payments__paymentId`, `get__subscriptions`, `setRenewalConsent`†, `requestRefund`†
- **RBAC/ABAC:** Payer owns quote/payment; finance approves refunds; nobody activates entitlement except the verified webhook handler.
- **Happy path:**
  1. Quote = immutable amount_minor + currency + tax + expiry from the market price book (no FX conversion).
  2. Checkout with Idempotency-Key → PSP intent.
  3. Signed webhook verified + deduplicated → payment captured → subscription ACTIVE + entitlement.
  4. Renewal: explicit consent only (FR-PAY-006); price change notice before renewal (UX-GLOB-007).
- **Alternate paths:**
  - Quote expired → 409 QUOTE_EXPIRED; new quote shown with any price change highlighted.
  - Webhook arrives before redirect → UI polls payment and shows ACTIVE.
  - Webhook out of order → state machine ignores stale transitions.
- **Denial / error:**
  - Redirect “success” without webhook → UI shows “pending confirmation”, never “paid”.
  - Three-decimal currency (KWD/BHD/OMR) → displayed and stored with exponent 3.
- **Timeout / network loss:**
  - Lost response after checkout → retry same key returns same intent.
  - PSP outage → checkout disabled with status; no partial subscription.
- **Double-click / idempotency:** Quote, checkout and refund requests keyed; webhooks deduplicated by provider event id.
- **Empty state:** No package in market → unavailable notice + waitlist.
- **Recovery:** Refund: request → approval → PSP refund in original currency/amount (FR-GEO-015) → ledger compensation; subscription REFUND_PENDING → (PARTIALLY_)REFUNDED.
- **Audit events:** `quote.created`, `payment.captured`, `subscription.activated`, `refund.requested`, `refund.settled`
- **Notifications:** Receipt/invoice; Renewal reminders (graded); Refund status
- **FR:** FR-PAY-001, FR-PAY-002, FR-PAY-003, FR-PAY-004, FR-PAY-005, FR-PAY-006, FR-GEO-005, FR-GEO-006, FR-GEO-007, FR-GEO-015
- **Source flows:** F01, F04, 03
- **Owner decisions:** O-02, O-01
- **Acceptance:** `acceptance/J05.feature` (3 scenarios)

## J06 · Classroom prejoin → device checks → in-app/external provider → incident/failover → attendance → teacher report
- **Persona:** Learner + teacher in a live lesson
- **Actors & session boundaries:** Learner, teacher (separate sessions) · Video provider (webhooks) · Ops (incident console).
- **Entry:** Join window opens (setting `booking.join_window_minutes`).
- **Exit:** Lesson COMPLETED with attendance summary, or INTERRUPTED → reschedule/compensation.
- **Screens:** `UX-LEARNER-009` → `UX-VPC-009` → `UX-LEARNER-010` → `UX-TEACHER-005` → `UX-TEACHER-006` → `UX-VPC-010` → `UX-VPC-008` → `UX-ADMIN-016` → `UX-ADMIN-018` → `UX-TEACHER-007`
- **API:** `get__lessons__lessonId`, `get__conferences__conferenceId__capabilities`, `post__lessons__lessonId__join`, `post__webhooks_video__provider`, `get__api_v1_admin_video_incidents`, `post__api_v1_admin_video_incidents_incidentId_recover`, `listAdminLessons`†, `postAttendanceDispute`, `post__lessons__lessonId__report`
- **RBAC/ABAC:** Join tokens only for participants, only inside the window; recording/AI capabilities only when provider-verified AND consented (flow 16).
- **Happy path:**
  1. Prejoin: camera/mic permission, network check, provider shown.
  2. Join → provider-bound session (binding never changes silently).
  3. Provider events build attendance chunks (join/leave/reconnect).
  4. End → attendance summary → teacher report.
- **Alternate paths:**
  - External meeting provider → open external link; attendance from provider events where supported, else teacher attestation.
  - Device permission denied → audio-only path explained.
- **Denial / error:**
  - Join before window → 409 with time remaining.
  - Recording requested without consent → capability disabled with reason.
- **Timeout / network loss:**
  - Learner disconnect → INTERRUPTED chunk; rejoin keeps the same binding.
  - Provider outage before start → authorized fallback with audit; during class → incident + manual replacement → reschedule/refund path.
- **Double-click / idempotency:** Join returns a fresh short-lived token per call; attendance dispute keyed per lesson.
- **Empty state:** —
- **Recovery:** Incident console records recovery; affected lessons flagged for compensation (FR-ATT-005).
- **Audit events:** `lesson.joined`, `conference.event`, `video.incident_opened`, `video.incident_recovered`, `attendance.disputed`
- **Notifications:** Join reminders; Incident notice with next steps
- **FR:** FR-VIDEO-001, FR-ATT-001, FR-ATT-002, FR-ATT-005, FR-VPC-008, FR-BOOK-008, FR-MEDIA-004
- **Source flows:** F08, F13, 06, 07, 16
- **Owner decisions:** O-03, O-05
- **Acceptance:** `acceptance/J06.feature` (2 scenarios)

## J07 · Teacher report draft/autosave → offline → version conflict → final submission → academic review
- **Persona:** Teacher
- **Actors & session boundaries:** Teacher (web or mobile session) · Academic supervisor (review).
- **Entry:** Lesson COMPLETED or teacher opens report within the report window.
- **Exit:** Report submitted (immutable) and visible to learner; or returned for correction with history.
- **Screens:** `UX-TEACHER-007` → `UX-MOBILE-010` → `UX-TEACHER-009` → `UX-LEARNER-011` → `UX-SUP-002`
- **API:** `saveLessonReportDraft`†, `post__lessons__lessonId__report`, `getLessonReport`, `submitSyncBatch`†
- **RBAC/ABAC:** Only the lesson’s teacher writes the draft; supervisors read within scope; learner sees only the submitted report.
- **Happy path:**
  1. Teacher writes; draft autosaves (If-Match version).
  2. Required fields (goal, revision, homework, result or absence reason) validated (FR-ATT-003).
  3. Submit → report immutable; learner notified.
- **Alternate paths:**
  - Edited on web and mobile → second save gets 412 with the server draft; teacher merges field-by-field.
  - Absent learner → absence reason replaces result.
- **Denial / error:**
  - Another teacher opens the report → 404.
  - Submit after window → requires supervisor reopen (audited).
- **Timeout / network loss:**
  - Offline on mobile → draft encrypted in the device queue; synced by J13.
  - Submit timeout → retry with same key.
- **Double-click / idempotency:** Final submit keyed; drafts versioned.
- **Empty state:** No lessons to report → “all reports done” state.
- **Recovery:** Corrections create a new version with reason; original kept.
- **Audit events:** `lesson_report.submitted`, `lesson_report.reopened`
- **Notifications:** Learner: report available
- **FR:** FR-ATT-003, FR-MOB-004, FR-ASMT-002
- **Source flows:** F13, F12, 19
- **Owner decisions:** none
- **Acceptance:** `acceptance/J07.feature` (2 scenarios)

## J08 · Learning plan approval → daily learning → oral assessment → evidence-backed revision queue and memory map
- **Persona:** Learner + teacher + academic supervisor
- **Actors & session boundaries:** Teacher proposes · AI drafts (advisory, provenance) · Supervisor approves · Learner studies (own session).
- **Entry:** Initial assessment done.
- **Exit:** Active plan; daily tasks and revision queue driven by teacher-verified evidence.
- **Screens:** `UX-LEARNER-004` → `UX-TEACHER-010` → `UX-TEACHER-011` → `UX-SUP-002` → `UX-LEARNER-012` → `UX-LEARNER-013` → `UX-LEARNER-014` → `UX-LEARNER-015` → `UX-LEARNER-016` → `UX-LEARNER-028`
- **API:** `post__assessments`, `post__assessments__assessmentId__approve`, `post__learning_plans_suggestions`, `patchLearningPlanDraft`, `post__api_v1_supervisor_academic_plans_planId_decision`, `post__learning_plans__planId__approve`, `get__revision_tasks`, `post__revision_tasks__taskId__evidence`, `get__memory_map`, `listLibraryItems`†
- **RBAC/ABAC:** AI output starts as `proposed` and is never shown as a final grade; only teacher/supervisor approve; learner sees approved versions only.
- **Happy path:**
  1. Teacher records assessment evidence (0–4 rubric).
  2. AI suggests a plan draft with provenance and uncertainty → teacher edits → supervisor approves.
  3. Learner gets daily wird and revision tasks; submits evidence.
  4. Teacher-verified evidence updates the memory map and spaced reviews.
- **Alternate paths:**
  - Supervisor requests changes → plan back to teacher with comments.
  - AI disabled (policy or consent) → manual plan path.
- **Denial / error:**
  - Learner tries to approve own plan → 403.
  - AI attempts to generate Quran text → blocked; references only to the licensed corpus (O-06).
- **Timeout / network loss:**
  - Evidence recorded offline → queued (J13).
- **Double-click / idempotency:** Evidence submission keyed per task.
- **Empty state:** New learner → plan pending notice; no fake progress.
- **Recovery:** Plan versions superseded, never edited in place.
- **Audit events:** `assessment.approved`, `plan.proposed`, `plan.approved`, `revision.evidence_recorded`
- **Notifications:** Plan approved; Review due (respecting quiet hours)
- **FR:** FR-ASMT-001, FR-ASMT-002, FR-PLAN-001, FR-PLAN-002, FR-PLAN-003, FR-AI-001, FR-CURR-003, FR-CURR-004, FR-NOTIF-003
- **Source flows:** F09, F14, 10, 13, 20
- **Owner decisions:** O-06, O-05 (AI audio)
- **Acceptance:** `acceptance/J08.feature` (2 scenarios)

## J09 · Exam start/timer → autosave → connection loss → final submit → grading/teacher review → result
- **Persona:** Learner
- **Actors & session boundaries:** Learner (own session) · Teacher (grading of recitation answers).
- **Entry:** Learner starts an available exam.
- **Exit:** Result published after review; appeal possible per FR-ASMT-006.
- **Screens:** `UX-LEARNER-017` → `UX-LEARNER-018` → `UX-MOBILE-007` → `UX-LEARNER-019` → `UX-TEACHER-010`
- **API:** `get__exams`, `post__exams__examId__attempts`, `postExamCheckpoint`, `getExamAttempt`, `post__exam_attempts__attemptId__submit`, `submitSyncBatch`†
- **RBAC/ABAC:** Attempt owned by learner; server-authoritative timer; graders scoped to assigned learners.
- **Happy path:**
  1. Start → server deadline returned.
  2. Answers checkpointed every change.
  3. Submit → under_review → graded → result published.
- **Alternate paths:**
  - Timer ends → server auto-submits last checkpoint.
  - Recitation answers → teacher grading queue.
- **Denial / error:**
  - Second concurrent attempt → 409.
  - Retake outside policy → 409 with next allowed time.
- **Timeout / network loss:**
  - Connection lost → answers kept locally; checkpoint resumes; server deadline unchanged.
  - Submit after deadline offline → server keeps the last checkpoint before deadline.
- **Double-click / idempotency:** Checkpoints carry sequence numbers; submit keyed.
- **Empty state:** No exams available → explain when the next one opens.
- **Recovery:** Crash → reopen attempt from last checkpoint.
- **Audit events:** `exam.attempt_started`, `exam.submitted`, `exam.graded`
- **Notifications:** Result available
- **FR:** FR-ASMT-003, FR-ASMT-005, FR-ASMT-006, FR-ASMT-007
- **Source flows:** F18, 13
- **Owner decisions:** O-06
- **Acceptance:** `acceptance/J09.feature` (2 scenarios)

## J10 · Competition enrollment → eligibility → round → judging → provisional result → appeal (independent session) → final → reward
- **Persona:** Learner entrant, judges, independent reviewer
- **Actors & session boundaries:** Entrant (own session) · Judge (own session) · Independent appeal reviewer (different person, own session) · Moderator.
- **Entry:** Competition registration_open.
- **Exit:** Results finalized; rewards issued only after legal review (O-07).
- **Screens:** `UX-LEARNER-020` → `UX-LEARNER-021` → `UX-LEARNER-022` → `UX-LEARNER-023` → `UX-LEARNER-024` → `UX-LEARNER-025` → `UX-TEACHER-014` → `UX-TEACHER-015` → `UX-ADMIN-028` → `UX-ADMIN-029` → `UX-ADMIN-030` → `UX-ADMIN-031` → `UX-SUP-005`
- **API:** `getContestEligibility`, `post__competitions__competitionId__register`, `getCompetitionRound`, `post__competitions__competitionId__submissions`, `assignCompetitionJudges`†, `post__competition_submissions__submissionId__judge`, `getCompetitionResult`, `post__competition_results__resultId__appeal`, `getAdminContestAppeals`, `postAdminContestAppealResolve`, `post__admin_competitions__competitionId__publish`
- **RBAC/ABAC:** Judges never judge their own learners (conflict check); reviewer ≠ original judge; minors never on public leaderboards (FR-CONTEST-009).
- **Happy path:**
  1. Eligibility check (age/level/subscription/consent).
  2. Register → round → submission.
  3. Two judges for finals → provisional results → appeal window.
  4. Appeals resolved by independent reviewer → finalized → (rewards after O-07).
- **Alternate paths:**
  - Appeal upheld → new score version; ranking recalculated.
  - Minor entrant → private result only.
- **Denial / error:**
  - Ineligible → reason shown; no paid “extra chances” (FR-CONTEST-014).
  - Reviewer = judge → 403/409 independence conflict.
- **Timeout / network loss:**
  - Submission upload resumes.
- **Double-click / idempotency:** Register and submit keyed.
- **Empty state:** No competitions → upcoming list.
- **Recovery:** Cancelled competition → public notice and reason.
- **Audit events:** `competition.registered`, `competition.judged`, `competition.appeal_resolved`, `competition.published`
- **Notifications:** Result + appeal window; Appeal outcome
- **FR:** FR-CONTEST-002, FR-CONTEST-003, FR-CONTEST-008, FR-CONTEST-009, FR-CONTEST-010, FR-CONTEST-011, FR-CONTEST-014, FR-ENG-003
- **Source flows:** F10, 12
- **Owner decisions:** O-07
- **Acceptance:** `acceptance/J10.feature` (2 scenarios)

## J11 · Supervisor scoped request → out-of-scope denial → reassignment/approval with separation of duties
- **Persona:** Supervisor + platform admin
- **Actors & session boundaries:** Supervisor (scoped session) · Second admin (approver).
- **Entry:** Supervisor opens a record.
- **Exit:** Either worked within scope, or reassigned via an approved assignment; all audited.
- **Screens:** `UX-SUP-001` → `UX-SUP-002` → `UX-SUP-008` → `UX-SUP-009` → `UX-ADMIN-002`
- **API:** `get__api_v1_supervisor_queues`, `post__api_v1_supervisor_academic_plans_planId_decision`, `get__api_v1_admin_supervisor_assignments`, `post__api_v1_admin_supervisor_assignments`, `post__api_v1_admin_supervisor_assignments_assignmentId_revoke`, `get__api_v1_admin_security_access_audits`, `postAccessAuditReview`†, `listAdminLearners`†
- **RBAC/ABAC:** ABAC market/program scope on every read and write; out-of-scope = non-revealing 404/403; no self-grant; second admin approves new assignments.
- **Happy path:**
  1. Supervisor works items in scope.
  2. Needs another market → asks an admin (out-of-band); admin creates assignment → second admin approves → active.
- **Alternate paths:**
  - Assignment with end date → auto-expires.
- **Denial / error:**
  - Out-of-scope record → “isn’t available in your scope”, no details.
  - Admin grants self → 403.
  - Reviewer reviews own access → 403 SELF_REVIEW_FORBIDDEN.
- **Timeout / network loss:**
  - Offline → queues read-only.
- **Double-click / idempotency:** Assignment creation keyed.
- **Empty state:** Empty queue → “nothing waiting in your scope”.
- **Recovery:** Revocation immediate.
- **Audit events:** `supervisor_assignment.created`, `supervisor_assignment.approved`, `supervisor_assignment.revoked`, `access_audit.reviewed`
- **Notifications:** Assignment changes to the supervisor
- **FR:** FR-SUP-001, FR-SUP-002, FR-SUP-009, FR-IAM-004, FR-SEC-001
- **Source flows:** F11, 11
- **Owner decisions:** D-39
- **Acceptance:** `acceptance/J11.feature` (2 scenarios)

## J12 · Admin price/config/provider change → preview/dry-run → distinct approver → activation → audit/rollback
- **Persona:** Admin maker + approver
- **Actors & session boundaries:** Maker (admin) · Checker (different admin, MFA) · System (effective-at activation).
- **Entry:** Maker drafts a change.
- **Exit:** Version active at effective date, or rejected/rolled back with audit.
- **Screens:** `UX-GLOB-012` → `UX-GLOB-013` → `UX-SUP-010` → `UX-VPC-004` → `UX-VPC-005` → `UX-VPC-006` → `UX-ADMIN-041`
- **API:** `post__api_v1_admin_price_books`, `post__api_v1_admin_price_books_priceBookId_decision`, `post__api_v1_admin_settings_drafts`, `post__api_v1_admin_settings_versions_settingsVersionId_decision`, `post__api_v1_admin_video_routing_policies`, `post__api_v1_admin_video_routing_policies_policyId_dry_run`, `post__api_v1_admin_video_routing_policies_policyId_decision`, `post__api_v1_admin_video_routing_policies_policyId_activate`, `post__api_v1_admin_video_routing_policies_policyId_rollback`
- **RBAC/ABAC:** Maker ≠ checker; MFA step-up for financial/safeguarding keys; existing bound lessons unaffected by provider switch.
- **Happy path:**
  1. Draft → impact preview / dry-run.
  2. Second admin approves with MFA.
  3. Activates at effective time (future-dated).
  4. Rollback creates a new version pointing to the prior one.
- **Alternate paths:**
  - Approver rejects with reason → draft returns.
- **Denial / error:**
  - Maker approves own draft → 403 SELF_APPROVAL_FORBIDDEN.
- **Timeout / network loss:**
  - Activation job retries idempotently.
- **Double-click / idempotency:** Decisions keyed; activation idempotent per version.
- **Empty state:** No pending drafts.
- **Recovery:** Rollback.
- **Audit events:** `settings.drafted`, `settings.approved`, `price_book.approved`, `routing_policy.activated`, `routing_policy.rolled_back`
- **Notifications:** Approver notified of pending change
- **FR:** FR-ADMIN-004, FR-GEO-005, FR-GEO-010, FR-VPC-001, FR-VPC-006, FR-SUP-011
- **Source flows:** F07, F16, 06, 18, 24
- **Owner decisions:** O-02, O-03
- **Acceptance:** `acceptance/J12.feature` (2 scenarios)

## J13 · Mobile offline draft → encrypted queue → re-auth → reconnect/batch sync → idempotency and conflict resolution
- **Persona:** Learner/teacher on Flutter
- **Actors & session boundaries:** User (device session) · Sync service.
- **Entry:** Device goes offline with queued work.
- **Exit:** Every queued item applied, deduplicated, or surfaced as a conflict for the user.
- **Screens:** `UX-MOBILE-002` → `UX-MOBILE-007` → `UX-MOBILE-010` → `UX-MOBILE-000` → `UX-MOBILE-001`
- **API:** `post__auth_refresh`, `submitSyncBatch`†, `saveLessonReportDraft`†, `postExamCheckpoint`, `post__revision_tasks__taskId__evidence`
- **RBAC/ABAC:** Each item re-authorized server-side at sync time (ownership may have changed while offline).
- **Happy path:**
  1. Allowed offline: evidence, report drafts, exam checkpoints (never payments/bookings/approvals).
  2. Queue encrypted at rest on device.
  3. On reconnect: refresh token → batch sync → per-item outcome.
- **Alternate paths:**
  - Refresh token expired → re-login, queue kept.
  - Conflict → user picks version.
- **Denial / error:**
  - Item no longer owned → rejected with reason; local copy kept for export to support.
- **Timeout / network loss:**
  - Partial batch → per-item results; retries only failed items.
- **Double-click / idempotency:** client_id per item; duplicates return `duplicate`.
- **Empty state:** Nothing queued → no banner.
- **Recovery:** Queue survives app restart; never silently dropped.
- **Audit events:** `sync.batch_applied`
- **Notifications:** In-app sync summary
- **FR:** FR-MOB-002, FR-MOB-004, FR-IAM-008
- **Source flows:** F12, 19
- **Owner decisions:** none
- **Acceptance:** `acceptance/J13.feature` (2 scenarios)

## J14 · Notifications, quiet hours, support incident and safeguarding escalation
- **Persona:** Learner, support agent, safeguarding lead
- **Actors & session boundaries:** Learner · Support agent · Safeguarding lead (restricted) · Academic (minimal context).
- **Entry:** Notification due, or learner reports a problem.
- **Exit:** Notification delivered per preferences; ticket resolved or safeguarding case handled with minimal data.
- **Screens:** `UX-LEARNER-030` → `UX-LEARNER-031` → `UX-ADMIN-035` → `UX-ADMIN-036` → `UX-SUP-004` → `UX-ADMIN-038` → `UX-GLOB-004`
- **API:** `listMyNotifications`†, `markNotificationsRead`†, `patch__api_v1_me_preferences`, `post__support_tickets`, `listMySupportTickets`†, `get__api_v1_supervisor_safeguarding_cases`, `post__api_v1_supervisor_safeguarding_cases`, `postBreakGlassGrant`†
- **RBAC/ABAC:** Safety channel separate from marketing (FR-NOTIF-004); safeguarding data only to assigned officers; break-glass is proposed (D-39).
- **Happy path:**
  1. Reminders respect quiet hours in the user’s zone; safety notices bypass quiet hours.
  2. Learner opens a ticket → agent resolves.
  3. Sensitive report → safeguarding case with minimal details → resolution notice.
- **Alternate paths:**
  - Channel not consented → in-app only.
- **Denial / error:**
  - Agent opens a safeguarding case → non-revealing 403.
- **Timeout / network loss:**
  - Push token invalid → fallback channel.
- **Double-click / idempotency:** Ticket creation keyed.
- **Empty state:** No notifications → calm empty state.
- **Recovery:** Escalation ladder with SLA (O-09).
- **Audit events:** `support.ticket_created`, `safeguarding.case_opened`, `break_glass.granted`
- **Notifications:** Graded safety notification to authorized team
- **FR:** FR-NOTIF-001, FR-NOTIF-002, FR-NOTIF-004, FR-I18N-005, FR-ADMIN-006, FR-SUP-004
- **Source flows:** 15, 17, 22, F17
- **Owner decisions:** O-09, D-39
- **Acceptance:** `acceptance/J14.feature` (2 scenarios)

## J15 · Payroll: accrual → calculation → review → dual approval → disbursement/reconciliation (no invented rules)
- **Persona:** Finance maker + checker, teacher
- **Actors & session boundaries:** Payroll system · Finance maker · Finance checker (different person) · Teacher (dispute).
- **Entry:** Period closes with approved attendance.
- **Exit:** Pay run reconciled; statements immutable; disputes recorded.
- **Screens:** `UX-ADMIN-021` → `UX-ADMIN-022` → `UX-TEACHER-016` → `UX-ADMIN-009`
- **API:** `listPayRuns`†, `post__admin_pay_runs__payRunId__approve`, `get__teachers_me_pay_statements`, `getCompensationPreview`, `disputePayStatement`†
- **RBAC/ABAC:** Maker ≠ checker; teachers see own statements only.
- **Happy path:**
  1. Accruals from approved attendance (rules = contract version, **O-08**).
  2. Maker prepares run → checker approves → payout → reconciliation.
- **Alternate paths:**
  - Teacher disputes a line → adjustment in next run (never edit a paid payout).
- **Denial / error:**
  - Self-approval → 403.
  - Unreviewed rule → calculation blocked (FR-PAYROLL-007).
- **Timeout / network loss:**
  - Approval keyed.
- **Double-click / idempotency:** Approve keyed.
- **Empty state:** No run for period.
- **Recovery:** Compensating adjustment.
- **Audit events:** `payroll.run_prepared`, `payroll.run_approved`, `payroll.dispute_opened`
- **Notifications:** Statement available
- **FR:** FR-PAYROLL-001, FR-PAYROLL-002, FR-PAYROLL-007, FR-PAYROLL-008, FR-PAYROLL-009
- **Source flows:** F15, 14
- **Owner decisions:** O-08
- **Acceptance:** `acceptance/J15.feature` (1 scenarios)

## J16 · Market activation and locale/country/timezone independence
- **Persona:** Regional manager, compliance, finance; any learner
- **Actors & session boundaries:** Regional manager · Compliance · Finance · Platform (dual approval).
- **Entry:** Country draft.
- **Exit:** Market active at a future effective date; language switch never changes price, currency or timezone.
- **Screens:** `UX-GLOB-010` → `UX-GLOB-011` → `UX-GLOB-012` → `UX-GLOB-013` → `UX-GLOB-014` → `UX-GLOB-004` → `UX-GLOB-017` → `UX-GLOB-003`
- **API:** `get__api_v1_admin_markets`, `post__api_v1_admin_markets`, `post__api_v1_admin_markets_marketId_decision`, `get__api_v1_admin_legal_market_readiness`, `get__api_v1_admin_payment_merchant_profiles`, `patch__api_v1_me_preferences`, `joinMarketWaitlist`†
- **RBAC/ABAC:** Compliance + finance approvals required (FR-GEO-010).
- **Happy path:**
  1. Draft → legal/privacy approval → PSP/merchant/tax verification → sandbox end-to-end → dual approval → scheduled activation.
  2. Learner switches AR↔EN: UI direction changes; market, currency, prices and times do not.
- **Alternate paths:**
  - Pause market → no new purchases; existing lessons honoured (FR-GEO-011).
- **Denial / error:**
  - Activation without legal readiness → blocked.
- **Timeout / network loss:**
  - —
- **Double-click / idempotency:** Decisions keyed.
- **Empty state:** No markets beyond defaults.
- **Recovery:** Pause / retire.
- **Audit events:** `market.approved`, `market.activated`, `market.paused`
- **Notifications:** Waitlisted adults notified on launch (with consent)
- **FR:** FR-GEO-002, FR-GEO-003, FR-GEO-010, FR-GEO-011, FR-I18N-006, FR-I18N-001
- **Source flows:** F02, F16, 01, 02, 24
- **Owner decisions:** O-01, O-02
- **Acceptance:** `acceptance/J16.feature` (1 scenarios)

## J17 · Kids / Professional / Simple mode switching (presentation only; permissions unchanged)
- **Persona:** Learner (6–12 kids, 13–59 professional, 60+ simple) and guardian
- **Actors & session boundaries:** Learner (own session); guardian PIN for kids settings (question open).
- **Entry:** After sign-up or from Account → App style.
- **Exit:** Chosen mode applied on the device; account permissions and consents unchanged.
- **Screens:** `UX-MOBILE-012` → `UX-MOBILE-K02` → `UX-MOBILE-K05` → `UX-MOBILE-K08` → `UX-MOBILE-K11` → `UX-MOBILE-S02` → `UX-MOBILE-S04` → `UX-MOBILE-S11` → `UX-MOBILE-011`
- **API:** `get__api_v1_me_preferences`, `patch__api_v1_me_preferences`, `get__achievements`, `getLearnerLearningSummary`
- **RBAC/ABAC:** `ui_mode` is presentation only (C-04): the server never uses it for authorization; minor protections come from age band + consents.
- **Happy path:**
  1. Default proposed by age band (D-35) → learner/guardian may change.
  2. Mode persists per account; layouts, type size and motion change; data and actions are the same contracts.
- **Alternate paths:**
  - Reduced motion or large text OS settings → respected in all modes.
- **Denial / error:**
  - Kids mode never shows public rankings, chat or purchases.
- **Timeout / network loss:**
  - Offline → last mode kept.
- **Double-click / idempotency:** Preference patch idempotent.
- **Empty state:** No badges yet → encouraging empty state (no fake stars).
- **Recovery:** Switch back anytime.
- **Audit events:** `preferences.updated`
- **Notifications:** —
- **FR:** FR-MOB-005, FR-ENG-004, FR-CONTEST-013, FR-IAM-007
- **Source flows:** F19
- **Owner decisions:** D-35, D-36, D-37, Guardian PIN storage
- **Acceptance:** `acceptance/J17.feature` (1 scenarios)
