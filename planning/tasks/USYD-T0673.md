# USYD-T0673 — J05: End-to-end Subscription quote → checkout → webhook → entitlement → renew/expire/refund (quote expiry, idempotency)

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S83 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J05.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-GLOB-002`
- `UX-GLOB-006`
- `UX-LEARNER-029`
- `UX-GLOB-007`
- `UX-ADMIN-019`
- `FR-PAY-001`
- `FR-PAY-002`
- `FR-PAY-003`
- `FR-PAY-004`
- `FR-PAY-005`
- `FR-PAY-006`
- `FR-GEO-005`
- `FR-GEO-006`
- `FR-GEO-007`
- `FR-GEO-015`

## Objective, scope & implementation detail
Execute the complete `J05` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J05.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Subscription quote → checkout → webhook → entitlement → renew/expire/refund (quote expiry, idempotency). Screen sequence: UX-GLOB-002, UX-GLOB-006, UX-LEARNER-029, UX-GLOB-007, UX-ADMIN-019. FR: FR-PAY-001, FR-PAY-002, FR-PAY-003, FR-PAY-004, FR-PAY-005, FR-PAY-006, FR-GEO-005, FR-GEO-006, FR-GEO-007, FR-GEO-015. Existing API: get__packages, post__api_v1_me_checkout_quotes, post__api_v1_me_payment_checkouts, post__webhooks_payments__provider, get__payments__paymentId, get__subscriptions. Proposed API: setRenewalConsent, requestRefund.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0588` — UX-GLOB-002: Localized Pricing Comparison — Next.js production screen
- `USYD-T0592` — UX-GLOB-006: Regional Checkout Quote — Next.js production screen
- `USYD-T0524` — UX-LEARNER-029: Subscription & Billing — Next.js production screen
- `USYD-T0593` — UX-GLOB-007: Renewal Price Change Notice — Next.js production screen
- `USYD-T0330` — API GET /api/v1/packages (get__packages)
- `USYD-T0376` — API POST /api/v1/me/checkout-quotes (post__api_v1_me_checkout_quotes)
- `USYD-T0377` — API POST /api/v1/me/payment-checkouts (post__api_v1_me_payment_checkouts)
- `USYD-T0354` — API POST /api/v1/webhooks/payments/{provider} (post__webhooks_payments__provider)
- `USYD-T0333` — API GET /api/v1/payments/{paymentId} (get__payments__paymentId)

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
- Branch: `qa/usyd-t0673-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0673-slug`).
- PR title: `USYD-T0673: J05: End-to-end Subscription quote → checkout → webhook → entitlement → renew/expire/refund (quote expiry, idempotency)`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0673`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Payments: signed webhook, replay/refund safeguards, immutable quote version, integer monetary minor units, multi-currency, subscription entitlement and ledger reconciliation.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
