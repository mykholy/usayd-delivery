# UX-MOBILE-000 — Flutter Splash (added)

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-MOBILE-000`
- **Name:** Flutter Splash (added)
- **Role:** Learner (Flutter) · inventory persona `MOBILE`
- **Module:** `MOB` · phase `P2`
- **Route:** `mobile://splash`
- **Design files:** `01_design/canvas/UX-MOBILE-000.dc.html` · `01_design/html/ar/UX-MOBILE-000.html` · `01_design/html/en/UX-MOBILE-000.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Animated splash while the app boots, then automatic routing.
- AR: شاشة افتتاحية متحركة أثناء تجهيز التطبيق، ثم توجيه المستخدم تلقائيًا.
- Primary action (inventory): لا يوجد — انتقال تلقائي

## 3. UI components
- Splash (animated brand mark)
- Loading skeleton
- Button
- Alert / Inline
- State panel
- Inventory anatomy: animated brand mark; wordmark; loader; native launch screen

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-MOBILE-002.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
- No form fields on this screen (read/act only).

## 6. Business rules
- Design addition D-16 (owner request 2026-11-21); not in blueprint v1.2 inventory
- Native launch screen (Android 12+ SplashScreen API / iOS LaunchScreen): static logo mark centred on #0F2529, no text — then the Flutter splash continues the same mark seamlessly
- Show only while bootstrapping (secure token read/refresh, locale + theme, remote config). Minimum 0.8 s, maximum 2.5 s; never a fixed artificial delay
- Routing: valid learner session -> UX-MOBILE-002; valid teacher session -> UX-MOBILE-009; no or expired session -> UX-MOBILE-001
- Offline with a cached session -> continue to home in offline mode; offline without session -> login with offline notice
- Splash is always the Night palette (both themes); respects reduced motion (static mark, no draw-in) and the device language for the tagline
- No ads, no promotional claims, no statistics on the splash

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Not applicable” · AR «لا ينطبق»
- **Error:** “We couldn’t load this” + retry; show error code `BOOTSTRAP_FAILED`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Ready” · AR «جاهز» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/auth/refresh` | `post__auth_refresh` |
| `GET /api/v1/me/preferences` | `get__api_v1_me_preferences` |
- **Functional requirements:** FR-MOB-001, FR-I18N-001
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Authenticated learner/teacher on Flutter; same server authorization as web. No admin parity in mobile v1.

## 10. Navigation destinations
- `UX-MOBILE-002.dc.html`
- Shell navigation: bottom tab bar

## 11. Responsive behavior
- Full-bleed, safe-area aware; mark 168 px on phones, 200 px on tablets; content centred vertically.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- ⚠️ Force-update / minimum supported app version policy is not defined in the blueprint
- ⚠️ Token refresh endpoint missing from OpenAPI v1.2

## 13. Analytics
- `screen_viewed` {screen_id:"UX-MOBILE-000", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"mobile-000.retry"} — Retry
- `action_clicked` {action_id:"mobile-000.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `mobile-000.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `mobile-000.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `post__auth_refresh` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `get__api_v1_me_preferences` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `mobile-000.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `mobile-000.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `mobile-000.retry` Retry | action | REFETCH | `get__api_v1_me_preferences` | high | Re-runs the failed request(s) |
| `mobile-000.reconnect` Reconnect | action | REFETCH | `get__api_v1_me_preferences` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
