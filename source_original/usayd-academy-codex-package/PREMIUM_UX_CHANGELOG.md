# Premium UX remediation — v0.5 (2026-11-21)

Source of the brief: `CLAUDE_PREMIUM_FIX_PROMPT.md`, `AUDIT_REPORT_AR.md` and `SCREEN_BY_SCREEN_AUDIT_160.csv`. The brand and all original 160 screen IDs and routes are unchanged (169 product screens today, after the documented additions). One screen was added earlier (`UX-MOBILE-000`, D-16).

## A · Design system
- **Contrast:**
  - `--tx3` is now #655F53 in light and #A39D91 in dark.
  - Every text token passes ≥ 4.5:1 on every surface (page, raised, subtle, sunken) in both themes. The check runs as code, in `palette.py`.
  - Danger buttons in dark use dark text.
  - The gold brand sub-line is no longer used on parchment.
- **Touch targets:** small buttons, icon buttons, segments, sidebar nav, tabs, standalone links, footer and header links are all ≥ 44×44 px. Verified on every render.
- **Semantics:**
  - Every screen has one H1 and no skipped heading levels. Card titles are H2.
  - A skip link is on every screen.
  - Scroll regions are focusable and named. Progress bars are named.
  - Language buttons use their visible text as the accessible name.
  - Tabs use tablist only when they really are tabs.
- **No inert controls:**
  - 0 `href="#"`.
  - Every in-place control is a `<button>` with an `action_id`. There are 641 contracts, in `ACTION_CONTRACTS.csv` and §14 of each spec.
- **Mobile:**
  - Tables become stacked records under 760 px. Calendars become agenda lists.
  - The top bar collapses to one row, and the auth panel collapses to a brand strip.
  - Public pages get a sticky primary action.
- **Status semantics:**
  - Disabled, locked, pending and denied now differ in shape and icon, not only colour.
  - Denied and offline copy is specific to each role and module. Out-of-scope records use non-revealing copy.

## B · Content honesty
- Bracket placeholders are now typed slots:
  - **owner content (CONTENT_REQUIRED)**, amber and labelled, 39 slots;
  - **runtime sample data**, dotted underline, 316 slots.
- Teacher avatars on public pages are photo slots, never stock faces.
- The testimonials section is a consent-gated slot, hidden in production.
- Prices stay owner content until O-02 is closed. No “free” claim.

## C · Role-specific hierarchy
- **Admin overview:** exceptions first, then the data source and timestamp, a partial-data flag, and proposed KPI definitions with a drill-down link.
- **Teacher day:** the next class comes first, with Start and Prep.
- **Supervisor queue:** the over-SLA item comes first, with an audit note.

## D · Critical journeys
- 9 state-model boards (`UX-JR-01..09`) cover success, cancel, retry, timeout, offline, server validation, permission, duplicate and irreversible confirmation.
- Role steps are separate sessions.
- Spec: `04_flows/JOURNEYS.md` (with mermaid state diagrams).

## E · Specs
- Every screen spec now has analytics events, action contracts, content slots, themes and breakpoints, acceptance criteria and its canonical implementation.
- New documents:
  - `07_api/API_GAPS.md`: 27 missing operations with PROPOSED payloads.
  - `05_requirements/FR_GAPS.md`: the 19 FRs, classified.
  - `DECISION_LOG.md`
  - `IMPLEMENTATION_GATES.md`

## F · Portable export
- Fonts are bundled locally (OFL, woff2, with licence file).
- Static AR/EN exports no longer load Google Fonts, `support.js` or private blob URLs. Theme switches with `?theme=dark`.
- Prototype-only blocks (spec bar, related-screen links) are stripped from the exports.

## QA
See `11_qa/QA_SUMMARY.md` and `11_qa/SCREEN_VISUAL_QA_160.csv`. **Human visual sign-off and screen-reader testing are still pending.**
