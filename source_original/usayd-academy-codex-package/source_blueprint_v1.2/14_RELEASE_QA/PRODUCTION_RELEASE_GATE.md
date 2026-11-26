# Production Release Gate — cannot be signed from specifications alone

## Gate 0 — Product/legal readiness
- [ ] Approved program and academic overseer; Quran content license/edition and verification.
- [ ] Market-by-market legal counsel decision, payments merchant verification, taxes, data transfer, children consent, teacher contracts.
- [ ] True privacy and safeguarding process and dedicated triage owner.
- [ ] Country availability defaults disabled unless approved; no unsupported PSP currency public price.

## Gate 1 — Engineering reliability
- [ ] Actual production code in repository and Docker/container/infra reproducible build.
- [ ] Backwards-compatible migrations, queue retry/DLQ, idempotent webhooks, secret vault and auditing.
- [ ] 100% sensitive endpoints protect roles, scope, owner, consent and purpose by tests.
- [ ] Confirmed UTC/local class and valid DST behavior, KWD/BHD 3 decimal amounts and checkout reconciliation.
- [ ] Provider switching only newly allocated classes; rollback and incident protocol tested.
- [ ] Zero critical/high exploitable bugs in release; dependency/security scans reviewed.
- [ ] Backup restore drill with measured RTO/RPO and monitoring alerts firing.

## Gate 2 — Product UX and accessibility
- [ ] Critical routes Figma approved and implemented for Arabic RTL and English LTR.
- [ ] Desktop/tablet/mobile and Flutter core screens tested on actual devices (if mobile in release).
- [ ] No clipped RTL, numeral, currency or Quranic verse text; WCAG 2.2 AA manual checks tracked.
- [ ] All role-dependent empty, loading, offline, 401/403, market unavailable, provider unsupported, failed payment states work.

## Gate 3 — Academic and AI
- [ ] Quran corpus tests + human academic verification.
- [ ] AI plan versioning, human signoff, explicit confidence/limitations.
- [ ] Policy review no automatic teacher punishment; privacy consent for every audio use, narrow retention.
- [ ] Contests minors privacy, judging conflict, manual appeal and rewards policy independently verified.

## Gate 4 — Commercial and global
- [ ] Approved pricing per active country and currency; PSP test charges and refund tested in each settlement profile.
- [ ] Transactional copy and legal terms translated and validated, local notification content/time correct.
- [ ] Teacher compensation settlement accurately matches attendance and role separation.
- [ ] Unit economics based on paid cohorts, not fictitious demand.

## Deployment acceptance
- Signed release checklist: Engineering Lead, Product Owner, Academic Lead, Privacy/Legal, Security Lead, Ops/Finance for active markets.
- Staging canary deploy with errors, p95 latency, queue lag, authorization failures, payment reconciliation, video join failures monitored.
- Rollback procedure including DB schema compatibility; clear incident escalation and customer communication.
- Re-run critical E2E in production with synthetic nonfinancial test conditions; no unauthorized live payment.

## State
**NOT SIGNED / BLOCKED** until app exists and evidence above is provided. v1.2 package passes documentation validation only.
