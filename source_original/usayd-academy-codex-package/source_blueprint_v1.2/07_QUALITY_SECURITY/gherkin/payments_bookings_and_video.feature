Feature: Payment, booking and conferencing integrity
  # Specification scenarios. Implement step bindings in backend/web/mobile test projects.

  Scenario: Concurrent last credit booking
    Given a learner with exactly one available lesson credit
    When two independent bookings reserve that credit concurrently
    Then exactly one reserves the credit and the balance never becomes negative

  Scenario: Concurrent teacher slot booking
    Given a teacher with one available slot
    When two eligible learners book it concurrently
    Then exactly one booking succeeds and the other receives SLOT_CONFLICT

  Scenario: Payment webhook replay
    Given one verified successful checkout event
    When the provider retries the exact webhook five times
    Then one payment and one credit grant exist

  Scenario: Forged webhook denied
    Given an unsigned or invalid-signature webhook
    When it reaches the payments endpoint
    Then the event does not change any payment or credit state

  Scenario: Checkout pending
    Given a new checkout awaiting provider confirmation
    When client returns from hosted payment
    Then the subscription is not active until a verified capture event

  Scenario: Teacher no show
    Given an active paid booking with absent teacher
    When attendance reconciliation completes
    Then credit is not consumed and a makeup/refund path opens

  Scenario: Provider outage before start
    Given active booking and primary vendor down
    When authorized learners request join
    Then system offers approved alternate provider without duplicate debit

  Scenario: Google Meet feature limitations
    Given a Google Meet external session without raw audio access
    When student opens classroom controls
    Then AI transcription controls are disabled with a capability explanation

  Scenario: Revoked stale join
    Given a cancelled lesson whose previous embedded token expired
    When actor reuses prior token
    Then room entry is denied where vendor supports revoke or grant expiration

  Scenario: Timezone daylight saving
    Given a teacher and learner in different IANA timezones on DST change
    When booking an available slot
    Then stored UTC instant and displayed local times remain consistent
