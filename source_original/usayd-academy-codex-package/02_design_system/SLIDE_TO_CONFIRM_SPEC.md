# Slide to confirm — interaction specification (OPEN-02, D-30, D-41)

Used only for important or irreversible actions (8 places): UX-MOBILE-002, UX-MOBILE-010, UX-PUBLIC-009, UX-GLOB-006, UX-LEARNER-008, UX-SUP-002, UX-TEACHER-007, UX-TEACHER-011.

## Behaviour (implemented in the AR/EN static exports and tested in Chrome)
| Input | Result |
|---|---|
| Pointer/touch drag of the thumb | Thumb and fill follow the pointer along the inline axis (right-to-left in Arabic) |
| Release at ≥ 90 % | **Confirmed** → label “Confirmed”, live-region announcement, then the action/navigation |
| Release before 90 % | Animated reset to start (0.3 s; instant with reduced motion); nothing happens |
| `pointercancel` (scroll takeover, incoming call, palm rejection) | Reset; nothing happens |
| Single tap / click / Enter / Space | **Armed**: label “Press again to confirm”, gold ring, live announcement; 5 s window |
| Second tap / Enter within 5 s | Confirmed (non-drag alternative, WCAG 2.5.7) |
| Esc while armed, or 5 s passes | Disarmed, original label restored |
| After confirmation | Control ignores further input (no double submit); the real action uses an Idempotency-Key |

## Accessibility
- Native `<a>`/`<button>`; accessible name = visible label; hint via `aria-describedby` (“Slide to confirm, or tap twice”).
- `touch-action: pan-y` so vertical scrolling still works; native link dragging disabled.
- Live region `#u-slide-live` (polite) announces Armed / Confirmed.
- Focus ring 3 px; target height 60 px.

## Evidence
`11_qa/automated/slide_test.json` — 8 controls × AR/EN = 16 runs × 8 checks (partial drag resets, cancel resets, full drag confirms, single tap only arms, live announcement, Esc disarms, Enter twice confirms, arm times out).

## Limits
- The Claude Design canvas keeps the CSS hover demonstration (no script runtime for drag there).
- Not tested on physical touch devices or with screen readers (UNVERIFIED).
- In the app, confirmation starts the real request: show loading on the control, then success or the error state; a failed request returns the control to start with the error announced.
