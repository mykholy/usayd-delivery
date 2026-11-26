# USYD-T0680 — J12: End-to-end Admin price/config/provider change → preview/dry-run → distinct approver → activation → audit/rollback

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S85 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J12.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-GLOB-012`
- `UX-GLOB-013`
- `UX-SUP-010`
- `UX-VPC-004`
- `UX-VPC-005`
- `UX-VPC-006`
- `UX-ADMIN-041`
- `FR-ADMIN-004`
- `FR-GEO-005`
- `FR-GEO-010`
- `FR-VPC-001`
- `FR-VPC-006`
- `FR-SUP-011`

## Objective, scope & implementation detail
Execute the complete `J12` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J12.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Admin price/config/provider change → preview/dry-run → distinct approver → activation → audit/rollback. Screen sequence: UX-GLOB-012, UX-GLOB-013, UX-SUP-010, UX-VPC-004, UX-VPC-005, UX-VPC-006, UX-ADMIN-041. FR: FR-ADMIN-004, FR-GEO-005, FR-GEO-010, FR-VPC-001, FR-VPC-006, FR-SUP-011. Existing API: post__api_v1_admin_price_books, post__api_v1_admin_price_books_priceBookId_decision, post__api_v1_admin_settings_drafts, post__api_v1_admin_settings_versions_settingsVersionId_decision, post__api_v1_admin_video_routing_policies, post__api_v1_admin_video_routing_policies_policyId_dry_run, post__api_v1_admin_video_routing_policies_policyId_decision, post__api_v1_admin_video_routing_policies_policyId_activate, post__api_v1_admin_video_routing_policies_policyId_rollback. Proposed API: .

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0598` — UX-GLOB-012: Country Pricing Matrix — Next.js production screen
- `USYD-T0599` — UX-GLOB-013: Price Approval & Version Diff — Next.js production screen
- `USYD-T0624` — UX-SUP-010: Settings Registry — Next.js production screen
- `USYD-T0608` — UX-VPC-004: Video Routing Rules — Next.js production screen
- `USYD-T0386` — API POST /api/v1/admin/price-books (post__api_v1_admin_price_books)
- `USYD-T0387` — API POST /api/v1/admin/price-books/{priceBookId}/decision (post__api_v1_admin_price_books_priceBookId_decision)
- `USYD-T0408` — API POST /api/v1/admin/settings/drafts (post__api_v1_admin_settings_drafts)
- `USYD-T0409` — API POST /api/v1/admin/settings/versions/{settingsVersionId}/decision (post__api_v1_admin_settings_versions_settingsVersionId_decision)
- `USYD-T0393` — API POST /api/v1/admin/video-routing-policies (post__api_v1_admin_video_routing_policies)

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
- Branch: `qa/usyd-t0680-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0680-slug`).
- PR title: `USYD-T0680: J12: End-to-end Admin price/config/provider change → preview/dry-run → distinct approver → activation → audit/rollback`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0680`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Admin: granular ABAC permissions, pagination, user data minimization, sensitive action audit, no unauthorized bulk edits.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
