# Modern components — v0.7

These were added on the owner's request ("modern, professional, glass buttons, slide-to actions"). They follow the Usayd brand and the accessibility rules in `MOTION_AND_ILLUSTRATION.md`. Styles live in `usayd-ui.css`, in the "v0.6" and "v0.7" blocks.

## Mobile night header + rounded sheet (`.u-mhead` + `.u-sheet`)
- **Night header:** pattern plus a lamp glow. It holds circular 44 px glass controls: back (or the brand mark on root tabs), theme, and notifications or help. An optional hero sits below them: a display heading, an illustration, and a glass summary card.
- **Content sheet:** a parchment sheet with 28 px top corners overlaps the header by 26 px. It has a grab-handle accent and its own scroll.
- **Flutter:** use a `Scaffold` with a `SliverAppBar`/custom header. Make the sheet a `Container` with `BorderRadius.vertical(top: Radius.circular(28))` and a negative top offset through a `Stack`. Respect `MediaQuery.padding`.
- **Web auth below 760 px:** the same pattern. The night brand strip sits on top and the form is a rounded sheet.

## Glass buttons
- **Secondary on light surfaces:** frosted translucent surface (62% raised + 14 px backdrop blur), a hairline border, an inner top highlight and a soft shadow.
- **Secondary on night surfaces** (header, hero, banners, night cards): white at 10% with a 24% border and an inner highlight.
- **Primary and accent:** solid fill with an inner top highlight and a lower edge, so they read as glossy and tactile.
- Text contrast stays at least 4.5:1. The glass effect is never the only way to tell a button apart, because the label is always visible.

## Slide to confirm (`.u-slide`)
- **When to use it:** important or irreversible actions only.
  - Pay (`UX-GLOB-006`).
  - Confirm booking (`UX-LEARNER-008`, `UX-PUBLIC-009`).
  - Publish a lesson report (`UX-TEACHER-007`, `UX-MOBILE-010`).
  - Approve a plan (`UX-TEACHER-011`, `UX-SUP-002`).
  - Join a lesson from the mobile hero (`UX-MOBILE-002`).
- Don't use it for navigation or reversible actions.
- **Anatomy:** a 60 px pill track, a 52 px thumb with a directional arrow, a centred label, and animated chevrons. In RTL the thumb starts on the right and slides left.
- **Behaviour (to implement):**
  - Dragging the thumb past 85% of the track confirms. Releasing earlier snaps it back.
  - **Single-pointer alternative (WCAG 2.5.7):** the first tap or Enter arms the control and shows “Tap again to confirm” for 4 s. A second tap or Enter confirms. Esc cancels.
  - After confirming, the track shows a spinner and then a success tick or an error, which uses the action's own states. It's idempotent: a second confirm is ignored while the request is pending.
  - A screen reader announces the label and the hint (`aria-describedby`).
  - Reduced motion: no thumb animation; the confirmation is shown as a state change.
- **Prototype note:** in the design, hover and focus animate the thumb across and a click navigates. Real dragging is **not** implemented in the static design.

## Avatar stack (`.u-avs`)
- Overlapping 40 px initials with a ring in the surface colour, plus a “+N” chip.
- Initials only. No photos without written rights.

## Amount display (`.u-amount`)
- A large tabular figure with the currency in a smaller, lighter weight. It is always LTR.
- When the price is not approved, the value is an owner-content slot (O-02).

## Icon fields
- A leading icon is chosen by type: email → mail, tel → phone, password → lock, date → calendar. Height is 52 px and the radius is 14 px.
- Password fields have a 44 px reveal button (`aria-pressed`, `aria-controls`).
- Focus shows a 2 px outline plus a halo.
