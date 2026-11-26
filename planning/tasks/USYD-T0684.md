# USYD-T0684 — J16: End-to-end Market activation and locale/country/timezone independence

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S87 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J16.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-GLOB-010`
- `UX-GLOB-011`
- `UX-GLOB-012`
- `UX-GLOB-013`
- `UX-GLOB-014`
- `UX-GLOB-004`
- `UX-GLOB-017`
- `UX-GLOB-003`
- `FR-GEO-002`
- `FR-GEO-003`
- `FR-GEO-010`
- `FR-GEO-011`

## Objective, scope & implementation detail
Execute the complete `J16` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J16.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Market activation and locale/country/timezone independence. Screen sequence: UX-GLOB-010, UX-GLOB-011, UX-GLOB-012, UX-GLOB-013, UX-GLOB-014, UX-GLOB-004, UX-GLOB-017, UX-GLOB-003. FR: FR-GEO-002, FR-GEO-003, FR-GEO-010, FR-GEO-011. Existing API: get__api_v1_admin_markets, post__api_v1_admin_markets, post__api_v1_admin_markets_marketId_decision, get__api_v1_admin_legal_market_readiness, get__api_v1_admin_payment_merchant_profiles, patch__api_v1_me_preferences. Proposed API: joinMarketWaitlist.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0596` — UX-GLOB-010: Markets Overview — Next.js production screen
- `USYD-T0597` — UX-GLOB-011: Market Launch Wizard — Next.js production screen
- `USYD-T0598` — UX-GLOB-012: Country Pricing Matrix — Next.js production screen
- `USYD-T0599` — UX-GLOB-013: Price Approval & Version Diff — Next.js production screen
- `USYD-T0382` — API GET /api/v1/admin/markets (get__api_v1_admin_markets)
- `USYD-T0383` — API POST /api/v1/admin/markets (post__api_v1_admin_markets)
- `USYD-T0384` — API POST /api/v1/admin/markets/{marketId}/decision (post__api_v1_admin_markets_marketId_decision)
- `USYD-T0421` — API GET /api/v1/admin/legal-market-readiness (get__api_v1_admin_legal_market_readiness)
- `USYD-T0413` — API GET /api/v1/admin/payment-merchant-profiles (get__api_v1_admin_payment_merchant_profiles)

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
- Branch: `qa/usyd-t0684-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0684-slug`).
- PR title: `USYD-T0684: J16: End-to-end Market activation and locale/country/timezone independence`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0684`.

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
