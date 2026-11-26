# USYD-T0659 — UX-MOBILE-K08: Kids · My stars (added) — Flutter UI

> **Issue type:** Story · **Epic:** USYD-E-MOB · **Repository:** `flutter` · **Assignee lane:** Flutter Developer · **Candidate Sprint:** S06 · **Priority:** Medium · **Points:** 3 · **Gate:** Blocked / Conditional

## Canonical source references
- `03_screens/screens/UX-MOBILE-K08.md`
- `01_design/canvas/UX-MOBILE-K08.dc.html`
- `FR-ENG-004`
- `get__achievements`

## Objective, scope & implementation detail
### Identity and route
**UX-MOBILE-K08 — Kids · My stars (added)**. Persona `MOBILE`; role `Learner (Flutter, Kids mode 6–12)`; route `mobile://kids/stars`; module `ENG`; phase `P2`.

### Intent and exact design source
EN: The child’s private stars and badges.
AR: النجوم والشارات الخاصة بالطفل.

- Exact implementation spec: `03_screens/screens/UX-MOBILE-K08.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-MOBILE-K08.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-MOBILE-K08.html` and `.../en/UX-MOBILE-K08.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Badge grid (kids); Alert / Inline; Button; Mobile / Night header + sheet; Loading skeleton; State panel; Mobile / Tab bar.
- Fields/validation hints: See per-screen spec.
- Responsive rule: Flutter phone frame 390×844 (min 360); app bar 60, bottom tab bar with safe-area 22px; content scrolls; landscape and tablet two-pane where noted..
- Duplicate canonical route: none.

### Exact screen actions (2 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `mobile-k08.retry` | Retry / أعد المحاولة | REFETCH | `get__achievements` | in place | error state panel with Retry |
| `mobile-k08.reconnect` | Reconnect / أعد الاتصال | REFETCH | `get__achievements` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: get__achievements.
- FRs: FR-ENG-004.
- Permission: .
- State inventory: default, loading, empty, error (`SERVER_ERROR`), denied, offline, success — adapted to real screen meaning, not generic fake success.
- Unresolved: `Badges endpoint not in OpenAPI v1.2; Badge catalogue and award rules (D-36)`. Owner-content slots hidden until approved.

### Acceptance and quality gates
Recreate responsive AR/EN visual composition in light/dark using canonical tokens, no prototype/spec-bar in production. Proper forms and keyboard/mobile navigation, AA contrast, touch targets, focus and aria status. Hook to real typed API when approved, otherwise display a clear feature-flag unavailable state (never mock-success). Browser/Flutter snapshot tests; 320/390/768/1440 CSS/visual, 6 states, permission-positive and negative tests. Apply exact spec and verify action contracts. PR link Jira ticket, screenshot evidence and test commands.

## Hard prerequisites
- `USYD-T0076` — Flutter design tokens, fonts/reference asset linking

## Owner/external block
Badges endpoint not in OpenAPI v1.2; Badge catalogue and award rules (D-36)

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] Visual/accessibility/device/contract tests matching target repo
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `flutter/usyd-t0659-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0659-slug`).
- PR title: `USYD-T0659: UX-MOBILE-K08: Kids · My stars (added) — Flutter UI`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Flutter Mobile. **Stable external key:** `USYD-T0659`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Validate exact UI/permission/API obligations against cited source, including success/failure, boundary values, cancellation and retries.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `flutter pub get; dart format --output=none --set-exit-if-changed .; flutter analyze; flutter test; widget/golden/integration tests for modified screens` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
