# Recommended source repositories and implementation conventions

## Repos (logical; may be mono-repo if team prefers)

```
academy-platform/
├── apps/
│   ├── api-laravel/
│   ├── web-next/
│   ├── flutter-mobile/             # P2
│   ├── ai-worker-python/           # P1
│   └── qa-e2e/
├── packages/
│   ├── openapi/
│   ├── design-tokens/
│   └── shared-test-fixtures/
├── docs/                             # THIS specification pack
├── infra/
│   ├── terraform-or-compose/
│   └── monitoring/
└── .github/workflows/
```

This is **a proposed structure, not repositories created**.

## Laravel directory rule

`app/Modules/<BoundedContext>/{Domain,Application,Infrastructure,Http,Providers}`. Example `app/Modules/Competitions/Domain/ScoreVersion.php` and `Application/FinalizeResults.php` with strict policy and transactions. Avoid giant controllers or direct cross-module DB writes. PHPUnit/Pest tests by module. API routes grouped as `/api/v1/...` with throttle policies and OpenAPI reviews.

## Implementation branch workflow

`main` protected, feature PRs tagged Jira ID + FR ID, staging integration, code owners Academic/Legal/Finance for respective modules, feature flag for unverified AI/rewards. CI checks static analysis, tests, request schema contract, sensitive-data static scanning and database migration rollback plan. No direct SQL production migrations without review.

## Code ownership examples

API lead: auth/booking/payment/interface, Academic engineering: revision and exam correctness, AI lead: model eval + worker, Frontend: web frames and design system, Mobile: Flutter client integration, QA: integration and UAT, Security: threat model/consent.
