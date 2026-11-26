# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J06 @FR-VIDEO-001 @FR-ATT-001 @FR-ATT-002 @FR-ATT-005
Feature: Classroom prejoin → device checks → in-app/external provider → incident/failover → attendance → teacher report

  Scenario: No silent provider switch
    Given a lesson bound to provider A
    When provider A is unhealthy 10 minutes before start
    Then an audited fallback is required
    And the binding change is visible to both participants

  Scenario: Join window
    Given a lesson starting in 30 minutes and a 10-minute window
    When the learner joins
    Then the API answers 409 with minutes remaining
