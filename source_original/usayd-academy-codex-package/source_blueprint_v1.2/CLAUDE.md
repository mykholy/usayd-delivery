# Claude / Figma design instructions — Smart Quran Academy

Read all `05_UI_UX/` docs and `02_REQUIREMENTS/` before design. Build an **editable Figma file** with real components, variants, auto-layout, variables, assets licenses and named frames; no static images pretending to be editable files. If Figma tooling is unavailable, declare limitation and deliver a fully inspectable editable spec/prototype source. Do not imply integration or actual app behavior from a mockup.

## Design quality
- Arabic RTL first; English LTR; Quran content isolated with verified source text and proper diacritics. Test both directions, compact phones (360), iPhone, tablet (768), desktop (1440).
- Five design surfaces: marketing, learner, teacher, academic supervisor/admin, Flutter mobile. Shared tokens but distinct information density. Premium restrained visual language; no generic AI template look.
- P0 flows first: signup, adult learning and minor consent, assessment, checkout, booking, conference embedded/external, teacher report, revision, support. P1 contests/exams, AI proposals, appeals; P2 mobile.
- Each frame includes states: normal, loading, empty, errors, offline, no permission, consent pending, expired session, payment pending, rescheduled, accessibility focus.
- AI indications are transparent (`اقتراح يحتاج اعتماد`), and competition rankings for minors are private by default.
- Audio analysis indicator must explain what is collected and why; do not depict surveillance as an invisible background feature.
- All dashboards show useful decisions/actions and readable charts, not fake metrics.

## Mandatory deliverables
Figma pages: 00 Foundations, 01 Components, 02 Marketing, 03 Learner, 04 Teacher, 05 Academic/Admin, 06 Contests & Exams, 07 Mobile, 08 Interactive Prototype, 09 Handoff, 10 QA Evidence. For each critical flow deliver clickable links, component variants, desktop/mobile responsive, AR+EN sample, empty/error states, annotations and UX-to-API mapping.

## Work order
1. Choose 2 distinct art directions + evaluate quickly; select one and record design ADR. 2. Semantic tokens and primitives. 3. P0 Critical journeys. 4. Reusable domain components. 5. P1 screens/AI/contests. 6. Mobile. 7. Accessibility/RTL/localization/low-bandwidth design QA. 8. Export file link and QA evidence (only if created).

## Never invent
Accreditation, real student records, real teacher photos or credentials, Quran content from memory, real revenue claims or resolved user permissions. Use clearly labeled fictional data.


## v1.2 design source of truth
Read `13_PREMIUM_UX/CLAUDE_FIGMA_FINAL_BRIEF.md`, `13_PREMIUM_UX/DESIGN_DIRECTION_AND_UI_SPEC.md`, `13_PREMIUM_UX/SCREEN_SPECS_v1.2.md`, `10_GLOBALIZATION/*`, `11_PLATFORM_ADMIN/*`, `12_USER_JOURNEYS/diagrams/*` and full `05_UI_UX/screen_inventory.csv`. Build *editable* Figma tokens/components/screens AR/EN RTL/LTR with responsive Flutter flows; do not claim generated Figma unless actually created. No fake customer/teacher data, no unlicensed Quran text. Provider settings, money/DST and supervisor portals must match detailed functional states.
