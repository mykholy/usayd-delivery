# UX-ADMIN-024 — Session Policy Review

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-ADMIN-024`
- **Name:** Session Policy Review
- **Role:** Platform admin (scoped) · inventory persona `ADMIN`
- **Module:** `AI` · phase `P0`
- **Route:** `/admin/session-reviews`
- **Design files:** `01_design/canvas/UX-ADMIN-024.dc.html` · `01_design/html/ar/UX-ADMIN-024.html` · `01_design/html/en/UX-ADMIN-024.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Human review of consented session flags.
- AR: مراجعة بشرية لإشارات الجلسات (بموافقة).
- Primary action (inventory): حسم الحالة

## 3. UI components
- Page header
- Key-value list
- Card
- Radio cards
- Form field
- Button
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- Alert / Inline
- State panel
- Inventory anatomy: evidence; consent; human disposition

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Record decision | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-ADMIN-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| d | radio | yes | one option required | — |
| Reason (recorded in audit) | textarea | yes | required; 10–500 chars | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- No automatic ban
- Transcript excerpt masked by default
- Retention timer shown

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Your changes were saved” · AR «تم حفظ التغييرات» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `GET /api/v1/admin/ai-policy-flags` | `get__admin_ai_policy_flags` |
| `POST /api/v1/admin/ai-policy-flags/{flagId}/resolve` | `post__admin_ai_policy_flags__flagId__resolve` |
- **Functional requirements:** FR-AI-008, FR-SUP-004, FR-SEC-005
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- Restricted reviewer role; dual review when safeguarding involved.

## 10. Navigation destinations
- `UX-ADMIN-001.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-ADMIN-024", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"admin-024.record-decision"} — Record decision
- `action_clicked` {action_id:"admin-024.retry"} — Retry
- `action_clicked` {action_id:"admin-024.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `admin-024.record-decision` | Record decision · سجّل القرار | action | **PROPOSED:** calls `post__admin_ai_policy_flags__flagId__resolve` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-024.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `admin-024.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `get__admin_ai_policy_flags` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__admin_ai_policy_flags__flagId__resolve` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `admin-024.record-decision` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-024.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `admin-024.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `admin-024.record-decision` Record decision | action | API_EXISTING | `post__admin_ai_policy_flags__flagId__resolve` | medium | Only write operation on the screen |
| `admin-024.retry` Retry | action | REFETCH | `get__admin_ai_policy_flags` | high | Re-runs the failed request(s) |
| `admin-024.reconnect` Reconnect | action | REFETCH | `get__admin_ai_policy_flags` | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
