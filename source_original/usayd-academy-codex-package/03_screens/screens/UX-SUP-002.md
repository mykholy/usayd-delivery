# UX-SUP-002 — Academic Plans Approval

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-SUP-002`
- **Name:** Academic Plans Approval
- **Role:** Supervisor (scoped) · inventory persona `SUPERVISOR`
- **Module:** `SUP` · phase `P0`
- **Route:** `/supervisor/academic/plans`
- **Design files:** `01_design/canvas/UX-SUP-002.dc.html` · `01_design/html/ar/UX-SUP-002.html` · `01_design/html/en/UX-SUP-002.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Approve academic plans or request changes.
- AR: اعتماد الخطط الأكاديمية أو طلب تعديلها.
- Primary action (inventory): Approve/reject

## 3. UI components
- Page header
- Tabs
- Status Chip
- Version diff viewer
- Key-value list
- Form field
- Slide to confirm
- Button
- Card
- Alert / Inline
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- State panel
- Inventory anatomy: learner rubric; teacher evidence; diff; AI disclaimer; change request

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Request changes | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-SUP-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| Your note | textarea | no | optional | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Only plans in supervisor market/program
- Cannot approve own proposals
- Learner PII minimized

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `OUT_OF_SCOPE`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Decision recorded; teacher notified” · AR «سُجّل قرارك واُبلغ المعلم» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/supervisor/academic-plans/{planId}/decision` | `post__api_v1_supervisor_academic_plans_planId_decision` |
| `GET /api/v1/learning-plans/{planId}` | `getLearningPlan` |
- v1.2 trace: `POST /api/v1/supervisor/academic-plans/{planId}/decision` · SPECIFIED; implementation pending
- **Functional requirements:** FR-SUP-002, FR-PLAN-002, FR-AI-003
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Supervisor — effective scope (role × market × program) + object ownership + assigned work; no self-approval; out-of-scope records denied server-side.

## 10. Navigation destinations
- `UX-SUP-001.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-SUP-002", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"sup-002.tabs"} — Tabs filter the list in place; selection is kept in the URL query
- `action_clicked` {action_id:"sup-002.slide-to-approve"} — Slide to approve
- `action_clicked` {action_id:"sup-002.request-changes"} — Request changes
- `action_clicked` {action_id:"sup-002.retry"} — Retry
- `action_clicked` {action_id:"sup-002.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `sup-002.tabs` | Tabs filter the list in place; selection is kept in the URL query · تبويبات تصفّي القائمة في نفس الصفحة | tabs | Switches the list filter without leaving the page | list updates in place · URL query keeps selection |
| `sup-002.slide-to-approve` | Slide to approve · اسحب للاعتماد | slide | Slide-to-confirm (see COMPONENTS.md › Slide to confirm). Then performs the screen’s confirm action — **PROPOSED:** calls `post__api_v1_supervisor_academic_plans_planId_decision` | armed (first tap/Enter) · confirmed (drag past 90% or second tap/Enter within 5 s) · cancelled (release before 90%, pointer cancel, Esc, or 5 s timeout) · then the action’s own success/error states |
| `sup-002.request-changes` | Request changes · اطلب تعديلًا | action | **PROPOSED:** calls `post__api_v1_supervisor_academic_plans_planId_decision` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-002.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `sup-002.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
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
- [ ] `post__api_v1_supervisor_academic_plans_planId_decision` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `getLearningPlan` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `sup-002.request-changes` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-002.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `sup-002.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `sup-002.tabs` Tabs filter the list in place; selection is kept in the URL query | tabs | LIST_QUERY | `getLearningPlan` | high | Re-queries the screen’s list operation with the parameter |
| `sup-002.slide-to-approve` Slide to approve | slide | API_EXISTING | `post__api_v1_supervisor_academic_plans_planId_decision` | medium | Only write operation on the screen |
| `sup-002.request-changes` Request changes | action | API_EXISTING | `post__api_v1_supervisor_academic_plans_planId_decision` | medium | Only write operation on the screen |
| `sup-002.retry` Retry | action | REFETCH | `getLearningPlan` | high | Re-runs the failed request(s) |
| `sup-002.reconnect` Reconnect | action | REFETCH | `getLearningPlan` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
