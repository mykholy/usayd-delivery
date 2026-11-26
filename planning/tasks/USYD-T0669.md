# USYD-T0669 — J01: End-to-end Guest market selection → browse → level-assessment booking → registration → verified booking

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S82 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J01.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-PUBLIC-001`
- `UX-GLOB-001`
- `UX-PUBLIC-002`
- `UX-PUBLIC-003`
- `UX-PUBLIC-005`
- `UX-PUBLIC-006`
- `UX-PUBLIC-009`
- `UX-GLOB-005`
- `UX-AUTH-001`
- `UX-AUTH-005`
- `UX-LEARNER-007`
- `FR-GEO-001`
- `FR-GEO-002`
- `FR-GEO-004`
- `FR-GEO-012`
- `FR-BOOK-001`
- `FR-BOOK-002`
- `FR-BOOK-007`
- `FR-IAM-001`
- `FR-IAM-002`
- `FR-NOTIF-002`

## Objective, scope & implementation detail
Execute the complete `J01` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J01.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Guest market selection → browse → level-assessment booking → registration → verified booking. Screen sequence: UX-PUBLIC-001, UX-GLOB-001, UX-PUBLIC-002, UX-PUBLIC-003, UX-PUBLIC-005, UX-PUBLIC-006, UX-PUBLIC-009, UX-GLOB-005, UX-AUTH-001, UX-AUTH-005, UX-LEARNER-007. FR: FR-GEO-001, FR-GEO-002, FR-GEO-004, FR-GEO-012, FR-BOOK-001, FR-BOOK-002, FR-BOOK-007, FR-IAM-001, FR-IAM-002, FR-NOTIF-002. Existing API: get__api_v1_public_markets, get__programs, get__api_v1_booking_available_slots, post__auth_register, post_bookings. Proposed API: getPublicTeacher, createSlotHold, joinMarketWaitlist.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0479` — UX-PUBLIC-001: Marketing Home — Next.js production screen
- `USYD-T0587` — UX-GLOB-001: Country & Currency Selector — Next.js production screen
- `USYD-T0480` — UX-PUBLIC-002: Programs Directory — Next.js production screen
- `USYD-T0481` — UX-PUBLIC-003: Program Detail — Next.js production screen
- `USYD-T0371` — API GET /api/v1/public/markets (get__api_v1_public_markets)
- `USYD-T0309` — API GET /api/v1/programs (get__programs)
- `USYD-T0380` — API GET /api/v1/booking/available-slots (get__api_v1_booking_available_slots)
- `USYD-T0301` — API POST /api/v1/auth/register (post__auth_register)
- `USYD-T0323` — API POST /api/v1/bookings (post_bookings)

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
- Branch: `qa/usyd-t0669-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0669-slug`).
- PR title: `USYD-T0669: J01: End-to-end Guest market selection → browse → level-assessment booking → registration → verified booking`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0669`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Markets: disabled-market waitlist, region selection independent of interface locale, pricebook scope and timezone representation.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
