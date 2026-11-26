# Usayd Academy (أكاديمية أُسَيْد) — Codex implementation package

> **v0.5 remediation (2026-11-21).** Read `PREMIUM_UX_CHANGELOG.md`, `IMPLEMENTATION_GATES.md`, `DECISION_LOG.md`, `07_api/API_GAPS.md`, `05_requirements/FR_GAPS.md`, `04_flows/JOURNEYS.md` and `11_qa/` first.
> Build gate by gate. Owner-content slots ship hidden, never with placeholder text. Every UNRESOLVED API stays behind a flag until its contract is approved.

You are OpenAI Codex. Build the **production** Usayd Academy platform (web + Flutter) from this package, module by module. This package is a specification and visual source — not running software.

## Read in this order
1. `00_AUDIT_AND_CHECKLIST.md` — what exists, duplicates, validation done, 169-screen checklist.
2. `02_design_system/` — `tokens.json`, `tokens.css`, `usayd-ui.css` (exact styles used by every screen), `COMPONENTS.md`, `BRAND.md`, `MOTION_AND_ILLUSTRATION.md`, `COLOR_AND_DARK_MODE.md` + `tokens.color.v0.4.json` (v0.4 palette, dark mode, contrast report), `SPLASH_SCREEN.md` (added screen UX-MOBILE-000, decision D-16).
3. `03_screens/SCREEN_SPECS_INDEX.md` → `03_screens/screens/<ID>.md` — one contract per screen (purpose, route, components, actions, fields + validation, states, navigation, API, permissions, responsive, unresolved). Machine-readable: `SCREEN_INVENTORY.csv` / `screen_inventory.json`.
4. `04_flows/USER_FLOWS.md` — 18 clickable journeys (+ the package’s 24 Mermaid flows and user stories).
5. `05_requirements/` — FRs, NFRs, business rules, globalization rules, **`UNRESOLVED.md`**.
6. `06_permissions/ROLES_AND_PERMISSIONS.md` — roles, permission keys, separation of duties, per-screen notes.
7. `07_api/` — `openapi.yaml` (authoritative), `API_CONTRACTS.md` (screen ↔ operation map + UNRESOLVED endpoints).
8. `08_data_model/` — entities, invariants, required additions.
9. `09_mapping/` — screen → module → FR → API; FR → screens.
10. `10_roadmap/IMPLEMENTATION_ROADMAP.md` — build order and exit criteria.

## Visual fidelity
- Open `01_design/html/ar/index.html` (or `/en/`) in a browser: static AR/EN exports of all 169 screens with working links. Match spacing, typography, colours and component styling exactly; reuse `usayd-ui.css` class names or port them 1:1 into your component library.
- `01_design/canvas/*.dc.html` are the live design sources (Claude Design canvas: https://claude.ai/artifact/NbQqBpDmhpBbY9Cvp5VHTR). Each holds both languages, light/dark and all states; strings live in the script block (`S.ar`, `S.en`) — use them as seed copy for i18n files.
- The dark strip at the top of each design (“spec bar”) and “Related screens” cards are design-only navigation aids. Do not ship them.

## Hard rules (do not break)
1. **Prototype ≠ backend.** Design buttons only navigate or toggle states. Implement real behavior from OpenAPI + specs; never fake success.
2. **Do not invent requirements.** Anything marked UNRESOLVED (27 endpoints, O-01…O-10, per-screen items) must be implemented behind a feature flag or raised as a question — never guessed, never hard-coded prices/legal text.
3. **Quran text** only from the licensed content service (`quran_references`); never typed, generated or machine-translated; never mirrored; no status colours on the text.
4. **AI** is advisory: provenance + reason + confidence label + teacher approval; gated by evaluation and consent; never authoritative grades or Quran wording.
5. **Minors:** unified learner account; limited mode until verified guardian consent (server-enforced); private results by default; no guardian dashboard in v1.
6. **Money & time:** integer minor units + ISO currency from market price books (KWD/BHD/OMR = 3 decimals); store UTC instants, display in each user’s IANA zone; DST ambiguity must be chosen by the user.
7. **Locale, country, timezone are independent settings.** Changing language never changes price, quote ID or booked instants.
8. **Authorization server-side** (RBAC × scope × ownership); no self-approval; reasons + append-only audit for sensitive actions; secrets never displayed.
9. **RTL/LTR** with logical CSS; AR default. Accessibility WCAG 2.2 AA (focus ring, 44px targets, labels, role=alert for errors, reduced motion).
10. Every screen ships all states: loading, empty, error (with stable code), no-permission (403 explained), offline, success.

## Definition of done per screen
Matches design (AR/EN, 1440/768/390, light/dark) · API calls per spec §8 · validation per §5 (server + client) · permission per §9 · states per §7 · analytics per §13 · tests: unit, API contract, E2E for its journeys, RTL visual snapshot, axe accessibility.

## Brand
أكاديمية أُسَيْد / Usayd Academy — see `02_design_system/BRAND.md`. The request text said “Ased Academy”; the brand book mandates **Usayd** (Latin) and «أُسَيْد» with tashkeel. Keep that unless the owner confirms otherwise.

## Source package
`source_blueprint_v1.2/` contains the full original specification package (SRS/PRD/OpenAPI/Jira/QA) for reference. Where it conflicts with this package, v1.2 rules + this package’s screen specs win; raise conflicts instead of guessing.

---
## Remediation release (2026-11-23) — read this section first
- Measured inventory: **169 product screens + 9 journey boards = 178 boards**. Any older “160/161 screens” or “170 boards” wording in historical files is superseded by this line (`SCREEN_VISUAL_QA_160.csv` keeps its old file name; it has one row per current screen).
- Start with `CODEX_HANDOFF_MASTER.md`, then `11_qa/HANDOFF_READINESS_REPORT_AR.md` (GO / CONDITIONAL GO / NO-GO).
- New: `07_api/API_RECONCILIATION_MATRIX.csv`, `openapi.proposed.yaml` (PROPOSED), `API_VALIDATION_REPORT.md`, `API_CONTRACT_TESTS.md`, `08_data_model/STATE_ALIGNMENT.md`, `04_flows/JOURNEY_WALKTHROUGHS.md`, `JOURNEY_COVERAGE_MATRIX.csv`, `acceptance/*.feature`, `FLOW_CLASSIFICATION.md`, `03_screens/ACTION_CONTRACTS_DETAILED.csv`, `CANONICAL_ROUTES.csv`, `OWNER_CONTENT_REGISTER.md`, `09_mapping/FR_TRACEABILITY.csv`, `SCREEN_API_MAP.csv`, `06_permissions/PERMISSIONS_MATRIX.*`, `10_roadmap/FEATURE_FLAGS.csv`, `OWNER_SIGNOFF_CHECKLIST.md`, `DECISION_REQUIRED_FROM_OWNER.md`, `11_qa/VISUAL_QA_MATRIX.csv`, `REMEDIATION_BASELINE.csv`, `REGRESSION_REPORT.md`, `CHANGE_MANIFEST.csv`, `CHANGELOG.md`.
