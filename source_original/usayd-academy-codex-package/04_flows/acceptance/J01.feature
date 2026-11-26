# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J01 @FR-GEO-001 @FR-GEO-002 @FR-GEO-004 @FR-GEO-012
Feature: Guest market selection → browse → level-assessment booking → registration → verified booking

  Scenario: Adult guest books an assessment
    Given an adult guest in a launched market
    And an available slot at 2026-12-10T17:30Z for teacher T
    When the guest holds the slot
    And signs up and confirms the booking with the hold
    Then exactly one booking is confirmed for T at 17:30Z
    And the learner sees 19:30 Africa/Cairo with the UTC time shown

  Scenario: Hold expires during sign-up
    Given a slot hold that expired 1 second ago
    When the learner confirms the booking
    Then the API answers 409 HOLD_EXPIRED
    And the slot picker reopens with the previous filters

  Scenario: Double submit
    Given a valid hold
    When the learner presses Confirm twice with the same Idempotency-Key
    Then one booking exists
    And both responses carry the same booking id
