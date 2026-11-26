# Flow inventory and classification

Reconciles the different journey counts used in older documents:

- **24 Mermaid models** in `04_flows/*.mmd` (blueprint): 22 business/state workflows, 1 capability-policy model (16), **1 architecture diagram (21 — not a user journey)**.
- **19 clickable screen-link journeys** `F01…F19` in `USER_FLOWS.md` (older documents said 18; F19 “App launch: splash to today” was added with D-16).
- **9 critical state-model boards** `UX-JR-01…09` on the canvas (journeys group).
- **17 required end-to-end workflows** `J01…J17` in `JOURNEY_WALKTHROUGHS.md` (this release), each mapped to the above.

| Mermaid file | Kind | Walkthrough(s) |
|---|---|---|
| `01_market_selection.mmd` | BUSINESS/STATE WORKFLOW | J01, J16 |
| `02_locale_independence.mmd` | BUSINESS/STATE WORKFLOW | J16 |
| `03_payment_quote.mmd` | BUSINESS WORKFLOW | J05 |
| `04_time_zone_booking.mmd` | BUSINESS WORKFLOW | J04 |
| `05_dst_ambiguity.mmd` | BUSINESS/STATE WORKFLOW | J04 |
| `06_video_provider_switch.mmd` | BUSINESS WORKFLOW | J06, J12 |
| `07_video_failover.mmd` | STATE/DECISION MODEL | J06 |
| `08_minor_guardian_consent.mmd` | BUSINESS/STATE WORKFLOW | J02 |
| `09_teacher_shift.mmd` | BUSINESS/STATE WORKFLOW | J03 |
| `10_academic_plan_approval.mmd` | BUSINESS WORKFLOW | J08 |
| `11_supervisor_abac.mmd` | BUSINESS/STATE WORKFLOW | J11 |
| `12_competition.mmd` | BUSINESS/STATE WORKFLOW | J10 |
| `13_assessment_adaptive.mmd` | BUSINESS WORKFLOW | J08, J09 |
| `14_payroll.mmd` | BUSINESS WORKFLOW | J15 |
| `15_localized_notifications.mmd` | BUSINESS/STATE WORKFLOW | J14 |
| `16_provider_capability_matrix.mmd` | CAPABILITY DECISION (policy model) | J06 |
| `17_support_incident.mmd` | BUSINESS/STATE WORKFLOW | J14 |
| `18_config_approval.mmd` | BUSINESS/STATE WORKFLOW | J12 |
| `19_mobile_offline.mmd` | BUSINESS/STATE WORKFLOW | J07, J13 |
| `20_learning_retention.mmd` | BUSINESS/STATE WORKFLOW | J08 |
| `21_platform_architecture.mmd` | ARCHITECTURE (not a user journey) | — |
| `22_supervisor_case.mmd` | BUSINESS WORKFLOW | J14 |
| `23_teacher_selection.mmd` | BUSINESS/STATE WORKFLOW | J01, J03 |
| `24_country_activation.mmd` | BUSINESS WORKFLOW | J12, J16 |

FLOW_MATRIX.md: 7 entries had an empty “Happy path”; filled 1:1 from their sequence diagrams (03 Payment Quote, 04 Time Zone Booking, 06 Video Provider Switch, 10 Academic Plan Approval, 14 Payroll, 22 Supervisor Case, 24 Country Activation). Diagrams unchanged.
