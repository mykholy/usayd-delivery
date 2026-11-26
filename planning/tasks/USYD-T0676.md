# USYD-T0676 — J08: End-to-end Learning plan approval → daily learning → oral assessment → evidence-backed revision queue and memory map

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S84 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J08.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-LEARNER-004`
- `UX-TEACHER-010`
- `UX-TEACHER-011`
- `UX-SUP-002`
- `UX-LEARNER-012`
- `UX-LEARNER-013`
- `UX-LEARNER-014`
- `UX-LEARNER-015`
- `UX-LEARNER-016`
- `UX-LEARNER-028`
- `FR-ASMT-001`
- `FR-ASMT-002`
- `FR-PLAN-001`
- `FR-PLAN-002`
- `FR-PLAN-003`
- `FR-AI-001`
- `FR-CURR-003`
- `FR-CURR-004`
- `FR-NOTIF-003`

## Objective, scope & implementation detail
Execute the complete `J08` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J08.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Learning plan approval → daily learning → oral assessment → evidence-backed revision queue and memory map. Screen sequence: UX-LEARNER-004, UX-TEACHER-010, UX-TEACHER-011, UX-SUP-002, UX-LEARNER-012, UX-LEARNER-013, UX-LEARNER-014, UX-LEARNER-015, UX-LEARNER-016, UX-LEARNER-028. FR: FR-ASMT-001, FR-ASMT-002, FR-PLAN-001, FR-PLAN-002, FR-PLAN-003, FR-AI-001, FR-CURR-003, FR-CURR-004, FR-NOTIF-003. Existing API: post__assessments, post__assessments__assessmentId__approve, post__learning_plans_suggestions, patchLearningPlanDraft, post__api_v1_supervisor_academic_plans_planId_decision, post__learning_plans__planId__approve, get__revision_tasks, post__revision_tasks__taskId__evidence, get__memory_map. Proposed API: listLibraryItems.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0499` — UX-LEARNER-004: Initial Assessment — Next.js production screen
- `USYD-T0537` — UX-TEACHER-010: Assessment Workspace — Next.js production screen
- `USYD-T0538` — UX-TEACHER-011: Plan Review Queue — Next.js production screen
- `USYD-T0616` — UX-SUP-002: Academic Plans Approval — Next.js production screen
- `USYD-T0314` — API POST /api/v1/assessments (post__assessments)
- `USYD-T0315` — API POST /api/v1/assessments/{assessmentId}/approve (post__assessments__assessmentId__approve)
- `USYD-T0317` — API POST /api/v1/learning-plans/suggestions (post__learning_plans_suggestions)
- `USYD-T0369` — API PATCH /api/v1/learning-plans/{planId} (patchLearningPlanDraft)
- `USYD-T0404` — API POST /api/v1/supervisor/academic-plans/{planId}/decision (post__api_v1_supervisor_academic_plans_planId_decision)

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
- Branch: `qa/usyd-t0676-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0676-slug`).
- PR title: `USYD-T0676: J08: End-to-end Learning plan approval → daily learning → oral assessment → evidence-backed revision queue and memory map`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0676`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Assessments: server-authoritative timers, idempotent attempts, autosave, stale version conflicts, grader permissions, publication and manual review.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
