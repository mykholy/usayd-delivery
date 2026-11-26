# API contracts used by the UI

Source of truth: `07_api/openapi.yaml` (v1.2 draft, copied unchanged). This file maps every UI operation to the screens that need it, and lists **UNRESOLVED** endpoints the UI needs but the OpenAPI does not define yet. Codex must add those to OpenAPI (reviewed) before implementing — do not invent payloads silently.

## Conventions (from the package)
- Base `/api/v1`; JSON; typed error codes (`errors.*`); idempotency keys on payments/bookings/submissions; optimistic versions (409) on plans, attempts, settings, routing.
- Money: `{amount_minor:int, currency:"ISO4217"}`; time: `starts_at_utc` + `timezone_id` (IANA) + display fields; never local strings as instants.
- Authorization on every call (role + scope + ownership); webhooks verified by signature and idempotent by provider event id.

## Operations defined in OpenAPI
| Operation | operationId | Screens |
|---|---|---|
| `GET /api/v1/achievements` | `get__achievements` | UX-LEARNER-026, UX-MOBILE-K08 |
| `GET /api/v1/admin/ai-policy-flags` | `get__admin_ai_policy_flags` | UX-ADMIN-024 |
| `GET /api/v1/admin/contest-appeals` | `getAdminContestAppeals` | UX-ADMIN-031 |
| `GET /api/v1/admin/finance/fx-rates` | `get__api_v1_admin_finance_fx_rates` | UX-GLOB-015 |
| `GET /api/v1/admin/kpis` | `get__admin_kpis` | UX-ADMIN-039 |
| `GET /api/v1/admin/kpis?domain=marketing` | `get__admin_kpis` | UX-ADMIN-034 |
| `GET /api/v1/admin/kpis?scope=` | `get__admin_kpis` | UX-ADMIN-001 |
| `GET /api/v1/admin/kpis?scope=region` | `get__admin_kpis` | UX-SUP-007 |
| `GET /api/v1/admin/legal-market-readiness` | `get__api_v1_admin_legal_market_readiness` | UX-GLOB-010 |
| `GET /api/v1/admin/markets` | `get__api_v1_admin_markets` | UX-GLOB-010 |
| `GET /api/v1/admin/operations/teacher-schedules` | `get__api_v1_admin_operations_teacher_schedules` | UX-ADMIN-010, UX-GLOB-016, UX-SUP-006 |
| `GET /api/v1/admin/payment-merchant-profiles` | `get__api_v1_admin_payment_merchant_profiles` | UX-GLOB-014 |
| `GET /api/v1/admin/price-books` | `get__api_v1_admin_price_books` | UX-GLOB-012 |
| `GET /api/v1/admin/security/access-audits` | `get__api_v1_admin_security_access_audits` | UX-ADMIN-040, UX-SUP-009 |
| `GET /api/v1/admin/settings/versions` | `get__api_v1_admin_settings_versions` | UX-ADMIN-041, UX-SUP-010 |
| `GET /api/v1/admin/settings/versions?domain=ai` | `get__api_v1_admin_settings_versions` | UX-ADMIN-023 |
| `GET /api/v1/admin/supervisor-assignments` | `get__api_v1_admin_supervisor_assignments` | UX-ADMIN-005, UX-SUP-008 |
| `GET /api/v1/admin/translations` | `get__api_v1_admin_translations` | UX-SUP-011 |
| `GET /api/v1/admin/translations?namespace=notifications` | `get__api_v1_admin_translations` | UX-ADMIN-038 |
| `GET /api/v1/admin/video-incidents` | `get__api_v1_admin_video_incidents` | UX-VPC-008 |
| `GET /api/v1/admin/video-provider-health` | `get__api_v1_admin_video_provider_health` | UX-VPC-001, UX-VPC-007 |
| `GET /api/v1/admin/video-providers` | `get__api_v1_admin_video_providers` | UX-ADMIN-017, UX-VPC-001 |
| `GET /api/v1/admin/video-providers/{id}/capabilities` | `get__api_v1_admin_video_providers_providerAccountId_capabilities` | UX-VPC-003 |
| `GET /api/v1/admin/video-routing-policies` | `get__api_v1_admin_video_routing_policies` | UX-VPC-004 |
| `GET /api/v1/booking/available-slots` | `get__api_v1_booking_available_slots` | UX-LEARNER-008, UX-GLOB-005, UX-MOBILE-004 |
| `GET /api/v1/booking/available-slots?type=assessment` | `get__api_v1_booking_available_slots` | UX-PUBLIC-009, UX-LEARNER-004 |
| `GET /api/v1/bookings` | `get_bookings` | UX-MOBILE-004, UX-MOBILE-S04 |
| `GET /api/v1/bookings?from=&to=` | `get_bookings` | UX-LEARNER-007 |
| `GET /api/v1/bookings?role=teacher` | `get_bookings` | UX-TEACHER-004, UX-MOBILE-009 |
| `GET /api/v1/bookings?role=teacher&date=today` | `get_bookings` | UX-TEACHER-002 |
| `GET /api/v1/bookings?upcoming=1` | `get_bookings` | UX-LEARNER-001 |
| `GET /api/v1/competition-results/{id}` | `getCompetitionResult` | UX-LEARNER-025 |
| `GET /api/v1/competitions` | `get__competitions` | UX-LEARNER-020 |
| `GET /api/v1/competitions/{id}` | `get__competitions__competitionId` | UX-LEARNER-021, UX-ADMIN-028, UX-ENG-001, UX-MOBILE-008 |
| `GET /api/v1/competitions/{id}/eligibility` | `getContestEligibility` | UX-LEARNER-020, UX-LEARNER-021 |
| `GET /api/v1/competitions/{id}/registration` | `getCompetitionRegistration` | UX-LEARNER-022 |
| `GET /api/v1/competitions/{id}/rounds/{roundId}` | `getCompetitionRound` | UX-LEARNER-023 |
| `GET /api/v1/competitions/{id}/standings` | `get__competitions__competitionId__standings` | UX-LEARNER-024 |
| `GET /api/v1/competitions?judge=me` | `get__competitions` | UX-TEACHER-013 |
| `GET /api/v1/competitions?public=true` | `get__competitions` | UX-PUBLIC-008 |
| `GET /api/v1/conferences/{id}/capabilities` | `get__conferences__conferenceId__capabilities` | UX-LEARNER-010, UX-TEACHER-006, UX-ADMIN-016, UX-VPC-009, UX-VPC-010 |
| `GET /api/v1/exam-attempts/{attemptId}` | `getExamAttempt` | UX-LEARNER-019 |
| `GET /api/v1/exams` | `get__exams` | UX-LEARNER-017 |
| `GET /api/v1/exams?type=practice` | `get__exams` | UX-ENG-002 |
| `GET /api/v1/learners/{id}` | `get__learners__learnerId` | UX-LEARNER-002, UX-TEACHER-009, UX-ADMIN-003 |
| `GET /api/v1/learners/{id}/audio-preferences` | `getLearnerAudioPreferences` | UX-LEARNER-016, UX-LEARNER-027 |
| `GET /api/v1/learners/{id}/learning-summary` | `getLearnerLearningSummary` | UX-LEARNER-001, UX-MOBILE-002, UX-MOBILE-K02, UX-MOBILE-S02 |
| `GET /api/v1/learners/{id}/learning-summary?period=week` | `getLearnerLearningSummary` | UX-ENG-003 |
| `GET /api/v1/learning-plans/{planId}` | `getLearningPlan` | UX-LEARNER-012, UX-LEARNER-013, UX-TEACHER-005, UX-SUP-002 |
| `GET /api/v1/learning-plans?status=proposed` | `get__learning_plans` | UX-TEACHER-011 |
| `GET /api/v1/lessons/{lessonId}` | `get__lessons__lessonId` | UX-LEARNER-009, UX-TEACHER-005, UX-GLOB-009 |
| `GET /api/v1/lessons/{lessonId}/report` | `getLessonReport` | UX-LEARNER-011 |
| `GET /api/v1/me` | `get__me` | UX-AUTH-002, UX-LEARNER-002 |
| `GET /api/v1/me/preferences` | `get__api_v1_me_preferences` | UX-LEARNER-032, UX-TEACHER-018, UX-GLOB-004, UX-MOBILE-000, UX-MOBILE-011 |
| `GET /api/v1/memory-map` | `get__memory_map` | UX-LEARNER-015, UX-MOBILE-005, UX-MOBILE-K05 |
| `GET /api/v1/memory-map?learnerId=` | `get__memory_map` | UX-TEACHER-009 |
| `GET /api/v1/packages` | `get__packages` | UX-ADMIN-020 |
| `GET /api/v1/payments/{id}` | `get__payments__paymentId` | UX-GLOB-006 |
| `GET /api/v1/payments/{paymentId}` | `get__payments__paymentId` | UX-LEARNER-029, UX-ADMIN-019 |
| `GET /api/v1/programs` | `get__programs` | UX-PUBLIC-001, UX-LEARNER-003, UX-ADMIN-011 |
| `GET /api/v1/programs/{programId}` | `get__programs__programId` | UX-PUBLIC-003 |
| `GET /api/v1/programs?country=&age_band=&goal=` | `get__programs` | UX-PUBLIC-002 |
| `GET /api/v1/public/markets` | `get__api_v1_public_markets` | UX-PUBLIC-001, UX-GLOB-001 |
| `GET /api/v1/public/pricing` | `get__api_v1_public_pricing` | UX-PUBLIC-003 |
| `GET /api/v1/public/pricing?country=` | `get__api_v1_public_pricing` | UX-PUBLIC-001, UX-PUBLIC-004, UX-GLOB-002 |
| `GET /api/v1/public/timezones?q=` | `get__api_v1_public_timezones` | UX-AUTH-005, UX-GLOB-004 |
| `GET /api/v1/revision-tasks?date=today` | `get__revision_tasks` | UX-LEARNER-013 |
| `GET /api/v1/revision-tasks?due=today` | `get__revision_tasks` | UX-LEARNER-001 |
| `GET /api/v1/revision-tasks?status=due` | `get__revision_tasks` | UX-LEARNER-014 |
| `GET /api/v1/subscriptions` | `get__subscriptions` | UX-LEARNER-029, UX-GLOB-007 |
| `GET /api/v1/supervisor/competition-appeals` | `get__api_v1_supervisor_competition_appeals` | UX-TEACHER-015, UX-SUP-005 |
| `GET /api/v1/supervisor/quality-observations` | `get__api_v1_supervisor_quality_observations` | UX-SUP-003 |
| `GET /api/v1/supervisor/queues` | `get__api_v1_supervisor_queues` | UX-SUP-001 |
| `GET /api/v1/supervisor/safeguarding-cases` | `get__api_v1_supervisor_safeguarding_cases` | UX-ADMIN-036, UX-SUP-004 |
| `GET /api/v1/teacher/me/availability-rules` | `get__api_v1_teacher_me_availability_rules` | UX-TEACHER-003, UX-GLOB-008 |
| `GET /api/v1/teachers/me/compensation-preview` | `getCompensationPreview` | UX-TEACHER-002, UX-TEACHER-016 |
| `GET /api/v1/teachers/me/pay-statements` | `get__teachers_me_pay_statements` | UX-TEACHER-016 |
| `GET /api/v1/teachers/me/shifts` | `getMyShifts` | UX-TEACHER-002 |
| `GET /api/v1/teachers/{id}/availability` | `get__teachers__teacherId__availability` | UX-LEARNER-006 |
| `GET /api/v1/teachers/{teacherId}/availability` | `get__teachers__teacherId__availability` | UX-PUBLIC-006 |
| `GET /api/v1/teachers?program=&language=` | `get__teachers` | UX-LEARNER-005 |
| `GET /api/v1/teachers?specialty=&language=&gender=` | `get__teachers` | UX-PUBLIC-005 |
| `PATCH /api/v1/admin/translations/{id}` | `patch__api_v1_admin_translations_translationId` | UX-SUP-011 |
| `PATCH /api/v1/learning-plans/{planId}` | `patchLearningPlanDraft` | UX-TEACHER-011 |
| `PATCH /api/v1/me/preferences` | `patch__api_v1_me_preferences` | UX-AUTH-005, UX-LEARNER-032, UX-TEACHER-018, UX-GLOB-004, UX-GLOB-017, UX-MOBILE-012, UX-MOBILE-K11, UX-MOBILE-S11 |
| `POST /api/v1/admin/ai-policy-flags/{flagId}/resolve` | `post__admin_ai_policy_flags__flagId__resolve` | UX-ADMIN-024 |
| `POST /api/v1/admin/competitions` | `post__admin_competitions` | UX-ADMIN-026 |
| `POST /api/v1/admin/competitions/{id}/publish` | `post__admin_competitions__competitionId__publish` | UX-ADMIN-028, UX-ADMIN-030 |
| `POST /api/v1/admin/contest-appeals/{id}/resolve` | `postAdminContestAppealResolve` | UX-TEACHER-015, UX-ADMIN-031 |
| `POST /api/v1/admin/markets` | `post__api_v1_admin_markets` | UX-GLOB-011 |
| `POST /api/v1/admin/markets/{id}/decision` | `post__api_v1_admin_markets_marketId_decision` | UX-GLOB-011 |
| `POST /api/v1/admin/pay-runs/{payRunId}/approve` | `post__admin_pay_runs__payRunId__approve` | UX-ADMIN-022 |
| `POST /api/v1/admin/payment-merchant-profiles` | `post__api_v1_admin_payment_merchant_profiles` | UX-GLOB-014 |
| `POST /api/v1/admin/price-books` | `post__api_v1_admin_price_books` | UX-GLOB-012 |
| `POST /api/v1/admin/price-books/{id}/decision` | `post__api_v1_admin_price_books_priceBookId_decision` | UX-GLOB-013 |
| `POST /api/v1/admin/settings/drafts` | `post__api_v1_admin_settings_drafts` | UX-SUP-010 |
| `POST /api/v1/admin/settings/versions/{id}/decision` | `post__api_v1_admin_settings_versions_settingsVersionId_decision` | UX-SUP-010 |
| `POST /api/v1/admin/supervisor-assignments` | `post__api_v1_admin_supervisor_assignments` | UX-SUP-008 |
| `POST /api/v1/admin/supervisor-assignments/{id}/revoke` | `post__api_v1_admin_supervisor_assignments_assignmentId_revoke` | UX-SUP-008 |
| `POST /api/v1/admin/teachers/{teacherId}/contracts` | `post__admin_teachers__teacherId__contracts` | UX-ADMIN-009 |
| `POST /api/v1/admin/translations/{id}/publish` | `post__api_v1_admin_translations_translationId_publish` | UX-SUP-011 |
| `POST /api/v1/admin/video-incidents/{id}/recover` | `post__api_v1_admin_video_incidents_incidentId_recover` | UX-VPC-008 |
| `POST /api/v1/admin/video-providers` | `post__api_v1_admin_video_providers` | UX-VPC-002 |
| `POST /api/v1/admin/video-providers/{id}/connection-test` | `post__api_v1_admin_video_providers_providerAccountId_connection_test` | UX-VPC-002 |
| `POST /api/v1/admin/video-routing-policies` | `post__api_v1_admin_video_routing_policies` | UX-VPC-004 |
| `POST /api/v1/admin/video-routing-policies/{id}/activate` | `post__api_v1_admin_video_routing_policies_policyId_activate` | UX-VPC-006 |
| `POST /api/v1/admin/video-routing-policies/{id}/decision` | `post__api_v1_admin_video_routing_policies_policyId_decision` | UX-VPC-006 |
| `POST /api/v1/admin/video-routing-policies/{id}/dry-run` | `post__api_v1_admin_video_routing_policies_policyId_dry_run` | UX-VPC-005 |
| `POST /api/v1/admin/video-routing-policies/{id}/rollback` | `post__api_v1_admin_video_routing_policies_policyId_rollback` | UX-VPC-006 |
| `POST /api/v1/assessments` | `post__assessments` | UX-LEARNER-004, UX-TEACHER-010 |
| `POST /api/v1/assessments/{id}/approve` | `post__assessments__assessmentId__approve` | UX-TEACHER-010 |
| `POST /api/v1/auth/login` | `post__auth_login` | UX-AUTH-003, UX-TEACHER-001, UX-MOBILE-001 |
| `POST /api/v1/auth/refresh` | `post__auth_refresh` | UX-AUTH-003, UX-MOBILE-000 |
| `POST /api/v1/auth/register` | `post__auth_register` | UX-PUBLIC-009, UX-AUTH-001, UX-MOBILE-001 |
| `POST /api/v1/bookings` | `post_bookings` | UX-PUBLIC-009, UX-LEARNER-004, UX-LEARNER-008 |
| `POST /api/v1/competition-results/{id}/appeal` | `post__competition_results__resultId__appeal` | UX-LEARNER-025 |
| `POST /api/v1/competition-submissions/{id}/judge` | `post__competition_submissions__submissionId__judge` | UX-TEACHER-014 |
| `POST /api/v1/competitions/{id}/register` | `post__competitions__competitionId__register` | UX-LEARNER-021 |
| `POST /api/v1/competitions/{id}/submissions` | `post__competitions__competitionId__submissions` | UX-LEARNER-023 |
| `POST /api/v1/consents` | `post__consents` | UX-AUTH-002 |
| `POST /api/v1/consents/{id}/withdraw` | `post__consents__consentId__withdraw` | UX-LEARNER-032 |
| `POST /api/v1/exam-attempts/{id}/checkpoint` | `postExamCheckpoint` | UX-LEARNER-018, UX-MOBILE-007 |
| `POST /api/v1/exam-attempts/{id}/submit` | `post__exam_attempts__attemptId__submit` | UX-LEARNER-018, UX-MOBILE-007 |
| `POST /api/v1/exams/{examId}/attempts` | `post__exams__examId__attempts` | UX-LEARNER-018 |
| `POST /api/v1/learners` | `post__learners` | UX-AUTH-001 |
| `POST /api/v1/learning-plans/suggestions` | `post__learning_plans_suggestions` | UX-LEARNER-027, UX-MOBILE-006 |
| `POST /api/v1/learning-plans/{planId}/approve` | `post__learning_plans__planId__approve` | UX-TEACHER-011 |
| `POST /api/v1/lessons/{id}/attendance-disputes` | `postAttendanceDispute` | UX-LEARNER-031, UX-TEACHER-016, UX-ADMIN-018 |
| `POST /api/v1/lessons/{id}/join` | `post__lessons__lessonId__join` | UX-MOBILE-003 |
| `POST /api/v1/lessons/{id}/report` | `post__lessons__lessonId__report` | UX-MOBILE-010 |
| `POST /api/v1/lessons/{lessonId}/join` | `post__lessons__lessonId__join` | UX-LEARNER-010, UX-TEACHER-006, UX-VPC-009, UX-VPC-010, UX-MOBILE-S02 |
| `POST /api/v1/lessons/{lessonId}/report` | `post__lessons__lessonId__report` | UX-TEACHER-007 |
| `POST /api/v1/lessons/{lessonId}/reschedule-request` | `post__api_v1_lessons_lessonId_reschedule_request` | UX-LEARNER-009 |
| `POST /api/v1/me/checkout-quotes` | `post__api_v1_me_checkout_quotes` | UX-LEARNER-008, UX-GLOB-006 |
| `POST /api/v1/me/payment-checkouts` | `post__api_v1_me_payment_checkouts` | UX-GLOB-006 |
| `POST /api/v1/revision-tasks/{taskId}/evidence` | `post__revision_tasks__taskId__evidence` | UX-LEARNER-014, UX-LEARNER-016 |
| `POST /api/v1/supervisor/academic-plans/{planId}/decision` | `post__api_v1_supervisor_academic_plans_planId_decision` | UX-SUP-002 |
| `POST /api/v1/supervisor/safeguarding-cases` | `post__api_v1_supervisor_safeguarding_cases` | UX-SUP-004 |
| `POST /api/v1/support/tickets` | `post__support_tickets` | UX-PUBLIC-011, UX-LEARNER-031, UX-TEACHER-017, UX-ADMIN-035 |
| `POST /api/v1/webhooks/payments/{provider}` | `post__webhooks_payments__provider` | UX-ADMIN-019 |
| `POST /api/v1/webhooks/video/{provider}` | `post__webhooks_video__provider` | UX-VPC-007 |
| `PUT /api/v1/teacher/me/availability-rules` | `put__api_v1_teacher_me_availability_rules` | UX-GLOB-008 |
| `static CMS page` | `NON_API_STATIC_CONTENT — served by the web app` | UX-PUBLIC-007, UX-PUBLIC-010 |

## UNRESOLVED — needed by UI, missing from OpenAPI (propose, review, then implement)
| Needed operation | Note | Screens | Suggested shape (to confirm) |
|---|---|---|---|
| `GET /api/v1/admin/bookings` | UNRESOLVED — PROPOSED listAdminBookings (P-47); was get_bookings?admin=1 (C-06) | UX-ADMIN-015 | define request/response + errors |
| `GET /api/v1/admin/competitions` | UNRESOLVED — PROPOSED listAdminCompetitions (P-14); was get__competitions?admin=1 (C-07) | UX-ADMIN-027 | define request/response + errors |
| `GET /api/v1/admin/competitions?kind=template` | UNRESOLVED — PROPOSED listAdminCompetitions (P-14), templates DEFERRED | UX-ADMIN-025 | define request/response + errors |
| `GET /api/v1/admin/consents` | UNRESOLVED — PROPOSED listAdminConsents (P-02, needs O-04) | UX-ADMIN-004 | define request/response + errors |
| `GET /api/v1/admin/crm/leads` | UNRESOLVED — PROPOSED listCrmLeads (P-16) | UX-ADMIN-033 | GET leads ?stage → {items[{id,source,stage,consent}]} |
| `GET /api/v1/admin/learners` | UNRESOLVED — PROPOSED listAdminLearners (P-01) | UX-ADMIN-002 | define request/response + errors |
| `GET /api/v1/admin/lessons` | UNRESOLVED — PROPOSED listAdminLessons (P-12) | UX-ADMIN-016 | define request/response + errors |
| `GET /api/v1/admin/library-items` | UNRESOLVED — PROPOSED listAdminLibraryItems (P-17) | UX-ADMIN-037 | GET ?program&type → {items[{id,title,duration_s,approved,low_data_url}]} |
| `GET /api/v1/admin/pay-runs` | UNRESOLVED — PROPOSED listPayRuns (P-13, flag payroll_v1) | UX-ADMIN-021 | GET pay-runs ?period → {items[{id,period,state,totals_by_currency}]} |
| `GET /api/v1/admin/quran-sources` | UNRESOLVED — PROPOSED listQuranSources (P-09, needs O-06) | UX-ADMIN-012 | GET/POST sources {id,name,riwayah,licence_state,approval_state} |
| `GET /api/v1/admin/rewards` | UNRESOLVED — OWNER_DECISION_REQUIRED (O-07), no contract drafted | UX-ADMIN-032 | GET/POST reward definitions |
| `GET /api/v1/admin/rubrics` | UNRESOLVED — PROPOSED listRubrics (P-11) | UX-ADMIN-014 | GET/POST rubric versions {id,version,criteria[{key,weight,levels[]}]} |
| `GET /api/v1/admin/teacher-applications` | UNRESOLVED — PROPOSED listTeacherApplications (P-03) | UX-ADMIN-006 | define request/response + errors |
| `GET /api/v1/admin/teachers` | UNRESOLVED — PROPOSED listAdminTeachers (P-07); was get__teachers?admin=1 (C-05) | UX-ADMIN-007 | define request/response + errors |
| `GET /api/v1/admin/teachers/{teacherId}` | UNRESOLVED — PROPOSED getAdminTeacher (P-06) | UX-ADMIN-008 | GET public teacher profile |
| `GET /api/v1/library-items` | UNRESOLVED — PROPOSED listLibraryItems (P-18) | UX-LEARNER-028 | GET ?program&type → {items[{id,title,duration_s,approved,low_data_url}]} |
| `GET /api/v1/me/notifications` | UNRESOLVED — PROPOSED listMyNotifications (P-24) | UX-LEARNER-030 | GET ?cursor&type → {items[{id,type,title_key,params,created_at,read_at}]} |
| `GET /api/v1/public/legal-documents/{slug}` | UNRESOLVED — PROPOSED getLegalDocument (P-26, content O-01) | UX-PUBLIC-012 | GET /legal/{slug}?market&locale → {version,effective_at,body_html} |
| `GET /api/v1/question-bank-items` | UNRESOLVED — PROPOSED listQuestionBankItems (P-10) | UX-ADMIN-013 | GET/POST question items {id,skill,level,source,quran_ref_id?,status,version} |
| `GET /api/v1/question-bank-items?status=review` | UNRESOLVED — PROPOSED listQuestionBankItems (P-10) | UX-TEACHER-012 | GET/POST question items {id,skill,level,source,quran_ref_id?,status,version} |
| `GET /api/v1/teachers/me/learners` | UNRESOLVED — PROPOSED listMyLearners (P-27) | UX-TEACHER-008 | define request/response + errors |
| `GET /api/v1/teachers/{teacherId}` | UNRESOLVED — PROPOSED getPublicTeacher (P-08) | UX-PUBLIC-006 | GET public teacher profile |
| `POST /api/v1/admin/competitions/{competitionId}/judges` | UNRESOLVED — PROPOSED assignCompetitionJudges (P-15) | UX-ADMIN-029 | POST assignments {judge_id, role, coi_state} |
| `POST /api/v1/auth/password-reset-requests` | UNRESOLVED — PROPOSED requestPasswordReset (P-20) + confirmPasswordReset (P-21) | UX-AUTH-004 | POST {contact} → 202 (no enumeration) |
| `POST /api/v1/public/market-waitlist` | UNRESOLVED — PROPOSED joinMarketWaitlist (P-22) | UX-GLOB-003 | POST {country, email, consent_version} → 202 |
| `POST /api/v1/subscriptions/{subscriptionId}/renewal-consent` | UNRESOLVED — PROPOSED setRenewalConsent (P-23, needs O-02) | UX-GLOB-007 | POST {price_version_id, decision:accept|cancel} |
| `POST /api/v1/teacher-applications` | UNRESOLVED — PROPOSED submitTeacherApplication (P-04) | UX-TEACHER-001 | define request/response + errors |
