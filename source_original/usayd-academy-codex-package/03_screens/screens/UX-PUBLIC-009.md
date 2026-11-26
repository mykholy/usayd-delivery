# UX-PUBLIC-009 — Free Assessment Booking

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-PUBLIC-009`
- **Name:** Free Assessment Booking
- **Role:** Guest (public) · inventory persona `PUBLIC`
- **Module:** `BOOK` · phase `P0`
- **Route:** `/trial`
- **Design files:** `01_design/canvas/UX-PUBLIC-009.dc.html` · `01_design/html/ar/UX-PUBLIC-009.html` · `01_design/html/en/UX-PUBLIC-009.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Book a level assessment in the visitor’s timezone with minimal data.
- AR: حجز تقييم مستوى بتوقيت الزائر وبيانات أقل.
- Primary action (inventory): احجز الموعد

## 3. UI components
- Button
- Page header
- Stepper
- Timezone chip
- Segmented control
- Card
- Form field
- Checkbox / consent
- Slide to confirm
- Page hero (illustrated)
- Shell / Public header
- Loading skeleton
- Alert / Inline
- State panel
- Shell / Public footer
- Inventory anatomy: contact; timezone; available slots; consent

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Next week | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Slide to confirm booking | navigates to `UX-AUTH-005.dc.html` | Navigate |
| Log in | navigates to `UX-AUTH-003.dc.html` | Navigate |
| Book a level assessment | navigates to `UX-PUBLIC-009.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Choose another country | navigates to `UX-GLOB-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| First name | text | yes | required, 2–50 chars | — |
| Email or phone | email | yes | required; valid email or E.164 phone | — |
| Age band | select | yes | required; <18 triggers guardian gate | — |
| Goal | select | yes | required | — |
| I agree to the Terms and Privacy Policy | checkbox | yes | must be checked | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Slot held 5 min (TTL) after selection; expiry releases slot
- Times displayed in visitor timezone with IANA label + UTC offset; stored as UTC
- Age band < 18 → guardian consent gate (UX-AUTH-002) before confirmation

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “No slots available this week” · AR «لا توجد مواعيد متاحة هذا الأسبوع» — with primary CTA
- **Error:** “We couldn’t load this” + retry; show error code `SLOT_TAKEN`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Assessment booked” · AR «تم حجز تقييم المستوى» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `GET /api/v1/booking/available-slots?type=assessment` | `get__api_v1_booking_available_slots` |
| `POST /api/v1/auth/register` | `post__auth_register` |
| `POST /api/v1/bookings` | `post_bookings` |
- **Functional requirements:** FR-BOOK-002, FR-TIME-001, FR-TIME-003, FR-IAM-001
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Guest → creates learner account at confirm; minors routed to guardian consent before booking is confirmed.

## 10. Navigation destinations
- `UX-AUTH-003.dc.html`
- `UX-AUTH-005.dc.html`
- `UX-GLOB-001.dc.html`
- `UX-PUBLIC-009.dc.html`
- Shell navigation: public header/footer

## 11. Responsive behavior
- Fluid page: max content 1280; ≥1100 multi-column; 760–1100 grids collapse to 2 columns; <760 single column, header nav hides (burger), CTAs stay visible; touch targets ≥44px.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-PUBLIC-009", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"public-009.next-week"} — Next week
- `action_clicked` {action_id:"public-009.slide-to-confirm-booking"} — Slide to confirm booking
- `action_clicked` {action_id:"public-009.retry"} — Retry
- `action_clicked` {action_id:"public-009.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `public-009.next-week` | Next week · الأسبوع التالي | action | **PROPOSED:** calls `post__auth_register` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `public-009.slide-to-confirm-booking` | Slide to confirm booking · اسحب لتأكيد الحجز | slide | Slide-to-confirm (see COMPONENTS.md › Slide to confirm). Then navigates to `UX-AUTH-005` | armed (first tap/Enter) · confirmed (drag past 90% or second tap/Enter within 5 s) · cancelled (release before 90%, pointer cancel, Esc, or 5 s timeout) · then the action’s own success/error states |
| `public-009.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `public-009.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `get__api_v1_booking_available_slots` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__auth_register` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post_bookings` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `public-009.next-week` follows its contract in §14 and is idempotent on double tap
- [ ] `public-009.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `public-009.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `public-009.next-week` Next week | action | LIST_QUERY | `get__api_v1_booking_available_slots` | high | Re-queries slots for the next week |
| `public-009.slide-to-confirm-booking` Slide to confirm booking | slide | NAVIGATE_AFTER_CONFIRM | — | high | Confirm, then navigate to UX-AUTH-005; the destination performs the write |
| `public-009.retry` Retry | action | REFETCH | `get__api_v1_booking_available_slots` | high | Re-runs the failed request(s) |
| `public-009.reconnect` Reconnect | action | REFETCH | `get__api_v1_booking_available_slots` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
