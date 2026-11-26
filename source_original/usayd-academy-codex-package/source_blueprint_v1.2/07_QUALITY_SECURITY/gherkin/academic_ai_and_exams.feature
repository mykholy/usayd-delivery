Feature: Learning and exam correctness
  # Specification scenarios. Implement step bindings in backend/web/mobile test projects.

  Scenario: Only approved Quran references rendered
    Given a corpus asset with wrong or unverified hash
    When content editor attempts publishing
    Then publication is blocked and academic alert is created

  Scenario: AI plan cannot auto publish
    Given approved human assessment and an AI suggested revision plan
    When the model returns valid JSON
    Then plan is pending teacher approval and student sees no official change

  Scenario: Teacher approves edited plan
    Given pending AI plan with evidence refs
    When qualified teacher edits and signs revision
    Then a new immutable approved plan version is activated

  Scenario: Revision self practice not verified mastery
    Given learner completes a solo practice task
    When the memory map updates
    Then progress is marked self practiced not teacher verified mastery

  Scenario: Sensitive AI prompt injection
    Given speech contains instructions to override app policies
    When analysis pipeline processes the transcript
    Then transcript is handled as untrusted data with no admin action

  Scenario: AI service unavailable
    Given AI service down during a live class
    When teacher submits manual lesson report
    Then class and reporting still work without AI

  Scenario: Exam double submit
    Given active exam attempt with same idempotency key
    When two submit requests race
    Then one canonical submission and score version result

  Scenario: Exam timeout with offline draft
    Given local draft and server time expired
    When mobile reconnects
    Then server deadline applies and draft is preserved as audit not secretly graded

  Scenario: Oral assessment needs human decision
    Given AI suspects a tajweed mistake
    When oral exam is marked
    Then result stays provisional until teacher or judge approves
