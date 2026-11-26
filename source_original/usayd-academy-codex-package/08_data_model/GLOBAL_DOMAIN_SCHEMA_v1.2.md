# Database extension / ERD guidance (for migrations, no production data assumed)

## Entities and important columns
- `market_regions(id,code,name,status,approval_state,effective_at,legal_entity_id,created_by,approved_by)`
- `country_profiles(id,iso2,locale_defaults_json,timezone_suggestions_json,market_region_id,availability)`
- `user_preferences(user_id,locale,timezone_id,selected_country,notification_timezone,source,updated_at)`
- `billing_profiles(id,user_id,billing_country,legal_name,psp_profile_id,consent_version,verified_at)`
- `price_books(id,market_id,status,version,effective_from,effective_to,currency_code,approved_by)`
- `price_items(id,price_book_id,program_id,package_id,amount_minor,currency_code,tax_policy_id,billing_cycle)`
- `checkout_quotes(id,user_id,price_book_version,amount_minor,tax_minor,total_minor,currency_code,merchant_id,expires_at,status,idem_key)`
- `payment_transactions(id,quote_id,provider,provider_account_id,provider_txn_id,amount_minor,currency_code,state,posted_at)`
- `exchange_rates(id,base_code,quote_code,rate_decimal,source,observed_at,expires_at,rate_version)`
- `teacher_availability_rules(id,teacher_id,timezone_id,rrule_text,valid_from_local,valid_to_local)`
- `teacher_timeoff(id,teacher_id,starts_at_utc,ends_at_utc,reason)`
- `lesson_slots(id,teacher_id,starts_at_utc,ends_at_utc,status,hold_expires_at,booked_timezone_snapshot)`
- `reminder_jobs(id,lesson_id,recipient_id,trigger_utc,delivery_locale,recipient_timezone,unique_key,status)`
- `video_provider_accounts(id,key,environment,region_eligibility,secret_ref,limits,status)`
- `video_provider_capabilities(id,account_id,feature,client,region,verification_state,evidence_ref,checked_at)`
- `video_routing_policy_versions(id,scope,priority_json,required_caps_json,status,effective_at,approver_1,approver_2)`
- `lesson_video_bindings(id,lesson_id,provider_account_id,policy_version,remote_room_ref,state,created_at,superseded_by_id)`
- `supervisor_assignments(id,actor_user_id,role,scope_type,scope_id,effective_from,effective_to,approved_by)`
- `supervision_cases(id,case_type,learner_id,lesson_id,status,priority,scope_region,privacy_classification,assigned_to)`
- `supervision_actions(id,case_id,actor_id,purpose,action,redacted_evidence_ref,created_at)`
- `settings_versions(id,namespace,scope,settings_json,schema_version,status,effective_at,checksum,proposed_by,approved_by)`
- `translation_entries(id,locale,namespace,key,value,version,status,reviewed_by)`
- `audit_events(id,trace_id,actor_id,subject_type,subject_id,action,old_hash,new_hash,purpose,ip_hash,created_at)`

## DB constraints + indexes
- Composite uniqueness `(market_id,package_id,billing_cycle,currency_code,price_version)`; exclusion of overlapping effective date ranges validated within serializable transaction.
- `(provider,provider_event_id)` unique webhook dedup; `(merchant_id,idem_key)` uniqueness for payment intent; immutable posted ledger.
- Lesson slots overlap exclusion is not native in MySQL: acquire per-teacher lock/slot-lock table within transaction; assert no overlap before insert; index `(teacher_id, starts_at_utc, ends_at_utc, status)`.
- At most one active video binding/lesson enforced with transaction + computed single active flag and unique key (or equivalent).
- Case evidence encryption and row-level/ABAC enforcement in app; restrict direct DB access and exports.
- Full audit history retained under approved retention, with chain/integrity checks for high-impact admin actions.
- Price snapshot contains semantic details and version; never re-price already paid invoice from current price book.

## Migration/seed strategy
Migrations backwards compatible; seed only ISO currencies/zones/placeholder market records, no active markets or synthetic "real" teacher or customer claims. No provider secret in seed. Default all new markets `disabled`; require explicit approval and sandbox PSP verification. Use feature flags for progressive rollout.
