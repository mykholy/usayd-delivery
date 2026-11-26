# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J05 @FR-PAY-001 @FR-PAY-002 @FR-PAY-003 @FR-PAY-004
Feature: Subscription quote → checkout → webhook → entitlement → renew/expire/refund (quote expiry, idempotency)

  Scenario: Entitlement only after verified webhook
    Given a checkout in pending state
    When the browser returns from the PSP with success
    Then the subscription is still PENDING_PAYMENT
    And after a valid signed webhook it becomes ACTIVE exactly once

  Scenario: Duplicate webhook
    Given a processed provider event id
    When the same webhook is delivered again
    Then the API answers 200 is returned
    And no second entitlement is created

  Scenario: Quote expiry
    Given a quote that expired
    When checkout is attempted
    Then the API answers 409 QUOTE_EXPIRED
    And a fresh quote is offered
