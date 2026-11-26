# USYD-T0487 — UX-PUBLIC-009: Free Assessment Booking — Next.js production screen

> **Issue type:** Story · **Epic:** USYD-E-BOOK · **Repository:** `web` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S33 · **Priority:** High · **Points:** 3 · **Gate:** Backlog

## Canonical source references
- `03_screens/screens/UX-PUBLIC-009.md`
- `01_design/canvas/UX-PUBLIC-009.dc.html`
- `FR-BOOK-002`
- `FR-TIME-001`
- `FR-TIME-003`
- `FR-IAM-001`
- `get__api_v1_booking_available_slots`
- `post__auth_register`
- `post_bookings`

## Objective, scope & implementation detail
### Identity and route
**UX-PUBLIC-009 — Free Assessment Booking**. Persona `PUBLIC`; role `Guest (public)`; route `/trial`; module `BOOK`; phase `P0`.

### Intent and exact design source
EN: Book a level assessment in the visitor’s timezone with minimal data.
AR: حجز تقييم مستوى بتوقيت الزائر وبيانات أقل.

- Exact implementation spec: `03_screens/screens/UX-PUBLIC-009.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-PUBLIC-009.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-PUBLIC-009.html` and `.../en/UX-PUBLIC-009.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Button; Page header; Stepper; Timezone chip; Segmented control; Card; Form field; Checkbox / consent; Slide to confirm; Page hero (illustrated); Shell / Public header; Loading skeleton; Alert / Inline; State panel; Shell / Public footer.
- Fields/validation hints: First name [required, 2–50 chars]; Email or phone [required; valid email or E.164 phone]; Age band [required; <18 triggers guardian gate]; Goal [required]; I agree to the Terms and Privacy Policy [must be checked].
- Responsive rule: Fluid page: max content 1280; ≥1100 multi-column; 760–1100 grids collapse to 2 columns; <760 single column, header nav hides (burger), CTAs stay visible; touch targets ≥44px..
- Duplicate canonical route: none.

### Exact screen actions (4 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `public-009.next-week` | Next week / الأسبوع التالي | LIST_QUERY | `get__api_v1_booking_available_slots` | in place | error state panel with Retry |
| `public-009.slide-to-confirm-booking` | Slide to confirm booking / اسحب لتأكيد الحجز | NAVIGATE_AFTER_CONFIRM | `nav-only` | UX-AUTH-005 | — |
| `public-009.retry` | Retry / أعد المحاولة | REFETCH | `get__api_v1_booking_available_slots` | in place | error state panel with Retry |
| `public-009.reconnect` | Reconnect / أعد الاتصال | REFETCH | `get__api_v1_booking_available_slots` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: get__api_v1_booking_available_slots; post__auth_register; post_bookings.
- FRs: FR-BOOK-002; FR-TIME-001; FR-TIME-003; FR-IAM-001.
- Permission: Guest → creates learner account at confirm; minors routed to guardian consent before booking is confirmed..
- State inventory: default, loading, empty, error (`SLOT_TAKEN`), denied, offline, success — adapted to real screen meaning, not generic fake success.
- Unresolved: `none`. Owner-content slots hidden until approved.

### Acceptance and quality gates
Recreate responsive AR/EN visual composition in light/dark using canonical tokens, no prototype/spec-bar in production. Proper forms and keyboard/mobile navigation, AA contrast, touch targets, focus and aria status. Hook to real typed API when approved, otherwise display a clear feature-flag unavailable state (never mock-success). Browser/Flutter snapshot tests; 320/390/768/1440 CSS/visual, 6 states, permission-positive and negative tests. Apply exact spec and verify action contracts. PR link Jira ticket, screenshot evidence and test commands.

## Hard prerequisites
- `USYD-T0064` — Web design tokens and component primitives
- `USYD-T0380` — API GET /api/v1/booking/available-slots (get__api_v1_booking_available_slots)
- `USYD-T0301` — API POST /api/v1/auth/register (post__auth_register)

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
- Branch: `web/usyd-t0487-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0487-slug`).
- PR title: `USYD-T0487: UX-PUBLIC-009: Free Assessment Booking — Next.js production screen`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Next.js Web. **Stable external key:** `USYD-T0487`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Booking: competing bookings for same slot with MySQL InnoDB locks; timezones/DST gaps/folds; retries/idempotency; cancellation cutoff; hold expiry and orphan cleanup.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `pnpm install --frozen-lockfile; pnpm lint; pnpm typecheck; pnpm test; pnpm build; pnpm e2e; visual/axe checks for changed screens` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
