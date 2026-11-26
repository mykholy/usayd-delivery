# Decision register / ADR-lite

## Confirmed design assumptions

| ID | Decision | Rationale | Revisit trigger |
|---|---|---|---|
| DEC-01 | Every user initially registers as `Learner` | Simple conversion and all-age product | Guardian portal phase later |
| DEC-02 | For minors, bind verified guardian contact/consent as required | Legal / safeguarding compliance without complex parental UI | Legal sign-off per country |
| DEC-03 | Modular Laravel monolith, API first, OpenAPI versioned | Lower complexity, strong domain boundaries | Scale bottleneck evidenced |
| DEC-04 | `VideoProvider` and `ClassroomClientAdapter`, not provider SDK spread across app | Avoid lock-in while respecting capability differences | Vendor test results |
| DEC-05 | Teachers may use salary, lesson, hour, shift or hybrid contracts | Business flexibility and enforceable payroll | Legal/local wage review |
| DEC-06 | Recorded curriculum is supplementary; live 1:1 primary | Learning quality | Actual cohort findings |
| DEC-07 | Academic correctness signed off by qualified teachers | AI hallucination and safety | Validated specialist ASR |
| DEC-08 | Competitions level-appropriate and opted in | Fairness and safety | Review retention and harms |
| DEC-09 | No compulsory recording for all sessions | Privacy and cost | Valid lawful basis + demonstrated necessity |
| DEC-10 | Provider-specific features degrade gracefully | Google Meet/Zoom meetings != embedded video SDK | New vendor capability |

## Open investor/product decisions (do not guess)

| ID | Decision required | Suggested default | Owner / gate |
|---|---|---|---|
| O-01 | Commercial legal entity and eligible geographies | Egypt initially; KSA pilots after settlement validation | Legal/CEO / before first payments |
| O-02 | Initial pricing tiers and currency | 8×30m entry offer; A/B test pricing | Commercial / before ads |
| O-03 | P0 in-app conferencing vendor | LiveKit and VideoSDK technical POC; Meet fallback | CTO / before build |
| O-04 | Which minors can enroll and required parent process | Stop before payment until consent verification | Legal / before onboarding minors |
| O-05 | Recording + AI processing purposes & consent | Disabled by default | Legal/DPO / before enabling features |
| O-06 | Academic supervisor and Quran content rights | Contract qualified owner and verify source license | Academic/Legal / before curriculum |
| O-07 | Prize policy for contests | Noncash learning rewards; no paid advantage | Legal/Academic / before contest launch |
| O-08 | Payroll contract forms and minimum wages | No payroll contract activated without local legal review | Finance/Legal / before teacher contracts |
| O-09 | Baseline support service hours and staff | Local coverage + response SLA, budgeted | Ops / before launch |
| O-10 | Funding amount and approval tranche | Gates: paid pilot → retention → controlled scale | Investors / funding meeting |

## Change control

Each scope change: author RFC → impact on requirement IDs + OpenAPI + UX + QA + Jira → Academic/Legal signoffs if applicable → new version/tag. No silent scope addition.
