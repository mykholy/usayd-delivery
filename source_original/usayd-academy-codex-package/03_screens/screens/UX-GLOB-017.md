# UX-GLOB-017 — Flutter Region & Language

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-GLOB-017`
- **Name:** Flutter Region & Language
- **Role:** Learner (Flutter) · inventory persona `MOBILE`
- **Module:** `I18N` · phase `P2`
- **Route:** `mobile://settings/region`
- **Design files:** `01_design/canvas/UX-GLOB-017.dc.html` · `01_design/html/ar/UX-GLOB-017.html` · `01_design/html/en/UX-GLOB-017.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Independent region, language and timezone in Flutter.
- AR: المنطقة واللغة والتوقيت في Flutter باستقلال.
- Primary action (inventory): Save

## 3. UI components
- Form field
- Alert / Inline
- Button
- Mobile / Night header + sheet
- Loading skeleton
- State panel
- Mobile / Tab bar
- Inventory anatomy: country; locale; IANA zone; currency; quote refresh guard

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Save | navigates to `UX-MOBILE-011.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-MOBILE-002.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| Language | select | yes | required | — |
| Country | select | yes | required | — |
| Timezone | select | yes | required | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Follow module rules in `05_requirements/` and the FRs listed in §8.

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Saved · your lessons didn’t move” · AR «حُفظ · لم تتغير مواعيدك» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `PATCH /api/v1/me/preferences` | `patch__api_v1_me_preferences` |
- v1.2 trace: `PATCH /api/v1/me/preferences` · SPECIFIED; implementation pending
- **Functional requirements:** FR-I18N-006, FR-TIME-001, FR-MOB-001
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1.

## 10. Navigation destinations
- `UX-MOBILE-002.dc.html`
- `UX-MOBILE-011.dc.html`
- Shell navigation: bottom tab bar

## 11. Responsive behavior
- Flutter phone 360–428 portrait; tablet uses two-pane where noted; respects safe areas and dynamic type.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-GLOB-017", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"glob-017.retry"} — Retry
- `action_clicked` {action_id:"glob-017.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `glob-017.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `glob-017.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `patch__api_v1_me_preferences` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `glob-017.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `glob-017.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `glob-017.retry` Retry | action | REFETCH | — | high | Re-runs the failed request(s) |
| `glob-017.reconnect` Reconnect | action | REFETCH | — | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
