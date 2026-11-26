# USYD-T0533 — UX-TEACHER-006: Teacher Classroom — Next.js production screen

> **Issue type:** Story · **Epic:** USYD-E-VIDEO · **Repository:** `web` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S37 · **Priority:** High · **Points:** 3 · **Gate:** Backlog

## Canonical source references
- `03_screens/screens/UX-TEACHER-006.md`
- `01_design/canvas/UX-TEACHER-006.dc.html`
- `FR-VIDEO-006`
- `FR-VIDEO-007`
- `FR-ATT-001`
- `FR-AI-010`
- `post__lessons__lessonId__join`
- `get__conferences__conferenceId__capabilities`

## Objective, scope & implementation detail
### Identity and route
**UX-TEACHER-006 — Teacher Classroom**. Persona `TEACHER`; role `Teacher`; route `/teach/lessons/:id/live`; module `VIDEO`; phase `P0`.

### Intent and exact design source
EN: Teacher classroom: video + interactive reader + quick rubric + notes.
AR: فصل المعلم: فيديو + قارئ تفاعلي + تقييم سريع + ملاحظات.

- Exact implementation spec: `03_screens/screens/UX-TEACHER-006.md` (read ALL sections).
- Live Claude Design: `01_design/canvas/UX-TEACHER-006.dc.html`; AR/EN HTML exports: `01_design/html/ar/UX-TEACHER-006.html` and `.../en/UX-TEACHER-006.html`.
- Shared tokens: `02_design_system/tokens.json`, `usayd-ui.css`, `AGE_ADAPTIVE_UI.md`.
- Components: Segmented control; Data table (cards < 760px); Status Chip; Quran reader (licensed text placeholder); Button; Card; Video stage; Classroom controls; Form field; Alert / Inline; Shell / Sidebar; Shell / App topbar; Timezone chip; Loading skeleton; State panel.
- Fields/validation hints: Teacher notes [optional].
- Responsive rule: App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production..
- Duplicate canonical route: none.

### Exact screen actions (5 detailed contracts)
| Action ID | AR / EN | Classification | Operation | Destination | Failure |
|---|---|---|---|---|---|
| `teacher-006.highlight-ayah` | Highlight ayah / تظليل الآية | API_EXISTING | `post__lessons__lessonId__join` | in place | inline Problem (code + localized message); 403 non-revealing; 409/412 conflict explained; 422 field errors |
| `teacher-006.add-note` | Add note / إضافة ملاحظة | API_EXISTING | `post__lessons__lessonId__join` | in place | inline Problem (code + localized message); 403 non-revealing; 409/412 conflict explained; 422 field errors |
| `teacher-006.share-passage` | Share passage / مشاركة المقطع | API_EXISTING | `post__lessons__lessonId__join` | in place | inline Problem (code + localized message); 403 non-revealing; 409/412 conflict explained; 422 field errors |
| `teacher-006.retry` | Retry / أعد المحاولة | REFETCH | `get__conferences__conferenceId__capabilities` | in place | error state panel with Retry |
| `teacher-006.reconnect` | Reconnect / أعد الاتصال | REFETCH | `get__conferences__conferenceId__capabilities` | in place | error state panel with Retry |

### API trace and permissions
- APIs from screen map: post__lessons__lessonId__join; get__conferences__conferenceId__capabilities.
- FRs: FR-VIDEO-006; FR-VIDEO-007; FR-ATT-001; FR-AI-010.
- Permission: Teacher — only assigned learners/lessons; PII minimized (no learner contact details)..
- State inventory: default, loading, empty, error (`SERVER_ERROR`), denied, offline, success — adapted to real screen meaning, not generic fake success.
- Unresolved: `none`. Owner-content slots hidden until approved.

### Acceptance and quality gates
Recreate responsive AR/EN visual composition in light/dark using canonical tokens, no prototype/spec-bar in production. Proper forms and keyboard/mobile navigation, AA contrast, touch targets, focus and aria status. Hook to real typed API when approved, otherwise display a clear feature-flag unavailable state (never mock-success). Browser/Flutter snapshot tests; 320/390/768/1440 CSS/visual, 6 states, permission-positive and negative tests. Apply exact spec and verify action contracts. PR link Jira ticket, screenshot evidence and test commands.

## Hard prerequisites
- `USYD-T0064` — Web design tokens and component primitives
- `USYD-T0326` — API POST /api/v1/lessons/{lessonId}/join (post__lessons__lessonId__join)
- `USYD-T0329` — API GET /api/v1/conferences/{conferenceId}/capabilities (get__conferences__conferenceId__capabilities)

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
- Branch: `web/usyd-t0533-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0533-slug`).
- PR title: `USYD-T0533: UX-TEACHER-006: Teacher Classroom — Next.js production screen`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Next.js Web. **Stable external key:** `USYD-T0533`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Classroom: one-time join token TTL, roster authorization, provider outage, fallback policy, recording consent, provider webhook verification, lesson status reconciliation.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `pnpm install --frozen-lockfile; pnpm lint; pnpm typecheck; pnpm test; pnpm build; pnpm e2e; visual/axe checks for changed screens` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
