# Executable-level business rules and negative-path decisions

## Enrollment & age
- BR-01 Every registrant creates learner identity; adult may act immediately following verification; legal-minor enrollment cannot join paid lesson until guardian consent has been verified where required.
- BR-02 Guardian consent is a separate record with purpose, policy version, country rule and timestamp; withdrawal halts optional audio AI immediately, while legal retention requests are handled by policy.
- BR-03 Do not expose a learner's birthdate to teacher; teacher sees only pedagogically necessary age band. Access tokens and sessions revoked after credential resets.

## Entitlements, bookings, time
- BR-04 Booking starts with `reserve` under DB lock and idempotency, then `confirm` after eligibility and credit reservation. A unique teacher-time slot invariant prevents double booking.
- BR-05 A failed external conferencing provider does not debit lesson entitlement as completed. Attendance confirmation requires join events or human-signed exception, not only page viewed.
- BR-06 Times stored UTC + original IANA timezone, DST transition ambiguity handled by explicit offset or next valid slot. Duration determined by package snapshot at purchase.
- BR-07 Reschedule policy version pinned per booking; teacher no-show, learner no-show, technical interruption and emergency have distinct credit/refund rules.
- BR-08 Cancellation and compensation settlement each create immutable journal entries; never update old payment or pay accrual in place.

## Teaching, evaluation, Quran source
- BR-09 No automatic final Tajweed grade, Quran citation or mastery verdict from AI. Correct readings/verses anchored in verified approved reference and riwaya.
- BR-10 Memory map mastery requires documented teacher-approved evidence and rubric version; practice-only progress marked as self-reported/provisional.
- BR-11 Adaptive revisions can suggest due dates but cannot silently erase an approved teacher plan; every adjustment versioned with explanation and manual override.

## Exams, contests
- BR-12 Exam timing uses server authority; transient offline answers checkpoint locally then reconcile with attempt version; no double submission, reveal or scoring leak.
- BR-13 Contest registration eligibility snapshot fixed at registration, revalidate if suspended/safety gate; ranking compares same rubric/level; no paid boost.
- BR-14 Provisional results visible only to participants under privacy mode; final publication requires academic sign-off, appeals window and minor safety rules.
- BR-15 Appeal reviewer independent; score correction appends new approved version and updates rewards ledger idempotently.

## Teacher operations
- BR-16 Compensation rule effective date pinned to each delivered lesson and contract snapshot; support per-lesson, per-minute, per-shift, monthly salary and hybrid minimum guarantee.
- BR-17 Same lesson cannot be paid twice; payroll has draft→reviewed→approved→paid→reconciled, with maker/checker separation.
- BR-18 Approved payroll cannot be silently edited; adjustments carried in next period and audited.

## AI/audio/media
- BR-19 No audio forwarding to AI by default; per-purpose consent and eligibility checked in each processing job and rechecked before execution; revocation cancels queued jobs.
- BR-20 Policy flag is an *unverified signal*, never an accusation; only authorized safeguarding staff can review restricted evidence; no automated dismissal.
- BR-21 Provider without raw-audio capability must return unsupported and disable transcript/AI; never create covert client capture as fallback.
- BR-22 Video/meeting recording retention tied to purpose/license/consent; links short lived; prevent public indexing.

## Support, privacy, localization
- BR-23 Full audit for overrides/refunds/guardian approval/provider switch/teacher pay/contest score.
- BR-24 Arabic RTL and English LTR; Quran text direction is independent of surrounding interface. All formatted dates/times/currencies localized, amounts persisted in ISO currency minor units.
- BR-25 Avoid revealing student/teacher contact data in chat, screens, exports, admin analytics or public leaderboard; feature-safe redaction and moderator route for concerns.
