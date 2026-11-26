# UX-TEACHER-007 — Lesson Report Editor

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-TEACHER-007`
- **Name:** Lesson Report Editor
- **Role:** Teacher · inventory persona `TEACHER`
- **Module:** `ATT` · phase `P0`
- **Route:** `/teach/lessons/:id/report`
- **Design files:** `01_design/canvas/UX-TEACHER-007.dc.html` · `01_design/html/ar/UX-TEACHER-007.html` · `01_design/html/en/UX-TEACHER-007.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Write and publish the lesson report.
- AR: كتابة تقرير الحصة ونشره بعد المراجعة.
- Primary action (inventory): اعتماد التقرير

## 3. UI components
- Page header
- Form field
- Status Chip
- Data table (cards < 760px)
- Slide to confirm
- Button
- Card
- AI suggestion card
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: rubric; passages; homework; submit

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Save draft | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Why this? | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Dismiss | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Propose plan change | navigates to `UX-TEACHER-011.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-TEACHER-002.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| Attendance outcome | select | yes | required | — |
| Note to learner | textarea | yes | required | — |
| Tasks until next lesson | textarea | yes | required | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Required: attendance outcome, at least one passage rating
- AI draft summary must be edited/confirmed by teacher
- Publishing creates audit event; edits after publish are versioned

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Report published to learner” · AR «نُشر التقرير للمتعلم» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/lessons/{lessonId}/report` | `post__lessons__lessonId__report` |
- Critical trace (package): `post__lessons__lessonId__report` · requirement family `FR-ATT-001` · acceptance: draft/submit/edit/audit
- **Functional requirements:** FR-ATT-002, FR-ATT-003, FR-AI-006, FR-PLAN-003
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Teacher — only assigned learners/lessons; PII minimized (no learner contact details).

## 10. Navigation destinations
- `UX-TEACHER-002.dc.html`
- `UX-TEACHER-011.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-TEACHER-007", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"teacher-007.slide-to-publish-to-learner"} — Slide to publish to learner
- `action_clicked` {action_id:"teacher-007.save-draft"} — Save draft
- `action_clicked` {action_id:"teacher-007.why-this"} — Why this?
- `action_clicked` {action_id:"teacher-007.dismiss"} — Dismiss
- `action_clicked` {action_id:"teacher-007.retry"} — Retry
- `action_clicked` {action_id:"teacher-007.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `teacher-007.slide-to-publish-to-learner` | Slide to publish to learner · اسحب للنشر للمتعلم | slide | Slide-to-confirm (see COMPONENTS.md › Slide to confirm). Then performs the screen’s confirm action — **PROPOSED:** calls `post__lessons__lessonId__report` | armed (first tap/Enter) · confirmed (drag past 90% or second tap/Enter within 5 s) · cancelled (release before 90%, pointer cancel, Esc, or 5 s timeout) · then the action’s own success/error states |
| `teacher-007.save-draft` | Save draft · احفظ مسودة | action | **PROPOSED:** calls `post__lessons__lessonId__report` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-007.why-this` | Why this? · لماذا هذا الاقتراح؟ | action | **PROPOSED:** calls `post__lessons__lessonId__report` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-007.dismiss` | Dismiss · إخفاء | action | Closes or reverts locally; no server write | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-007.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `teacher-007.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `post__lessons__lessonId__report` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `teacher-007.save-draft` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-007.why-this` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-007.dismiss` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-007.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `teacher-007.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `teacher-007.slide-to-publish-to-learner` Slide to publish to learner | slide | API_EXISTING | `post__lessons__lessonId__report` | medium | Only write operation on the screen |
| `teacher-007.save-draft` Save draft | action | API_EXISTING | `post__lessons__lessonId__report` | medium | Only write operation on the screen |
| `teacher-007.why-this` Why this? | action | UI_ONLY | — | high | Opens the AI provenance/explanation panel from data already loaded |
| `teacher-007.dismiss` Dismiss | action | UI_ONLY | — | high | Hides the suggestion locally for this session (no server write) |
| `teacher-007.retry` Retry | action | REFETCH | — | high | Re-runs the failed request(s) |
| `teacher-007.reconnect` Reconnect | action | REFETCH | — | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
