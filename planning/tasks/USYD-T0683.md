# USYD-T0683 — J15: End-to-end Payroll: accrual → calculation → review → dual approval → disbursement/reconciliation (no invented rules)

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S86 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J15.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-ADMIN-021`
- `UX-ADMIN-022`
- `UX-TEACHER-016`
- `UX-ADMIN-009`
- `FR-PAYROLL-001`
- `FR-PAYROLL-002`
- `FR-PAYROLL-007`
- `FR-PAYROLL-008`
- `FR-PAYROLL-009`

## Objective, scope & implementation detail
Execute the complete `J15` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J15.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Payroll: accrual → calculation → review → dual approval → disbursement/reconciliation (no invented rules). Screen sequence: UX-ADMIN-021, UX-ADMIN-022, UX-TEACHER-016, UX-ADMIN-009. FR: FR-PAYROLL-001, FR-PAYROLL-002, FR-PAYROLL-007, FR-PAYROLL-008, FR-PAYROLL-009. Existing API: post__admin_pay_runs__payRunId__approve, get__teachers_me_pay_statements, getCompensationPreview. Proposed API: listPayRuns, disputePayStatement.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0566` — UX-ADMIN-021: Payroll Calculations — Next.js production screen
- `USYD-T0567` — UX-ADMIN-022: Payroll Approval — Next.js production screen
- `USYD-T0543` — UX-TEACHER-016: Teacher Pay Statements — Next.js production screen
- `USYD-T0554` — UX-ADMIN-009: Teacher Contract Builder — Next.js production screen
- `USYD-T0347` — API POST /api/v1/admin/pay-runs/{payRunId}/approve (post__admin_pay_runs__payRunId__approve)
- `USYD-T0345` — API GET /api/v1/teachers/me/pay-statements (get__teachers_me_pay_statements)
- `USYD-T0359` — API GET /api/v1/teachers/me/compensation-preview (getCompensationPreview)
- `USYD-T0436` — API GET /api/v1/admin/pay-runs (listPayRuns)
- `USYD-T0465` — API POST /api/v1/teachers/me/pay-statements/{statementId}/disputes (disputePayStatement)

## Owner/external block
None documented in this ticket; always check source decision register and flags.

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] Visual/accessibility/device/contract tests matching target repo
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `qa/usyd-t0683-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0683-slug`).
- PR title: `USYD-T0683: J15: End-to-end Payroll: accrual → calculation → review → dual approval → disbursement/reconciliation (no invented rules)`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0683`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Payroll: contract version, compensation precision, dual authorization and reconciliation.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
