# USYD-T0048 — VPC: approve scope, OpenAPI and state-machine contract

> **Issue type:** Task · **Epic:** USYD-E-CONTRACTS · **Repository:** `api` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S05 · **Priority:** High · **Points:** 2 · **Gate:** Backlog

## Canonical source references
- `07_api/openapi.yaml`
- `07_api/openapi.proposed.yaml`
- `07_api/API_RECONCILIATION_MATRIX.csv`
- `08_data_model/STATE_ALIGNMENT.md`
- `FR-VPC-001`
- `FR-VPC-002`
- `FR-VPC-003`
- `FR-VPC-004`
- `FR-VPC-005`
- `FR-VPC-006`
- `FR-VPC-007`
- `FR-VPC-008`
- `FR-VPC-009`
- `FR-VPC-010`
- `FR-VPC-011`
- `FR-VPC-012`
- `FR-VPC-013`
- `FR-VPC-014`

## Objective, scope & implementation detail
Review exact module requirements: FR-VPC-001, FR-VPC-002, FR-VPC-003, FR-VPC-004, FR-VPC-005, FR-VPC-006, FR-VPC-007, FR-VPC-008, FR-VPC-009, FR-VPC-010, FR-VPC-011, FR-VPC-012, FR-VPC-013, FR-VPC-014. Reconcile `openapi.yaml`, `openapi.proposed.yaml`, `API_RECONCILIATION_MATRIX.csv`, `STATE_ALIGNMENT.md`, permissions and decisions. Classify each operation approved/proposed/blocked; do not implement pending contract until technical approval. Publish signed compatibility baseline to other repos.

## Hard prerequisites
- `USYD-T0037` — Cross-repo compatibility and published contracts

## Owner/external block
None documented in this ticket; always check source decision register and flags.

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] MySQL integration & concurrency tests for stateful API actions (no SQLite-only substitute)
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `api/usyd-t0048-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0048-slug`).
- PR title: `USYD-T0048: VPC: approve scope, OpenAPI and state-machine contract`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Backend/API. **Stable external key:** `USYD-T0048`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Validate exact UI/permission/API obligations against cited source, including success/failure, boundary values, cancellation and retries.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `composer validate; ./vendor/bin/pint --test; php artisan test (MySQL service DB); OpenAPI lint; migration fresh; static analysis where configured` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
