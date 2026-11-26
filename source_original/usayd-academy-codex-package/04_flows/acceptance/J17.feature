# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J17 @FR-MOB-005 @FR-ENG-004 @FR-CONTEST-013 @FR-IAM-007
Feature: Kids / Professional / Simple mode switching (presentation only; permissions unchanged)

  Scenario: Mode does not change permissions
    Given a 15-year-old learner without competition consent in Professional mode
    When they switch to Kids mode
    Then competitions remain unavailable
    And no API scope changes
