# Three-repo architecture & engineering standards

## Separation and release contract
- **usayd-api:** Laravel 13 modular monolith, PHP >=8.3, MySQL 8.4 LTS (InnoDB strict SQL), Redis + Horizon, private S3-compatible storage, transactional outbox, API `/api/v1`, Pest, security policies. Owns approved OpenAPI, domains, migrations and contract test fixtures.
- **usayd-web:** Latest verified **stable** Next.js App Router + TypeScript, AR/EN RTL, light/dark, public/learner/teacher/supervisor/admin workspaces. Typed generated API client pinned to published OpenAPI artifact and SHA. Playwright + axe + visual baselines. SEO, SSR/cache rules, performance budgets.
- **usayd-flutter:** Flutter single app for Android/iOS with learner/teacher and Kids/Professional/Simple adaptive interfaces, local encrypted drafts/offline queue, typed API SDK pinned, Widget/Golden/Integration and real devices.

## Contract changes
1. Ticket & proposal in api repo, with approval from tech lead for OpenAPI/semantics.
2. Contract validation (spectral/schema, 401/403/409/422, parameters, examples), backward compatibility and version bump; publish spec artifact and SHA256.
3. Consumer repos regenerate clients with pinned artifact; consumer PRs track producer API PR; compatibility smoke tests.
4. Deploy api safely first in backward compatible mode; web later; mobile versions may remain deployed for months. Never break existing app versions without deprecation window.

## Workflow
Backlog → Ready → In Progress → PR Review → QA/Staging → Done. `Blocked` is a flag/status, not a false Done. One PR per code ticket, no bypass for required review. Reviewer of sensitive code must be a different authorized human; AI assessment may supplement but never replace formal approval. Hotfixes use documented emergency workflow.

## Integration and tests
- API: Pest unit, feature, contract, MySQL migrations/replay/idempotency/race tests, auth/ABAC adversarial tests, queue/outbox recovery, load.
- Web: typed API requests, Playwright E2E for actual state transitions, RTL/dark/contrast/a11y, screen snapshots at 320, 390, 768, 1440, 1920; human review.
- Flutter: Widget+Golden, real devices and VoiceOver/TalkBack, encrypted offline sync, token expiry, store/reconnect conflict and 4xx/5xx.
- Cross-repo: 17 journey files, 36 Gherkin examples, owner approvals and contract hashes. No fabricated backend behavior; no tests marked passed without running.

## MySQL specific invariants
- UTC `DATETIME(6)` and separately stored IANA timezone; never use local strings as timestamps.
- Monetary integer minor units, signed price book, currency ISO4217; preserve 3-decimal currencies.
- Booking: unique index/slot ownership or booked interval locking with deterministic serialized resource lock, `SELECT ... FOR UPDATE`, retry deadlocks, bounded holds, optimistic version/idempotency key; verify with simultaneous **real MySQL** transactions. MySQL has no PostgreSQL exclusion constraints.
- Outbox in same transaction for state changes, webhooks signature/idempotency and ledger correctness.
- Indexes and nullable/unique semantics explicitly tested; no SQLite in integration acceptance.

## Realistic two-person capacity
Only candidate sprint buckets are provided. 18 FullStack and 12 Flutter story points are speculative caps per 2-week sprint, not committed velocity. Multiple AI agents DO NOT increase the human review and product approval capacity automatically. Commit S00 and S01 only after review; resize/refine the remaining backlog every sprint.
