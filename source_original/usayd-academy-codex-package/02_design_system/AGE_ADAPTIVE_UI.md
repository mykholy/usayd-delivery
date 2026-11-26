# Age-adaptive interface — learner app only (v0.8)

The owner requested this on 2026-11-22 (decision D-34). It applies **only to the Flutter learner app**: not the web portals, and not the teacher, supervisor or admin apps.

## Proposed age ranges (D-35 — needs owner approval)
| Mode | Default for | Feel | Screens |
|---|---|---|---|
| **Kids** | 6–12 | Motivating, warm, round, playful within the Usayd palette | `UX-MOBILE-K02` mission · `K05` path · `K08` stars · `K11` me |
| **Professional** | 13–59 | The existing app: full tools, dense but calm | `UX-MOBILE-001…011` |
| **Simple** | 60+ | As simple as possible: big type, one action, 3 tabs | `UX-MOBILE-S02` today · `S04` lessons · `S11` help |

Why these cut-offs:
- **6:** reading and touch skills are enough for short missions. Younger children use the app *with* a parent.
- **12/13:** teenagers reject childish UI. Learners aged 13–17 get Professional, but **all minor protections stay on**: guardian consent, privacy and no public ranking.
- **60:** a common threshold for larger type and simpler navigation. It is a default, never a lock.

## Rules
- The default comes **only** from the age band entered at sign-up. Never infer age from photos, voice or behaviour.
- The mode is a preference saved on the account and shown on every device. Change it in `UX-MOBILE-012` (App style).
  - Anyone can choose Simple.
  - Kids mode for an under-13 learner is set by the guardian, behind the guardian PIN.
- The Quran text, the mushaf view, lesson rooms and payments are **the same in every mode**. Kids mode never styles ayat playfully.
- **Kids mode safeguards:**
  - No payments or external links.
  - No public ranking or leaderboard.
  - Stars and badges are private and non-monetary. Badges are teacher-awarded or come from teacher-approved tasks.
  - A missed day pauses progress and never resets it (FR-ENG-004 retention without coercion).
  - Read-aloud instructions are available. Celebration sounds are off by default.
- **Simple mode:**
  - Body text 19–20 px, targets ≥ 56–60 px, one primary action per screen, 3 tabs.
  - No slide-to-confirm: a large button plus a confirmation dialog instead.
  - Dates are written in words with the time-zone name. Animations are off. Text size and high contrast are in Help.

## Tokens per mode
| Token | Kids | Professional | Simple |
|---|---|---|---|
| Body text | 16 px | 15–16 px | 19 px |
| Button height | 56 px | 44–54 px | 60 px |
| Card radius | 24 px | 20 px | 20 px + 1.5 px strong border |
| Header | Green night + gold glow + stars | Night + lamp glow | Plain night, no pattern |
| Motion | Gentle (respects reduced motion) | Standard | None |
| Tabs | 4 (Mission, Path, Stars, Me) | 5 | 3 (Today, Lessons, Help) |

## Flutter
- `enum InterfaceMode { kids, pro, simple }` is stored in user preferences (`PATCH /api/v1/me/preferences`).
- A `ThemeExtension<UsaydMode>` holds the type scale, radii, target sizes and motion flags. A `ModeScope` InheritedWidget picks the shell (tabs) and the home route.
- Routes:
  - Kids: `/kids/today`, `/kids/path`, `/kids/stars`, `/kids/me`.
  - Simple: `/simple/today`, `/simple/lessons`, `/simple/help`.
  - Shared: `/lesson/:id`, `/review/:id`.

## Kids cartoon graphics (v0.9, D-37)
- An original flat cartoon set:
  - a festive night scene (garland, lanterns, crescent, stars, hills, mushaf on a rahl);
  - six medals with ribbons;
  - a treasure-of-light destination at the end of the path;
  - lantern avatars in four colours.
- Style: thick rounded outline `#2B2118` (3 px), flat fills from a kids-only accent palette (gold, orange, mint, leaf, sky, coral, cream) on top of the brand. No gradients except the soft lamp glow.
- **No faces of people or animals.** This avoids the question of image depiction for a Quran academy and keeps the design culturally safe.
  - An optional mascot character is an **owner decision (D-37)**.
  - If approved, it must be an object (a lantern or a book) and never a person, an animal or any religious figure.
- Never placed on or next to Quran text. Vector only, and decorative (`aria-hidden`).
- Files: `01_design/assets/illustrations/kids-*.svg`.

## Open
- **D-35:** approve the age ranges.
- **D-36:** approve the badge catalogue and award rules.
- The badges endpoint is missing from OpenAPI.
- Guardian PIN: device-local or server-side (with O-04).
