# DevOps, observability and production runbook

## Environments and release strategy

`local → test-ci → staging → production`. Separate credentials and provider projects. IaC for database/Redis/storage/secrets, encryption, network restrictions, firewalls and automated restore tests. Blue/green or rolling with backward-compatible migrations; feature flags for AI/competitions. No production student data in staging.

## CI/CD gates

1. Lint, static analysis (PHPStan/Larastan, ESLint/TypeScript), dependency/security scan, OpenAPI schema lint, data migration dry run.
2. Unit/integration/contract + concurrency tests; visual regression for UX, accessibility automated tests and manual check.
3. Staging paid checkout with sandbox webhook replay; vendor join and disconnect; data retention test.
4. Business approval for price/payment changes, finance approval for payroll, academic approval for Quran text/rubric, privacy approval for recording/AI changes.
5. Deploy with rollback and smoke tests, alert routing, release notes and audit snapshots.

## Operations SLO and alerting

- Auth/paid booking p95 and error rate; server-side payment webhook delays; video join success and reconnection failures.
- Teacher no-show threshold; support response queue; safeguarding incident fast escalation.
- AI cost per learner/week; quota and model drift; audio jobs stuck; hallucinated verse detection 0 allowed.
- Competition scoring backlog/duplicate attempt/appeals; payout discrepancies; security WAF abuse.

## Incident playbooks

**Video vendor outage:** stop new affected lesson creation → show outage banner → offer verified fallback/credit → status update → reconcile attendance and payouts → RCA.

**Payment misfire:** disable checkout attempt repeat if webhook uncertain → inspect idempotency store → reconcile provider statement → issue correction transaction → notify affected users.

**AI inappropriate recommendation:** disable feature flag → quarantine outputs → notify academic reviewer → repair and retest model/prompt → optionally correct published plan.

**Minor data leak/safeguarding:** isolate access → preserve minimal investigation evidence → privacy/legal/safety escalation → notifications per applicable law → restore least privilege → post-incident improvements.

**Contest integrity issue:** freeze provisional results and prizes → review audit trail → independent judge → corrected results with explanation and appeals.

## Backups and rollback

Encrypted DB snapshots and object storage versioning with privacy-compatible retention; test restoration in isolated staging on cadence and after schema changes. Reconcile job queue messages/financial ledger when restoring; never restore paid state without comparing external provider.
