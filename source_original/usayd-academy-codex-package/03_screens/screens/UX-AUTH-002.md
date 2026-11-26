# UX-AUTH-002 — Guardian Consent Step

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-AUTH-002`
- **Name:** Guardian Consent Step
- **Role:** Guest / onboarding user · inventory persona `AUTH`
- **Module:** `IAM` · phase `P0`
- **Route:** `/onboarding/guardian-consent`
- **Design files:** `01_design/canvas/UX-AUTH-002.dc.html` · `01_design/html/ar/UX-AUTH-002.html` · `01_design/html/en/UX-AUTH-002.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Guardian consent gate for minors without a guardian dashboard.
- AR: بوابة موافقة ولي الأمر للقاصر دون لوحة ولي أمر.
- Primary action (inventory): إرسال طلب الموافقة

## 3. UI components
- Stepper
- Alert / Inline
- Form field
- Checkbox / consent
- Button
- Key-value list
- Card
- Unresolved-requirement note
- Loading skeleton
- State panel
- Inventory anatomy: guardian contact; proof; consent receipt; pending

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Send approval request | navigates to `UX-AUTH-005.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Choose another country | navigates to `UX-GLOB-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| Guardian name | text | yes | required | — |
| Guardian phone or email | tel | yes | required; must differ from learner contact | — |
| Relationship | select | yes | required | — |
| I understand approval happens on the guardian’s device, not in my account | checkbox | yes | must be checked | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- A minor’s own checkbox is NOT guardian consent
- Verified guardian contact (OTP to guardian)
- Learner stays in limited mode: no payment, no live lesson
- Consent receipt versioned, withdrawable

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `CONSENT_EXPIRED`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Consent request sent to guardian” · AR «أرسلنا طلب الموافقة لولي الأمر» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/consents` | `post__consents` |
| `GET /api/v1/me` | `get__me` |
- Critical trace (package): `post__consents` · requirement family `FR-IAM-007` · acceptance: consent pending/declined/expired; learner remains limited
- **Functional requirements:** FR-IAM-006, FR-IAM-007, FR-PROF-005
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Learner (minor) — limited mode until consent verified.

## 10. Navigation destinations
- `UX-AUTH-005.dc.html`
- `UX-GLOB-001.dc.html`
- Shell navigation: auth layout

## 11. Responsive behavior
- Two-panel (brand night panel + form) ≥760; single column <760 with brand panel stacked above; form max 640.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ Legal verification method per country (O-04)
- ⚠️ Legal guardian-verification method per country (O-04).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-AUTH-002", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"auth-002.retry"} — Retry
- `action_clicked` {action_id:"auth-002.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `auth-002.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `auth-002.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `post__consents` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `get__me` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `auth-002.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `auth-002.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `auth-002.retry` Retry | action | REFETCH | `get__me` | high | Re-runs the failed request(s) |
| `auth-002.reconnect` Reconnect | action | REFETCH | `get__me` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
