# Unresolved requirements & decisions (do not guess)

Codex must implement these behind feature flags or stop and ask. Nothing here may be invented.

## Open product/legal decisions (from package `DECISIONS_AND_OPEN_ITEMS.md`)
| O-01 | Commercial legal entity and eligible geographies | Egypt initially; KSA pilots after settlement validation | Legal/CEO / before first payments |
| O-02 | Initial pricing tiers and currency | 8×30m entry offer; A/B test pricing | Commercial / before ads |
| O-03 | P0 in-app conferencing vendor | LiveKit and VideoSDK technical POC; Meet fallback | CTO / before build |
| O-04 | Which minors can enroll and required parent process | Stop before payment until consent verification | Legal / before onboarding minors |
| O-05 | Recording + AI processing purposes & consent | Disabled by default | Legal/DPO / before enabling features |
| O-06 | Academic supervisor and Quran content rights | Contract qualified owner and verify source license | Academic/Legal / before curriculum |
| O-07 | Prize policy for contests | Noncash learning rewards; no paid advantage | Legal/Academic / before contest launch |
| O-08 | Payroll contract forms and minimum wages | No payroll contract activated without local legal review | Finance/Legal / before teacher contracts |
| O-09 | Baseline support service hours and staff | Local coverage + response SLA, budgeted | Ops / before launch |
| O-10 | Funding amount and approval tranche | Gates: paid pilot → retention → controlled scale | Investors / funding meeting |

## Design decisions awaiting brand-owner approval
- D-03 `bg/raised #FFFCF5` paper surface for dense data (brand book uses `surface-raised #F3EBDA` for cards).
- D-04 input border `#8E8574` (3.4:1) instead of ink-muted.
- D-14 CTA “احجز تقييم مستوى” without the word “free” until commercial decision O-02.
- Spelling: brand = **Usayd / أُسَيْد** (the request said “Ased”; the brand book forbids other spellings). Confirm.

## Per-screen unresolved items
- `UX-PUBLIC-004` Pricing: Final prices and packages per market (O-02).
- `UX-PUBLIC-006` Teacher Public Profile: API: GET /api/v1/teachers/{teacherId} — UNRESOLVED — PROPOSED getPublicTeacher (P-08)
- `UX-PUBLIC-010` About/Academic Standards: Name and approval of the partner academic body (O-06).
- `UX-PUBLIC-012` Legal & Consents: Final legal texts per country (O-01).; API: GET /api/v1/public/legal-documents/{slug} — UNRESOLVED — PROPOSED getLegalDocument (P-26, content O-01)
- `UX-AUTH-002` Guardian Consent Step: Legal verification method per country (O-04); Legal guardian-verification method per country (O-04).
- `UX-AUTH-004` Password Recovery: API: POST /api/v1/auth/password-reset-requests — UNRESOLVED — PROPOSED requestPasswordReset (P-20) + confirmPasswordReset (P-21)
- `UX-LEARNER-016` Practice Recording: AI recitation analysis legal basis & model validation (O-05, AI eval gates)
- `UX-LEARNER-028` Course Library: API: GET /api/v1/library-items — UNRESOLVED — PROPOSED listLibraryItems (P-18)
- `UX-LEARNER-030` Notifications: API: GET /api/v1/me/notifications — UNRESOLVED — PROPOSED listMyNotifications (P-24)
- `UX-TEACHER-001` Teacher Login & Onboarding: API: POST /api/v1/teacher-applications — UNRESOLVED — PROPOSED submitTeacherApplication (P-04)
- `UX-TEACHER-008` My Assigned Learners: API: GET /api/v1/teachers/me/learners — UNRESOLVED — PROPOSED listMyLearners (P-27)
- `UX-TEACHER-012` Question Bank Review: API: GET /api/v1/question-bank-items?status=review — UNRESOLVED — PROPOSED listQuestionBankItems (P-10)
- `UX-ADMIN-002` Learner Directory: API: GET /api/v1/admin/learners — UNRESOLVED — PROPOSED listAdminLearners (P-01)
- `UX-ADMIN-004` Guardian Consent Queue: API: GET /api/v1/admin/consents — UNRESOLVED — PROPOSED listAdminConsents (P-02, needs O-04)
- `UX-ADMIN-006` Teacher Recruitment: API: GET /api/v1/admin/teacher-applications — UNRESOLVED — PROPOSED listTeacherApplications (P-03)
- `UX-ADMIN-007` Teacher Management: Admin teacher list should use a dedicated admin operation (proposed `listAdminTeachers`, API_RECONCILIATION_MATRIX) — public `get__teachers` must not expose contract or employment fields; API: GET /api/v1/admin/teachers — UNRESOLVED — PROPOSED listAdminTeachers (P-07); was get__teachers?admin=1 (C-05)
- `UX-ADMIN-008` Teacher Profile Admin: API: GET /api/v1/admin/teachers/{teacherId} — UNRESOLVED — PROPOSED getAdminTeacher (P-06)
- `UX-ADMIN-009` Teacher Contract Builder: Minimum wage and contract templates per country (O-08)
- `UX-ADMIN-012` Quran Content Sources: Licensed Quran corpus and font approval (O-06); Choose the licensed corpus and Mushaf font after licence review (O-06).; API: GET /api/v1/admin/quran-sources — UNRESOLVED — PROPOSED listQuranSources (P-09, needs O-06)
- `UX-ADMIN-013` Question Bank Manager: API: GET /api/v1/question-bank-items — UNRESOLVED — PROPOSED listQuestionBankItems (P-10)
- `UX-ADMIN-014` Assessment Rubrics: API: GET /api/v1/admin/rubrics — UNRESOLVED — PROPOSED listRubrics (P-11)
- `UX-ADMIN-015` Bookings Operations: Admin booking list should use a scoped admin operation (proposed `listAdminBookings`); `get_bookings` is the learner’s own list; API: GET /api/v1/admin/bookings — UNRESOLVED — PROPOSED listAdminBookings (P-47); was get_bookings?admin=1 (C-06)
- `UX-ADMIN-016` Live Lessons Monitor: API: GET /api/v1/admin/lessons — UNRESOLVED — PROPOSED listAdminLessons (P-12)
- `UX-ADMIN-021` Payroll Calculations: API: GET /api/v1/admin/pay-runs — UNRESOLVED — PROPOSED listPayRuns (P-13, flag payroll_v1)
- `UX-ADMIN-025` Competition Templates: API: GET /api/v1/admin/competitions?kind=template — UNRESOLVED — PROPOSED listAdminCompetitions (P-14), templates DEFERRED
- `UX-ADMIN-026` Contest Builder Wizard: Prize policy (O-07); Prize policy (O-07)
- `UX-ADMIN-027` Competitions List: Admin competition list should use a dedicated admin operation (proposed `listAdminCompetitions`) so drafts are never visible to learners; API: GET /api/v1/admin/competitions — UNRESOLVED — PROPOSED listAdminCompetitions (P-14); was get__competitions?admin=1 (C-07)
- `UX-ADMIN-029` Judge Assignments: API: POST /api/v1/admin/competitions/{competitionId}/judges — UNRESOLVED — PROPOSED assignCompetitionJudges (P-15)
- `UX-ADMIN-032` Contest Rewards & Certificates: Prize policy (O-07); API: GET /api/v1/admin/rewards — UNRESOLVED — OWNER_DECISION_REQUIRED (O-07), no contract drafted
- `UX-ADMIN-033` CRM Pipeline: API: GET /api/v1/admin/crm/leads — UNRESOLVED — PROPOSED listCrmLeads (P-16)
- `UX-ADMIN-037` Recorded Content Library: API: GET /api/v1/admin/library-items — UNRESOLVED — PROPOSED listAdminLibraryItems (P-17)
- `UX-GLOB-003` Unavailable Country & Waitlist: API: POST /api/v1/public/market-waitlist — UNRESOLVED — PROPOSED joinMarketWaitlist (P-22)
- `UX-GLOB-007` Renewal Price Change Notice: API: POST /api/v1/subscriptions/{subscriptionId}/renewal-consent — UNRESOLVED — PROPOSED setRenewalConsent (P-23, needs O-02)
- `UX-GLOB-011` Market Launch Wizard: Legal entity per market (O-01); Legal entity per market (O-01)
- `UX-SUP-004` Safeguarding Case Console: Starting break-glass access needs an API operation and a policy decision (proposed: postBreakGlassGrant, D-39)
- `UX-SUP-009` Audit and Break-glass Review: Recording a review outcome needs an API operation that doesn’t exist (proposed: postAccessAuditReview)
- `UX-MOBILE-000` Flutter Splash (added): Force-update / minimum supported app version policy is not defined in the blueprint; Token refresh endpoint missing from OpenAPI v1.2
- `UX-MOBILE-K08` Kids · My stars (added): Badges endpoint not in OpenAPI v1.2; Badge catalogue and award rules (D-36)
- `UX-MOBILE-K11` Kids · Me (added): Guardian PIN — device-local or server-side? (decision with O-04)

## Functional requirements with no UI screen mapped (backend-only or gap)
FR-IAM-010, FR-CURR-004, FR-CURR-005, FR-BOOK-007, FR-BOOK-008, FR-PAY-008, FR-ASMT-004, FR-CONTEST-004, FR-MEDIA-003, FR-CRM-006, FR-ADMIN-009, FR-SEC-002, FR-SEC-003, FR-SEC-007, FR-SEC-008, FR-GEO-012, FR-I18N-002, FR-VPC-007, FR-SUP-012
