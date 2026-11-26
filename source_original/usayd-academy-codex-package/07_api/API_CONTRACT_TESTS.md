# API contract tests — specifications

Written as executable-looking specifications for the Laravel test suite (Pest/PHPUnit) and a contract runner (e.g. Schemathesis) **once the backend exists**. None has been run: there is no backend.

## P-01 `GET /api/v1/admin/learners` — `listAdminLearners`
- Status: PROPOSED
- ✅ platform_admin within scope → `200` body matches `AdminLearnerRowList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- 📜 audit event `admin.learner_list.viewed (sampled)` written append-only with actor, scope, request_id

## P-02 `GET /api/v1/admin/consents` — `listAdminConsents`
- Status: PROPOSED — NEEDS_APPROVAL · flag `guardian_consent_v1` off until O-04 (verification_method enum)
- ✅ platform_admin within scope → `200` body matches `AdminConsentRowList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-03 `GET /api/v1/admin/teacher-applications` — `listTeacherApplications`
- Status: PROPOSED
- ✅ platform_admin within scope → `200` body matches `TeacherApplicationList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-04 `POST /api/v1/teacher-applications` — `submitTeacherApplication`
- Status: PROPOSED
- ✅ authenticated_user within scope → `201` body matches `TeacherApplicationEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `409` APPLICATION_ALREADY_OPEN
- 📜 audit event `teacher_application.submitted` written append-only with actor, scope, request_id

## P-05 `POST /api/v1/admin/teacher-applications/{applicationId}/decision` — `decideTeacherApplication`
- Status: PROPOSED
- ✅ academic_supervisor within scope → `200` body matches `TeacherApplicationEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `409` SAFEGUARDING_NOT_CLEARED
- ❌ `403` SELF_DECISION_FORBIDDEN
- 📜 audit event `teacher_application.decided` written append-only with actor, scope, request_id

## P-06 `GET /api/v1/admin/teachers/{teacherId}` — `getAdminTeacher`
- Status: PROPOSED
- ✅ platform_admin within scope → `200` body matches `AdminTeacherEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ `404` NOT_FOUND (also returned when out of scope)
- 📜 audit event `admin.teacher_profile.viewed` written append-only with actor, scope, request_id

## P-07 `GET /api/v1/admin/teachers` — `listAdminTeachers`
- Status: PROPOSED
- ✅ platform_admin within scope → `200` body matches `AdminTeacherList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-08 `GET /api/v1/teachers/{teacherId}` — `getPublicTeacher`
- Status: PROPOSED
- ✅ guest within scope → `200` body matches `PublicTeacherEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ `404` NOT_FOUND

## P-09 `GET /api/v1/admin/quran-sources` — `listQuranSources`
- Status: PROPOSED — NEEDS_APPROVAL · flag `quran_source_v1` off until O-06 licensed source + academic authority
- ✅ academic_supervisor within scope → `200` body matches `QuranSourceList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-10 `GET /api/v1/question-bank-items` — `listQuestionBankItems`
- Status: PROPOSED — NEEDS_APPROVAL · flag `` off until O-06 for items that quote Quran text
- ✅ content_editor within scope → `200` body matches `QuestionBankItemList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-11 `GET /api/v1/admin/rubrics` — `listRubrics`
- Status: PROPOSED
- ✅ academic_supervisor within scope → `200` body matches `RubricList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-12 `GET /api/v1/admin/lessons` — `listAdminLessons`
- Status: PROPOSED
- ✅ ops_supervisor within scope → `200` body matches `AdminLessonRowList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-13 `GET /api/v1/admin/pay-runs` — `listPayRuns`
- Status: PROPOSED — NEEDS_APPROVAL · flag `payroll_v1` off until O-08 (calculation rules; list itself is safe)
- ✅ finance_supervisor within scope → `200` body matches `PayRunRowList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-14 `GET /api/v1/admin/competitions` — `listAdminCompetitions`
- Status: PROPOSED
- ✅ platform_admin within scope → `200` body matches `AdminCompetitionRowList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-15 `POST /api/v1/admin/competitions/{competitionId}/judges` — `assignCompetitionJudges`
- Status: PROPOSED
- ✅ competition_moderator within scope → `200` body matches `JudgeAssignmentEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `409` JUDGE_CONFLICT_OF_INTEREST
- 📜 audit event `competition.judges_assigned` written append-only with actor, scope, request_id

## P-16 `GET /api/v1/admin/crm/leads` — `listCrmLeads`
- Status: PROPOSED
- ✅ marketing_admin within scope → `200` body matches `CrmLeadList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-17 `GET /api/v1/admin/library-items` — `listAdminLibraryItems`
- Status: PROPOSED — NEEDS_APPROVAL · flag `library_v1` off until Licensing of each item (FR-MEDIA-001)
- ✅ content_editor within scope → `200` body matches `LibraryItemList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-18 `GET /api/v1/library-items` — `listLibraryItems`
- Status: PROPOSED
- ✅ learner within scope → `200` body matches `LibraryItemList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-20 `POST /api/v1/auth/password-reset-requests` — `requestPasswordReset`
- Status: PROPOSED
- ✅ guest within scope → `202`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 📜 audit event `auth.reset_requested` written append-only with actor, scope, request_id

## P-21 `POST /api/v1/auth/password-resets` — `confirmPasswordReset`
- Status: PROPOSED
- ✅ guest within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- ❌ `410` TOKEN_EXPIRED
- 📜 audit event `auth.password_reset (revokes all sessions)` written append-only with actor, scope, request_id

## P-22 `POST /api/v1/public/market-waitlist` — `joinMarketWaitlist`
- Status: PROPOSED
- ✅ guest within scope → `202`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` MARKET_ALREADY_ACTIVE
- 📜 audit event `market_waitlist.joined` written append-only with actor, scope, request_id

## P-23 `POST /api/v1/subscriptions/{subscriptionId}/renewal-consent` — `setRenewalConsent`
- Status: PROPOSED — NEEDS_APPROVAL · flag `auto_renew_v1` off until O-02 pricing/renewal policy + PSP support
- ✅ learner (payer) within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `subscription.renewal_consent_changed` written append-only with actor, scope, request_id

## P-24 `GET /api/v1/me/notifications` — `listMyNotifications`
- Status: PROPOSED
- ✅ learner within scope → `200` body matches `NotificationList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-25 `POST /api/v1/me/notifications/read` — `markNotificationsRead`
- Status: PROPOSED
- ✅ learner within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`

## P-26 `GET /api/v1/public/legal-documents/{slug}` — `getLegalDocument`
- Status: PROPOSED — NEEDS_APPROVAL · flag `` off until O-01 (content only — contract is safe)
- ✅ guest within scope → `200` body matches `LegalDocumentEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ `404` NOT_PUBLISHED

## P-27 `GET /api/v1/teachers/me/learners` — `listMyLearners`
- Status: PROPOSED
- ✅ teacher within scope → `200` body matches `MyLearnerRowList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-30 `POST /api/v1/booking/slot-holds` — `createSlotHold`
- Status: PROPOSED
- ✅ learner within scope → `201` body matches `SlotHoldEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` SLOT_TAKEN
- ❌ `423` HOLD_LIMIT
- 📜 audit event `booking.slot_held` written append-only with actor, scope, request_id

## P-31 `POST /api/v1/bookings/{bookingId}/cancel` — `cancelBooking`
- Status: PROPOSED — NEEDS_APPROVAL · flag `` off until Credit/forfeit rules per window (O-02 commercial policy)
- ✅ learner within scope → `200` body matches `BookingCancellationEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `409` OUTSIDE_CANCELLATION_WINDOW
- 📜 audit event `booking.cancelled` written append-only with actor, scope, request_id

## P-32 `POST /api/v1/learners/{learnerId}/guardian-invitations` — `createGuardianInvitation`
- Status: PROPOSED — NEEDS_APPROVAL · flag `guardian_consent_v1` off until O-04 verification method
- ✅ learner (minor) / onboarding user within scope → `201` body matches `GuardianInvitationEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `429` TOO_MANY_INVITES
- 📜 audit event `guardian_invitation.sent` written append-only with actor, scope, request_id

## P-33 `GET /api/v1/guardian-invitations/{invitationToken}` — `getGuardianInvitation`
- Status: PROPOSED — NEEDS_APPROVAL · flag `guardian_consent_v1` off until O-04
- ✅ guardian (token) within scope → `200` body matches `GuardianInvitationEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ `410` INVITATION_EXPIRED

## P-34 `POST /api/v1/guardian-invitations/{invitationToken}/decision` — `decideGuardianConsent`
- Status: PROPOSED — NEEDS_APPROVAL · flag `guardian_consent_v1` off until O-04, O-05
- ✅ guardian (token) within scope → `200` body matches `GuardianInvitationEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `410` INVITATION_EXPIRED
- 📜 audit event `consent.recorded (per purpose, policy version)` written append-only with actor, scope, request_id

## P-35 `PUT /api/v1/lessons/{lessonId}/report-draft` — `saveLessonReportDraft`
- Status: PROPOSED
- ✅ teacher within scope → `200` body matches `ReportDraftEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- ⚔ stale If-Match → `412 VERSION_CONFLICT` and the server version is returned
- ❌ `412` VERSION_CONFLICT — returns server draft
- ❌ `409` REPORT_ALREADY_SUBMITTED

## P-36 `POST /api/v1/me/sync-batches` — `submitSyncBatch`
- Status: PROPOSED
- ✅ learner within scope → `200` body matches `SyncBatchResultEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `413` BATCH_TOO_LARGE
- 📜 audit event `sync.batch_applied` written append-only with actor, scope, request_id

## P-37 `POST /api/v1/me/devices` — `registerDevice`
- Status: PROPOSED
- ✅ learner within scope → `201` body matches `DeviceEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`

## P-38 `DELETE /api/v1/me/devices/{deviceId}` — `unregisterDevice`
- Status: PROPOSED
- ✅ learner within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ `404` NOT_FOUND

## P-39 `POST /api/v1/auth/logout` — `logout`
- Status: PROPOSED
- ✅ any authenticated within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 📜 audit event `auth.logout` written append-only with actor, scope, request_id

## P-40 `POST /api/v1/payments/{paymentId}/refund-requests` — `requestRefund`
- Status: PROPOSED — NEEDS_APPROVAL · flag `refunds_v1` off until O-02 refund policy
- ✅ learner (payer) within scope → `201` body matches `RefundCaseEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `409` REFUND_EXCEEDS_REFUNDABLE
- 📜 audit event `refund.requested` written append-only with actor, scope, request_id

## P-41 `POST /api/v1/admin/break-glass-grants` — `postBreakGlassGrant`
- Status: PROPOSED — NEEDS_APPROVAL · flag `break_glass_v1` off until D-39
- ✅ safeguarding_lead within scope → `201` body matches `BreakGlassGrantEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `break_glass.granted (review required within 24 h)` written append-only with actor, scope, request_id

## P-42 `POST /api/v1/admin/security/access-audits/{auditId}/review` — `postAccessAuditReview`
- Status: PROPOSED
- ✅ security_reviewer within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `403` SELF_REVIEW_FORBIDDEN
- 📜 audit event `access_audit.reviewed` written append-only with actor, scope, request_id

## P-43 `POST /api/v1/uploads` — `createUpload`
- Status: PROPOSED
- ✅ authenticated_user within scope → `201` body matches `UploadEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `413` FILE_TOO_LARGE
- ❌ `415` UNSUPPORTED_TYPE

## P-44 `POST /api/v1/admin/learners/{learnerId}/teacher-assignment` — `assignTeacher`
- Status: PROPOSED
- ✅ ops_supervisor within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `409` TEACHER_NOT_ACTIVE
- 📜 audit event `learner.teacher_assigned` written append-only with actor, scope, request_id

## P-45 `POST /api/v1/teachers/me/pay-statements/{statementId}/disputes` — `disputePayStatement`
- Status: PROPOSED — NEEDS_APPROVAL · flag `payroll_v1` off until O-08
- ✅ teacher within scope → `201` body matches `PayStatementDisputeEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `payroll.dispute_opened` written append-only with actor, scope, request_id

## P-47 `GET /api/v1/admin/bookings` — `listAdminBookings`
- Status: PROPOSED
- ✅ ops_supervisor within scope → `200` body matches `AdminBookingList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-46 `GET /api/v1/me/support-tickets` — `listMySupportTickets`
- Status: PROPOSED
- ✅ learner within scope → `200` body matches `SupportTicketRowList`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence

## P-48 `POST /api/v1/admin/exports` — `createExport`
- Status: PROPOSED
- ✅ platform_admin within scope → `202` body matches `ExportJobEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `export.requested (who, when, filters)` written append-only with actor, scope, request_id

## P-49 `POST /api/v1/admin/learners/{learnerId}/pii-reveals` — `revealLearnerPii`
- Status: PROPOSED
- ✅ support_agent within scope → `200` body matches `RevealedPiiEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `pii.revealed (fields, reason)` written append-only with actor, scope, request_id

## P-50 `POST /api/v1/admin/guardian-invitations/{invitationId}/resend` — `resendGuardianInvitation`
- Status: PROPOSED — NEEDS_APPROVAL · flag `guardian_consent_v1` off until O-04
- ✅ platform_admin within scope → `202`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `429` TOO_MANY_INVITES
- 📜 audit event `guardian_invitation.resent` written append-only with actor, scope, request_id

## P-51 `POST /api/v1/admin/programs` — `createProgramDraft`
- Status: PROPOSED
- ✅ content_editor within scope → `201`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `program.draft_created` written append-only with actor, scope, request_id

## P-52 `POST /api/v1/question-bank-items` — `createQuestionDraft`
- Status: PROPOSED — NEEDS_APPROVAL · flag `` off until O-06 for Quran-quoting items
- ✅ content_editor within scope → `201`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `question.draft_created` written append-only with actor, scope, request_id

## P-53 `POST /api/v1/question-bank-items/{itemId}/decision` — `decideQuestionItem`
- Status: PROPOSED
- ✅ teacher (assigned reviewer) within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `403` SELF_REVIEW_FORBIDDEN
- 📜 audit event `question.decided` written append-only with actor, scope, request_id

## P-54 `POST /api/v1/admin/rubrics` — `createRubricVersion`
- Status: PROPOSED
- ✅ academic_supervisor within scope → `201`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `rubric.version_created` written append-only with actor, scope, request_id

## P-55 `POST /api/v1/supervisor/quality-observations` — `recordQualityObservation`
- Status: PROPOSED
- ✅ quality_supervisor within scope → `201`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `quality.observation_recorded` written append-only with actor, scope, request_id

## P-56 `POST /api/v1/admin/contest-appeals/{appealId}/reviewer` — `assignAppealReviewer`
- Status: PROPOSED
- ✅ competition_moderator within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `409` REVIEWER_NOT_INDEPENDENT
- 📜 audit event `appeal.reviewer_assigned` written append-only with actor, scope, request_id

## P-57 `POST /api/v1/me/teacher-change-requests` — `requestTeacherChange`
- Status: PROPOSED
- ✅ learner within scope → `202`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- 📜 audit event `teacher_change.requested` written append-only with actor, scope, request_id

## P-58 `PATCH /api/v1/learners/{learnerId}/goals` — `patchLearnerGoals`
- Status: PROPOSED
- ✅ learner within scope → `204`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- ⚔ stale If-Match → `412 VERSION_CONFLICT` and the server version is returned
- ❌ `409` STATE_CONFLICT
- 📜 audit event `learner.goals_updated` written append-only with actor, scope, request_id

## P-59 `POST /api/v1/me/data-requests` — `createDataRequest`
- Status: PROPOSED
- ✅ learner within scope → `202` body matches `DataRequestCaseEnvelope`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `409` REQUEST_ALREADY_OPEN
- 📜 audit event `privacy.data_request_received` written append-only with actor, scope, request_id

## P-60 `POST /api/v1/admin/video-providers/{providerAccountId}/credential-rotations` — `rotateProviderCredentials`
- Status: PROPOSED
- ✅ security_admin within scope → `202`
- ❌ no token → `401 UNAUTHENTICATED`
- ❌ out-of-scope / non-owner → `403 FORBIDDEN_SCOPE` (or `404` for object reads) — never reveals existence
- ❌ invalid body → `422 VALIDATION_FAILED` with `field` + `code`
- 🔁 same Idempotency-Key + same body twice → one side effect, same response; different body → `409 IDEMPOTENCY_MISMATCH`
- ❌ `409` STATE_CONFLICT
- ❌ `403` SELF_APPROVAL_FORBIDDEN
- 📜 audit event `video.credentials_rotation_requested` written append-only with actor, scope, request_id
