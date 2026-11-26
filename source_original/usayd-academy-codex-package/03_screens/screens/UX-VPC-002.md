# UX-VPC-002 — Video Provider Credentials

> Prototype notice: buttons in the design only navigate between artboards or switch the displayed state. Nothing in the design is real backend behavior; the contract below is.

## 1. Identity
- **Screen ID:** `UX-VPC-002`
- **Name:** Video Provider Credentials
- **Role:** Platform admin (scoped) · inventory persona `ADMIN`
- **Module:** `VPC` · phase `P0`
- **Route:** `/admin/settings/video-providers/:id/credentials`
- **Design files:** `01_design/canvas/UX-VPC-002.dc.html` · `01_design/html/ar/UX-VPC-002.html` · `01_design/html/en/UX-VPC-002.html`
- **Duplicate / related:** — 

## 2. Purpose
- EN: Provider credentials (masked vault ref) and connection test.
- AR: بيانات اعتماد المزود (مرجع خزنة مقنّع) واختبار الاتصال.
- Primary action (inventory): Rotate/validate

## 3. UI components
- Page header
- Key-value list
- Form field
- Button
- Card
- Alert / Inline
- Shell / Sidebar
- Shell / App topbar
- Timezone chip
- Loading skeleton
- State panel
- Inventory anatomy: masked secret reference; environment; connection test; MFA challenge; audit

## 4. User actions & interactions
| Action (EN label) | Result in prototype | Production behavior |
|---|---|---|
| Rotate (needs 2nd approval) | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Test connection | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Retry | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |
| Back to home | navigates to `UX-ADMIN-001.dc.html` | Navigate |
| Reconnect | in-place (no navigation) | Call the API in §8 / update local state; show success/error states |

## 5. Form fields & validation
| Field | Type | Required | Validation rule | Example error |
|---|---|---|---|---|
| New secret (never shown after save) | password | yes | write-only; sent to vault | — |
| Reason (recorded in audit) | textarea | yes | required; 10–500 chars | — |

- Server re-validates every field; client validation is a convenience. Errors use stable codes from the `errors.*` namespace and are announced via `role=alert`.

## 6. Business rules
- Follow module rules in `05_requirements/` and the FRs listed in §8.

## 7. States
- **Loading:** skeleton cards (aria-busy) — no layout shift; keep last data if refreshing.
- **Empty:** EN “Nothing here yet” · AR «لا توجد بيانات لعرضها بعد»
- **Error:** “We couldn’t load this” + retry; show error code `SERVER_ERROR`; keep user input.
- **No permission:** server returns 403 → panel with role/scope-specific copy + “Request access” (audited). For out-of-scope records the copy never reveals that the record exists.
- **Offline:** last cached copy if allowed; drafts stored locally; no payment/submit offline.
- **Success:** EN “Connection test passed (sandbox)” · AR «نجح اختبار الاتصال (بيئة تجريبية)» (inline status, role=status).

## 8. Backend data & API
| Method & path | operationId / status |
|---|---|
| `POST /api/v1/admin/video-providers` | `post__api_v1_admin_video_providers` |
| `POST /api/v1/admin/video-providers/{id}/connection-test` | `post__api_v1_admin_video_providers_providerAccountId_connection_test` |
- v1.2 trace: `POST /api/v1/admin/video-providers/{providerAccountId}/connection-test` · SPECIFIED; implementation pending
- **Functional requirements:** FR-VPC-001, FR-VPC-004, FR-SEC-006
- Required data: see `08_data_model/DATA_MODEL.md` for the entities behind each operation; all money = integer minor units + ISO 4217; all instants = UTC + IANA zone for display.

## 9. Permissions
- video.providers.credentials.rotate (security custodian, dual control)

## 10. Navigation destinations
- `UX-ADMIN-001.dc.html`
- Shell navigation: sidebar + topbar for role

## 11. Responsive behavior
- App shell: night sidebar 256 docked on logical start (right in AR, left in EN); <760 sidebar collapses to top bar with menu; content max 1280; split layouts (2fr/1fr) stack <1100; tables scroll horizontally inside their box and should switch to card lists <760 in production.
- RTL/LTR: same markup, `dir` on root; use logical CSS properties; mirror directional icons only; never mirror Quran text, logo or play icons.

## 12. Unresolved
- None specific to this screen (see global open decisions).

## 13. Analytics
- `screen_viewed` {screen_id:"UX-VPC-002", locale, theme, market} on load; `state_shown` {state} for empty/error/denied/offline.
- `action_clicked` {action_id:"vpc-002.show-password"} — Show / hide password
- `action_clicked` {action_id:"vpc-002.rotate-needs-2nd-approval"} — Rotate (needs 2nd approval)
- `action_clicked` {action_id:"vpc-002.test-connection"} — Test connection
- `action_clicked` {action_id:"vpc-002.retry"} — Retry
- `action_clicked` {action_id:"vpc-002.reconnect"} — Reconnect
- Payloads are privacy-safe: no names, contact data, Quran audio or free text. Minors: no marketing analytics.

## 14. Action contracts (in-place controls)
| action_id | Label (EN · AR) | Kind | Production behaviour | Exit states |
|---|---|---|---|---|
| `vpc-002.show-password` | Show / hide password · إظهار / إخفاء كلمة المرور | action | **PROPOSED:** calls `post__api_v1_admin_video_providers` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `vpc-002.rotate-needs-2nd-approval` | Rotate (needs 2nd approval) · تدوير (يحتاج اعتمادًا ثانيًا) | action | **PROPOSED:** calls `post__api_v1_admin_video_providers` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `vpc-002.test-connection` | Test connection · اختبر الاتصال | action | **PROPOSED:** calls `post__api_v1_admin_video_providers` | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `vpc-002.retry` | Retry · أعد المحاولة | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |
| `vpc-002.reconnect` | Reconnect · أعد الاتصال | action | Re-runs the failed request(s) for this screen | success · validation error (422) · forbidden (403) · offline (queued or blocked) · timeout (retry with same idempotency key) |

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
- [ ] `post__api_v1_admin_video_providers` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `post__api_v1_admin_video_providers_providerAccountId_connection_test` errors 401/403/404/409/422/429/5xx map to the states above; no client-side permission decisions
- [ ] `vpc-002.show-password` follows its contract in §14 and is idempotent on double tap
- [ ] `vpc-002.rotate-needs-2nd-approval` follows its contract in §14 and is idempotent on double tap
- [ ] `vpc-002.test-connection` follows its contract in §14 and is idempotent on double tap
- [ ] `vpc-002.retry` follows its contract in §14 and is idempotent on double tap
- [ ] `vpc-002.reconnect` follows its contract in §14 and is idempotent on double tap

## 18. Implementation
- Single implementation for this route.
- QA status: see `11_qa/VISUAL_QA_MATRIX.csv` (row for this screen).

## 19. Action bindings (contract audit 2026-11-23)
| Action | Kind | Classification | Operation | Confidence | Behaviour |
|---|---|---|---|---|---|
| `vpc-002.show-password` Show / hide password | action | UI_ONLY | — | high | Toggles password visibility locally; announces state |
| `vpc-002.rotate-needs-2nd-approval` Rotate (needs 2nd approval) | action | API_PROPOSED | `rotateProviderCredentials` † | high | Bound by the 2026-11-23 contract audit |
| `vpc-002.test-connection` Test connection | action | API_EXISTING | `post__api_v1_admin_video_providers_providerAccountId_connection_test` | medium | Matched “test” to the operation name |
| `vpc-002.retry` Retry | action | REFETCH | — | high | Re-runs the failed request(s) |
| `vpc-002.reconnect` Reconnect | action | REFETCH | — | high | Re-runs the failed request(s) |

† PROPOSED operation (`07_api/openapi.proposed.yaml`), not approved.
