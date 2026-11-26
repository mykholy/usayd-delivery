# v1.2 user stories with acceptance criteria
> Every story is attached to a Jira issue, required API/UX capability and positive+negative test cases; use the Requirement ID as permanent trace key.

## FR-GEO-001 — Country hint only
**As:** guest,student. **Phase:** P0. **Priority:** Must.
**I want** Use coarse IP location as default storefront suggestion, never automatic billing identity.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Unknown or VPN country requires selector and does not block access.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Country is editable; no raw IP leaked into analytics.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-001-POS`, `TC-FR-GEO-001-NEG`.

## FR-GEO-002 — Market selector
**As:** guest,student. **Phase:** P0. **Priority:** Must.
**I want** Guest and learner may select supported market independently of browser locale.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Country is preserved across visits and profiles.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Switching market mid-checkout requires re-quote, not changing paid order.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-002-POS`, `TC-FR-GEO-002-NEG`.

## FR-GEO-003 — Market status workflow
**As:** regional_manager,compliance. **Phase:** P0. **Priority:** Must.
**I want** Countries progress draft/review/payment test/active/paused/retired.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Disabled country never offers chargeable plan.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Active country requires compliance and PSP signoffs.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-003-POS`, `TC-FR-GEO-003-NEG`.

## FR-GEO-004 — Market-limited catalogue
**As:** student,admin. **Phase:** P0. **Priority:** Must.
**I want** Program/bundle availability and content can vary by country.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Price cards reflect current market and version.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Unavailable program shows eligible alternative or waitlist.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-004-POS`, `TC-FR-GEO-004-NEG`.

## FR-GEO-005 — Country-specific price books
**As:** finance_manager. **Phase:** P0. **Priority:** Must.
**I want** Versioned, effective-dated amount_minor fixed by currency and program.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Existing invoices retain old price snapshot.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Overlapping published price windows rejected.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-005-POS`, `TC-FR-GEO-005-NEG`.

## FR-GEO-006 — Money minor-unit precision
**As:** finance_manager. **Phase:** P0. **Priority:** Must.
**I want** Support ISO fractions incl 3 decimals for KWD and BHD.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** KWD 7.500 has exactly 7500 minor units.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** No floats in ledger or charge validation.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-006-POS`, `TC-FR-GEO-006-NEG`.

## FR-GEO-007 — Billing country validation
**As:** student,finance_manager. **Phase:** P0. **Priority:** Must.
**I want** Ask/verify billing country separately from storefront and IP.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** PSP account and applicable tax policy selected by verified billing context.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Country mismatch requires explicit resolution, never silent rerouting.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-007-POS`, `TC-FR-GEO-007-NEG`.

## FR-GEO-008 — Price preview in admin
**As:** platform_admin. **Phase:** P0. **Priority:** Should.
**I want** Admin previews storefront for each country, language, currency and timezone.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Draft price preview never leaks publicly.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Unavailable PSP blocks preview checkout acceptance.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-008-POS`, `TC-FR-GEO-008-NEG`.

## FR-GEO-009 — Rate/provenance accounting
**As:** finance_manager. **Phase:** P1. **Priority:** Must.
**I want** Reporting FX rate, timestamp and source saved separately from fixed retail price.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Multi-currency report sums only using auditable conversions.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Stale exchange rate cannot silently reprice subscription.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-009-POS`, `TC-FR-GEO-009-NEG`.

## FR-GEO-010 — Market publication approvals
**As:** regional_manager,finance_manager. **Phase:** P0. **Priority:** Must.
**I want** Require finance and compliance authorization on market launch and price changes.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Proposer cannot act as all approvers.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Change log includes exact old/new values and effective time.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-010-POS`, `TC-FR-GEO-010-NEG`.

## FR-GEO-011 — Market pause continuity
**As:** platform_admin. **Phase:** P0. **Priority:** Must.
**I want** Paused country blocks new purchases but preserves legitimate existing lessons and refunds.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Existing entitlements and refund workflow remain accessible.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** No mass cancellation triggered automatically by market pause.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-011-POS`, `TC-FR-GEO-011-NEG`.

## FR-GEO-012 — Visitor city timezone
**As:** student. **Phase:** P0. **Priority:** Must.
**I want** Multiple timezone countries require city/IANA choice; country alone is insufficient.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** US user explicitly selects timezone when ambiguous.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Chosen timezone overrides country default.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-012-POS`, `TC-FR-GEO-012-NEG`.

## FR-GEO-013 — Price promo eligibility
**As:** finance_manager. **Phase:** P1. **Priority:** Must.
**I want** Coupons scoped by country/currency/plan and never exceed authorized discount caps.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Promo validates market and quote version server side.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Cross-currency coupon misuse denied.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-013-POS`, `TC-FR-GEO-013-NEG`.

## FR-GEO-014 — Country-specific payment methods
**As:** student,finance_manager. **Phase:** P0. **Priority:** Must.
**I want** Checkout displays only legal and configured methods for that merchant/charge currency.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Unsupported charge currency blocks checkout before PSP request.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Card never collected on our server.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-014-POS`, `TC-FR-GEO-014-NEG`.

## FR-GEO-015 — International refunds
**As:** finance_manager. **Phase:** P0. **Priority:** Must.
**I want** Refund in original charged amount/currency, preserve historic exchange rate and audit.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Original ledger remains immutable.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Staff cannot refund alternate currency without approved provider workflow.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-015-POS`, `TC-FR-GEO-015-NEG`.

## FR-GEO-016 — Localized marketing routes
**As:** marketing_admin. **Phase:** P1. **Priority:** Should.
**I want** Use /ar and /en with hreflang/canonical and locale-specific SEO copy.
**So that** the user receives a trustworthy, localized and controlled GEO experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Both locale pages render complete translated metadata.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Country choice does not create duplicate canonical mess.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-GEO-016-POS`, `TC-FR-GEO-016-NEG`.

## FR-TIME-001 — Explicit IANA zone preference
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** Save user timezone independent of locale and country.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Browser zone is suggested; user can override.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Invalid IANA zone rejected.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-001-POS`, `TC-FR-TIME-001-NEG`.

## FR-TIME-002 — Teacher local availability
**As:** teacher,operations_supervisor. **Phase:** P0. **Priority:** Must.
**I want** Recurring shifts entered in teacher local timezone, projected to UTC per occurrence.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Future DST changes maintain intended local shift wall clock.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Teacher cannot have overlapping booked sessions in UTC.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-002-POS`, `TC-FR-TIME-002-NEG`.

## FR-TIME-003 — UTC slot storage
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** All session instants and reminders authoritative UTC.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Cairo/Riyadh views represent same UTC instant.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Changing viewer timezone never edits session UTC start.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-003-POS`, `TC-FR-TIME-003-NEG`.

## FR-TIME-004 — DST nonexistent time
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** Nonexistent local clock times show error and valid alternatives.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Europe/London spring missing slot cannot be booked.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** No automatic silent shift.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-004-POS`, `TC-FR-TIME-004-NEG`.

## FR-TIME-005 — DST ambiguous time
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** Duplicated fall hour shows two UTC offsets and stores chosen one.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** America/New_York 01:30 duplicated hours shown distinctly.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Chosen instant remains stable after saving.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-005-POS`, `TC-FR-TIME-005-NEG`.

## FR-TIME-006 — Cross-market collision lock
**As:** operations_supervisor. **Phase:** P0. **Priority:** Must.
**I want** Teacher booked by different country clients cannot overlap actual UTC intervals.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Concurrent writes produce one booking and one conflict.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** No double debit on failed collision.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-006-POS`, `TC-FR-TIME-006-NEG`.

## FR-TIME-007 — Timezone notice copy
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** Lesson cards and reminders display local timezone label and UTC offset.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Arabic and English both show explicit time zone.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** No "UTC+2" fixed offset during DST periods.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-007-POS`, `TC-FR-TIME-007-NEG`.

## FR-TIME-008 — Timezone-aware reminders
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** T-24h/1h alerts scheduled on UTC, recipient quiet hours local.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Timezone preference edit does not duplicate reminder.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Suppressed alert not incorrectly marked delivered.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-008-POS`, `TC-FR-TIME-008-NEG`.

## FR-TIME-009 — ICS calendar invites
**As:** student,teacher. **Phase:** P1. **Priority:** Should.
**I want** Generate stable UID, cancellation and reschedule events, correct UTC times.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Google/Apple calendar display same instant.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Cancel sends SEQUENCE update, not new duplicate event.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-009-POS`, `TC-FR-TIME-009-NEG`.

## FR-TIME-010 — TZDB change audit
**As:** platform_admin. **Phase:** P1. **Priority:** Must.
**I want** Schedule audit after timezone rules change, flag impacted future bookings.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Job reports affected bookings and notification plan.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Booked UTC instant not silently adjusted.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-010-POS`, `TC-FR-TIME-010-NEG`.

## FR-TIME-011 — Teacher pay time accounting
**As:** finance_manager. **Phase:** P0. **Priority:** Must.
**I want** Payroll duration derived from approved attendance UTC, not local strings.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Two timezones produce same approved minutes.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Malformed client local clock cannot inflate pay.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-011-POS`, `TC-FR-TIME-011-NEG`.

## FR-TIME-012 — Regional working hours
**As:** operations_supervisor. **Phase:** P1. **Priority:** Should.
**I want** Region-specific legal/student safe-hours scheduling policies configurable.
**So that** the user receives a trustworthy, localized and controlled TIME experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Scheduling respects market rules and teacher shift.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Blocked off-hours slot cannot be forced by default.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-TIME-012-POS`, `TC-FR-TIME-012-NEG`.

## FR-I18N-001 — Complete Arabic and English key parity
**As:** student,admin. **Phase:** P0. **Priority:** Must.
**I want** No missing translations across web/mobile/admin, messages and forms.
**So that** the user receives a trustworthy, localized and controlled I18N experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** CI checks key and placeholder equality.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Untranslated keys fail release gate.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-I18N-001-POS`, `TC-FR-I18N-001-NEG`.

## FR-I18N-002 — RTL/LTR mirrored layout
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** Directional UI changes meaningfully with ar/en and maintains accessibility.
**So that** the user receives a trustworthy, localized and controlled I18N experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** All navigation/breadcrumb/drawer states tested at 360 and 1440.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Quran text and media play icon never mirrored incorrectly.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-I18N-002-POS`, `TC-FR-I18N-002-NEG`.

## FR-I18N-003 — Legal content localized review
**As:** content_localization_manager. **Phase:** P0. **Priority:** Must.
**I want** Billing consent and legal copy require human translation approval.
**So that** the user receives a trustworthy, localized and controlled I18N experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Approved versions traced to locale at acceptance.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Draft legal translation never shown in paid checkout.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-I18N-003-POS`, `TC-FR-I18N-003-NEG`.

## FR-I18N-004 — Quran text canonical isolation
**As:** academic_supervisor. **Phase:** P0. **Priority:** Must.
**I want** Quran verses always retrieved from verified licensed source, no generative replacement.
**So that** the user receives a trustworthy, localized and controlled I18N experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Language switch preserves canonical verse.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** AI-generated text never appears as verified Quran.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-I18N-004-POS`, `TC-FR-I18N-004-NEG`.

## FR-I18N-005 — Locale-suitable notifications
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** Emails/SMS/push messages and reminder times localized to recipient.
**So that** the user receives a trustworthy, localized and controlled I18N experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** English student gets English CTA and time labels.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Placeholder/plural correctness automatic checked.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-I18N-005-POS`, `TC-FR-I18N-005-NEG`.

## FR-I18N-006 — Language preference persists
**As:** student,teacher,admin. **Phase:** P0. **Priority:** Must.
**I want** Learner or staff can switch languages without altering country/currency/timezone.
**So that** the user receives a trustworthy, localized and controlled I18N experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** UI switch persists across login on web and Flutter.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Quote amount remains stable while switching language.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-I18N-006-POS`, `TC-FR-I18N-006-NEG`.

## FR-I18N-007 — Bidi-safe money and contacts
**As:** student,finance_manager. **Phase:** P0. **Priority:** Must.
**I want** Phone/email/invoice references isolated inside RTL; currency from Intl/CLDR.
**So that** the user receives a trustworthy, localized and controlled I18N experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Mixed Arabic/English field values appear in correct visual order.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Three-decimal KWD remains mathematically exact.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-I18N-007-POS`, `TC-FR-I18N-007-NEG`.

## FR-I18N-008 — Accessible localized reader
**As:** student. **Phase:** P1. **Priority:** Must.
**I want** Screen-reader labels, text scale, keyboard focus, Quran reading typography reviewed.
**So that** the user receives a trustworthy, localized and controlled I18N experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** WCAG AA manual test completed for core flows.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Reduced motion honored on competitions screens.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-I18N-008-POS`, `TC-FR-I18N-008-NEG`.

## FR-VPC-001 — Provider registry and account config
**As:** platform_admin. **Phase:** P0. **Priority:** Must.
**I want** Admin CRUD draft provider accounts, secret refs and regional eligibility.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** No credentials returned to client or logs.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Unconfigured account never routes production class.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-001-POS`, `TC-FR-VPC-001-NEG`.

## FR-VPC-002 — Capabilities verified per context
**As:** tech_ops. **Phase:** P0. **Priority:** Must.
**I want** Provider features tracked by market, platform, evidence and last verified time.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Google Meet unavailable raw-audio AI displays unsupported.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Unknown capabilities fail closed for sensitive processing.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-002-POS`, `TC-FR-VPC-002-NEG`.

## FR-VPC-003 — Provider selection routing rules
**As:** platform_admin. **Phase:** P0. **Priority:** Must.
**I want** Versioned routing priority by country, program and client.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** New lessons follow approved effective policy.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Existing active rooms remain bound to previous provider.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-003-POS`, `TC-FR-VPC-003-NEG`.

## FR-VPC-004 — Provider connection test
**As:** tech_ops. **Phase:** P0. **Priority:** Must.
**I want** Admin sandbox credentials test and sample room creation.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Result exposes status without secret or PII.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Failed test prevents production activation.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-004-POS`, `TC-FR-VPC-004-NEG`.

## FR-VPC-005 — Provider switch dry-run
**As:** platform_admin. **Phase:** P0. **Priority:** Must.
**I want** Previews affected lessons, capabilities and cost/region constraints.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Dry-run clearly reports unsupported Flutter/AI features.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** No room provisioning or customer notification in dry-run.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-005-POS`, `TC-FR-VPC-005-NEG`.

## FR-VPC-006 — Two-person provider publish
**As:** security_admin,platform_admin. **Phase:** P0. **Priority:** Must.
**I want** Approved config change scheduled and audited with MFA.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Requester cannot approve own activation.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Unauthorized activation denied, logged.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-006-POS`, `TC-FR-VPC-006-NEG`.

## FR-VPC-007 — Provider manual override
**As:** operations_supervisor. **Phase:** P1. **Priority:** Must.
**I want** Authorized operations can migrate future provisioned lesson with proper invalidation.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Affected parties receive updated join details.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Active mid-call session not silently migrated.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-007-POS`, `TC-FR-VPC-007-NEG`.

## FR-VPC-008 — Provider outage fallback
**As:** operations_supervisor. **Phase:** P0. **Priority:** Must.
**I want** Pre-join failover with locking or safe delay; recovery notification.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** No duplicate charged lessons/attendance.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Mid-call recovery requires explicit new join experience.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-008-POS`, `TC-FR-VPC-008-NEG`.

## FR-VPC-009 — Provider monitoring dashboard
**As:** platform_admin. **Phase:** P1. **Priority:** Must.
**I want** Health, cost/quota, active rooms, errors, routing history.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Stale monitoring marked stale instead of healthy.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Region restricted supervisors see only scoped metrics.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-009-POS`, `TC-FR-VPC-009-NEG`.

## FR-VPC-010 — Provider webhook normalize
**As:** engineer. **Phase:** P0. **Priority:** Must.
**I want** Verify signatures, dedupe by provider event ID, reconcile lesson facts.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Duplicate webhooks produce one attendance update.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Forged webhook does not mutate lesson.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-010-POS`, `TC-FR-VPC-010-NEG`.

## FR-VPC-011 — Provider URL/client join policies
**As:** student,teacher. **Phase:** P0. **Priority:** Must.
**I want** Embedded vs external mode returns correct join contract and labels.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Google Meet external route has explicit join instructions.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Unauthorized student cannot get token or meeting URL.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-011-POS`, `TC-FR-VPC-011-NEG`.

## FR-VPC-012 — Consent-aware recording controls
**As:** student,admin. **Phase:** P0. **Priority:** Must.
**I want** Recording/transcription/AI opt-in features require purpose and valid consent.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Withdrawal immediately disables future processing.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Provider switch never bypasses consent.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-012-POS`, `TC-FR-VPC-012-NEG`.

## FR-VPC-013 — Provider rollback
**As:** platform_admin. **Phase:** P0. **Priority:** Must.
**I want** Rollback routing rules for new lessons with immutable previous versions.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** History shows prior provider and policy version.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Rollback never deletes recorded attendance.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-013-POS`, `TC-FR-VPC-013-NEG`.

## FR-VPC-014 — Provider mobile parity
**As:** tech_ops. **Phase:** P1. **Priority:** Must.
**I want** Each provider client capability verified web, Android and iOS.
**So that** the user receives a trustworthy, localized and controlled VPC experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Unsupported mobile capability causes compatible alternative flow.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** App cannot claim verified status without device evidence.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-VPC-014-POS`, `TC-FR-VPC-014-NEG`.

## FR-SUP-001 — Scoped supervisor assignments
**As:** super_admin. **Phase:** P0. **Priority:** Must.
**I want** Supervisor access by region/program/cohort and temporary delegated grants.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Supervisor cannot see out-of-scope learner by guessing ID.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Expired grant instantly denied on API, not only UI.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-001-POS`, `TC-FR-SUP-001-NEG`.

## FR-SUP-002 — Academic approval queue
**As:** academic_supervisor. **Phase:** P0. **Priority:** Must.
**I want** Teacher-proposed plans/assessment reviewed and versioned by authorized academic supervisor.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Approve writes evaluator/time/plan version and teacher notification.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Proposer cannot bypass approval via API.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-002-POS`, `TC-FR-SUP-002-NEG`.

## FR-SUP-003 — Quality review workflow
**As:** quality_supervisor. **Phase:** P1. **Priority:** Must.
**I want** Qualified supervisor reviews samples lawfully and issues coaching notes.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Review queue filtered by assignment and valid purpose.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Accessing absent consent evidence denied.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-003-POS`, `TC-FR-SUP-003-NEG`.

## FR-SUP-004 — Safeguarding escalation
**As:** safeguarding_officer. **Phase:** P0. **Priority:** Must.
**I want** Case priority, protected evidence, human triage and escalation process.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Report creates private case with SLA and audit.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** AI flag alone does not trigger automatic punishment.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-004-POS`, `TC-FR-SUP-004-NEG`.

## FR-SUP-005 — Contest multi-judge approval
**As:** competition_manager,competition_judge. **Phase:** P1. **Priority:** Must.
**I want** Scoring, second review, conflict checks, publication, appeal handling.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Judge cannot score own learner and publish.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Minors leaderboard private or alias by approved policy.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-005-POS`, `TC-FR-SUP-005-NEG`.

## FR-SUP-006 — Finance separation of duties
**As:** finance_manager,finance_approver. **Phase:** P0. **Priority:** Must.
**I want** Payroll creator cannot approve same payrun; refunds similarly governed.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Maker-checker enforced on API.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Dual approval cannot be fulfilled with two roles of same human.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-006-POS`, `TC-FR-SUP-006-NEG`.

## FR-SUP-007 — Regional operations console
**As:** operations_supervisor. **Phase:** P0. **Priority:** Must.
**I want** Schedules, teacher capacity, no-show disputes, regional SLAs and alerts.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Supervisor can resolve assigned incident with auditable reason.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Cannot change teacher grades or payouts.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-007-POS`, `TC-FR-SUP-007-NEG`.

## FR-SUP-008 — Supervisor dashboard scope
**As:** academic_supervisor,operations_supervisor. **Phase:** P1. **Priority:** Must.
**I want** Role-specific KPI widgets and queues with least privilege.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Different supervisors see correct modules and data scopes.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Server enforces same permissions as UI nav.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-008-POS`, `TC-FR-SUP-008-NEG`.

## FR-SUP-009 — Break-glass access
**As:** safeguarding_officer. **Phase:** P0. **Priority:** Must.
**I want** Time-limited emergency access with reason/MFA and independent review.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Grant expires automatically and alerts separate reviewer.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** No silent/standing access to all recordings.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-009-POS`, `TC-FR-SUP-009-NEG`.

## FR-SUP-010 — Localization draft approval
**As:** content_localization_manager. **Phase:** P0. **Priority:** Must.
**I want** Translator cannot publish legal/Quran text without required academic/legal review.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Approved translation version indicated in settings.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Draft rejected for public route and app.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-010-POS`, `TC-FR-SUP-010-NEG`.

## FR-SUP-011 — Setting inheritance and version
**As:** platform_admin. **Phase:** P0. **Priority:** Must.
**I want** Global→region→program→cohort overrides with explicit precedence and rollback.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Admin preview shows inherited origin and effective version.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Conflicting concurrent save returns 409 and preserves history.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-011-POS`, `TC-FR-SUP-011-NEG`.

## FR-SUP-012 — Teacher compensation preview
**As:** finance_manager,teacher. **Phase:** P0. **Priority:** Must.
**I want** Simulate salary/shift/hour/session/hybrid rules with immutable payroll evidence.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Teacher sees own statement with approval and period.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Disputed attendance cannot auto-inflate pay.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-012-POS`, `TC-FR-SUP-012-NEG`.

## FR-SUP-013 — Market activation governance
**As:** regional_manager,compliance_officer. **Phase:** P0. **Priority:** Must.
**I want** Regional proposal with legal+finance approvals, test evidence and audit.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Unapproved country stays unavailable for payment.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Admin cannot activate by editing a frontend flag.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-013-POS`, `TC-FR-SUP-013-NEG`.

## FR-SUP-014 — Redacted support view
**As:** support_agent. **Phase:** P0. **Priority:** Must.
**I want** Support can handle bookings and tickets without protected audio or credentials.
**So that** the user receives a trustworthy, localized and controlled SUP experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Logs and exports redact sensitive data by role.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Support cannot retrieve raw transcript through alternate endpoint.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-SUP-014-POS`, `TC-FR-SUP-014-NEG`.

## FR-ENG-001 — Localized competitions
**As:** student,competition_manager. **Phase:** P1. **Priority:** Must.
**I want** Competitions support market and locale-specific time windows with UTC boundaries.
**So that** the user receives a trustworthy, localized and controlled ENG experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Leaderboard updates according to local display with same UTC deadline.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Late submissions rejected consistently across timezones.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-ENG-001-POS`, `TC-FR-ENG-001-NEG`.

## FR-ENG-002 — Adaptive review tests
**As:** student,academic_supervisor. **Phase:** P1. **Priority:** Must.
**I want** AI suggests practice exam from teacher-verified weakness categories.
**So that** the user receives a trustworthy, localized and controlled ENG experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Student sees goals and teacher-reviewed assessment criteria.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** AI output never auto-awards official mastery.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-ENG-002-POS`, `TC-FR-ENG-002-NEG`.

## FR-ENG-003 — Fair consented leaderboards
**As:** student,competition_manager. **Phase:** P1. **Priority:** Must.
**I want** Competitions default anonymous/private for minors and opt-in adults.
**So that** the user receives a trustworthy, localized and controlled ENG experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** Minor identity not public by default.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** Opt-out does not remove earned private progress.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-ENG-003-POS`, `TC-FR-ENG-003-NEG`.

## FR-ENG-004 — Retention without coercion
**As:** student. **Phase:** P1. **Priority:** Should.
**I want** Weekly progress, review reminders, gentle streak recovery, accessibility.
**So that** the user receives a trustworthy, localized and controlled ENG experience.
**Given** an authorized valid actor and a published configuration, **when** the feature is used, **then** No dark patterns or penalizing healthy breaks.
**Given** an invalid, stale or unauthorized state, **when** attempted, **then** No religious obligation messaging used to shame learner.
**Nonfunctional acceptance:** localized AR/EN; permission checked server side; audit event for mutations; mobile parity; response schemas and 4xx/409 states tested. **Evidence:** `TC-FR-ENG-004-POS`, `TC-FR-ENG-004-NEG`.
