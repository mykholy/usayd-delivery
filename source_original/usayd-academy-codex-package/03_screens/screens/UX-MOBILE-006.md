# UX-MOBILE-006 — Flutter AI Coach

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-MOBILE-006`
- **Name:** Flutter AI Coach
- **Role:** Learner (Flutter) · inventory persona `MOBILE`
- **Module:** `AI` · phase `P2`
- **Route:** `mobile://coach`
- **Design files:** `01_design/canvas/UX-MOBILE-006.dc.html` · `01_design/html/ar/UX-MOBILE-006.html` · `01_design/html/en/UX-MOBILE-006.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: AI coach on mobile.
- AR: المرافق الذكي على الموبايل.
- Primary action (inventory): ابدأ تمرين

## 3. UI components
- Night banner (greeting)
- Alert / Inline
- AI suggestion card
- Status Chip
- Button
- Card
- Mobile / Night header + sheet
- Loading skeleton
- State panel
- Mobile / Tab bar
- Inventory anatomy: chat; suggestion; approved plan

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Why this? | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Dismiss | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-MOBILE-002.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Follow module rules in `05_requirements/` and the FRs listed in §8.

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `AI_UNAVAILABLE`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Your changes were saved” · AR «تم حفظ التغييرات» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/learning-plans/suggestions` | `post__learning_plans_suggestions` |
- **Functional requirements:** FR-AI-007, FR-AI-002
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1.

## 10. Navigation destinations
- `UX-MOBILE-002.dc.html`
- Shell navigation: bottom tab bar

## 11. Responsive behavior
- Flutter phone 360–428 portrait; tablet uses two-pane where noted; respects safe areas and dynamic type.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-MOBILE-006", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"mobile-006.why-this"} — Why this?
- `action_clicked` {action_id:"mobile-006.dismiss"} — Dismiss
- `action_clicked` {action_id:"mobile-006.retry"} — Retry
- `action_clicked` {action_id:"mobile-006.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `mobile-006.why-this` | Why this? · لماذا هذا الاقتراح؟ | action | **PROPOSED:** calls `post__learning_plans_suggestions` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `mobile-006.dismiss` | Dismiss · إخفاء | action | Closes or reverts locally; no server write | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `mobile-006.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `mobile-006.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- None.

## 16. Themes & breakpoints
- Light and dark use the same markup; colours only from tokens (`02_design_system/tokens.color.v0.4.json`). Night surfaces stay night in both themes.
- 360/390: Flutter phone layout, safe areas, bottom tabs · 768: two columns where space allows, sidebar collapses to the top bar · 1024: sidebar visible, splits stack below 1100 · 1440: design reference width.

## 17. Acceptance criteria
- [ ] Renders in Arabic (RTL) and English (LTR), light and dark, at 360, 390, 768, 1024 and 1440 px without horizontal page scroll
- [ ] All seven states (default, loading, empty, error, no-permission, offline, success) are reachable and use the copy in §7
- [ ] Every interactive target is at least 44×44 px; every control has an accessible name; focus order follows reading order
- [ ] Text contrast ≥ 4.5:1 and non-text ≥ 3:1 in both themes (axe: 0 serious/critical violations)
- [ ] One H1; heading levels never skip
- [ ] `post__learning_plans_suggestions` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `mobile-006.why-this` follows its contract in §14 and is idempotent on double tap
- [ ] `mobile-006.dismiss` follows its contract in §14 and is idempotent on double tap
- [ ] `mobile-006.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `mobile-006.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `mobile-006.why-this` Why this? | action | UI_ONLY | — | high | Opens the AI provenance/explanation panel from data already loaded |
| `mobile-006.dismiss` Dismiss | action | UI_ONLY | — | high | Hides the suggestion locally for this session (no server write) |
| `mobile-006.retry` Retry | action | REFETCH | — | high | Re-runs the failed request(s) |
| `mobile-006.reconnect` Reconnect | action | REFETCH | — | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
