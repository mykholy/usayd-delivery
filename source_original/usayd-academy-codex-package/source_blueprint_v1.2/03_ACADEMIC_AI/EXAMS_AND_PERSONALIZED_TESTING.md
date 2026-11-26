# Smart Exams & Personalized Testing — implementation-level specification

## Goal
Convert verified progress into actionable feedback and learning plans; quizzes do not substitute teacher's qualified judgment of recitation. Tests must strengthen weak passages without creating punishment/shame.

## Exam types

| Type | Item source | Evaluation method | Allowed automation |
|---|---|---|---|
| Baseline assessment | Approved rubric | Qualified teacher oral test | Schedule and report prep |
| Spaced revision oral | Due passage queue | Teacher and/or approved specialist pilot | Suggest segments; not final judge |
| Written concepts | Reviewed item bank | Deterministic correct answer | Auto grade with item version |
| Memorization continuation | Verified passage ranges | Teacher oral exam | Flag possible omission only after evaluation |
| Tajweed identification quiz | Reviewed rules/examples | Deterministic selection | Grade closed-ended, not phonetics |
| Long-term checkpoint | Same comparable rubric | Human teacher/supervisor | Analyze improvement after approval |
| Competition qualifying | Locked academic bank | Approved fair rules | Anti-abuse flags/human final |

## Adaptive item selection policy

Inputs only: learner program level, teacher-approved weak skills and passage ranges, recent approved rubric, missed revisions, valid prior responses, declared accommodations. Build selection against a human-reviewed bank. New questions suggested by AI enter `DRAFT` and cannot be served before academic approval. Mix: 50% verified weak areas, 30% due review, 20% calibrated level benchmark initially **hypothesis**, configurable by academic authority. Each selected item logs `selection_policy_version`, `input_evidence_ids` and exposure count to defend bias. Do not increase difficulty when a learner fails due to accessibility/network problems.

## Attempt lifecycle

`eligible → reserved → in_progress → submitted → auto_marked (closed-ended only) / teacher_review → approved → published → appeal (optional) → corrected`. Server clock authoritative; device offline may save draft but not count final submit until server receipt. One attempt ID/idempotency token; enforced max attempts, fair retry after technical outage; never erase old result on retake.

## Scoring and feedback

Written concept questions may auto-score if answer key version approved. Oral recitation is a rubric: text correctness, approved tajweed competencies, retention, self-correction; scoring differences by program/level. Avoid invented numeric AI confidence. Feedback has three sections: `you did well`, `needs revision`, `next study task` referencing legitimate verified evidence and Quran passage ids.

## Sample adaptive scenario

- Adult learner assessed `reading=3/4`, `retention=1/4`, teacher confirms weakness on 3 specific passage ranges.
- Next test prioritizes those three ranges, includes one calibrated control and optional explanation to learner.
- Learner performs 2/4 on one range; system *suggests* an additional review and postpones new memorization on next plan version.
- Teacher approves. Student receives updated 15-minute daily task in dashboard; `plan_version` increments with reason.
- Reassessment one week later compares same rubric and passage difficulty; analytics avoids claiming a causal effect from app opens alone.

## Student views

List, filters, due date, duration, difficulty indication, pre-exam instructions, attempt in progress, interruption recovery, answer review subject to anti-cheat policy, teacher feedback, retest booking, appeal and learning update.

## Teacher views

Assigned exams, qualified rubric, active oral assessments, comment-by-criterion, review AI suggestions as untrusted, publish only after evidence check, answer item bank quality issues.

## Admin views

Exam builder, question versioning, approved-only publishing, test assignment rules, accessibility accommodations, score corrections, audit, item analysis (difficulty/drop rate) and AI costs.

## Safety and fairness acceptance

No child personal data in public results; no final religious correctness judgement from unvalidated models. For identical age/level/riwaya/rubric, scores comparable; cross-rubric score not directly ranked. Allow retest after technical failure without arbitrary penalty. Exam errors have human correction and privacy-safe incident log.
