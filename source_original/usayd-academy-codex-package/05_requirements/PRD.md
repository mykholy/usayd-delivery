# PRD — Product Requirements Document
**Owner:** Product Manager | **Version:** 1.0 | **Market:** Egypt, Saudi test, expansion later

## Product narrative
The learner registers with one unified profile and can learn either as an independent adult or as a minor with mandatory guardian consent controls. The academy provides a qualified teacher, live classroom, curated Quranic content, assessment-driven study plan, revisions, practice, competitions, quality assurance and ongoing coaching. All clients (web, Flutter mobile, admin) call a versioned REST API. Video and payment vendor dependencies are abstracted, but their capabilities cannot be assumed identical.

## Personas and jobs to be done

| Persona | Need | Primary job | Risk |
|---|---|---|---|
| Adult beginner | Understand starting level | Schedule lessons and see non-intimidating progress | Drop out after first week |
| Adult reviewer | Retain old memorization | Rehearse weak passages and pass periodic assessment | False mastery claims |
| Minor learner | Age-appropriate lessons | Attend safely and progress | Consent and abuse |
| Teacher | Prepare/teach/report efficiently | Reliable schedule and fair pay | Admin overload |
| Academic supervisor | Ensure correct and fair learning | Approve programs, assessments, contests and AI | Hallucinated religious content |
| Support operator | Resolve appointments/technical problems | Refund/credit with evidence | Excess permissions |
| Finance officer | Collect/reconcile/payout | Accurate ledger and contractual pay | Duplicate payments |
| Executive | Scale profitably and ethically | Monitor cohort unit economics and safety | Misleading dashboards |

## North-star and supporting metrics

Primary: `Retained Paying Learners with Verified Learning Activity (RPL-VLA)`: paid learner with at least one approved lesson/practice evidence within recent active cycle and a subsequent renewal. Report numerator and denominator per cohort; never confuse time spent with learning outcomes.

Secondary: CAC payback months, verified revision improvement by rubric, teacher slot utilization, first lesson latency, completion rate, renewal rate. Guardrails: safeguarding incidents, appeals overturn, AI false positives, refund rate, chargebacks and low-bandwidth failures.

## Core journeys

- Discovery → lead → trial assessment → learner enrollment and consent → package → payment → schedule → join → report → review → renewal.
- Adult independently joins without a guardian; minor may not access restricted paid processing before valid guardian authorization.
- Teacher application → vetting → availability → assigned cohort → classroom → reporting → approved compensation → payouts.
- Competition discovery → eligibility → register → tasks/tests or supervised recitation → human judge → moderated standings → appeals → final awards → reflective revision plan.
- Learner receives weakness assessment → AI suggestion grounded in recorded evaluations → teacher approval → adaptive assignments → next assessment → plan comparison.

## Product invariants

1. Content of the Quran must be sourced from a verified source with explicit recitation/riwaya; no model-generated authoritative verse text.
2. Every lesson belongs to exactly one learner/group session, subscription entitlement and a provider instance; provider IDs are not source-of-truth for educational progress.
3. Grade state `published` requires authorized teacher/supervisor review for oral recitation and sensitive quality claims.
4. Competition results cannot be edited after published without versioned correction and notice.
5. Every money mutation has ledger/audit and idempotency; teacher payout uses immutable effective-dated contract snapshot.
6. All stored AI summaries reference authorized evidence, model/prompt version, consent status and human reviewer if applicable.
7. Withdrawn consent blocks future optional audio analysis, and triggers applicable retention/deletion workflow.
8. Learning streak never penalizes absence or becomes a gateway to academic success or prizes.

## Release slices

| Slice | Customer value | Required modules | Gate |
|---|---|---|---|
| R0 Foundation | Can sign up, be safely verified and browse programs | IAM, PROF, CURR, TCHR | security/legal/academic |
| R1 Paid pilot | Can pay/book/attend/get approved report and request help | PAY, BOOK, VIDEO, ATT, ADMIN, NOTIF, CRM | end-to-end paid UAT |
| R2 Learning product | Personal plan, revision, practice and assessment | ASMT, PLAN, MEDIA | academic fidelity UAT |
| R3 Engagement | Fair competitions, achievements and judge workflows | CONTEST, ASMT | ethics/legal/accessibility UAT |
| R4 AI | Approved study advice, summaries, monitored pilot detection | AI + consent | model evaluation/false positive gate |
| R5 Mobile | Flutter native parity for learner/teacher essential flows | MOB | app store + reliability gate |

## Exclusions from v1 promises

Automatic authoritative tajweed grading, always-on surveillance, public child leaderboards, full provider interchangeability, automatic accreditation, parental portal, school tenancy and all-language expansion.

## UX quality bar

Arabic-first RTL, English technical parity, WCAG 2.2 AA target, 360/390/768/1440 breakpoints, keyboard accessibility, clear focus, captions/transcript where appropriate, low-bandwidth audio option, clear errors, no dark patterns in billing or retention.

## Definition of done per feature

(1) requirement-ID mapped to code/test/screen; (2) server policy; (3) loading/empty/error/permission/RTL/mobile states; (4) localized accessibility; (5) analytics event; (6) audit where relevant; (7) monitoring and rollback; (8) no placeholders in production.
