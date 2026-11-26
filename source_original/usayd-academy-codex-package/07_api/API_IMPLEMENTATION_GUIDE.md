# API implementation contract guide

## Spec status

`openapi.yaml` is a **draft contract seed** to orient client/backend and Jira; endpoints and request/response shapes must be expanded by API design review before merging production controller code. Its `GenericItem` response is deliberate placeholder and must be replaced with typed DTOs as each module is implemented.

## Universal conventions

- HTTPS only; `Accept-Language`, `X-Request-Id`, IANA timezone and authenticated `actor` context.
- JSON request/response, `application/problem+json` for errors. Explicit error `code`: `CONSENT_REQUIRED`, `CREDIT_INSUFFICIENT`, `SLOT_CONFLICT`, `VENDOR_UNAVAILABLE`, `EXAM_LOCKED`, `CONTEST_INELIGIBLE`, `PAYMENT_PENDING`.
- All list responses have cursor pagination, `limit` bounds, safe sort/filter allowlists and efficient index.
- Never trust user-supplied `learner_id` for ownership; obtain authorized learner from claims/ABAC.
- 409 for stale `If-Match`/version and domain state conflicts; 422 for semantic validation when appropriate.
- Payment and attempt endpoints require `Idempotency-Key`; durable idempotency store with retention.
- Webhook controllers accept raw body and source-specific verified signature, verify timestamp, store unique event ID and return immediately before queue processing.
- Consistent RFC3339 UTC timestamps, client timezone display; amounts in **minor currency units** and currency ISO 4217 to avoid float money errors.

## Client SDK design

`AcademyApiClient` generated or typed from OpenAPI; mobile/web share endpoint semantics not UI state. Store tokens safely and rotate; never embed cloud video keys. For video external providers return `JoinDestination(mode=external,url,permissionLimitations)`; for custom SDK `mode=embedded` with short-lived grants. `clientClassroomAdapter` specific per SDK.

## API error examples

```json
{"type":"https://example.invalid/problems/consent-required","title":"Consent required","status":403,"code":"CONSENT_REQUIRED","detail":"Guardian approval required before this action.","request_id":"req_123"}
```

## API requirements test checklist

- Invalid JWT; expired join; cross-learner object ID; revoked consent; duplicate booking; concurrent credit use; stale plan/score version; forged webhook; repeated payment webhook; negative balances; overquota AI; assignment without teacher qualifications; broken timezone; partial outages.
- OpenAPI docs generated in staging, versioned, diffed in PR, with contract tests for Flutter and web SDKs.
