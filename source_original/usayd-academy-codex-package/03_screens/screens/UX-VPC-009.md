# UX-VPC-009 — Embedded vs External Prejoin

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-VPC-009`
- **Name:** Embedded vs External Prejoin
- **Role:** Learner · inventory persona `STUDENT`
- **Module:** `VPC` · phase `P0`
- **Route:** `/lessons/:id/prejoin`
- **Design files:** `01_design/canvas/UX-VPC-009.dc.html` · `01_design/html/ar/UX-VPC-009.html` · `01_design/html/en/UX-VPC-009.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Prejoin: embedded vs external depending on provider.
- AR: ما قبل الدخول: داخل المنصة أو رابط خارجي حسب المزود.
- Primary action (inventory): Join

## 3. UI components
- Page header
- Status Chip
- Video stage
- Form field
- List row
- Card
- Button
- Alert / Inline
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- State panel
- Inventory anatomy: mic/camera; timezone; provider badge; consent; external explanation

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Join lesson | navigates to `UX-LEARNER-010.dc.html` | Navigate |
| Open Google Meet | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Come back here for your report | navigates to `UX-LEARNER-011.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-LEARNER-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| Microphone | select | yes | required | — |
| Camera | select | yes | required | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Join token short-lived; never exposes vendor keys
- External providers open in new tab with return action
- Camera optional where policy allows (audio-only)

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `JOIN_NOT_OPEN`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Your changes were saved” · AR «تم حفظ التغييرات» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/lessons/{lessonId}/join` | `post__lessons__lessonId__join` |
| `GET /api/v1/conferences/{id}/capabilities` | `get__conferences__conferenceId__capabilities` |
- v1.2 trace: `POST /api/v1/lessons/{lessonId}/join` · SPECIFIED; implementation pending
- **Functional requirements:** FR-VPC-011, FR-VIDEO-004, FR-VPC-014, FR-VIDEO-008
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation.

## 10. Navigation destinations
- `UX-LEARNER-001.dc.html`
- `UX-LEARNER-010.dc.html`
- `UX-LEARNER-011.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-VPC-009", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"vpc-009.open-google-meet"} — Open Google Meet
- `action_clicked` {action_id:"vpc-009.retry"} — Retry
- `action_clicked` {action_id:"vpc-009.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `vpc-009.open-google-meet` | Open Google Meet · افتح Google Meet | action | **PROPOSED:** calls `post__lessons__lessonId__join` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `vpc-009.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `vpc-009.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `post__lessons__lessonId__join` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `get__conferences__conferenceId__capabilities` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `vpc-009.open-google-meet` follows its contract in §14 and is idempotent on double tap
- [ ] `vpc-009.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `vpc-009.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `vpc-009.open-google-meet` Open Google Meet | action | API_EXISTING | `post__lessons__lessonId__join` | medium | Only write operation on the screen |
| `vpc-009.retry` Retry | action | REFETCH | `get__conferences__conferenceId__capabilities` | high | Re-runs the failed request(s) |
| `vpc-009.reconnect` Reconnect | action | REFETCH | `get__conferences__conferenceId__capabilities` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
