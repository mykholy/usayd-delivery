# USYD-T0649 — UX-MOBILE-010: Flutter Teacher Report — Flutter UI

> **Issue type:** Story · **Epic:** USYD-E-MOB · **Repository:** `flutter` · **Assignee lane:** Flutter Developer · **Candidate Sprint:** S05 · **Priority:** Medium · **Points:** 3 · **Gate:** Backlog

## Canonical source references
- `03_screens/screens/UX-MOBILE-010.md`
- `01_design/canvas/UX-MOBILE-010.dc.html`
- `FR-ATT-003`
- `FR-MOB-004`
- `post__lessons__lessonId__report`

## Objective, scope & implementation detail
### Identity and route
**UX-MOBILE-010 — Flutter Teacher Report**. Persona `MOBILE`; role `Teacher (Flutter)`; route `mobile://teacher/report`; module `ATT`; phase `P2`.

### Intent and exact design source
EN: Brief lesson report from mobile.
AR: تقرير حصة مختصر من الموبايل.

- Exact implementation spec: `03_screens/screens/UX-MOBILE-010.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-MOBILE-010.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-MOBILE-010.html` and `.../en/UX-MOBILE-010.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Form field; Alert / Inline; Slide to confirm; Mobile / Night header + sheet; Loading skeleton; Button; State panel; Mobile / Tab bar.
- Fields/validation hints: Attendance [required]; Al-Mulk 1–5 [required]; Note to learner [required].
- Responsive rule: Flutter phone 360–428 portrait; tablet uses two-pane where noted; respects safe areas and dynamic type..
- Duplicate canonical route: none.

### Exact screen actions (3 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `mobile-010.slide-to-publish` | Slide to publish / اسحب للنشر | NAVIGATE_AFTER_CONFIRM | `nav-only` | UX-MOBILE-009 | — |
| `mobile-010.retry` | Retry / أعد المحاولة | REFETCH | `nav-only` | in place | error state panel with Retry |
| `mobile-010.reconnect` | Reconnect / أعد الاتصال | REFETCH | `nav-only` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: post__lessons__lessonId__report.
- FRs: FR-ATT-003; FR-MOB-004.
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
- Branch: `flutter/usyd-t0649-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0649-slug`).
- PR title: `USYD-T0649: UX-MOBILE-010: Flutter Teacher Report — Flutter UI`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Flutter Mobile. **Stable external key:** `USYD-T0649`.

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
