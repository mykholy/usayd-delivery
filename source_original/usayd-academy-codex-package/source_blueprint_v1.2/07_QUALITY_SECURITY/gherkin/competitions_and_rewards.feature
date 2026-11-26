Feature: Contest integrity, appeals, privacy
  # Specification scenarios. Implement step bindings in backend/web/mobile test projects.

  Scenario: Duplicate registration
    Given learner registered in a competition
    When a second register request is retried
    Then only one canonical registration exists

  Scenario: Wrong level excluded
    Given beginner learner and advanced-only round
    When registering
    Then a transparent ineligibility reason is shown

  Scenario: Minors private results
    Given a minor in a contest
    When an unauthenticated visitor views standings
    Then minor identity and score cannot be inferred

  Scenario: Rubric locked after opening
    Given competition registration has started
    When admin changes scoring weights without review
    Then update is blocked pending versioned notice and approval

  Scenario: Judge own student conflict
    Given a judge evaluating a private student in prize final
    When submitting a sole judgment
    Then independent qualified review is required

  Scenario: Appeal generates new score version
    Given provisional score and timely approved appeal
    When independent reviewer corrects score
    Then original score remains auditable and new version is effective

  Scenario: Awards issued once
    Given finalized competition result
    When award issue job is retried
    Then exactly one active award record exists

  Scenario: No pay-to-win entry
    Given a free contest with locked attempt limits
    When a learner purchases a lesson package
    Then contest ranking chance count does not increase
