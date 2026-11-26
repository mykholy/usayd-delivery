# Regression report

Inventory measured from the canvas: **169 product screens + 9 journey boards = 178 boards**.

## Automated cycles after the remediation

| Cycle | Renders | Focus stops | Invisible focus | Findings |
|---|---|---|---|---|
| cycle10 | 4,984 | 0 | 0 | {'overflow': 16} |
| cycle11 | 14,520 | 9,624 | 0 | 0 |
| cycle12 | 14,520 | 9,624 | 0 | 0 |

Matrix per cycle: every board × AR/EN × light/dark × 320/360/390/430/768/1024/1280/1440/1920 px (default state) + every product screen × 6 non-default states (loading, empty, error, no-permission, offline, success) × AR/EN × light/dark × 390/1440 px + keyboard focus pass (14 Tab stops, AR/EN, 390/1440). Reduced motion on. Checks: page overflow, clipped text, targets < 44 px, axe-core WCAG 2.0/2.1/2.2 A+AA, exactly one H1, `href="#"`, focus visibility.

## Other executed checks
- Internal links in AR/EN static exports: **7,572 hrefs, 0 broken** (was 86 broken).
- Slide-to-confirm interaction (real pointer events in Chrome): 16 runs (8 controls × AR/EN) × 8 checks — **16/16 runs pass**
- OpenAPI: baseline 121 operations parsed; `openapi.proposed.yaml` 57 operations — openapi-spec-validator: **valid** (OpenAPI 3.1); JSON-schema/example errors: 0.
- Journeys: 17 walkthroughs, 36 Gherkin scenarios; unknown screens/operations/FRs: 0.
- Action contracts: 641 rows; classes {'LIST_QUERY': 143, 'REFETCH': 338, 'API_PROPOSED': 25, 'DISABLED': 22, 'API_EXISTING': 69, 'UI_ONLY': 39, 'NAVIGATE_AFTER_CONFIRM': 5}.
- FR traceability: 216 FRs; status {'MAPPED': 199, 'screen enhancement': 9, 'backend-only': 5, 'new screen': 1, 'deferred': 1, 'backend-only / design-system rule': 1}.

## Issues (REMEDIATION_BASELINE.csv)
| Severity | Fixed | Proposed (needs approval) | Open |
|---|---|---|---|
| P0 | 0 | 0 | 0 |
| P1 | 8 | 2 | 0 |
| P2 | 9 | 1 | 0 |
| P3 | 5 | 0 | 4 |

## Not verified
- Screen readers (TalkBack, VoiceOver, NVDA) — UNVERIFIED; manual script in A11Y_MANUAL_TEST_SCRIPT.md
- Real devices, safe areas, on-screen keyboard avoidance — UNVERIFIED
- Text-only 200% resize and Windows forced colours — UNVERIFIED (not automated)
- Dialog focus trapping — UNVERIFIED (static exports have no modal runtime)
- Flutter rendering — UNVERIFIED (no Flutter build exists)
- Backend behaviour, payments, video providers — NOT APPLICABLE (no backend exists)
- Human visual sign-off — PENDING (AI visual review only)

## What “PASS” means here
PASS = the static HTML exports passed the automated checks above. It does **not** prove the live web app, Flutter, screen-reader output, backend behaviour or provider integrations.
