# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J13 @FR-MOB-002 @FR-MOB-004 @FR-IAM-008
Feature: Mobile offline draft → encrypted queue → re-auth → reconnect/batch sync → idempotency and conflict resolution

  Scenario: Duplicate item
    Given item c1 already applied
    When the batch contains c1 again
    Then outcome duplicate
    And no second record

  Scenario: Ownership changed offline
    Given the learner was reassigned while offline
    When a report draft syncs
    Then outcome rejected with reason
