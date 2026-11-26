# API gaps — reclassified (2026-11-23)

The 28 rows found by the design scan were investigated one by one against the parsed `openapi.yaml` (121 operations). Result: TRUE_MISSING_PROPOSAL **20**, OWNER_DECISION_REQUIRED **3**, EXISTING_NEEDS_CORRECTION **2**, DEFERRED_OR_FLAGGED **1**, EXISTING_AND_VALID **1**, NON_API_STATIC_CONTENT **1**.

Proposed contracts are in `openapi.proposed.yaml` (status PROPOSED; nothing is approved or implemented). Journey-level operations missing from this list (slot hold, cancellation, guardian invitation, report draft, offline sync, logout, refunds, break-glass, uploads …) are P-30…P-46 in `API_RECONCILIATION_MATRIX.csv`.

| Gap | As referenced | Screens | Classification | Resolution | Note |
|---|---|---|---|---|---|
| G-01 | `GET /api/v1/learners?market=&status=` | `UX-ADMIN-002` | **TRUE_MISSING_PROPOSAL** | P-01 | No learner list exists; admin projection proposed under /admin (D-42). |
| G-02 | `GET /api/v1/consents?status=pending` | `UX-ADMIN-004` | **TRUE_MISSING_PROPOSAL** | P-02 | List proposed; `verification_method` enum waits for O-04. |
| G-03 | `GET /api/v1/admin/teachers/applications` | `UX-ADMIN-006` | **TRUE_MISSING_PROPOSAL** | P-03 | Plus decision operation P-05 (journey J03). |
| G-04 | `GET /api/v1/teachers/{id}` | `UX-ADMIN-008` | **TRUE_MISSING_PROPOSAL** | P-06 | Same path shape as G-23 but private fields → separate admin op. |
| G-05 | `GET /api/v1/admin/quran-sources` | `UX-ADMIN-012` | **OWNER_DECISION_REQUIRED** | P-09 | Fields beyond FR-CURR-003 wait for O-06; flag quran_source_v1 off. |
| G-06 | `GET /api/v1/question-bank` | `UX-ADMIN-013` | **TRUE_MISSING_PROPOSAL** | P-10 | One operation for G-06 and G-28. |
| G-07 | `GET /api/v1/admin/rubrics` | `UX-ADMIN-014` | **TRUE_MISSING_PROPOSAL** | P-11 |  |
| G-08 | `GET /api/v1/admin/live-lessons` | `UX-ADMIN-016` | **TRUE_MISSING_PROPOSAL** | P-12 | Partly overlaps `get__api_v1_admin_operations_teacher_schedules` (schedules) and video incidents; live state list still missing. |
| G-09 | `GET /api/v1/admin/pay-runs` | `UX-ADMIN-021` | **TRUE_MISSING_PROPOSAL** | P-13 | List is safe; calculations stay blocked by O-08. |
| G-10 | `GET /api/v1/admin/competition-templates` | `UX-ADMIN-025` | **DEFERRED_OR_FLAGGED** | P-14 | No FR defines “templates”; served later by `kind=template` on the admin list. |
| G-11 | `POST /api/v1/admin/competitions/{id}/judges` | `UX-ADMIN-029` | **TRUE_MISSING_PROPOSAL** | P-15 |  |
| G-12 | `GET /api/v1/admin/rewards` | `UX-ADMIN-032` | **OWNER_DECISION_REQUIRED** |  | Prize/reward policy O-07; no contract drafted (fields would be invented). |
| G-13 | `GET /api/v1/admin/crm/leads` | `UX-ADMIN-033` | **TRUE_MISSING_PROPOSAL** | P-16 |  |
| G-14 | `GET /api/v1/admin/library` | `UX-ADMIN-037` | **TRUE_MISSING_PROPOSAL** | P-17 | Library items need licensing per item. |
| G-15 | `GET /api/v1/admin/audit-events` | `UX-ADMIN-040` | **EXISTING_NEEDS_CORRECTION** | C-02 | Use `get__api_v1_admin_security_access_audits` (exists); add `category` filter (finance/judging/consent/token) to cover FR-SEC-004 instead of a second audit endpoint. |
| G-16 | `POST /api/v1/auth/password-reset` | `UX-AUTH-004` | **TRUE_MISSING_PROPOSAL** | P-20,P-21 | Two operations: non-enumerating request + token confirm. |
| G-17 | `POST /api/v1/public/waitlist` | `UX-GLOB-003` | **TRUE_MISSING_PROPOSAL** | P-22 | Backed by flow 01 (waitlist or unavailable notice) and FR-CRM-005 consent. |
| G-18 | `POST /api/v1/subscriptions/{id}/renewal-consent` | `UX-GLOB-007` | **OWNER_DECISION_REQUIRED** | P-23 | Renewal policy O-02 and PSP support. |
| G-19 | `GET /api/v1/library?program=` | `UX-LEARNER-028` | **TRUE_MISSING_PROPOSAL** | P-18 |  |
| G-20 | `GET /api/v1/notifications` | `UX-LEARNER-030` | **TRUE_MISSING_PROPOSAL** | P-24,P-25 |  |
| G-21 | `POST /api/v1/auth/refresh` | `UX-MOBILE-000` | **EXISTING_AND_VALID** | post__auth_refresh | Already defined: POST /api/v1/auth/refresh, operationId `post__auth_refresh`, RefreshRequest → AuthTokenEnvelope, security []. Was listed as a gap because the gap scanner matched only the screen’s free-text reference. Minor correction C-03: document refresh-token rotation and reuse detection (409 on replay). |
| G-22 | `GET /api/v1/me/badges` | `UX-MOBILE-K08` | **EXISTING_NEEDS_CORRECTION** | get__achievements | Use existing `GET /api/v1/achievements` (Achievement.type = badge key) instead of `/me/badges` (D-43); badge catalogue waits for D-36. |
| G-23 | `GET /api/v1/teachers/{teacherId}` | `UX-PUBLIC-006` | **TRUE_MISSING_PROPOSAL** | P-08 | Public projection; alias of G-04 path shape only. |
| G-24 | `static CMS page` | `UX-PUBLIC-007`, `UX-PUBLIC-010` | **NON_API_STATIC_CONTENT** |  | About/How-it-works are CMS/static pages served by the web app; no API. |
| G-25 | `GET /api/v1/legal/{slug}` | `UX-PUBLIC-012` | **TRUE_MISSING_PROPOSAL** | P-26 | Versioned so consent receipts can cite the text version; content is O-01. |
| G-26 | `POST /api/v1/teachers/applications` | `UX-TEACHER-001` | **TRUE_MISSING_PROPOSAL** | P-04 | Needs createUpload P-43 for documents. |
| G-27 | `GET /api/v1/learners?assigned=me` | `UX-TEACHER-008` | **TRUE_MISSING_PROPOSAL** | P-27 | Teacher-scoped list instead of a `?assigned=me` flag on a shared endpoint. |
| G-28 | `GET /api/v1/question-bank?status=review` | `UX-TEACHER-012` | **TRUE_MISSING_PROPOSAL** | P-10 | Query variant of G-06. |

## Corrections to existing operations
| ID | Operation | Issue | Proposed fix | FR |
|---|---|---|---|---|
| C-01 | `post_bookings` (POST /api/v1/bookings) | BookingRequest has no hold reference; no Idempotency-Key header; only 201/403/409/422 responses | Add `hold_id` (from P-30), require Idempotency-Key, add 401/429 | FR-BOOK-001 |
| C-02 | `get__api_v1_admin_security_access_audits` (GET /api/v1/admin/security/access-audits) | Covers privileged access only; FR-SEC-004 also needs finance/judging/consent/token events | Add `category` + `actor_id` + `from/to` filters and cursor pagination | FR-SEC-004 |
| C-03 | `post__auth_refresh` (POST /api/v1/auth/refresh) | Rotation/reuse semantics undocumented | Document one-time refresh tokens; replay → 409 TOKEN_REUSED and family revocation | FR-IAM-008 |
| C-04 | `patch__api_v1_me_preferences` (PATCH /api/v1/me/preferences) | Preference schema has no UI mode for Kids/Professional/Simple (D-34/D-35) | Add `ui_mode` enum [kids, professional, simple]; server ignores it for authorization (presentation only) | FR-MOB-005 |
| C-05 | `get__teachers` (GET /api/v1/teachers) | Used with `?admin=1` by UX-ADMIN-007; a query flag must not unlock private fields | Remove the admin use; bind UX-ADMIN-007 to listAdminTeachers (P-07) | FR-SEC-001 |
| C-06 | `get_bookings` (GET /api/v1/bookings) | Used with `?admin=1` by UX-ADMIN-015; also returns only 200 (no error responses) | Bind admin to a scoped `listAdminBookings` (follow-up proposal) and add 401/403/422/429 | FR-BOOK-004 |
| C-07 | `get__competitions` (GET /api/v1/competitions) | Used with `?admin=1` by UX-ADMIN-027; drafts must never be visible to learners | Bind admin to listAdminCompetitions (P-14) | FR-CONTEST-001 |
| C-17 | `post__learning_plans__planId__approve` (POST /api/v1/learning-plans/{planId}/approve) | Teacher can only approve; “Reject with reason” on UX-TEACHER-011 has no operation | Accept `{decision: approve|reject, reason}` (or add a sibling reject operation) | FR-PLAN-002 |
| C-08 | `post__lessons__lessonId__report` (POST /api/v1/lessons/{lessonId}/report) | No draft version link; concurrent edits undetectable | Accept `draft_version`; 412 VERSION_CONFLICT on mismatch (with P-35) | FR-ATT-003 |
| C-09 | `schema:Subscription` ( ) | Subscription.status = ['pending', 'active', 'paused', 'expired', 'cancelled'] vs state machine [PENDING_PAYMENT, ACTIVE, RENEWAL_DUE, SUSPENDED, REFUND_PENDING, PARTIALLY_REFUNDED, REFUNDED, EXPIRED, CANCELLED] | API lacks renewal_due/suspended/refund states and has `paused`, which the state machine does not define — PROPOSED; the state machine is the domain authority |  |
| C-10 | `schema:Lesson` ( ) | Lesson.attendance_state = ['pending', 'verified', 'disputed'] vs state machine [DRAFT, CONFIRMED, READY, IN_PROGRESS, INTERRUPTED, RESCHEDULE_PENDING, COMPLETED, CANCELLED, DISPUTED, RESOLVED] | Lesson has no lifecycle `state` field at all; add it (attendance_state stays separate) — PROPOSED; the state machine is the domain authority |  |
| C-11 | `schema:Competition` ( ) | Competition.(none) = None vs state machine [draft … academic_review … legal_review … registration_open … running … scoring … provisional_results … appeal_window … finalized … prizes_issued … archived] | Competition has no state field; add the 13-state lifecycle + cancelled — PROPOSED; the state machine is the domain authority |  |
| C-12 | `schema:ConsentReceipt` ( ) | ConsentReceipt.state = ['pending', 'approved', 'revoked', 'expired'] vs state machine [not_requested, requested, verified/granted, withdrawn, expired] | Names differ (approved↔granted, revoked↔withdrawn); a guardian `declined` outcome exists in neither — add it — PROPOSED; the state machine is the domain authority |  |
| C-13 | `schema:Assessment` ( ) | Assessment.status = ['draft', 'submitted', 'reviewing', 'approved', 'rejected'] vs state machine [DRAFT, SUBMITTED, HUMAN_REVIEW, APPROVED, REJECTED, PUBLISHED, APPEALED, CORRECTED] | API stops at approved/rejected; published/appealed/corrected missing (FR-ASMT-007) — PROPOSED; the state machine is the domain authority |  |
| C-14 | `schema:LearningPlan` ( ) | LearningPlan.state = ['draft', 'pending_teacher_review', 'approved', 'archived'] vs state machine [draft, proposed, teacher_review, approved, active, superseded, archived] | AI drafts must start at `proposed`; API has no proposed/active/superseded — PROPOSED; the state machine is the domain authority |  |
| C-15 | `schema:PayRun` ( ) | PayRun.state = ['draft', 'calculated', 'reviewed', 'approved', 'paid', 'reconciled'] vs state machine [accrued, calculated, reviewed, approved, payout_requested, paid, reconciled (+ disputed)] | payout_requested and disputed missing — PROPOSED; the state machine is the domain authority |  |
| C-16 | `schema:CompetitionSubmission` ( ) | CompetitionSubmission.status = ['draft', 'submitted', 'under_review', 'judged'] vs state machine [submitted, evaluating, reviewed, final (FR-CONTEST-008)] | Names differ from FR-CONTEST-008; no second-review state — PROPOSED; the state machine is the domain authority |  |
