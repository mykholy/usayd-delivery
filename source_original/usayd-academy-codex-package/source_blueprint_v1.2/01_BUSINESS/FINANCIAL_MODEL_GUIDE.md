# Financial model guide and spreadsheet-equivalent logic

`financial_scenarios.csv` is **not observed revenue** and not a signed financial plan. Every input is a management hypothesis and must be replaced by quotes and cohort data. Numbers shown in EGP unless marked otherwise. FX assumption 50 EGP/USD is illustrative, not current rate quote.

## Formulas

```
ARPU = (1 - GulfShare)*799 + GulfShare*(30 USD * 50 EGP/USD)
Revenue = ActiveLearners * ARPU
Teacher = ActiveLearners * LessonsPerLearner(8) * TeacherPerLesson
Video = ActiveLearners * Lessons(8) * Duration(30m) * Participants(2) * USD_per_participant_min(0.004) * FX(50)
Processing = 0.035 * Revenue
Support = 30 * ActiveLearners
AI = AI_budget_per_learner * ActiveLearners
Contest moderation = contest_budget_per_learner * ActiveLearners
Replacement ad spend = ActiveLearners * monthly_churn * fully_loaded_CAC
Overhead = fixed_base + active_learners * scaled_overhead_rate
OperatingResult = Revenue - Teacher - Video - Processing - Support - AI - Contests - ReplacementAdSpend - Overhead
```

**Cost caveats:** Video `.004` is a *synthetic normalized scenario*, not a final vendor offer; may double-count or exclude actual plan allowances, recording, traffic and taxes. Teacher per lesson must be *fully loaded* under chosen contract. AI and contest budgets are assumptions, not vendor quotes. `replacement CAC` finances maintenance of a stable active learner base, **not growth to the selected size from zero**. Paid acquisition of 100 new learners incurs full CAC for all 100 and may make the initial month loss-making. Taxes, founder pay, platform CAPEX, specialized academic training and payment refunds may require additional lines.

## Example base 100 learners

From CSV: confirm row for 100/base. Prices by market should be revised independently and validated with paid cohorts before investing. See sensitivities in downside vs upside rows for 25/50/100/300/500/1000 learners.

## Teacher model unit evaluation

`Per lesson cost = settled eligible lessons × agreed fee`; hourly per lesson equivalent `paid eligible teacher minutes / delivered lesson count × hourly rate`; shift `shift payable cash / delivered eligible lessons`; monthly salary `fully loaded salary / eligible delivered lessons`. Compare only identical service quality/contract compliance and teacher capacity. Idle-time cost must be included, and teacher holidays/rest cannot be removed to make a theoretical margin.
