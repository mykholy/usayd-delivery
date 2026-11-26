# Pull Request Review & Approval Queue
**Project:** Usayd Platform (`USYD`)  
**Status Date:** November 24, 2026  
**Governance Policy:** In accordance with P0 safety guidelines, automated unattended merging is disabled on personal private repositories lacking branch protection rules. All pull requests affecting sensitive files (workflows, database schemas, authentication, security, authorization, and build configs) are intentionally held open by the `human-approval-gate` for genuine human sign-off.

---

## 1. Summary of PRs Awaiting Human Review

- **Total Open PRs in Review:** 15
  - `usayd-api`: 10 open PRs (PR #2 through PR #11)
  - `usayd-flutter`: 6 open PRs (PR #1 through PR #6 — assigned to Ahmed Mamdouh El-Sayed)
- **CI Health:** 100% Green on all automated checks (Pint, Formatter, Static Analysis, MySQL 8.4 tests, Flutter tests).

---

## 2. Detailed Approval Queue by Repository

### 2.1 Backend Repository: `usayd-api`

| PR | Jira Key | Task ID | Branch | CI Check | Gate Status | Sensitive Files / Approval Rationale | Quick Approval Command |
|---|---|---|---|---|---|---|---|
| **#2** | - | `GOV-REPAIR` | `fix/governance-ci-and-review-repair` | **PASS** | `AWAITING SIGN-OFF` | `.github/workflows/ci.yml` governance repair. | `gh pr review 2 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#3** | **USYD-55** | `USYD-T0022` | `feat/USYD-T0022-modular-monolith-adr` | **PASS** | `AWAITING SIGN-OFF` | Architecture governance ADR files added. | `gh pr review 3 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#4** | **USYD-56** | `USYD-T0023` | `feat/USYD-T0023-laravel-bootstrap` | **PASS** | `AWAITING SIGN-OFF` | `composer.json` dependencies, Laravel bootstrap, MySQL 8.4 CI runner. | `gh pr review 4 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#5** | **USYD-57** | `USYD-T0024` | `feat/USYD-T0024-mysql-schema-foundations` | **PASS** | `AWAITING SIGN-OFF` | Database migrations and base schema foundation. | `gh pr review 5 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#6** | **USYD-58** | `USYD-T0025` | `feat/USYD-T0025-concurrency-harness` | **PASS** | `AWAITING SIGN-OFF` | Middleware, transaction deadlock retries, idempotency tables. | `gh pr review 6 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#7** | **USYD-59** | `USYD-T0026` | `feat/USYD-T0026-redis-queue-lifecycle` | **PASS** | `AWAITING SIGN-OFF` | Horizon config, Redis queue partitions, and failed job CLI. | `gh pr review 7 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#8** | **USYD-66** | `USYD-T0027` | `feat/USYD-T0027-error-taxonomy` | **PASS** | **PASS** | RFC 7807/9457 error taxonomy, localization dictionaries, traceId middleware. | `gh pr review 8 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#9** | **USYD-67** | `USYD-T0028` | `feat/USYD-T0028-auth-security` | **PASS** | `AWAITING SIGN-OFF` | Sanctum dual boundary, single-use refresh token migration, login rate limiting. | `gh pr review 9 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#10** | **USYD-68** | `USYD-T0029` | `feat/USYD-T0029-authz-audit` | **PASS** | `AWAITING SIGN-OFF` | 3D authorization policies, audit_events migration, immutable model hooks. | `gh pr review 10 --repo mykholy/usayd-api --approve -b "Approved"` |
| **#11** | **USYD-69** | `USYD-T0030` | `feat/USYD-T0030-feature-flags` | **PASS** | **PASS** | Feature flag engine, Redis caching, CheckFeatureFlag middleware, admin audit endpoints. | `gh pr review 11 --repo mykholy/usayd-api --approve -b "Approved"` |

### 2.2 Mobile Repository: `usayd-flutter` (Assignee: Ahmed Mamdouh El-Sayed)

| PR | Jira Key | Task ID | Branch | CI Check | Gate Status | Sensitive Files / Approval Rationale | Quick Approval Command |
|---|---|---|---|---|---|---|---|
| **#1** | **USYD-60** | `USYD-T0075` | `feat/USYD-T0075-flutter-bootstrap` | **PASS** | `AWAITING SIGN-OFF` | Flutter project bootstrap, flavors (dev, staging, prod), CI workflow. | `gh pr review 1 --repo mykholy/usayd-flutter --approve -b "Approved"` |
| **#2** | **USYD-61** | `USYD-T0076` | `feat/USYD-T0076-design-tokens` | **PASS** | `AWAITING SIGN-OFF` | Design tokens, typography, theme extensions, SVG asset linking. | `gh pr review 2 --repo mykholy/usayd-flutter --approve -b "Approved"` |
| **#3** | **USYD-62** | `USYD-T0077` | `feat/USYD-T0077-localization-themes` | **PASS** | `AWAITING SIGN-OFF` | RTL Arabic / LTR English localization, light/dark themes. | `gh pr review 3 --repo mykholy/usayd-flutter --approve -b "Approved"` |
| **#4** | **USYD-63** | `USYD-T0078` | `feat/USYD-T0078-responsive-shell` | **PASS** | `AWAITING SIGN-OFF` | Age-adaptive shell (Kids, Pro, Simple), safe area, bottom nav. | `gh pr review 4 --repo mykholy/usayd-flutter --approve -b "Approved"` |
| **#5** | **USYD-72** | `USYD-T0079` | `feat/USYD-T0079-api-client` | **PASS** | `AWAITING SIGN-OFF` | `pubspec.yaml` dependencies (http, flutter_secure_storage), typed ApiClient. | `gh pr review 5 --repo mykholy/usayd-flutter --approve -b "Approved"` |
| **#6** | **USYD-73** | `USYD-T0080` | `feat/USYD-T0080-routing-permissions` | **PASS** | `AWAITING SIGN-OFF` | `pubspec.yaml` dependency (`go_router: ^17.5.0`), declarative routing & guards. | `gh pr review 6 --repo mykholy/usayd-flutter --approve -b "Approved"` |

---

## 3. Human Review Instructions

To approve and merge these PRs sequentially:
1. Review the PR diff on GitHub using the links above.
2. Approve the PR via the GitHub Web UI or CLI:
   ```bash
   gh pr review <PR_NUMBER> --repo mykholy/<REPO_NAME> --approve -b "LGTM - Approved by repository owner"
   ```
3. Once approved, merge using squash or merge commit:
   ```bash
   gh pr merge <PR_NUMBER> --repo mykholy/<REPO_NAME> --squash
   ```
