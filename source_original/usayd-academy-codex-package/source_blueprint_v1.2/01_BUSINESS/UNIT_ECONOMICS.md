# Financial model and unit economics (illustrative only)

## Pricing hypotheses

| Package | Egypt | Gulf test | Lessons | Notes |
|---|---:|---:|---|---|
| 1:1 Basic | EGP 799 | USD 30 | 8 × 30 min | Reference mix |
| 1:1 Standard | EGP 1099 | USD 43 | 12 × 30 min | Margin by duration |
| 1:1 Intensive | EGP 1399 | USD 55 | 16 × 30 min | Teacher capacity risk |
| Small group | EGP 399 / seat | USD 18 / seat | 8 × 40 min | Requires matched level; phase 2 |

## Simple controllable model

`Average revenue = EG_share*EG_price + Gulf_share*USD_price*FX`.

`Teacher cost / learner = delivered_lessons_per_learner * full_cost_per_lesson`.

`Video cost = participants * elapsed_minutes * vendor_effective_rate + egress + storage + network + add-ons`.

`AI cost = analyzed_minutes * STT_rate + token_input/output + monitoring + review_labor + storage`.

`Contribution/learner = collected_rev - refunds - processing - teaching - video - AI - per-learner service costs`.

`Replacement acquisition cost = active_students * monthly_paid_churn * fully_loaded_CAC`.

`Operating result = active_students * contribution_per_learner - replacement_CAC - fixed_overhead - founder pay - payroll taxes` (do not mix cash and revenue recognition).

## Base test calculation (reference, NOT forecast)

- 70% Egyptian learners at EGP 799, 30% Gulf at USD 30; **assumed FX = EGP 50/USD**.
- Average gross revenue per learner = `0.7*799 + 0.3*1500 = EGP 1009.30`.
- 8 × 30min teacher cost at assumed EGP 50/lesson = **EGP 400**.
- Card/payment fees assumption 3.5% ≈ **EGP 35.33**.
- 2-person video per learner = `8*30*2 = 480 participant-minutes`, plus egress and STT separately.
- Support variable EGP 30 per learner, technology variable estimated from quotes at decision time.
- Assumed monthly churn 15%, replacement CAC 350 → expected replacement acquisition burden = 52.5 EGP/active learner/month (NOT new-growth CAC).

At 100 active learners revenue = EGP 100,930; teaching alone = EGP 40,000. Every EGP 10 change in teacher/lesson cost changes monthly cost by **EGP 8,000**. Recalculate in `financial_scenarios.csv` with actual paid cohorts before investor presentation.

## Capacity model

If a 30-minute lesson + 10-minute buffer = 40 minutes effective teacher capacity, a 6-hour teaching allocation supports 9 bookable lessons/day before scheduling losses. Never assume 16 uninterrupted half-hour lessons in an 8-hour shift. Account for prep, breaks, reporting, cancellations, overlap, weekly rest and local labor rules.

## Scenario driver table

| Lever | Downside | Base hypothesis | Upside | Sensitivity |
|---|---|---|---|---|
| Paid learner mix (Gulf) | 0% | 30% | 50% | Price and CAC vary jointly |
| Full teaching cost per lesson | EGP 75 | EGP 50 | EGP 40 | 8× cost per learner |
| Paid churn per month | 25% | 15% | 8% | Reacquisition & lifetime |
| Fully loaded CAC | EGP 650 | EGP 350 | EGP 200 | Include trials/support time |
| Lesson delivery % | 100% cost with makeup | 95% | 90% | Beware under-delivery misleading 'margin' |
| Active learners | 30 | 100 | 300 | Must reconcile teacher capacity |

## Retention and LTV caveats

Simple steady-state expected paid tenure = `1/churn` months *if constant hazard holds*. Do not promise LTV without observed cohort renewals and refunds. A retained learner has a cost of delivery every month; never use gross subscription price as LTV profit. Churn and CAC differ by country, adult/minor, teacher and package.

## Accounting controls

Double-entry / journal-style transaction records for revenue, teacher accrued costs, refunds, settlement deposits, cash vs recognized revenues; independent reconciliation. Teacher payroll model has effective-dated rules and no retroactive recalculation of approved payout snapshots.
