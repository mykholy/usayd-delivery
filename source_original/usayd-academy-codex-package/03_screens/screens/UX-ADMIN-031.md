# UX-ADMIN-031 — Contest Appeals

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-ADMIN-031`
- **Name:** Contest Appeals
- **Role:** Platform admin (scoped) · inventory persona `ADMIN`
- **Module:** `CONTEST` · phase `P0`
- **Route:** `/admin/contest-appeals`
- **Design files:** `01_design/canvas/UX-ADMIN-031.dc.html` · `01_design/html/ar/UX-ADMIN-031.html` · `01_design/html/en/UX-ADMIN-031.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Contest appeals and independent resolution.
- AR: قائمة التظلمات وحلها المستقل.
- Primary action (inventory): حسم الاستئناف

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
- Inventory anatomy: score history; reason; reviewer

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Open | navigates to `UX-TEACHER-015.dc.html` | Navigate |
| Assign reviewer | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Assign reviewer | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Open | navigates to `UX-TEACHER-015.dc.html` | Navigate |
| Assign reviewer | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Open | navigates to `UX-TEACHER-015.dc.html` | Navigate |
| Open | navigates to `UX-TEACHER-015.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-ADMIN-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- The reviewer must not be the original judge (independence check server-side)
- Results stay provisional until every appeal in the window is resolved

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
| `GET /api/v1/admin/contest-appeals` | `getAdminContestAppeals` |
| `POST /api/v1/admin/contest-appeals/{id}/resolve` | `postAdminContestAppealResolve` |
- Critical trace (package): `postAdminContestAppealResolve` · requirement family `FR-CONTEST-001` · acceptance: independent appeal adjudication
- **Functional requirements:** FR-CONTEST-011, FR-SUP-005
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver.

## 10. Navigation destinations
- `UX-ADMIN-001.dc.html`
- `UX-TEACHER-015.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-ADMIN-031", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"admin-031.assign-reviewer"} — Assign reviewer
- `action_clicked` {action_id:"admin-031.assign-reviewer"} — Assign reviewer
- `action_clicked` {action_id:"admin-031.assign-reviewer"} — Assign reviewer
- `action_clicked` {action_id:"admin-031.tabs"} — Tabs filter the list in place; selection is kept in the URL query
- `action_clicked` {action_id:"admin-031.sort-appeal"} — Sort by Appeal
- `action_clicked` {action_id:"admin-031.sort-contest"} — Sort by Contest
- `action_clicked` {action_id:"admin-031.sort-criterion"} — Sort by Criterion
- `action_clicked` {action_id:"admin-031.sort-reviewer"} — Sort by Reviewer
- `action_clicked` {action_id:"admin-031.sort-sla"} — Sort by SLA
- `action_clicked` {action_id:"admin-031.next-page"} — Next page
- `action_clicked` {action_id:"admin-031.previous-page"} — Previous page
- `action_clicked` {action_id:"admin-031.retry"} — Retry
- `action_clicked` {action_id:"admin-031.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `admin-031.assign-reviewer` | Assign reviewer · أسند مراجعًا | action | **PROPOSED:** calls `postAdminContestAppealResolve` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-031.assign-reviewer` | Assign reviewer · أسند مراجعًا | action | **PROPOSED:** calls `postAdminContestAppealResolve` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-031.assign-reviewer` | Assign reviewer · أسند مراجعًا | action | **PROPOSED:** calls `postAdminContestAppealResolve` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-031.tabs` | Tabs filter the list in place; selection is kept in the URL query · تبويبات تصفّي القائمة في نفس الصفحة | tabs | Switches the list filter without leaving the page | list updates in place · URL query keeps selection |
| `admin-031.sort-appeal` | Sort by Appeal · ترتيب حسب التظلم | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-031.sort-contest` | Sort by Contest · ترتيب حسب المسابقة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-031.sort-criterion` | Sort by Criterion · ترتيب حسب المعيار | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-031.sort-reviewer` | Sort by Reviewer · ترتيب حسب المراجع | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-031.sort-sla` | Sort by SLA · ترتيب حسب المهلة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `admin-031.next-page` | Next page · الصفحة التالية | pager | Requests the next page with the `next_cursor` returned by the list operation; no total count is shown | next cursor page loads · focus moves to first row · loading row while fetching · end of list disables Next |
| `admin-031.previous-page` | Previous page · الصفحة السابقة | disabled | Not actionable; the reason is shown next to it | none — shows the reason it is disabled |
| `admin-031.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-031.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- runtime data (sample in design): 3 · ٣
- runtime data (sample in design): 5 · ٥
- runtime data (sample in design): 2 · ٢
- runtime data (sample in design): 7 · ٧
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
- [ ] `getAdminContestAppeals` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `postAdminContestAppealResolve` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `admin-031.assign-reviewer` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-031.assign-reviewer` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-031.assign-reviewer` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `admin-031.assign-reviewer` Assign reviewer | action | API_EXISTING | `postAdminContestAppealResolve` | medium | Only write operation on the screen |
| `admin-031.assign-reviewer` Assign reviewer | action | API_EXISTING | `postAdminContestAppealResolve` | medium | Only write operation on the screen |
| `admin-031.assign-reviewer` Assign reviewer | action | API_EXISTING | `postAdminContestAppealResolve` | medium | Only write operation on the screen |
| `admin-031.tabs` Tabs filter the list in place; selection is kept in the URL query | tabs | LIST_QUERY | `getAdminContestAppeals` | high | Re-queries the screen’s list operation with the parameter |
| `admin-031.sort-appeal` Sort by Appeal | sort | LIST_QUERY | `getAdminContestAppeals` | high | Re-queries the screen’s list operation with the parameter |
| `admin-031.sort-contest` Sort by Contest | sort | LIST_QUERY | `getAdminContestAppeals` | high | Re-queries the screen’s list operation with the parameter |
| `admin-031.sort-criterion` Sort by Criterion | sort | LIST_QUERY | `getAdminContestAppeals` | high | Re-queries the screen’s list operation with the parameter |
| `admin-031.sort-reviewer` Sort by Reviewer | sort | LIST_QUERY | `getAdminContestAppeals` | high | Re-queries the screen’s list operation with the parameter |
| `admin-031.sort-sla` Sort by SLA | sort | LIST_QUERY | `getAdminContestAppeals` | high | Re-queries the screen’s list operation with the parameter |
| `admin-031.next-page` Next page | pager | LIST_QUERY | `getAdminContestAppeals` | high | Re-queries the screen’s list operation with the parameter |
| `admin-031.previous-page` Previous page | disabled | DISABLED | — | high | Not actionable; reason shown |
| `admin-031.retry` Retry | action | REFETCH | `getAdminContestAppeals` | high | Re-runs the failed request(s) |
| `admin-031.reconnect` Reconnect | action | REFETCH | `getAdminContestAppeals` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
