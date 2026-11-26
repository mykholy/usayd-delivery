# UX-ADMIN-015 — Bookings Operations

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-ADMIN-015`
- **Name:** Bookings Operations
- **Role:** Platform admin (scoped) · inventory persona `ADMIN`
- **Module:** `BOOK` · phase `P0`
- **Route:** `/admin/bookings`
- **Design files:** `01_design/canvas/UX-ADMIN-015.dc.html` · `01_design/html/ar/UX-ADMIN-015.html` · `01_design/html/en/UX-ADMIN-015.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Booking operations: pending, conflicting, cancelled.
- AR: عمليات الحجز: المعلقة والمتعارضة والملغاة.
- Primary action (inventory): حل تعارض

## 3. UI components
- Status Chip
- Button
- Page header
- Status summary strip
- Exception lane (needs attention)
- Card
- Tabs
- Data table (sortable, cursor pager)
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: calendar; filters; conflict alerts

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Details | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Offer credit/refund | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Details | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Pick another time | navigates to `UX-GLOB-005.dc.html` | Navigate |
| Details | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Reassign | navigates to `UX-ADMIN-010.dc.html` | Navigate |
| Details | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Details | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Resolve DST | navigates to `UX-GLOB-005.dc.html` | Navigate |
| Shift planner | navigates to `UX-ADMIN-010.dc.html` | Navigate |
| Live lessons | navigates to `UX-ADMIN-016.dc.html` | Navigate |
| Regional schedules | navigates to `UX-GLOB-016.dc.html` | Navigate |
| Attendance & make-ups | navigates to `UX-ADMIN-018.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-ADMIN-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Follow module rules in `05_requirements/` and the FRs listed in §8.

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “This view is up to date” · AR «البيانات محدَّثة الآن» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `GET /api/v1/admin/bookings` | `UNRESOLVED — PROPOSED listAdminBookings (P-47); was get_bookings?admin=1 (C-06)` |
- **Functional requirements:** FR-BOOK-001, FR-BOOK-004, FR-BOOK-006, FR-TIME-006
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver.

## 10. Navigation destinations
- `UX-ADMIN-001.dc.html`
- `UX-ADMIN-010.dc.html`
- `UX-ADMIN-016.dc.html`
- `UX-ADMIN-018.dc.html`
- `UX-GLOB-005.dc.html`
- `UX-GLOB-016.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ Admin booking list should use a scoped admin operation (proposed `listAdminBookings`); `get_bookings` is the learner’s own list
- ⚠️ API: GET /api/v1/admin/bookings — UNRESOLVED — PROPOSED listAdminBookings (P-47); was get_bookings?admin=1 (C-06)

## 13. Analytics
- `screen_viewed` {screen_id:"UX-ADMIN-015", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"admin-015.details"} — Details
- `action_clicked` {action_id:"admin-015.offer-credit-refund"} — Offer credit/refund
- `action_clicked` {action_id:"admin-015.details"} — Details
- `action_clicked` {action_id:"admin-015.details"} — Details
- `action_clicked` {action_id:"admin-015.details"} — Details
- `action_clicked` {action_id:"admin-015.details"} — Details
- `action_clicked` {action_id:"admin-015.tabs"} — Tabs filter the list in place; selection is kept in the URL query
- `action_clicked` {action_id:"admin-015.sort-booking"} — Sort by Booking
- `action_clicked` {action_id:"admin-015.sort-learner"} — Sort by Learner
- `action_clicked` {action_id:"admin-015.sort-teacher"} — Sort by Teacher
- `action_clicked` {action_id:"admin-015.sort-time-utc"} — Sort by Time (UTC)
- `action_clicked` {action_id:"admin-015.sort-status"} — Sort by Status
- `action_clicked` {action_id:"admin-015.next-page"} — Next page
- `action_clicked` {action_id:"admin-015.previous-page"} — Previous page
- `action_clicked` {action_id:"admin-015.retry"} — Retry
- `action_clicked` {action_id:"admin-015.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `admin-015.details` | Details · التفاصيل | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-015.offer-credit-refund` | Offer credit/refund · عرض رصيد/استرداد | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-015.details` | Details · التفاصيل | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-015.details` | Details · التفاصيل | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-015.details` | Details · التفاصيل | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-015.details` | Details · التفاصيل | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-015.tabs` | Tabs filter the list in place; selection is kept in the URL query · تبويبات تصفّي القائمة في نفس الصفحة | tabs | Switches the list filter without leaving the page | list updates in place · URL query keeps selection |
| `admin-015.sort-booking` | Sort by Booking · ترتيب حسب الحجز | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-015.sort-learner` | Sort by Learner · ترتيب حسب المتعلم | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-015.sort-teacher` | Sort by Teacher · ترتيب حسب المعلم | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-015.sort-time-utc` | Sort by Time (UTC) · ترتيب حسب الموعد (UTC) | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-015.sort-status` | Sort by Status · ترتيب حسب الحالة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-015.next-page` | Next page · الصفحة التالية | pager | Requests the next page with the `next_cursor` returned by the list operation; no total count is shown | next cursor page loads · focus moves to first row · loading row while fetching · end of list disables Next |
| `admin-015.previous-page` | Previous page · الصفحة السابقة | disabled | Not actionable; the reason is shown next to it | none — shows the reason it is disabled |
| `admin-015.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-015.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- runtime data (sample in design): Name · اسم
- runtime data (sample in design): Name · اسم
- runtime data (sample in design): Name · اسم
- runtime data (sample in design): Name · اسم
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
- [ ] `GET /api/v1/admin/bookings` is behind a feature flag until its contract is approved (see `07_api/API_GAPS.md`)
- [ ] `admin-015.details` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-015.offer-credit-refund` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-015.details` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-015.details` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-015.details` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-015.details` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `admin-015.details` Details | action | UI_ONLY | — | high | Expands the row / opens the record drawer using the list payload |
| `admin-015.offer-credit-refund` Offer credit/refund | action | API_PROPOSED | `requestRefund` † | high | Bound by the 2026-11-23 contract audit |
| `admin-015.details` Details | action | UI_ONLY | — | high | Expands the row / opens the record drawer using the list payload |
| `admin-015.details` Details | action | UI_ONLY | — | high | Expands the row / opens the record drawer using the list payload |
| `admin-015.details` Details | action | UI_ONLY | — | high | Expands the row / opens the record drawer using the list payload |
| `admin-015.details` Details | action | UI_ONLY | — | high | Expands the row / opens the record drawer using the list payload |
| `admin-015.tabs` Tabs filter the list in place; selection is kept in the URL query | tabs | LIST_QUERY | `listAdminBookings` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-015.sort-booking` Sort by Booking | sort | LIST_QUERY | `listAdminBookings` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-015.sort-learner` Sort by Learner | sort | LIST_QUERY | `listAdminBookings` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-015.sort-teacher` Sort by Teacher | sort | LIST_QUERY | `listAdminBookings` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-015.sort-time-utc` Sort by Time (UTC) | sort | LIST_QUERY | `listAdminBookings` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-015.sort-status` Sort by Status | sort | LIST_QUERY | `listAdminBookings` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-015.next-page` Next page | pager | LIST_QUERY | `listAdminBookings` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-015.previous-page` Previous page | disabled | DISABLED | — | high | Not actionable; reason shown |
| `admin-015.retry` Retry | action | REFETCH | `listAdminBookings` † | high | Re-runs the failed request(s) |
| `admin-015.reconnect` Reconnect | action | REFETCH | `listAdminBookings` † | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
