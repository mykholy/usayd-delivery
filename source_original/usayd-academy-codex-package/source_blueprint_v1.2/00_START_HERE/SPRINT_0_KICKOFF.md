# Sprint 0 — start real implementation safely

## Day 1 — owner decisions
Product/academic/legal/finance sign draft scope and document unresolved blockers. Confirm entity/brand/domain, approved Quran corpus, actual payment provider sandbox, video PoC credentials, minor safeguarding policy, teacher employment classification. Never store keys in prompt, Figma, Jira or repository.

## Day 2 — technical groundwork
Codex scaffolds repo directories `/backend /web /mobile /infra /docs /tests` and selects current vendor-supported versions. Write ADR version pins + lockfiles; containerized DB/Redis, local .env.example placeholders, database migrations, HTTP health/status endpoint, request ID/log redaction, tenant/role policy skeleton. No production deploy.

## Day 3–4 — real vertical slice
Adult learner sign-up/login/verification → level assessment request → program & verified teacher catalog → booking with fake credits → join sandbox video with authenticated scoped token → teacher report. Write tests first and execute. Minor consent gate separately tested before opening to minors.

## Day 5 — quality gate
Run Linux CI, API schema, PHP unit/integration, frontend build, E2E smoke on staging/sandbox, permission abuse tests, QA evidence. Product, Academic, Legal, CTO review. Fix defects before Sprint 1.

## Jira ready definition
Each issue: accountable owner, phase, linked FR and UX ID, exact API paths, data invariants, acceptance Gherkin, security/consent, test setup and CI command, definition of done, rollback. Unknown major vendor/legal behavior is `Blocked` with decision ticket.
