# USYD-T0461 — API POST /api/v1/admin/break-glass-grants (postBreakGlassGrant)

> **Issue type:** Story · **Epic:** USYD-E-SUP · **Repository:** `api` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S73 · **Priority:** Medium · **Points:** 3 · **Gate:** Blocked / Conditional

## Canonical source references
- `07_api/openapi.proposed.yaml`
- `operationId:postBreakGlassGrant`
- `UX-SUP-004`
- `FR-SUP-004`
- `FR-SUP-009`
- `FR-SEC-004`

## Objective, scope & implementation detail
### HTTP contract
`POST /api/v1/admin/break-glass-grants` — `postBreakGlassGrant`. Source `openapi.proposed.yaml`. Status: **PROPOSED_UNAPPROVED**.
Tags: `Admin`. Summary: Time-boxed emergency access to a safeguarding case.

### Required contract behavior
- Security: `[{"BearerAuth": []}]` (audit explicitly for guest access; never assume global bearer correct).
- Request parameters: `[{"name": "Idempotency-Key", "in": "header", "required": true, "schema": {"type": "string", "format": "uuid"}, "description": "Same key + same body within 24 h returns the first result; same key + different body → 409 IDEMPOTENCY_MISMATCH"}]`.
- Request body definition: `{"required": true, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/BreakGlassRequest"}}}}`.
- Responses/statuses: `201, 401, 403, 429, 409, 422`.
- Referencing UI screens: `UX-SUP-004`; requirements: `FR-SUP-004; FR-SUP-009; FR-SEC-004`.
- Decision refs: `D-39`.

### Deliverables
Approve a complete OpenAPI operation including request/response schemas, 4xx behavior, permissions, rate limits, idempotency for writes, pagination for list GETs and test fixtures. Implement controller, FormRequest, service, repository/model and Policy as applicable. Create migrations only after domain invariants are settled. Treat `openapi.proposed.yaml` as **not approved** until technical sign-off.

### Tests
Unit, feature HTTP, MySQL migration+query, negative 401/403/404/409/422, contract schema and repeat/concurrency when applicable; no 200 response on fake data.

## Hard prerequisites
- `USYD-T0058` — SUP: approve scope, OpenAPI and state-machine contract
- `USYD-T0286` — FR-SUP-004: Safeguarding escalation
- `USYD-T0291` — FR-SUP-009: Break-glass access

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
- Branch: `api/usyd-t0461-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0461-slug`).
- PR title: `USYD-T0461: API POST /api/v1/admin/break-glass-grants (postBreakGlassGrant)`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Backend/API. **Stable external key:** `USYD-T0461`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Supervision: cross-market out-of-scope denial, no private-record leakage, independent approval, immutable access audit.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `composer validate; ./vendor/bin/pint --test; php artisan test (MySQL service DB); OpenAPI lint; migration fresh; static analysis where configured` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
