# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J03 @FR-TCHR-001 @FR-TCHR-002 @FR-TCHR-003 @FR-TCHR-004
Feature: Teacher application → document verification → approval → availability → learner assignment

  Scenario: Approval requires a cleared safeguarding check
    Given an application with safeguarding_check in_progress
    When a supervisor approves it
    Then the API answers 409 SAFEGUARDING_NOT_CLEARED
    And state is unchanged

  Scenario: Separation of duties
    Given supervisor S ran the recitation interview
    When S submits the decision
    Then the API answers 403 SELF_DECISION_FORBIDDEN
