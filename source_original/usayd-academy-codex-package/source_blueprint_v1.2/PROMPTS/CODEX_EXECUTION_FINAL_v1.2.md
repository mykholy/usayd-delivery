# Codex end-to-end project execution prompt — paste with whole v1.2 archive
Act as staff engineer and independent QA lead. The package is **a specification**, not code. Create working Laravel API, Next.js/web frontend and (separately phased) Flutter apps with fully tested flows. Read `AGENTS.md`, `00_START_HERE/FINAL_HANDOFF_v1.2.md`, full requirements, user stories, diagrams, UX specs, OpenAPI and QA plan before coding.

## Deliver in ordered verified vertical slices
A. Repo/workspace, verified framework versions, lockfiles, CI, DB migrations, auth/RBAC and contracts.
B. Market selector, locale, timezone, pricebook, quote, PSP eligibility, tests including currency decimals and DST.
C. Teacher availability, class booking/attendance, configurable per-provider adapter and admin switch wizard; start with one fully verified vendor and contract stubs for others marked unsupported until real PoCs.
D. Learning programs/Quran reader verified content, tutor assignments, assessment, reviews and study progress.
E. Supervisor portal academic/quality/safety/contest/finance scopes, 2-person approvals.
F. Competitions/challenges and adaptive study/AI under academic+privacy evaluation gate.
G. Flutter consuming API contract, both locales, offline recovery and vendor client compatibility.
H. Performance, security, backup restore, UAT, legal operational signoff and release evidence.

## Execution contract
One Jira Story at a time (plus needed linked QA Task), create actual code/diffs/migrations/API DTOs/validation/policies/jobs/docs/tests, run available commands, include exact outputs and what remains untested, commit through approved workflow. Do not invent Figma assets or release claims. If capability uncertain, use an ADR and feature flag, fail closed for recording/raw audio and child data. Respect developer source-of-truth and real provider SDK documentation; do not hard-code a mock API pretending to be production.

## Guardrails
- Country/IP geolocation suggestion cannot set legal billing identity. No hardcoded USD->EGP conversion. Price is market version and charge_currency settled only by eligible PSP merchant.
- All lesson instants UTC, recurrence in teacher IANA zone with DST fold/gap handling.
- Provider settings require connection verification/dry-run/dual approvals; existing rooms remain bound; external Meet/Zoom has less embedded/AI capability than native SDK.
- No unauthorized exposure for regional supervisors; complete separation for minors' consent and session audio. Never automatically penalize teachers from AI flags.
- Quran canonical text verified academic dataset; any AI plan or Tajweed judgement is draft, teacher approved.
- Refund and payroll immutable signed ledger snapshots, idempotent webhooks, no double class payment.
- Real tests for EGP/SAR/KWD, Egypt/UK/US DST, AR/EN, role scoping, provider switch, lessons, contests, AI consent, mobile.

## Required completion evidence per story
File paths, tests commands and real outputs, screenshots or links when available, trace IDs, requirement/user flow, API contract diff, security threat addressed, migration and rollback, reviewer signature, blocked checks listed. Tests to run: Pest/PHPUnit+static analysis+API contract, Playwright AR/EN+responsive+accessibility, Flutter tests (when code exists), OWASP/secret scan/restore drills before production.

## Final success condition
A production deployment may only be marked Ready after passing `14_RELEASE_QA/PRODUCTION_RELEASE_GATE.md` with named human approvals. This prompt authorizes no unreviewed production payment, rollout or deployment.
