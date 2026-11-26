# USYD-T0702: Release Coordination Across API, Web, and Flutter
**Jira Key:** [USYD-64](https://mykholy.atlassian.net/browse/USYD-64)  
**Task ID:** `USYD-T0702`  
**Candidate Sprint:** `S00`  
**Authoritative Repositories:**  
- `usayd-api` (`https://github.com/mykholy/usayd-api`)
- `usayd-web` (`https://github.com/mykholy/usayd-web`)
- `usayd-flutter` (`https://github.com/mykholy/usayd-flutter`)

---

## 1. Executive Summary & Objective

Usayd Academy operates across three independent Git repositories representing a decoupled system architecture:
1. **`usayd-api`**: Laravel current stable + MySQL 8.4 LTS backend modular monolith providing RFC 7807/9457 API endpoints.
2. **`usayd-web`**: Next.js 15+ (App Router, React 19, TypeScript) responsive web application for learners, teachers, and administrators.
3. **`usayd-flutter`**: Flutter 3.29+ mobile application providing age-adaptive interfaces (Kids, Pro, Simple) on iOS and Android.

The objective of this specification is to govern cross-repository compatibility windows, contract ownership, breaking change isolation, rollout sequencing, database migration safety, canary deployments, mobile app store update lag, and emergency rollback protocols.

---

## 2. API Contract Governance & Compatibility Windows

### 2.1 Contract Authority and Single Source of Truth
- The planning specification is `source_original/usayd-academy-codex-package/07_api/openapi.yaml`; proposed operations are separate. The implemented consumer contract is [usayd-api/docs/api/implemented.openapi.json](https://github.com/mykholy/usayd-api/blob/main/docs/api/implemented.openapi.json), versioned and published with SHA256 under [producer policy](https://github.com/mykholy/usayd-api/blob/main/docs/api/CONTRACT_PUBLICATION.md).
- `usayd-api` is the **producer** of API contracts.
- `usayd-web` and `usayd-flutter` are **consumers** of API contracts.
- **Contract Freezing Rule:** No breaking change may be introduced to an existing endpoint without a formal API deprecation notice and a concurrent versioning strategy (`/api/v1` to `/api/v2`).

### 2.2 Compatibility Window Rules (The N-2 Rule)
- Web browsers load updated client code upon reload; mobile apps on Google Play and Apple App Store lag behind by days, weeks, or months due to review cycles and un-updated client devices.
- **Backend Invariant:** `usayd-api` must support at minimum:
  - The current production Flutter release ($N$).
  - The previous release ($N-1$).
  - The oldest supported release ($N-2$, defined by `min_supported_version`).
- **Graceful Degradation:** When optional fields or new response nodes are added, client parsers must use lenient deserialization (ignoring unknown keys) to avoid parsing crashes.

### 2.3 Mobile App Store Version Constraints
- Every mobile client request transmits:
  - `X-App-Version`: SemVer string (e.g., `1.0.0`).
  - `X-App-Build`: Numeric build number (e.g., `100`).
  - `X-Platform`: `ios` or `android`.
  - `X-Trace-ID`: Client trace UUID.
- Future approved contract: the backend will check `min_supported_version` via configuration/feature flags. This is a planned acceptance requirement, not evidence of a currently implemented cutoff. Store links must be verified before publication:
  - If `X-App-Version < min_supported_version`: Returns RFC 7807 `426 Upgrade Required` with:
    ```json
    {
      "type": "https://errors.usayd.com/UPGRADE_REQUIRED",
      "title": "تحديث التطبيق مطلوب",
      "status": 426,
      "code": "UPGRADE_REQUIRED",
      "detail": "يرجى تحديث تطبيق أُسَيْد للاستمرار في الاستخدام.",
      "traceId": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
      "invalidParams": {}
    }
    ```

---

## 3. Database Migration & Schema Compatibility (Expand-Contract Pattern)

All schema changes in `usayd-api` must be strictly backward-compatible with running versions of the application:
1. **Phase 1 (Expand):**
   - Add new nullable columns or tables.
   - Rehearse and measure migration impact; zero downtime is not assumed.
   - Deploy backend code that writes to both old and new columns, reading from old if new is null.
2. **Phase 2 (Backfill):**
   - Run idempotent queued jobs to backfill historical data from old columns to new columns.
3. **Phase 3 (Switch Read):**
   - Update application code to read exclusively from new columns.
4. **Phase 4 (Contract):**
   - After all consumers and mobile clients have transitioned beyond the compatibility window, deploy a cleanup migration to drop old columns or tables.
- **Rollback Guarantee:** Test reversible migrations on isolated data. Never assume down() restores deleted data. Prefer application rollback against compatible expanded schema; destructive migration or restore needs explicit approval and proven backup/restore.

---

## 4. Release Sequencing & Promotion Pipeline

```
[Delivery / Specs]
       │
       ▼
[usayd-api: Main] ──(Passes CI + Approval)──► Staging API ──► Production API
       │                                            │                  │
       ├──► OpenAPI Contract Published              │                  │
       │                                            ▼                  ▼
[usayd-web: Main] ──(Passes CI + Approval)──► Staging Web ──► Production Web
       │                                            │                  │
       ▼                                            ▼                  ▼
[usayd-flutter: Main] (CI + Approval) ─────► Internal Track ─► Production App
```

### 4.1 Deployment Sequence
1. **Step 1 — Backend Schema Migration:** Follow the [approved-for-preparation release runbook](https://github.com/mykholy/usayd-api/blob/main/docs/operations/RELEASE_PROTOCOL.md), including backup/restore proof and isolated migration lock; real deployment deferred.
2. **Step 2 — Backend Application Rollout:** Rolling update of `usayd-api` worker and web pods.
3. **Step 3 — Web Frontend Rollout:** Deploy Next.js SSR/Static build to production edge.
4. **Step 4 — Mobile Submission:** Build signed AAB (Android) and IPA (iOS), upload to TestFlight / Google Play Internal Testing, execute smoke test suite, and promote to phased release (1%, 5%, 20%, 50%, 100%).

---

## 5. Rollback & Emergency Protocols

1. **API Rollback:**
   - Because of the Expand-Contract rule, the previous container image can be redeployed immediately without rolling back database migrations.
   - If an emergency rollback is required, route traffic to the previous stable container revision.
2. **Web Rollback:**
   - Restore the previous verified immutable web deployment through the future approved hosting platform; actual provider and rollback evidence pending.
3. **Mobile Rollback / Hotfix:**
   - Native apps cannot be rolled back once downloaded by end-users.
   - If a critical bug occurs on mobile, trigger the **Kill Switch** or **Maintenance Mode** for the affected feature via backend feature flags (only through approved authorized feature-flag operations; implemented update route is `PUT /api/v1/admin/feature-flags/{key}`).
   - Ship an expedited hotfix build to app store review pipelines.

---

## 6. End-to-End Smoke Test Matrix

Prior to promoting any coordinated release, the following smoke test matrix must pass across all three repositories:

| Test ID | Flow | Target | Expected Result |
|---|---|---|---|
| `SMK-01` | Health & Readiness | `GET /api/v1/health` | 200 OK, DB connected, Redis connected |
| `SMK-02` | Correlation Tracing | Any endpoint with `X-Request-ID` | Response headers mirror `X-Request-ID` and `X-Trace-ID` |
| `SMK-03` | Localized Error Taxonomy | Test-only harness in isolated test environment; never use test route in production | RFC 7807 404 with Arabic message and traceId |
| `SMK-04` | Auth Token Refresh | `POST /api/v1/auth/refresh` | Single-use rotation, previous refresh token invalidated |
| `SMK-05` | Mobile Age-Adaptive Shell | Launch Flutter dev/staging flavor | Correct tab layout based on mode (Kids: 4, Pro: 5, Simple: 3) |
| `SMK-06` | RTL Layout & Typography | Arabic locale render | Layout mirrored, IBM Plex Sans Arabic / approved design tokens v0.4, Quranic text unaltered |
| `SMK-07` | Web SSR Hydration | Next.js landing & dashboard | Zero hydration mismatch errors, WCAG 2.2 AA targets intact |

## 7. Current verification boundary — 2026-11-27

API PR #38 published a candidate implemented contract (16 operations), with version and SHA256 verified in CI. Consumer N/N-1/N-2, actual mobile releases, live smoke tests and deployment rollback are not verified. No specialist approvers appointed; see [cross-team runbook](CROSS_TEAM_OPERATIONS_RUNBOOK.md). AWS provisioning deferred. Keep USYD-64 In Review pending actual coordination evidence; no Flutter changes.
