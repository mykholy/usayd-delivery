# Timezone, DST and scheduling domain contract

## Time semantics
- All persisted instants use UTC ISO-8601 / MySQL microsecond datetime stored in UTC; never use ambiguous local clock time as an instant.
- Each **participant** has editable `timezone_id` as IANA string (`Africa/Cairo`, `Asia/Riyadh`, `Asia/Dubai`, `Europe/London`, `America/New_York`, etc.). No hardcoded offsets (`UTC+2`) for recurring scheduling.
- User's country only supplies a suggestion. Browser `Intl.DateTimeFormat().resolvedOptions().timeZone` suggests but user must be able to override. City picker for multi-zone countries.
- A teacher's `availability_rule` stores local recurrence + IANA timezone + recurrence boundaries + exceptions + tzdb version reference; projected lesson slots hold `starts_at_utc`,`ends_at_utc`,`teacher_timezone_at_booking`,`learner_timezone_at_booking` and snapshot of displayed local time at commitment.
- Meetings are immutable UTC events with customer-visible timezone reference. Render dates in learner timezone by default, teacher timezone on teacher view, supervisor timezone with explicit switch.
- DST transitions: if a requested wall-clock time **doesn't exist**, require user to pick valid time; if **ambiguous**, show offset/zone alternatives and store selected `fold`/instant. Never silently adjust time.
- Recurring slots are generated in teacher-local timezone first then converted to UTC for each occurrence; reevaluate future occurrences after tzdb updates and notify conflicts; keep booked UTC appointments stable unless explicitly rescheduled.
- Editing timezone preference changes the **display**, never silently changes already confirmed meeting instants.
- IANA tzdb updated with dependency/security release; if government updates offset rules, run affected bookings audit, notify and re-confirm when needed.

## API contract examples
Learner sees `2026-12-01 19:00 Asia/Riyadh`; teacher in `Africa/Cairo` receives same instant represented locally. API returns `{starts_at_utc:..., timezone_id:"Asia/Riyadh", start_local:"...", utc_offset:"+03:00", tzdb_version:"..."}`; local time is display convenience, UTC is authoritative.

## Booking invariants
- Availability endpoints return slots with UTC, localized labels and timezone abbreviation + UTC offset.
- Double-booking prevented with transaction/slot lock and unique constraints: one instructor cannot have overlapping sessions even across two countries.
- Booking cutoff and reschedule windows evaluated in UTC durations (not "calendar day" unless market legal policy requires local-day definition).
- Program availability per region: teacher shift legality and human availability checked against teacher-local time.
- Reminder rules: 24h/1h/10min relative to UTC session instant; quiet hours defined in **recipient-local zone**; urgent reminders can have explicit exception.
- ICS `DTSTART/DTEND` UTC + timezone notes; calendar invites contain stable UID, cancellation SEQUENCE bump, learner language and timezone detail.
- Live class starts_at_utc; if attendee traveling, previously booked instant remains same; participant sees updated local display.
- In the learner UI date/time always show e.g. `الثلاثاء ٧:٠٠ م (توقيت الرياض، UTC+03:00)` and a one-click timezone switch.

## Detailed state transition
`availability_proposed -> held (TTL 5m) -> payment_pending -> booked -> reschedule_requested -> rescheduled OR booked -> in_progress -> completed -> report_approved`.
- Hold expiry frees time slot and does not charge student; payment async returns to confirm via webhook.
- Webhook arrives after hold expires: reconcile payment and avoid auto-booking occupied slot; offer credit/refund workflow.
- Learner and teacher reschedule independently request changes but cannot unilaterally change a confirmed start without policy/notification.
- Payout uses attendance verified against UTC meeting interval; not local display strings.

## Special test matrix
| Test | Acceptance |
|---|---|
| Egypt daylight-saving forward/back | correct IANA conversion and no phantom duplicate class |
| London DST transition | local recurrence preserves wall time, UTC offset changes |
| US New York second 01:30 DST | two instants clearly differentiated |
| US nonexistent 02:30 spring | conflict shown, alternate valid times |
| User changes zone Cairo→Riyadh | confirmed lesson UTC unchanged |
| Teacher has student Egypt and KSA | one actual session blocks both schedules |
| User traveling with same account | browser hint not forced over profile |
| Reminder after timezone edit | sent once based on UTC; local quiet hours respected |
| Mass tzdb update | affected slot preview and notification approval |
| iOS/Flutter vs web | same UTC values and correct localized labels |

## Sources
https://www.iana.org/time-zones ; https://data.iana.org/time-zones/tzdb-2026e/tz-link.html
