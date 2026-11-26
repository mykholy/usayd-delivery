# Audit & completion checklist

## 1. Audit of what existed before this pass
- **Figma file** (`z5MGNpTCoAq4QvxV2SpJrQ`): tokens, 30 text styles, 101 icons, ~25 component sets. **0 screens** — stopped by the Figma Starter MCP limit. No further Figma reads were used (as requested).
- **Previously completed screens:** none (0/160). Brand, logo, colours, typography and decisions D-01…D-15 were preserved and carried into the canvas.
- **Now:** 169/169 product screens + 9 journey boards designed on the Claude Design canvas `https://claude.ai/artifact/NbQqBpDmhpBbY9Cvp5VHTR` + static HTML exports (AR/EN) in `01_design/html`.

## 2. Duplicates / overlaps found in the inventory (design once, implement once)
| Screen | Overlaps with | Resolution |
|---|---|---|
| `UX-PUBLIC-004` Pricing | UX-GLOB-002 | Canonical route implemented once; this ID kept as variant/alias for traceability |
| `UX-LEARNER-003` Programs Discover | UX-PUBLIC-002 (catalogue component shared) | Canonical route implemented once; this ID kept as variant/alias for traceability |
| `UX-LEARNER-005` Teachers Discover | UX-PUBLIC-005 (shared teacher card) | Canonical route implemented once; this ID kept as variant/alias for traceability |
| `UX-ADMIN-017` Conference Provider Registry | UX-VPC-001 | Canonical route implemented once; this ID kept as variant/alias for traceability |
| `UX-ADMIN-041` Settings & Feature Flags | UX-SUP-010 | Canonical route implemented once; this ID kept as variant/alias for traceability |
| `UX-TEACHER-003` Availability | `UX-GLOB-008` editor | Overview vs detailed editor (both designed) |
| `UX-TEACHER-005` Lesson briefing | `UX-GLOB-009` dual-zone details | Briefing vs time-detail (both designed) |
| `UX-ADMIN-005` Staff | `UX-SUP-008` Role scopes | Overview vs assignment (both designed) |
| `UX-ADMIN-040` Audit | `UX-SUP-009` Access audit | Global audit vs privileged-access review |

## 3. Incomplete / unresolved
- 27 UI operations missing from OpenAPI (see `07_api/API_CONTRACTS.md` → UNRESOLVED).
- 19 functional requirements have no UI screen (backend-only or gap): FR-IAM-010, FR-CURR-004, FR-CURR-005, FR-BOOK-007, FR-BOOK-008, FR-PAY-008, FR-ASMT-004, FR-CONTEST-004, FR-MEDIA-003, FR-CRM-006, FR-ADMIN-009, FR-SEC-002, FR-SEC-003, FR-SEC-007, FR-SEC-008, FR-GEO-012, FR-I18N-002, FR-VPC-007, FR-SUP-012.
- Open decisions O-01…O-10 and per-screen items: `05_requirements/UNRESOLVED.md`.
- Real content pending: prices, legal texts, teacher bios/photos (with rights), licensed Quran text and font approval, certificate artwork, mascot «شبل».

## 4. Validation performed
- Structural (every screen): balanced HTML, all bilingual keys present in AR and EN, no Arabic in EN strings / no untranslated AR strings (technical IDs exempt), all links resolve to existing artboards, no orphan screens, every screen has all 7 states (default, loading, empty, error, no-permission, offline, success).
- Responsive (every screen, static export, headless Chrome): AR + EN at 1440 and 390 (mobile frames at 390) — 0 elements overflowing the viewport outside scroll containers, 0 clipped buttons/chips/nav items.
- Visual spot-check: UX-PUBLIC-001 (AR), UX-LEARNER-001 (AR/EN), UX-MOBILE-002, UX-TEACHER-006 @390. **Not done:** a human visual review of all 169 screens, screen-reader testing, and colour-contrast measurement on every rendered combination.

## 5. Completion checklist (169)
| # | Screen | Designed | AR | EN | States | Links OK | Responsive check | Spec | Open items |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `UX-PUBLIC-001` Marketing Home | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-001.md) | — |
| 2 | `UX-PUBLIC-002` Programs Directory | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-002.md) | — |
| 3 | `UX-PUBLIC-003` Program Detail | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-003.md) | — |
| 4 | `UX-PUBLIC-004` Pricing | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-004.md) | ⚠️ |
| 5 | `UX-PUBLIC-005` Teacher Directory | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-005.md) | — |
| 6 | `UX-PUBLIC-006` Teacher Public Profile | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-006.md) | ⚠️ |
| 7 | `UX-PUBLIC-007` How It Works | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-007.md) | — |
| 8 | `UX-PUBLIC-008` Competition Landing | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-008.md) | — |
| 9 | `UX-PUBLIC-009` Free Assessment Booking | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-009.md) | — |
| 10 | `UX-PUBLIC-010` About/Academic Standards | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-010.md) | ⚠️ |
| 11 | `UX-PUBLIC-011` FAQ & Support | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-011.md) | — |
| 12 | `UX-PUBLIC-012` Legal & Consents | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-PUBLIC-012.md) | ⚠️ |
| 13 | `UX-AUTH-001` Unified Signup | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-AUTH-001.md) | — |
| 14 | `UX-AUTH-002` Guardian Consent Step | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-AUTH-002.md) | ⚠️ |
| 15 | `UX-AUTH-003` Login | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-AUTH-003.md) | — |
| 16 | `UX-AUTH-004` Password Recovery | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-AUTH-004.md) | ⚠️ |
| 17 | `UX-AUTH-005` Welcome Onboarding | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-AUTH-005.md) | — |
| 18 | `UX-LEARNER-001` Learner Home | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-001.md) | — |
| 19 | `UX-LEARNER-002` My Learning Profile | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-002.md) | — |
| 20 | `UX-LEARNER-003` Programs Discover | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-003.md) | — |
| 21 | `UX-LEARNER-004` Initial Assessment | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-004.md) | — |
| 22 | `UX-LEARNER-005` Teachers Discover | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-005.md) | — |
| 23 | `UX-LEARNER-006` Teacher Detail | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-006.md) | — |
| 24 | `UX-LEARNER-007` Calendar | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-007.md) | — |
| 25 | `UX-LEARNER-008` Booking Wizard | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-008.md) | — |
| 26 | `UX-LEARNER-009` Lesson Detail | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-009.md) | — |
| 27 | `UX-LEARNER-010` Classroom | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-010.md) | — |
| 28 | `UX-LEARNER-011` Post-Lesson Report | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-011.md) | — |
| 29 | `UX-LEARNER-012` Learning Plan | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-012.md) | — |
| 30 | `UX-LEARNER-013` Daily Study | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-013.md) | — |
| 31 | `UX-LEARNER-014` Revision Queue | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-014.md) | — |
| 32 | `UX-LEARNER-015` Memory Map | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-015.md) | — |
| 33 | `UX-LEARNER-016` Practice Recording | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-016.md) | ⚠️ |
| 34 | `UX-LEARNER-017` Exam Catalog | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-017.md) | — |
| 35 | `UX-LEARNER-018` Exam Taking | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-018.md) | — |
| 36 | `UX-LEARNER-019` Exam Results | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-019.md) | — |
| 37 | `UX-LEARNER-020` Competitions Discover | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-020.md) | — |
| 38 | `UX-LEARNER-021` Competition Detail | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-021.md) | — |
| 39 | `UX-LEARNER-022` Competition Preparation | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-022.md) | — |
| 40 | `UX-LEARNER-023` Competition Round | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-023.md) | — |
| 41 | `UX-LEARNER-024` Competition Standings | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-024.md) | — |
| 42 | `UX-LEARNER-025` Competition Result & Appeal | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-025.md) | — |
| 43 | `UX-LEARNER-026` Achievements | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-026.md) | — |
| 44 | `UX-LEARNER-027` AI Study Assistant | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-027.md) | — |
| 45 | `UX-LEARNER-028` Course Library | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-028.md) | ⚠️ |
| 46 | `UX-LEARNER-029` Subscription & Billing | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-029.md) | — |
| 47 | `UX-LEARNER-030` Notifications | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-030.md) | ⚠️ |
| 48 | `UX-LEARNER-031` Support and Reports | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-031.md) | — |
| 49 | `UX-LEARNER-032` Account Settings | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-LEARNER-032.md) | — |
| 50 | `UX-TEACHER-001` Teacher Login & Onboarding | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-001.md) | ⚠️ |
| 51 | `UX-TEACHER-002` Teacher Home | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-002.md) | — |
| 52 | `UX-TEACHER-003` Availability | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-003.md) | — |
| 53 | `UX-TEACHER-004` Teaching Calendar | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-004.md) | — |
| 54 | `UX-TEACHER-005` Lesson Briefing | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-005.md) | — |
| 55 | `UX-TEACHER-006` Teacher Classroom | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-006.md) | — |
| 56 | `UX-TEACHER-007` Lesson Report Editor | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-007.md) | — |
| 57 | `UX-TEACHER-008` My Assigned Learners | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-008.md) | ⚠️ |
| 58 | `UX-TEACHER-009` Learner Academic Detail | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-009.md) | — |
| 59 | `UX-TEACHER-010` Assessment Workspace | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-010.md) | — |
| 60 | `UX-TEACHER-011` Plan Review Queue | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-011.md) | — |
| 61 | `UX-TEACHER-012` Question Bank Review | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-012.md) | ⚠️ |
| 62 | `UX-TEACHER-013` Contests Assigned | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-013.md) | — |
| 63 | `UX-TEACHER-014` Contest Judging | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-014.md) | — |
| 64 | `UX-TEACHER-015` Appeals Academic Review | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-015.md) | — |
| 65 | `UX-TEACHER-016` Teacher Pay Statements | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-016.md) | — |
| 66 | `UX-TEACHER-017` Teacher Support | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-017.md) | — |
| 67 | `UX-TEACHER-018` Teacher Account & Consent | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-TEACHER-018.md) | — |
| 68 | `UX-ADMIN-001` Executive Dashboard | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-001.md) | — |
| 69 | `UX-ADMIN-002` Learner Directory | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-002.md) | ⚠️ |
| 70 | `UX-ADMIN-003` Learner 360 | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-003.md) | — |
| 71 | `UX-ADMIN-004` Guardian Consent Queue | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-004.md) | ⚠️ |
| 72 | `UX-ADMIN-005` Staff & Permissions | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-005.md) | — |
| 73 | `UX-ADMIN-006` Teacher Recruitment | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-006.md) | ⚠️ |
| 74 | `UX-ADMIN-007` Teacher Management | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-007.md) | ⚠️ |
| 75 | `UX-ADMIN-008` Teacher Profile Admin | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-008.md) | ⚠️ |
| 76 | `UX-ADMIN-009` Teacher Contract Builder | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-009.md) | ⚠️ |
| 77 | `UX-ADMIN-010` Teacher Shift Planner | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-010.md) | — |
| 78 | `UX-ADMIN-011` Programs CMS | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-011.md) | — |
| 79 | `UX-ADMIN-012` Quran Content Sources | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-012.md) | ⚠️ |
| 80 | `UX-ADMIN-013` Question Bank Manager | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-013.md) | ⚠️ |
| 81 | `UX-ADMIN-014` Assessment Rubrics | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-014.md) | ⚠️ |
| 82 | `UX-ADMIN-015` Bookings Operations | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-015.md) | ⚠️ |
| 83 | `UX-ADMIN-016` Live Lessons Monitor | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-016.md) | ⚠️ |
| 84 | `UX-ADMIN-017` Conference Provider Registry | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-017.md) | — |
| 85 | `UX-ADMIN-018` Attendance & Makeups | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-018.md) | — |
| 86 | `UX-ADMIN-019` Payments & Invoices | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-019.md) | — |
| 87 | `UX-ADMIN-020` Packages & Promotions | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-020.md) | — |
| 88 | `UX-ADMIN-021` Payroll Calculations | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-021.md) | ⚠️ |
| 89 | `UX-ADMIN-022` Payroll Approval | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-022.md) | — |
| 90 | `UX-ADMIN-023` AI Learning Control | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-023.md) | — |
| 91 | `UX-ADMIN-024` Session Policy Review | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-024.md) | — |
| 92 | `UX-ADMIN-025` Competition Templates | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-025.md) | ⚠️ |
| 93 | `UX-ADMIN-026` Contest Builder Wizard | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-026.md) | ⚠️ |
| 94 | `UX-ADMIN-027` Competitions List | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-027.md) | ⚠️ |
| 95 | `UX-ADMIN-028` Competition Control Room | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-028.md) | — |
| 96 | `UX-ADMIN-029` Judge Assignments | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-029.md) | ⚠️ |
| 97 | `UX-ADMIN-030` Leaderboard & Publish | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-030.md) | — |
| 98 | `UX-ADMIN-031` Contest Appeals | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-031.md) | — |
| 99 | `UX-ADMIN-032` Contest Rewards & Certificates | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-032.md) | ⚠️ |
| 100 | `UX-ADMIN-033` CRM Pipeline | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-033.md) | ⚠️ |
| 101 | `UX-ADMIN-034` Campaign Analytics | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-034.md) | — |
| 102 | `UX-ADMIN-035` Support Center | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-035.md) | — |
| 103 | `UX-ADMIN-036` Safeguarding Incident Queue | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-036.md) | — |
| 104 | `UX-ADMIN-037` Recorded Content Library | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-037.md) | ⚠️ |
| 105 | `UX-ADMIN-038` Notification Center | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-038.md) | — |
| 106 | `UX-ADMIN-039` Reports and KPI Explorer | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-039.md) | — |
| 107 | `UX-ADMIN-040` Audit Trail | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-040.md) | — |
| 108 | `UX-ADMIN-041` Settings & Feature Flags | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ADMIN-041.md) | — |
| 109 | `UX-GLOB-001` Country & Currency Selector | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-001.md) | — |
| 110 | `UX-GLOB-002` Localized Pricing Comparison | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-002.md) | — |
| 111 | `UX-GLOB-003` Unavailable Country & Waitlist | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-003.md) | ⚠️ |
| 112 | `UX-GLOB-004` Language & Regional Preferences | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-004.md) | — |
| 113 | `UX-GLOB-005` Timezone Preview & DST Warning | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-005.md) | — |
| 114 | `UX-GLOB-006` Regional Checkout Quote | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-006.md) | — |
| 115 | `UX-GLOB-007` Renewal Price Change Notice | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-007.md) | ⚠️ |
| 116 | `UX-GLOB-008` Timezone Availability Editor | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-008.md) | — |
| 117 | `UX-GLOB-009` Cross Timezone Lesson Details | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-009.md) | — |
| 118 | `UX-GLOB-010` Markets Overview | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-010.md) | — |
| 119 | `UX-GLOB-011` Market Launch Wizard | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-011.md) | ⚠️ |
| 120 | `UX-GLOB-012` Country Pricing Matrix | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-012.md) | — |
| 121 | `UX-GLOB-013` Price Approval & Version Diff | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-013.md) | — |
| 122 | `UX-GLOB-014` Merchant Profiles | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-014.md) | — |
| 123 | `UX-GLOB-015` FX Reporting & Settlement | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-015.md) | — |
| 124 | `UX-GLOB-016` Regional Schedule Dashboard | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-016.md) | — |
| 125 | `UX-GLOB-017` Flutter Region & Language | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-GLOB-017.md) | — |
| 126 | `UX-VPC-001` Video Providers Overview | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-001.md) | — |
| 127 | `UX-VPC-002` Video Provider Credentials | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-002.md) | — |
| 128 | `UX-VPC-003` Video Provider Capabilities | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-003.md) | — |
| 129 | `UX-VPC-004` Video Routing Rules | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-004.md) | — |
| 130 | `UX-VPC-005` Video Switch Impact & Dry-run | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-005.md) | — |
| 131 | `UX-VPC-006` Video Routing Approval | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-006.md) | — |
| 132 | `UX-VPC-007` Video Provider Monitoring | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-007.md) | — |
| 133 | `UX-VPC-008` Video Failover Incident Console | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-008.md) | — |
| 134 | `UX-VPC-009` Embedded vs External Prejoin | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-009.md) | — |
| 135 | `UX-VPC-010` Teacher Provider Join Health | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-VPC-010.md) | — |
| 136 | `UX-SUP-001` Supervisor Home | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-001.md) | — |
| 137 | `UX-SUP-002` Academic Plans Approval | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-002.md) | — |
| 138 | `UX-SUP-003` Quality Observation Queue | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-003.md) | — |
| 139 | `UX-SUP-004` Safeguarding Case Console | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-004.md) | ⚠️ |
| 140 | `UX-SUP-005` Competition Moderation | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-005.md) | — |
| 141 | `UX-SUP-006` Operations Coverage Board | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-006.md) | — |
| 142 | `UX-SUP-007` Regional KPI & Enrollment | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-007.md) | — |
| 143 | `UX-SUP-008` Role Assignments & Scopes | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-008.md) | — |
| 144 | `UX-SUP-009` Audit and Break-glass Review | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-009.md) | ⚠️ |
| 145 | `UX-SUP-010` Settings Registry | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-010.md) | — |
| 146 | `UX-SUP-011` Localization Content Studio | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-SUP-011.md) | — |
| 147 | `UX-ENG-001` Competition Localized Schedule | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ENG-001.md) | — |
| 148 | `UX-ENG-002` Adaptive Practice Brief | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ENG-002.md) | — |
| 149 | `UX-ENG-003` Gentle Progress & Streak Recovery | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-ENG-003.md) | — |
| 150 | `UX-MOBILE-000` Flutter Splash (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-000.md) | ⚠️ |
| 151 | `UX-MOBILE-001` Flutter Login | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-001.md) | — |
| 152 | `UX-MOBILE-002` Flutter Today | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-002.md) | — |
| 153 | `UX-MOBILE-003` Flutter Classroom | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-003.md) | — |
| 154 | `UX-MOBILE-004` Flutter Schedule | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-004.md) | — |
| 155 | `UX-MOBILE-005` Flutter Memory Map | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-005.md) | — |
| 156 | `UX-MOBILE-006` Flutter AI Coach | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-006.md) | — |
| 157 | `UX-MOBILE-007` Flutter Exam | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-007.md) | — |
| 158 | `UX-MOBILE-008` Flutter Competition | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-008.md) | — |
| 159 | `UX-MOBILE-009` Flutter Teacher Today | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-009.md) | — |
| 160 | `UX-MOBILE-010` Flutter Teacher Report | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-010.md) | — |
| 161 | `UX-MOBILE-011` Flutter Account | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-011.md) | — |
| 162 | `UX-MOBILE-012` App style chooser (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-012.md) | — |
| 163 | `UX-MOBILE-K02` Kids · Today mission (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-K02.md) | — |
| 164 | `UX-MOBILE-K05` Kids · My path (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-K05.md) | — |
| 165 | `UX-MOBILE-K08` Kids · My stars (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-K08.md) | ⚠️ |
| 166 | `UX-MOBILE-K11` Kids · Me (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-K11.md) | ⚠️ |
| 167 | `UX-MOBILE-S02` Simple · Today (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-S02.md) | — |
| 168 | `UX-MOBILE-S04` Simple · My lessons (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-S04.md) | — |
| 169 | `UX-MOBILE-S11` Simple · Help (added) | ✅ | ✅ | ✅ | ✅ 7/7 | ✅ | ✅ | [md](../03_screens/screens/UX-MOBILE-S11.md) | — |
