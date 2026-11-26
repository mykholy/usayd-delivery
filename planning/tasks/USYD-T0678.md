# USYD-T0678 — J10: End-to-end Competition enrollment → eligibility → round → judging → provisional result → appeal (independent session) → final → reward

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S85 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J10.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-LEARNER-020`
- `UX-LEARNER-021`
- `UX-LEARNER-022`
- `UX-LEARNER-023`
- `UX-LEARNER-024`
- `UX-LEARNER-025`
- `UX-TEACHER-014`
- `UX-TEACHER-015`
- `UX-ADMIN-028`
- `UX-ADMIN-029`
- `UX-ADMIN-030`
- `UX-ADMIN-031`
- `UX-SUP-005`
- `FR-CONTEST-002`
- `FR-CONTEST-003`
- `FR-CONTEST-008`
- `FR-CONTEST-009`
- `FR-CONTEST-010`
- `FR-CONTEST-011`
- `FR-CONTEST-014`
- `FR-ENG-003`

## Objective, scope & implementation detail
Execute the complete `J10` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J10.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Competition enrollment → eligibility → round → judging → provisional result → appeal (independent session) → final → reward. Screen sequence: UX-LEARNER-020, UX-LEARNER-021, UX-LEARNER-022, UX-LEARNER-023, UX-LEARNER-024, UX-LEARNER-025, UX-TEACHER-014, UX-TEACHER-015, UX-ADMIN-028, UX-ADMIN-029, UX-ADMIN-030, UX-ADMIN-031, UX-SUP-005. FR: FR-CONTEST-002, FR-CONTEST-003, FR-CONTEST-008, FR-CONTEST-009, FR-CONTEST-010, FR-CONTEST-011, FR-CONTEST-014, FR-ENG-003. Existing API: getContestEligibility, post__competitions__competitionId__register, getCompetitionRound, post__competitions__competitionId__submissions, post__competition_submissions__submissionId__judge, getCompetitionResult, post__competition_results__resultId__appeal, getAdminContestAppeals, postAdminContestAppealResolve, post__admin_competitions__competitionId__publish. Proposed API: assignCompetitionJudges.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0515` — UX-LEARNER-020: Competitions Discover — Next.js production screen
- `USYD-T0516` — UX-LEARNER-021: Competition Detail — Next.js production screen
- `USYD-T0517` — UX-LEARNER-022: Competition Preparation — Next.js production screen
- `USYD-T0518` — UX-LEARNER-023: Competition Round — Next.js production screen
- `USYD-T0357` — API GET /api/v1/competitions/{competitionId}/eligibility (getContestEligibility)
- `USYD-T0339` — API POST /api/v1/competitions/{competitionId}/register (post__competitions__competitionId__register)
- `USYD-T0362` — API GET /api/v1/competitions/{competitionId}/rounds/{roundId} (getCompetitionRound)
- `USYD-T0341` — API POST /api/v1/competitions/{competitionId}/submissions (post__competitions__competitionId__submissions)
- `USYD-T0342` — API POST /api/v1/competition-submissions/{submissionId}/judge (post__competition_submissions__submissionId__judge)

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
- Branch: `qa/usyd-t0678-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0678-slug`).
- PR title: `USYD-T0678: J10: End-to-end Competition enrollment → eligibility → round → judging → provisional result → appeal (independent session) → final → reward`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0678`.

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
