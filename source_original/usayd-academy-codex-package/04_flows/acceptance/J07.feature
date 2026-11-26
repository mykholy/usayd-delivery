# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J07 @FR-ATT-003 @FR-MOB-004 @FR-ASMT-002
Feature: Teacher report draft/autosave → offline → version conflict → final submission → academic review

  Scenario: Version conflict
    Given draft version 4 on the server
    And the teacher edits version 3 offline
    When the teacher saves
    Then the API answers 412 VERSION_CONFLICT with the server draft
    And no data is lost

  Scenario: Immutable after submit
    Given a submitted report
    When the teacher saves a draft
    Then the API answers 409 REPORT_ALREADY_SUBMITTED
