# Video Provider Control Center — admin UX, technical RFC and operational runbook

## Intent
Admin can select and swap the default provider for **new classes and future unprovisioned lessons** without deployment. This is **not** a magic transparent mid-call migration. Existing room credentials, SDK components, transcript support and capacity remain provider-specific. Classes already provisioned retain their `provider_binding_id` until explicit migration policy and consent obligations permit change.

## Supported adapters and classes
| Provider key | Integration class | In-app classroom | Raw audio AI expectation | Room control | Important notes |
|---|---|---|---|---|---|
| `livekit` | embedded native SDK | yes after PoC | candidate capability | server-side | room tokens, web/iOS/Flutter verify |
| `videosdk` | embedded native SDK | yes after PoC | verify per product | vendor API | separate recording/transcription pricing |
| `daily` | embedded native SDK | yes after PoC | verify pipeline | vendor API | room token limitations to test |
| `zoom_video_sdk` | embedded custom SDK | yes after PoC | verify product-specific | server SDK | NOT same as normal Zoom Meeting |
| `zoom_meeting` | external/Meeting SDK | partial | unknown/limited | meeting API | meeting account/license restrictions |
| `google_meet` | external meeting | no guaranteed fully embedded white-label | unavailable via planned Media API sunset | Meet REST API | not assume audio injection or token-specific participant removal |

No static `true` capabilities shipped merely because docs mention possible features: run per-account/region/client PoC and update `verified` state with test timestamp.

## Provider configuration domain
`video_providers`: key, class, lifecycle status, created_at.
`video_provider_accounts`: provider, environment, account alias, api_endpoint, secret_ref (vault only), allowed_regions, concurrency_limit, quota, pricing reference, webhook status.
`video_capabilities`: account_id, capability, `verified|unsupported|unknown`, client/platform, region, evidence, checked_at, expires_at.
`video_routing_policies`: version, scope (market/program/cohort/lesson type), provider_priority[], required_capabilities[], effective_start, status, approved_by.
`video_provider_bindings`: lesson_id, provider, account_id, policy_version, external_room_reference, lifecycle, initiated_at, replaced_by, immutable history.
`video_events`: provider+external_event_id unique, verified signature, idempotent processing status.
`provider_health_checks`: region, latency, auth connectivity, quota, timestamp and redacted failure reason.
`video_secrets`: vault references only, never token contents in DB/client/UI.

## Admin page design
`/admin/settings/video-providers` — title, primary provider badge, active policy, last successful live test, top-level rollout banner. Cards per provider with icon, label, environment, health (`verified healthy / degraded / outage / unknown`), supported markets, current active rooms, today's cost estimate, credentials rotation due. No fabricated uptime.

**Provider detail tabs:**
1. Overview: capabilities matrix per web/Flutter and market, verified evidence, compatibility caution.
2. Credentials: vault secret reference masked, rotate via secure input, never reveal stored secret; test connection.
3. Session config: room TTL, lobby, waiting-room policy, moderator mapping, recording and audio-processing flags gated by per-session consent.
4. Routing: default provider, country/program overrides, fallback sequence, dry-run allocation by sample lesson.
5. Monitoring: rate-limited webhook logs, errors, active assignments, quotas, cost per participant minute.
6. History: who/when/why, effective date, preview/diff, rollback and approval history.

**Switch Provider wizard** `Select -> Check compatibility -> Dry-run -> Impact preview -> Approve -> Schedule/activate -> Audit`:
- P1 choose provider/account/affected countries and programs.
- P2 compare capability gaps (raw audio, chat, screen share, recording, mobile), indicate all impacted UX.
- P3 verify credentials, minimum quota, data protection/transfer, legal approval, mobile SDK capability, 2-person approval when active market.
- P4 test sandbox meeting and teacher/learner join; price and quotas preview.
- P5 effective future time with target only `unprovisioned` lessons by default. Confirm in a modal with human-readable rollout summary.
- P6 rollback old routing version for **future** lessons; cannot claim ongoing classes magically moved.

## Secure decision and routing pseudocode
```
routeLesson(lesson, region, clientRequirements):
  assert lesson not already bound OR explicit authorized migration request
  policy = fetchCurrentApprovedRoutingPolicy(region, program, effectiveAt)
  for account in policy.ordered_accounts:
    if account.active && healthyRecentEnough(account) && capacityAvailable(account)
       && verifiedCapabilities(account, clientRequirements) && legalRegionsAllow(account, region):
         return bindUnderLessonLock(lesson, account, policy.version)
  return CLASSROOM_UNAVAILABLE_WITH_RECOVERY_OPTIONS
```
`issueJoin` **always** authorizes enrolled learner/assigned teacher/approved supervisor, checks consent and meeting status, and obtains short-lived vendor grant or externally hosted meeting access per actual provider. Never expose vendor signing keys. Roles scoped to room.

## Provider failover policies
- Before session: if provider outage or credentials invalid, only unprovisioned lessons can route to fallback automatically under lock; provisioned lesson uses an explicit migration job with room close/invalidations where supported, notifications, audit and provider-specific revocation limitations.
- During session: show reconnection/status and support-assisted "change meeting" workflow; human-led recovery, attendance reconciled, no double debits, no false claim of seamless media migration.
- A provider **switch does not authorize** recording or AI access automatically. Missing consent/capability disables feature and produces specific UI state.
- Webhooks can arrive out of order or be duplicated; normalize by account and event, reconcile canonical attendance.

## Exact admin permissions
- `video.providers.view`: Ops supervisor, security, platform-admin.
- `video.providers.configure_draft`: platform-admin, authorized tech-ops.
- `video.providers.test_connection`: tech-ops in sandbox; prod test separately approved.
- `video.providers.activate`: platform-admin proposer + security/ops second approver.
- `video.providers.credentials.rotate`: security custodian only, dual control.
- `video.provider_policy.rollback`: two approvers and audit; affects future allocations only.
- `video.lesson.override`: designated operations supervisor, reason, audit, learner notification.
- `video.recording.enable`: explicit guardian/student appropriate consent plus authorized safeguarding/academic policy; no admin force bypass.

## Testable acceptance criteria
- Changing default LiveKit→Daily from admin changes **new** lesson allocations with no code redeploy; existing active classes remain LiveKit.
- Changing to Google Meet clearly disables in-app media and unsupported AI/room moderation; UI offers external link mode.
- Activate without verified credentials, capability, legal account, MFA or second approver is blocked.
- Disabling one provider does not delete its existing event history or recording retention obligations.
- Routing changes use optimistic version/concurrency conflicts (409); audit and rollback surfaces show correct effective_at.
- Provider failure sends one notification per affected lesson and never double-charges, double-attends or auto-marks a lesson completed.
- Web/iOS/Android SDK join tested before marking provider 'verified for client'.

## Verification links
- https://docs.livekit.io/reference/other/roomservice-api/
- https://developers.zoom.us/docs/meeting-sdk/web/
- https://developers.google.com/workspace/meet/api/guides/overview
- https://developers.google.com/workspace/release-notes (Media API ending Jan 15 2027)
- https://docs.videosdk.live/docs/realtime-communication/intro
