# Codex handoff — master brief

Read this first. It replaces nothing; it tells you what to build, in what order, from which files.

## What exists
- **169 product screens + 9 journey boards** (stable IDs, routes unchanged): `03_screens/SCREEN_INVENTORY.csv`, one spec per screen in `03_screens/screens/` (sections 1–19; §19 = action bindings).
- Visual source: `01_design/html/{ar,en}/` static exports (open `index.html`) + `02_design_system/` (tokens, components, `usayd-ui.css`).
- **API baseline:** `07_api/openapi.yaml` — 121 operations (draft, approved for planning, not implemented).
- **API proposals:** `07_api/openapi.proposed.yaml` — 57 operations, **PROPOSED, not approved**. `API_RECONCILIATION_MATRIX.csv` says which screen/journey needs which.
- Journeys: `04_flows/JOURNEY_WALKTHROUGHS.md` (J01–J17) + `04_flows/acceptance/*.feature` (36 scenarios).
- Requirements: `09_mapping/FR_TRACEABILITY.csv` (216 FRs) · permissions `06_permissions/PERMISSIONS_MATRIX.md` · decisions `DECISION_REQUIRED_FROM_OWNER.md` · flags `10_roadmap/FEATURE_FLAGS.csv`.

## Rules you must not break
1. Never generate or paraphrase Quran text; references only, from the licensed source (O-06).
2. Never ship owner content as sample text (`03_screens/OWNER_CONTENT_REGISTER.md`) — hide and show the safe state.
3. Authorization server-side on every request: role × scope × ownership; out-of-scope = non-revealing 403/404.
4. Money = integer minor units + ISO currency (3-decimal currencies supported); entitlement only from verified, deduplicated webhooks.
5. Time = UTC instant + IANA zone (+ tzdb version for rules); DST gaps rejected, overlaps resolved explicitly.
6. No self-approval; maker ≠ checker; append-only audit events.
7. Do not merge a PROPOSED operation into `openapi.yaml` until it is approved; operations marked NEEDS_APPROVAL stay behind their feature flag.
8. Do not build mock backends and call them production. Tests against stubs are labelled as such.

## Build sequence (Laravel API first, then web, then Flutter)
| # | Module | Start when | Build from |
|---|---|---|---|
| 0 | Foundations: project, CI, RFC 7807 errors, Idempotency-Key middleware, audit log, outbox, settings versions, feature flags, i18n (ar/en) | now | IMPLEMENTATION_GATES §0, D-42 |
| 1 | Identity, sessions, MFA, RBAC/ABAC + logout (P-39) + password reset (P-20/21) + devices (P-37/38) | after D-42 approval | J11, PERMISSIONS_MATRIX |
| 2 | Markets, price books, locale/timezone independence | O-01 for activation (build with markets off) | J16, J01 |
| 3 | Consent ledger + guardian flow | **O-04/O-05** — build ledger + limited mode now; guardian verification behind `guardian_consent_v1` | J02 |
| 4 | Programs, teachers (applications P-03/04/05, admin/public profiles P-06/07/08), availability | — | J03 |
| 5 | Booking & time: slot holds (P-30), bookings (C-01), reschedule, cancel (P-31), DST | O-02 only for cancellation credit rules | J04 |
| 6 | Classroom: join, provider adapter, webhooks, attendance, incidents | O-03 for in-app vendor (external links first) | J06 |
| 7 | Lesson reports: drafts (P-35) + submit (C-08) | — | J07 |
| 8 | Learning: assessments, plans (C-13/14/17), revision, memory map | O-06 for Quran references | J08, J09 |
| 9 | Payments: quotes, checkout, webhooks, subscriptions, refunds (P-40) | **O-01, O-02** | J05 |
| 10 | Supervision, settings, audit review (P-42), notifications (P-24/25), support | D-39 for break-glass | J11, J12, J14 |
| 11 | Competitions + appeals | O-07 for rewards | J10 |
| 12 | Payroll | **O-08** | J15 |
| 13 | Mobile (Flutter): offline sync (P-36), app styles (C-04) | D-35/36/37 for kids mode | J13, J17 |

Each module: implement only approved contracts → contract tests (`07_api/API_CONTRACT_TESTS.md`) → acceptance scenarios → negative permission tests → AR/EN UI from the static exports → visual compare at 390 and 1440 px.
