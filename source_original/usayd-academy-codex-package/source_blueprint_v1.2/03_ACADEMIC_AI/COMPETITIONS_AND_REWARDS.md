# Competition, Challenge, Exam, Rewards & Gamification — dedicated SRS
**Doc ID:** COMP-SRS-001 | **Owners:** Product + Academic Supervisor + Legal/Safeguarding + QA | **Launch:** R3/P1

## 1. Product intent and constraints

Use competitions to increase voluntary participation and evidence-backed review, *not* to create compulsive usage or an opaque ranking of religious merit. A contestant should receive useful feedback even when not winning. Adult and minor competitions are segregated or carefully designed by pedagogical level, with minors' public profile exposure disabled by default. Competition success does not equal scholarly authorization/ijazah.

## 2. Competition taxonomy

| Type | Entry requirement | Mechanism | Assessment | Reward |
|---|---|---|---|---|
| Weekly Revision Challenge | Level and recently learned segments | Complete 3 assigned revisions and oral check | Teacher-approved retention rubric | Study badge |
| Monthly Memorization Cup | Specific approved curriculum | Supervised recitation of assigned range | Human judges + double review finalists | Certificate + authorized prize |
| Tajweed Skills League | Matched levels | Approved quiz + oral correction | Rubric by qualified tutor | Personal skill report |
| Comeback Challenge | Inactive learner returning | Complete tailored recovery tasks | Improvement vs own approved baseline | Private achievement |
| Team Revision Week | Opt-in compatible level | Group tasks, no open public chat for minors | Team normalized per eligible participant | Group badge |
| Seasonal Program (e.g. Ramadan) | Curriculum-specific | Fixed 2–4-week program | Balanced education over volume | Non-pay-to-win recognition |

## 3. Contest configuration editor

Metadata: `title_ar/en`, category, description, legal jurisdiction, organizer, teacher/judges, eligibility rule version, age band, level band, allowed countries, approved program/riwaya, registration start/end, start/end, round schedule, entry cap, seats, timezone, privacy mode, fee=0 by default, prize list, judging rubric version, scoring rules, tie rules, appeal window, terms version, sponsorship/consent.

### Lifecycle

```
DRAFT → ACADEMIC_REVIEW → LEGAL_REVIEW → SCHEDULED → REGISTRATION_OPEN
  → REGISTRATION_CLOSED → RUNNING → SCORING → PROVISIONAL_RESULTS
  → APPEAL_WINDOW → FINALIZED → PRIZES_ISSUED → ARCHIVED
```

Cancel/void transitions require reason and notices. Publishing requires both academic and legal sign-offs if material prizes are involved. Changing scoring rubric after registration requires notice/permission or cancellation—not silent retroactive edits.

## 4. Eligible registration contract

- Verified learner identity; active status; minimum valid consents; level assessment and supported age group; approved country/riwaya.
- Each learner gets **at most one canonical registration** per contest, with optional retries per defined test policy.
- Deny when already registered, out of eligibility, contest full, too late, banned for manually confirmed serious abuse or no required consent.
- Contest may permit free learners explicitly; no buying additional chances, paid advantage or lottery mechanisms.
- All rejections show a transparent reason and support path.

## 5. Round execution and rubric

`ContestRound`: quiz, timed approved task, oral recitation, replayable memory task, live judge event or cumulative teacher-assessed revision. Each has published start/end, attempts, accessibility accommodations, max time, source and locked items. Quiz questions need subject-matter QA. Oral contest needs identity/age authorization and recorded participant consent if recording is necessary; alternative live assessment where possible.

**Example rubric (illustrative only; subject to academic signoff)**

| Criterion | Weight | Evidence | Scoring guard |
|---|---:|---|---|
| Memorization correctness | 50% | Human verified oral assessment | Do not let AI independently assign final score |
| Recall stability / revision | 25% | Approved repeat test across dates | Do not overreward longer submissions |
| Target tajweed competencies | 15% | Qualified judge rubric | Program/level/riwaya adjusted |
| Completion of required learning tasks | 10% | Auditable accepted tasks | No points for mere screen time |

For beginner programs weights and skills **must differ**; never compare an absolute score from different rubrics as if equal. **No global ranking across fundamentally incomparable levels**. Display level-specific ranking and improvement-based private feedback.

### Tie breaker example
1. Correctness score before secondary engagement; 2. approved revision score; 3. joint ranking or second human judged tie-break. Never use enrollment time, fee paid, device speed or private personal characteristics to determine winner.

## 6. Judges and review

- Admin nominates academic judges with qualifications and conflict of interest disclosure.
- Two reviewers for prize-relevant finals and suspected manipulation; judges cannot evaluate their own private student for high-value prize without independent reviewer.
- Blind score where practical; no child face/real name exposure to nonessential users.
- Maintain `score_version`, `rubric_version`, per-criterion notes, judge ID and signed decision.
- AI suggestions to judge must be visibly marked 'مساعدة آلية غير معتمدة' and never saved as final without human approval.

## 7. Leaderboard/privacy

- Default scoreboard: learner sees personal result and percentile band only if enough cohort size. Public adult leaderboard requires explicit opt-in. For minors use private view or pseudonyms with valid guardian authorization and minimum cohort size to prevent re-identification.
- No teacher/student contact fields, exact birth dates, device IDs or home city published.
- No shame badges, public failure labels, penalty for breaks, addictive push patterns or monetized streak restoration.
- Standings from **final approved scores**; provisional scores labeled and not treated as final.

## 8. Rewards ledger and certificates

Badge `awarded` only after final approved result; revisions have revocation entries not destructive overwrite. Issued certificate has verifiable ID, course/competition name, criterion and issue date and explicitly states **academy-issued participation/achievement; not officially accredited** unless separately authorized. Monetary/value prizes require country-specific legal review, anti-fraud, fraud reporting, accounting and taxation.

## 9. Appeals and integrity

Appeal within configured window, reason and evidence; independent adjudicator; retain prior decision, corrected score and notification. Anti-cheat signals (rapid impossible attempts, duplicate accounts, changed answers) create case for *human* review. Don't claim cheating based solely on similarity score or AI.

## 10. App surfaces

**Learner:** Competition directory, contest detail, eligibility, enroll, preparation plan, round page, oral slot booking, submission confirmation, my standing, result breakdown, appeal form, achievements and certificates.

**Teacher/Judge:** assigned contests, rubric, blinded candidate queue, oral evaluation, save draft, submit, peer review, conflict declaration, appeals.

**Admin:** contest templates, creation wizard, scoring formula & tie policies, cohort segmentation, roster, judges, submissions, moderation, public/private standings, prizes, appeal queue, analytics/retention impact.

**Mobile:** deep link, countdown with server time, push opt-in, resume interrupted quiz, back from system call, offline handling (do not silently submit unreliable quiz), accessibility timing accommodations.

## 11. Acceptance criteria and adversarial tests

1. Underage learner without valid consent cannot join a restricted contest, even through direct API call.
2. Learners from different level bands cannot appear in the same ranked leaderboard unless an explicitly approved normalizing rubric exists.
3. A correct answer change after academic QA yields a new item version; affected existing results require reviewed regrading.
4. Duplicate submissions, clock skew, repeated webhooks or refresh do not grant extra attempts/awards.
5. Teacher cannot silently alter finalist score after publication; change goes through correction/appeal workflow.
6. Student who withdraws public leaderboard consent disappears from public rankings promptly while retained legal/accounting records are handled under policy.
7. Losing or missing a challenge does not block core lessons or create penalty points.
8. `P1` cannot launch unless legal and safeguarding review on prizes, minor visibility and data is signed.

## 12. Competition KPIs, without dark patterns

Educational: approved revision completion lift vs matched non-participants, change in rubric assessment after 4 weeks, satisfaction, appeal overturn rate, unfair disqualification rate, voluntary continuation. Commercial: first renewal delta, contest-related support cost. Monitor negative impact on student well-being; competitive engagement alone is not a learning outcome.
