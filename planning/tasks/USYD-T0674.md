# USYD-T0674 — J06: End-to-end Classroom prejoin → device checks → in-app/external provider → incident/failover → attendance → teacher report

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S83 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J06.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-LEARNER-009`
- `UX-VPC-009`
- `UX-LEARNER-010`
- `UX-TEACHER-005`
- `UX-TEACHER-006`
- `UX-VPC-010`
- `UX-VPC-008`
- `UX-ADMIN-016`
- `UX-ADMIN-018`
- `UX-TEACHER-007`
- `FR-VIDEO-001`
- `FR-ATT-001`
- `FR-ATT-002`
- `FR-ATT-005`
- `FR-VPC-008`
- `FR-BOOK-008`
- `FR-MEDIA-004`

## Objective, scope & implementation detail
Execute the complete `J06` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J06.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Classroom prejoin → device checks → in-app/external provider → incident/failover → attendance → teacher report. Screen sequence: UX-LEARNER-009, UX-VPC-009, UX-LEARNER-010, UX-TEACHER-005, UX-TEACHER-006, UX-VPC-010, UX-VPC-008, UX-ADMIN-016, UX-ADMIN-018, UX-TEACHER-007. FR: FR-VIDEO-001, FR-ATT-001, FR-ATT-002, FR-ATT-005, FR-VPC-008, FR-BOOK-008, FR-MEDIA-004. Existing API: get__lessons__lessonId, get__conferences__conferenceId__capabilities, post__lessons__lessonId__join, post__webhooks_video__provider, get__api_v1_admin_video_incidents, post__api_v1_admin_video_incidents_incidentId_recover, postAttendanceDispute, post__lessons__lessonId__report. Proposed API: listAdminLessons.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0504` — UX-LEARNER-009: Lesson Detail — Next.js production screen
- `USYD-T0613` — UX-VPC-009: Embedded vs External Prejoin — Next.js production screen
- `USYD-T0505` — UX-LEARNER-010: Classroom — Next.js production screen
- `USYD-T0532` — UX-TEACHER-005: Lesson Briefing — Next.js production screen
- `USYD-T0325` — API GET /api/v1/lessons/{lessonId} (get__lessons__lessonId)
- `USYD-T0329` — API GET /api/v1/conferences/{conferenceId}/capabilities (get__conferences__conferenceId__capabilities)
- `USYD-T0326` — API POST /api/v1/lessons/{lessonId}/join (post__lessons__lessonId__join)
- `USYD-T0355` — API POST /api/v1/webhooks/video/{provider} (post__webhooks_video__provider)
- `USYD-T0398` — API GET /api/v1/admin/video-incidents (get__api_v1_admin_video_incidents)

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
- Branch: `qa/usyd-t0674-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0674-slug`).
- PR title: `USYD-T0674: J06: End-to-end Classroom prejoin → device checks → in-app/external provider → incident/failover → attendance → teacher report`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0674`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Classroom: one-time join token TTL, roster authorization, provider outage, fallback policy, recording consent, provider webhook verification, lesson status reconciliation.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
