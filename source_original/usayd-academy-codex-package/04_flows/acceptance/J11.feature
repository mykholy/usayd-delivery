# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J11 @FR-SUP-001 @FR-SUP-002 @FR-SUP-009 @FR-IAM-004
Feature: Supervisor scoped request → out-of-scope denial → reassignment/approval with separation of duties

  Scenario: Non-revealing denial
    Given a supervisor scoped to Egypt
    When they open a Saudi learner by id
    Then the API answers 404 is returned
    And the response does not confirm existence

  Scenario: No self-grant
    Given admin A
    When A creates an assignment for A
    Then the API answers 403 and an audit event
