# USYD-T0002 — O-04: Minors: who may enrol and how guardians are verified

> **Issue type:** Decision · **Epic:** USYD-E-PRODUCT · **Repository:** `docs` · **Assignee lane:** Product Owner / approving specialist · **Candidate Sprint:** S00 · **Priority:** High · **Points:** 1 · **Gate:** Needs Owner Approval

## Canonical source references
- `DECISION_REQUIRED_FROM_OWNER.md#O-04`
- `DECISION_LOG.md`

## Objective, scope & implementation detail
Review `O-04` in `DECISION_REQUIRED_FROM_OWNER.md` and `DECISION_LOG.md`. Capture option, legal/academic/security impact, explicit approver, approval date, and safe behavior while blocked. Do NOT approve by agent inference. Update flags/contract status and make an auditable ADR when signed.

## Hard prerequisites
- None

## Owner/external block
Requires authorized product-owner decision

## Acceptance criteria & Definition of Done
- [ ] Decision owner approved explicitly in signed decision log
- [ ] Affected FR/Screen/API/flags documented
- [ ] Human sign-off retained; never set approved autonomously

## PR contract
- Branch: `docs/usyd-t0002-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0002-slug`).
- PR title: `USYD-T0002: O-04: Minors: who may enrol and how guardians are verified`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0002`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Validate exact UI/permission/API obligations against cited source, including success/failure, boundary values, cancellation and retries.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
