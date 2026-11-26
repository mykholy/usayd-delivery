# QA, test and release gate strategy

## Scale

- **148 functional requirements**, each with baseline positive/negative test IDs = 296 requirement test cases.
- **40 deep adversarial E2E cases** are in `test_cases.csv` (total 336 rows).
- **119 UX screens** with required visual/permission/loading/error/RTL/mobile acceptance states.

## Test pyramid

Unit: domain money/credits/timezone/revision/score rules; property-based money and score invariants; contract tests for video and payments; integration: DB concurrency, outbox/webhooks, rights, consent; E2E: registration→paid lesson→revision, contest→appeal, teacher pay→reconcile; load: booking races and vendor rooms; security: OWASP API Top 10, token abuse and logging PII; accessibility: WCAG 2.2 AA; academic: verified Quran source and rubric; AI evaluation: false correction and false policy flags.

## Release gating by roles

- Product accepts journeys and UX.
- Academic supervisor signs Quran sources, rubric, plans and competition rules.
- Legal/privacy signs minors and audio purposes, public contest, prize and reward policies.
- Finance signs payment settlement/payroll formulas/credits.
- CTO signs provider POC, incident runbooks, security; QA signs test evidence.

## Target UAT journeys

1. Adult starts independently → assessment → paid subscription → books class → joins embedded/external provider → teacher report → due revision → renews.
2. Minor starts account → legal guardian consent proof → eligible lesson → consent withdrawn → optional audio stops.
3. Teacher applies/vetted → opens shift/slots → attends → reports → compensation paid under each chosen contract model.
4. Admin creates contest → academic/legal approve → learner enters → exam or oral judgement → private scores → appeal → corrected result and award.
5. AI proposed plan from verified assessment → teacher edits and approves → learner gets adapted due reviews → follow-up supervised exam changes plan.
6. Video outage and payment outage resolution without losing a lesson or charging twice.

## Performance and disaster testing

Staging dataset seeded synthetic and license-safe; 500 concurrent API reads, 100 concurrent booking attempts for same slot, 50 concurrent rooms vendor POC (may require vendor capacity), checkout load using payment sandbox, queue backpressure 1000 jobs, restore drill. Load targets subject to actual infrastructure and negotiated SLA. Record p50/p95/p99 and error counts. Do not mislabel scenario as a measured benchmark.

## Code and data checklists

API auth object-level checks; all financial decimal minor-unit handling; Quran content checksum/source; model output schema/version; no audio without consent; no public minors identity; no unapproved educational grade; no contest pay-to-win; no duplicate payouts; UI AR/EN; auditable corrective actions.

## Production release blocker list

Unreviewed legal child consent, no verified content rights, high-severity safeguarding issue unresolved, negative or double credit possible, inability to reconcile payment webhooks, cross-learner read, unsafe recording behavior, unreviewed competition score publishing, unsupervised AI tajweed verdict, broken provider join on supported mobile device.
