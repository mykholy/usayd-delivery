# USYD-T0107 — FR-TCHR-001: تسجيل واستقدام المعلمين

> **Issue type:** Story · **Epic:** USYD-E-TCHR · **Repository:** `api` · **Assignee lane:** Full Stack / Codex · **Candidate Sprint:** S24 · **Priority:** High · **Points:** 2 · **Gate:** Backlog

## Canonical source references
- `05_requirements/functional_requirements.csv`
- `FR:FR-TCHR-001`
- `UX-ADMIN-006`
- `UX-TEACHER-001`

## Objective, scope & implementation detail
### Approved requirement text (verbatim)
طلب/وثائق/تحقق هوية ومؤهلات ومراجع واختبار تدريس ومراجعة حماية القاصرين.

### Engineering implementation
Implement domain-specific rule for **FR-TCHR-001** with explicit invariants, validation, state transitions, scope/ownership, and persistence only where required by approved contract. For requirements that are UI-only or about accessibility, put behavior in the owning app; do not build unnecessary endpoints.

### Traceability
- Requirement role: `teacher,admin`; phase `P0`; priority `Must`.
- Mapped screens: `UX-ADMIN-006; UX-TEACHER-001`.
- Existing APIs: `post__auth_login`.
- Proposed APIs: `decideTeacherApplication; listTeacherApplications; submitTeacherApplication`.
- Entities: `teacher_profiles, teacher_credentials, teacher_availability`.
- Journeys: `J03 `.
- Contract acceptance reference: `acceptance/J03.feature`.

### Verification
Positive unit test; invalid boundary test; ownership and negative permission test; concurrent/retry test if stateful; MySQL integration tests for persistence. Validate API compatibility if relevant. Never promote blocked decisions to approved.

## Hard prerequisites
- `USYD-T0044` — TCHR: approve scope, OpenAPI and state-machine contract

## Owner/external block
None documented in this ticket; always check source decision register and flags.

## Acceptance criteria & Definition of Done
- [ ] Implement exactly approved requirements and preserve original behavior / visual design
- [ ] Add positive, negative, permission/ownership, timeout/error tests as applicable
- [ ] MySQL integration & concurrency tests for stateful API actions (no SQLite-only substitute)
- [ ] Run formatting, static analysis, unit and relevant integration E2E checks
- [ ] Create focused branch and one reviewed PR linked to this ticket and passing CI
- [ ] Update contract docs / SDK version / migration docs if affected
- [ ] No unapproved decision, placeholder, simulated success or live secrets

## PR contract
- Branch: `api/usyd-t0107-short-slug` (adapt to Git naming restrictions; prefer `feat/USYD-T0107-slug`).
- PR title: `USYD-T0107: FR-TCHR-001: تسجيل واستقدام المعلمين`.
- Body: Jira link, FR/Screen/Operation IDs, design before/after if UI, migrations, test commands/results, security/privacy review, rollback.
- Await independent review for sensitive IAM, minors, payments, payroll, video recording, secrets, permissions, schema or deployment changes.
- Merge only after required checks, reviewer approval and no unresolved blocking comments. Do not self-approve or bypass protection. After merge, close the ticket only with real evidence.

## Production execution detail — reviewer checklist

**Owning application:** Backend/API. **Stable external key:** `USYD-T0107`.

### Before implementation
- Read every canonical reference in this ticket from `source_original/usayd-academy-codex-package/`; open full screen-specific Markdown and actual HTML/CSS/RTL exports when referenced. Do not implement from the ticket headline alone.
- Confirm dependency keys have been merged (not simply opened), and that proposed API and business decisions are approved for this scope. No speculative schema or unauthorized paid/child-sensitive behavior.
- Prepare a short contract-first plan in the PR: inputs, outputs, state mutations, authorization, error states, rollback and consumers.

### Domain-specific edge cases to demonstrate
- Validate exact UI/permission/API obligations against cited source, including success/failure, boundary values, cancellation and retries.
- Verify at least one **negative** scenario and one **boundary** scenario from original specs; use the actual example data or approved fixtures, not a simulated success response.
- On cross-repo contracts, publish a versioned OpenAPI/schema artifact and create consumer update tickets rather than directly editing another repository within this PR.

### Concrete PR evidence
- Attach the exact command and result for `composer validate; ./vendor/bin/pint --test; php artisan test (MySQL service DB); OpenAPI lint; migration fresh; static analysis where configured` (skip inapplicable commands only with written justification).
- Include actual changed files, safe migration/rollback notes, security and privacy impact, AR/EN+light/dark screenshots for UI, and linked Jira key.
- Mark `Blocked` if a required owner/legal decision is missing; don't silently invent it.
- AI review is **advisory code quality evidence**, not a substitute for a required human reviewer. Auto-merge requires verified branch rules + green required checks; high-risk changes additionally require independent human approval.
