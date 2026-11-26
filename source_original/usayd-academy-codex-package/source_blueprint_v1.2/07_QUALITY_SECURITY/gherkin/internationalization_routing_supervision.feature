Feature: International prices, locale, timezone, meeting settings and supervisors
  Background:
    Given academy markets and staff are seeded with synthetic authorized fixtures

  Scenario: A returning learner's country beats a coarse IP hint
    Given a learner selected Saudi Arabia and visits from a Cairo IP address
    When the pricing page opens
    Then the Saudi market price book and SAR charge option are shown if approved
    And the UI language and timezone remain their stored independent preferences

  Scenario: A country is unavailable until PSP and compliance approval
    Given the United Arab Emirates market is in payment testing
    When a visitor selects that market and attempts checkout
    Then checkout is denied before a payment intent is created
    And waitlist and clear availability information are displayed

  Scenario: KWD monetary precision survives round trip
    Given a Kuwait sample package price is 7.500 KWD
    When the quote and payment payload are generated
    Then the minor-unit amount is 7500
    And total and charged currency agree exactly with the PSP response

  Scenario: A saved price quote does not change after locale switch
    Given a learner has a valid EGP checkout quote
    When the learner changes Arabic to English
    Then the quote ID, amount in minor units and charged currency are unchanged
    And the localized number display is correct

  Scenario: Teacher shift projects through DST
    Given a teacher recurrence is configured in America/New_York
    When occurrences are projected across a daylight-saving transition
    Then valid wall clock recurrence produces correct UTC instants
    And nonexistent local time is rejected with alternatives

  Scenario: An ambiguous local slot requires an explicit UTC offset
    Given a learner chooses 01:30 during New York autumn overlap
    When the platform shows the possible slot instants
    Then both available UTC offsets are displayed
    And no booking occurs until one is explicitly chosen

  Scenario: Two countries cannot double-book one teacher
    Given an Egyptian learner and Saudi learner request one overlapping UTC slot
    When both requests are submitted concurrently
    Then exactly one is accepted
    And the other receives a conflict without charge

  Scenario: Admin routes only new lessons to another provider
    Given LiveKit is currently bound to active lessons
    And the new approved routing rule prioritizes Daily
    When the effective time passes
    Then new unprovisioned lessons use Daily
    And active LiveKit lessons stay unchanged

  Scenario: Google Meet cannot falsely promise live raw audio AI
    Given the default route candidate is Google Meet
    When a class demands embedded raw audio transcription
    Then the capability preflight marks it unsupported
    And routing uses an approved compatible vendor or returns clear unavailable state

  Scenario: Provider activation requires independent approval
    Given a platform admin drafted a production provider change
    When the same account attempts to approve and activate it
    Then the system rejects the action
    And audit records that separation of duties was enforced

  Scenario: Unapproved transcription remains off after provider change
    Given a student withdrew session audio analysis consent
    When a provider routing policy changes
    Then session audio analysis remains disabled for that student
    And core teaching service remains available

  Scenario: Scoped supervisor cannot inspect outside country
    Given academic supervisor is assigned only to Egypt
    When they request Saudi learner assessment through the API
    Then the request is rejected without disclosing the learner record

  Scenario: AI plan requires human academic approval
    Given the AI proposed a memory review schedule
    When the recommendation is shown to the student
    Then it is labeled as suggestion until a teacher or supervisor approves
    And its evidence and version are preserved

  Scenario: Minor competitor has privacy-safe ranking
    Given a minor joins a competition with appropriate consent
    When results are published
    Then public full identity is never exposed by default
    And appeal and judging conflict checks are available

  Scenario: Arabic and English error copies cover all admin settings
    Given an admin previews a failed merchant profile
    When the locale is switched between Arabic and English
    Then the same stable error code has translated labels and actions
    And no locale switch modifies any previously published setting
