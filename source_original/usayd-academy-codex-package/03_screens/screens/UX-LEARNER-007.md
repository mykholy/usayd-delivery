# UX-LEARNER-007 — Calendar

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-LEARNER-007`
- **Name:** Calendar
- **Role:** Learner · inventory persona `LEARNER`
- **Module:** `BOOK` · phase `P0`
- **Route:** `/app/calendar`
- **Design files:** `01_design/canvas/UX-LEARNER-007.dc.html` · `01_design/html/ar/UX-LEARNER-007.html` · `01_design/html/en/UX-LEARNER-007.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Calendar of upcoming and past lessons in my time.
- AR: تقويم الحصص القادمة والسابقة بتوقيتي.
- Primary action (inventory): حجز أو تغيير

## 3. UI components
- Button
- Page header
- Segmented control
- Week calendar
- Agenda list (mobile calendar)
- List row
- Card
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: day/week; timezone label; upcoming

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Book a lesson | navigates to `UX-LEARNER-008.dc.html` | Navigate |
| Book a lesson | navigates to `UX-LEARNER-008.dc.html` | Navigate |
| Export ICS | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Previous | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Next | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Details | navigates to `UX-LEARNER-009.dc.html` | Navigate |
| Details | navigates to `UX-LEARNER-009.dc.html` | Navigate |
| Teachers | navigates to `UX-LEARNER-005.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-LEARNER-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Follow module rules in `05_requirements/` and the FRs listed in §8.

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “No lessons in this range” · AR «لا حصص في هذه الفترة» — with primary CTA
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “This view is up to date” · AR «البيانات محدَّثة الآن» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `GET /api/v1/bookings?from=&to=` | `get_bookings` |
- **Functional requirements:** FR-BOOK-001, FR-TIME-007, FR-TIME-009
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation.

## 10. Navigation destinations
- `UX-LEARNER-001.dc.html`
- `UX-LEARNER-005.dc.html`
- `UX-LEARNER-008.dc.html`
- `UX-LEARNER-009.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-LEARNER-007", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"learner-007.export-ics"} — Export ICS
- `action_clicked` {action_id:"learner-007.previous"} — Previous
- `action_clicked` {action_id:"learner-007.next"} — Next
- `action_clicked` {action_id:"learner-007.retry"} — Retry
- `action_clicked` {action_id:"learner-007.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `learner-007.export-ics` | Export ICS · تصدير ICS | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `learner-007.previous` | Previous · السابق | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `learner-007.next` | Next · التالي | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `learner-007.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `learner-007.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- runtime data (sample in design): Name · اسم
- runtime data (sample in design): Name · اسم
- runtime data (sample in design): Name · اسم
- runtime data (sample in design): Name · اسم
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
- [ ] `get_bookings` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `learner-007.export-ics` follows its contract in §14 and is idempotent on double tap
- [ ] `learner-007.previous` follows its contract in §14 and is idempotent on double tap
- [ ] `learner-007.next` follows its contract in §14 and is idempotent on double tap
- [ ] `learner-007.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `learner-007.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `learner-007.export-ics` Export ICS | action | UI_ONLY | — | high | Generates an .ics file client-side from lessons already loaded (UTC + TZID) |
| `learner-007.previous` Previous | action | UI_ONLY | — | high | Re-queries the visible range (GET with date/cursor param) |
| `learner-007.next` Next | action | UI_ONLY | — | high | Re-queries the visible range (GET with date/cursor param) |
| `learner-007.retry` Retry | action | REFETCH | `get_bookings` | high | Re-runs the failed request(s) |
| `learner-007.reconnect` Reconnect | action | REFETCH | `get_bookings` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
