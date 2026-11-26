# UX-AUTH-001 — Unified Signup

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-AUTH-001`
- **Name:** Unified Signup
- **Role:** Guest / onboarding user · inventory persona `AUTH`
- **Module:** `IAM` · phase `P0`
- **Route:** `/signup`
- **Design files:** `01_design/canvas/UX-AUTH-001.dc.html` · `01_design/html/ar/UX-AUTH-001.html` · `01_design/html/en/UX-AUTH-001.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Unified learner signup for all ages with minimal data.
- AR: تسجيل متعلم موحد لكل الأعمار بأقل بيانات.
- Primary action (inventory): إنشاء حساب

## 3. UI components
- Segmented control
- Form field
- Checkbox / consent
- Button
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: contact; name; age band; OTP; terms

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Create account | navigates to `UX-AUTH-002.dc.html` | Navigate |
| Log in | navigates to `UX-AUTH-003.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Choose another country | navigates to `UX-GLOB-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| Email | email | yes | required; RFC 5322 email; unique | — |
| Password | password | yes | required; ≥8 chars; ≥1 digit; not in breached list | — |
| Country | select | yes | required; ISO-3166; market must be active or waitlist | — |
| Age band | select | yes | required; drives consent gate | — |
| I agree to the Terms and Privacy Policy | checkbox | yes | must be checked | — |
| Send me optional learning reminders | checkbox | no | optional | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Email or phone (E.164) with OTP verification
- Country is a user choice; IP only suggests
- Age band only — no full birthdate unless market law requires
- Under 18 → UX-AUTH-002 before any payment or lesson
- Rate-limit OTP: 5/hour

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `CONTACT_ALREADY_REGISTERED`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Verification code sent” · AR «أرسلنا رمز التحقق» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/auth/register` | `post__auth_register` |
| `POST /api/v1/learners` | `post__learners` |
- Critical trace (package): `post__auth_register` · requirement family `FR-IAM-001` · acceptance: register → verified contact / invalid OTP / rate-limit
- **Functional requirements:** FR-IAM-001, FR-IAM-002, FR-IAM-007, FR-GEO-001
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Guest.

## 10. Navigation destinations
- `UX-AUTH-002.dc.html`
- `UX-AUTH-003.dc.html`
- `UX-GLOB-001.dc.html`
- Shell navigation: auth layout

## 11. Responsive behavior
- Two-panel (brand night panel + form) ≥760; single column <760 with brand panel stacked above; form max 640.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-AUTH-001", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"auth-001.show-password"} — Show / hide password
- `action_clicked` {action_id:"auth-001.retry"} — Retry
- `action_clicked` {action_id:"auth-001.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `auth-001.show-password` | Show / hide password · إظهار / إخفاء كلمة المرور | action | **PROPOSED:** calls `post__auth_register` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `auth-001.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `auth-001.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `post__auth_register` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__learners` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `auth-001.show-password` follows its contract in §14 and is idempotent on double tap
- [ ] `auth-001.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `auth-001.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `auth-001.show-password` Show / hide password | action | UI_ONLY | — | high | Toggles password visibility locally; announces state |
| `auth-001.retry` Retry | action | REFETCH | — | high | Re-runs the failed request(s) |
| `auth-001.reconnect` Reconnect | action | REFETCH | — | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
