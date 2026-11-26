Feature: Unified learner account and guardian gates
  # Specification scenarios. Implement step bindings in backend/web/mobile test projects.

  Scenario: Adult learner signs up without guardian
    Given a verified adult learner with no guardian account
    When the learner completes onboarding
    Then the learner can book an eligible paid lesson without a guardian profile

  Scenario: Minor consent pending cannot join
    Given a minor learner whose required guardian approval is pending
    When the learner attempts to join a paid lesson
    Then the server returns CONSENT_REQUIRED and issues no conference token

  Scenario: Guardian approval must be verifiable
    Given an attacker who controls a learner account but not the guardian contact
    When an unverified guardian value is submitted
    Then verification remains pending and paid booking stays blocked

  Scenario: Guardian revokes AI consent
    Given a queued transcript job and a withdrawn purpose-specific consent
    When the AI worker polls the job
    Then no audio is processed and the job is cancelled with audit

  Scenario: Unrelated learner object forbidden
    Given learner A authenticated
    When learner A requests learner B academic record
    Then access is denied without disclosing B data

  Scenario: Admin needs MFA
    Given admin with correct password but incomplete MFA
    When requesting restricted policy evidence
    Then no restricted data is returned
