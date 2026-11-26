# API Contract v1.2 — added operations

Status: **design-only, not deployed**. All paths under `/api/v1`, typed response models and explicit permission notes. Mutating money/security actions require idempotency keys; role and object ownership enforced on server.

| Method | Path | Operation ID |
|---|---|---|
| GET | `/api/v1/public/markets` | `get__api_v1_public_markets` |
| GET | `/api/v1/public/pricing` | `get__api_v1_public_pricing` |
| GET | `/api/v1/public/timezones` | `get__api_v1_public_timezones` |
| GET | `/api/v1/me/preferences` | `get__api_v1_me_preferences` |
| PATCH | `/api/v1/me/preferences` | `patch__api_v1_me_preferences` |
| POST | `/api/v1/me/checkout-quotes` | `post__api_v1_me_checkout_quotes` |
| POST | `/api/v1/me/payment-checkouts` | `post__api_v1_me_payment_checkouts` |
| GET | `/api/v1/teacher/me/availability-rules` | `get__api_v1_teacher_me_availability_rules` |
| PUT | `/api/v1/teacher/me/availability-rules` | `put__api_v1_teacher_me_availability_rules` |
| GET | `/api/v1/booking/available-slots` | `get__api_v1_booking_available_slots` |
| POST | `/api/v1/lessons/{lessonId}/reschedule-request` | `post__api_v1_lessons_lessonId_reschedule_request` |
| GET | `/api/v1/admin/markets` | `get__api_v1_admin_markets` |
| POST | `/api/v1/admin/markets` | `post__api_v1_admin_markets` |
| POST | `/api/v1/admin/markets/{marketId}/decision` | `post__api_v1_admin_markets_marketId_decision` |
| GET | `/api/v1/admin/price-books` | `get__api_v1_admin_price_books` |
| POST | `/api/v1/admin/price-books` | `post__api_v1_admin_price_books` |
| POST | `/api/v1/admin/price-books/{priceBookId}/decision` | `post__api_v1_admin_price_books_priceBookId_decision` |
| GET | `/api/v1/admin/video-providers` | `get__api_v1_admin_video_providers` |
| POST | `/api/v1/admin/video-providers` | `post__api_v1_admin_video_providers` |
| POST | `/api/v1/admin/video-providers/{providerAccountId}/connection-test` | `post__api_v1_admin_video_providers_providerAccountId_connection_test` |
| GET | `/api/v1/admin/video-providers/{providerAccountId}/capabilities` | `get__api_v1_admin_video_providers_providerAccountId_capabilities` |
| GET | `/api/v1/admin/video-routing-policies` | `get__api_v1_admin_video_routing_policies` |
| POST | `/api/v1/admin/video-routing-policies` | `post__api_v1_admin_video_routing_policies` |
| POST | `/api/v1/admin/video-routing-policies/{policyId}/dry-run` | `post__api_v1_admin_video_routing_policies_policyId_dry_run` |
| POST | `/api/v1/admin/video-routing-policies/{policyId}/decision` | `post__api_v1_admin_video_routing_policies_policyId_decision` |
| POST | `/api/v1/admin/video-routing-policies/{policyId}/activate` | `post__api_v1_admin_video_routing_policies_policyId_activate` |
| POST | `/api/v1/admin/video-routing-policies/{policyId}/rollback` | `post__api_v1_admin_video_routing_policies_policyId_rollback` |
| GET | `/api/v1/admin/video-incidents` | `get__api_v1_admin_video_incidents` |
| POST | `/api/v1/admin/video-incidents/{incidentId}/recover` | `post__api_v1_admin_video_incidents_incidentId_recover` |
| GET | `/api/v1/admin/supervisor-assignments` | `get__api_v1_admin_supervisor_assignments` |
| POST | `/api/v1/admin/supervisor-assignments` | `post__api_v1_admin_supervisor_assignments` |
| POST | `/api/v1/admin/supervisor-assignments/{assignmentId}/revoke` | `post__api_v1_admin_supervisor_assignments_assignmentId_revoke` |
| GET | `/api/v1/supervisor/queues` | `get__api_v1_supervisor_queues` |
| POST | `/api/v1/supervisor/academic-plans/{planId}/decision` | `post__api_v1_supervisor_academic_plans_planId_decision` |
| GET | `/api/v1/supervisor/safeguarding-cases` | `get__api_v1_supervisor_safeguarding_cases` |
| POST | `/api/v1/supervisor/safeguarding-cases` | `post__api_v1_supervisor_safeguarding_cases` |
| GET | `/api/v1/admin/settings/versions` | `get__api_v1_admin_settings_versions` |
| POST | `/api/v1/admin/settings/drafts` | `post__api_v1_admin_settings_drafts` |
| POST | `/api/v1/admin/settings/versions/{settingsVersionId}/decision` | `post__api_v1_admin_settings_versions_settingsVersionId_decision` |
| GET | `/api/v1/admin/translations` | `get__api_v1_admin_translations` |
| PATCH | `/api/v1/admin/translations/{translationId}` | `patch__api_v1_admin_translations_translationId` |
| POST | `/api/v1/admin/translations/{translationId}/publish` | `post__api_v1_admin_translations_translationId_publish` |
| GET | `/api/v1/admin/payment-merchant-profiles` | List verified PSP merchant profiles |
| POST | `/api/v1/admin/payment-merchant-profiles` | Draft merchant profile referencing secret vault only |
| GET | `/api/v1/admin/finance/fx-rates` | Get versioned FX reporting provenance |
| GET | `/api/v1/admin/operations/teacher-schedules` | Region-scoped teacher UTC schedule and availability |
| GET | `/api/v1/admin/security/access-audits` | Read privacy-redacted privileged access trail |
| GET | `/api/v1/supervisor/quality-observations` | List assigned quality observations with valid purpose |
| GET | `/api/v1/supervisor/competition-appeals` | List contest appeals restricted by assigned judge |
| GET | `/api/v1/admin/video-provider-health` | Get scoped verified video provider health |
| GET | `/api/v1/admin/legal-market-readiness` | Get preflight market licensing and PSP approval gates |
