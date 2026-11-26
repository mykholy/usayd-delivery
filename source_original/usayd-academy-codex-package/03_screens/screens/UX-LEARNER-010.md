# UX-LEARNER-010 — Classroom

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-LEARNER-010`
- **Name:** Classroom
- **Role:** Learner · inventory persona `LEARNER`
- **Module:** `VIDEO` · phase `P0`
- **Route:** `/app/lessons/:id/live`
- **Design files:** `01_design/canvas/UX-LEARNER-010.dc.html` · `01_design/html/ar/UX-LEARNER-010.html` · `01_design/html/en/UX-LEARNER-010.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Live classroom: video + reader + objectives, per provider capability.
- AR: الفصل المباشر: فيديو + القارئ + أهداف الدرس، حسب قدرات المزود.
- Primary action (inventory): إنهاء الحصة

## 3. UI components
- Status Chip
- Button
- Video stage
- Classroom controls
- Alert / Inline
- Quran reader (licensed text placeholder)
- Card
- List row
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- State panel
- Inventory anatomy: video; Quran; teacher annotations; mic/video; reconnect

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Report a problem | navigates to `UX-LEARNER-031.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-LEARNER-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Learner never sees other learners’ streams
- Unsupported provider features are hidden with explanation
- Recording indicator only when consented recording is active
- Disconnect → reconnect banner; entitlement protected

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `PROVIDER_UNAVAILABLE`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Your changes were saved” · AR «تم حفظ التغييرات» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/lessons/{lessonId}/join` | `post__lessons__lessonId__join` |
| `GET /api/v1/conferences/{id}/capabilities` | `get__conferences__conferenceId__capabilities` |
- **Functional requirements:** FR-VIDEO-006, FR-VIDEO-007, FR-VIDEO-009, FR-VIDEO-010, FR-I18N-008
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Learner (own data only). Minor learners: consent-gated features hidden/disabled with explanation.

## 10. Navigation destinations
- `UX-LEARNER-001.dc.html`
- `UX-LEARNER-031.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-LEARNER-010", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"learner-010.retry"} — Retry
- `action_clicked` {action_id:"learner-010.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `learner-010.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `learner-010.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- runtime data (sample in design):  Ayah text from the licensed Quran source  ·  نص الآية من المصدر القرآني المعتمد 
- runtime data (sample in design):  Ayah text from the licensed Quran source  ·  نص الآية من المصدر القرآني المعتمد 
- runtime data (sample in design):  Ayah text from the licensed Quran source  ·  نص الآية من المصدر القرآني المعتمد 
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
- [ ] `learner-010.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `learner-010.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `learner-010.retry` Retry | action | REFETCH | `get__conferences__conferenceId__capabilities` | high | Re-runs the failed request(s) |
| `learner-010.reconnect` Reconnect | action | REFETCH | `get__conferences__conferenceId__capabilities` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
