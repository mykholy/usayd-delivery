# Premium screen specifications — v1.2 addition
Screens are **specifications, not Figma frames or implemented routes**. Every screen has RTL and LTR, plus responsive 360/390/768/1440 variants and tested a11y.

## UX-GLOB-001 — Country & Currency Selector
**Persona:** PUBLIC · **Route:** `/choose-country` · **Phase:** P0.
**User goal:** Select storefront market; verify unsupported market.
**Hero / action:** Confirm country.
**Component contract:** country search, flag icon, currency label, availability badge, selected state, help, waitlist.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-002 — Localized Pricing Comparison
**Persona:** PUBLIC · **Route:** `/pricing` · **Phase:** P0.
**User goal:** Review localized offers and exact price/currency.
**Hero / action:** Choose plan.
**Component contract:** market bar, plan comparison, VAT note, curriculum, currency, renewal terms, switch market.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-003 — Unavailable Country & Waitlist
**Persona:** PUBLIC · **Route:** `/unavailable-market` · **Phase:** P1.
**User goal:** Capture interest without taking payment.
**Hero / action:** Join waitlist.
**Component contract:** country illustration, clear unavailable explanation, no fake prices, privacy consent.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-004 — Language & Regional Preferences
**Persona:** STUDENT · **Route:** `/me/preferences/region` · **Phase:** P0.
**User goal:** Save independently locale/market/timezone.
**Hero / action:** Save preferences.
**Component contract:** country selector, language segmented, IANA zone dropdown, preview dates, currency notice.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-005 — Timezone Preview & DST Warning
**Persona:** STUDENT · **Route:** `/me/schedule/timezone-preview` · **Phase:** P0.
**User goal:** Resolve ambiguous/nonexistent booking local time.
**Hero / action:** Pick valid instant.
**Component contract:** local calendar, UTC offset, timezone comparison, DST alternatives, info icon.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-006 — Regional Checkout Quote
**Persona:** STUDENT · **Route:** `/checkout/:quoteId` · **Phase:** P0.
**User goal:** Understand merchant, currency, taxes and quote expiry.
**Hero / action:** Pay securely.
**Component contract:** quote breakdown, locale switch, billing country, PSP methods, data/privacy notice.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-007 — Renewal Price Change Notice
**Persona:** STUDENT · **Route:** `/me/subscriptions/:id/renewal` · **Phase:** P1.
**User goal:** Review and consent to new regional price version.
**Hero / action:** Accept renewal terms.
**Component contract:** old vs new, date of effect, currency, cancel option, FAQ.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-008 — Timezone Availability Editor
**Persona:** TEACHER · **Route:** `/teacher/availability` · **Phase:** P0.
**User goal:** Edit recurring slots in teacher home timezone.
**Hero / action:** Save availability.
**Component contract:** weekly grid, exceptions, DST preview, region students, conflicts, time zone badge.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-009 — Cross Timezone Lesson Details
**Persona:** TEACHER · **Route:** `/teacher/lessons/:id` · **Phase:** P0.
**User goal:** Understand exact instant in teacher zone and learner zone.
**Hero / action:** Join lesson.
**Component contract:** dual time display, timezone switch, student plan, join button, reschedule.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-010 — Markets Overview
**Persona:** ADMIN · **Route:** `/admin/markets` · **Phase:** P0.
**User goal:** Supervise country launch states and compliance.
**Hero / action:** Create draft market.
**Component contract:** market table, approval chips, gateway/currency badges, filters, audit.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-011 — Market Launch Wizard
**Persona:** ADMIN · **Route:** `/admin/markets/new` · **Phase:** P0.
**User goal:** Propose and approve new country launch.
**Hero / action:** Submit for review.
**Component contract:** country, allowed legal entity, PSP, currencies, tax, privacy, staged approval.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-012 — Country Pricing Matrix
**Persona:** ADMIN · **Route:** `/admin/pricing/matrix` · **Phase:** P0.
**User goal:** Manage price books and preview locale/currency pricing.
**Hero / action:** Create price draft.
**Component contract:** market rows, package cols, amount_minor, effective date, currencies, compare.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-013 — Price Approval & Version Diff
**Persona:** ADMIN · **Route:** `/admin/pricing/approvals/:id` · **Phase:** P0.
**User goal:** Approve proposed localized pricing safely.
**Hero / action:** Approve/reject.
**Component contract:** old/new price, quote impact, tax/merchant, approvals, comments, dual control.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-014 — Merchant Profiles
**Persona:** ADMIN · **Route:** `/admin/payments/merchant-profiles` · **Phase:** P0.
**User goal:** Configure PSP eligibility by legal entity/country.
**Hero / action:** Test sandbox.
**Component contract:** redacted merchant ID, currencies, key reference, payout currency, test badge.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-015 — FX Reporting & Settlement
**Persona:** ADMIN · **Route:** `/admin/finance/fx` · **Phase:** P1.
**User goal:** Trace reporting conversion rates and settlement currencies.
**Hero / action:** Export finance summary.
**Component contract:** FX source, as-of time, currencies, originals, reconciliation differences.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-016 — Regional Schedule Dashboard
**Persona:** ADMIN · **Route:** `/admin/operations/timezones` · **Phase:** P0.
**User goal:** Manage cross-country booking capacity and conflicts.
**Hero / action:** Resolve collision.
**Component contract:** world clocks, UTC timeline, teacher lanes, conflict chips, locale previews.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-GLOB-017 — Flutter Region & Language
**Persona:** MOBILE · **Route:** `mobile://settings/region` · **Phase:** P2.
**User goal:** Country language timezone without forced account parent relation.
**Hero / action:** Save.
**Component contract:** country, locale, IANA zone, currency, quote refresh guard.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-001 — Video Providers Overview
**Persona:** ADMIN · **Route:** `/admin/settings/video-providers` · **Phase:** P0.
**User goal:** Set primary vendor and inspect capability/health.
**Hero / action:** Configure vendor.
**Component contract:** provider icons, status, region, active sessions, cost, limits, last check.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-002 — Video Provider Credentials
**Persona:** ADMIN · **Route:** `/admin/settings/video-providers/:id/credentials` · **Phase:** P0.
**User goal:** Manage secret vault references safely.
**Hero / action:** Rotate/validate.
**Component contract:** masked secret reference, environment, connection test, MFA challenge, audit.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-003 — Video Provider Capabilities
**Persona:** ADMIN · **Route:** `/admin/settings/video-providers/:id/capabilities` · **Phase:** P0.
**User goal:** Check per-device per-market capabilities and evidence.
**Hero / action:** Run verified PoC.
**Component contract:** matrix, unknown/unsupported/verified states, timestamps, source links.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-004 — Video Routing Rules
**Persona:** ADMIN · **Route:** `/admin/settings/video-routing` · **Phase:** P0.
**User goal:** Order vendor preferences by market and class.
**Hero / action:** Edit draft policy.
**Component contract:** drag priorities, filter, required capability, effect time, retry/fail closed.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-005 — Video Switch Impact & Dry-run
**Persona:** ADMIN · **Route:** `/admin/settings/video-routing/dry-run` · **Phase:** P0.
**User goal:** Preview affected future lessons and blocked features.
**Hero / action:** Run test.
**Component contract:** impact counts, capabilities, mobile parity, unsafe changes, diff.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-006 — Video Routing Approval
**Persona:** ADMIN · **Route:** `/admin/settings/video-routing/approvals/:id` · **Phase:** P0.
**User goal:** Two-person signoff for new active routing version.
**Hero / action:** Approve rollout.
**Component contract:** MFA, two reviewers, dry-run evidence, effective instant, rollback.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-007 — Video Provider Monitoring
**Persona:** ADMIN · **Route:** `/admin/monitoring/video` · **Phase:** P1.
**User goal:** Inspect provider health, room counts and incident backlog.
**Hero / action:** Open incident.
**Component contract:** health timeline, webhook queue, redacted events, cost and quotas.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-008 — Video Failover Incident Console
**Persona:** ADMIN · **Route:** `/admin/operations/video-incidents/:id` · **Phase:** P0.
**User goal:** Recover class safely if meeting provider fails.
**Hero / action:** Create replacement.
**Component contract:** participant notices, status, old binding, new binding, refund options, audit.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-009 — Embedded vs External Prejoin
**Persona:** STUDENT · **Route:** `/lessons/:id/prejoin` · **Phase:** P0.
**User goal:** Enter according to actual provider mode and capabilities.
**Hero / action:** Join.
**Component contract:** mic/camera, timezone, provider badge, consent, external explanation.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-VPC-010 — Teacher Provider Join Health
**Persona:** TEACHER · **Route:** `/teacher/lessons/:id/join` · **Phase:** P0.
**User goal:** Check audio quality and available classroom tools.
**Hero / action:** Join as teacher.
**Component contract:** device permission, connection test, unsupported AI warning, support.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-001 — Supervisor Home
**Persona:** SUPERVISOR · **Route:** `/supervisor` · **Phase:** P0.
**User goal:** Role-scoped queues, alerts and academic actions.
**Hero / action:** Open assigned queue.
**Component contract:** cards, permissions, next actions, SLA, no finance data when unauthorized.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-002 — Academic Plans Approval
**Persona:** SUPERVISOR · **Route:** `/supervisor/academic/plans` · **Phase:** P0.
**User goal:** Review AI-drafted/teacher-proposed plans.
**Hero / action:** Approve/reject.
**Component contract:** learner rubric, teacher evidence, diff, AI disclaimer, change request.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-003 — Quality Observation Queue
**Persona:** SUPERVISOR · **Route:** `/supervisor/quality/observations` · **Phase:** P1.
**User goal:** Assess permitted teacher-class quality samples.
**Hero / action:** Record coaching.
**Component contract:** role purpose, assignment, lawful evidence, rubric, escalation.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-004 — Safeguarding Case Console
**Persona:** SUPERVISOR · **Route:** `/supervisor/safeguarding/cases` · **Phase:** P0.
**User goal:** Triage protected minor and misconduct reports.
**Hero / action:** Escalate safely.
**Component contract:** private case table, severity, minimal evidence, break-glass log.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-005 — Competition Moderation
**Persona:** SUPERVISOR · **Route:** `/supervisor/competitions` · **Phase:** P1.
**User goal:** Contest eligibility judging appeals and minors privacy.
**Hero / action:** Assign judges.
**Component contract:** rounds, conflict checks, scoring rubric, appeals, anonymity.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-006 — Operations Coverage Board
**Persona:** SUPERVISOR · **Route:** `/supervisor/operations/schedule` · **Phase:** P0.
**User goal:** Teacher schedules absences cover and no-show disputes.
**Hero / action:** Assign replacement.
**Component contract:** shifts, UTC/local timeline, teacher load, audit, notices.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-007 — Regional KPI & Enrollment
**Persona:** SUPERVISOR · **Route:** `/supervisor/regions` · **Phase:** P1.
**User goal:** Country/cohort revenue and learning QA with scopes.
**Hero / action:** View cohort.
**Component contract:** filter region, cohort, paid conversion, churn, no exposed PII.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-008 — Role Assignments & Scopes
**Persona:** ADMIN · **Route:** `/admin/security/supervisors` · **Phase:** P0.
**User goal:** Add scoped staff privileges with expiry/MFA.
**Hero / action:** Request access.
**Component contract:** role builder, region/program scopes, approval chain, expiry, revoke.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-009 — Audit and Break-glass Review
**Persona:** ADMIN · **Route:** `/admin/security/access-audits` · **Phase:** P0.
**User goal:** Investigate privileged data access and emergency grants.
**Hero / action:** Review incident.
**Component contract:** redacted timeline, purpose, actor, alerts, revocation.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-010 — Settings Registry
**Persona:** ADMIN · **Route:** `/admin/settings` · **Phase:** P0.
**User goal:** Configure settings by global/market/program precedence.
**Hero / action:** Create draft.
**Component contract:** search, inheritance breadcrumb, publish diff, scope icon, approval.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-SUP-011 — Localization Content Studio
**Persona:** ADMIN · **Route:** `/admin/content/translations` · **Phase:** P1.
**User goal:** Create and approve bilingual copies and legal strings.
**Hero / action:** Submit translation.
**Component contract:** AR/EN split editor, namespace, review badge, placeholders, preview.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-ENG-001 — Competition Localized Schedule
**Persona:** STUDENT · **Route:** `/competitions/:id/schedule` · **Phase:** P1.
**User goal:** Show time zone aware rounds and deadline rules.
**Hero / action:** Register.
**Component contract:** round timeline, UTC and local label, leaderboard consent.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-ENG-002 — Adaptive Practice Brief
**Persona:** STUDENT · **Route:** `/study/practice/recommended` · **Phase:** P1.
**User goal:** Practice weak Quran sections based on teacher-verified evidence.
**Hero / action:** Start practice.
**Component contract:** strength map, evidence, AI disclaimer, teacher rubric, accessible controls.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.

## UX-ENG-003 — Gentle Progress & Streak Recovery
**Persona:** STUDENT · **Route:** `/me/progress/weekly` · **Phase:** P1.
**User goal:** Maintain positive motivation without punitive gamification.
**Hero / action:** Set weekly goal.
**Component contract:** achievement, due review, missed week recovery, accessible celebration.
**All states:** Default; Loading; Empty; Validation error; Unauthorized; No network; API timeout; Locale AR/EN; Small mobile; Keyboard focus; Permission denied; Pending review.
**Flow detail:** load role-scoped data → show defaults/suggested values with source → user edits draft → inline validation → server preflight & confirmation → transaction/approval → success notification + audit; on failure preserve safe draft, show actionable retry.
**Security & privacy:** no secrets or unauthorized sensitive data; market and provider operations require admin permissions and step-up approval; finance screens show quote amounts in verified charge currency.
**Mobile UX:** collapse heavy tables into searchable cards and filters; use bottom sheet for selectors; disable impossible action while keeping explanation and support entry.
