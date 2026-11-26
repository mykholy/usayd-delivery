# Motion & illustration — v0.3

All rules are implemented in `usayd-ui.css` (block "v0.3 modern layer") and are the visual source of truth.

## Illustrations
- Vector SVG only (resolution-independent, sharp on any screen density). Files: `01_design/assets/illustrations/`.
- Generated from the brand mark's motifs: canopy arc, three hanging lamps, open mushaf on a rahl, night sky, 8-point star lattice.
- **No people, no faces, never the Sahaba.** No stock photos presented as real learners/teachers.
- Real photography (teachers, lessons) is allowed only as licensed, academy-approved images in the marked `u-ph` slots.
- On screens the SVGs are inlined so their CSS animations run. In Flutter use `flutter_svg` for static art and Rive/Lottie or `AnimatedBuilder` for the lamp glow/sway if animated.
- Spot illustrations use CSS variables (`--canopy`, `--book`, `--bg-accent-soft`, `--lamp`, `--ok`, `--err`, `--ai`) so they follow light/dark theme. The exported files have light-theme values baked in.

| Asset | Used on |
|---|---|
| hero-night-scene | Home hero (PUBLIC-001), auth side panel (AUTH-*, TEACHER-001) |
| lanterns-night / lanterns-paper | Learner home banner, public page heroes |
| spot-memorize / tajweed / review / foundations | Program cards |
| spot-teacher / ai / live | "How it works" steps, teacher banner, AI banners |
| spot-competition | Competitions banners (LEARNER-020, MOBILE-008) |
| spot-empty / error / denied / offline | State panels on all 169 screens |
| spot-success | Reserved for confirmation screens |
| pattern-star-night / paper | Sidebar, hero, footer, night cards, banners, first public section |

## Motion tokens
| Token | Value | Use |
|---|---|---|
| `--ease` | `cubic-bezier(.2,.7,.2,1)` | all UI transitions |
| rise | 700 ms, translateY 14px→0 + fade, stagger 70 ms (max 280 ms) | page sections, grid cards, banner content on first paint |
| hover lift | 350 ms, translateY −3px + shadow `--sh-2` | cards in grids |
| press | scale .97, 180 ms | all buttons |
| bar fill | 1.3 s from 0 (origin follows reading direction) | progress bars |
| chart grow | 1 s from 0, stagger 60 ms | bar charts |
| lamp glow | 4.2 s loop, opacity .6→1, scale .92→1.06 | illustration lamps |
| lamp sway | 6.5 s loop, ±1.6° from chain top | hanging lamps |
| twinkle | 3.6 s loop | stars, AI nodes, verified memory cells |
| skeleton | 1.5 s shimmer | loading state |

## Accessibility
- `prefers-reduced-motion: reduce` disables every animation and transition, including hover lifts.
- Motion never carries meaning on its own. Status is always also shown in text and colour.
- Illustrations are decorative (`aria-hidden="true"`). Meaning lives in the adjacent heading and text.

## Depth & glass
- Shadows: `--sh-1` at rest and `--sh-2` on hover. Both are soft and warm. Dark theme uses inset highlights instead of heavy drop shadows.
- Glass: top bar, public header and mobile app bar use `backdrop-filter: blur(14px)` over `--glass`.
- Lamp halo: a radial lamp-gold glow at ≤ 18% opacity, used only on night surfaces. No purple or blue gradients.
