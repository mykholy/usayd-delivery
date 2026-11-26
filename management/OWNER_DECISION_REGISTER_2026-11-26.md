# Owner decisions — supplementary record, 2026-11-26

Source: explicit owner chat decisions on 26 Nov and verified Jira comments 10046–10061, 10063–10070, 10077–10080. This record supplements, never overwrites, immutable DECISION_LOG.md and DECISION_REQUIRED_FROM_OWNER.md. Directions are not legal, academic or specialist approval. No production feature activation, pricing publication, data deletion or AWS purchase implied.

| Jira | Decision | Recorded direction | Outstanding evidence / safe behavior |
|---|---|---|---|
| [USYD-34](https://mykholy.atlassian.net/browse/USYD-34) | O-01 | Existing Egyptian company, owner-supplied name Usayd Academy; Egypt and GCC | Registered legal identity and per-market legal clearance; waitlist only |
| [USYD-35](https://mykholy.atlassian.net/browse/USYD-35) | O-04 | OTP + electronic guardian declaration | OTP proves possession not guardianship; legal/DPO approval per market; minors limited |
| [USYD-36](https://mykholy.atlassian.net/browse/USYD-36) | O-06 | King Fahd Quran Printing Complex, subject to license verification | Exact corpus/version/riwayah, distribution rights and academic/legal signoff; no unverified text |
| [USYD-37](https://mykholy.atlassian.net/browse/USYD-37) | D-42 | Separate public/admin/teacher API namespaces | Tech-lead contract and field/scope authorization review |
| [USYD-38](https://mykholy.atlassian.net/browse/USYD-38) | O-03 | Delegated vendor selection: LiveKit candidate for PoC, external links fallback | Latency, DPA, costs and approval; no live vendor activation |
| [USYD-39](https://mykholy.atlassian.net/browse/USYD-39) | O-05 | Recording and AI off by default; explicit separate consent per purpose; proposed 30/7/90 day retention | Legal/DPO approval; no processing or destructive lifecycle activation |
| [USYD-40](https://mykholy.atlassian.net/browse/USYD-40) | O-07 | Certificates and non-monetary badges only initially | Approved contest terms and badge catalogue |
| [USYD-41](https://mykholy.atlassian.net/browse/USYD-41) | O-08 | Support lesson, hourly, salary and hybrid teacher pay | Finance/legal contracts and market wage rules; payroll off |
| [USYD-42](https://mykholy.atlassian.net/browse/USYD-42) | D-24 | Canonical routes and redirects | Review exact aliases and permissions; pricing UX-GLOB-002; settings UX-SUP-010 |
| [USYD-43](https://mykholy.atlassian.net/browse/USYD-43) | D-35 | Proposed Kids 6–12, Pro 13–59, Simple 60+, changeable | Academic approval; minors 13–17 still safeguarded |
| [USYD-44](https://mykholy.atlassian.net/browse/USYD-44) | D-39 | Time-boxed break-glass, MFA, audit, 24h review direction | Security/safeguarding approval; assigned officer only pending policy |
| [USYD-45](https://mykholy.atlassian.net/browse/USYD-45) | O-02 | Delegated pricing; illustrative monthly 4/8/12 lessons of 30 min: Egypt 399/749/1049 EGP, Saudi 79/149/209 SAR | Not market validated or approved; costs, market price books, renewal/refund approval; checkout off |
| [USYD-46](https://mykholy.atlassian.net/browse/USYD-46) | O-09 | 24-hour support conditional on staffing | Rota, channels, response/escalation targets; no guaranteed published SLA |
| [USYD-47](https://mykholy.atlassian.net/browse/USYD-47) | D-44 | Retain tagline as design direction | Academic approval of precise wording/source; hadith not approved |
| [USYD-48](https://mykholy.atlassian.net/browse/USYD-48) | O-10 | Implement all planned features before public launch, not MVP first | Funding amount/tranches unspecified; incremental tests and all release gates remain |
| [USYD-49](https://mykholy.atlassian.net/browse/USYD-49) | D-16 | Keep splash screen UX-MOBILE-000 | Decision Done only, not Flutter implementation |
| [USYD-50](https://mykholy.atlassian.net/browse/USYD-50) | D-27 | Revenue, subscriptions, attendance and retention KPIs direction | Signed definitions/denominators/time windows and revenue recognition |
| [USYD-51](https://mykholy.atlassian.net/browse/USYD-51) | D-36 | Private teacher-awarded non-monetary kids badges | Academic catalogue and criteria pending |
| [USYD-52](https://mykholy.atlassian.net/browse/USYD-52) | D-43 | Reuse GET /api/v1/achievements direction | Technical contract approval, D-36 catalogue |
| [USYD-53](https://mykholy.atlassian.net/browse/USYD-53) | D-37 | Faceless graphics; no face mascot | Decision Done only |
| [USYD-71](https://mykholy.atlassian.net/browse/USYD-71) | Storage | AWS private S3; 30 days recordings, 7 days AI audio, 90 days security logs conditional on legal approval | PR #29 merged, tested S3-compatible/ClamAV. Actual AWS IAM/region/production signature freshness and retention signoff pending; no live upload route |
| [USYD-77](https://mykholy.atlassian.net/browse/USYD-77) | Infrastructure | Owner deferred server provisioning; delegated region choice. Frankfurt eu-central-1 provisional engineering candidate | Recheck AWS Health, latency, calculator and legal residency before purchase; PR #30 merged; actual deployment evidence pending; no actual staging deployed |

## Evidence

- [Current live delivery state](../automation/LIVE_DELIVERY_STATE.json) and [PR evidence](../automation/PR_APPROVAL_QUEUE.md).
- API #26, #27, #28, #29 merged normally with automated green checks; no independent human approval inferred. PR #29: 178 tests/1689 assertions, 16 actual API operations and 13 OpenAPI fixtures. USYD-71 In Review, not Done; legal/DPO retention and real AWS verification remain gates.
- Technical region recommendation is provisional, not legally approved; [AWS regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html), [AWS Health](https://health.aws.amazon.com/health/status), [data privacy](https://aws.amazon.com/compliance/data-privacy-faq/).
- USYD-54 branch protection verification, USYD-64 release coordination, USYD-65 authentic media/content remain open. Never fabricate specialist signoff. Flutter implementation untouched.
