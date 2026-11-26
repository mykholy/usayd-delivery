# UX-TEACHER-001 — Teacher Login & Onboarding

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-TEACHER-001`
- **Name:** Teacher Login & Onboarding
- **Role:** Guest / onboarding user · inventory persona `TEACHER`
- **Module:** `TCHR` · phase `P0`
- **Route:** `/teach/start`
- **Design files:** `01_design/canvas/UX-TEACHER-001.dc.html` · `01_design/html/ar/UX-TEACHER-001.html` · `01_design/html/en/UX-TEACHER-001.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Teacher sign-in & onboarding: credentials, safeguarding, contract, training.
- AR: تسجيل المعلم وتهيئته: المؤهلات والحماية والعقد والتدريب.
- Primary action (inventory): استكمال البيانات

## 3. UI components
- Stepper
- Status Chip
- List row
- Card
- Form field
- Checkbox / consent
- Button
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: qualification checklist; contract; safeguarding

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Continue | navigates to `UX-TEACHER-002.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Choose another country | navigates to `UX-GLOB-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| ID / document number | text | yes | required; stored encrypted; visible to HR only | — |
| I acknowledge the child safeguarding policy | checkbox | yes | must be checked | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Follow module rules in `05_requirements/` and the FRs listed in §8.

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Your changes were saved” · AR «تم حفظ التغييرات» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/auth/login` | `post__auth_login` |
| `POST /api/v1/teacher-applications` | `UNRESOLVED — PROPOSED submitTeacherApplication (P-04)` |
- **Functional requirements:** FR-TCHR-001, FR-TCHR-005, FR-IAM-005, FR-PAYROLL-001
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Teacher applicant / onboarding teacher. MFA mandatory.

## 10. Navigation destinations
- `UX-GLOB-001.dc.html`
- `UX-TEACHER-002.dc.html`
- Shell navigation: auth layout

## 11. Responsive behavior
- Two-panel (brand night panel + form) ≥760; single column <760 with brand panel stacked above; form max 640.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ API: POST /api/v1/teacher-applications — UNRESOLVED — PROPOSED submitTeacherApplication (P-04)

## 13. Analytics
- `screen_viewed` {screen_id:"UX-TEACHER-001", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"teacher-001.retry"} — Retry
- `action_clicked` {action_id:"teacher-001.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `teacher-001.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-001.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- None.

## 16. Themes & breakpoints
- Light and dark use the same markup; colours only from tokens (`02_design_system/tokens.color.v0.4.json`). Night surfaces stay night in both themes.
- 360/390: single column, sticky primary CTA, tables become stacked records, calendar becomes an agenda list · 768: two columns where space allows, sidebar collapses to the top bar · 1024: sidebar visible, splits stack below 1100 · 1440: design reference width.

## 17. Acceptance criteria
- [ ] Renders in Arabic (RTL) and English (LTR), light and dark, at 360, 390, 768, 1024 and 1440 px without horizontal page scroll
- [ ] All seven states (default, loading, empty, error, no-permission, offline, success) are reachable and use the copy in §7
- [ ] Every interactive target is at least 44×44 px; every control has an accessible name; focus order follows reading order
- [ ] Text contrast ≥ 4.5:1 and non-text ≥ 3:1 in both themes (axe: 0 serious/critical violations)
- [ ] One H1; heading levels never skip
- [ ] `post__auth_login` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `POST /api/v1/teacher-applications` is behind a feature flag until its contract is approved (see `07_api/API_GAPS.md`)
- [ ] `teacher-001.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-001.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `teacher-001.retry` Retry | action | REFETCH | — | high | Re-runs the failed request(s) |
| `teacher-001.reconnect` Reconnect | action | REFETCH | — | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
