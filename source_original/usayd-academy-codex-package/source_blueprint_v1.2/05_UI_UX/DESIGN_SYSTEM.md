# Premium design system — Figma-ready specification

## Principles

Contemporary, refined, credible and calm. Respect the subject matter without clichés. Use subtle geometric accents inspired by Islamic art only as unobtrusive decoration. Layout and readability dominate ornament. Typography must support Arabic diacritics well, with *verified Quran text rendering* isolated from general UI typography.

## Suggested direction (tokens are creative proposals, not a required brand)

| Token | Light | Dark | Role |
|---|---|---|---|
| `--brand-950` | `#102E2B` | `#0D2525` | primary dark |
| `--brand-700` | `#176B60` | `#42B6A5` | primary action |
| `--brand-500` | `#2E8A7D` | `#66CDBE` | interactive |
| `--accent-500` | `#B58B49` | `#D3AE6A` | restrained gold accent |
| `--canvas` | `#F7FAF8` | `#0C1516` | overall background |
| `--surface` | `#FFFFFF` | `#142222` | cards |
| `--text` | `#172726` | `#EAF5F0` | headings and body |
| `--muted` | `#61736E` | `#A3B7B0` | metadata |
| `--border` | `#DDE7E3` | `#2F4542` | controls |
| `--danger` | `#B94545` | `#EF9898` | warnings/errors |
| `--success` | `#1E7F5A` | `#71D4AA` | verified progress |

**Contrast caveat:** color values must be checked per foreground/background pairing in Figma against WCAG AA, adjusted if needed; don't assert compliance from hex values alone.

## Typography and spacing

- General Arabic UI: Tajawal or IBM Plex Sans Arabic (verify licenses/availability); Latin UI: Inter. Quran text separate approved Mushaf typeface/engine and proper verse marks.
- Scale: 12/14/16 body, 20/24/32/40 headings, adapt line-height 1.6–1.85 for Arabic prose, larger for Quran readings. Avoid cramped label badges.
- Grid: 8px spacing; layout max width 1280–1440; side navigation 240–256; card radius 16; border 1px; soft shadow sparingly.
- Responsive frames: 360, 390, 428 (mobile), 768/1024 tablet, 1280/1440 desktop. Flutter screens for phones and tablets, support cutouts and safe areas.

## Figma variables / semantic tokens

Color tokens: `background/page`, `background/raised`, `text/primary`, `text/secondary`, `border/default`, `action/primary`, `action/primary-hover`, `feedback/error`, `feedback/success`, `learning/due`, `learning/verified`, `competition/provisional`, `competition/final`, `privacy/locked`.

Sizes: `space/xs=4`, `sm=8`, `md=16`, `lg=24`, `xl=32`, `2xl=48`, `3xl=64`; radius `sm=8`, `md=12`, `lg=16`, `xl=24`; input 48px; touch target minimum 44px; icons 16/20/24.

## Component inventory + variants

- `Button` primary/secondary/ghost/danger, sizes S/M/L, default/hover/focus/disabled/loading; icon-left/right RTL-aware.
- `Field` input/select/phone/OTP/password/textarea/search; required/optional/error/helper/success/disabled/read-only.
- `Modal/Sheet` desktop dialog, mobile bottom sheet, confirm/escape/trap focus.
- `Navigation` public header, learner sidebar/mobile tab, teacher nav, admin RBAC nav, breadcrumb, active/disabled labels.
- `TeacherCard`, `ProgramCard`, `PackageCard`, `LessonCard`, `AssessmentRubricCard`, `SurahSegmentCard`, `RevisionDueCard`.
- `QuranReader` surah/ayah labels, selection ranges, teacher annotation, copy restrictions aligned with license.
- `VideoStage` embedded/external, prejoin, reconnection, permission denied, audio-only, recording consent indicator.
- `StudyPlanTimeline`, `MemoryMapGrid`, `MasteryBadge`, `DueReviewStack`, `AssessmentQuestion`, `ExamAttemptStatus`.
- `CompetitionCard`, `RegistrationEligibility`, `RoundTimeline`, `JudgeRubricGrid`, `PrivateLeaderboard`, `AppealStatus`, `Certificate`.
- `CompensationRuleBuilder`, `PayoutStatement`, `PolicyCase`, `AuditHistory`, `KPITrend`, `DataTable`, `FilterBar`.
- `Skeleton/Empty/Error/Offline/Toast/InlineAlert`, `ConsentGate`, `SessionExpired`, `PaymentPending`.

## Visual language for Quran progress

Do not color Quran text itself as guilt/shame. Use progress states in adjacent metadata/chips (text and icon), moderate green, warm amber, neutral gray. Explanatory tooltip: `محتاج مراجعة` vs `مُثبت وفق آخر اختبار`. Confidence is a documented teacher rubric not numeric 'AI certainty'.

## Motion and usability

120–220ms interactions, respect reduced motion. Achievement microanimation gentle, no confetti overload, no streak anxiety. Success state uses text + icon. Dark mode opt-in; never force night mode when reading Quran. Forms autosave when complex with clear save status. Timer for assessments includes fair accommodations and pause policy.

## Brand imagery

Real teacher photos with explicit rights; modest, authentic educational settings, diverse adult ages, no generated fake testimonials or unverifiable credential badges. Optional abstract geometric illustration only as support; Quran content text from verified source.
