# USAYD ACADEMY — COMPREHENSIVE SECURITY, CONCURRENCY & GOVERNANCE AUDIT
**Date:** November 24, 2026  
**Repositories Audited:**  
- `usayd-api` (`https://github.com/mykholy/usayd-api`)
- `usayd-web` (`https://github.com/mykholy/usayd-web`)
- `usayd-flutter` (`https://github.com/mykholy/usayd-flutter`)
**Applicable Regulations & Standards:** OWASP API Security Top 10 (2023), RFC 7807/9457, GDPR/COPPA Minor Protections, ISO/IEC 27001 Auditability.

---

## 1. Executive Summary

This independent security and concurrency audit evaluates the foundational architecture implemented across Sprint S00 and Sprint S01 for the Usayd Platform. The system implements a defense-in-depth posture with strict boundary separation between mobile and web clients, immutable audit logging, and resilient concurrency controls against MySQL 8.4 LTS InnoDB.

---

## 2. Concurrency, Transaction Isolation & Idempotency Harness

### 2.1 MySQL 8.4 InnoDB Transaction Isolation
- **Default Isolation Level:** MySQL 8.4 uses `REPEATABLE READ` with Next-Key Locking to eliminate phantom reads.
- **Pessimistic Row-Level Locking:** High-contention financial, slot booking, and reservation operations in `usayd-api` employ `SELECT ... FOR UPDATE` within atomic transaction closures (`DB::transaction`).
- **Deadlock Mitigation (`ResilientTransaction`):** Implemented in PR #6 (`USYD-T0025`), critical transactions are wrapped in automatic exponential retry loops with jitter (up to 3 retries on SQLSTATE `40001` / error code `1213`).

### 2.2 Idempotency Key Scoping Architecture
- **Vulnerability Addressed:** Replay attacks, duplicate payments, and multi-tenant key collision.
- **Enforcement Mechanism:**
  - Header: `Idempotency-Key` (UUIDv4 or cryptographic hash).
  - **Compound Cache/DB Key:** Keys are never stored as bare strings. The lookup key is strictly scoped:
    $$\text{CompoundKey} = \text{hash}(\text{principal\_id} \,\|\, \text{operation\_name} \,\|\, \text{idempotency\_key})$$
  - Unauthenticated requests cannot invoke idempotent mutating state transitions.
  - In-flight operations acquire an atomic Redis lock (`lock_ttl = 30s`) to reject concurrent duplicate submissions with RFC 7807 `409 Conflict`.
  - Finished executions cache the serialized response payload, HTTP status, and headers for 24 hours.

---

## 3. Dual Authentication Boundary & Token Lifecycle

### 3.1 Web vs. Mobile Dual Boundary
The system cleanly separates web session authentication from mobile bearer authentication:
1. **Web SPA Boundary (`usayd-web`):**
   - Uses Laravel Sanctum SPA stateful cookie authentication.
   - Cookies: `HttpOnly = true`, `Secure = true`, `SameSite = Lax`.
   - CSRF token validation on all mutating requests (`X-XSRF-TOKEN`).
2. **Mobile Boundary (`usayd-flutter`):**
   - Uses Sanctum API Bearer Tokens (`personal_access_tokens`).
   - Tokens are stored in hardware-backed secure storage (`FlutterSecureStorage` via iOS Keychain / Android KeyStore).

### 3.2 Single-Use Refresh Token Rotation & Race Handling
- **Rotation Contract:** Refresh tokens are state-backed in MySQL and single-use only.
- Upon calling `POST /api/v1/auth/refresh`:
  1. The incoming refresh token is verified against the hash in `personal_access_tokens`.
  2. The current token is **immediately revoked** in the database.
  3. A new access token and a new single-use refresh token are issued.
- **Concurrent Refresh Race Condition Mitigation:**
  - In `usayd-flutter` (`ApiClient`), concurrent 401 interceptors are coalesced into a single in-flight `Future<AuthTokens>` request.
  - Secondary concurrent requests wait for the primary refresh promise to resolve, rather than triggering multiple conflicting refresh requests.
- **Brute-Force Protection:**
  - Login endpoint (`POST /api/v1/auth/login`) enforces strict rate limiting: maximum 5 failed attempts per minute per IP/Email.
  - Exceeding the threshold yields RFC 7807 `429 Too Many Requests`.

---

## 4. Audit Trail & Immutability Guarantees

### 4.1 Eloquent Lifecycle Hooks vs. Database-Level Immutability
In PR #10 (`USYD-T0029`), the `AuditEvent` model provides append-only audit logging:
```php
static::updating(function () {
    throw new \RuntimeException('Audit events are strictly immutable and cannot be updated.');
});
static::deleting(function () {
    throw new \RuntimeException('Audit events are strictly immutable and cannot be deleted.');
});
```

### 4.2 Security Limitations & Production Requirements
- **Audit Finding:** Eloquent model lifecycle hooks protect all operations executed via standard Eloquent ORM calls (`$event->update()`, `$event->delete()`).
- **Limitation:** They do **not** intercept:
  1. Direct Query Builder calls (`DB::table('audit_events')->where(...)->delete()`).
  2. Raw SQL statements (`DB::statement('DELETE FROM audit_events ...')`).
  3. Direct administrative SQL commands executed by database administrators.
- **Production Hardening Requirement (D-39):**
  To guarantee complete database-level immutability in production:
  1. **MySQL Triggers:** Enforce triggers that reject updates and deletions:
     ```sql
     CREATE TRIGGER audit_events_no_update BEFORE UPDATE ON audit_events
     FOR EACH ROW SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'audit_events is append-only';
     CREATE TRIGGER audit_events_no_delete BEFORE DELETE ON audit_events
     FOR EACH ROW SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'audit_events is append-only';
     ```
  2. **Principle of Least Privilege:** The application database user must be granted only `SELECT, INSERT` on the `audit_events` table (revoking `UPDATE, DELETE, DROP, ALTER`).

---

## 5. Three-Dimensional Authorization Matrix

Privilege verification in `usayd-api` enforces a 3D matrix:
$$\text{Permission} = f(\text{RBAC Role}, \text{Operational Scope}, \text{Resource Ownership})$$

| Role | Permitted Actions | Scope Limitations | Reason Required (`X-Audit-Reason`) |
|---|---|---|---|
| `learner` | Read own plan, attend session, submit homework | Own user resources only | No |
| `teacher` | Grade homework, view assigned students, set marks | Assigned learners only | No |
| `academic` | Review curricula, certify Ijazah, inspect sessions | Academic domain | Yes |
| `support` | View learner tickets, assist in live room issues | Assigned tickets | Yes |
| `finance` | Review settlements, issue refunds, export invoices | Financial operations | Yes |
| `admin` | System config, role assignments, user management | Global | Yes (Mandatory) |

- **Reason Metadata Enforcement:** Privileged administrative actions fail with RFC 7807 `400 Bad Request` if the `X-Audit-Reason` header is missing or fewer than 10 characters.

---

## 6. Information Leakage & Error Taxonomy

- **Zero Debug Leakage:** When `APP_DEBUG=false`, uncaught exceptions are caught by `Handler.php` and rendered as RFC 7807 `500 Internal Server Error` with:
  - Sanitized title: «حدث خطأ داخلي في الخادم»
  - No database credentials, SQL queries, or stack traces in response body.
  - Unique `traceId` (`X-Trace-ID`) for correlation in internal error logs.

---

## 7. Audit Conclusion & Sign-Off Checklist

The current security baseline in `usayd-api` and `usayd-flutter` conforms to high security standards for sensitive educational and financial workloads. All pull requests are gated by the `human-approval-gate` CI check to prevent unauthorized automated merging.
