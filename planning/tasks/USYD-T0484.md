# USYD-T0484 — UX-PUBLIC-006: Teacher Public Profile — Next.js production screen

> **Issue type:** Story · **Epic:** USYD-E-TCHR · **Repository:** `web` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S28 · **Priority:** High · **Points:** 3 · **Gate:** Blocked / Conditional

## Canonical source references
- `03_screens/screens/UX-PUBLIC-006.md`
- `01_design/canvas/UX-PUBLIC-006.dc.html`
- `FR-TCHR-002`
- `get__teachers__teacherId__availability`

## Objective, scope & implementation detail
### Identity and route
**UX-PUBLIC-006 — Teacher Public Profile**. Persona `PUBLIC`; role `Guest (public)`; route `/teachers/:slug`; module `TCHR`; phase `P0`.

### Intent and exact design source
EN: Public teacher profile and credentials.
AR: عرض ملف المعلم العام والمؤهلات.

- Exact implementation spec: `03_screens/screens/UX-PUBLIC-006.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-PUBLIC-006.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-PUBLIC-006.html` and `.../en/UX-PUBLIC-006.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Button; Page header; Image placeholder (licensed asset pending); Card; Status Chip; List row; Timezone chip; Page hero (illustrated); Shell / Public header; Loading skeleton; Alert / Inline; State panel; Shell / Public footer.
- Fields/validation hints: See per-screen spec.
- Responsive rule: Fluid page: max content 1280; ≥1100 multi-column; 760–1100 grids collapse to 2 columns; <760 single column, header nav hides (burger), CTAs stay visible; touch targets ≥44px..
- Duplicate canonical route: none.

### Exact screen actions (2 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `public-006.retry` | Retry / أعد المحاولة | REFETCH | `getPublicTeacher; get__teachers__teacherId__availability` | in place | error state panel with Retry |
| `public-006.reconnect` | Reconnect / أعد الاتصال | REFETCH | `getPublicTeacher; get__teachers__teacherId__availability` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: P-08; get__teachers__teacherId__availability.
- FRs: FR-TCHR-002.
- Permission: Public; PII minimized..
- State inventory: default, loading, empty, error (`SERVER_ERROR`), denied, offline, success — adapted to real screen meaning, not generic fake success.
- Unresolved: `API: GET /api/v1/teachers/{teacherId} — UNRESOLVED — PROPOSED getPublicTeacher (P-08)`. Owner-content slots hidden until approved.

### Acceptance and quality gates
Recreate responsive AR/EN visual composition in light/dark using canonical tokens, no prototype/spec-bar in production. Proper forms and keyboard/mobile navigation, AA contrast, touch targets, focus and aria status. Hook to real typed API when approved, otherwise display a clear feature-flag unavailable state (never mock-success). Browser/Flutter snapshot tests; 320/390/768/1440 CSS/visual, 6 states, permission-positive and negative tests. Apply exact spec and verify action contracts. PR link Jira ticket, screenshot evidence and test commands.

## Hard prerequisites
- `USYD-T0064` — Web design tokens and component primitives
- `USYD-T0312` — API GET /api/v1/teachers/{teacherId}/availability (get__teachers__teacherId__availability)

## Owner/external block
API: GET /api/v1/teachers/{teacherId} — UNRESOLVED — PROPOSED getPublicTeacher (P-08)

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] Visual/accessibility/device/contract tests matching target repo
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `web/usyd-t0484-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0484-slug`).
- PR title: `USYD-T0484: UX-PUBLIC-006: Teacher Public Profile — Next.js production screen`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Next.js Web. **Stable external key:** `USYD-T0484`.

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
