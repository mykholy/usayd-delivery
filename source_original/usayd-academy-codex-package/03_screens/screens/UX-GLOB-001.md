# UX-GLOB-001 — Country & Currency Selector

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-GLOB-001`
- **Name:** Country & Currency Selector
- **Role:** Guest (public) · inventory persona `PUBLIC`
- **Module:** `GEO` · phase `P0`
- **Route:** `/choose-country`
- **Design files:** `01_design/canvas/UX-GLOB-001.dc.html` · `01_design/html/ar/UX-GLOB-001.html` · `01_design/html/en/UX-GLOB-001.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Pick the storefront market (country) and check availability.
- AR: اختيار سوق المتجر (البلد) والتحقق من توفره.
- Primary action (inventory): Confirm country

## 3. UI components
- Status Chip
- Page header
- Filter bar
- Alert / Inline
- Card
- List row
- Button
- Page hero (illustrated)
- Shell / Public header
- Loading skeleton
- State panel
- Shell / Public footer
- Inventory anatomy: country search; flag icon; currency label; availability badge; selected state; help; waitlist

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Confirm country | navigates to `UX-GLOB-002.dc.html` | Navigate |
| My country isn’t available | navigates to `UX-GLOB-003.dc.html` | Navigate |
| Book a level assessment | navigates to `UX-PUBLIC-009.dc.html` | Navigate |
| Log in | navigates to `UX-AUTH-003.dc.html` | Navigate |
| Book a level assessment | navigates to `UX-PUBLIC-009.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Choose another country | navigates to `UX-GLOB-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- IP country is a hint only; user selection persists
- Changing country changes price book & charge currency only — not language or timezone

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
| `GET /api/v1/public/markets` | `get__api_v1_public_markets` |
- v1.2 trace: `GET /api/v1/public/markets` · SPECIFIED; implementation pending
- **Functional requirements:** FR-GEO-001, FR-GEO-002, FR-GEO-003
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Public.

## 10. Navigation destinations
- `UX-AUTH-003.dc.html`
- `UX-GLOB-001.dc.html`
- `UX-GLOB-002.dc.html`
- `UX-GLOB-003.dc.html`
- `UX-PUBLIC-009.dc.html`
- Shell navigation: public header/footer

## 11. Responsive behavior
- Fluid page: max content 1280; ≥1100 multi-column; 760–1100 grids collapse to 2 columns; <760 single column, header nav hides (burger), CTAs stay visible; touch targets ≥44px.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-GLOB-001", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"glob-001.retry"} — Retry
- `action_clicked` {action_id:"glob-001.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `glob-001.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `glob-001.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

- Mappings marked **PROPOSED** are inferred from this screen’s operations and need confirmation before build.

## 15. Content slots
- None.

## 16. Themes & breakpoints
- Light and dark use the same markup; colours only from tokens (`02_design_system/tokens.color.v0.4.json`). Night surfaces stay night in both themes.
- 360/390: single column, sticky primary CTA, tables become stacked records, calendar becomes an agenda list · 768: two columns where space allows, sidebar collapses to the top bar · 1024: sidebar visible, splits stack below 1100 · 1440: design reference width.

## 17. Acceptance criteria
- [ ] Renders in Arabic (RTL) and English (LTR), light and dark, at 360, 390, 768, 1024 and 1440 px without horizontal page scroll
- [ ] All seven states (default, loading, empty, error, no-permission, offline, success) are reachable and use the copy in §7
- [ ] Every interactive target is at least 44×44 px; every control has an accessible name; focus order follows reading order
- [ ] Text contrast ≥ 4.5:1 and non-text ≥ 3:1 in both themes (axe: 0 serious/critical violations)
- [ ] One H1; heading levels never skip
- [ ] `get__api_v1_public_markets` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `glob-001.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `glob-001.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `glob-001.retry` Retry | action | REFETCH | `get__api_v1_public_markets` | high | Re-runs the failed request(s) |
| `glob-001.reconnect` Reconnect | action | REFETCH | `get__api_v1_public_markets` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
