# UX-GLOB-003 — Unavailable Country & Waitlist

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-GLOB-003`
- **Name:** Unavailable Country & Waitlist
- **Role:** Guest (public) · inventory persona `PUBLIC`
- **Module:** `GEO` · phase `P1`
- **Route:** `/unavailable-market`
- **Design files:** `01_design/canvas/UX-GLOB-003.dc.html` · `01_design/html/ar/UX-GLOB-003.html` · `01_design/html/en/UX-GLOB-003.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Capture interest from an unavailable country without payment.
- AR: جمع الاهتمام من بلد غير متاح دون أخذ دفع.
- Primary action (inventory): Join waitlist

## 3. UI components
- Status Chip
- Form field
- Checkbox / consent
- Button
- Image placeholder (licensed asset pending)
- Shell / Public header
- Loading skeleton
- Alert / Inline
- State panel
- Shell / Public footer
- Inventory anatomy: country illustration; clear unavailable explanation; no fake prices; privacy consent

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Join the waitlist | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Choose another country | navigates to `UX-GLOB-001.dc.html` | Navigate |
| Log in | navigates to `UX-AUTH-003.dc.html` | Navigate |
| Book a level assessment | navigates to `UX-PUBLIC-009.dc.html` | Navigate |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Choose another country | navigates to `UX-GLOB-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| Country | select | yes | required | — |
| Email | email | yes | required | — |
| I agree to receive one message at launch | checkbox | yes | must be checked | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- No prices shown for unavailable markets
- Marketing consent separate and optional

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “You’re on the waitlist” · AR «أضفناك لقائمة الانتظار» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/public/market-waitlist` | `UNRESOLVED — PROPOSED joinMarketWaitlist (P-22)` |
- v1.2 trace: `GET /api/v1/public/markets` · SPECIFIED; implementation pending
- **Functional requirements:** FR-GEO-003, FR-CRM-001
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Public.

## 10. Navigation destinations
- `UX-AUTH-003.dc.html`
- `UX-GLOB-001.dc.html`
- `UX-PUBLIC-009.dc.html`
- Shell navigation: public header/footer

## 11. Responsive behavior
- Fluid page: max content 1280; ≥1100 multi-column; 760–1100 grids collapse to 2 columns; <760 single column, header nav hides (burger), CTAs stay visible; touch targets ≥44px.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ API: POST /api/v1/public/market-waitlist — UNRESOLVED — PROPOSED joinMarketWaitlist (P-22)

## 13. Analytics
- `screen_viewed` {screen_id:"UX-GLOB-003", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"glob-003.join-the-waitlist"} — Join the waitlist
- `action_clicked` {action_id:"glob-003.retry"} — Retry
- `action_clicked` {action_id:"glob-003.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `glob-003.join-the-waitlist` | Join the waitlist · انضم لقائمة الانتظار | action | **PROPOSED:** calls `POST /api/v1/public/market-waitlist (UNRESOLVED)` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `glob-003.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `glob-003.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `POST /api/v1/public/market-waitlist` is behind a feature flag until its contract is approved (see `07_api/API_GAPS.md`)
- [ ] `glob-003.join-the-waitlist` follows its contract in §14 and is idempotent on double tap
- [ ] `glob-003.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `glob-003.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `glob-003.join-the-waitlist` Join the waitlist | action | API_PROPOSED | `joinMarketWaitlist` † | medium | Only write operation on the screen |
| `glob-003.retry` Retry | action | REFETCH | — | high | Re-runs the failed request(s) |
| `glob-003.reconnect` Reconnect | action | REFETCH | — | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
