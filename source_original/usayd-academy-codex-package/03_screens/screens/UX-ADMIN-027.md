# UX-ADMIN-027 — Competitions List

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-ADMIN-027`
- **Name:** Competitions List
- **Role:** Platform admin (scoped) · inventory persona `ADMIN`
- **Module:** `CONTEST` · phase `P0`
- **Route:** `/admin/competitions`
- **Design files:** `01_design/canvas/UX-ADMIN-027.dc.html` · `01_design/html/ar/UX-ADMIN-027.html` · `01_design/html/en/UX-ADMIN-027.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Competitions list and states.
- AR: قائمة المسابقات وحالاتها.
- Primary action (inventory): فتح مسابقة

## 3. UI components
- Status Chip
- Button
- Page header
- Status summary strip
- Exception lane (needs attention)
- Card
- Filter bar
- Data table (sortable, cursor pager)
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: state; registrations; compliance status

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Control room | navigates to `UX-ADMIN-028.dc.html` | Navigate |
| Edit | navigates to `UX-ADMIN-026.dc.html` | Navigate |
| Control room | navigates to `UX-ADMIN-028.dc.html` | Navigate |
| Edit | navigates to `UX-ADMIN-026.dc.html` | Navigate |
| Appeals | navigates to `UX-ADMIN-031.dc.html` | Navigate |
| Results | navigates to `UX-ADMIN-030.dc.html` | Navigate |
| New competition | navigates to `UX-ADMIN-026.dc.html` | Navigate |
| Templates | navigates to `UX-ADMIN-025.dc.html` | Navigate |
| Judges | navigates to `UX-ADMIN-029.dc.html` | Navigate |
| Appeals | navigates to `UX-ADMIN-031.dc.html` | Navigate |
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
| `GET /api/v1/admin/competitions` | `UNRESOLVED — PROPOSED listAdminCompetitions (P-14); was get__competitions?admin=1 (C-07)` |
- **Functional requirements:** FR-CONTEST-001, FR-ADMIN-003
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver.

## 10. Navigation destinations
- `UX-ADMIN-001.dc.html`
- `UX-ADMIN-025.dc.html`
- `UX-ADMIN-026.dc.html`
- `UX-ADMIN-028.dc.html`
- `UX-ADMIN-029.dc.html`
- `UX-ADMIN-030.dc.html`
- `UX-ADMIN-031.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ Admin competition list should use a dedicated admin operation (proposed `listAdminCompetitions`) so drafts are never visible to learners
- ⚠️ API: GET /api/v1/admin/competitions — UNRESOLVED — PROPOSED listAdminCompetitions (P-14); was get__competitions?admin=1 (C-07)

## 13. Analytics
- `screen_viewed` {screen_id:"UX-ADMIN-027", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"admin-027.state"} — State
- `action_clicked` {action_id:"admin-027.market"} — Market
- `action_clicked` {action_id:"admin-027.age-band"} — Age band
- `action_clicked` {action_id:"admin-027.sort-competition"} — Sort by Competition
- `action_clicked` {action_id:"admin-027.sort-state"} — Sort by State
- `action_clicked` {action_id:"admin-027.sort-participants"} — Sort by Participants
- `action_clicked` {action_id:"admin-027.sort-pending-judging"} — Sort by Pending judging
- `action_clicked` {action_id:"admin-027.sort-next-deadline-utc"} — Sort by Next deadline (UTC)
- `action_clicked` {action_id:"admin-027.next-page"} — Next page
- `action_clicked` {action_id:"admin-027.previous-page"} — Previous page
- `action_clicked` {action_id:"admin-027.retry"} — Retry
- `action_clicked` {action_id:"admin-027.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `admin-027.state` | State · الحالة | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `admin-027.market` | Market · السوق | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `admin-027.age-band` | Age band · الفئة العمرية | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `admin-027.sort-competition` | Sort by Competition · ترتيب حسب المسابقة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-027.sort-state` | Sort by State · ترتيب حسب الحالة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-027.sort-participants` | Sort by Participants · ترتيب حسب المشاركون | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-027.sort-pending-judging` | Sort by Pending judging · ترتيب حسب بانتظار التحكيم | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-027.sort-next-deadline-utc` | Sort by Next deadline (UTC) · ترتيب حسب الموعد التالي (UTC) | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-027.next-page` | Next page · الصفحة التالية | pager | Requests the next page with the `next_cursor` returned by the list operation; no total count is shown | next cursor page loads · focus moves to first row · loading row while fetching · end of list disables Next |
| `admin-027.previous-page` | Previous page · الصفحة السابقة | disabled | Not actionable; the reason is shown next to it | none — shows the reason it is disabled |
| `admin-027.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-027.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- runtime data (sample in design): — · —
- runtime data (sample in design): — · —
- runtime data (sample in design): — · —
- runtime data (sample in design): — · —
- runtime data (sample in design): — · —
- runtime data (sample in design): — · —
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
- [ ] `GET /api/v1/admin/competitions` is behind a feature flag until its contract is approved (see `07_api/API_GAPS.md`)

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `admin-027.state` State | filter | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.market` Market | filter | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.age-band` Age band | filter | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.sort-competition` Sort by Competition | sort | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.sort-state` Sort by State | sort | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.sort-participants` Sort by Participants | sort | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.sort-pending-judging` Sort by Pending judging | sort | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.sort-next-deadline-utc` Sort by Next deadline (UTC) | sort | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.next-page` Next page | pager | LIST_QUERY | `listAdminCompetitions` † | high | Re-queries the screen’s list operation with the parameter |
| `admin-027.previous-page` Previous page | disabled | DISABLED | — | high | Not actionable; reason shown |
| `admin-027.retry` Retry | action | REFETCH | `listAdminCompetitions` † | high | Re-runs the failed request(s) |
| `admin-027.reconnect` Reconnect | action | REFETCH | `listAdminCompetitions` † | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
