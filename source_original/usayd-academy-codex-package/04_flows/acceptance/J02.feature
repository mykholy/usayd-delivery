# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J02 @FR-IAM-002 @FR-IAM-006 @FR-IAM-007 @FR-PROF-005
Feature: Minor sign-up → separate guardian session → purpose-level consent, decline, expiry, withdrawal, limited mode

  Scenario: Guardian grants lessons only
    Given a minor in limited mode
    And a guardian invitation for lessons and recording
    When the guardian grants lessons and declines recording
    Then two consent receipts exist with the policy version
    And booking is allowed
    And recording stays disabled with a reason

  Scenario: Learner cannot decide for the guardian
    Given a minor’s access token
    When it calls decideGuardianConsent
    Then the API answers 403
    And no receipt is written

  Scenario: Invitation expiry
    Given an invitation that expired
    When the guardian opens it
    Then the API answers 410 INVITATION_EXPIRED is shown in AR/EN
    And the minor can resend

  Scenario: Withdrawal stops a purpose
    Given granted AI processing
    When the guardian withdraws AI processing
    Then the next AI analysis request is refused
    And a withdrawal receipt is appended
