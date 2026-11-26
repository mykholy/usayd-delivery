# Consumer/provider request examples — synthetic

All IDs/emails/phone placeholders; use no real contact or payment data. API base `https://api.example.invalid/api/v1` (replace with environment actual origin).

## Unified registration adult
```http
POST /api/v1/auth/register
Content-Type: application/json

{"name":"Test Learner","contact":"learner@example.invalid","password":"sample-pass123!","age_band":"adult","country_code":"EG","timezone":"Africa/Cairo"}
```
Expected: 201 typed user/verification status; never reveal staff role. Actual schema fields follow authoritative `openapi.yaml` after design sign-off.

## Minor consent
```http
POST /api/v1/consents
Authorization: Bearer <redacted>
Content-Type: application/json

{"purpose":"guardian_approval","subject_learner_id":"00000000-0000-0000-0000-000000000001","consent_document_version":"2026-11-draft","granted":true,"guardian_verification_token":"<verified-guardian-proof>"}
```
Expected: pending verification receipt, not an approved boolean from an unverified contact. Use verified server flow.

## Lesson booking / race
```http
POST /api/v1/bookings
Authorization: Bearer <redacted>
Idempotency-Key: booking-test-001
Content-Type: application/json

{"learner_id":"00000000-0000-0000-0000-000000000001","teacher_id":"00000000-0000-0000-0000-000000000002","program_id":"00000000-0000-0000-0000-000000000003","start_at":"2026-12-06T15:00:00Z","timezone":"Africa/Cairo"}
```
Expected: one confirmed or reserved booking, insufficient credit or 409 if raced, immutable credit reserve record.

## Video join example (typed)
```json
{"data":{"provider":"livekit","mode":"embedded","expires_at":"2026-12-06T15:05:00Z","capabilities":{"raw_audio_ai":false,"recording":false,"screen_share":true},"embed_token":"<short-lived-token>"}}
```
Do not log embedded token or external meeting URL. External providers return `mode:external`, `external_url` and capability limits; do not claim in-app features where missing.

## AI suggestion
```json
{"data":{"id":"00000000-0000-0000-0000-000000000101","kind":"learning_plan","state":"pending_teacher_review","evidence_refs":["assessment:sample-1"],"recommendation":{"revision_minutes":15},"model_version":"prototype-v1"}}
```
Never show as approved plan until educator signs.
