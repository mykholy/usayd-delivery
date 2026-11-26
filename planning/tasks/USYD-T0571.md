# USYD-T0571 — UX-ADMIN-026: Contest Builder Wizard — Next.js production screen

> **Issue type:** Story · **Epic:** USYD-E-CONTEST · **Repository:** `web` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S61 · **Priority:** High · **Points:** 3 · **Gate:** Blocked / Conditional

## Canonical source references
- `03_screens/screens/UX-ADMIN-026.md`
- `01_design/canvas/UX-ADMIN-026.dc.html`
- `FR-CONTEST-001`
- `FR-CONTEST-002`
- `FR-CONTEST-010`
- `FR-CONTEST-014`
- `post__admin_competitions`

## Objective, scope & implementation detail
### Identity and route
**UX-ADMIN-026 — Contest Builder Wizard**. Persona `ADMIN`; role `Platform admin (scoped)`; route `/admin/competitions/new`; module `CONTEST`; phase `P0`.

### Intent and exact design source
EN: Contest builder wizard.
AR: معالج إنشاء مسابقة.

- Exact implementation spec: `03_screens/screens/UX-ADMIN-026.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-ADMIN-026.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-ADMIN-026.html` and `.../en/UX-ADMIN-026.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Page header; Stepper; Form field; Checkbox / consent; Card; Status Chip; List row; Button; Unresolved-requirement note; Shell / Sidebar; Shell / App topbar; Timezone chip; Loading skeleton; Alert / Inline; State panel.
- Fields/validation hints: Eligible levels [required]; Age group [required]; Markets [required]; Requires guardian consent for minors [must be checked]; Minors’ standings private by default [must be checked]; Free entry, no mandatory fees [must be checked].
- Responsive rule: App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production..
- Duplicate canonical route: none.

### Exact screen actions (3 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `admin-026.next-rounds` | Next: rounds / التالي: الجولات | API_EXISTING | `post__admin_competitions` | in place | inline Problem (code + localized message); 403 non-revealing; 409/412 conflict explained; 422 field errors |
| `admin-026.retry` | Retry / أعد المحاولة | REFETCH | `nav-only` | in place | error state panel with Retry |
| `admin-026.reconnect` | Reconnect / أعد الاتصال | REFETCH | `nav-only` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: post__admin_competitions.
- FRs: FR-CONTEST-001; FR-CONTEST-002; FR-CONTEST-010; FR-CONTEST-014.
- Permission: Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver..
- State inventory: default, loading, empty, error (`SERVER_ERROR`), denied, offline, success — adapted to real screen meaning, not generic fake success.
- Unresolved: `Prize policy (O-07); Prize policy (O-07)`. Owner-content slots hidden until approved.

### Acceptance and quality gates
Recreate responsive AR/EN visual composition in light/dark using canonical tokens, no prototype/spec-bar in production. Proper forms and keyboard/mobile navigation, AA contrast, touch targets, focus and aria status. Hook to real typed API when approved, otherwise display a clear feature-flag unavailable state (never mock-success). Browser/Flutter snapshot tests; 320/390/768/1440 CSS/visual, 6 states, permission-positive and negative tests. Apply exact spec and verify action contracts. PR link Jira ticket, screenshot evidence and test commands.

## Hard prerequisites
- `USYD-T0064` — Web design tokens and component primitives
- `USYD-T0348` — API POST /api/v1/admin/competitions (post__admin_competitions)

## Owner/external block
Prize policy (O-07); Prize policy (O-07)

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] Visual/accessibility/device/contract tests matching target repo
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `web/usyd-t0571-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0571-slug`).
- PR title: `USYD-T0571: UX-ADMIN-026: Contest Builder Wizard — Next.js production screen`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Next.js Web. **Stable external key:** `USYD-T0571`.

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
