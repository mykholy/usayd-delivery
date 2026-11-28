# S01 — live status (2026-11-26)

Candidate sprint labels, not confirmation of active/closed Jira sprint. Source: [LIVE_DELIVERY_STATE.json](LIVE_DELIVERY_STATE.json). Supersedes historical 24 Nov claims; history retained in Git.

All: 5/10 Done. Non-Flutter: 5/6 Done. Flutter statuses read only, not independent mobile test verification.

| Jira | Stable ID | Scope | Live status | Summary |
|---|---|---|---|---|
| [USYD-66](https://mykholy.atlassian.net/browse/USYD-66) | USYD-T0027 | non-flutter | Done | API RFC7807 error taxonomy & localization |
| [USYD-67](https://mykholy.atlassian.net/browse/USYD-67) | USYD-T0028 | non-flutter | Done | Auth/API security scaffolding |
| [USYD-68](https://mykholy.atlassian.net/browse/USYD-68) | USYD-T0029 | non-flutter | Done | Authorization gates and audit trail |
| [USYD-69](https://mykholy.atlassian.net/browse/USYD-69) | USYD-T0030 | non-flutter | Done | Feature flags & kill switches |
| [USYD-70](https://mykholy.atlassian.net/browse/USYD-70) | USYD-T0031 | non-flutter | Done | Transactional outbox for notifications |
| [USYD-71](https://mykholy.atlassian.net/browse/USYD-71) | USYD-T0032 | non-flutter | In Review | Storage privacy and signed links |
| [USYD-72](https://mykholy.atlassian.net/browse/USYD-72) | USYD-T0079 | flutter-read-only | In Review | Flutter typed API client, token storage and refresh contracts |
| [USYD-73](https://mykholy.atlassian.net/browse/USYD-73) | USYD-T0080 | flutter-read-only | In Review | Flutter routing and account permissions |
| [USYD-74](https://mykholy.atlassian.net/browse/USYD-74) | USYD-T0081 | flutter-read-only | In Review | Flutter offline queue and encryption scaffolding |
| [USYD-75](https://mykholy.atlassian.net/browse/USYD-75) | USYD-T0082 | flutter-read-only | In Review | Flutter testing infrastructure |

USYD-71 engineering merged in PR #29, 178 tests / 1689 assertions, SeaweedFS and ClamAV verified; Jira remains In Review for retention approval. AWS provisioning deferred.
