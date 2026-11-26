# Domain events, analytics taxonomy and financial reconciliation

## Domain event envelope

```json
{"event_id":"uuid","aggregate_type":"lesson","aggregate_id":"uuid","event_type":"LessonCompleted","version":1,"occurred_at":"2026-11-21T10:30:00Z","correlation_id":"uuid","actor_id":"uuid","payload":{"lesson_id":"uuid","attendance_verification":"vendor_reconciled"}}
```

Commit events via transactional outbox; dispatcher at-least-once; consumers idempotent by `(event_id,consumer)`; payload versioned with no raw audio or unnecessary child personal data. Failed events go to DLQ with manual replay.

## Mandatory events

- `LearnerRegistered`, `ConsentGranted`, `ConsentWithdrawn`, `AssessmentApproved`, `SubscriptionPaid`, `SubscriptionRenewed`, `PaymentRefunded`.
- `TeacherApproved`, `TeacherScheduleChanged`, `LessonBooked`, `LessonRescheduled`, `LessonStarted`, `LessonCompleted`, `LessonNoShow`, `LessonInterrupted`, `AttendanceReconciled`.
- `LessonReportApproved`, `PlanVersionApproved`, `RevisionDue`, `RevisionVerified`, `ExamSubmitted`, `ExamPublished`, `AIRecommendationApproved`.
- `CompetitionPublished`, `CompetitionJoined`, `RoundStarted`, `SubmissionReceived`, `JudgmentApproved`, `ScoreCorrected`, `AppealDecided`, `AwardIssued`.
- `TeacherAccrualRecorded`, `PayoutApproved`, `PayoutReconciled`, `PolicyFlagRaised`, `PolicyFlagResolved`, `SupportSafetyEscalated`.

## Product analytics events (privacy-safe)

| Event | Properties | Owner |
|---|---|---|
| `landing_viewed` | campaign, segment, page_id | Growth |
| `assessment_booked` | segment, locale, lead_id_hash | Growth |
| `assessment_attended` | booking_id, segment, mode | Product |
| `checkout_paid` | cohort, package, currency, recognized_amount | Finance |
| `first_lesson_completed` | cohort, provider, elapsed_bucket | Academic |
| `revision_assigned` | program, planned_minutes, level | Learning |
| `revision_verified` | rubric_version, program, delayed_recall | Academic |
| `competition_joined` | type, level, age_band, opted_public_display | Product |
| `contest_appeal_upheld` | contest_type, issue_type | Trust |
| `subscription_renewed` | cohort_month, package, country | Finance |
| `teacher_payout_reconciled` | contract_model, period, amount | Finance |
| `ai_flag_reviewed` | model_version, policy_code, false_positive, outcome | Trust |

## KPI definitions

1. **Paid renewal rate:** count cohort learners with second paid billing cycle / count eligible first-cycle learners, excluding still-not-due; report by calendar cohort and market.
2. **Fully loaded CAC:** acquisition costs (paid media + sales time + paid trials + agency/referral) / *new* paying learners attributable to period; don't count reactivated as new blindly.
3. **Contribution margin:** net collected subscription revenue less direct instruction, payment fees, video, AI, variable support and refunds, by learner/country/package; before fixed overhead.
4. **On-time lesson rate:** completed lessons started inside allowed grace / confirmed lessons due, excluding vendor outages with explicit denominator note.
5. **Verified learning improvement:** matched teacher rubric for same skill/riwaya and comparable difficulty, baseline vs later test; do not use app-opening streak as mastery.
6. **Teacher utilization:** eligible teaching minutes in actual delivered paid lessons / contracted billable teaching allocation; include cancellations separately.
7. **Contest educational lift:** compare similar eligible learners with and without participation, adjust for baseline skill and prior activity; self-selection limits causal interpretation.
8. **Safety KPI:** time to acknowledge/resolution of high-severity incidents, number/frequency without hiding low volume or suppressing reporting.

## Dashboards

Growth: visits→leads→trials→paid→renewal; Operations: teachers/slots/no-shows/provider issues; Academics: rubric levels/missed reviews; Games: submissions/appeals/retention/abuse; Finance: collections/refunds/payroll/contribution; AI: runs/errors/spend/accuracy flags; Trust: active safeguarding incidents and requests.
