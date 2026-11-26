# Implementation roadmap (module by module)

Codex builds the production system in this order. Each module is “done” only with: screens matching the design at 1440/768/390 in AR+EN, API implemented per OpenAPI (+ reviewed additions), server-side authorization, audit events, all states (loading/empty/error/no-permission/offline/success), automated tests (unit + API + E2E for the module’s journeys), and accessibility checks.

| # | Module | Screens | Key FR | Exit criteria |
|---|---|---|---|---|
| 0 | Foundations | design tokens, `usayd-ui` components, app shells, i18n (ar/en), theming, error codes, auth skeleton | FR-I18N-*, FR-SEC-* | Component library + Storybook/visual tests in AR/EN light/dark; RTL snapshot tests |
| 1 | Identity, consent, markets | UX-AUTH-001..005, UX-GLOB-001..004, UX-PUBLIC-012 | FR-IAM-001..010, FR-GEO-001..004, FR-PROF-* | Minor limited mode enforced server-side; locale/country/timezone independent |
| 2 | Public website | UX-PUBLIC-001..011, UX-GLOB-002/003 | FR-GEO-016, FR-CURR-001 | SEO routes per locale, honest content placeholders, price from price book |
| 3 | Pricing, checkout, subscriptions | UX-GLOB-006/007, UX-LEARNER-029, UX-ADMIN-019/020, UX-GLOB-012..015 | FR-PAY-*, FR-GEO-005..015 | Immutable quotes, idempotent checkout, webhook-only confirmation, dual-approved price books |
| 4 | Scheduling & time | UX-LEARNER-004..009, UX-GLOB-005, UX-TEACHER-002..005, UX-GLOB-008/009, UX-ADMIN-010/015, UX-GLOB-016 | FR-BOOK-*, FR-TIME-* | UTC storage, DST ambiguity UI, collision lock across markets, ICS |
| 5 | Video & classroom | UX-VPC-001..010, UX-LEARNER-010, UX-TEACHER-006, UX-ADMIN-016..018 | FR-VIDEO-*, FR-VPC-*, FR-ATT-* | Provider adapter, capability matrix, routing dry-run + dual approval, failure recovery |
| 6 | Learning core | UX-LEARNER-001/002/011..016/026/028/030..032, UX-TEACHER-007..011, UX-ENG-002/003 | FR-PLAN-*, FR-ASMT-001/002/008, FR-MEDIA-* | Teacher-approved plans/reports, memory map from verified evidence only |
| 7 | Exams | UX-LEARNER-017..019, UX-TEACHER-012, UX-ADMIN-013/014 | FR-ASMT-003..007 | Server timer, autosave with versions, accommodations |
| 8 | Competitions | UX-LEARNER-020..025, UX-ENG-001, UX-TEACHER-013..015, UX-ADMIN-025..032, UX-SUP-005 | FR-CONTEST-*, FR-ENG-* | Eligibility server-side, double judging, appeals with score versions, minor privacy |
| 9 | AI (gated) | UX-LEARNER-027, UX-ADMIN-023/024 | FR-AI-* | Eval gates, consent receipts, provenance, never Quran text generation |
| 10 | Supervisors & admin governance | UX-SUP-001..011, UX-ADMIN-001..009/011/012/021/022/033..041 | FR-SUP-*, FR-ADMIN-*, FR-PAYROLL-*, FR-CRM-* | Scoped access, no self-approval, break-glass review, audit trail |
| 11 | Flutter mobile | UX-MOBILE-001..011, UX-GLOB-017 | FR-MOB-* | Same API, offline drafts, reconnect, push with quiet hours |

Blocked until decisions: legal entity & markets (O-01), prices (O-02), video vendor PoC (O-03), minor verification (O-04), recording/AI consent (O-05), Quran source licence (O-06), prizes (O-07), payroll legal review (O-08).
