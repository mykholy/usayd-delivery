# UX-MOBILE-K08 — Kids · My stars (added)

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-MOBILE-K08`
- **Name:** Kids · My stars (added)
- **Role:** Learner (Flutter, Kids mode 6–12) · inventory persona `MOBILE`
- **Module:** `ENG` · phase `P2`
- **Route:** `mobile://kids/stars`
- **Design files:** `01_design/canvas/UX-MOBILE-K08.dc.html` · `01_design/html/ar/UX-MOBILE-K08.html` · `01_design/html/en/UX-MOBILE-K08.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: The child’s private stars and badges.
- AR: النجوم والشارات الخاصة بالطفل.
- Primary action (inventory): 

## 3. UI components
- Badge grid (kids)
- Alert / Inline
- Button
- Mobile / Night header + sheet
- Loading skeleton
- State panel
- Mobile / Tab bar
- Inventory anatomy: 

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Earn a star today | navigates to `UX-MOBILE-K02.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-MOBILE-K02.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Kids mode (6–12) is only available with a verified guardian consent (O-04); until then the limited mode applies
- No payments, no external links, no chat with strangers, no public ranking or leaderboard in kids mode
- Stars and badges are private, non-monetary and awarded by the teacher or by completing teacher-approved tasks; no streak-loss penalties (a missed day pauses, never resets)
- Quran text and the mushaf view are identical in every mode — no playful styling on ayat
- Guardian settings are behind the guardian PIN; changing mode for under-13 requires the guardian
- Badge catalogue and award rules need academic approval (decision D-36)

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
| `GET /api/v1/achievements` | `get__achievements` |
- **Functional requirements:** FR-ENG-004
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- 

## 10. Navigation destinations
- `UX-MOBILE-K02.dc.html`
- Shell navigation: bottom tab bar

## 11. Responsive behavior
- Flutter phone frame 390×844 (min 360); app bar 60, bottom tab bar with safe-area 22px; content scrolls; landscape and tablet two-pane where noted.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ Badges endpoint not in OpenAPI v1.2
- ⚠️ Badge catalogue and award rules (D-36)

## 13. Analytics
- `screen_viewed` {screen_id:"UX-MOBILE-K08", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"mobile-k08.retry"} — Retry
- `action_clicked` {action_id:"mobile-k08.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `mobile-k08.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `mobile-k08.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `get__achievements` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `mobile-k08.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `mobile-k08.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `mobile-k08.retry` Retry | action | REFETCH | `get__achievements` | high | Re-runs the failed request(s) |
| `mobile-k08.reconnect` Reconnect | action | REFETCH | `get__achievements` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
