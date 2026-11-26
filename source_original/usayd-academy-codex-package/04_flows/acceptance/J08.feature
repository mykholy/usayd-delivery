# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J08 @FR-ASMT-001 @FR-ASMT-002 @FR-PLAN-001 @FR-PLAN-002
Feature: Learning plan approval → daily learning → oral assessment → evidence-backed revision queue and memory map

  Scenario: AI never final
    Given an AI plan suggestion
    When the learner opens the plan
    Then nothing is shown until a teacher and supervisor approve

  Scenario: Evidence drives the memory map
    Given an approved revision task
    When the teacher verifies the evidence
    Then the memory segment strength updates
    And the next review date follows the plan rules
