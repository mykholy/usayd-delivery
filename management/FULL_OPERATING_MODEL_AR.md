# Usayd Academy — Operating Model (3 repositories)

## Source of truth
- Product/UX/SRS: `source_original/usayd-academy-codex-package/` (READY, byte-for-byte except font binaries). Never copy older drafts into it.
- Work scheduling: `planning/tasks/*.md` (707), `planning/sprints/*.md`, `planning/DEPENDENCIES.csv`. Jira receives and tracks actual keys.
- Engineering: independent `usayd-api` (Laravel/MySQL), `usayd-web` (Next.js), `usayd-flutter` (Flutter). Shared contract = published versioned OpenAPI from API repo, consume generated SDKs pinned to a release SHA.
- Product decisions: `DECISION_REQUIRED_FROM_OWNER.md`; default DENY/feature OFF for undecided payment, guardian, recording, legal, prizes and Quran-content areas.

## Team
- Full Stack lead owns API and Web; one Flutter developer owns Mobile; Gemini/Codex assists both. Two human engineers cannot review their own PRs as independent reviewers.
- One code change per ticket/PR/repo. If a logical feature spans repositories, create an API PR → publish contract → Web/Mobile integration PRs.
- Sprint duration two weeks; 91 candidate sprint batches are a *backlog estimate*, not 91 approved schedule commitments. Activate two future sprints maximum and replan from velocity every sprint.

## Workflow
1. Owner approves domain decisions or marks explicit feature flag.
2. QA/readiness checks ticket dependencies, source references, OpenAPI contract, test ownership; move ticket to Ready.
3. Gemini/Codex reads full source, works in a dedicated limited-permission checkout, creates `feat/USYD-T0000-slug`.
4. Local tests first, then focused PR with screenshots, migration notes and traceability.
5. CI runs exact per-repo tests; independent Gemini diff review reads patch as untrusted content and flags risk; CODEOWNERS and human review apply to sensitive changes.
6. Re-run checks on changes; GitHub auto-merge ONLY after configured ruleset, required approvals and checks permit it. Manual oversight of security, consent, legal and production changes is required.
7. After real merge SHA and staging smoke, update Jira and unblock dependent tasks. Never set Done on merely open PR.
8. Feature complete only after API contract + UI integration + mobile interaction + E2E and UAT, not on screen count.

## Tickets
Each ticket's stable ID (`USYD-T####`) remains immutable even when Jira allocates a different key. Preserve both in PR title and description. Avoid duplicating on re-import.

## Release gates
- G0: 3 repos, secrets, license checks, database/redis, verified CI and protected main.
- G1: real adult onboarding, public catalog, login, teacher management, scheduling incl. DST.
- G2: lesson join, attendance, authorized reports, learning plans/revision, web+mobile integration with MySQL.
- G3: authorized billing/child consent/content release and restricted features only after explicit owner approval.
- G4: security, privacy, accessibility and measured performance, recovery, UAT, incident plan.
