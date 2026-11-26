# Blockers and open decisions (separate register)

The grouped, actionable version is `DECISION_REQUIRED_FROM_OWNER.md` (repository root). This page is the QA-side summary.

## Owner decisions (blueprint O-01…O-10) — all still open
O-01 legal entity & markets · O-02 pricing · O-03 video vendor · O-04 minors & guardian verification · O-05 recording/AI consent · O-06 Quran text licence & academic authority · O-07 contest prizes · O-08 payroll contracts · O-09 support hours · O-10 funding tranche.
Pending design decisions: D-16, D-24, D-27, D-35, D-36, D-37 (mascot), D-39, D-42, D-43 and the kids guardian-PIN storage question.

## Owner content
`03_screens/OWNER_CONTENT_REGISTER.md` (12 content items; CONTENT_REQUIRED slot instances counted in `CONTENT_SLOTS.csv`). Hidden in production until supplied.

## API
The 28 gap rows are reclassified in `07_api/API_GAPS.md`; proposals in `openapi.proposed.yaml` (PROPOSED, not approved). Operations that also need an owner decision stay behind feature flags (`10_roadmap/FEATURE_FLAGS.csv`).

## Design work still open
- R-019 (P3, accepted risk): no sort control on stacked admin tables below 760 px.

## Needs human / external verification
Screen readers, real devices, 200% text resize, forced colours, Flutter, human visual sign-off. Script: `A11Y_MANUAL_TEST_SCRIPT.md`.
