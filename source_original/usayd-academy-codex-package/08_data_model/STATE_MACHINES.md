# Domain state machines & invariants

## Lesson

```mermaid
stateDiagram-v2
  [*] --> DRAFT
  DRAFT --> CONFIRMED: entitlement reserved / slot lock
  CONFIRMED --> READY: provider provisioned
  READY --> IN_PROGRESS: authorized join
  IN_PROGRESS --> COMPLETED: duration + report/attendance checks
  IN_PROGRESS --> INTERRUPTED: disconnect/provider outage
  INTERRUPTED --> RESCHEDULE_PENDING: approval
  CONFIRMED --> CANCELLED: allowed cancellation
  RESCHEDULE_PENDING --> CONFIRMED: new slot/provider
  COMPLETED --> DISPUTED: support appeal
  DISPUTED --> RESOLVED: decision+ledger adjustments
```

## Subscription

```mermaid
stateDiagram-v2
  [*] --> PENDING_PAYMENT
  PENDING_PAYMENT --> ACTIVE: signed payment confirmation
  PENDING_PAYMENT --> EXPIRED: timeout
  ACTIVE --> RENEWAL_DUE: billing end
  RENEWAL_DUE --> ACTIVE: paid renewal
  RENEWAL_DUE --> SUSPENDED: grace expires
  ACTIVE --> REFUND_PENDING: approved request
  REFUND_PENDING --> PARTIALLY_REFUNDED: ledger compensation
  REFUND_PENDING --> REFUNDED: ledger compensation
  ACTIVE --> CANCELLED: allowed end
```

## Assessment / plan / AI suggestion

```mermaid
stateDiagram-v2
 [*] --> DRAFT
 DRAFT --> SUBMITTED
 SUBMITTED --> HUMAN_REVIEW
 HUMAN_REVIEW --> APPROVED
 HUMAN_REVIEW --> REJECTED
 APPROVED --> PUBLISHED
 PUBLISHED --> APPEALED
 APPEALED --> CORRECTED
```

Plan version: `draft → proposed → teacher_review → approved → active → superseded/archived`; any AI-generated update starts at `proposed`. Finalized student grade never overwritten without revision history.

## Teacher compensation

`accrued → calculated → reviewed → approved → payout_requested → paid → reconciled`; `disputed` branches before/after payout with compensating adjustment. Never modify a paid payout transaction.

## Consent

`not_requested → requested → verified/granted → withdrawn/expired`; audience and purpose specific. Regrant creates new consent receipt with version/time, not overwriting previous record.

## Contest

`draft → academic_review → legal_review → scheduled → registration_open → registration_closed → running → scoring → provisional_results → appeal_window → finalized → prizes_issued → archived`. Cancel/void reason and public notice. No scored final without judge approval.

## Transaction consistency invariants

- All critical transitions check actor permission, effective state, idempotency key and ownership.
- Side effects follow transactional outbox; retries don't produce double records.
- External vendor callback cannot override an academic grade, payout or contest result.
