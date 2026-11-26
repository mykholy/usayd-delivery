# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J09 @FR-ASMT-003 @FR-ASMT-005 @FR-ASMT-006 @FR-ASMT-007
Feature: Exam start/timer → autosave → connection loss → final submit → grading/teacher review → result

  Scenario: Server deadline wins
    Given an attempt with 1 minute left
    And the device clock is 10 minutes slow
    When time passes
    Then the server auto-submits at its deadline

  Scenario: Resume after loss
    Given checkpoint 17 saved
    When the app reconnects
    Then answers up to checkpoint 17 are restored
