# v1.1 Release Notes — AI Implementation Handoff

## Changes versus v1.0
- Added root `AGENTS.md` and `CLAUDE.md`; separated design and engineering instructions, phase-level stop rules and handoff contract.
- Repaired OpenAPI base URL duplication, auth exceptions, typed responses for all existing operations; added concrete API examples, validation and explicit security notes.
- Added actionable academic/competition/guardian/payment/video Gherkin journeys and adversarial tests.
- Added test evidence requirements, `pytest`/Python-independent validator (unittest), CI specification checks, Playwright/Pest/Flutter starter patterns (templates only).
- Added domain event/outbox/idempotency, lesson provider negotiation, failover expectations and compensation ledger design.
- Added screen interaction matrix + Figma component/state sign-off + mobile edge cases.
- Added Jira tasks for contract typing, privacy, infrastructure, CI, QA, AI model evaluation, fairness, mobile reliability and first launch.
- Captured unresolved business/legal/vendor decisions as gates; no invented stakeholder sign-off.

## What this release DOES NOT mean
- No Laravel, React, Flutter, Figma or video backend has been built or executed.
- Sample tests check package integrity and abstract contracts. They cannot verify running software yet.
- Neither provider terms nor academic certifications nor permissions to process minor audio are approved by this pack.
- Generic requirements still need story-level mapping to live endpoints and designs during implementation; changes require traceability updates.
