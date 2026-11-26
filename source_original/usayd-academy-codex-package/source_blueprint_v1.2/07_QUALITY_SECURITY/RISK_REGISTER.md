# Risk register and owner actions

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Trigger |
|---|---|---|---|---|---|---|
| R-01 | Weak paid demand or price acceptance | Med | High | Paid pilot, segmented pricing | Growth | Qualified-lead → paid low |
| R-02 | Teacher cost exceeds revenue margin | Med | High | Models salary/hour/lesson and capacity review | Finance | Teacher direct cost > planned unit value |
| R-03 | Major video provider outage | Med | High | adapter/feature policy, refund fallback, POC | CTO | Join success dips |
| R-04 | Google Meet media API shutdown impacts AI | High | Med | Do not depend on Google Meet live audio | CTO | Vendor cutoff 2027-01-15 |
| R-05 | Wrong Quranic feedback by AI | Med | Very High | verified source, specialist benchmarks, teacher gate | Academic/AI | Model flags incorrect verse |
| R-06 | Child privacy/safeguarding incident | Med | Very High | consent, vetted teachers, no open contact, escalations | Safety | Incident ticket |
| R-07 | Competition unfairness or cheating | Med | High | level bands, judges, appeal, immutable scores | Academic | Appeal overturn spikes |
| R-08 | High AI processing costs | High | Med | quotas, batch, opt-in, trace cost | Engineering | Spend/learner budget breach |
| R-09 | Low subscription renewal | Med | High | verified plan, quality, proactive support | Product | Renewal cohort below gate |
| R-10 | Payment chargebacks/settlement failure | Med | High | verified webhook, ledger, provider reconciliation | Finance | Reconciliation mismatch |
| R-11 | Cross-border payment restrictions | Med | High | verify checkout and merchant settlement before ads | Legal/Finance | KSA card failure |
| R-12 | Teacher poaching | High | Med | value-added service, contact protection, enforceable contract | Ops | Verified off-platform solicitation |
| R-13 | Unauthorized source content or recording | Med | High | license registry, media policies and provenance | Legal/Academic | Rights complaint |
| R-14 | Shipping entire scope at once | High | High | release gating, owner decisions, feature flags | Sponsor/Product | Cycle time/slippage |
| R-15 | Jira backlog oversized for team | High | Med | refine epics, prioritize thin vertical slices | PM/CTO | Repeated sprint carryover |
| R-16 | Vendor data residency conflicts | Med | High | DPA, processor map and options | Privacy | Provider fails compliance |
| R-17 | Accessibility on Quran/RTL | Med | Med | WCAG and Arabic diacritic QA | UX/QA | Clip/focus bugs |
| R-18 | Mobile app stores reject permissions | Med | Med | privacy disclosure, careful mic/audio and native SDK tests | Mobile Lead | Store review failure |
