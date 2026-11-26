# AI experiments and release gate protocol

**Scopes:** (A) learning-plan drafting; (B) transcript summaries; (C) policy risk flagging; (D) Quran recitation error suggestions — separate model cards and gates.

## Evaluation datasets
- Legally collected, representative Arabic dialects, different devices, noise, ages where permitted, Quran recitation modes/riwayat, speech overlaps, common educator phrases and non-violations. Never reuse real minors' recordings to build test sets without specific lawful basis.
- Every sample: consent/license source, language/riwaya, class type, human-verified label, reviewer, confidence in **annotation only**, retention/delete date. Use synthetic or adult volunteer fixtures until approved.
- Hold out independent blind test set; no data leakage from prompt examples, teacher-specific memorization or eval prompts. Audit subgroup error rates; avoid grading learners by accent.

## Must-measure quality
| Feature | Metric | Launch gate |
|---|---|---|
| Plan assistant | teacher-rated safety/correctness, unsupported assertions, edit time, citation validity | academic lead approval; no plan auto publish |
| Lesson summaries | factual precision, omissions, unauthorized PII capture, Arabic readability | teacher approval of every learner-facing summary in pilot |
| Policy flags | precision/recall for attempts to solicit outside contacts, severity-aware FN/FP, appeals overturned | **no automatic discipline**; thresholds set by safety lead after evaluation |
| Quran ASR | word-error and verse-alignment rate by riwaya/device; error suggestion PPV; harm review | research-only until separate Quran specialists sign off |
| AI cost | per analyzed minute/learner, token and media storage cost, job latency | budget caps + kill switch tested |

## Model governance
- `ai_runs` stores model/provider/version, system prompt SHA, evidence identifiers, actor purpose, consent receipt/version, cost units, status; never reveal raw secrets or private transcripts in logs.
- `ai_suggestions` structured JSON, `draft`→`teacher_review`→`approved/rejected`; no automatic canonical Quran quote or grade.
- `policy_flags` `new`→`triage`→`confirmed/false_positive`→`actioned/closed`; urgent safeguarding pathways are human-operated and incident-based.
- Per purpose opt-in/withdrawal, fresh consent check **at processing time**, region/storage/vendor transfer assessment, retention expiry, deletion workflow.
- A/B test AI vs non-AI on verified learning outcomes, satisfaction and teacher workload; retention alone cannot imply education improvement.

## Red-team and injection
Teacher/student speech, lesson documents, uploaded content and chat text are **untrusted data**, not instructions for the AI agent. Prompt injection must not grant records, bypass permissions, auto-approve plans or request payment. Strip irrelevant PII and require strict schema validation.

## Failure fallback
AI unreachable → core lessons, exams, revision and teacher manual report stay functional. Disable optional AI without blocking payment or attendance. Expose user-friendly `AI_UNAVAILABLE`, avoid phantom tasks or silent incorrect scores.
