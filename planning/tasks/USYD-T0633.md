# USYD-T0633 — UX-MOBILE-002: Flutter Today — Flutter UI

> **Issue type:** Story · **Epic:** USYD-E-MOB · **Repository:** `flutter` · **Assignee lane:** Flutter Developer · **Candidate Sprint:** S03 · **Priority:** Medium · **Points:** 3 · **Gate:** Backlog

## Canonical source references
- `03_screens/screens/UX-MOBILE-002.md`
- `01_design/canvas/UX-MOBILE-002.dc.html`
- `FR-MOB-001`
- `FR-PLAN-003`
- `getLearnerLearningSummary`

## Objective, scope & implementation detail
### Identity and route
**UX-MOBILE-002 — Flutter Today**. Persona `MOBILE`; role `Learner (Flutter)`; route `mobile://home`; module `MOB`; phase `P2`.

### Intent and exact design source
EN: Learner today on mobile.
AR: يوم المتعلم على الموبايل.

- Exact implementation spec: `03_screens/screens/UX-MOBILE-002.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-MOBILE-002.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-MOBILE-002.html` and `.../en/UX-MOBILE-002.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Mobile hero (night); Slide to confirm; Progress bar; Card; List row; AI suggestion card; Status Chip; Button; Mobile / Night header + sheet; Loading skeleton; Alert / Inline; State panel; Mobile / Tab bar.
- Fields/validation hints: See per-screen spec.
- Responsive rule: Flutter phone 360–428 portrait; tablet uses two-pane where noted; respects safe areas and dynamic type..
- Duplicate canonical route: none.

### Exact screen actions (5 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `mobile-002.slide-to-join-lesson` | Slide to join lesson / اسحب لدخول الحصة | NAVIGATE_AFTER_CONFIRM | `nav-only` | UX-MOBILE-003 | — |
| `mobile-002.why-this` | Why this? / لماذا هذا الاقتراح؟ | UI_ONLY | `nav-only` | in place | — |
| `mobile-002.dismiss` | Dismiss / إخفاء | UI_ONLY | `nav-only` | in place | — |
| `mobile-002.retry` | Retry / أعد المحاولة | REFETCH | `getLearnerLearningSummary` | in place | error state panel with Retry |
| `mobile-002.reconnect` | Reconnect / أعد الاتصال | REFETCH | `getLearnerLearningSummary` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: getLearnerLearningSummary.
- FRs: FR-MOB-001; FR-PLAN-003.
- Permission: Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1..
- State inventory: default, loading, empty, error (`SERVER_ERROR`), denied, offline, success — adapted to real screen meaning, not generic fake success.
- Unresolved: `none`. Owner-content slots hidden until approved.

### Acceptance and quality gates
Recreate responsive AR/EN visual composition in light/dark using canonical tokens, no prototype/spec-bar in production. Proper forms and keyboard/mobile navigation, AA contrast, touch targets, focus and aria status. Hook to real typed API when approved, otherwise display a clear feature-flag unavailable state (never mock-success). Browser/Flutter snapshot tests; 320/390/768/1440 CSS/visual, 6 states, permission-positive and negative tests. Apply exact spec and verify action contracts. PR link Jira ticket, screenshot evidence and test commands.

## Hard prerequisites
- `USYD-T0076` — Flutter design tokens, fonts/reference asset linking

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
- Branch: `flutter/usyd-t0633-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0633-slug`).
- PR title: `USYD-T0633: UX-MOBILE-002: Flutter Today — Flutter UI`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Flutter Mobile. **Stable external key:** `USYD-T0633`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Mobile: device permissions, offline draft encryption, sync conflicts, AR/EN RTL/LTR, accessibility, child-safe navigation.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `flutter pub get; dart format --output=none --set-exit-if-changed .; flutter analyze; flutter test; widget/golden/integration tests for modified screens` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
