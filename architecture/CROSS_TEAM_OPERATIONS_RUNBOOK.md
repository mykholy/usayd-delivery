# Cross-team operating runbook and decision ownership

USYD-T0035 / [USYD-78](https://mykholy.atlassian.net/browse/USYD-78). Operational overlay, 2026-11-27; original specification remains immutable. API implementation evidence: [PR #39](https://github.com/mykholy/usayd-api/pull/39) merged; [CI](https://github.com/mykholy/usayd-api/actions/runs/45902995433) passed 178 PHPUnit / 1689 assertions, 4 operational fixtures, platform and Artisan inventory checks. Cross-team acceptance remains pending.

## Ownership and approvals

| Function | Appointment | Scope of required evidence |
|---|---|---|
| Legal / DPO | UNASSIGNED | Legal entity, markets, guardian verification, consent, retention, residency, content rights |
| Academic / religious | UNASSIGNED | Licensed Quran corpus, teacher credentials, academic policies and authentic content |
| Finance | UNASSIGNED | Price books, refund/renewal, payroll and fiscal controls |
| Independent technical / security | UNASSIGNED | Contract and permission changes, sensitive changes, release review |
| Operations / support | UNASSIGNED | Incident response, support rota, restore rehearsal, production operations |

Owner confirmation 2026-11-27; Jira USYD-78 comment 10095. No names fabricated. Owner direction does not replace specialist approval or independent maker/checker. Staffing is not a reason to enable gated features. Record approved scope, person, date, and evidence before changing a gate.

## Developer handoff

- API: [README](https://github.com/mykholy/usayd-api/blob/main/README.md), [local operations](https://github.com/mykholy/usayd-api/blob/main/docs/operations/LOCAL_OPERATIONS.md), [backend standards](https://github.com/mykholy/usayd-api/blob/main/docs/standards/BACKEND_ENGINEERING.md). PHP 8.4.1+ in tested 8.4 series, Composer lock, MySQL 8.4, Redis 7.4. Horizon config exists but package not installed. Use isolated services and synthetic data only. Run Composer platform checks, Pint, actual integration tests, route parity and readiness according to the API docs.
- Web: [bootstrap instructions](https://github.com/mykholy/usayd-web/blob/main/README_BOOTSTRAP.md). USYD-81 depends on USYD-54. Do not claim a working Next.js build before implementation and green build evidence.
- Mobile: [Flutter repository](https://github.com/mykholy/usayd-flutter). Mobile developer owns its code and Jira tasks; full-stack sync reads status only. No mobile edits or credentials requested.
- Design: [screen catalog](../management/SCREEN_DESIGN_CATALOG.md), [implementation guide](../management/DESIGN_IMPLEMENTATION_GUIDE.md), exact source files and action/permission contracts for each task.
- Contracts: [producer policy](https://github.com/mykholy/usayd-api/blob/main/docs/api/CONTRACT_PUBLICATION.md). Pin tested producer SHA/version/checksum, separately review consumer changes, run negative and positive tests. PR #38 produced a candidate artifact, not approved production release. Never generate from proposed operations.

## Release and incident procedures

Follow [API release protocol](https://github.com/mykholy/usayd-api/blob/main/docs/operations/RELEASE_PROTOCOL.md) for backup, restore proof, lock-aware migration, rollout stop criteria and rollback. AWS provisioning explicitly deferred. Do not run live migrations, upload production data, retry non-idempotent jobs, flush queues, rotate existing keys or change access policy from this documentation task. Incident evidence should include trace ID, affected service/commit, sanitized logs, severity, containment action and escalation owner; do not expose minors' data or credentials. If no accountable approver exists, keep sensitive operation disabled and escalate to the owner for appointment. No guaranteed support SLA yet.

## Governance and evidence checklist

See [repository governance checklist](REPOSITORY_GOVERNANCE_EVIDENCE.md) for required protection settings. Live GitHub and Jira evidence supersedes stale reports. Update overlay after every verified PR, keep source unchanged. Report failed or unavailable CI explicitly. Required independent approval is not inferred from automated checks.

Validation of this overlay must include preflight and live-overlay verifier. No production operation is executed by these checks. Delivery CI failure/no steps is still an external blocker; cross-team acceptance must not be marked Done on documentation alone.
