# Financial & payroll settlement architecture (implementation specification)

## Currency and accounting
- Every price/fee/credit/payout = integer minor units + ISO 4217 currency, with tax fields separately. No floating point persisted or arithmetic used for money.
- Immutable `payment_events`/`subscription_credit_ledger`/`teacher_accruals`/`payrun_adjustments`, with `source_type`, `source_id`, `idempotency_key`, `version`, author, timestamp.
- Atomic `credit_reserved` for booking; `credit_consumed` only after verified delivered lesson/approved attendance, or explicit authorized charge policy.
- Payment provider webhook: signed raw payload+timestamp validation; dedup unique `(provider, event_id)`, state transition guard, queue via outbox, prompt ACK, retries safe.

## Payroll rule interfaces
```json
{"contract_id":"ct_01","teacher_id":"t_01","currency":"EGP","effective_from":"2026-12-01","mode":"hybrid","rules":{"base_salary_minor":700000,"per_lesson_minor":2500,"min_guarantee_minor":700000,"shift_hours_per_month":160,"no_show_policy":"unpaid_if_unexcused","overtime_requires_approval":true}}
```
This example is a fictional **contract schema illustration**, not a lawful or recommended wage. Actual rules require finance/legal sign-off. Supported models: `salary`, `session_fixed`, `hourly`, `shift`, `hybrid`, `group_rate`, `bonus`, `minimum_guarantee`, `revenue_share` (only if lawful).

## Rounding conventions
- Minutes rounded only per signed rule version (e.g. billing granularity); use exact durations for audit, rounded payable minutes separately.
- Overtime, no-show, unplanned group change, leave, makeup class, overtime and emergency are separate entries, not edits to old totals.
- Payroll accrual keyed `(teacher_id, lesson_id, contract_revision_id, accrual_type)`, preventing duplicate reward from replayed lesson webhook.

## State machines
`Payment`: initiated→pending→authorized→captured→settled | failed | refunded/partially_refunded | disputed. Terminal transitions not reversible without compensating entry.
`PayRun`: draft→calculated→reviewed→approved→disbursing→paid→reconciled; reject maker=checker; dispute→adjustment next run.

## Test oracle examples
- Two simultaneous bookings for one last credit: exactly one receives reservation; balance never negative.
- Webhook delivered 5 times/out of order: exactly one capture and subscription activation.
- Teacher contract changes on 15th: existing lessons apply proper effective-dated snapshot; no retroactive rewrite.
- Teacher taught 1-to-3 group on scheduled lesson: pay governed by contract group rule not arbitrary count.
- Partial refund after delivered lesson: reverse only unused service value according to versioned policy.
- Payrun approval replay: one payment instruction, maker/checker recorded, payouts reconciled.
