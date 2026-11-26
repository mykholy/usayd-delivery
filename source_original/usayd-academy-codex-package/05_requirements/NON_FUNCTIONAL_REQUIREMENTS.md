# Non-functional requirements / quality attributes

**Targets are design acceptance targets, not measured production results.**

| ID | Dimension | Measurable target and method | Phase |
|---|---|---|---|
| NFR-001 | Availability | Paid booking, auth and current schedule target >=99.9% monthly excluding announced windows; error budget by SLO | P0 |
| NFR-002 | Performance | p95 cached GET <=500ms and p95 normal write <=800ms in load-test baseline excluding vendor wait; test p99 too | P0 |
| NFR-003 | Scalability | Initial load test 500 concurrent app users; 50 concurrent classrooms by vendor POC; scale targets revised with real demand | P0 |
| NFR-004 | Mobile responsive | 360/390px core screens, tablet 768, desktop 1440 without overflow or unreadable Quran text | P0 |
| NFR-005 | Accessibility | WCAG 2.2 AA design/implementation target, keyboard navigation, labels, touch targets, focus and audio alternatives | P0 |
| NFR-006 | Localization | Arabic RTL default, English LTR, localized numbers/prices and IANA timezone conversions | P0 |
| NFR-007 | Security | OWASP API Top 10 threat coverage, BOLA tests, rate limits, secrets hygiene, MFA for privileged accounts | P0 |
| NFR-008 | Privacy | Purpose-specific consent, minimization, retention tiers, access requests and cross-border transfer assessment | P0 |
| NFR-009 | Safeguarding | Human incident queue, minors restrictions, response on urgent reports per operational policy and audit trails | P0 |
| NFR-010 | Recoverability | Encrypted backups, restore test each release cycle; pilot RPO<=24h RTO<=8h to be negotiated | P0 |
| NFR-011 | Observability | Traces/correlation ids, payment/video/AI separate dashboards, privacy-safe logs with short TTL | P0 |
| NFR-012 | AI reproducibility | Every output stores prompt/model version, evidence refs, token/minute costs and human approval state | P1 |
| NFR-013 | AI safety | No auto sanctions, no unreviewed religious verdict, quality evaluations by segment and age before rollout | P1 |
| NFR-014 | Billing correctness | Idempotent externally-triggered mutations, double-approval payout, immutable ledger events | P0 |
| NFR-015 | Concurrency correctness | Scheduling locks prevent double bookings and credits consumed twice under racing requests | P0 |
| NFR-016 | Provider reliability | Degraded feature flags and failover/rebooking runbooks for vendor downtime | P0 |
| NFR-017 | Data integrity | Content Q/A, curriculum revisions, verse references (surah:ayah ranges, riwaya), historical evaluations unchanged | P0 |
| NFR-018 | Auditability | Sensitive admin changes, contest scoring, appeals and AI flags retain actor/timestamp/reason | P0 |
| NFR-019 | Tests | Core mutation integration + E2E user journeys, test coverage of high-risk branches and vendor contract harness | P0 |
| NFR-020 | Cost controls | Vendor spend caps and alerts by domain (video/AI/notifications/media) with per-learner allocation | P1 |
| NFR-021 | No lock-in | Provider interface has documented capability matrix and adapter contract tests | P0 |
| NFR-022 | Analytics quality | Signed source events and consistent cohort grain; no pseudo-precision in educational effectiveness | P1 |
| NFR-023 | Contest fairness | Human adjudication, eligibility/audit, age and level stratification, pseudonym privacy, no pay-to-win | P1 |
| NFR-024 | App release readiness | Flutter secure storage, deep links, push controls, background audio and app-store policy review | P2 |

## Proof before production

Performance tests with synthetic learner and teacher schedules, on 2G/3G emulated links and Android budget devices; privacy DPIA; vendor webhook replay test; backup restoration; security penetration test; accessibility audit; game fairness review; AI evaluation for Arabic/quran recognition (separately).
