# USYD-T0539 — UX-TEACHER-012: Question Bank Review — Next.js production screen

> **Issue type:** Story · **Epic:** USYD-E-CURR · **Repository:** `web` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S23 · **Priority:** High · **Points:** 3 · **Gate:** Blocked / Conditional

## Canonical source references
- `03_screens/screens/UX-TEACHER-012.md`
- `01_design/canvas/UX-TEACHER-012.dc.html`
- `FR-CURR-006`
- `FR-CONTEST-006`
- `FR-AI-005`

## Objective, scope & implementation detail
### Identity and route
**UX-TEACHER-012 — Question Bank Review**. Persona `TEACHER`; role `Teacher`; route `/teach/questions`; module `CURR`; phase `P0`.

### Intent and exact design source
EN: Review question-bank items before publishing.
AR: مراجعة أسئلة بنك الاختبارات قبل النشر.

- Exact implementation spec: `03_screens/screens/UX-TEACHER-012.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-TEACHER-012.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-TEACHER-012.html` and `.../en/UX-TEACHER-012.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Page header; Status Chip; Button; Data table (cards < 760px); Quran reader (licensed text placeholder); Card; Shell / Sidebar; Shell / App topbar; Timezone chip; Loading skeleton; Alert / Inline; State panel.
- Fields/validation hints: See per-screen spec.
- Responsive rule: App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production..
- Duplicate canonical route: none.

### Exact screen actions (6 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `teacher-012.review` | Review / راجع | UI_ONLY | `nav-only` | in place | — |
| `teacher-012.review` | Review / راجع | UI_ONLY | `nav-only` | in place | — |
| `teacher-012.approve` | Approve / اعتمد | API_PROPOSED | `decideQuestionItem` | in place | inline Problem (code + localized message); 403 non-revealing; 409/412 conflict explained; 422 field errors |
| `teacher-012.request-changes` | Request changes / اطلب تعديلًا | API_PROPOSED | `decideQuestionItem` | in place | inline Problem (code + localized message); 403 non-revealing; 409/412 conflict explained; 422 field errors |
| `teacher-012.retry` | Retry / أعد المحاولة | REFETCH | `listQuestionBankItems` | in place | error state panel with Retry |
| `teacher-012.reconnect` | Reconnect / أعد الاتصال | REFETCH | `listQuestionBankItems` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: P-10.
- FRs: FR-CURR-006; FR-CONTEST-006; FR-AI-005.
- Permission: Teacher — only assigned learners/lessons; PII minimized (no learner contact details)..
- State inventory: default, loading, empty, error (`SERVER_ERROR`), denied, offline, success — adapted to real screen meaning, not generic fake success.
- Unresolved: `API: GET /api/v1/question-bank-items?status=review — UNRESOLVED — PROPOSED listQuestionBankItems (P-10)`. Owner-content slots hidden until approved.

### Acceptance and quality gates
Recreate responsive AR/EN visual composition in light/dark using canonical tokens, no prototype/spec-bar in production. Proper forms and keyboard/mobile navigation, AA contrast, touch targets, focus and aria status. Hook to real typed API when approved, otherwise display a clear feature-flag unavailable state (never mock-success). Browser/Flutter snapshot tests; 320/390/768/1440 CSS/visual, 6 states, permission-positive and negative tests. Apply exact spec and verify action contracts. PR link Jira ticket, screenshot evidence and test commands.

## Hard prerequisites
- `USYD-T0064` — Web design tokens and component primitives

## Owner/external block
API: GET /api/v1/question-bank-items?status=review — UNRESOLVED — PROPOSED listQuestionBankItems (P-10)

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] Visual/accessibility/device/contract tests matching target repo
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `web/usyd-t0539-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0539-slug`).
- PR title: `USYD-T0539: UX-TEACHER-012: Question Bank Review — Next.js production screen`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Next.js Web. **Stable external key:** `USYD-T0539`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Curriculum: Quran licensed-source availability, surah/ayah boundary correctness, no generated Quran text, authorized curriculum editing and version tracking.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `pnpm install --frozen-lockfile; pnpm lint; pnpm typecheck; pnpm test; pnpm build; pnpm e2e; visual/axe checks for changed screens` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
