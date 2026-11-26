# Accessibility manual test script (screen readers, devices, zoom)

Automated checks cannot prove these. Each line needs a person, a device and a recorded result (PASS / FAIL + note + date). Until then the status is **UNVERIFIED**.

## Devices / tools
- Android + TalkBack (Arabic and English system language) · iPhone + VoiceOver (Arabic and English) · Windows + NVDA + Chrome · macOS + VoiceOver + Safari.

## Scripts (run in AR and EN)
1. **Landmarks & headings** — open UX-LEARNER-001, UX-ADMIN-001, UX-MOBILE-002: one H1 announced first; headings navigable in order; skip link moves to main.
2. **Language & direction** — Arabic text read with Arabic voice; numbers/IDs (`B-5521`, times) read correctly; mixed AR/EN strings do not reorder.
3. **Forms** — UX-AUTH-001/003/004: every field has its label read; errors announced and linked (`aria-describedby`); password reveal state announced.
4. **Tables** — UX-ADMIN-015: column headers read with cells; sort state (“sorted ascending”) announced; stacked records at 390 px read label + value.
5. **State changes** — trigger loading/empty/error/no-permission/offline/success on any screen: the state title is announced; Retry/Reconnect reachable.
6. **Slide to confirm** — UX-LEARNER-008: double-tap arms (“Press again to confirm” announced), double-tap again confirms; swipe gestures of the reader do not trigger it accidentally.
7. **Dialogs** (in the built app) — focus moves into the dialog, is trapped, Esc closes, focus returns to the trigger.
8. **Zoom / text size** — browser 200 % text-only zoom and OS large text: no clipped labels, no overlapping sticky bars (UX-PUBLIC-004, UX-GLOB-006).
9. **Forced colours / high contrast** — Windows High Contrast: focus ring and status chips remain visible.
10. **Kids & Simple modes** — UX-MOBILE-K02/K08, S02: images have meaningful names or are hidden; large targets reachable with Switch Access.
11. **Safe areas & keyboard** — on a notched phone: header and tab bar clear of the notch/home indicator; on-screen keyboard never hides the focused field (UX-MOBILE-001).
12. **Reduced motion** — OS setting on: no parallax/float/shimmer; slide resets instantly.
