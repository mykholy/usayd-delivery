# Decision log

## Design decisions
| ID | Decision | Why | Status |
|---|---|---|---|
| D-01..D-15 | Earlier design decisions (brand, tokens, AI colour, focus ring, no Quran from memory, Usayd spelling, no “free”) | See `00_AUDIT_AND_CHECKLIST.md` history | Accepted |
| D-16 | Added `UX-MOBILE-000` splash screen (owner request); not in blueprint inventory | Owner request 2026-11-21 | Needs owner confirmation |
| D-17 | Colour v0.4: refined light + rebuilt dark; every text token ≥ 4.5:1 on every surface (verified) | Audit HIGH-03 | Accepted |
| D-18 | All interactive targets ≥ 44×44 px (sm buttons, icon buttons, segments, nav, tabs, standalone links) | Project rule + audit HIGH-03 | Accepted |
| D-19 | Tables become stacked records and calendars become agenda lists below 760 px | Audit HIGH-04 | Accepted |
| D-20 | In-place controls are `<button>`s with an `action_id` and a documented contract; no `href="#"` anywhere | Audit HIGH-07 | Accepted |
| D-21 | Placeholders split into **owner content** (CONTENT_REQUIRED, hidden in production until supplied) and **runtime sample data** (dotted underline in design) | Prompt rule 1 | Accepted |
| D-22 | No-permission copy is role-specific; out-of-scope records use non-revealing copy | Prompt rule 3 | Accepted |
| D-23 | Critical journeys are drawn as state models (`UX-JR-01..09`) separate from screen links; each role step is its own session | Audit HIGH-05 | Accepted |
| D-24 | Duplicate routes map to one implementation; aliases are PROPOSED redirects that need review | Audit §6.8 | Needs review |
| D-25 | Fonts bundled locally (OFL) for offline builds; static exports no longer depend on Google Fonts, `support.js` or private blob URLs | Audit HIGH-06 | Accepted |
| D-26 | Testimonials section exists only as a consent-gated slot; hidden in production until real, consented content exists | Prompt §B | Accepted |
| D-27 | KPI definitions on `UX-ADMIN-001` are proposals and labelled as such | Prompt §C | Needs owner approval |
| D-28 | Mobile shell = night header with circular glass controls + rounded parchment sheet (28 px); hero on login and today; same pattern for auth below 760 px | Owner reference (premium app pattern) | Accepted |
| D-29 | Glass buttons: frosted secondary on light, translucent on night; primary/accent get glossy inner highlights. Pill shape on mobile only; web keeps 14 px radius | Owner request | Accepted |
| D-30 | Slide-to-confirm only for important/irreversible actions (8 places), with a tap-twice/keyboard alternative (WCAG 2.5.7) | Owner request | Accepted |
| D-31 | Icon fields (leading icon by type, 52 px, password reveal), avatar stacks (initials only) and a large amount display | Owner request (modern components) | Accepted |
| D-32 | State titles are the page H1 when a state replaces the content (demoted to H2 under a mobile header/hero H1) | Audit cycle 2 | Accepted |
| D-33 | No duplicate sticky CTA on pricing pages; scroll-padding keeps focused elements clear of sticky bars | Audit cycle 3 | Accepted |
| D-34 | Age-adaptive learner app: Kids / Professional / Simple modes (8 added screens: UX-MOBILE-012, K02, K05, K08, K11, S02, S04, S11); app only | Owner request 2026-11-22 | Accepted |
| D-35 | Proposed default ranges: Kids 6–12, Professional 13–59 (minor protections on for 13–17), Simple 60+; mode is a changeable preference | Design proposal | Needs owner approval |
| D-36 | Kids badges: private, non-monetary, teacher-awarded; catalogue and rules | Design proposal | Needs academic approval |
| D-37 | Kids cartoon graphics: original flat set, thick outlines, no faces of people/animals; any mascot with a face needs owner approval | Owner request 2026-11-22 | Accepted (mascot: needs owner decision) |
| D-38 | No “Request access” button anywhere (no access-request API or FR exists): no-permission states route to the role home or support. Success copy matches the screen: read-only screens say “This view is up to date”; write screens say “Your changes were saved” | Remediation audit 2026-11-23 (§D, §F) | Accepted (design fix) |
| D-39 | Break-glass access to safeguarding cases is a PROPOSED operation (`postBreakGlassGrant`) behind a disabled control; needs security/safeguarding policy (who, how long, review SLA) | Remediation audit 2026-11-23 | Needs owner approval |
| D-40 | Operational lists (OPEN-01): status summary strip, exception lane, sortable headers (`aria-sort`), cursor pagination with no total count unless the API returns one, no bulk actions without an API | Audit HIGH-02 / OPEN-01 | Accepted (design, reversible) |
| D-41 | Slide-to-confirm is interactive in the static AR/EN exports (pointer drag ≥ 90%, release/cancel reset, tap-twice, Enter-twice, Esc, 5 s disarm, live announcement). The Claude Design canvas keeps the CSS demonstration only | OPEN-02 | Accepted |
| D-42 | Admin/teacher list and detail endpoints are separate from public ones (`/admin/...`, `/teachers/me/...`) so private fields never leak through public operations | API reconciliation 2026-11-23 | Proposed — needs tech lead approval |
| D-43 | Kids badges read from the existing `GET /api/v1/achievements` (Achievement.type) instead of a new `/me/badges`; catalogue still needs D-36 | API reconciliation 2026-11-23 | Proposed — needs tech lead approval |
| D-44 | Brand tagline «اقرأ بصوتٍ تدنو له الملائكة» alludes to the authentic narration about Usayd ibn Hudayr; it is a brand line, not a citation. Any quoted hadith text with a reference (e.g. on About) is owner content approved by the academic board | Remediation audit 2026-11-23 (§B) | Needs academic approval |

## Open owner decisions (from the blueprint) — still open
| ID | Decision | Owner | Design impact |
|---|---|---|---|
| O-01 | Commercial legal entity and eligible geographies | Legal/CEO | Legal pages, market list, checkout |
| O-02 | Initial pricing tiers and currency | Commercial | All prices (shown as owner-content slots), “free assessment” wording |
| O-03 | P0 in-app conferencing vendor | CTO | VPC defaults, lesson room |
| O-04 | Which minors can enroll; parent verification process | Legal | UX-AUTH-002, UX-JR-02, minors limited mode |
| O-05 | Recording + AI processing purposes & consent | Legal/DPO | Recording toggles (off), AI audio analysis (off) |
| O-06 | Academic supervisor and Quran content rights | Academic/Legal | Every Quran text block (placeholder only) |
| O-07 | Prize policy for contests | Legal/Academic | Rewards, contest pages |
| O-08 | Payroll contract forms and minimum wages | Finance/Legal | Teacher contracts and pay statements |
| O-09 | Support hours and staff | Ops | Support SLAs shown to users |
| O-10 | Funding amount and tranche | Investors | Scope of the first release |

None of the open decisions were assumed. Screens that depend on them show labelled slots or are behind flags.
