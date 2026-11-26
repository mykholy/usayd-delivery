# UX-TEACHER-011 — Plan Review Queue

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-TEACHER-011`
- **Name:** Plan Review Queue
- **Role:** Teacher · inventory persona `TEACHER`
- **Module:** `PLAN` · phase `P0`
- **Route:** `/teach/plans`
- **Design files:** `01_design/canvas/UX-TEACHER-011.dc.html` · `01_design/html/ar/UX-TEACHER-011.html` · `01_design/html/en/UX-TEACHER-011.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Approve/reject plans and AI recommendations.
- AR: اعتماد أو رفض الخطط والاقتراحات الذكية.
- Primary action (inventory): اعتماد أو رفض

## 3. UI components
- Page header
- Tabs
- Status Chip
- Version diff viewer
- Key-value list
- Slide to confirm
- Button
- Card
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: side by side; evidence; version diff

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Edit then approve | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Reject with reason | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Plan history | navigates to `UX-TEACHER-009.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-TEACHER-002.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Approve/reject requires reason when rejecting
- Optimistic version (409 on conflict)
- AI provenance shown: model, inputs, confidence label

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `PLAN_VERSION_CONFLICT`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Plan version 3 approved” · AR «اعتمدت النسخة 3 من الخطة» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `GET /api/v1/learning-plans?status=proposed` | `get__learning_plans` |
| `PATCH /api/v1/learning-plans/{planId}` | `patchLearningPlanDraft` |
| `POST /api/v1/learning-plans/{planId}/approve` | `post__learning_plans__planId__approve` |
- Critical trace (package): `post__learning_plans__planId__approve` · requirement family `FR-PLAN-001` · acceptance: teacher AI proposal approval
- **Functional requirements:** FR-PLAN-002, FR-AI-003, FR-AI-012, FR-SUP-002
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
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-TEACHER-011", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"teacher-011.tabs"} — Tabs filter the list in place; selection is kept in the URL query
- `action_clicked` {action_id:"teacher-011.slide-to-approve-plan"} — Slide to approve plan
- `action_clicked` {action_id:"teacher-011.edit-then-approve"} — Edit then approve
- `action_clicked` {action_id:"teacher-011.reject-with-reason"} — Reject with reason
- `action_clicked` {action_id:"teacher-011.retry"} — Retry
- `action_clicked` {action_id:"teacher-011.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `teacher-011.tabs` | Tabs filter the list in place; selection is kept in the URL query · تبويبات تصفّي القائمة في نفس الصفحة | tabs | Switches the list filter without leaving the page | list updates in place · URL query keeps selection |
| `teacher-011.slide-to-approve-plan` | Slide to approve plan · اسحب لاعتماد الخطة | slide | Slide-to-confirm (see COMPONENTS.md › Slide to confirm). Then performs the screen’s confirm action — **PROPOSED:** calls `patchLearningPlanDraft` | armed (first tap/Enter) · confirmed (drag past 90% or second tap/Enter within 5 s) · cancelled (release before 90%, pointer cancel, Esc, or 5 s timeout) · then the action’s own success/error states |
| `teacher-011.edit-then-approve` | Edit then approve · عدّل ثم اعتمد | action | **PROPOSED:** calls `patchLearningPlanDraft` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-011.reject-with-reason` | Reject with reason · ارفض مع سبب | action | **PROPOSED:** calls `patchLearningPlanDraft` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-011.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-011.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `get__learning_plans` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `patchLearningPlanDraft` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__learning_plans__planId__approve` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `teacher-011.edit-then-approve` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-011.reject-with-reason` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-011.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-011.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `teacher-011.tabs` Tabs filter the list in place; selection is kept in the URL query | tabs | LIST_QUERY | `get__learning_plans` | high | Re-queries the screen’s list operation with the parameter |
| `teacher-011.slide-to-approve-plan` Slide to approve plan | slide | API_EXISTING | `post__learning_plans__planId__approve` | medium | Matched “approve” to the operation name |
| `teacher-011.edit-then-approve` Edit then approve | action | API_EXISTING | `post__learning_plans__planId__approve` | medium | Matched “approve” to the operation name |
| `teacher-011.reject-with-reason` Reject with reason | action | API_EXISTING | `post__learning_plans__planId__approve` | high | Bound by the 2026-11-23 contract audit |
| `teacher-011.retry` Retry | action | REFETCH | `get__learning_plans` | high | Re-runs the failed request(s) |
| `teacher-011.reconnect` Reconnect | action | REFETCH | `get__learning_plans` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
