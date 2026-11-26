# UX-SUP-010 — Settings Registry

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-SUP-010`
- **Name:** Settings Registry
- **Role:** Platform admin (scoped) · inventory persona `ADMIN`
- **Module:** `SUP` · phase `P0`
- **Route:** `/admin/settings`
- **Design files:** `01_design/canvas/UX-SUP-010.dc.html` · `01_design/html/ar/UX-SUP-010.html` · `01_design/html/en/UX-SUP-010.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Versioned settings registry with inheritance and approval (canonical /admin/settings).
- AR: سجل الإعدادات المُصدَر بالوراثة والاعتماد (المسار الكانوني لـ /admin/settings).
- Primary action (inventory): Create draft

## 3. UI components
- Status Chip
- Button
- Page header
- Status summary strip
- Filter bar
- Data table (sortable, cursor pager)
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: search; inheritance breadcrumb; publish diff; scope icon; approval

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Draft edit | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Draft edit | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Draft edit | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Draft edit | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Draft edit | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Draft edit | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Review | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Draft change | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-ADMIN-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Financial and safeguarding keys need dual approval
- Every change creates a new version with rollback

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
| `GET /api/v1/admin/settings/versions` | `get__api_v1_admin_settings_versions` |
| `POST /api/v1/admin/settings/drafts` | `post__api_v1_admin_settings_drafts` |
| `POST /api/v1/admin/settings/versions/{id}/decision` | `post__api_v1_admin_settings_versions_settingsVersionId_decision` |
- v1.2 trace: `POST /api/v1/admin/settings/drafts` · SPECIFIED; implementation pending
- **Functional requirements:** FR-SUP-011, FR-ADMIN-004
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
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-SUP-010", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"sup-010.draft-edit"} — Draft edit
- `action_clicked` {action_id:"sup-010.draft-edit"} — Draft edit
- `action_clicked` {action_id:"sup-010.draft-edit"} — Draft edit
- `action_clicked` {action_id:"sup-010.draft-edit"} — Draft edit
- `action_clicked` {action_id:"sup-010.draft-edit"} — Draft edit
- `action_clicked` {action_id:"sup-010.draft-edit"} — Draft edit
- `action_clicked` {action_id:"sup-010.review"} — Review
- `action_clicked` {action_id:"sup-010.draft-change"} — Draft change
- `action_clicked` {action_id:"sup-010.domain"} — Domain
- `action_clicked` {action_id:"sup-010.scope"} — Scope
- `action_clicked` {action_id:"sup-010.status"} — Status
- `action_clicked` {action_id:"sup-010.sort-key"} — Sort by Key
- `action_clicked` {action_id:"sup-010.sort-effective-value"} — Sort by Effective value
- `action_clicked` {action_id:"sup-010.sort-inherited-from"} — Sort by Inherited from
- `action_clicked` {action_id:"sup-010.sort-version"} — Sort by Version
- `action_clicked` {action_id:"sup-010.sort-status"} — Sort by Status
- `action_clicked` {action_id:"sup-010.next-page"} — Next page
- `action_clicked` {action_id:"sup-010.previous-page"} — Previous page
- `action_clicked` {action_id:"sup-010.retry"} — Retry
- `action_clicked` {action_id:"sup-010.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `sup-010.draft-edit` | Draft edit · مسودة تعديل | action | **PROPOSED:** calls `post__api_v1_admin_settings_drafts` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.draft-edit` | Draft edit · مسودة تعديل | action | **PROPOSED:** calls `post__api_v1_admin_settings_drafts` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.draft-edit` | Draft edit · مسودة تعديل | action | **PROPOSED:** calls `post__api_v1_admin_settings_drafts` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.draft-edit` | Draft edit · مسودة تعديل | action | **PROPOSED:** calls `post__api_v1_admin_settings_drafts` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.draft-edit` | Draft edit · مسودة تعديل | action | **PROPOSED:** calls `post__api_v1_admin_settings_drafts` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.draft-edit` | Draft edit · مسودة تعديل | action | **PROPOSED:** calls `post__api_v1_admin_settings_drafts` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.review` | Review · راجع | action | **PROPOSED:** calls `post__api_v1_admin_settings_drafts` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.draft-change` | Draft change · مسودة تغيير | action | **PROPOSED:** calls `post__api_v1_admin_settings_drafts` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.domain` | Domain · المجال | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `sup-010.scope` | Scope · النطاق | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `sup-010.status` | Status · الحالة | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `sup-010.sort-key` | Sort by Key · ترتيب حسب المفتاح | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-010.sort-effective-value` | Sort by Effective value · ترتيب حسب القيمة الفعّالة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-010.sort-inherited-from` | Sort by Inherited from · ترتيب حسب موروثة من | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-010.sort-version` | Sort by Version · ترتيب حسب النسخة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-010.sort-status` | Sort by Status · ترتيب حسب الحالة | sort | Re-queries the list with `sort=<column>&order=asc|desc` (server-side sort); toggles direction on repeat | list re-queries with sort param · aria-sort updates · URL keeps sort |
| `sup-010.next-page` | Next page · الصفحة التالية | pager | Requests the next page with the `next_cursor` returned by the list operation; no total count is shown | next cursor page loads · focus moves to first row · loading row while fetching · end of list disables Next |
| `sup-010.previous-page` | Previous page · الصفحة السابقة | disabled | Not actionable; the reason is shown next to it | none — shows the reason it is disabled |
| `sup-010.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-010.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
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
- [ ] `get__api_v1_admin_settings_versions` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__api_v1_admin_settings_drafts` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__api_v1_admin_settings_versions_settingsVersionId_decision` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `sup-010.draft-edit` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-010.draft-edit` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-010.draft-edit` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-010.draft-edit` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-010.draft-edit` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-010.draft-edit` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-010.review` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-010.draft-change` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Canonical implementation; `UX-ADMIN-041` aliases here (PROPOSED).
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `sup-010.draft-edit` Draft edit | action | API_EXISTING | `post__api_v1_admin_settings_drafts` | high | Bound by the 2026-11-23 contract audit |
| `sup-010.draft-edit` Draft edit | action | API_EXISTING | `post__api_v1_admin_settings_drafts` | high | Bound by the 2026-11-23 contract audit |
| `sup-010.draft-edit` Draft edit | action | API_EXISTING | `post__api_v1_admin_settings_drafts` | high | Bound by the 2026-11-23 contract audit |
| `sup-010.draft-edit` Draft edit | action | API_EXISTING | `post__api_v1_admin_settings_drafts` | high | Bound by the 2026-11-23 contract audit |
| `sup-010.draft-edit` Draft edit | action | API_EXISTING | `post__api_v1_admin_settings_drafts` | high | Bound by the 2026-11-23 contract audit |
| `sup-010.draft-edit` Draft edit | action | API_EXISTING | `post__api_v1_admin_settings_drafts` | high | Bound by the 2026-11-23 contract audit |
| `sup-010.review` Review | action | UI_ONLY | — | high | Opens the item detail (navigation within the screen) |
| `sup-010.draft-change` Draft change | action | API_EXISTING | `post__api_v1_admin_settings_drafts` | high | Bound by the 2026-11-23 contract audit |
| `sup-010.domain` Domain | filter | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.scope` Scope | filter | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.status` Status | filter | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.sort-key` Sort by Key | sort | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.sort-effective-value` Sort by Effective value | sort | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.sort-inherited-from` Sort by Inherited from | sort | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.sort-version` Sort by Version | sort | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.sort-status` Sort by Status | sort | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.next-page` Next page | pager | LIST_QUERY | `get__api_v1_admin_settings_versions` | high | Re-queries the screen’s list operation with the parameter |
| `sup-010.previous-page` Previous page | disabled | DISABLED | — | high | Not actionable; reason shown |
| `sup-010.retry` Retry | action | REFETCH | `get__api_v1_admin_settings_versions` | high | Re-runs the failed request(s) |
| `sup-010.reconnect` Reconnect | action | REFETCH | `get__api_v1_admin_settings_versions` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
