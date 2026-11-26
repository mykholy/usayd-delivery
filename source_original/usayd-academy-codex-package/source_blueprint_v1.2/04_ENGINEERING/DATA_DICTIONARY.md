# Data model and dictionary — draft

**Data model is conceptual; implementation migration types, indexes and FKs require architecture approval.**

| Entity / Table | Critical columns | Invariant / privacy constraint |
|---|---|---|
| users | id, email, phone, password_hash, locale, country, timezone, status | unique verified contact; no shared user per learner |
| roles,permissions,user_roles | role,permission,user_id,assigned_by,expires_at | role-scoped; protected system roles |
| learners | id,user_id,age_band,program_goal,preferences_json,created_at | 1 learner primary account, no required guardian_id |
| learner_guardians | id,learner_id,guardian_contact,relation,verified_at | minimum data, verified relationship |
| consent_receipts | id,subject_id,guardian_id,purpose,version,state,timestamp,proof_hash | append-only; withdraw creates event |
| teacher_profiles | id,user_id,qualification_status,subjects,languages,bio | sensitive documents private |
| teacher_credentials | teacher_id,type,issuer,verified_by,expires_at | read academic/admin only |
| teacher_availability | teacher_id,rrule,timezone,start_at,end_at,exceptions | no overlap of active slots |
| teacher_contracts | id,teacher_id,model,effective_from,effective_to,pay_rules_json,currency | immutable revision snapshots |
| programs | id,slug,category,level,riwaya,lang,status | versioned, approved owners |
| curricula | id,program_id,version,approved_by,content_license | never retroactive edits |
| quran_references | id,source,edition,riwaya,surah,start_ayah,end_ayah | text by verified licensed source only |
| packages | id,market,currency,price,session_length,session_qty,validity | tax and policy version |
| subscriptions | id,learner_id,package_id,state,begins_at,ends_at | no active before paid webhook |
| credit_ledger | id,subscription_id,lesson_id,delta,reason,source_event | sum credits never below zero |
| payments | id,subscription_id,provider_ref,amount,currency,state,idempotency_key | webhook replay safe |
| payment_webhook_events | provider,event_id,body_hash,processed_at,status | unique provider event id |
| invoices | id,payment_id,total,taxes,number,issued_at | immutable issued version |
| lessons | id,learner_id,teacher_id,program_id,booking_status,start_at,end_at | UTC; uniqueness of live slot |
| lesson_participants | lesson_id,user_id,role,authorization_state | min participants; scoped |
| conference_sessions | id,lesson_id,provider,provider_session_id,capabilities_json,state | one active at time; provider refs private |
| conference_events | id,session_id,event_key,actor_id,kind,occurred_at,raw_checksum | dedup; private PII |
| attendance_summaries | lesson_id,actor_id,minutes,source,verified_at,status | reconciled with provider events |
| lesson_reports | id,lesson_id,author_id,status,objectives,notes,approved_at | approved factual report only |
| assessments | id,learner_id,program_id,rubric_version,grade,state,approved_by | history retained |
| assessment_evidence | id,assessment_id,question_id,segment_ref,result,evaluator_id | Quran-specific evidence |
| question_banks | id,program_id,item_version,verified_by,license,status | approved only served to learners |
| exam_attempts | id,exam_id,learner_id,attempt_no,score,state,grade_version | retry policy and idempotency |
| learning_plans | id,learner_id,program_id,active_version,goal,approved_by | one approved active plan per program |
| plan_versions | id,plan_id,revision,source_evidence_ids,status,approved_by | AI drafts not auto approved |
| study_tasks | id,plan_version_id,type,quran_ref_id,due_at,estimated_min,status | may reschedule gently |
| memorization_segments | id,learner_id,quran_ref_id,state,last_verified_at | do not infer mastery from app opens |
| revision_events | id,segment_id,result,evaluator_id,occurred_at,next_due_at | append-only review evidence |
| competitions | id,type,version,level,age_band,privacy,terms_version,status | verified academic and legal review |
| competition_rounds | id,competition_id,kind,start_at,end_at,attempt_policy | server time, versioned rules |
| competition_registrations | id,competition_id,learner_id,eligibility_snapshot,status | unique learner per competition |
| competition_submissions | id,round_id,registration_id,payload_ref,status,submitted_at | consent, checksum, audit |
| contest_judgments | id,submission_id,judge_id,rubric_version,scores,status,notes | independent for finalists |
| contest_score_versions | id,registration_id,version,total,approved_at,state | no destructive overwrite |
| contest_appeals | id,registration_id,score_version,reason,status,reviewer_id | independent appeal reviewer |
| awards | id,registration_id,type,award_ref,issued_at,revoked_at | private for minors unless authorized |
| ai_runs | id,kind,subject_id,model,prompt_version,consent_receipt,evidence_refs,cost,state | full audit, no unreviewed final |
| ai_recommendations | id,run_id,target_type,target_id,payload,approved_by,status | proposed only until approved |
| policy_flags | id,session_id,ai_run_id,policy_rule,evidence_ref,state,resolved_by | not proof of violation |
| teacher_accruals | id,teacher_id,lesson_id,contract_snapshot,amount,reason,state | versioned rule proof |
| teacher_payouts | id,teacher_id,period,amount,currency,state,approved_by | immutable paid payout |
| leads | id,source,utm,contact_hash,stage,consent,owner_id | dedupe, privacy boundaries |
| support_tickets | id,subject_id,priority,safety_level,assignee_id,state | redacted access; escalations |
| notifications | id,user_id,channel,template,consent_ref,sent_at,status | retry/dedupe and unsubscribe |
| audit_events | id,actor_id,subject_type,subject_id,action,reason,ts | append-only; sensitive logging |
| analytics_events | id,actor_hash,event_name,property_json,occurred_at | no raw PII or transcript text |
| outbox_messages | id,aggregate_type,aggregate_id,event_type,payload,status | transactional eventual effects |
| media_assets | id,owner_type,owner_id,license,storage_ref,retention_until,status | private signed access and deletion |

## Data storage / access classifications

- `PUBLIC`: approved published teacher bios, anonymous program descriptions and contest overview.
- `INTERNAL`: ops metrics, public-safe aggregated counts, compensation rules without personal identifiers.
- `CONFIDENTIAL`: adult learner records, academic feedback, payments and teacher documents.
- `RESTRICTED`: minor details, guardian consents, raw lesson audio, safety cases, sensitive support interactions.

Use field-level access control plus row-level ownership in application layer, optionally DB-level RLS if PostgreSQL. Access is role/purpose scoped. IDs UUID/ULID; store timestamps UTC with server-side timezone conversion; store currency in minor units with ISO currency. Text Quran content references source edition rather than model-generated content.

## Relations and integrity constraints

- `learner.user_id → users.id`, `learner_guardians.learner_id → learners.id` optional for adult.
- Lesson unique active teacher slot; one active provider conference per lesson. Booking and credit reservation are atomic.
- `competition_registrations(competition_id,learner_id)` unique.
- `exam_attempts(exam_id,learner_id,attempt_no)` unique; contest submissions have idempotency key.
- One active plan version per learner/program combination, preserving history.
- Staff permission changes and payroll grades are audited append-only.
- Add composite indexes: `(teacher_id,start_at,status)`, `(learner_id,due_at,status)`, `(program_id,level)`, `(competition_id,status)`, `(learner_id,state)`, `(teacher_id,period)`.
