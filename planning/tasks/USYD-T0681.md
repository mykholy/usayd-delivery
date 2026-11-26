# USYD-T0681 — J13: End-to-end Mobile offline draft → encrypted queue → re-auth → reconnect/batch sync → idempotency and conflict resolution

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S86 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J13.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-MOBILE-002`
- `UX-MOBILE-007`
- `UX-MOBILE-010`
- `UX-MOBILE-000`
- `UX-MOBILE-001`
- `FR-MOB-002`
- `FR-MOB-004`
- `FR-IAM-008`

## Objective, scope & implementation detail
Execute the complete `J13` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J13.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Mobile offline draft → encrypted queue → re-auth → reconnect/batch sync → idempotency and conflict resolution. Screen sequence: UX-MOBILE-002, UX-MOBILE-007, UX-MOBILE-010, UX-MOBILE-000, UX-MOBILE-001. FR: FR-MOB-002, FR-MOB-004, FR-IAM-008. Existing API: post__auth_refresh, postExamCheckpoint, post__revision_tasks__taskId__evidence. Proposed API: submitSyncBatch, saveLessonReportDraft.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0633` — UX-MOBILE-002: Flutter Today — Flutter UI
- `USYD-T0643` — UX-MOBILE-007: Flutter Exam — Flutter UI
- `USYD-T0649` — UX-MOBILE-010: Flutter Teacher Report — Flutter UI
- `USYD-T0629` — UX-MOBILE-000: Flutter Splash (added) — Flutter UI
- `USYD-T0303` — API POST /api/v1/auth/refresh (post__auth_refresh)
- `USYD-T0361` — API POST /api/v1/exam-attempts/{attemptId}/checkpoint (postExamCheckpoint)
- `USYD-T0320` — API POST /api/v1/revision-tasks/{taskId}/evidence (post__revision_tasks__taskId__evidence)
- `USYD-T0456` — API POST /api/v1/me/sync-batches (submitSyncBatch)
- `USYD-T0455` — API PUT /api/v1/lessons/{lessonId}/report-draft (saveLessonReportDraft)

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
- Branch: `qa/usyd-t0681-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0681-slug`).
- PR title: `USYD-T0681: J13: End-to-end Mobile offline draft → encrypted queue → re-auth → reconnect/batch sync → idempotency and conflict resolution`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0681`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Mobile: device permissions, offline draft encryption, sync conflicts, AR/EN RTL/LTR, accessibility, child-safe navigation.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
