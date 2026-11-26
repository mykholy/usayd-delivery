# Permissions matrix (design specification — enforcement is a backend requirement)

Legend: **A** allow · **O** own only · **S** scoped (market/program/assignment) · **M** masked/minimised · **C** consent-gated · **2** a different second approver is required · **R** with recorded reason · **BG** proposed break-glass (D-39) · **–** deny. Combined letters apply together (e.g. **S2**, **SM**).

| Capability | guest | adult_learner | minor_learner | guardian_session | teacher | academic_supervisor | quality_supervisor | competition_moderator | judge | support_agent | finance_supervisor | safeguarding_lead | ops_supervisor | regional_manager | platform_admin | Operations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Browse public catalogue/prices (market-limited) | A | A | A | A | A | A | A | A | A | A | A | A | A | A | A | get__programs, get__api_v1_public_pricing |
| Register / log in | A | A | A | – | A | A | A | A | A | A | A | A | A | A | A | post__auth_register, post__auth_login |
| Read own learner profile & history | – | O | O | – | – | – | – | – | – | – | – | – | – | – | – | get__learners__learnerId |
| Book / reschedule / cancel lessons | – | O | C | – | S | – | – | – | – | – | – | – | S | – | – | post_bookings, cancelBooking |
| Pay / manage subscription | – | O | – | – | – | – | – | – | – | – | S | – | – | – | – | post__api_v1_me_payment_checkouts |
| Decide guardian consent per purpose | – | – | – | O | – | – | – | – | – | – | – | – | – | – | – | decideGuardianConsent |
| Withdraw consent | – | O | – | O | – | – | – | – | – | – | – | – | – | – | – | post__consents__consentId__withdraw |
| View consent queue | – | – | – | – | – | – | – | – | – | S | – | S | – | – | S | listAdminConsents |
| Join live lesson | – | O | C | – | S | – | – | – | – | – | – | – | – | – | – | post__lessons__lessonId__join |
| Write lesson report | – | – | – | – | S | – | – | – | – | – | – | – | – | – | – | saveLessonReportDraft, post__lessons__lessonId__report |
| Read lesson report | – | O | O | – | S | S | S | – | – | – | – | – | – | – | – | getLessonReport |
| Propose learning plan (AI advisory) | – | – | – | – | S | – | – | – | – | – | – | – | – | – | – | post__learning_plans_suggestions |
| Approve learning plan | – | – | – | – | – | S2 | – | – | – | – | – | – | – | – | – | post__api_v1_supervisor_academic_plans_planId_decision |
| List learners (directory) | – | – | – | – | – | S | – | – | – | SM | – | S | S | S | SM | listAdminLearners |
| Reveal learner PII | – | – | – | – | – | – | – | – | – | R | – | R | – | – | R | revealLearnerPii |
| Read safeguarding case | – | – | – | – | – | – | – | – | – | – | – | S | – | – | BG | get__api_v1_supervisor_safeguarding_cases |
| Open safeguarding case | – | A | A | – | A | A | A | – | – | A | – | A | A | – | A | post__api_v1_supervisor_safeguarding_cases (report intake) |
| Judge submission | – | – | – | – | – | – | – | – | S | – | – | – | – | – | – | post__competition_submissions__submissionId__judge |
| Resolve appeal (independent of judge) | – | – | – | – | – | S | – | S | – | – | – | – | – | – | – | postAdminContestAppealResolve |
| Publish competition results | – | – | – | – | – | – | – | S2 | – | – | – | – | – | – | S2 | post__admin_competitions__competitionId__publish |
| Public leaderboard entry | – | C | – | – | – | – | – | – | – | – | – | – | – | – | – | get__competitions__competitionId__standings (minors never listed) |
| Prepare pay run | – | – | – | – | – | – | – | – | – | – | S | – | – | – | – | payroll.prepare |
| Approve pay run | – | – | – | – | – | – | – | – | – | – | S2 | – | – | – | – | post__admin_pay_runs__payRunId__approve |
| Draft price book | – | – | – | – | – | – | – | – | – | – | S | – | – | S | – | post__api_v1_admin_price_books |
| Approve price book / market | – | – | – | – | – | – | – | – | – | – | S2 | – | – | S2 | S2 | post__api_v1_admin_price_books_priceBookId_decision |
| Change video routing policy | – | – | – | – | – | – | – | – | – | – | – | – | S | – | S2 | post__api_v1_admin_video_routing_policies_policyId_decision |
| Assign supervisor roles | – | – | – | – | – | – | – | – | – | – | – | – | – | – | S2 | post__api_v1_admin_supervisor_assignments |
| Edit settings (sensitive keys) | – | – | – | – | – | – | – | – | – | – | – | – | – | – | S2 | post__api_v1_admin_settings_versions_settingsVersionId_decision |
| Read audit trail | – | – | – | – | – | – | – | – | – | – | – | S | – | – | S | get__api_v1_admin_security_access_audits |
| Review privileged access | – | – | – | – | – | – | – | – | – | – | – | S | – | – | S2 | postAccessAuditReview (reviewer ≠ actor) |
| Impersonate (read-only, reason) | – | – | – | – | – | – | – | – | – | R | – | – | – | – | R | not in contract — PROPOSED policy only; audited |
| Export data | – | – | – | – | – | – | – | – | – | – | S | – | – | – | S | createExport (watermark + reason) |

## Negative tests (must exist in the backend suite)
| Area | Attempt | Expected |
|---|---|---|
| Object ownership (BOLA) | Learner A requests GET /learners/{B} | 404, no data, audit sample |
| Market scope | Supervisor (EG) lists SA learners | empty or 403, never SA rows |
| Program scope | Academic supervisor (memorization) approves a tajweed plan | 403 FORBIDDEN_SCOPE |
| Sensitive child data | Support agent opens a minor’s profile without ticket | masked fields only; reveal needs reason + open ticket |
| Audit read | Teacher calls access-audits | 403 |
| Impersonation | Admin impersonates a minor | read-only, reason required, safeguarding-reviewed (policy PROPOSED) |
| Break-glass | Admin opens a safeguarding case without grant | non-revealing 403; with grant → time-boxed, review within 24 h (D-39 PROPOSED) |
| Self-approval | Maker approves own price book / pay run / settings / role grant | 403 SELF_APPROVAL_FORBIDDEN + audit |
| Guardian proxy | Admin grants consent on behalf of a guardian | not possible — no operation exists |
| UI mode | Kids mode client sends ui_mode=professional to unlock competitions | no effect; authorization uses age band + consents only |
