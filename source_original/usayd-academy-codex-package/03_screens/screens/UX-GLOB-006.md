# UX-GLOB-006 — Regional Checkout Quote

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-GLOB-006`
- **Name:** Regional Checkout Quote
- **Role:** Learner · inventory persona `STUDENT`
- **Module:** `PAY` · phase `P0`
- **Route:** `/checkout/:quoteId`
- **Design files:** `01_design/canvas/UX-GLOB-006.dc.html` · `01_design/html/ar/UX-GLOB-006.html` · `01_design/html/en/UX-GLOB-006.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Understand merchant, currency, tax and quote expiry, then pay.
- AR: فهم التاجر والعملة والضريبة وانتهاء عرض السعر ثم الدفع.
- Primary action (inventory): Pay securely

## 3. UI components
- Page header
- Stepper
- Radio cards
- Form field
- Slide to confirm
- Card
- Amount display
- Key-value list
- Status Chip
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Button
- Alert / Inline
- State panel
- Inventory anatomy: quote breakdown; locale switch; billing country; PSP methods; data/privacy notice

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Slide to pay securely | navigates to `UX-LEARNER-029.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-LEARNER-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| pm | radio | yes | one option required | — |
| Billing country | select | yes | must match market eligibility | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Quote immutable with ID + expiry; language switch never changes amount or quote ID
- Idempotency key per checkout
- Billing country must match market rules

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `QUOTE_EXPIRED`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Verifying payment — we’ll confirm once notified” · AR «جاري التحقق من الدفع — سنؤكد فور وصول الإشعار» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/me/checkout-quotes` | `post__api_v1_me_checkout_quotes` |
| `POST /api/v1/me/payment-checkouts` | `post__api_v1_me_payment_checkouts` |
| `GET /api/v1/payments/{id}` | `get__payments__paymentId` |
- v1.2 trace: `POST /api/v1/me/payment-checkouts` · SPECIFIED; implementation pending
- **Functional requirements:** FR-PAY-003, FR-PAY-004, FR-GEO-006, FR-GEO-007, FR-GEO-014, FR-I18N-007
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation.

## 10. Navigation destinations
- `UX-LEARNER-001.dc.html`
- `UX-LEARNER-029.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-GLOB-006", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"glob-006.slide-to-pay-securely"} — Slide to pay securely
- `action_clicked` {action_id:"glob-006.retry"} — Retry
- `action_clicked` {action_id:"glob-006.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `glob-006.slide-to-pay-securely` | Slide to pay securely · اسحب للدفع بأمان | slide | Slide-to-confirm (see COMPONENTS.md › Slide to confirm). Then navigates to `UX-LEARNER-029` | armed (first tap/Enter) · confirmed (drag past 90% or second tap/Enter within 5 s) · cancelled (release before 90%, pointer cancel, Esc, or 5 s timeout) · then the action’s own success/error states |
| `glob-006.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `glob-006.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- **CONTENT_REQUIRED (owner)**: PRICE · السعر
- runtime data (sample in design): — · —
- runtime data (sample in design): — · —
- runtime data (sample in design): — · —
- **CONTENT_REQUIRED (owner)**: Approved entity · الكيان المعتمد
- runtime data (sample in design): User name · اسم المستخدم

## 16. Themes & breakpoints
- Light and dark use the same markup; colours only from tokens (`02_design_system/tokens.color.v0.4.json`). Night surfaces stay night in both themes.
- 360/390: single column, sticky primary CTA, tables become stacked records, calendar becomes an agenda list · 768: two columns where space allows, sidebar collapses to the top bar · 1024: sidebar visible, splits stack below 1100 · 1440: design reference width.

## 17. Acceptance criteria
- [ ] Renders in Arabic (RTL) and English (LTR), light and dark, at 360, 390, 768, 1024 and 1440 px without horizontal page scroll
- [ ] All seven states (default, loading, empty, error, no-permission, offline, success) are reachable and use the copy in §7
- [ ] Every interactive target is at least 44×44 px; every control has an accessible name; focus order follows reading order
- [ ] Text contrast ≥ 4.5:1 and non-text ≥ 3:1 in both themes (axe: 0 serious/critical violations)
- [ ] One H1; heading levels never skip
- [ ] `post__api_v1_me_checkout_quotes` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__api_v1_me_payment_checkouts` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `get__payments__paymentId` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `glob-006.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `glob-006.reconnect` follows its contract in §14 and is idempotent on double tap
- [ ] No owner-content slot ships with placeholder text: the block is hidden until approved content exists

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `glob-006.slide-to-pay-securely` Slide to pay securely | slide | NAVIGATE_AFTER_CONFIRM | — | high | Confirm, then navigate to UX-LEARNER-029; the destination performs the write |
| `glob-006.retry` Retry | action | REFETCH | `get__payments__paymentId` | high | Re-runs the failed request(s) |
| `glob-006.reconnect` Reconnect | action | REFETCH | `get__payments__paymentId` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
