# UX-MOBILE-001 — Flutter Login

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-MOBILE-001`
- **Name:** Flutter Login
- **Role:** Learner (Flutter) · inventory persona `MOBILE`
- **Module:** `MOB` · phase `P2`
- **Route:** `mobile://auth`
- **Design files:** `01_design/canvas/UX-MOBILE-001.dc.html` · `01_design/html/ar/UX-MOBILE-001.html` · `01_design/html/en/UX-MOBILE-001.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Flutter sign-in/sign-up.
- AR: دخول وتسجيل في تطبيق Flutter.
- Primary action (inventory): دخول

## 3. UI components
- Mobile hero (night)
- Status Chip
- Form field
- Checkbox / consent
- Button
- Mobile / Night header + sheet
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: auth; OTP; biometric optional

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Forgot password? | navigates to `UX-AUTH-004.dc.html` | Navigate |
| Sign in | navigates to `UX-MOBILE-002.dc.html` | Navigate |
| Phone code | navigates to `UX-AUTH-001.dc.html` | Navigate |
| Biometrics | navigates to `UX-MOBILE-002.dc.html` | Navigate |
| Create a learner account | navigates to `UX-AUTH-001.dc.html` | Navigate |
| Teacher sign-in | navigates to `UX-MOBILE-009.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-MOBILE-002.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| Email or phone | email | yes | required | — |
| Password | password | yes | required | — |
| Remember me | checkbox | no | optional | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Biometric sign-in is offered only after a successful password sign-in on this device and only if the device supports it (inventory: biometric optional)
- Phone sign-in uses a one-time code (same flow as UX-AUTH-001 phone option)
- Five failed attempts → cooldown with the 429 copy; never reveal whether the email exists

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `INVALID_CREDENTIALS`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Your changes were saved” · AR «تم حفظ التغييرات» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/auth/login` | `post__auth_login` |
| `POST /api/v1/auth/register` | `post__auth_register` |
- **Functional requirements:** FR-MOB-001, FR-IAM-003
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1.

## 10. Navigation destinations
- `UX-AUTH-001.dc.html`
- `UX-AUTH-004.dc.html`
- `UX-MOBILE-002.dc.html`
- `UX-MOBILE-009.dc.html`
- Shell navigation: bottom tab bar

## 11. Responsive behavior
- Flutter phone 360–428 portrait; tablet uses two-pane where noted; respects safe areas and dynamic type.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-MOBILE-001", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"mobile-001.show-password"} — Show / hide password
- `action_clicked` {action_id:"mobile-001.retry"} — Retry
- `action_clicked` {action_id:"mobile-001.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `mobile-001.show-password` | Show / hide password · إظهار / إخفاء كلمة المرور | action | **PROPOSED:** calls `post__auth_login` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `mobile-001.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `mobile-001.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- None.

## 16. Themes & breakpoints
- Light and dark use the same markup; colours only from tokens (`02_design_system/tokens.color.v0.4.json`). Night surfaces stay night in both themes.
- 360/390: Flutter phone layout, safe areas, bottom tabs · 768: two columns where space allows, sidebar collapses to the top bar · 1024: sidebar visible, splits stack below 1100 · 1440: design reference width.

## 17. Acceptance criteria
- [ ] Renders in Arabic (RTL) and English (LTR), light and dark, at 360, 390, 768, 1024 and 1440 px without horizontal page scroll
- [ ] All seven states (default, loading, empty, error, no-permission, offline, success) are reachable and use the copy in §7
- [ ] Every interactive target is at least 44×44 px; every control has an accessible name; focus order follows reading order
- [ ] Text contrast ≥ 4.5:1 and non-text ≥ 3:1 in both themes (axe: 0 serious/critical violations)
- [ ] One H1; heading levels never skip
- [ ] `post__auth_login` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__auth_register` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `mobile-001.show-password` follows its contract in §14 and is idempotent on double tap
- [ ] `mobile-001.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `mobile-001.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `mobile-001.show-password` Show / hide password | action | UI_ONLY | — | high | Toggles password visibility locally; announces state |
| `mobile-001.retry` Retry | action | REFETCH | — | high | Re-runs the failed request(s) |
| `mobile-001.reconnect` Reconnect | action | REFETCH | — | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
