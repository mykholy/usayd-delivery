# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J10 @FR-CONTEST-002 @FR-CONTEST-003 @FR-CONTEST-008 @FR-CONTEST-009
Feature: Competition enrollment → eligibility → round → judging → provisional result → appeal (independent session) → final → reward

  Scenario: Independent appeal
    Given judge J scored submission S
    When J is assigned to review the appeal on S
    Then the assignment is refused for conflict

  Scenario: No public child ranking
    Given a minor finalist
    When the public standings load
    Then the minor is not listed
