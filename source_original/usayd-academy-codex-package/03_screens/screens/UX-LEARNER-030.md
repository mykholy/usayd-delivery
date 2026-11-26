# UX-LEARNER-030 — Notifications

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-LEARNER-030`
- **Name:** Notifications
- **Role:** Learner · inventory persona `LEARNER`
- **Module:** `NOTIF` · phase `P0`
- **Route:** `/app/notifications`
- **Design files:** `01_design/canvas/UX-LEARNER-030.dc.html` · `01_design/html/ar/UX-LEARNER-030.html` · `01_design/html/en/UX-LEARNER-030.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Notifications and reminder preferences.
- AR: الإشعارات وتفضيلات التذكير.
- Primary action (inventory): ضبط الإشعارات

## 3. UI components
- Button
- Page header
- Tabs
- List row
- Card
- Checkbox / consent
- Form field
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: inbox; prefs; quiet hours

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Mark all read | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Details | navigates to `UX-LEARNER-009.dc.html` | Navigate |
| Read | navigates to `UX-LEARNER-011.dc.html` | Navigate |
| Review | navigates to `UX-LEARNER-014.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-LEARNER-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| 1-hour lesson reminder | checkbox | no | optional | — |
| Daily review reminder (optional) | checkbox | no | optional | — |
| Competition messages | checkbox | no | optional | — |
| Quiet hours | select | yes | required | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Follow module rules in `05_requirements/` and the FRs listed in §8.

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “No new notifications” · AR «لا إشعارات جديدة»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “This view is up to date” · AR «البيانات محدَّثة الآن» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `GET /api/v1/me/notifications` | `UNRESOLVED — PROPOSED listMyNotifications (P-24)` |
- **Functional requirements:** FR-NOTIF-002, FR-NOTIF-003, FR-TIME-008
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation.

## 10. Navigation destinations
- `UX-LEARNER-001.dc.html`
- `UX-LEARNER-009.dc.html`
- `UX-LEARNER-011.dc.html`
- `UX-LEARNER-014.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ API: GET /api/v1/me/notifications — UNRESOLVED — PROPOSED listMyNotifications (P-24)

## 13. Analytics
- `screen_viewed` {screen_id:"UX-LEARNER-030", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"learner-030.mark-all-read"} — Mark all read
- `action_clicked` {action_id:"learner-030.tabs"} — Tabs filter the list in place; selection is kept in the URL query
- `action_clicked` {action_id:"learner-030.retry"} — Retry
- `action_clicked` {action_id:"learner-030.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `learner-030.mark-all-read` | Mark all read · تحديد الكل كمقروء | action | **NEEDS_DECISION:** no write operation documented for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `learner-030.tabs` | Tabs filter the list in place; selection is kept in the URL query · تبويبات تصفّي القائمة في نفس الصفحة | tabs | Switches the list filter without leaving the page | list updates in place · URL query keeps selection |
| `learner-030.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `learner-030.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `GET /api/v1/me/notifications` is behind a feature flag until its contract is approved (see `07_api/API_GAPS.md`)
- [ ] `learner-030.mark-all-read` follows its contract in §14 and is idempotent on double tap
- [ ] `learner-030.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `learner-030.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `learner-030.mark-all-read` Mark all read | action | API_PROPOSED | `markNotificationsRead` † | high | Bound by the 2026-11-23 contract audit |
| `learner-030.tabs` Tabs filter the list in place; selection is kept in the URL query | tabs | LIST_QUERY | `listMyNotifications` † | high | Re-queries the screen’s list operation with the parameter |
| `learner-030.retry` Retry | action | REFETCH | `listMyNotifications` † | high | Re-runs the failed request(s) |
| `learner-030.reconnect` Reconnect | action | REFETCH | `listMyNotifications` † | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
