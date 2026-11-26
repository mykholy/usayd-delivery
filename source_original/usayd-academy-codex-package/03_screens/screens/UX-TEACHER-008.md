# UX-TEACHER-008 — My Assigned Learners

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-TEACHER-008`
- **Name:** My Assigned Learners
- **Role:** Teacher · inventory persona `TEACHER`
- **Module:** `TCHR` · phase `P0`
- **Route:** `/teach/learners`
- **Design files:** `01_design/canvas/UX-TEACHER-008.dc.html` · `01_design/html/ar/UX-TEACHER-008.html` · `01_design/html/en/UX-TEACHER-008.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: My assigned learners.
- AR: المتعلمون المسندون إليّ.
- Primary action (inventory): افتح الملف

## 3. UI components
- Page header
- Filter bar
- Status Chip
- Data table (cards < 760px)
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Button
- Alert / Inline
- State panel
- Inventory anatomy: list; filter; no direct contact numbers

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Record | navigates to `UX-TEACHER-009.dc.html` | Navigate |
| Record | navigates to `UX-TEACHER-009.dc.html` | Navigate |
| Record | navigates to `UX-TEACHER-009.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-TEACHER-002.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Follow module rules in `05_requirements/` and the FRs listed in §8.

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “No assigned learners” · AR «لا يوجد متعلمون مسندون»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “This view is up to date” · AR «البيانات محدَّثة الآن» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `GET /api/v1/teachers/me/learners` | `UNRESOLVED — PROPOSED listMyLearners (P-27)` |
- **Functional requirements:** FR-TCHR-004, FR-SEC-001
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Teacher — only assigned learners/lessons; PII minimized (no learner contact details).

## 10. Navigation destinations
- `UX-TEACHER-002.dc.html`
- `UX-TEACHER-009.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ API: GET /api/v1/teachers/me/learners — UNRESOLVED — PROPOSED listMyLearners (P-27)

## 13. Analytics
- `screen_viewed` {screen_id:"UX-TEACHER-008", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"teacher-008.level"} — Level
- `action_clicked` {action_id:"teacher-008.program"} — Program
- `action_clicked` {action_id:"teacher-008.needs-attention"} — Needs attention
- `action_clicked` {action_id:"teacher-008.retry"} — Retry
- `action_clicked` {action_id:"teacher-008.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `teacher-008.level` | Level · المستوى | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `teacher-008.program` | Program · البرنامج | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `teacher-008.needs-attention` | Needs attention · يحتاج انتباه | filter | Opens a listbox; applies the filter to the list query | list updates · empty result state · error state |
| `teacher-008.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-008.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `GET /api/v1/teachers/me/learners` is behind a feature flag until its contract is approved (see `07_api/API_GAPS.md`)
- [ ] `teacher-008.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-008.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `teacher-008.level` Level | filter | LIST_QUERY | `listMyLearners` † | high | Re-queries the screen’s list operation with the parameter |
| `teacher-008.program` Program | filter | LIST_QUERY | `listMyLearners` † | high | Re-queries the screen’s list operation with the parameter |
| `teacher-008.needs-attention` Needs attention | filter | LIST_QUERY | `listMyLearners` † | high | Re-queries the screen’s list operation with the parameter |
| `teacher-008.retry` Retry | action | REFETCH | `listMyLearners` † | high | Re-runs the failed request(s) |
| `teacher-008.reconnect` Reconnect | action | REFETCH | `listMyLearners` † | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
