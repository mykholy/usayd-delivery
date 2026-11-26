# Changelog

## 2026-11-23 — remediation release (design/spec/contract readiness; no backend)
Baseline: the 2026-11-22 package (`usayd-academy-codex-package.zip`). File-level diff: `11_qa/CHANGE_MANIFEST.csv` ({'added': 103, 'removed': 1, 'modified': 751}). Stable screen IDs and routes unchanged; `source_blueprint_v1.2/` untouched.

### Design
- No-permission states: “Request access” removed everywhere (no API/FR); role-home or support link instead. Success copy matches the screen (D-38).
- UX-SUP-004: break-glass disabled with reason; assignment guidance (D-39).
- OPEN-01: 10 admin/supervisor screens redesigned for operational density (D-40, `DENSITY_SCENARIOS.md`).
- OPEN-02: interactive slide-to-confirm in static exports (D-41, `SLIDE_TO_CONFIRM_SPEC.md`).
- Deferred/blocked buttons disabled with reasons: Import (question bank), New template (competitions), Listen to approved reciter (O-06).
- CSS v1.0 layer (density + slide) — canvas asset updated.
- Static exports: 86 broken internal links fixed (K/S screens + index).

### Contracts and specifications
- API: 28 gap rows reclassified individually; 57 PROPOSED operations in `openapi.proposed.yaml` (valid OpenAPI 3.1); 17 corrections to existing operations/schemas; state-machine alignment.
- Every screen API reference resolved (existing, proposed, owner decision or static content); admin screens no longer use public operations with `?admin=1`.
- Action contracts: 641 rows classified and bound in `ACTION_CONTRACTS_DETAILED.csv` and spec §19.
- Journeys: 17 walkthroughs (J01–J17), 36 Gherkin scenarios, coverage matrix; FLOW_MATRIX happy paths filled for 7 flows; flow classification.
- Requirements: FR traceability for 216 FRs; FR_GAPS revalidated; permissions matrix + negative tests; canonical routes; owner content register; feature flags; owner decision brief + sign-off checklist.
- Decision log: D-38 … D-43 added; D-16/24/27/35/36/37/39/42/43 and O-01…O-10 remain open.
