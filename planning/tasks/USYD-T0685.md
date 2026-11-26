# USYD-T0685 — J17: End-to-end Kids / Professional / Simple mode switching (presentation only; permissions unchanged)

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S87 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J17.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-MOBILE-012`
- `UX-MOBILE-K02`
- `UX-MOBILE-K05`
- `UX-MOBILE-K08`
- `UX-MOBILE-K11`
- `UX-MOBILE-S02`
- `UX-MOBILE-S04`
- `UX-MOBILE-S11`
- `UX-MOBILE-011`
- `FR-MOB-005`
- `FR-ENG-004`
- `FR-CONTEST-013`
- `FR-IAM-007`

## Objective, scope & implementation detail
Execute the complete `J17` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J17.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Kids / Professional / Simple mode switching (presentation only; permissions unchanged). Screen sequence: UX-MOBILE-012, UX-MOBILE-K02, UX-MOBILE-K05, UX-MOBILE-K08, UX-MOBILE-K11, UX-MOBILE-S02, UX-MOBILE-S04, UX-MOBILE-S11, UX-MOBILE-011. FR: FR-MOB-005, FR-ENG-004, FR-CONTEST-013, FR-IAM-007. Existing API: get__api_v1_me_preferences, patch__api_v1_me_preferences, get__achievements, getLearnerLearningSummary. Proposed API: .

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0653` — UX-MOBILE-012: App style chooser (added) — Flutter UI
- `USYD-T0655` — UX-MOBILE-K02: Kids · Today mission (added) — Flutter UI
- `USYD-T0657` — UX-MOBILE-K05: Kids · My path (added) — Flutter UI
- `USYD-T0659` — UX-MOBILE-K08: Kids · My stars (added) — Flutter UI
- `USYD-T0374` — API GET /api/v1/me/preferences (get__api_v1_me_preferences)
- `USYD-T0375` — API PATCH /api/v1/me/preferences (patch__api_v1_me_preferences)
- `USYD-T0344` — API GET /api/v1/achievements (get__achievements)
- `USYD-T0367` — API GET /api/v1/learners/{learnerId}/learning-summary (getLearnerLearningSummary)

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
- Branch: `qa/usyd-t0685-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0685-slug`).
- PR title: `USYD-T0685: J17: End-to-end Kids / Professional / Simple mode switching (presentation only; permissions unchanged)`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0685`.

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
