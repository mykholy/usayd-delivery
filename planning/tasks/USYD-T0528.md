# USYD-T0528 — UX-TEACHER-001: Teacher Login & Onboarding — Next.js production screen

> **Issue type:** Story · **Epic:** USYD-E-TCHR · **Repository:** `web` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S26 · **Priority:** High · **Points:** 3 · **Gate:** Blocked / Conditional

## Canonical source references
- `03_screens/screens/UX-TEACHER-001.md`
- `01_design/canvas/UX-TEACHER-001.dc.html`
- `FR-TCHR-001`
- `FR-TCHR-005`
- `FR-IAM-005`
- `FR-PAYROLL-001`
- `post__auth_login`

## Objective, scope & implementation detail
### Identity and route
**UX-TEACHER-001 — Teacher Login & Onboarding**. Persona `TEACHER`; role `Guest / onboarding user`; route `/teach/start`; module `TCHR`; phase `P0`.

### Intent and exact design source
EN: Teacher sign-in & onboarding: credentials, safeguarding, contract, training.
AR: تسجيل المعلم وتهيئته: المؤهلات والحماية والعقد والتدريب.

- Exact implementation spec: `03_screens/screens/UX-TEACHER-001.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-TEACHER-001.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-TEACHER-001.html` and `.../en/UX-TEACHER-001.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Stepper; Status Chip; List row; Card; Form field; Checkbox / consent; Button; Loading skeleton; Alert / Inline; State panel.
- Fields/validation hints: ID / document number [required; stored encrypted; visible to HR only]; I acknowledge the child safeguarding policy [must be checked].
- Responsive rule: Two-panel (brand night panel + form) ≥760; single column <760 with brand panel stacked above; form max 640..
- Duplicate canonical route: none.

### Exact screen actions (2 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `teacher-001.retry` | Retry / أعد المحاولة | REFETCH | `nav-only` | in place | error state panel with Retry |
| `teacher-001.reconnect` | Reconnect / أعد الاتصال | REFETCH | `nav-only` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: post__auth_login; P-04.
- FRs: FR-TCHR-001; FR-TCHR-005; FR-IAM-005; FR-PAYROLL-001.
- Permission: Teacher applicant / onboarding teacher. MFA mandatory..
- State inventory: default, loading, empty, error (`SERVER_ERROR`), denied, offline, success — adapted to real screen meaning, not generic fake success.
- Unresolved: `API: POST /api/v1/teacher-applications — UNRESOLVED — PROPOSED submitTeacherApplication (P-04)`. Owner-content slots hidden until approved.

### Acceptance and quality gates
Recreate responsive AR/EN visual composition in light/dark using canonical tokens, no prototype/spec-bar in production. Proper forms and keyboard/mobile navigation, AA contrast, touch targets, focus and aria status. Hook to real typed API when approved, otherwise display a clear feature-flag unavailable state (never mock-success). Browser/Flutter snapshot tests; 320/390/768/1440 CSS/visual, 6 states, permission-positive and negative tests. Apply exact spec and verify action contracts. PR link Jira ticket, screenshot evidence and test commands.

## Hard prerequisites
- `USYD-T0064` — Web design tokens and component primitives
- `USYD-T0302` — API POST /api/v1/auth/login (post__auth_login)

## Owner/external block
API: POST /api/v1/teacher-applications — UNRESOLVED — PROPOSED submitTeacherApplication (P-04)

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] Visual/accessibility/device/contract tests matching target repo
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `web/usyd-t0528-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0528-slug`).
- PR title: `USYD-T0528: UX-TEACHER-001: Teacher Login & Onboarding — Next.js production screen`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Next.js Web. **Stable external key:** `USYD-T0528`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Validate exact UI/permission/API obligations against cited source, including success/failure, boundary values, cancellation and retries.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `pnpm install --frozen-lockfile; pnpm lint; pnpm typecheck; pnpm test; pnpm build; pnpm e2e; visual/axe checks for changed screens` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
