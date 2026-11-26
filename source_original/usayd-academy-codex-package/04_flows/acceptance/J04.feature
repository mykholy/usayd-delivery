# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J04 @FR-BOOK-001 @FR-BOOK-003 @FR-BOOK-004 @FR-BOOK-006
Feature: Booking, cancellation and reschedule across time zones (DST gap/overlap, double booking, hold expiry, offline retry)

  Scenario: DST gap is rejected, not shifted
    Given a learner in a zone where 02:30 local does not exist on 2027-03-28
    When they hold 02:30 local
    Then the API answers 422 DST_GAP
    And no hold exists

  Scenario: DST overlap needs a choice
    Given 01:30 local occurs twice
    When they hold without dst_resolution
    Then the API answers 422 DST_AMBIGUOUS_NEEDS_RESOLUTION
    And both offsets are offered

  Scenario: Concurrent holds
    Given two learners request the same slot at the same time
    When both call createSlotHold
    Then exactly one 201 and one 409 SLOT_TAKEN
