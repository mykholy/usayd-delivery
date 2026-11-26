# Roles & permissions

Authorization is enforced **server-side** on every request: role (RBAC) × scope (market, program, time window) × object ownership/assignment (ABAC) × purpose for sensitive data. UI hiding is never the control.

## Roles
| Role | Sees | Never sees / never does |
|---|---|---|
| Guest | Public site, prices for selected market | Any account data |
| Learner (all ages) | Own data, own lessons/plans/results; minors in limited mode until guardian consent | Other learners’ data; minors cannot pay or join live lessons before consent |
| Teacher | Assigned learners & lessons, own pay | Learner contacts, other teachers’ pay, unassigned learners |
| Academic supervisor | Plans/assessments in scope | Out-of-scope markets/programs; safeguarding cases |
| Quality supervisor | Observations with stated purpose | Media without consent |
| Competition supervisor / judge | Assigned contests, aliases only | Participant identity when blind; own appeals |
| Customer-support supervisor | Redacted support view | Full PII without reason |
| Finance supervisor | Payments, pay runs (second approver) | Approving own preparations |
| Safeguarding officer | Restricted cases | — (all access logged; dual review) |
| Operations supervisor | Schedules, live lesson status | Media streams |
| Platform admin | Configuration within scope | Self-approval; reading secrets; granting guardian consent |

## Permission keys used by the UI (extend in code)
- `video.providers.view`
- `video.providers.configure_draft`
- `video.providers.test_connection`
- `video.providers.activate`
- `video.providers.credentials.rotate`
- `video.provider_policy.rollback`
- `video.lesson.override`
- `video.recording.enable`
- `markets.draft`
- `markets.decide`
- `pricebooks.draft`
- `pricebooks.decide`
- `payroll.prepare`
- `payroll.approve`
- `contracts.draft`
- `contracts.approve`
- `learners.read_masked`
- `learners.reveal_pii (reason)`
- `consents.read`
- `safeguarding.cases.read`
- `safeguarding.break_glass`
- `plans.approve`
- `assessments.approve`
- `contests.manage`
- `contests.judge`
- `appeals.resolve`
- `settings.draft`
- `settings.decide`
- `translations.draft`
- `translations.publish`
- `supervisors.assign`
- `supervisors.revoke`
- `audit.read`
- `ai.policy_flags.resolve`

## Separation of duties
- Proposer ≠ approver for: price books, market activation, video routing, pay runs, contracts, settings, credential rotation.
- Every sensitive action requires a reason (10–500 chars) and writes an append-only audit event.

## Per-screen permission notes
| Screen | Role | Permission note |
|---|---|---|
| `UX-PUBLIC-001` | Guest (public) | Public (guest). |
| `UX-PUBLIC-002` | Guest (public) | Public. |
| `UX-PUBLIC-003` | Guest (public) | Public; only published programs in the visitor’s market. |
| `UX-PUBLIC-004` | Guest (public) | Public. |
| `UX-PUBLIC-005` | Guest (public) | Public; shows only verified, published profiles. |
| `UX-PUBLIC-006` | Guest (public) | Public; PII minimized. |
| `UX-PUBLIC-007` | Guest (public) | Public. |
| `UX-PUBLIC-008` | Guest (public) | Public; no minor names or results. |
| `UX-PUBLIC-009` | Guest (public) | Guest → creates learner account at confirm; minors routed to guardian consent before booking is confirmed. |
| `UX-PUBLIC-010` | Guest (public) | Public. |
| `UX-PUBLIC-011` | Guest (public) | Public; ticket requires contact verification. |
| `UX-PUBLIC-012` | Guest (public) | Public. |
| `UX-AUTH-001` | Guest / onboarding user | Guest. |
| `UX-AUTH-002` | Guest / onboarding user | Learner (minor) — limited mode until consent verified. |
| `UX-AUTH-003` | Guest / onboarding user | Guest. Staff accounts require MFA. |
| `UX-AUTH-004` | Guest / onboarding user | Guest. |
| `UX-AUTH-005` | Guest / onboarding user | Authenticated learner. |
| `UX-LEARNER-001` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-002` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-003` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-004` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-005` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-006` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-007` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-008` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-009` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-010` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-011` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-012` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-013` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-014` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-015` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-016` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-017` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-018` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-019` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-020` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-021` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-022` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-023` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-024` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-025` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-026` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-027` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-028` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-029` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-030` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-031` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-LEARNER-032` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-TEACHER-001` | Guest / onboarding user | Teacher applicant / onboarding teacher. MFA mandatory. |
| `UX-TEACHER-002` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-003` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-004` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-005` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-006` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-007` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-008` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-009` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-010` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-011` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-012` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-013` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-014` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-015` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-016` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-017` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-TEACHER-018` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-ADMIN-001` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-002` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-003` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-004` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-005` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-006` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-007` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-008` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-009` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-010` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-011` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-012` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-013` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-014` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-015` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-016` | Platform admin (scoped) | Ops supervisor; no access to media streams. |
| `UX-ADMIN-017` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-018` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-019` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-020` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-021` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-022` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-023` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-024` | Platform admin (scoped) | Restricted reviewer role; dual review when safeguarding involved. |
| `UX-ADMIN-025` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-026` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-027` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-028` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-029` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-030` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-031` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-032` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-033` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-034` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-035` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-036` | Platform admin (scoped) | Safeguarding officer only; admins without scope see counts only. |
| `UX-ADMIN-037` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-038` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-039` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-040` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ADMIN-041` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-GLOB-001` | Guest (public) | Public. |
| `UX-GLOB-002` | Guest (public) | Public. |
| `UX-GLOB-003` | Guest (public) | Public. |
| `UX-GLOB-004` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-GLOB-005` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-GLOB-006` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-GLOB-007` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-GLOB-008` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-GLOB-009` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-GLOB-010` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-GLOB-011` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-GLOB-012` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-GLOB-013` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-GLOB-014` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-GLOB-015` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-GLOB-016` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-GLOB-017` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-VPC-001` | Platform admin (scoped) | video.providers.view |
| `UX-VPC-002` | Platform admin (scoped) | video.providers.credentials.rotate (security custodian, dual control) |
| `UX-VPC-003` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-VPC-004` | Platform admin (scoped) | video.providers.configure_draft |
| `UX-VPC-005` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-VPC-006` | Platform admin (scoped) | video.providers.activate (proposer + different security/ops approver, MFA) |
| `UX-VPC-007` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-VPC-008` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-VPC-009` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-VPC-010` | Teacher | Teacher — only assigned learners/lessons; PII minimized (no learner contact details). |
| `UX-SUP-001` | Supervisor (scoped) | Supervisor — effective scope (role × market × program) + object ownership + assigned work; no self-approval; out-of-scope records denied server-side. |
| `UX-SUP-002` | Supervisor (scoped) | Supervisor — effective scope (role × market × program) + object ownership + assigned work; no self-approval; out-of-scope records denied server-side. |
| `UX-SUP-003` | Supervisor (scoped) | Supervisor — effective scope (role × market × program) + object ownership + assigned work; no self-approval; out-of-scope records denied server-side. |
| `UX-SUP-004` | Supervisor (scoped) | Safeguarding officer only. Others get a non-revealing 403; break-glass is a proposed, reviewed operation (D-39). |
| `UX-SUP-005` | Supervisor (scoped) | Supervisor — effective scope (role × market × program) + object ownership + assigned work; no self-approval; out-of-scope records denied server-side. |
| `UX-SUP-006` | Supervisor (scoped) | Supervisor — effective scope (role × market × program) + object ownership + assigned work; no self-approval; out-of-scope records denied server-side. |
| `UX-SUP-007` | Supervisor (scoped) | Supervisor — effective scope (role × market × program) + object ownership + assigned work; no self-approval; out-of-scope records denied server-side. |
| `UX-SUP-008` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-SUP-009` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-SUP-010` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-SUP-011` | Platform admin (scoped) | Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver. |
| `UX-ENG-001` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-ENG-002` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-ENG-003` | Learner | Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation. |
| `UX-MOBILE-000` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-001` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-002` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-003` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-004` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-005` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-006` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-007` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-008` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-009` | Teacher (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-010` | Teacher (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-011` | Learner (Flutter) | Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1. |
| `UX-MOBILE-012` | Learner (Flutter) |  |
| `UX-MOBILE-K02` | Learner (Flutter, Kids mode 6–12) |  |
| `UX-MOBILE-K05` | Learner (Flutter, Kids mode 6–12) |  |
| `UX-MOBILE-K08` | Learner (Flutter, Kids mode 6–12) |  |
| `UX-MOBILE-K11` | Learner (Flutter, Kids mode 6–12) |  |
| `UX-MOBILE-S02` | Learner (Flutter, Simple mode 60+) |  |
| `UX-MOBILE-S04` | Learner (Flutter, Simple mode 60+) |  |
| `UX-MOBILE-S11` | Learner (Flutter, Simple mode 60+) |  |
