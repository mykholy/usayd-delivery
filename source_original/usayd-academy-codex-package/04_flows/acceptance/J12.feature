# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J12 @FR-ADMIN-004 @FR-GEO-005 @FR-GEO-010 @FR-VPC-001
Feature: Admin price/config/provider change → preview/dry-run → distinct approver → activation → audit/rollback

  Scenario: Maker-checker
    Given a price book drafted by A
    When A approves it
    Then the API answers 403 SELF_APPROVAL_FORBIDDEN

  Scenario: Bound lessons unchanged
    Given lessons already bound to provider A
    When a routing policy to B activates
    Then existing lessons keep A
    And new lessons use B
