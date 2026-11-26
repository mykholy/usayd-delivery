# International, provider and supervisor QA plan — v1.2

## Coverage
`INTERNATIONAL_E2E_SCENARIOS.csv`: detailed 60 scenarios, with actor, initial data, stimulus and expected behavior. Existing `test_cases.csv`: positive/negative traceability for every 216 functional requirement. Gherkin and existing test files are **templates/spec checks**, not evidence that Laravel/Flutter is implemented.

## Test layers
**Unit (Pest/PHPUnit):** Money amount_minor with ISO scale; price version lookup; currency mismatch; timezone overlap/gap; normalized charge quote; compensation rules fixed/hour/lesson/shift/hybrid; ABAC; settings precedence; routing capability matrix; admin two-person approval; clean vs contaminated AI learning suggestion.

**Integration (Laravel MySQL Redis):** amount and webhook signature verification, idempotent quote+payment, transaction-level teacher locks, region scope policy, notifications, IP preference override, user preference persistence, provider sandbox credential exchange and webhook normalization.

**Contract (OpenAPI and vendor-specific):** no undocumented fields, proper 400/401/403/404/409/422/429, localized error codes, vendor account connectivity, capabilities per client and market, payment PSP request/response snapshots.

**E2E (Playwright web):** AR/EN public→price→assessment→checkout; timezone dropdown DST; teacher availability overlap; video admin vendor switching with two approvals; supervisor cross-region 403; contest deadline and appeal, responsive at 360/390/768/1440 and keyboard flow.

**Flutter (unit/widget/integration):** timezone/currency parity with API, intl/currency formatting, provider client per device, offline autosave and sync conflicts, playback accessibility, Arabic shaping and app state restoration.

**Media/video PoC:** every provider (separate adapter), Egypt↔Saudi network, Safari/iOS/Android, 4G loss, audio-only, join token leakage attempt, external Meet link, webhook replay, participant moderation, cost/participant-minute, raw audio permissions evidence. **No claim of equivalence**.

**Security:** OWASP API Top 10/ASVS, credential vault and rotation, injection, XSS, SSRF through provider endpoints, cross-user booking/grades, minors privacy, purpose/consent withdrawal, region access, audit tamper, forged signed webhooks, SAST/SCA/DAST, dependency lockfiles.

**AI/academic:** approved Quran corpus integrity hashes, no hallucinated Quranic text, teacher approval and evidence, recitation ASR benchmark by accent/age/noise (subject to lawful access), false-positive/false-negative policy alerts, bias and fairness tests, support to contest appeal and privacy deletion.

**Nonfunctional:** P95 API latency and error budget agreed before testing; load at target concurrent rooms and real provider quotas; backup restore drill, retry storms, webhook backlog, time synchronization, queue worker failure, data retention jobs and consent withdrawal; client memory and bandwidth budgets.

## Fixtures
- Countries EG/SA/AE/KW/QA/BH/OM/GB/US; statuses active/sandbox/paused/waitlist.
- Price books EGP 799.00 (79900 minor), SAR 79.00 (7900), KWD 7.500 (7500); all fixtures are synthetic and never public published prices.
- Timezones Africa/Cairo, Asia/Riyadh, Asia/Dubai, Europe/London, America/New_York; DST fold/gap.
- Roles learner, minor with documented guardian, teacher, academic, regional, quality, safety, contest judge, finance maker/checker, support, super admin, denied outsider.
- Providers `livekit`, `videosdk`, `daily`, `zoom_video_sdk`, `zoom_meeting`, `google_meet`; capability states `verified`, `unsupported`, `unknown`; no real credentials in files.

## CI pipeline gates
Stage 1 spec audit + OpenAPI lint + locale parity + source link integrity + Jira traceability.
Stage 2 format + static analysis + migrations + unit tests and coverage by domain.
Stage 3 ephemeral integration DB/Redis + policies+contract tests + auth money webhook tests.
Stage 4 Playwright and Flutter smoke tests AR/EN + responsive, developer test accounts only.
Stage 5 security scan + privacy retention + AI benchmark signed review + 2 video providers PoC.
Stage 6 deploy staging, canary metrics, rollback drill, supervised UAT signoffs.

**Proposed zero-tolerance:** any cross-learner/region leakage; any unapproved minor access/audio; double charge; mismatch in charged currency/amount; leaked vendor secret; AI-public Quran corruption; automated sanction or published unreviewed contest result; silent provider switch to unsupported feature; wrong UTC appointment.

## Evidence for release
Immutable CI URLs/job IDs, precise test command/outcome, coverage diff, test dataset provenance, PoC latency and legal permission outcomes, code review signoff, screenshots/video of Figma and running app, signed academic and privacy review, rollback log and open defect list.
