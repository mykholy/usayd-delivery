# Component specifications

Visual source: `02_design_system/usayd-ui.css` (the exact stylesheet used by every artboard) + `tokens.json`. Implement these as components in the web app (and Flutter widgets for mobile). Usage counts come from the 169 screen specs.

## Global rules
- Arabic RTL default, English LTR: same markup, `dir` on root, logical CSS properties only (`margin-inline-start`, `text-align:start`).
- Fonts: Reem Kufi (display/headings), IBM Plex Sans Arabic (Arabic text), IBM Plex Sans (English text), Amiri Quran (Quran only).
- Focus: 2px brass ring with 2px surface gap. Touch targets ≥ 44px. Contrast ≥ 4.5:1 text, ≥ 3:1 UI. `prefers-reduced-motion` disables animation.
- Themes: Parchment (light, default) and Night (dark) via `[data-theme]`. Never force dark while reading Quran.

## Button
- **Class / markup:** `.u-btn + .p/.a/.s/.g/.d, size .sm/.lg, [aria-disabled]`
- **Anatomy:** icon? + label (+ trailing icon)
- **Variants:** Primary (night; lamp in dark theme), Accent (lamp + ink), Secondary, Ghost, Danger × S36/M44/L52
- **States:** default, hover, focus (2px brass ring + 2px gap), disabled (explain why nearby), loading (spinner + label, aria-busy)
- **A11y & RTL:** Real <button>/<a>. Leading icon sits on the logical start; directional arrows mirror in RTL. Min target 44px.
- **Used on:** 178 screens (e.g. UX-ADMIN-001, UX-ADMIN-002, UX-ADMIN-003, UX-ADMIN-004, UX-ADMIN-005, UX-ADMIN-006)

## Status Chip
- **Class / markup:** `.u-chip + tone (ok, err, warn, info, ai, lock, clay, brand, lamp)`
- **Anatomy:** icon + text
- **Variants:** Learning states (not started / in progress / due / verified / strengthen), competition provisional/final, privacy locked, AI suggestion
- **States:** static
- **A11y & RTL:** Never colour-only: always icon + text. Never colour Quran text by status.
- **Used on:** 117 screens (e.g. UX-ADMIN-001, UX-ADMIN-002, UX-ADMIN-003, UX-ADMIN-005, UX-ADMIN-006, UX-ADMIN-007)

## Form field
- **Class / markup:** `.u-field > label + .u-input (+ .err) + .u-help`
- **Anatomy:** label, required marker / “(optional)”, control, helper or error
- **Variants:** text, email, tel, password, select, textarea, date, datetime-local
- **States:** default, focus, filled, error (2px border + message + role=alert), disabled, read-only
- **A11y & RTL:** Emails/phones/IDs: dir=ltr inside RTL. Error text says how to fix. 48px height.
- **Used on:** 40 screens (e.g. UX-ADMIN-009, UX-ADMIN-018, UX-ADMIN-022, UX-ADMIN-024, UX-ADMIN-026, UX-AUTH-001)

## Checkbox / consent
- **Class / markup:** `.u-check`
- **Anatomy:** checkbox + label text
- **Variants:** required consent, optional preference
- **States:** checked, unchecked, disabled
- **A11y & RTL:** Optional consents default OFF. A minor’s own checkbox is never guardian consent.
- **Used on:** 11 screens (e.g. UX-ADMIN-026, UX-AUTH-001, UX-AUTH-002, UX-AUTH-003, UX-GLOB-003, UX-LEARNER-021)

## Radio cards
- **Class / markup:** `label.u-card + input[type=radio]`
- **Anatomy:** radio + title + caption
- **Variants:** 2–3 options
- **States:** selected (2px outline), unselected
- **A11y & RTL:** role=radiogroup; arrow-key navigation.
- **Used on:** 7 screens (e.g. UX-ADMIN-009, UX-ADMIN-018, UX-ADMIN-024, UX-AUTH-005, UX-GLOB-005, UX-GLOB-006)

## Segmented control
- **Class / markup:** `.u-seg > button[aria-pressed]`
- **Anatomy:** options
- **Variants:** 2–5 options
- **States:** selected, default
- **A11y & RTL:** Use for view switches only (not for form submission).
- **Used on:** 16 screens (e.g. UX-ADMIN-010, UX-AUTH-001, UX-GLOB-016, UX-LEARNER-007, UX-LEARNER-008, UX-LEARNER-013)

## Tabs
- **Class / markup:** `.u-tabs > a[aria-current]`
- **Anatomy:** tab links
- **Variants:** route tabs
- **States:** active (lamp underline), default
- **A11y & RTL:** Tabs that change route are links.
- **Used on:** 18 screens (e.g. UX-ADMIN-003, UX-ADMIN-004, UX-ADMIN-008, UX-ADMIN-015, UX-ADMIN-018, UX-ADMIN-028)

## Stepper
- **Class / markup:** `.u-steps > .u-step(.on/.done)`
- **Anatomy:** number bubble + label
- **Variants:** wizards
- **States:** done ✓, current, upcoming
- **A11y & RTL:** Announce “step x of n”.
- **Used on:** 9 screens (e.g. UX-ADMIN-026, UX-AUTH-002, UX-AUTH-005, UX-GLOB-006, UX-GLOB-011, UX-LEARNER-004)

## Card
- **Class / markup:** `section.u-card(.feat/.night/.arch)`
- **Anatomy:** optional header (icon, title, subtitle, action) + body
- **Variants:** default, featured (surface-raised), night, arch (brand canopy top)
- **States:** static
- **A11y & RTL:** Radius 14. No heavy shadows; depth from surface contrast.
- **Used on:** 147 screens (e.g. UX-ADMIN-001, UX-ADMIN-003, UX-ADMIN-005, UX-ADMIN-006, UX-ADMIN-007, UX-ADMIN-008)

## KPI Tile
- **Class / markup:** `.u-card.u-kpi`
- **Anatomy:** icon + label, value, note, “Sample data” tag
- **Variants:** —
- **States:** loading skeleton
- **A11y & RTL:** Every metric shows source; design values are labelled sample data.
- **Used on:** 12 screens (e.g. UX-ADMIN-001, UX-ADMIN-016, UX-ADMIN-021, UX-ADMIN-023, UX-ADMIN-028, UX-ADMIN-034)

## Data table (cards < 760px)
- **Class / markup:** `.u-tablebox > table.u-table`
- **Anatomy:** caption?, thead, rows, numeric cells (.num, bidi-isolated)
- **Variants:** —
- **States:** empty (State panel), loading (skeleton rows)
- **A11y & RTL:** Scrolls horizontally inside its box; production should render card lists < 760px.
- **Used on:** 63 screens (e.g. UX-ADMIN-002, UX-ADMIN-004, UX-ADMIN-012, UX-ADMIN-013, UX-ADMIN-014, UX-ADMIN-016)

## List row
- **Class / markup:** `.u-li`
- **Anatomy:** icon, title (+link), meta, trailing control
- **Variants:** —
- **States:** —
- **A11y & RTL:** Whole-row link only if it has one destination.
- **Used on:** 42 screens (e.g. UX-ADMIN-001, UX-ADMIN-008, UX-ADMIN-026, UX-ADMIN-030, UX-ADMIN-039, UX-ENG-002)

## Alert / Inline
- **Class / markup:** `.u-alert + tone (info, ok, warn, err, ai, lock)`
- **Anatomy:** icon, title, body, optional action
- **Variants:** tones
- **States:** role=status / role=alert (error)
- **A11y & RTL:** AI tone mandatory for any unapproved AI output.
- **Used on:** 178 screens (e.g. UX-ADMIN-001, UX-ADMIN-002, UX-ADMIN-003, UX-ADMIN-004, UX-ADMIN-005, UX-ADMIN-006)

## State panel
- **Class / markup:** `.u-card.u-state(.err)`
- **Anatomy:** badge icon, title, body, action
- **Variants:** empty, error, no-permission, offline
- **States:** —
- **A11y & RTL:** Always says what happened, why, and what to do next. Error shows stable code.
- **Used on:** 178 screens (e.g. UX-ADMIN-001, UX-ADMIN-002, UX-ADMIN-003, UX-ADMIN-004, UX-ADMIN-005, UX-ADMIN-006)

## Loading skeleton
- **Class / markup:** `.u-sk`
- **Anatomy:** grey bars
- **Variants:** —
- **States:** pulse; static under reduced motion
- **A11y & RTL:** aria-busy on the region.
- **Used on:** 178 screens (e.g. UX-ADMIN-001, UX-ADMIN-002, UX-ADMIN-003, UX-ADMIN-004, UX-ADMIN-005, UX-ADMIN-006)

## Timezone chip
- **Class / markup:** `.u-chip + globe icon`
- **Anatomy:** weekday time · city label (UTC±hh:mm)
- **Variants:** —
- **States:** —
- **A11y & RTL:** Display only; tapping switches display zone, never moves a booked UTC instant.
- **Used on:** 131 screens (e.g. UX-ADMIN-001, UX-ADMIN-002, UX-ADMIN-003, UX-ADMIN-004, UX-ADMIN-005, UX-ADMIN-006)

## Localized price
- **Class / markup:** `value + currency + period + tax note`
- **Anatomy:** —
- **Variants:** per market price book
- **States:** —
- **A11y & RTL:** amount_minor + ISO currency; CLDR formatting; KWD/BHD/OMR 3 decimals.
- **Used on:** 4 screens (e.g. UX-GLOB-002, UX-PUBLIC-001, UX-PUBLIC-003, UX-PUBLIC-004)

## Lesson card (dual timezone)
- **Class / markup:** `card.feat`
- **Anatomy:** teacher, provider chip, local time + teacher time, actions
- **Variants:** join locked / join open / external provider
- **States:** —
- **A11y & RTL:** External providers open new tab with return path.
- **Used on:** 2 screens (e.g. UX-LEARNER-001, UX-LEARNER-009)

## AI suggestion card
- **Class / markup:** `card + AI chip`
- **Anatomy:** status chip, suggestion, reason, provenance, actions
- **Variants:** pending / approved / declined
- **States:** —
- **A11y & RTL:** Never final; never generates Quran text.
- **Used on:** 6 screens (e.g. UX-LEARNER-001, UX-LEARNER-012, UX-LEARNER-027, UX-MOBILE-002, UX-MOBILE-006, UX-TEACHER-007)

## Quran reader (licensed text placeholder)
- **Class / markup:** `.u-quran > p.u-q.u-ayah(.hl/.sel)`
- **Anatomy:** surah label, licence chip, ayah lines, teacher note, source line
- **Variants:** reading, highlighted, selected, annotated
- **States:** —
- **A11y & RTL:** Text only from licensed corpus; Amiri Quran; never mirrored; states on container only.
- **Used on:** 11 screens (e.g. UX-LEARNER-010, UX-LEARNER-013, UX-LEARNER-016, UX-LEARNER-018, UX-LEARNER-023, UX-MOBILE-003)

## Memory map grid (juz)
- **Class / markup:** `.u-mem > .u-cell(.v/.d/.p/.s)`
- **Anatomy:** juz label + status icon/text; lamp dot when verified
- **Variants:** 5 statuses
- **States:** —
- **A11y & RTL:** 6 columns desktop, 3 phone.
- **Used on:** 4 screens (e.g. UX-LEARNER-001, UX-LEARNER-015, UX-MOBILE-005, UX-TEACHER-009)

## Week calendar
- **Class / markup:** `.u-cal`
- **Anatomy:** time column + 7 day columns, events (.u-ev .av/.cf)
- **Variants:** availability, lessons, conflicts
- **States:** —
- **A11y & RTL:** Scrolls horizontally on phone; show zone in header.
- **Used on:** 6 screens (e.g. UX-ADMIN-010, UX-GLOB-016, UX-LEARNER-007, UX-SUP-006, UX-TEACHER-003, UX-TEACHER-004)

## Video stage
- **Class / markup:** `.u-video + .u-tile`
- **Anatomy:** teacher tile, self tile, status overlay
- **Variants:** embedded / prejoin preview
- **States:** connecting, reconnecting, failed
- **A11y & RTL:** Capabilities from provider; hide unsupported controls with explanation.
- **Used on:** 4 screens (e.g. UX-LEARNER-010, UX-MOBILE-003, UX-TEACHER-006, UX-VPC-009)

## Classroom controls
- **Class / markup:** `.u-ctrls > .u-ctrl(.end)`
- **Anatomy:** mic, camera, share, hand, chat, leave
- **Variants:** per provider capability
- **States:** on/off/disabled
- **A11y & RTL:** aria-label on every icon button.
- **Used on:** 2 screens (e.g. UX-LEARNER-010, UX-TEACHER-006)

## Timeline / audit trail
- **Class / markup:** `.u-tl > .u-tli(.on/.ok)`
- **Anatomy:** title + caption
- **Variants:** process steps, audit history
- **States:** —
- **A11y & RTL:** —
- **Used on:** 12 screens (e.g. UX-ADMIN-003, UX-ADMIN-009, UX-ADMIN-022, UX-GLOB-013, UX-LEARNER-002, UX-LEARNER-021)

## Version diff viewer
- **Class / markup:** `.u-diff > .del/.ins`
- **Anatomy:** monospace lines
- **Variants:** —
- **States:** —
- **A11y & RTL:** Always LTR (config/code).
- **Used on:** 4 screens (e.g. UX-GLOB-013, UX-SUP-002, UX-TEACHER-011, UX-VPC-006)

## Dual approval status
- **Class / markup:** `card + timeline + lock alert`
- **Anatomy:** proposer, approver 1, approver 2
- **Variants:** —
- **States:** pending / approved
- **A11y & RTL:** Self-approval forbidden and explained.
- **Used on:** 3 screens (e.g. UX-ADMIN-022, UX-GLOB-013, UX-VPC-006)

## Shell / Sidebar
- **Class / markup:** `aside.u-side > a.u-nav(.on)`
- **Anatomy:** brand, role scope, nav items (lock icon if out of scope), account
- **Variants:** learner, teacher, admin, supervisor
- **States:** active, hover, locked
- **A11y & RTL:** Docks on logical start; collapses to .u-mbar < 760px.
- **Used on:** 127 screens (e.g. UX-ADMIN-001, UX-ADMIN-002, UX-ADMIN-003, UX-ADMIN-004, UX-ADMIN-005, UX-ADMIN-006)

## Shell / App topbar
- **Class / markup:** `.u-top`
- **Anatomy:** search, timezone chip, language switch, notifications, avatar
- **Variants:** —
- **States:** —
- **A11y & RTL:** Language switch changes locale only.
- **Used on:** 127 screens (e.g. UX-ADMIN-001, UX-ADMIN-002, UX-ADMIN-003, UX-ADMIN-004, UX-ADMIN-005, UX-ADMIN-006)

## Shell / Public header
- **Class / markup:** `.u-pub`
- **Anatomy:** lockup, links, market selector, language, login, CTA
- **Variants:** —
- **States:** —
- **A11y & RTL:** Market selector ≠ language.
- **Used on:** 15 screens (e.g. UX-GLOB-001, UX-GLOB-002, UX-GLOB-003, UX-PUBLIC-001, UX-PUBLIC-002, UX-PUBLIC-003)

## Shell / Public footer
- **Class / markup:** `.u-foot`
- **Anatomy:** brand + tagline, link columns, honest certificate note
- **Variants:** —
- **States:** —
- **A11y & RTL:** —
- **Used on:** 15 screens (e.g. UX-GLOB-001, UX-GLOB-002, UX-GLOB-003, UX-PUBLIC-001, UX-PUBLIC-002, UX-PUBLIC-003)

## Mobile / Tab bar
- **Class / markup:** `.u-tabbar > a(.on)`
- **Anatomy:** icon pill + label
- **Variants:** learner (5), teacher (3)
- **States:** active
- **A11y & RTL:** Labels always visible; first tab on the right in Arabic.
- **Used on:** 16 screens (e.g. UX-GLOB-017, UX-MOBILE-002, UX-MOBILE-004, UX-MOBILE-005, UX-MOBILE-006, UX-MOBILE-008)

## Marketing hero
- **Class / markup:** `.u-hero`
- **Anatomy:** eyebrow, display title, lead, CTAs, product preview, licensed photo placeholder
- **Variants:** —
- **States:** —
- **A11y & RTL:** No fake photos/testimonials.
- **Used on:** 1 screens (e.g. UX-PUBLIC-001)
