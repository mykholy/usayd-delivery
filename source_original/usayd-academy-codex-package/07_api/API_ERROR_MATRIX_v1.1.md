# Standard API error catalog and UX behavior

Use RFC7807-style `application/problem+json` with `code`, `status`, `request_id`, localized-safe `title/detail`; internal stack traces never returned.

| Error code | HTTP | Recovery UX | Retry |
|---|---:|---|---|
| VALIDATION_FAILED | 422 | Inline field errors without losing draft | after correction |
| UNAUTHENTICATED | 401 | Login preserving intent, no sensitive return URL | after login |
| FORBIDDEN / RESOURCE_NOT_FOUND | 403/404 | Safe access-denied or neutral not found | no |
| CONSENT_REQUIRED | 403 | Guardian verification or consent explanation | after permission |
| CONSENT_WITHDRAWN | 403 | Stop audio AI; show safe alternate function | no auto retry |
| SLOT_CONFLICT | 409 | Refresh slots + retain chosen filters | choose new slot |
| CREDIT_INSUFFICIENT | 409 | Payment/credit info + support | after refill |
| PAYMENT_PENDING | 202/409 | Do not assume activation; show pending and refresh status | status poll bounded |
| PAYMENT_REPLAYED | 200/409 | Neutral already-processed response | no double charge |
| PROVIDER_UNAVAILABLE | 503 | Reconnect or alternate approved provider, no lost credit | exponential backoff |
| PROVIDER_CAPABILITY_UNSUPPORTED | 422 | Explain unavailable AI/recording/chat; keep lesson | no |
| AI_UNAVAILABLE | 503 | Manual learning/teacher plan available | after recovery |
| AI_CONSENT_REQUIRED | 403 | Opt in information or manual alternative | after consent |
| EXAM_LOCKED / EXAM_TIMEOUT | 409 | Show authoritative server result and appeal path | no automatic submit |
| CONTEST_INELIGIBLE | 403 | Explain rubric/age/level/registration rules | only if eligible |
| CONTEST_SCORE_VERSION_CONFLICT | 409 | Reload latest approved score/appeal | after refresh |
| PAYRUN_ALREADY_APPROVED | 409 | Show approved immutable statement | no |
| RATE_LIMITED | 429 | Neutral cooldown, Retry-After | bounded |
| MAINTENANCE | 503 | Accessible safe service status; save drafts | bounded |

Each code must have contract tests, localized AR/EN copy and telemetry without sensitive payload.
