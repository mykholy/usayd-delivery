# Video providers: capability negotiation and failure domain

Provider types: `embedded_sdk` (LiveKit, VideoSDK, Daily, Zoom Video SDK) vs `external_meeting` (Google Meet, Zoom Meetings). Do not assume Meeting SDK/REST features match custom Video SDK feature set.

## Backend VideoProvider contract
```ts
type Capability = 'embedded_room'|'video'|'audio'|'screen_share'|'in_app_chat'|'participant_kick'|'moderator'|'recording'|'live_transcript'|'raw_audio_ai'|'server_webhook'|'mobile_native';
type ProviderKey = 'livekit'|'videosdk'|'daily'|'zoom_video_sdk'|'zoom_meeting'|'google_meet';
interface VideoProvider {
  capabilities(context: {region: string, client: 'web'|'flutter', account: string}): Promise<Record<Capability, boolean|'unknown'>>;
  createOrReuseLessonRoom(lessonId: string, idemKey: string): Promise<RoomRef>;
  issueJoin(lessonId: string, actorId: string, role: 'learner'|'teacher'|'supervisor'): Promise<JoinResult>;
  revokeJoin(lessonId: string, actorId: string): Promise<void>;
  closeRoom(lessonId: string): Promise<void>;
  normalizeWebhook(raw: Uint8Array, headers: Record<string,string>): Promise<VerifiedVideoEvent>;
  health(): Promise<{status:'ok'|'degraded'|'down', updatedAt:string}>;
}
```
`JoinResult`: `mode=embedded|external`; `room_public_id`; for embedded: short expiry, scoped SDK grant and client configuration; for external: meeting URL + instructions + capability limitations. NEVER expose server keys or raw vendor credentials.

## Capability states and UX
- `supported` → show enabled UI and controls.
- `unsupported` → show clear explanation; preserve main lesson service.
- `unknown` → fail closed for recording, transcripts, AI analysis, participant moderation, *not* core join where safe.
- Set feature flags per provider + environment + client (web/flutter) + region. Never turn on based on global static flag.

## Transition and recovery
1. Lesson references `conference_sessions` history, and at most one `active` conference at once.
2. On pre-join provider outage: block join briefly, create alternate provider session under DB lock, notify participants, mark old session `superseded`, do not double consume lesson credits.
3. Mid-call failure: never promise seamless transfer; show reconnection UI, authorized replacement link if provided, and an incident/compensation policy.
4. Reject stale join tokens and old room URLs where vendor supports revoke; otherwise expire quickly and change external room on cancellation.
5. Provider events deduped `(provider,event_id)`, reconciled against authoritative lesson slots and client join notices; attendance stays `pending` until verified.
6. Audio AI is provider-dependent and separately gated by law/consent; Google Meet Media API sunset Jan 15, 2027 means no new dependency on that interface.
7. Teacher payout calculated from approved attendance/contract, never from raw provider webhook alone.

## Mandatory PoC matrix
Web Chrome/Firefox/Safari, Android Chrome, iOS Safari, Flutter Android/iOS, Egypt ↔ Saudi networks, audio-only fallback, camera/mic denied, intermittent 3G/4G, room churn 100 joins, concurrent rooms, raw audio availability, transcription consent indicator, join token theft, close room, webhook reorder and duplicate, per-100-class normalized total cost.

## Official verification references
- https://docs.livekit.io/frontends/reference/tokens-grants/
- https://www.videosdk.live/pricing
- https://developers.zoom.us/docs/meeting-sdk/
- https://developers.zoom.us/docs/video-sdk/
- https://developers.google.com/workspace/release-notes
