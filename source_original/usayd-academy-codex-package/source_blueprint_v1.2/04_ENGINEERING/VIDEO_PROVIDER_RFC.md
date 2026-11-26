# RFC: Swappable Video Conference Provider
**Status:** design decision for POC | **Scope:** Meet, Zoom Meeting, Zoom Video SDK, VideoSDK, LiveKit, Daily

## Critical distinction

Google Meet and Zoom Meetings are meeting products with APIs/SDKs with restricted media control; LiveKit, VideoSDK, Daily and Zoom Video SDK are building blocks for custom in-platform classrooms. **No promise of feature parity.** Google Meet Media API is being shut down 2027-01-15 per official Google release notes; do not build live-audio AI dependence on it.

## Capability matrix (planning hypotheses; verify in sandbox and contract terms)

| Capability | LiveKit | VideoSDK | Daily | Zoom Video SDK | Zoom Meetings | Google Meet |
|---|---|---|---|---|---|---|
| Own branded classroom | Yes | Yes | Yes | Yes | Partial/SDK and licensing | No general equivalent to custom raw SDK |
| Browser native integration | Yes | Yes | Yes | Yes | Meeting SDK/browser | External/Embed availability not relied upon |
| Mobile native SDK | Yes | Yes | Yes | Yes | Yes | Meet app links |
| Direct raw audio for custom AI | Verify scope; feasible with tracks/agents | Verify access | Feasible with integration | Platform-supported with constraints | Restricted permissions/platform | Do not depend on discontinued Media API |
| Attendance events | Webhooks | APIs/webhooks | Webhooks | SDK/webhooks | Reports/webhooks | Conference records/events |
| Platform-controlled chat | Yes app-defined | Yes app-defined | Yes app-defined | Yes app-defined | Meeting chat restrictions | Meet moderation permissions only |
| Moderation/room close | Yes | Yes | Yes | Yes | Host-dependent | Host/REST-dependent |
| Teacher screen/PDF sync | Custom app | Custom app | Custom app | Custom app | Side companion UI | Side companion UI |
| Provider switching mid-call | Not guaranteed | Not guaranteed | Not guaranteed | Not guaranteed | Not guaranteed | Not guaranteed |

## Provider contracts (language-agnostic shape)

```
interface VideoProvider {
  capabilities(accountContext, region): CapabilitySet;
  reserveConference(lesson, policy): ConferenceGrant;
  joinGrant(conference, actor, role): JoinDestination; // embed-token or external URL
  endConference(conference, actor): Result;
  parseWebhook(rawBody, headers): VerifiedEvent;
  getAttendance(conference): AttendanceSnapshot | Unsupported;
  startRecording(conference, consentRef): MediaJob | Unsupported;
  deleteMedia(mediaRef): Result | Unsupported;
}

interface ClassroomClientAdapter {
  mount(destination, viewerContext): void;
  muteAudio(): Result | Unsupported;
  toggleVideo(): Result | Unsupported;
  shareAppData(topic, payload): Result | Unsupported;
  reconnect(): Result;
  unmount(): void;
}
```

`CapabilitySet` fields: `embed`, `recording`, `rawAudio`, `transcript`, `attendanceWebhook`, `moderation`, `screenShare`, `chatDisable`, `simultaneousRooms`, `mobileSDK`, `hostAccountRequired`, `externalJoin`, `serverSideExit`, `egress`, `region`, `planId`. Each feature has `supported`, `conditional`, `unsupported`, `not_verified` statuses, not boolean guessed `true`.

## Selection and fallback policy

- `ProviderPolicy` priority per region, package, feature request and budget. For AI transcript-required sessions, select only providers where consent and technical capabilities are available; otherwise turn AI feature off and keep teaching.
- Provider assigned to `conference_session` at creation and stored; switching after room has participants requires a new conference and participant notice, not silent hot swap.
- Google Meet/Zoom Meetings external flow: deep link to meeting; run Quran workspace in platform in parallel; record attendance through available conference events, show degraded features plainly.
- Default recording disabled; consent required separately, provider feature must be enabled explicitly with visible indicator.

## POC test matrix / decision evidence

1. Egypt teacher + Saudi learner: Android Chrome, iPhone Safari, desktop, 4G & low bandwidth, camera/mic permissions and background/foreground.
2. Join with wrong lesson ID, expired token, swapped learner, teacher without assignment, concurrent sessions.
3. 2-person 30min and small-group load, join/rejoin, packet loss, devices poor CPU.
4. Disconnect/reschedule, teacher no-show, dual webhook delivery, calendar DST.
5. Live audio analysis consent on/off and per-speaker isolation. Verify explicit SDK feature grants/licensing.
6. Accessibility controls, keyboard, low data and audio-only.
7. Record total bill: participant minutes, egress, transcript, recording, network, storage, tax.
8. Contract review: DPA, geographic location, withdrawal, retention, data processing rights.

## Gate

POC owner writes a signed comparison: pass/fail + p50/p95 metrics + cost scenario + missing capability list + UX screenshots. No irreversible SDK choice before evidence.
