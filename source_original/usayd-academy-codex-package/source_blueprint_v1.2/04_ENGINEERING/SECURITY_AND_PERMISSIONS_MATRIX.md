# Authorization matrix (draft least privilege)

Legend: `O` own data, `A` assigned student or task, `R` role-authorized aggregate/record, `-` denied. Exact policy conditions also require minor consent, publication and purpose limits.

| Resource/action | Learner | Teacher | Academic | Support | Finance | Admin |
|---|---|---|---|---|---|---|
| Own learning plan | O read | A read/propose | R approve | - | - | R audit |
| Teacher-approved grades | O read | A create/propose | R approve/correct | - | - | R audit |
| Booking | O create/edit | A view/request | R override | R resolve | - | R audit |
| Protected classroom join | O if entitled | A if assigned | R only for authorized supervision | - | - | R exceptional |
| Minor guardian contact | O limited | - | R limited purpose | R for authorized support | - | R exceptional |
| Session transcript/audio | O only permitted access | A if consent/license permits | R restricted | - | - | R exceptional with audit |
| AI policy flags | - | R own case feedback after decision | R specialist | R safeguarding only | - | R limited |
| Question bank draft | - | A create | R approve | - | - | R audit |
| Competition join | O if eligible | - | R judges | R support | - | R configure |
| Contest judging | O own score only | A assigned as judge | R approve | - | - | R audit |
| Public scoreboard | O public-opted adult or private own; minors private | R as authorized | R | R public only | - | R governed |
| Teacher contract/payout | - | O statements | - | - | R approve | R restricted |
| Payment invoice | O | - | - | R support view limited | R full | R restricted |
| Customer marketing contact | O preferences | - | - | R assigned and consented | - | R governance |
| Consent withdrawal | O appropriate actor | O teacher consent | - | R facilitate authorized | - | R audit |

## Mandatory enforcement

Policy object-level checks for every resource; no UI-only hiding; independent staff privilege escalation approval, privileged MFA, guard personal data exports, audit high-sensitivity access and contest publication. Vendor meetings may not offer equivalent isolation; show clear capability limitations and secure meeting host policy.
