# Automation and pull-request gates for 3 independent repos

## Jira → Gemini → GitHub → CI → Merge → Jira

1. Jira ticket marked Ready **only** when approved scope, repository, dependencies and owner decisions are satisfied.
2. Gemini/Codex runner reads exactly one READY ticket and referenced original specs, creates feature branch in the owning repository, implements tests+code and opens PR.
3. GitHub Actions verifies per-repo test matrix and emits check result. No runner may write fabricated pass statuses.
4. Separate review checks adherence to FR/Screen/Operation, security, performance, i18n, negative cases and data privacy; reviewer comments on PR.
5. Protected ruleset controls merge. Low-risk tasks *may* use GitHub Auto-merge only when all required real approvals, CI, vulnerability gates and restrictions pass. No automatic approval by author or agent pretending to be human.
6. Merge event fires Jira status update using an authorized GitHub App or Jira Automation; rejected/failed PR returns In Progress with linked CI log. The agent must not mark Done before actual merge.
7. API repository publishes versioned OpenAPI artifact with SHA on release; consumer repositories open separate SDK upgrade PRs. Avoid coordinated unreviewed multi-repo merges.

## Required checks by repository
- API: `composer validate`, `laravel pint --test`, static analysis (configured), MySQL 8.4+Redis backed Pest, migration from clean schema, OpenAPI lint, dependency scan, race/ABAC tests on sensitive PRs.
- Web: `pnpm install --frozen-lockfile`, eslint/typecheck, build, Playwright desktop/mobile AR/EN light/dark, accessibility, visual regression, security lint; no API mocks in staging smoke.
- Flutter: `flutter pub get`, `dart format --output=none --set-exit-if-changed .`, `flutter analyze`, `flutter test`, golden tests, integration tests on supported devices, signing review.

## Safe workflow triggers
- `workflow_dispatch` or a tightly authorized Jira automation event to an externally configured Gemini runner. Minimum GitHub scopes and bounded concurrent jobs (`concurrency: usayd-${repo}-${ticket}`) to prevent conflicting code changes.
- Do not place an LLM API key in PR context or send secrets to untrusted forks. GitHub Actions uses least-privileged GitHub Apps, audited access, protected environments, no `pull_request_target` code execution from untrusted branches.
- Max one issue/PR per job; stop and notify on missing permissions, unapproved API, failed test, blocked workflow or unavailable data.
- Require human approval for minors, consents, Quran rights, payment, payroll, AI voice, record handling, production deploy, IAM/ABAC and destructive data migrations.

## Jira and GitHub state mapping
Ready → In Progress (branch exists) → Code Review (PR opened) → QA (CI green and reviewer approved) → Done (merged and deployed/verified if required). If blocked, status/flag Blocked, record decision ID and next owner action.

## No false claims
This package includes a specification of the automation protocol and import/sync scripts. **It does not provision the runner, secrets, GitHub repositories, CI, or Jira issues automatically.** Actual execution requires connected tools and explicit approval gates.
