# Premium UI/UX art direction & component handoff (Figma)

## Positioning
A premium, trustworthy online Quran academy for adults and minors with an **unobtrusive, calm** visual character. Not a templated generic LMS, not an over-ornamented mosque-style page, and no fake academic claims. Refined editorial hierarchy; clear action; useful data and respectful Quran typography. Use **design tokens** and component variants to demonstrate production quality, not only high-fidelity screenshots.

## Visual identity starting tokens (proposals, test accessibility)
Primary deep ink green `#102E2B`; primary verdigris `#176B60`; secondary `#2E8A7D`; restrained gold `#B58B49`; canvas `#F7FAF8`; white surface `#FFFFFF`; dark text `#172726`; subtle border `#DDE7E3`; neutral shadow. Support true dark mode separately, not merely invert. Define semantic states success/warning/danger/information/focus and contrast-check all combinations at WCAG 2.2 AA.

Typography: interface Arabic Tajawal/IBM Plex Sans Arabic (license review), English Inter; Quran rendering with **approved Quran text and typeface separate**. Logical CSS directions rather than left/right hardcoding. Icon family Lucide or phosphor, licensed, with consistent optical size 20/24 px, meaningful semantic mapping, not decorative overuse.

## Figma files / pages and ordering
`00 Cover & Decisions`, `01 Brand Tokens`, `02 UI Foundations`, `03 Components`, `04 Public Website`, `05 Onboarding & Markets`, `06 Learner Web`, `07 Teacher Web`, `08 Supervisor Portal`, `09 Admin`, `10 Competition/AI`, `11 Flutter Mobile`, `12 RTL-LTR Comparisons`, `13 Interaction Prototypes`, `14 Error/Empty/Edge States`, `15 Accessibility Review`, `16 Developer Handoff`.

## Component library definitions
- `BrandHeader`, `LocaleSwitch`, `CountryCurrencySwitch`, `TimezoneChip`, `CurrencyPrice`, `MarketDisabledBanner`, `MarketPriceComparison`, `LocalizedQuote`, `DualApprovalStatus`, `ConfigDiffViewer`, `VersionHistory`.
- `PrimaryButton`, `SecondaryButton`, `IconButton`, `SegmentedControl`, `Menu`, `Select`, `SearchableCombo`, `TimeZonePicker`, `DateTimePickerDST`, `Calendar`, `RangePicker`, `Skeleton`, `InlineError`, `Toast`, `ConfirmationModal`.
- `ResponsiveDataTable`, `SortableMobileCards`, `KPIOverviewCard`, `AuditTimeline`, `RoleScopeTree`, `SupervisorQueue`, `AssignmentChip`, `EscalationCard`.
- `ProviderCard`, `ConnectionTest`, `ProviderCapabilityGrid`, `ProviderRoutingPriority`, `RoutingDryRun`, `HealthAlert`, `FailoverRecovery`, `SecurePreJoin`, `ExternalMeetHandoff`.
- `QuranReader`, `SurahNavigator`, `AyahHighlight`, `MemoryMap`, `ReviewDue`, `AIRecommendationEvidence`, `AcademicApprovalCard`, `AssessmentRubric`, `ContestRound`, `LeaderboardAlias`, `AppealReview`.
- `TeacherAvailability`, `DualZoneLessonCard`, `LearnerToday`, `LessonProgressReport`, `PhoneNumberMasked`, `ConsentStatus`, `InvoiceMoney`, `SubscriptionPlanCard`.

Each: props, variants, responsive breakpoints, keyboard focus, reduced motion, disabled/error/loading/empty/success and AR/EN mirror. Provide compositional examples on desktop and mobile.

## High-value design patterns
### Marketing premium home
Large editorial hero, qualified teacher proof, "How it works" 3 steps, honest screenshot of learning map, pricing tied to selected market and currency, timezone indicator where booking preview, security and privacy trust, FAQ, strong "Book assessment" CTA. Avoid meaningless quote/video generated from fake customers. Hero uses genuine licensed editorial assets, not generic mosque wallpaper or AI-generated claims.
### Learner dashboard
Next lesson with local time+timezone, progress summary, due reviews, AI study card flagged as suggestion, current track with teacher-approved milestone, one gentle competition invitation, upcoming schedule and subscription status. Mobile bottom nav 4–5 elements.
### Teacher dashboard
My schedule (teacher local), assigned learners with level, pre-lesson notes, inline Quran tools, attendance, assessment drafts, payment preview and compliance reminders. Avoid PII.
### Supervisor dashboard
Relevant assigned queues first; approvals and deadlines, scoped region/program filters, incidents visibly restricted, no inappropriate learner details in list view.
### Admin
Settings discoverability, country matrix, international price approval with currency, video provider list and switch wizard, roles/supervisors, localized content, payment reconciliation and operational KPI, neutral audit links.

## Internationalization UX screens
Users see persistent language toggle AR/EN and transparent country selector. When market changes, show what changed: package availability/charge currency, not language or timezone. Timezone chosen separately with searchable IANA/city labels, saved preference and local preview. A countdown to booked lesson is computed against UTC. Avoid false "open now" information.

## Visual references to hand Claude (not external source assets)
A polished education SaaS with generous white space, refined glass-free cards, subtle Islamic geometric line accents in hero/background only, editorial typography, chart minimalism, balanced border and whitespace. Avoid fake photos, fabricated teacher credentials, illegible Arabic text or unlicensed Quran verse photography. Use real licensed brand/teacher pictures once delivered by product owner; until then use clearly labeled neutral placeholders in Figma.

## Figma QA acceptance
- All 160+ catalogued views exist as frames/spec variants or mapped reusable composites (don't fake a count with duplicate frames); critical 30+ scenarios have clickable prototype.
- 360/390/768/1440, Arabic RTL and English LTR, light/dark if scope approved; mobile landscape in classroom.
- Prototype start-to-end journeys for market selection→checkout, learner assessment→plan, provider switch→new join, supervisor approval, competition appeal, time change DST.
- Contrast+focus+screen-reader review notes; no placeholder lorem ipsum; Quran text sourced only from approved corpus or labeled placeholder.
- Handoff names/frame IDs correspond to `Screen ID` registry and a components page with variables/tokens, not just exported PNGs.
- Error/empty/loading/offline/privacy restriction states per screen documented.
