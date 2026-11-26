# API validation report

Baseline `openapi.yaml`: **121 operations** on 109 paths (parsed with PyYAML; operationIds unique: True). It is not modified.

## `openapi.proposed.yaml`
- 57 proposed operations on 55 paths; 99 schemas.
- openapi-spec-validator: **valid** (OpenAPI 3.1)
- JSON Schema 2020-12 check of every proposed schema + request examples: **0 errors**
- operationId collisions with baseline: none · method+path collisions with baseline: none · duplicate operationIds inside proposals: none · unresolved $refs: none

## Lint of the baseline (findings, not fixed in place — the baseline is the approved draft)

| Finding | Operations | Examples |
|---|---|---|
| no x-data-classification | 67 | `getLessonReport`, `getLearnerAudioPreferences`, `getContestEligibility`, `postAttendanceDispute` … |
| collection GET without cursor/limit parameters | 51 | `get__me`, `get__programs`, `get__teachers`, `get__teachers__teacherId__availability` … |
| path parameter but no 404 response | 40 | `get__learners__learnerId`, `post__consents__consentId__withdraw`, `get__programs__programId`, `get__teachers__teacherId__availability` … |
| write without 422 VALIDATION_FAILED | 35 | `post__auth_register`, `post__auth_login`, `post__auth_refresh`, `post__learners` … |
| write without Idempotency-Key header | 23 | `post__auth_login`, `post__auth_refresh`, `post__learners`, `post__consents` … |
| secured operation without 401 | 15 | `get_bookings`, `post_bookings`, `getLearnerAudioPreferences`, `getContestEligibility` … |

These are recorded as EXISTING_NEEDS_CORRECTION rows (category `lint`) in `API_RECONCILIATION_MATRIX.csv`. Targeted corrections that block journeys are C-01…C-08.

**What this report does not prove:** that any endpoint exists or works. There is no backend; no request was sent anywhere.
