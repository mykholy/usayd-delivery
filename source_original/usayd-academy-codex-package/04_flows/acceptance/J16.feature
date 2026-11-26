# language: en
# Specification only — no backend exists; run once the Laravel API implements the approved contracts.
@J16 @FR-GEO-002 @FR-GEO-003 @FR-GEO-010 @FR-GEO-011
Feature: Market activation and locale/country/timezone independence

  Scenario: Language switch keeps price
    Given a learner in Egypt viewing EGP prices
    When they switch to English
    Then prices, currency and times are identical
