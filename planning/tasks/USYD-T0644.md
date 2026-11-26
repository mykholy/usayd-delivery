# USYD-T0644 — UX-MOBILE-007: real API, offline and permission integration

> **Issue type:** Story · **Epic:** USYD-E-MOB · **Repository:** `flutter` · **Assignee lane:** Flutter Developer · **Candidate Sprint:** S49 · **Priority:** Medium · **Points:** 2 · **Gate:** Backlog

## Canonical source references
- `UX-MOBILE-007`
- `postExamCheckpoint`
- `post__exam_attempts__attemptId__submit`

## Objective, scope & implementation detail
Integrate `UX-MOBILE-007` against the exact approved OpenAPI operations `postExamCheckpoint; post__exam_attempts__attemptId__submit`. Replace Fixtures only on the live code path; preserve deterministic fixtures in tests. Validate auth refresh, token expiry, 403 scope, timeouts, retries, pagination, offline queue semantics, conflict resolution, AR/EN and dark/light. Check production success only after server confirmation. Add integration tests with real staging API and negative cases. Upstream visual ticket: `USYD-T0643`. Source: `03_screens/screens/UX-MOBILE-007.md`.

## Hard prerequisites
- `USYD-T0643` — UX-MOBILE-007: Flutter Exam — Flutter UI
- `USYD-T0361` — API POST /api/v1/exam-attempts/{attemptId}/checkpoint (postExamCheckpoint)
- `USYD-T0336` — API POST /api/v1/exam-attempts/{attemptId}/submit (post__exam_attempts__attemptId__submit)

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
- Branch: `flutter/usyd-t0644-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0644-slug`).
- PR title: `USYD-T0644: UX-MOBILE-007: real API, offline and permission integration`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Flutter Mobile. **Stable external key:** `USYD-T0644`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Mobile: device permissions, offline draft encryption, sync conflicts, AR/EN RTL/LTR, accessibility, child-safe navigation.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `flutter pub get; dart format --output=none --set-exit-if-changed .; flutter analyze; flutter test; widget/golden/integration tests for modified screens` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
