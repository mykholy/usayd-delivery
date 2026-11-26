# USYD-T0679 — J11: End-to-end Supervisor scoped request → out-of-scope denial → reassignment/approval with separation of duties

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S85 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J11.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-SUP-001`
- `UX-SUP-002`
- `UX-SUP-008`
- `UX-SUP-009`
- `UX-ADMIN-002`
- `FR-SUP-001`
- `FR-SUP-002`
- `FR-SUP-009`
- `FR-IAM-004`
- `FR-SEC-001`

## Objective, scope & implementation detail
Execute the complete `J11` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J11.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Supervisor scoped request → out-of-scope denial → reassignment/approval with separation of duties. Screen sequence: UX-SUP-001, UX-SUP-002, UX-SUP-008, UX-SUP-009, UX-ADMIN-002. FR: FR-SUP-001, FR-SUP-002, FR-SUP-009, FR-IAM-004, FR-SEC-001. Existing API: get__api_v1_supervisor_queues, post__api_v1_supervisor_academic_plans_planId_decision, get__api_v1_admin_supervisor_assignments, post__api_v1_admin_supervisor_assignments, post__api_v1_admin_supervisor_assignments_assignmentId_revoke, get__api_v1_admin_security_access_audits. Proposed API: postAccessAuditReview, listAdminLearners.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0615` — UX-SUP-001: Supervisor Home — Next.js production screen
- `USYD-T0616` — UX-SUP-002: Academic Plans Approval — Next.js production screen
- `USYD-T0622` — UX-SUP-008: Role Assignments & Scopes — Next.js production screen
- `USYD-T0623` — UX-SUP-009: Audit and Break-glass Review — Next.js production screen
- `USYD-T0403` — API GET /api/v1/supervisor/queues (get__api_v1_supervisor_queues)
- `USYD-T0404` — API POST /api/v1/supervisor/academic-plans/{planId}/decision (post__api_v1_supervisor_academic_plans_planId_decision)
- `USYD-T0400` — API GET /api/v1/admin/supervisor-assignments (get__api_v1_admin_supervisor_assignments)
- `USYD-T0401` — API POST /api/v1/admin/supervisor-assignments (post__api_v1_admin_supervisor_assignments)
- `USYD-T0402` — API POST /api/v1/admin/supervisor-assignments/{assignmentId}/revoke (post__api_v1_admin_supervisor_assignments_assignmentId_revoke)

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
- Branch: `qa/usyd-t0679-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0679-slug`).
- PR title: `USYD-T0679: J11: End-to-end Supervisor scoped request → out-of-scope denial → reassignment/approval with separation of duties`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0679`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Supervision: cross-market out-of-scope denial, no private-record leakage, independent approval, immutable access audit.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
