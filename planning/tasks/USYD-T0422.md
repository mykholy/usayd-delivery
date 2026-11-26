# USYD-T0422 — API GET /api/v1/admin/learners (listAdminLearners)

> **Issue type:** Story · **Epic:** USYD-E-IAM · **Repository:** `api` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S74 · **Priority:** Medium · **Points:** 2 · **Gate:** Blocked / Conditional

## Canonical source references
- `07_api/openapi.proposed.yaml`
- `operationId:listAdminLearners`
- `UX-ADMIN-002`
- `FR-IAM-004`
- `FR-ADMIN-002`
- `FR-PROF-004`

## Objective, scope & implementation detail
### HTTP contract
`GET /api/v1/admin/learners` — `listAdminLearners`. Source `openapi.proposed.yaml`. Status: **PROPOSED_UNAPPROVED**.
Tags: `Admin`. Summary: Scoped learner directory.

### Required contract behavior
- Security: `[{"BearerAuth": []}]` (audit explicitly for guest access; never assume global bearer correct).
- Request parameters: `[{"name": "market", "in": "query", "schema": {"type": "string", "pattern": "^[A-Z]{2}$"}}, {"name": "status", "in": "query", "schema": {"type": "string", "enum": ["active", "limited", "paused", "closed"]}}, {"name": "age_band", "in": "query", "schema": {"type": "string", "enum": ["minor_under_13", "minor_13_17", "adult"]}}, {"name": "q", "in": "query", "schema": {"type": "string", "maxLength": 64}, "description": "display_ref or learner id only; no name search for minors"}, {"name": "sort", "in": "query", "schema": {"type": "string", "enum": ["display_ref", "status", "market"], "default": "display_ref"}}, {"name": "order", "in": "query", "schema": {"type": "string", "enum": ["asc", "desc"], "default": "asc"}}, {"name": "cursor", "in": "query", "schema": {"type": "string"}, "description": "Opaque cursor from `next_cursor`"}, {"name": "limit", "in": "query", "schema": {"type": "integer", "minimum": 1, "maximum": 100, "default": 25}}]`.
- Request body definition: `{}`.
- Responses/statuses: `200, 401, 403, 429, 422`.
- Referencing UI screens: `UX-ADMIN-002`; requirements: `FR-IAM-004; FR-ADMIN-002; FR-PROF-004`.
- Decision refs: `none listed`.

### Deliverables
Approve a complete OpenAPI operation including request/response schemas, 4xx behavior, permissions, rate limits, idempotency for writes, pagination for list GETs and test fixtures. Implement controller, FormRequest, service, repository/model and Policy as applicable. Create migrations only after domain invariants are settled. Treat `openapi.proposed.yaml` as **not approved** until technical sign-off.

### Tests
Unit, feature HTTP, MySQL migration+query, negative 401/403/404/409/422, contract schema and repeat/concurrency when applicable; no 200 response on fake data.

## Hard prerequisites
- `USYD-T0038` — IAM: approve scope, OpenAPI and state-machine contract
- `USYD-T0088` — FR-IAM-004: RBAC/ABAC
- `USYD-T0212` — FR-ADMIN-002: صلاحيات متعددة

## Owner/external block
PROPOSED: requires contract approval before implementation

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] MySQL integration & concurrency tests for stateful API actions (no SQLite-only substitute)
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `api/usyd-t0422-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0422-slug`).
- PR title: `USYD-T0422: API GET /api/v1/admin/learners (listAdminLearners)`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Backend/API. **Stable external key:** `USYD-T0422`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Identity: guest/learner/teacher/admin role isolation; expired invitation; MFA/OTP rate limiting; revoked sessions; negative consent checks; enumeration-safe reset.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `composer validate; ./vendor/bin/pint --test; php artisan test (MySQL service DB); OpenAPI lint; migration fresh; static analysis where configured` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
