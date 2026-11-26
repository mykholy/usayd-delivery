# USYD-T0670 — J02: End-to-end Minor sign-up → separate guardian session → purpose-level consent, decline, expiry, withdrawal, limited mode

> **Issue type:** Story · **Epic:** USYD-E-QUALITY · **Repository:** `qa` · **Assignee lane:** Full Stack / Codex + Flutter review · **Candidate Sprint:** S82 · **Priority:** High · **Points:** 5 · **Gate:** Backlog

## Canonical source references
- `04_flows/acceptance/J02.feature`
- `04_flows/JOURNEY_COVERAGE_MATRIX.csv`
- `UX-AUTH-001`
- `UX-AUTH-002`
- `UX-PUBLIC-012`
- `UX-AUTH-005`
- `UX-LEARNER-001`
- `UX-LEARNER-032`
- `UX-ADMIN-004`
- `FR-IAM-002`
- `FR-IAM-006`
- `FR-IAM-007`
- `FR-PROF-005`
- `FR-SEC-005`

## Objective, scope & implementation detail
Execute the complete `J02` journey from `04_flows/JOURNEYS.md`, `04_flows/acceptance/J02.feature` and related Mermaid sources. Actor boundaries are separate real sessions. Journey title: Minor sign-up → separate guardian session → purpose-level consent, decline, expiry, withdrawal, limited mode. Screen sequence: UX-AUTH-001, UX-AUTH-002, UX-PUBLIC-012, UX-AUTH-005, UX-LEARNER-001, UX-LEARNER-032, UX-ADMIN-004. FR: FR-IAM-002, FR-IAM-006, FR-IAM-007, FR-PROF-005, FR-SEC-005. Existing API: post__auth_register, post__consents, post__consents__consentId__withdraw. Proposed API: createGuardianInvitation, getGuardianInvitation, decideGuardianConsent, getLegalDocument, listAdminConsents.

**Do not limit test to a single happy path**: verify authorization, validation, timeouts, duplicate submissions, server-side state transition, currency/timezone, minor consent, independent approval, rollback/retry, audit/outbox and user-visible AR/EN state as applicable. Execute with MySQL+Redis backend plus browser/Flutter runtime in staging, collect sanitized evidence and exact PR links. Mark blocked by owner decisions instead of skipping silently.

## Hard prerequisites
- `USYD-T0491` — UX-AUTH-001: Unified Signup — Next.js production screen
- `USYD-T0492` — UX-AUTH-002: Guardian Consent Step — Next.js production screen
- `USYD-T0490` — UX-PUBLIC-012: Legal & Consents — Next.js production screen
- `USYD-T0495` — UX-AUTH-005: Welcome Onboarding — Next.js production screen
- `USYD-T0301` — API POST /api/v1/auth/register (post__auth_register)
- `USYD-T0307` — API POST /api/v1/consents (post__consents)
- `USYD-T0308` — API POST /api/v1/consents/{consentId}/withdraw (post__consents__consentId__withdraw)
- `USYD-T0452` — API POST /api/v1/learners/{learnerId}/guardian-invitations (createGuardianInvitation)
- `USYD-T0453` — API GET /api/v1/guardian-invitations/{invitationToken} (getGuardianInvitation)

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
- Branch: `qa/usyd-t0670-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0670-slug`).
- PR title: `USYD-T0670: J02: End-to-end Minor sign-up → separate guardian session → purpose-level consent, decline, expiry, withdrawal, limited mode`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Cross-team/Owner. **Stable external key:** `USYD-T0670`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Identity: guest/learner/teacher/admin role isolation; expired invitation; MFA/OTP rate limiting; revoked sessions; negative consent checks; enumeration-safe reset.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `verify requirement/decision source, cross-team impact, agreed contracts and signoff` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
