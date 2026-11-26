# Audit cycles

Each cycle renders **every board** (cycles 1–5: 161 screens + 9 journey boards; cycles 6–11: 169 screens + 9 journey boards) in Arabic/English × light/dark at 320, 360, 390, 430, 768, 1024, 1280, 1440 and 1920 px. It also renders every product screen in the 6 non-default states (loading, empty, error, no-permission, offline, success) at 390 and 1440 px, AR/EN × light/dark, and does a keyboard focus pass (14 Tab stops per screen, AR/EN, 390 + 1440). Reduced motion is on.

Checks per render: page horizontal overflow, clipped text, interactive targets < 44×44 px, exactly one H1, `href="#"`, axe-core WCAG 2.0/2.1/2.2 A+AA. Focus pass: the focused element has a visible outline or ring.

| Cycle | Renders | Focus stops | Findings | Result |
|---|---|---|---|---|
| Cycle 1 (initial; states partially run: loading/empty/error) | 9984 | 0 | overflow 144, h1!=1 3744 | issues → fixed next cycle |
| Cycle 2 | 13848 | 9182 | h1!=1 6160, axe:target-size 2, focus-invisible 48 | issues → fixed next cycle |
| Cycle 3 | 13848 | 9182 | axe:target-size 2, focus-invisible 2 | issues → fixed next cycle |
| Cycle 4 | 13848 | 9182 | none | clean |
| Cycle 5 | 13848 | 9182 | none | clean |
| Cycle 6 (after age-adaptive modes; default state only, stopped to fix) | 6408 | 0 | axe:color-contrast 27, axe:scrollable-region-focusable 36 | issues → fixed next cycle |
| Cycle 7 | 14520 | 9610 | none | clean |
| Cycle 8 (default state only; superseded by the cartoon change) | 6408 | 0 | none | clean |
| Cycle 9 (after kids cartoon graphics) | 14520 | 9610 | none | clean |
| Cycle 10 (after the 2026-11-23 remediation; default state 320–1280, stopped to fix R-029) | 4984 | 0 | overflow 16 | issues → fixed next cycle |
| Cycle 11 (full, after the R-029 fix) | 14520 | 9624 | none | clean |
| Cycle 12 (full regression confirmation, no changes in between) | 14520 | 9624 | none | clean |

## Issues by severity (all cycles)
| Severity | Found | Fixed and verified | Open |
|---|---|---|---|
| P0 | 0 | 0 | 0 |
| P1 | 17 | 15 | 2 |
| P2 | 15 | 14 | 1 |
| P3 | 10 | 6 | 4 |

Details: `ISSUE_REGISTER.csv`.

## Not verifiable here (marked UNVERIFIED, not passed)
- Screen readers (TalkBack, VoiceOver, NVDA): no real assistive-technology session was possible.
- Real devices: safe areas, notches, the dynamic island and the keyboard covering inputs. Simulated only by viewport size.
- Text-only resize to 200%. Reflow was covered by the 320 px renders, which equal 400% zoom of 1280 px.
- Dialog focus trapping: the prototype has no live dialogs. It is specified in the component docs.
- Real slide-to-confirm dragging and Flutter rendering.
- Human visual sign-off. My visual reviews are AI reviews of rendered contact sheets, not a human design review.

## Visual reviews performed (AI, on rendered screenshots)
- v0.5: every screen, AR light 390 and EN light 1440. Dark mode sampled at 1440 and 390.
- v0.6/v0.7: the redesigned mobile shell, login, today, report, teacher day, checkout and auth on mobile, in AR/EN and light/dark (see `after_contact_sheets/`).
- v0.8/v0.9: the 8 age-adaptive screens (chooser, 4 kids, 3 simple) and the kids cartoon set, in AR/EN and light/dark.
- v1.0 (2026-11-23): every product screen, AR light 390 and EN light 1440 (`visual_review/` sheets; notes per screen in `VISUAL_QA_MATRIX.csv`).
