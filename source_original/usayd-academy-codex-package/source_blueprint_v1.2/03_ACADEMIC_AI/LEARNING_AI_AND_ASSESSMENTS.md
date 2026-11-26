# Adaptive Learning, AI tutor and Assessment — technical/academic design
**Owners:** Academic lead + AI lead + Product | **Prerequisite:** authorized Quran corpus and rubric sign-off

## 1. Learning framework

Programs: reading foundations, correcting recitation, tajweed, new memorization, strengthening past memorization, revision/review cycle. Each program references an approved edition/riwaya, versioned syllabus, skill taxonomy, learner objectives, max weekly workload and a qualified academic owner.

## 2. Initial assessment (human-led)

Input: goal, age group only for pedagogy/safeguarding, current recitation fluency, existing memorization, available hours, preferred time zone, declared health/access needs only if optional and needed. Output: rubric ratings by dimension, notes, evidence id, proposed level, tutor confidence expressed as rubric evidence (not made-up AI probabilities).

Rubric example (each 0–4; trained assessor required): recognition/reading accuracy, articulation accuracy, known tajweed applications, memorization recall, retention after delay, ability to self-correct, study consistency. Not all dimensions apply to all programs. Provide user-readable description for every rating.

## 3. Learning plan source-of-truth

```
Assessment (human approved) + Goals + Weekly availability
     ↓
Deterministic Eligibility and Workload Constraints
     ↓
Rule-based first plan OR AI recommendation with evidence_refs
     ↓
Teacher review: change/edit/approve/reject
     ↓
PlanVersion ACTIVE + daily tasks + revision due queue
     ↓
Evidence: teacher rubric / supervised test / learner practice
     ↓
Weekly review: plan changes as proposed DRAFT only
```

### Daily study task types

`new_hifz`, `revision`, `listen`, `reading_practice`, `oral_teacher_test`, `short_quiz`, `self_reflection`. Task has estimated time, min/max, lesson/ayah range, due date, completion mode, reviewer and optional reminder. User can reschedule without punishment.

## 4. Adaptive revision — safe baseline

Start with transparent rule-based schedule, not black-box AI: after approved oral test or teacher rubric, schedule first review after 1 day (weak), 3 days (moderate), or 7 days (solid); then adjust by *actual next evidence*, not calendar alone. All these intervals are **initial product hypotheses**, not a religious/educational standard. Teacher may override with reason. Avoid collapsing all verses of a whole surah to a single mastery claim.

Pseudo-logic:

```
for segment in approved_segments:
  strength = rubric.latest(segment)
  missed = overdue_revision_count(segment)
  interval = teacher_override or rules(level, strength, missed, last_review_result)
  revision_due_at = last_reviewed_at + interval
  emit Recommendation(evidence_id, reason, interval, version)
```

## 5. Assessment/question bank

- Human-reviewed source-backed questions; version each item and prevent learner-facing draft questions.
- Types: Quran continuation prompt at approved verse boundary (oral); correct reading practice; memory recall; compare similar passages (mutashabihat) by authorized text; review recitation and comprehension only with qualified authors.
- Exams: diagnostic, weekly formative, milestone, comprehensive, contest oral/written.
- Attempt policy configurable: timer only when pedagogically useful, no disability discrimination, fair retakes, instructor visibility.
- Score record = `rubric_version + evaluator_user + evidence + answers + feedback + decision`; item exposure limits and question randomization from authorized sets.
- Publish/explain result with strengths and next steps; appeal has reversible versioned correction.

## 6. AI service architecture and agent contracts

Separate tasks with separate models/data policies:

- `PlanSuggestionAgent`: input teacher-approved assessment, previous plan, schedule; JSON `weekly_goals`, `segments`, `workload_minutes`, `evidence_ids`, `risks`; result status DRAFT.
- `RevisionSuggestionAgent`: due queue, weak passages, recent approved tests; JSON `suggested_revision_ids`, `rationale`, `requires_teacher_review`.
- `LessonSummaryAgent`: lesson form fields; optional consented transcript. Never invent a taught verse or error.
- `StudyAssistant`: authorized learner facts only; retrieval from whitelisted program and plan; clear uncertainty; no personal religious rulings.
- `SessionPolicyAgent`: consented transcript excerpts, speaker attribution, policy clauses and context window; risk flag for human queue, not verdict.
- `RecitationResearchAgent`: isolated pilot with specialist ASR/forced-alignment Quran-specific corpus, precision/recall/false accusations evaluated, cannot publish authoritative judgments without approval.

## 7. Dataset segregation and consent

Video/audio content NEVER used to train third-party models by default. Pseudonymized identifiers, data minimization, redaction where accuracy allows, purpose codes, provider DPAs, data residency/export legal review, prompt injection defense, encryption and deletion audit. For minors provide equivalent learning path when optional analytics consent is absent.

## 8. AI evaluation protocol

| Dimension | Test | Gate |
|---|---|---|
| Quran text integrity | Compare every quoted ayah against source edition and licensed text | Zero unverified canonical text surfaced |
| Recommendation grounding | Each plan target supported by approved assessment or declared goal | 100% traceable evidence IDs in staging |
| Wrong correction detection | Human reviewers score ASR errors by age/accent/noise/riwaya | No production release before threshold approved |
| Session flag precision | Double-reviewed simulated policy cases, negative context cases | False-positive rate reviewed; no automatic discipline |
| Cost/latency | Track per task per minute/token and worst-case concurrency | Feature flag spends within budget |
| Privacy | No optional audio processing without consent; deletion tests | Hard blocking tests must pass |

## 9. Suggested prompt contract (nonproduction template)

> You are a **plan suggestion assistant**, not a Quran jurist. Use only the assessment, program and verified ayah reference IDs provided. Do not produce Quran verse text. Return strictly JSON matching the schema. Every educational recommendation must cite evidence IDs. If evidence is insufficient, set `needs_human_input=true`. Never finalize scores or plans.

## 10. Teacher copilot integration

Teacher receives pre-lesson briefing (approved plan, due reviews, previous lesson report). Teacher can edit, reject and approve every AI item. Unapproved suggestions never appear as a verified achievement to the learner. Keep source of error classifications recorded to avoid model hallucinations becoming cumulative 'facts'.
