# Test strategy v1.1: SPEC validation vs REAL PRODUCT verification

## Honest status
The shipped runnable Python tests verify documentation, IDs and OpenAPI conventions. **They cannot verify Laravel or mobile features until code exists.** `test_cases.csv` is a test registry, not execution evidence. Test outcome column `Not Run` until CI actually executes.

## Required implementation suites
| Level | Tool | P0 target | Gate |
|---|---|---|---|
| Unit | Pest/PHPUnit + PHPStan | Policies, credits, money/payroll, clocks, contest scoring, plan versioning | no red |
| API integration | Laravel tests with MySQL/Redis/queue fake | transaction locks, idempotency, webhooks, ACL, guardian revocation | no red |
| Contract | OpenAPI lint + Schemathesis/Dredd as approved | typed request/response + authenticated/public routes | no mismatch |
| Web E2E | Playwright | adult/minor, checkout sandbox, booking/join, teacher report, exam, contest appeal | no critical fail |
| Flutter | `flutter test` + integration_test | secure auth, RTL, state restoration, permissions and provider joins | Android/iOS smoke |
| Security | composer audit, npm audit, SAST, secret scan, OWASP API test | no unresolved critical/high exploitable vulnerability |
| Load & resilience | k6/Locust sandbox | slot race, retries, queue failure, vendor outage; p95 and throughput recorded | agreed SLA |
| Accessibility | axe-core + manual screen reader | WCAG 2.2 AA, 200% zoom, RTL/LTR | no blocking defect |
| AI evaluation | approved blind labeled set | safety false pos/neg, educational accuracy, redaction, cost | human signoff |
| Academic | teacher proof-checks | canonical Quran script, riwaya, rubric, exam content | zero unverified public text |

## TDD implementation pattern
For every story: write failing test from FR ID → minimal domain implementation → tests unit/integration → endpoint contract → UI E2E/semantics → performance/security where relevant → PR evidence. Use fake payment/video provider with deterministic clock, not real charges.

## Evidence required for a release
Build SHA, config/version, execution date, command+exit code, test counts/pass/fail/skip, artifact links (JUnit, screenshots, traces, coverage), risk acceptance and reviewers. A SKIP does not equal PASS. Treat failures in core money, minors consent, IDOR, Quran source, contest grade, audio disclosure as release blockers.

## Critical scenarios to automate
- verified adult signs up independently and pays, books, joins and receives approved lesson report;
- minor without verified consent is blocked at relevant gate;
- parallel last-credit/last-slot reservation resolves to one booking;
- fake/replayed payment webhook never creates double credits;
- teacher absence and provider outage do not consume an unearned lesson;
- teacher plan suggestion must be reviewed; revoked consent cancels queued AI processing;
- race in exam submissions cannot duplicate or exceed time; appeal does not erase score history;
- contest tie, rubric version, judge conflict and minor leaderboard privacy;
- staff RBAC/IDOR, audit export redaction, payroll signature and replay;
- fallback Google Meet/Zoom mode has no false raw audio feature.

## Mobile test matrix
Android 9+, current Android; iOS supported minimum defined after Flutter project creation; offline/background mic permission/reconnect, screen rotations, status bar inset, large text, talkback/voiceover, two devices same account, timezones, Arabic/English. Pin actual OS/device matrix before store release.
