Feature: Teacher settlement, operations, safety
  # Specification scenarios. Implement step bindings in backend/web/mobile test projects.

  Scenario: Contract effective date
    Given teacher pay rules change mid-month
    When payroll calculates completed lessons
    Then each accrual uses contract revision effective on delivery date

  Scenario: Same lesson paid once
    Given provider webhook replay and teacher lesson approval
    When accrual job retries
    Then teacher gets only one eligible base accrual

  Scenario: Payrun maker checker
    Given finance operator created payrun
    When same operator tries final approval
    Then approval is rejected and audited

  Scenario: Support privilege boundary
    Given support role without safeguarding privilege
    When reading sensitive session audio evidence
    Then access is denied and attempt logged without audio text

  Scenario: Student safe competition message
    Given minor student participating in a challenge
    When another student attempts direct contact
    Then unsupported private messaging is blocked

  Scenario: Restricted media signed URL expiry
    Given private lesson recording link expired
    When a visitor attempts playback
    Then access is denied and no public object URL is exposed

  Scenario: Restore drill
    Given encrypted database backup and restricted media
    When restore performed to isolated test environment
    Then key tables reconcile and no production notifications fire

  Scenario: No fake educational certifications
    Given an internal achievement certificate
    When user opens public verification
    Then certificate correctly identifies academy-issued status and limits
