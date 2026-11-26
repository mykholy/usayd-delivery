# UX master specification — platform and mobile
**Design lead approval required** | **Style:** calm, premium, contemporary Islamic-inspired design, *not* a copied religious template, no over-decoration.

## Information architecture

### Public
Header: Programs / How it works / Teachers / Pricing / Competitions / FAQ / Language / Login / CTA Assessment. Footer: contact, verified academic standards, refund policy, privacy/terms, accessibility.

### Learner side nav
Today / My Learning Plan / Memorization Map / Daily Study / Revisions / Lessons & Calendar / Exams / Competitions / Recorded Library / AI Study Companion / Achievements / Billing / Support / Settings.

### Teacher nav
Today / My Calendar / Students / Assessment / Plans To Review / Lesson Reports / Contests/Judging / Pay Statements / Support / Settings.

### Admin nav (role-specific)
Executive / CRM / Learners / Guardian Consents / Teachers & Contract / Programs & Quran Text / Lessons & Video / Assessments & Questions / Learning AI / Competitions & Judging / Finance & Payroll / Support & Safeguarding / Content / Analytics / Audit & Settings.

### Flutter bottom tabs
Student: Today, Plan, Lessons, Challenges, Profile; secondary screens via contextual navigation. Teacher: Today, Calendar, Learners, Reports, Account. No admin full parity promised for Flutter in first mobile release.

## Primary learner journey — first paid lesson

1. Marketing campaign landing with clear price proof, teacher bio and outcome.
2. Unified learner registration in 1–2 minimal steps. Age band only when required; minors go to consent verification gate, no parent portal demanded.
3. Initial assessment booking, including time zone and teacher availability. Consent and device check.
4. Teacher conducts assessment and submits approved rubric; learner can view why level was assigned.
5. Program offer and schedule with price/lesson count/refund terms transparent. Payment status follows signed webhook, not redirect.
6. Lesson prejoin camera/mic/connection test and policy notices. For Meet/Zoom external use clear opening and return action.
7. During class: Quran reading workspace, segment mark, task note and optional role-based AI status. Teacher-only rating not shown as final mid-call.
8. After: approved report, clear daily tasks, practice, revision queue, next lesson and optional contest path if eligible.

## Primary competition journey

1. Eligibility card (level, age band, terms) → detail with round timeline, fairness, privacy and scoring.
2. One-tap opt-in registration after legal/guardian gates → preparation checklist.
3. Open round: accessible interactive quiz or schedule live recital (teacher judge). Save draft, handle reconnection and time server-side.
4. Submission receipt immutable → judging queue → provisional feedback (no premature winners) → results with own breakdown/private standings.
5. If appeal allowed, file reason and see progress → verified decision/score revision → academy certificate/educational reward.

## Primary teacher journey

1. Onboard: apply, upload qualification, complete safeguarding checks, sign effective-dated contract and training.
2. Today: slots/calls, prelesson brief, assigned tasks with time budgets.
3. Prejoin with session info/verified Quran references, lesson curriculum and revision targets.
4. Classroom: video controls + Quran + structured rubric quick actions; avoid complex windows or multiple copy/paste fields.
5. Post class: report prepared from form, optional AI suggestion clearly labeled, teacher confirms and publishes.
6. Finance: see eligible minutes/lessons, model version, bonuses, manual adjustments, payout and dispute.
7. Competition judge: eligibility, blind scores as appropriate, rubric criteria, conflict declaration, draft, second review and appeal.

## Admin/operations journey

KPI exception panel → pick issue → open evidence/role-scoped record → safe action with reason → audit log → affected learner/teacher notice. Preserve context; use side panels for quick fixes and full pages for complex teacher contract, contest builder and safeguarding.

## Detailed flagship screen layouts

### 1. Learner Today (1440)
Sidebar 248; center content 8-column grid; top row next lesson prominent with teacher, join state and timezone; adjacent due-revision ring and weekly plan progress based on actual approved results; below study tasks sorted by due urgency, recent academic feedback and eligible competition card; right column compact AI recommendations with citations. On 390, next lesson first, then due revision, plan, challenges, AI; bottom sticky tab navigation, no overloaded metrics.

### 2. Smart Quran Classroom
Layout switch between teacher video focus + Quran workspace (teacher shares passage/ayah/highlight) and compact mobile stacked sheets; prejoin tests and privacy note; call timer and connection indicator; teacher rubric tool in privileged drawer; student cannot access other users' camera streams; chat/links limited by provider. Always reveal external-meeting limitations. Show visible consented recording indicator only when active.

### 3. Memory Map
Juz/surah chapter index with statuses: `not_started`, `in_progress`, `review_due`, `verified`, `needs_strengthening`; color + icon + text, no color-only state; tap opens verse-range details with last verified rubric and next due; source Quran text consistent; user can filter by review urgency.

### 4. Adaptive Exam
Instructions, purpose, level, permitted retries and timing; accessible question types; navigation, autosave local/remote draft (subject to security), explicit submit confirmation; timeout policy server-side; results show skill-specific improvement and rationale, never AI certainty masquerading as evaluation.

### 5. Competition Control Room
Admin tabs: Setup/Eligibility/Rounds/Participants/Submissions/Judges/Scores/Appeals/Prizes/Analytics. Show current state, pending review count, policy constraints. No Publish until academic/legal gates met and scores independently reviewed. Guardian/privacy overlays on minors' public profile fields.

### 6. Teacher Compensation Builder
Contract type selector salary/hour/lesson/shift/hybrid; live sample calculation and warning for contradictory rules; effective dates, state, jurisdiction, version history; financial approval with independent signoff; no retroactive rewriting paid statements.

### 7. AI Session Review
Restricted queue shows consent scope, event category, transcript excerpt masked, speaker confidence/limitations, time anchor, human decision buttons and appeal. No automatic ban; restricted access, retention timer, dual review when safeguarding is involved.

## Cross-platform UX rules

- Arabic-first naturally readable typography; Quran text uses a verified Quran-capable font in product but font licensing must be checked. Figma delivery uses font *names/recommendations*, never redistributes font files.
- Error variants: no internet, out of credits, provider failure, consent pending, teacher canceled, payment pending, contest ineligible, appeal closed, AI unavailable, content not licensed.
- All events/billing copy differentiated between actual and demo sample. Accessible contrast, touch target, focus, disabled explanation and dark-mode optional.
- No manipulative streaks or shame/leaderboard for minors. Respect notification quiet hours and opt-out.
- Avoid forcing camera where audio-only suffices and policy permits; ensure comfortable poor-network experience.

## UX deliverables for Figma

1. Sitemap / role navigation boards and user journey map.
2. Tokens/variables styles in AR/EN, light/dark and density.
3. Library with states and variants, auto-layout components, design-to-dev naming.
4. Hi-fi desktop, tablet, mobile frames for each critical screen; mobile native frames for separate flows.
5. Functional clickable prototypes with success/empty/denied/provider-failure variants.
6. Annotations linking each screen to `UX-*` and `FR-*` and critical API endpoints.
