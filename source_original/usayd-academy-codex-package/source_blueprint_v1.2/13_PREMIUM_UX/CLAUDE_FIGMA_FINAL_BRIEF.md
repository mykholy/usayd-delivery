# Claude/Figma production design master brief — paste after attaching full v1.2 archive
You are Lead Product Designer and Design Systems Architect designing a **premium bilingual Arabic/English Quran learning academy**, with web and Flutter mobile. DO NOT deliver just mockups or uneditable image screenshots. Create real editable Figma frames/components/variables/prototypes if you have Figma tool access; if not available, output a structured handoff, Figma-ready token JSON, frame metadata, and exact steps rather than falsely saying it was done.

## Read order (obligatory)
1. `00_START_HERE/FINAL_HANDOFF_v1.2.md`
2. `05_UI_UX/UX_MASTER_SPEC.md`, `05_UI_UX/DESIGN_SYSTEM.md`, `05_UI_UX/figma_tokens.json`
3. `13_PREMIUM_UX/DESIGN_DIRECTION_AND_UI_SPEC.md`, `13_PREMIUM_UX/SCREEN_SPECS_v1.2.md`
4. `05_UI_UX/screen_inventory.csv` (all old and new screens), `05_UI_UX/SCREEN_DETAILED_SPECS.md`
5. `12_USER_JOURNEYS/FLOW_MATRIX.md`, `12_USER_JOURNEYS/USER_STORIES_AND_ACCEPTANCE.md` and `12_USER_JOURNEYS/diagrams/`
6. `11_PLATFORM_ADMIN/VIDEO_PROVIDER_CONSOLE.md`, `11_PLATFORM_ADMIN/SUPERVISOR_RBAC_WORKFLOWS.md`, `10_GLOBALIZATION/*`
7. `04_ENGINEERING/openapi.yaml`, `07_QUALITY_SECURITY/*`.

## Deliverable structure
Figma pages 00-16 as specified. Use semantic color/type/spacing/radius/elevation tokens, scalable components (variants/states), Auto Layout, constraints and reusable patterns. Create desktop web, responsive tablet/phone, and Flutter native screens. No generic dashboard template. Use meaningful icons and restrained premium Quran-inspired aesthetic. AR RTL / EN LTR for **every core journey**, not just landing page.

## Screens must cover
Public: localized homepage, programs, price comparison and market selector, onboarding, assessment signup, country availability, legal/consent.
Learner: onboarding, goals, dashboard, Quran reader, active lesson, teacher booking, history, plan, AI practice, reviews, exams, competition/challenges/leaderboards, invoices, preferences country/language/timezone.
Teacher: weekly local shift, booking approvals, classroom, lesson report and learning plan, payroll preview and attendance disputes.
Supervisors: academic approval, quality, safeguarding restricted case, regional operations, competition judging and appeals, scoped KPI.
Admin: markets, price books version diff, merchant settlement, country availability, provider registry / secret masking / health / capability / route dry-run / approval / rollback, role scope tree, localization admin, audit.
Mobile Flutter: all core learner flows and teacher subset, custom classroom and external meeting mode, device permissions, offline states, timezone locale controls.

## Interaction fidelity
Mandatory clickable flows: change locale independent of country; price by market; regional payment quote; ambiguous DST time choice; teacher schedule collision; provider switch with safe approvals; Zoom/Meet external fallback; consent-based AI analysis; competition score appeal; supervisor approval with scope denial; mobile offline study draft and reconnect. Draw icons and provide color text not color-only status. Verify Arabic shaping and responsive Bidi numerals.

## Required handoff per screen
`Screen ID` / role / state / breakpoint / locale / source data/API ID / user action / validation / loading+empty+error / accessibility considerations / export component reference / feature-flag condition. Include textual sample content that is honest and not fake user/customer data.

## Quality bar
- Figma editable, pixel-polished consistent 8px rhythm, no clipped text, accessible touch areas, high-quality Arabic text and adequate Quran line-height.
- Test English and Arabic in real narrow viewport; long labels; KWD 3 decimals; teacher vs student time zone; unavailable markets and no permissions.
- Provide screenshot proof + component link + variant map, do not claim tool artifact unless created.
- Log missing source assets or approved Quran font licensing; do not invent brand identity as "final approved".

## Work execution
Plan component foundations → critical E2E journeys → remaining screens by persona → responsive/language variants → prototype → dev handoff → QA. Report phase completion only with actual Figma links/frame IDs and reviewed exports. Export tokens and icon inventory under a defined version.
