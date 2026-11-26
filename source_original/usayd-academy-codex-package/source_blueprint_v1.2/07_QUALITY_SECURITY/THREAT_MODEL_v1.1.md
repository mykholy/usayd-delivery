# Threat model — core STRIDE and abuse cases

| Asset / flow | Threat | Control | Verification |
|---|---|---|---|
| Learner profile | IDOR/BOLA across learner IDs | policy with resource ownership and purpose; deny by default | API tests for cross-learner GET/POST |
| Minor enrollment | fake guardian/consent bypass | OTP or equivalent verified consent receipt, immutable versions | consent withdrawal/forgery tests |
| Conference link | token theft, unauthorized join | short TTL grant, room scoped, join server policy | stolen token/expired/join replay |
| Audio AI | covert collection or over-retention | purpose toggle, visible notices, job consent recheck, deletion schedule | revoke mid-queue; log inspection |
| Quran content | poisoned text/riwaya mismatch | pinned corpus hash, approved license, academic editorial review | hash and academic fixture tests |
| Payment | forged webhook, replay, race | raw signature, timestamp bound, idempotency, journal | 5 duplicate webhooks + out of order |
| Bookings | double-slot/double-credit | DB transaction + unique active key + immutable ledger | concurrency load test |
| Contest | answer leakage, paid ranking, judge collusion | question bank RBAC, judge conflict, approved score versions | adversarial E2E and score re-evaluation |
| Teacher payout | duplicate accrual / unauthorized approval | rule snapshots, maker/checker, payrun ledger | payroll state machine tests |
| Support/admin | staff exfiltration, secret in audit | least privilege, redaction, MFA, alerts | permission matrix automated |
| AI prompt | voice/transcript prompt injection to agent | treat transcript as data, strict schema & no tool privilege | injection suite |
| Media storage | public exposure, stale signed URL | private bucket, short signed URL, rotate/revoke | URL expiry and ACL tests |

Privacy and safeguarding reviews are distinct from cyber security; serious child-safety reports require named trained incident responder and documented escalation, not AI-only handling.
