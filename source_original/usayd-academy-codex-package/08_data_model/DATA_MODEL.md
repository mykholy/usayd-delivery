# Data model requirements

Authoritative drafts copied alongside: `DATA_DICTIONARY.md`, `GLOBAL_DOMAIN_SCHEMA_v1.2.md`, `STATE_MACHINES.md`. Below: entities each module needs for the designed screens, plus additions required by UNRESOLVED endpoints.

## Invariants
- Money as integer minor units + ISO 4217 (KWD/BHD/OMR exponent 3). Price comes from versioned market price books, never FX conversion.
- Instants stored UTC; participants keep IANA `timezone_id`; recurring availability stored as local RRULE + zone + tzdb version.
- Append-only: audit_events, revision_events, conference_events, contest_score_versions, consent_receipts. Versioned: plans, curricula, rubrics, contracts, price books, routing policies, settings.
- Quran text only via `quran_references` from a licensed source; never stored as free text in reports/questions.

## Entities by module (from DATA_DICTIONARY)
| Module | Entities |
|---|---|
| IAM/PROF | users, learners, learner_guardians, consent_receipts |
| TCHR/PAYROLL | teacher_profiles, teacher_credentials, teacher_availability, teacher_contracts, teacher_accruals, teacher_payouts |
| CURR | programs, curricula, quran_references, question_banks, media_assets |
| PAY/GEO | markets*, price_books*, packages, subscriptions, credit_ledger, payments, payment_webhook_events, invoices, merchant_profiles*, fx_rates* |
| BOOK/VIDEO/ATT | lessons, lesson_participants, conference_sessions, conference_events, attendance_summaries, lesson_reports, video_providers*, video_provider_accounts*, video_capabilities*, video_routing_policies*, video_provider_bindings* |
| ASMT/PLAN | assessments, assessment_evidence, exam_attempts, learning_plans, plan_versions, study_tasks, memorization_segments, revision_events |
| CONTEST | competitions, competition_rounds, competition_registrations, competition_submissions, contest_judgments, contest_score_versions, contest_appeals, awards |
| AI | ai_runs, ai_recommendations, policy_flags |
| SUP/ADMIN | supervisor_assignments*, settings_versions*, translations*, audit_events, support_tickets, safeguarding_cases* |
| CRM/NOTIF | leads, notifications, analytics_events, outbox_messages |

\* defined in `GLOBAL_DOMAIN_SCHEMA_v1.2.md` / `VIDEO_PROVIDER_CONSOLE.md`.

## Additions required by the designed screens (UNRESOLVED — confirm before migrating)
- `waitlist_entries` (country, contact_hash, consent_version, created_at) — UX-GLOB-003
- `legal_documents` (slug, market, locale, version, effective_at, body, approved_by) — UX-PUBLIC-012
- `teacher_applications` (stage, documents, checks) — UX-TEACHER-001, UX-ADMIN-006
- `rubric_versions` (criteria json, weights) — UX-ADMIN-014, UX-TEACHER-010
- `competition_templates`, `reward_definitions`, `judge_assignments (coi_state)` — UX-ADMIN-025/029/032
- `quran_sources` (licence_state, approval_state) — UX-ADMIN-012
- `renewal_consents` (subscription_id, price_version_id, decision) — UX-GLOB-007
- notification inbox read-state on `notifications` (read_at) — UX-LEARNER-030
- `pay_runs` (period, state, totals_by_currency, prepared_by, approvals) — UX-ADMIN-021/022

