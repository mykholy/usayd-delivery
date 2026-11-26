# API ↔ state-machine alignment

Cross-check of `07_api/openapi.yaml` schemas against `STATE_MACHINES.md` (domain authority). All corrections are **PROPOSED** and need tech-lead approval; the baseline YAML is unchanged.

| ID | Schema.field | API enum today | State machine | Proposed correction |
|---|---|---|---|---|
| C-09 | `Subscription.status` | pending, active, paused, expired, cancelled | PENDING_PAYMENT, ACTIVE, RENEWAL_DUE, SUSPENDED, REFUND_PENDING, PARTIALLY_REFUNDED, REFUNDED, EXPIRED, CANCELLED | API lacks renewal_due/suspended/refund states and has `paused`, which the state machine does not define |
| C-10 | `Lesson.attendance_state` | pending, verified, disputed | DRAFT, CONFIRMED, READY, IN_PROGRESS, INTERRUPTED, RESCHEDULE_PENDING, COMPLETED, CANCELLED, DISPUTED, RESOLVED | Lesson has no lifecycle `state` field at all; add it (attendance_state stays separate) |
| C-11 | `Competition.(none)` | — | draft … academic_review … legal_review … registration_open … running … scoring … provisional_results … appeal_window … finalized … prizes_issued … archived | Competition has no state field; add the 13-state lifecycle + cancelled |
| C-12 | `ConsentReceipt.state` | pending, approved, revoked, expired | not_requested, requested, verified/granted, withdrawn, expired | Names differ (approved↔granted, revoked↔withdrawn); a guardian `declined` outcome exists in neither — add it |
| C-13 | `Assessment.status` | draft, submitted, reviewing, approved, rejected | DRAFT, SUBMITTED, HUMAN_REVIEW, APPROVED, REJECTED, PUBLISHED, APPEALED, CORRECTED | API stops at approved/rejected; published/appealed/corrected missing (FR-ASMT-007) |
| C-14 | `LearningPlan.state` | draft, pending_teacher_review, approved, archived | draft, proposed, teacher_review, approved, active, superseded, archived | AI drafts must start at `proposed`; API has no proposed/active/superseded |
| C-15 | `PayRun.state` | draft, calculated, reviewed, approved, paid, reconciled | accrued, calculated, reviewed, approved, payout_requested, paid, reconciled (+ disputed) | payout_requested and disputed missing |
| C-16 | `CompetitionSubmission.status` | draft, submitted, under_review, judged | submitted, evaluating, reviewed, final (FR-CONTEST-008) | Names differ from FR-CONTEST-008; no second-review state |

Also: `Booking.status` starts at `reserved` while the Lesson machine starts at `DRAFT → CONFIRMED (slot lock)`. Keep both (booking ≠ lesson) and document the mapping reserved→DRAFT, confirmed→CONFIRMED.
Money and time representations are consistent with the invariants (`amount_minor` integer + ISO currency; UTC instants + IANA zone) in every proposed schema.
