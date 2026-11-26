# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J14 @FR-NOTIF-001 @FR-NOTIF-002 @FR-NOTIF-004 @FR-I18N-005
Feature: Notifications, quiet hours, support incident and safeguarding escalation

  Scenario: Quiet hours
    Given quiet hours 22:00–07:00 in Asia/Riyadh
    When a review reminder is due at 23:00 local
    Then it is deferred to 07:00 local

  Scenario: Safety bypasses quiet hours
    Given a safety notice at 23:00 local
    When it is sent
    Then it is delivered immediately on the safety channel
