# UX-SUP-009 — Audit and Break-glass Review

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-SUP-009`
- **Name:** Audit and Break-glass Review
- **Role:** Platform admin (scoped) · inventory persona `ADMIN`
- **Module:** `SUP` · phase `P0`
- **Route:** `/admin/security/access-audits`
- **Design files:** `01_design/canvas/UX-SUP-009.dc.html` · `01_design/html/ar/UX-SUP-009.html` · `01_design/html/en/UX-SUP-009.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Review privileged and break-glass access.
- AR: مراجعة الوصول المميز والطارئ.
- Primary action (inventory): Review incident

## 3. UI components
- Status Chip
- Page header
- Status summary strip
- Exception lane (needs attention)
- Card
- Filter bar
- Data table (sortable, cursor pager)
- Unresolved-requirement note
- Button
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: redacted timeline; purpose; actor; alerts; revocation

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Record review outcome | disabled (shows reason) | Call the API in §8 / update local state; show success/error states |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-ADMIN-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Read-only, append-only trail; reviewers can’t review their own access
- Child data in objects is redacted to IDs

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
| `GET /api/v1/admin/security/access-audits` | `get__api_v1_admin_security_access_audits` |
- v1.2 trace: `GET /api/v1/admin/security/access-audits` · SPECIFIED; implementation pending
- **Functional requirements:** FR-SUP-009, FR-SEC-004
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Platform admin; every list/action filtered by RBAC + ABAC scope (market/program); sensitive actions need reason + audit, some need a second approver.

## 10. Navigation destinations
- `UX-ADMIN-001.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ Recording a review outcome needs an API operation that doesn’t exist (proposed: postAccessAuditReview)

## 13. Analytics
- `screen_viewed` {screen_id:"UX-SUP-009", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"sup-009.type"} — Type
- `action_clicked` {action_id:"sup-009.staff"} — Staff
- `action_clicked` {action_id:"sup-009.review-state"} — Review state
- `action_clicked` {action_id:"sup-009.sort-time-utc"} — Sort by Time (UTC)
- `action_clicked` {action_id:"sup-009.sort-staff"} — Sort by Staff
- `action_clicked` {action_id:"sup-009.sort-type"} — Sort by Type
- `action_clicked` {action_id:"sup-009.sort-object"} — Sort by Object
- `action_clicked` {action_id:"sup-009.sort-reason"} — Sort by Reason
- `action_clicked` {action_id:"sup-009.sort-review"} — Sort by Review
- `action_clicked` {action_id:"sup-009.next-page"} — Next page
- `action_clicked` {action_id:"sup-009.previous-page"} — Previous page
- `action_clicked` {action_id:"sup-009.record-review-outcome"} — Record review outcome
- `action_clicked` {action_id:"sup-009.retry"} — Retry
- `action_clicked` {action_id:"sup-009.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `sup-009.type` | Type · النوع | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `sup-009.staff` | Staff · الموظف | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `sup-009.review-state` | Review state · حالة المراجعة | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `sup-009.sort-time-utc` | Sort by Time (UTC) · ترتيب حسب الوقت (UTC) | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-009.sort-staff` | Sort by Staff · ترتيب حسب الموظف | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-009.sort-type` | Sort by Type · ترتيب حسب النوع | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-009.sort-object` | Sort by Object · ترتيب حسب الكائن | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-009.sort-reason` | Sort by Reason · ترتيب حسب السبب | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-009.sort-review` | Sort by Review · ترتيب حسب المراجعة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-009.next-page` | Next page · الصفحة التالية | pager | Requests the next page with the `next_cursor` returned by the list operation; no total count is shown | next cursor page loads · focus moves to first row · loading row while fetching · end of list disables Next |
| `sup-009.previous-page` | Previous page · الصفحة السابقة | disabled | Not actionable; the reason is shown next to it | none — shows the reason it is disabled |
| `sup-009.record-review-outcome` | Record review outcome · سجّل نتيجة المراجعة | disabled | Not actionable; the reason is shown next to it | none — shows the reason it is disabled |
| `sup-009.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-009.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- runtime data (sample in design): Admin · مدير
- runtime data (sample in design): Finance · مالية
- runtime data (sample in design): Support · دعم
- runtime data (sample in design): Admin · مدير
- runtime data (sample in design): Safeguarding · حماية
- runtime data (sample in design): Admin · مدير
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
- [ ] `get__api_v1_admin_security_access_audits` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions

## 18. Implementation
- Shares the audit-trail component with `UX-ADMIN-040`.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `sup-009.type` Type | filter | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.staff` Staff | filter | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.review-state` Review state | filter | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.sort-time-utc` Sort by Time (UTC) | sort | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.sort-staff` Sort by Staff | sort | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.sort-type` Sort by Type | sort | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.sort-object` Sort by Object | sort | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.sort-reason` Sort by Reason | sort | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.sort-review` Sort by Review | sort | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.next-page` Next page | pager | LIST_QUERY | `get__api_v1_admin_security_access_audits` | high | Re-queries the screen’s list operation with the parameter |
| `sup-009.previous-page` Previous page | disabled | DISABLED | — | high | Not actionable; reason shown |
| `sup-009.record-review-outcome` Record review outcome | disabled | DISABLED | — | high | Not actionable; reason shown |
| `sup-009.retry` Retry | action | REFETCH | `get__api_v1_admin_security_access_audits` | high | Re-runs the failed request(s) |
| `sup-009.reconnect` Reconnect | action | REFETCH | `get__api_v1_admin_security_access_audits` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
