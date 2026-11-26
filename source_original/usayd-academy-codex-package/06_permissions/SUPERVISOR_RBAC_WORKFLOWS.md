# Supervisors, roles, permissions and operational workflows

## Roles (one human may have multiple authorized roles)
| Role | Responsibility | Allowed scope | Explicitly denied without extra grant |
|---|---|---|---|
| `super_admin` | role assignment, infrastructure governance | full meta operations, audited | self-approve finance, access minors' audio without purpose |
| `platform_admin` | catalog/policy/regions/config changes | allowed markets | secret reveal, self-approve prod switch |
| `operations_supervisor` | capacity, teacher scheduling, escalation | own regions/programs | grades and payouts final approval |
| `academic_supervisor` | teacher vetting, programs, level validation, plans | assigned programs + student cohorts | payments, raw learner contacts, recordings without consent |
| `quality_supervisor` | observation and class quality audits | assigned samples and lawful data access | payout alteration or disciplinary automation |
| `safeguarding_officer` | minors' safety, incidents, protected reporting | need-to-know incidents, emergency break-glass with logs | blanket ongoing hidden monitoring |
| `competition_manager` | stages, registration, content scheduling | assigned contests/markets | judge final results independently |
| `competition_judge` | score assigned submissions | assigned rounds, blinded where possible | score publication, own family/student evaluation |
| `finance_manager` | invoices, refunds, payroll rules | legal entity/market scope | teacher assignment, judge scoring |
| `finance_approver` | payouts/refund batch approval | independent from creator | own initiated transaction approval |
| `support_agent` | learner tickets and booking help | assigned queues, minimal PII | transcript access, grade override, secret management |
| `regional_manager` | rollout, teacher supply, regional funnel | assigned countries | activate market without compliance/finance review |
| `content_localization_manager` | English/Arabic text/local content | locale content draft | publish legal/academic claims without review |
| `security_admin` | credentials, IAM, audits | managed systems | view private course or audio content by default |
| `teacher` | assigned learners, classes, reports | own teaching assignments | raw student contact, payouts other teachers |
| `learner` | learning, bookings, payments | own account | other students' records |

## Permission enforcement equation
`allow = actor.active && permission.granted && resource.scope(region,program,cohort,assignment) && purpose.authorized && consent.valid_if_needed && workflow.state_allows && separation_of_duties_satisfied`.
- Backend policies, scoped DB queries, queue worker rechecks, audit events. UI visibility follows but does not replace authorization.
- Privileged staff roles have MFA and session renewal; temporary grants expire; emergency `break_glass` requires named reason, limited duration, alert and independent retrospective review.
- Staff access to minors' contact/audio requires documented safeguarding purpose and relevant consent/legal basis. Audit includes resource id, actor, purpose, action, decision, timestamp; logs redact text/audio/secret.

## Supervisory operating journeys
### Academic assessment approval
Teacher proposes a level/plan and attaches rubric evidence -> academic supervisor queue filters market/program -> sees relevant progress only -> accepts / requests change / rejects with note -> learner and teacher notified -> auditable revision and AI provenance preserved.

### Quality observation
Quality supervisor receives scheduled random sample with valid authority/consent -> reviews teacher note, attendance, approved snippet if lawful -> rubric: accuracy, pacing, learner engagement, adherence to plan -> coaching task issued -> follow-up sample -> escalation only if validated concern. AI flag is a hint only.

### Safeguarding case
Learner report or verified red flag -> privacy-restricted case -> triage urgency -> temporary safety measures according to policy -> authorized investigator collects minimum evidence -> human finding + action -> appeal/review and retention clock; serious concerns escalated to relevant authorities according to law. No AI-only sanctions or secret monitoring.

### Competition approval
Organizer drafts competition and scoring rubric -> academic supervisor approves content -> safeguards/eligibility and minors' visibility reviewed -> assigned judge scores blinded entry -> second judge or supervisor resolves discrepancy -> publication approver signs -> affected learner receives score and appeal window -> independent appeal handling.

### Payroll approval
Compensation manager drafts contract rule -> finance approval -> immutable version -> attendance reconciliation -> payroll simulation -> finance reviewer (not creator) approves payrun -> payment execution controlled -> teacher statement & dispute. Academic/quality supervisor cannot silently alter teaching hours.

### Market/provider rollout approval
Regional manager proposes market/provider -> compliance checks geography and data transfer, finance checks PSP/currency, technology verifies video capability -> second approver activates at future effective timestamp -> affected bookings preview, audit, rollback.

## UX modules in supervisor portal
- Supervisor Overview: queues, SLA, cohorts, program performance, exceptions, role-scoped analytics.
- Academic: placement approvals, plans, exams, question banks, teacher mentoring, content licensing.
- Operations: weekly schedule, workload heatmap, absence cover, no-show disputes, substitute teacher allocation.
- Safeguarding: private incidents, role-limited evidence timeline, triage, audit and retention.
- Contest: builder, eligibility, rounds, score review, appeals, awards and private minors leaderboard.
- Finance: price books, payroll simulation, invoices, refunds, reconciliation, two-person approvals.
- Settings: markets, locales, prices, timezone/default, provider routing, IAM policy, notifications, AI/privacy policies.

## Segregation-of-duties / red-team tests
1. A support agent cannot view full recordings via API even if sidebar hidden.
2. A finance initiator cannot approve own payroll/payment.
3. An admin cannot route a case outside assigned region without explicit grant.
4. A judge cannot score own student/family submission or publish final results.
5. A quality supervisor denied transcript cannot use an AI summary to infer protected content.
6. A supervisor with expired delegation immediately loses access in UI and API.
7. Break-glass alert routed to another authority, immutable reason and access logs.
8. API authorization re-evaluated after role changes for long-running jobs.
