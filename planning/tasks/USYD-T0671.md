# USYD-T0671 — J03: End-to-end Teacher application → document verification → approval → availability → learner assignment

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S82 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J03.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-TEACHER-001`
- `UX-ADMIN-006`
- `UX-ADMIN-008`
- `UX-ADMIN-009`
- `UX-TEACHER-003`
- `UX-GLOB-008`
- `UX-ADMIN-003`
- `UX-TEACHER-008`
- `FR-TCHR-001`
- `FR-TCHR-002`
- `FR-TCHR-003`
- `FR-TCHR-004`
- `FR-TCHR-005`
- `FR-MEDIA-003`
- `FR-SEC-002`

## Objective, scope & implementation detail
Execute the complete `J03` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J03.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Teacher application → document verification → approval → availability → learner assignment. Screen sequence: UX-TEACHER-001, UX-ADMIN-006, UX-ADMIN-008, UX-ADMIN-009, UX-TEACHER-003, UX-GLOB-008, UX-ADMIN-003, UX-TEACHER-008. FR: FR-TCHR-001, FR-TCHR-002, FR-TCHR-003, FR-TCHR-004, FR-TCHR-005, FR-MEDIA-003, FR-SEC-002. Existing API: post__admin_teachers__teacherId__contracts, put__api_v1_teacher_me_availability_rules. Proposed API: createUpload, submitTeacherApplication, listTeacherApplications, decideTeacherApplication, getAdminTeacher, assignTeacher, listMyLearners.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0528` — UX-TEACHER-001: Teacher Login & Onboarding — Next.js production screen
- `USYD-T0551` — UX-ADMIN-006: Teacher Recruitment — Next.js production screen
- `USYD-T0553` — UX-ADMIN-008: Teacher Profile Admin — Next.js production screen
- `USYD-T0554` — UX-ADMIN-009: Teacher Contract Builder — Next.js production screen
- `USYD-T0346` — API POST /api/v1/admin/teachers/{teacherId}/contracts (post__admin_teachers__teacherId__contracts)
- `USYD-T0379` — API PUT /api/v1/teacher/me/availability-rules (put__api_v1_teacher_me_availability_rules)
- `USYD-T0463` — API POST /api/v1/uploads (createUpload)
- `USYD-T0425` — API POST /api/v1/teacher-applications (submitTeacherApplication)
- `USYD-T0424` — API GET /api/v1/admin/teacher-applications (listTeacherApplications)

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
- Branch: `qa/usyd-t0671-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0671-slug`).
- PR title: `USYD-T0671: J03: End-to-end Teacher application → document verification → approval → availability → learner assignment`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0671`.

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
