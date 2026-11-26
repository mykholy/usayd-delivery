# Critical UX interaction contracts — must be demonstrated in editable Figma

Each flow specifies `role`, `screen IDs`, `entry`, `success`, `error states`, `analytics`, `API`, `accessibility`, `mobile`. Build **actual clickable transitions**, not just static page variations.

## F01: unified enrollment + age/guardian
- Entry `UX-AUTH-001`: adult or minor identifies as learner. Age determines policy gate only, not account type. Verification link/OTP, password requirements, language/timezone, consent checkboxes distinct by purpose.
- Minor `UX-AUTH-002`: capture guardian contact and verified receipt; pending screen cannot book/pay/join until rule allows; retry/resend limits, expired code, guardian declines, revoked consent, correction if mistaken age.
- Success → learner onboarding; error 422 localized, 429 cooldown; no disclosure whether email/phone registered.

## F02: level assessment → personalized plan
- Student submits goal/riwaya/availability and books assessment. Teacher dashboard gets review rubric. After evaluation shows separate `teacher-approved level`, `AI draft plan` and `pending academic approval`.
- Teacher edits/rejects; state history and reason; approved only visible as official plan. Empty/no teacher matched, late assessment, teacher unavailable and AI offline states.

## F03: purchase → booking → live classroom
- Pricing shows country/currency and duration/refund rule version. Checkout can be pending/rejected; do not show credits until verified webhook.
- Availability shows local time + timezone; conflict, insufficient credits, teacher leave, waitlist, reschedule, makeup and DST edge cases.
- Join screen preflight mic/camera; provider card `embedded/external`, limitations and safe recording indicator; consent required alternative. Disconnection, room closed, and fallback with fresh link are first-class states.
- Lesson report drafted/approved; attendance disagreement shows support dispute and credit pending.

## F04: self-study, Memory Map and adaptive revision
- Quran reader uses verified corpus only; separate status `self-reported/practiced/teacher-verified/needs-review` and provenance.
- Today panel chooses a realistic set of revisions; the learner can pause/reschedule, skip with reason and resume without guilt. AI recommendation marked draft and has 'why' and 'review with teacher'.
- Mobile offline draft persists securely and sync conflict resolved explicitly, never silently overwriting approved plan.

## F05: exam with interruption and accessibility
- Server countdown visible with 1-minute warning; save answer states `draft/syncing/saved/failed`; reconnect and replay safe; allow approved accommodations and appeals.
- Submit asks confirmation; one submission; result provisional until human review for oral/tajweed; show feedback without leaking future question-bank answers.

## F06: competition lifecycle
- List eligible/ineligible with understandable reasons; register once; round status and due schedule; judge-only evidence; `provisional` vs `final` status explicit.
- Private leaderboard for minors; public opt-in for adults; pseudonyms default. Appeal form includes deadline and receipt; corrected score version not overwritten; awards issued only once post-final.
- Safe rewards: no paid boosts, no rankings across incompatible levels, no manipulative streak punishments.

## F07: teacher and admin
- Teacher: availability editing with collisions/timezones, lesson preparation, learner progress, report, payroll preview and dispute. Admin: permissions, provider selection, incident triage, AI policy review, subscriptions/refunds, score/judge controls and audit history.
- Financial actions have explicit irreversible confirmation + 2-person approval when relevant; never show private audio to unauthorized staff.

## Cross-cutting Figma acceptance
- Layouts 360/390/768/1440, Arabic RTL and English LTR, WCAG 2.2 AA focus/keyboard, 44px touch targets, loading/empty/error/offline/permission/consent states, native Flutter navigation patterns.
- Every submit button state mapped to API error codes in `04_ENGINEERING/API_ERROR_MATRIX_v1.1.md`; all frames have UX ID/requirement ID tags.
