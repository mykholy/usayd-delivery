# Implementation Roadmap, Phases, Sprints & Stage Gates
**Planning horizon:** 24–32 weeks for staged comprehensive product with lean team; actual velocity unknown. P0 paid pilot may be earlier if scope constrained and vendor POC passes.

## Time-based sequencing proposal

| Phase | Weeks | Key work | Exit gate / measurable evidence |
|---|---|---|---|
| 0 Discovery & contracts | 1–3 | product/academic/legal, teacher recruitment, price interviews, video SDK 2-vendor POC, Figma foundations | sponsor, academic, legal approve pilot; real payment and provider viability |
| 1 Foundation and web | 4–7 | auth unified learner/guardian consent, teacher directory, programs, public/web design, API core | independent adults enroll, minors appropriately gated, verified teacher profiles |
| 2 Paid Academy MVP | 8–12 | package/payment, booking, attendance, provider join, lesson report, admin/teacher schedule | paid end-to-end with 10–20 learner pilot; no critical safety/billing bugs |
| 3 Learning and exams | 13–16 | verified plans, memory map, revision, exams/question bank, library | academic rubric and plan approval verified |
| 4 Competitions and engagement | 17–20 | contest builder, eligibility, judges, results, privacy, appeals, certificates | fairness/privacy/legal sign-offs, contest UAT from entry to appeal |
| 5 AI assistants and policy | 21–25 | evidence-backed plans, summaries, assistant, consented transcript review, cost limits | offline model evaluation, no silent AI decisions, consent gate |
| 6 Mobile production & optimize | 26–32 | Flutter learner and teacher core, native video SDK, push, performance and security, optional recitation research | store readiness, 3G/device tests, finance/retention decision |

**Parallel:** growth discovery/teacher quality/recruitment, public website/SEO and customer support can operate alongside engineering. Any advanced AI recitation proof-of-concept remains a separate research gate.

## Feature gate levels

- `P0-BASE`: safe all-age identity, verified guardian process, curriculum, qualified teacher, paid entitlements, booking, attendance, report, help, basic dashboards, secure API and basic video.
- `P1-LEARNING`: teacher-approved plan, spaced revision, memorization map, question bank, adaptive tests, recorded rights-compliant content, contest with human judging/appeals.
- `P1-AI`: assistant recommendations, teacher copilot, session intelligence pilots with legal consent and false-positive evaluation.
- `P2-MOBILE`: Flutter clients and native call support.
- `P2-EXPERIMENTAL`: Quran ASR + automatic probable mistake detection only after academic model benchmark and disclosures.

## Release gate checklist per phase

**Academic:** correct Quran text/reference, qualified reviewers, accessible level rubric, error reporting, no fictitious Quran correctness.

**Safety:** age/guardian consent and child protections; privileged access audit; recording appropriately disclosed; contests fair, minors anonymous/default private; escalation owner staffed.

**Finance:** valid payment webhooks, invoice/refund and fully-loaded teacher compensation verified; all numeric terms in actual contracts.

**Engineering:** OpenAPI contract, server authorization, concurrency, staging, rollback, incident runbook, all critical test cases green.

**Business:** pilot/retention observed, price by market, realistic CAC; no claims from proxy TAM.

## Delivery RACI

| Decision | Accountable | Responsible | Consulted |
|---|---|---|---|
| Scope/pricing | CEO/Product Owner | Product/Growth | Finance, academic |
| Quran content/rubrics/contests | Academic Lead | Teachers/academic reviewer | Legal, Product |
| Security/architecture/video | CTO | Backend/DevOps/QA | Privacy, Product |
| Consent/recording/minor policies | Legal/DPO | Product/Engineering | Academic, Safeguarding |
| Payroll payout | Finance Controller | Payroll Operations | HR/Legal |
| Student safety incident | Safeguarding Lead | Authorized support/team | Legal, Academic |
| Figma UX / accessibility | UX Lead | Product Designer | Engineering/QA |
| Paid media/retention | Growth Owner | Growth/CRM | Finance/Product |

## Investor sign-off proposal

Fund discovery & paid pilot with explicit cap and reserve; release further tranche upon achieved paid starts and first renewals, lessons delivered on time and acceptable unit economics. More investment on advanced AI should follow verified quality/evaluation, not just a demo.
