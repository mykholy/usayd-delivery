# Design + Development Coordination Protocol

1. One design and code SSOT: UX ID + FR ID + API operationId + Jira ID. Every screen gets an interaction contract with input, output, state, error code, user roles.
2. Before UI work, Claude creates tokens/components and annotates each screen with API requirements. Codex reviews technical feasibility and gives feedback via an ADR, not silent design edits.
3. When an endpoint changes, Codex updates OpenAPI, generated typings and a `design-impact` list referencing UX IDs. Claude confirms affected variants and states.
4. When a design changes validation or business rules, Claude opens a spec change request; neither designer nor AI agent may silently alter payments, consent or eligibility.
5. Weekly integration demo from real staging with synthetic data, not static screenshots; unresolved mismatches tracked as Blockers.
6. Each user-facing flow requires contract, component, localization, telemetry and E2E acceptance. No cherry-picked happy path demos only.
7. Figma source, design exports, typed clients, test evidence and changelog form the release artifact set.
