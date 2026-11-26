# Screen-by-screen UI implementation specification

**Scope:** 119 screens; all variants must be represented in Figma and tested (loading, empty, error, permission, no internet).

## Shared UX rules
- Arabic RTL default; English LTR switch, no flipping Quran verse direction.
- Each page has proper breadcrumb/header/main/primary action, focus order, escape action, help and clear data provenance.
- Public pages crawlable and fast, authenticated apps accessible keyboard and on touch.
- Primary CTA disabled with cause tooltip/text when prerequisites unmet; never permit unsafe action solely from hidden button.
- Every restricted learner page includes guardian consent/teacher role rules server-side, not only a UI gate.
- Tables have mobile card alternative; modal sheets on mobile, full page for multi-step and forms.

## UX-PUBLIC-001 — Marketing Home
- **Role / route / phase:** `PUBLIC` / `/` / `P0`
- **User goal:** بناء الثقة وإظهار البرامج والنتائج وآلية المتابعة.
- **Primary action:** احجز تقييم مستوى.
- **Content / anatomy:** Hero; teacher proof; feature journey; pricing; real FAQ; CTA.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-001`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-002 — Programs Directory
- **Role / route / phase:** `PUBLIC` / `/programs` / `P0`
- **User goal:** مقارنة برامج الحفظ/التجويد/المراجعة.
- **Primary action:** استكشف البرنامج.
- **Content / anatomy:** program cards; outcomes; level/age tags; tabs.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-002`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-003 — Program Detail
- **Role / route / phase:** `PUBLIC` / `/programs/:slug` / `P0`
- **User goal:** عرض مسار ومخرجات البرنامج.
- **Primary action:** ابدأ تقييم المستوى.
- **Content / anatomy:** curriculum roadmap; eligibility; teachers; price.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-003`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-004 — Pricing
- **Role / route / phase:** `PUBLIC` / `/pricing` / `P0`
- **User goal:** توضيح الباقات حسب البلد والعملات.
- **Primary action:** اختر باقة.
- **Content / anatomy:** country currency; package duration; refund policy.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-004`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-005 — Teacher Directory
- **Role / route / phase:** `PUBLIC` / `/teachers` / `P0`
- **User goal:** عرض المعلمين المؤهلين.
- **Primary action:** تعرف على المعلم.
- **Content / anatomy:** teacher cards; filters; verified qualifications.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-005`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-006 — Teacher Public Profile
- **Role / route / phase:** `PUBLIC` / `/teachers/:slug` / `P0`
- **User goal:** تعريف خبرة المعلم قبل الاشتراك.
- **Primary action:** احجز تجربة.
- **Content / anatomy:** bio; certificates verified; languages; schedule.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-006`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-007 — How It Works
- **Role / route / phase:** `PUBLIC` / `/how-it-works` / `P0`
- **User goal:** عرض رحلة التعلم بلا ادعاءات.
- **Primary action:** احجز تجربة.
- **Content / anatomy:** steps; learning map demo; FAQ.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-007`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-008 — Competition Landing
- **Role / route / phase:** `PUBLIC` / `/challenges` / `P0`
- **User goal:** شرح المسابقات العامة بدون بيانات حساسة.
- **Primary action:** اكتشف التحديات.
- **Content / anatomy:** contest marketing cards; eligibility copy; examples.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-008`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-009 — Free Assessment Booking
- **Role / route / phase:** `PUBLIC` / `/trial` / `P0`
- **User goal:** حجز تقييمي مباشر بحدود الاستغلال.
- **Primary action:** احجز الموعد.
- **Content / anatomy:** contact; timezone; available slots; consent.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-009`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-010 — About/Academic Standards
- **Role / route / phase:** `PUBLIC` / `/about` / `P0`
- **User goal:** عرض المعايير الأكاديمية والاعتمادات الحقيقية.
- **Primary action:** شوف البرامج.
- **Content / anatomy:** team; method; teacher checks.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-010`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-011 — FAQ & Support
- **Role / route / phase:** `PUBLIC` / `/help` / `P0`
- **User goal:** دعم العملاء والاسترداد والجدولة.
- **Primary action:** ابدأ محادثة الدعم.
- **Content / anatomy:** FAQ; policies; contact support.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-011`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-PUBLIC-012 — Legal & Consents
- **Role / route / phase:** `PUBLIC` / `/legal/:slug` / `P0`
- **User goal:** عرض الشروط والخصوصية بمستويات فهم.
- **Primary action:** اقرأ السياسة.
- **Content / anatomy:** policy archive; accessibility; language toggle.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-PUBLIC-012`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-AUTH-001 — Unified Signup
- **Role / route / phase:** `AUTH` / `/signup` / `P0`
- **User goal:** تسجيل جميع الأعمار كمتعلم.
- **Primary action:** إنشاء حساب.
- **Content / anatomy:** contact; name; age band; OTP; terms.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-AUTH-001`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-AUTH-002 — Guardian Consent Step
- **Role / route / phase:** `AUTH` / `/onboarding/guardian-consent` / `P0`
- **User goal:** استيفاء تحقق ولي الأمر للقاصر.
- **Primary action:** إرسال طلب الموافقة.
- **Content / anatomy:** guardian contact; proof; consent receipt; pending.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-AUTH-002`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-AUTH-003 — Login
- **Role / route / phase:** `AUTH` / `/login` / `P0`
- **User goal:** تسجيل الدخول سريع وآمن.
- **Primary action:** تسجيل الدخول.
- **Content / anatomy:** email/phone; password or code; recover.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-AUTH-003`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-AUTH-004 — Password Recovery
- **Role / route / phase:** `AUTH` / `/forgot-password` / `P0`
- **User goal:** استرداد الحساب دون تسريب وجوده.
- **Primary action:** استرداد.
- **Content / anatomy:** contact; OTP; neutral messages.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-AUTH-004`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-AUTH-005 — Welcome Onboarding
- **Role / route / phase:** `AUTH` / `/onboarding` / `P0`
- **User goal:** هدف ووقت ورواية ومستوى.
- **Primary action:** متابعة.
- **Content / anatomy:** goal; duration; timezone; preference.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-AUTH-005`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-001 — Learner Home
- **Role / route / phase:** `LEARNER` / `/app` / `P0`
- **User goal:** إنجاز اليوم والحصة القادمة والتقدم.
- **Primary action:** ابدأ مهمة اليوم.
- **Content / anatomy:** next lesson; daily card; due revision; alerts; contest.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-001`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-002 — My Learning Profile
- **Role / route / phase:** `LEARNER` / `/app/profile` / `P0`
- **User goal:** تعديل تفضيلات الدراسة.
- **Primary action:** حفظ التغييرات.
- **Content / anatomy:** goals; schedule; locale; accessibility; security.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-002`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-003 — Programs Discover
- **Role / route / phase:** `LEARNER` / `/app/programs` / `P0`
- **User goal:** إضافة مسار تعلم.
- **Primary action:** شوف البرنامج.
- **Content / anatomy:** tracks; level filter; teacher availability.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-003`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-004 — Initial Assessment
- **Role / route / phase:** `LEARNER` / `/app/assessment` / `P0`
- **User goal:** حجز/عرض تقييم أولي.
- **Primary action:** حجز تقييم.
- **Content / anatomy:** rubric; assessment history; feedback.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-004`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-005 — Teachers Discover
- **Role / route / phase:** `LEARNER` / `/app/teachers` / `P0`
- **User goal:** اختيار معلم مناسب.
- **Primary action:** اختيار موعد.
- **Content / anatomy:** verified filters; teacher card; availability.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-005`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-006 — Teacher Detail
- **Role / route / phase:** `LEARNER` / `/app/teachers/:id` / `P0`
- **User goal:** استعراض المؤهلات وأوقات المعلم.
- **Primary action:** احجز مع المعلم.
- **Content / anatomy:** bio; level; languages; slots.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-006`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-007 — Calendar
- **Role / route / phase:** `LEARNER` / `/app/calendar` / `P0`
- **User goal:** استعراض جدول الحصص بالتوقيت المحلي.
- **Primary action:** حجز أو تغيير.
- **Content / anatomy:** day/week; timezone label; upcoming.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-007`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-008 — Booking Wizard
- **Role / route / phase:** `LEARNER` / `/app/book` / `P0`
- **User goal:** اختيار البرنامج والمعلم والوقت والرصيد.
- **Primary action:** تأكيد الحجز.
- **Content / anatomy:** stepper; conflict validation; credit preview.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-008`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-009 — Lesson Detail
- **Role / route / phase:** `LEARNER` / `/app/lessons/:id` / `P0`
- **User goal:** عرض التفاصيل وخطة الدرس وتذكير.
- **Primary action:** دخول الحصة.
- **Content / anatomy:** teacher; join window; consent; provider mode.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-009`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-010 — Classroom
- **Role / route / phase:** `LEARNER` / `/app/lessons/:id/live` / `P0`
- **User goal:** تسميع ومصحف وواجب ووسائل اتصال.
- **Primary action:** إنهاء الحصة.
- **Content / anatomy:** video; Quran; teacher annotations; mic/video; reconnect.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-010`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** State model: prejoin/device-test → connecting → ready → muted/unmuted → reconnecting → ended/failed; external provider mode must show limitations and safe return action.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-011 — Post-Lesson Report
- **Role / route / phase:** `LEARNER` / `/app/lessons/:id/report` / `P0`
- **User goal:** عرض الحفظ والمراجعة والأخطاء.
- **Primary action:** راجع الواجب.
- **Content / anatomy:** coverage; revision; approved notes; rating.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-011`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-012 — Learning Plan
- **Role / route / phase:** `LEARNER` / `/app/plan` / `P0`
- **User goal:** متابعة خطة أسبوعية وشهرية.
- **Primary action:** ابدأ المهمة.
- **Content / anatomy:** timeline; teacher-approved versions; daily goals.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-012`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Label AI outputs as suggestion; show sources (approved teacher evidence), human approval status, safe fallback and cost/rate limits.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-013 — Daily Study
- **Role / route / phase:** `LEARNER` / `/app/study` / `P0`
- **User goal:** إنجاز ممارسة ذاتية.
- **Primary action:** إنهاء التدريب.
- **Content / anatomy:** Quran; steps; timer optional; self-report.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-013`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-014 — Revision Queue
- **Role / route / phase:** `LEARNER` / `/app/revision` / `P0`
- **User goal:** المراجعات المستحقة حسب الضعف.
- **Primary action:** راجع الآن.
- **Content / anatomy:** due groups; passage chips; estimated time.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-014`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-015 — Memory Map
- **Role / route / phase:** `LEARNER` / `/app/memory-map` / `P0`
- **User goal:** مخطط حفظ السور والآيات.
- **Primary action:** افتح المقطع.
- **Content / anatomy:** surah grid; segment status; evidence dates.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-015`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-016 — Practice Recording
- **Role / route / phase:** `LEARNER` / `/app/practice` / `P0`
- **User goal:** تسميع اختياري مع ضوابط.
- **Primary action:** إرسال للمعلم.
- **Content / anatomy:** mic; consent; duration; private replay.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-016`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-017 — Exam Catalog
- **Role / route / phase:** `LEARNER` / `/app/exams` / `P0`
- **User goal:** اختبارات متناسبة مع المستوى.
- **Primary action:** ابدأ اختبار.
- **Content / anatomy:** difficulty tags; eligible exams; previous attempts.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-017`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-018 — Exam Taking
- **Role / route / phase:** `LEARNER` / `/app/exams/:id/take` / `P0`
- **User goal:** تقديم اختبار بأسئلة معتمدة.
- **Primary action:** تسليم الاختبار.
- **Content / anatomy:** progress; question renderer; timer policy; draft save.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-018`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-019 — Exam Results
- **Role / route / phase:** `LEARNER` / `/app/exams/:id/result` / `P0`
- **User goal:** نقاط قوة وضعف وتوصيات مراجعة.
- **Primary action:** عرض الخطة الجديدة.
- **Content / anatomy:** rubric breakdown; review buttons; appeal.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-019`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-020 — Competitions Discover
- **Role / route / phase:** `LEARNER` / `/app/competitions` / `P0`
- **User goal:** اكتشاف مسابقات مناسبة.
- **Primary action:** عرض التفاصيل.
- **Content / anatomy:** level tabs; current/upcoming; private mode.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-020`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-021 — Competition Detail
- **Role / route / phase:** `LEARNER` / `/app/competitions/:id` / `P0`
- **User goal:** معرفة الأهلية والقواعد والجوائز.
- **Primary action:** اشترك.
- **Content / anatomy:** rules; timeline; level band; prize; consent.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-021`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-022 — Competition Preparation
- **Role / route / phase:** `LEARNER` / `/app/competitions/:id/prepare` / `P0`
- **User goal:** دراسة خطة تحدي قبل التصفيات.
- **Primary action:** ابدأ مهمة التحضير.
- **Content / anatomy:** due revisions; task list; round slots.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-022`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-023 — Competition Round
- **Role / route / phase:** `LEARNER` / `/app/competitions/:id/round/:roundId` / `P0`
- **User goal:** تنفيذ الاختبار أو التسميع.
- **Primary action:** إرسال المشاركة.
- **Content / anatomy:** question/recitation; attempt; timeout; accessibility.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-023`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-024 — Competition Standings
- **Role / route / phase:** `LEARNER` / `/app/competitions/:id/standings` / `P0`
- **User goal:** نتائج عادلة وخاصة.
- **Primary action:** عرض نتيجتي.
- **Content / anatomy:** level-specific ranking; opt-in pseudonyms.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-024`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-025 — Competition Result & Appeal
- **Role / route / phase:** `LEARNER` / `/app/competitions/:id/result` / `P0`
- **User goal:** تقرير المحكم والمراجعة والاعتراض.
- **Primary action:** تقديم تظلم.
- **Content / anatomy:** criterion scores; review status; appeal window.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-025`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-026 — Achievements
- **Role / route / phase:** `LEARNER` / `/app/achievements` / `P0`
- **User goal:** الشهادات والشارات الداخلية.
- **Primary action:** عرض الشهادة.
- **Content / anatomy:** badges; certificates; no external accreditation.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-026`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-027 — AI Study Assistant
- **Role / route / phase:** `LEARNER` / `/app/ai-coach` / `P0`
- **User goal:** أسئلة عن الخطة فقط وتوصيات موثقة.
- **Primary action:** اسأل عن مراجعاتك.
- **Content / anatomy:** chat; cited tasks; safe fallback; usage budget.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-027`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Label AI outputs as suggestion; show sources (approved teacher evidence), human approval status, safe fallback and cost/rate limits.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-028 — Course Library
- **Role / route / phase:** `LEARNER` / `/app/library` / `P0`
- **User goal:** عرض مقاطع مرخصة قابلة للمشاهدة.
- **Primary action:** شاهد الدرس.
- **Content / anatomy:** program chapters; progress; locked entitlements.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-028`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-029 — Subscription & Billing
- **Role / route / phase:** `LEARNER` / `/app/billing` / `P0`
- **User goal:** ترقية/تجديد وفواتير واضحة.
- **Primary action:** تجديد الاشتراك.
- **Content / anatomy:** plans; credit count; payment status; receipts.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-029`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Currency, taxes, refund, expiry, confirmed webhook state, idempotency and receipts must be visible; never mark paid from redirect alone.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-030 — Notifications
- **Role / route / phase:** `LEARNER` / `/app/notifications` / `P0`
- **User goal:** تنبيهات قابلة للتحكم.
- **Primary action:** ضبط الإشعارات.
- **Content / anatomy:** inbox; prefs; quiet hours.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-030`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-031 — Support and Reports
- **Role / route / phase:** `LEARNER` / `/app/support` / `P0`
- **User goal:** حل مشكلة حصة أو الإبلاغ عن سلامة.
- **Primary action:** فتح تذكرة.
- **Content / anatomy:** ticket categories; status; priority; no oversharing.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-031`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-LEARNER-032 — Account Settings
- **Role / route / phase:** `LEARNER` / `/app/settings` / `P0`
- **User goal:** إدارة الأجهزة والخصوصية وطلب البيانات.
- **Primary action:** حفظ.
- **Content / anatomy:** sessions; withdrawal; export; delete.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-LEARNER-032`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-001 — Teacher Login & Onboarding
- **Role / route / phase:** `TEACHER` / `/teach/start` / `P0`
- **User goal:** تأكيد الهوية والموافقة والعقد.
- **Primary action:** استكمال البيانات.
- **Content / anatomy:** qualification checklist; contract; safeguarding.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-001`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-002 — Teacher Home
- **Role / route / phase:** `TEACHER` / `/teach` / `P0`
- **User goal:** الحصص القادمة والمهام والتقارير المستحقة.
- **Primary action:** افتح الحصة.
- **Content / anatomy:** today timetable; overdue reports; alerts.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-002`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-003 — Availability
- **Role / route / phase:** `TEACHER` / `/teach/availability` / `P0`
- **User goal:** تعديل أوقات العمل والاستثناءات.
- **Primary action:** حفظ التوافر.
- **Content / anatomy:** weekly slots; breaks; timezone.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-003`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Label AI outputs as suggestion; show sources (approved teacher evidence), human approval status, safe fallback and cost/rate limits.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-004 — Teaching Calendar
- **Role / route / phase:** `TEACHER` / `/teach/calendar` / `P0`
- **User goal:** تتبع الحصص والطلاب.
- **Primary action:** عرض الحصة.
- **Content / anatomy:** week grid; student info minimal; status.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-004`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-005 — Lesson Briefing
- **Role / route / phase:** `TEACHER` / `/teach/lessons/:id` / `P0`
- **User goal:** عرض خطة الطالب قبل الحصة.
- **Primary action:** ابدأ الحصة.
- **Content / anatomy:** last approved level; due revision; plan.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-005`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-006 — Teacher Classroom
- **Role / route / phase:** `TEACHER` / `/teach/lessons/:id/live` / `P0`
- **User goal:** تدريس وتحديد آيات ودرجات.
- **Primary action:** إغلاق الحصة.
- **Content / anatomy:** video; Quran annotation; rubric; report quick.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-006`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** State model: prejoin/device-test → connecting → ready → muted/unmuted → reconnecting → ended/failed; external provider mode must show limitations and safe return action.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-007 — Lesson Report Editor
- **Role / route / phase:** `TEACHER` / `/teach/lessons/:id/report` / `P0`
- **User goal:** تسجيل أدلة الحفظ والمراجعة.
- **Primary action:** اعتماد التقرير.
- **Content / anatomy:** rubric; passages; homework; submit.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-007`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-008 — My Assigned Learners
- **Role / route / phase:** `TEACHER` / `/teach/learners` / `P0`
- **User goal:** متابعة الطلاب المخصصين فقط.
- **Primary action:** افتح الملف.
- **Content / anatomy:** list; filter; no direct contact numbers.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-008`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-009 — Learner Academic Detail
- **Role / route / phase:** `TEACHER` / `/teach/learners/:id` / `P0`
- **User goal:** التاريخ والمراجعة والخطة.
- **Primary action:** اقترح تعديل الخطة.
- **Content / anatomy:** memory map; prior reports; weak passages.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-009`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-010 — Assessment Workspace
- **Role / route / phase:** `TEACHER` / `/teach/assessments` / `P0`
- **User goal:** تقييم مستوى جديد.
- **Primary action:** حفظ واعتماد.
- **Content / anatomy:** rubric; assessment evidence; supervisor queue.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-010`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-011 — Plan Review Queue
- **Role / route / phase:** `TEACHER` / `/teach/plans` / `P0`
- **User goal:** مراجعة AI plans وتعديلها.
- **Primary action:** اعتماد أو رفض.
- **Content / anatomy:** side by side; evidence; version diff.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-011`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Label AI outputs as suggestion; show sources (approved teacher evidence), human approval status, safe fallback and cost/rate limits.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-012 — Question Bank Review
- **Role / route / phase:** `TEACHER` / `/teach/questions` / `P0`
- **User goal:** مراجعة أسئلة المناهج.
- **Primary action:** إرسال للمشرف.
- **Content / anatomy:** source; rubric; edit history.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-012`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-013 — Contests Assigned
- **Role / route / phase:** `TEACHER` / `/teach/competitions` / `P0`
- **User goal:** المهام المكلف بها المعلم كحكم.
- **Primary action:** فتح التحكيم.
- **Content / anatomy:** assigned rounds; conflict declaration.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-013`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-014 — Contest Judging
- **Role / route / phase:** `TEACHER` / `/teach/competitions/:id/judge` / `P0`
- **User goal:** التقييم المتزن للمشاركات.
- **Primary action:** حفظ الدرجة.
- **Content / anatomy:** rubric; evidence; separate judge role.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-014`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-015 — Appeals Academic Review
- **Role / route / phase:** `TEACHER` / `/teach/appeals` / `P0`
- **User goal:** فحص الاعتراضات المكلف بها.
- **Primary action:** حفظ القرار.
- **Content / anatomy:** history; independent reviewer.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-015`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-016 — Teacher Pay Statements
- **Role / route / phase:** `TEACHER` / `/teach/pay` / `P0`
- **User goal:** عرض المستحقات حسب العقد.
- **Primary action:** عرض كشف الشهر.
- **Content / anatomy:** salary/lesson/hour/shift; adjustments.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-016`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Currency, taxes, refund, expiry, confirmed webhook state, idempotency and receipts must be visible; never mark paid from redirect alone.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-017 — Teacher Support
- **Role / route / phase:** `TEACHER` / `/teach/support` / `P0`
- **User goal:** التواصل مع الإدارة.
- **Primary action:** فتح طلب.
- **Content / anatomy:** help; dispute pay; lesson incident.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-017`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-TEACHER-018 — Teacher Account & Consent
- **Role / route / phase:** `TEACHER` / `/teach/settings` / `P0`
- **User goal:** إدارة الأمان وتفضيلات الإعلام.
- **Primary action:** حفظ.
- **Content / anatomy:** password/MFA; teacher bio approval.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-TEACHER-018`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Teacher only sees assigned learners and learning data; student direct personal contact details masked.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-001 — Executive Dashboard
- **Role / route / phase:** `ADMIN` / `/admin` / `P0`
- **User goal:** فهم الإيراد والحضور والمشاكل.
- **Primary action:** فتح التقرير.
- **Content / anatomy:** KPI segments; exceptions; alerts.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-001`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-002 — Learner Directory
- **Role / route / phase:** `ADMIN` / `/admin/learners` / `P0`
- **User goal:** البحث بحدود الصلاحيات.
- **Primary action:** فتح متعلم.
- **Content / anatomy:** filters; safeguarding flags role-limited.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-002`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-003 — Learner 360
- **Role / route / phase:** `ADMIN` / `/admin/learners/:id` / `P0`
- **User goal:** ملف تعلم وفواتير وتواصل وتاريخ.
- **Primary action:** حل المشكلة.
- **Content / anatomy:** profile; consent flags; plan; billing; support.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-003`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-004 — Guardian Consent Queue
- **Role / route / phase:** `ADMIN` / `/admin/consents` / `P0`
- **User goal:** مراجعة إثبات الموافقات للقاصرين.
- **Primary action:** اعتماد/رفض.
- **Content / anatomy:** consent document; verification; audit.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-004`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-005 — Staff & Permissions
- **Role / route / phase:** `ADMIN` / `/admin/staff` / `P0`
- **User goal:** إدارة صلاحيات الفريق.
- **Primary action:** تغيير الدور.
- **Content / anatomy:** RBAC; MFA; access review.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-005`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-006 — Teacher Recruitment
- **Role / route / phase:** `ADMIN` / `/admin/teachers/applications` / `P0`
- **User goal:** قبول ومراجعة المعلمين.
- **Primary action:** فتح الطلب.
- **Content / anatomy:** documents; checks; demo lesson.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-006`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-007 — Teacher Management
- **Role / route / phase:** `ADMIN` / `/admin/teachers` / `P0`
- **User goal:** القائمة وحالات الاعتماد.
- **Primary action:** فتح المعلم.
- **Content / anatomy:** teacher capacity; active/suspended.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-007`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-008 — Teacher Profile Admin
- **Role / route / phase:** `ADMIN` / `/admin/teachers/:id` / `P0`
- **User goal:** معلومات المعلم ومؤهلاته.
- **Primary action:** اعتماد.
- **Content / anatomy:** skills; credentials; policies; pay model.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-008`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-009 — Teacher Contract Builder
- **Role / route / phase:** `ADMIN` / `/admin/teachers/:id/compensation` / `P0`
- **User goal:** تحديد عقد الراتب أو الحصة أو الساعة.
- **Primary action:** اعتماد العقد.
- **Content / anatomy:** rate rules; preview; effective date; audit.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-009`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-010 — Teacher Shift Planner
- **Role / route / phase:** `ADMIN` / `/admin/teachers/shifts` / `P0`
- **User goal:** تنظيم جداول المعلمين.
- **Primary action:** حفظ الشيفت.
- **Content / anatomy:** shift blocks; breaks; capacity.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-010`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-011 — Programs CMS
- **Role / route / phase:** `ADMIN` / `/admin/programs` / `P0`
- **User goal:** إدارة البرامج والمناهج.
- **Primary action:** برنامج جديد.
- **Content / anatomy:** curriculum versions; approval.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-011`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-012 — Quran Content Sources
- **Role / route / phase:** `ADMIN` / `/admin/quran-sources` / `P0`
- **User goal:** ضمان المصادر والروايات والتراخيص.
- **Primary action:** اعتماد المصدر.
- **Content / anatomy:** edition registry; license, checksum.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-012`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-013 — Question Bank Manager
- **Role / route / phase:** `ADMIN` / `/admin/question-bank` / `P0`
- **User goal:** تجميع أسئلة اختبار معتمدة.
- **Primary action:** إضافة سؤال.
- **Content / anatomy:** item versions; source; reviewers.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-013`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-014 — Assessment Rubrics
- **Role / route / phase:** `ADMIN` / `/admin/rubrics` / `P0`
- **User goal:** تعريف مقاييس تقييم.
- **Primary action:** إصدار جديد.
- **Content / anatomy:** criterion weights; program/level/riwaya.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-014`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-015 — Bookings Operations
- **Role / route / phase:** `ADMIN` / `/admin/bookings` / `P0`
- **User goal:** حالة الحجوزات والتعارض والتعويض.
- **Primary action:** حل تعارض.
- **Content / anatomy:** calendar; filters; conflict alerts.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-015`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-016 — Live Lessons Monitor
- **Role / route / phase:** `ADMIN` / `/admin/live` / `P0`
- **User goal:** حالة الجلسات وفق الصلاحيات.
- **Primary action:** إعادة جدولة.
- **Content / anatomy:** provider health; join status; not raw surveillance.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-016`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** State model: prejoin/device-test → connecting → ready → muted/unmuted → reconnecting → ended/failed; external provider mode must show limitations and safe return action.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-017 — Conference Provider Registry
- **Role / route / phase:** `ADMIN` / `/admin/video-providers` / `P0`
- **User goal:** تعيين المزود وقدراته دون تخزين أسرار بالواجهة.
- **Primary action:** تحديث السياسات.
- **Content / anatomy:** provider availability; capabilities; failover.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-017`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-018 — Attendance & Makeups
- **Role / route / phase:** `ADMIN` / `/admin/attendance` / `P0`
- **User goal:** تسوية الحصص والغياب.
- **Primary action:** اعتماد التعويض.
- **Content / anatomy:** events; reasons; disputes.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-018`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-019 — Payments & Invoices
- **Role / route / phase:** `ADMIN` / `/admin/payments` / `P0`
- **User goal:** المدفوعات والتسويات والاسترداد.
- **Primary action:** استرداد منضبط.
- **Content / anatomy:** provider status; ledgers; receipts.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-019`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Currency, taxes, refund, expiry, confirmed webhook state, idempotency and receipts must be visible; never mark paid from redirect alone.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-020 — Packages & Promotions
- **Role / route / phase:** `ADMIN` / `/admin/packages` / `P0`
- **User goal:** تسعير حسب البلد والاشتراك.
- **Primary action:** إنشاء باقة.
- **Content / anatomy:** pricing; currency; taxes; policy.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-020`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Currency, taxes, refund, expiry, confirmed webhook state, idempotency and receipts must be visible; never mark paid from redirect alone.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-021 — Payroll Calculations
- **Role / route / phase:** `ADMIN` / `/admin/payroll` / `P0`
- **User goal:** حساب مستحقات المعلمين.
- **Primary action:** توليد دورة دفع.
- **Content / anatomy:** contract version; paid minutes; adjustments.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-021`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Currency, taxes, refund, expiry, confirmed webhook state, idempotency and receipts must be visible; never mark paid from redirect alone.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-022 — Payroll Approval
- **Role / route / phase:** `ADMIN` / `/admin/payroll/:id` / `P0`
- **User goal:** مراجعة وإقرار المستحقات.
- **Primary action:** اعتماد الدفع.
- **Content / anatomy:** dual signoff; discrepancy flags.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-022`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Currency, taxes, refund, expiry, confirmed webhook state, idempotency and receipts must be visible; never mark paid from redirect alone.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-023 — AI Learning Control
- **Role / route / phase:** `ADMIN` / `/admin/ai-learning` / `P0`
- **User goal:** النماذج والتكلفة والاقتراحات.
- **Primary action:** إيقاف النموذج.
- **Content / anatomy:** usage; model versions; false outputs.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-023`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Label AI outputs as suggestion; show sources (approved teacher evidence), human approval status, safe fallback and cost/rate limits.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-024 — Session Policy Review
- **Role / route / phase:** `ADMIN` / `/admin/session-reviews` / `P0`
- **User goal:** مراجعة أعلام المخالفات المصرح بها.
- **Primary action:** حسم الحالة.
- **Content / anatomy:** evidence; consent; human disposition.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-024`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-025 — Competition Templates
- **Role / route / phase:** `ADMIN` / `/admin/competition-templates` / `P0`
- **User goal:** بناء قوالب المسابقات.
- **Primary action:** قالب جديد.
- **Content / anatomy:** event types; level criteria; safe defaults.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-025`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-026 — Contest Builder Wizard
- **Role / route / phase:** `ADMIN` / `/admin/competitions/new` / `P0`
- **User goal:** إنشاء مسابقة من البداية حتى الاعتماد.
- **Primary action:** إرسال للمراجعة.
- **Content / anatomy:** details; eligibility; round; rubric; prize.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-026`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-027 — Competitions List
- **Role / route / phase:** `ADMIN` / `/admin/competitions` / `P0`
- **User goal:** كل المسابقات وسير العمل.
- **Primary action:** فتح مسابقة.
- **Content / anatomy:** state; registrations; compliance status.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-027`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-028 — Competition Control Room
- **Role / route / phase:** `ADMIN` / `/admin/competitions/:id` / `P0`
- **User goal:** إدارة المسابقة المباشرة.
- **Primary action:** بدء جولة.
- **Content / anatomy:** roster; submissions; judge queue; moderation.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-028`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-029 — Judge Assignments
- **Role / route / phase:** `ADMIN` / `/admin/competitions/:id/judges` / `P0`
- **User goal:** تحديد المحكمين ومنع تضارب المصالح.
- **Primary action:** تأكيد المحكمين.
- **Content / anatomy:** qualified judges; conflicts; double review.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-029`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-030 — Leaderboard & Publish
- **Role / route / phase:** `ADMIN` / `/admin/competitions/:id/results` / `P0`
- **User goal:** نتائج وفئات دون كشف أطفال.
- **Primary action:** اعتماد النتائج.
- **Content / anatomy:** provisional; anonymization; audit.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-030`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-031 — Contest Appeals
- **Role / route / phase:** `ADMIN` / `/admin/contest-appeals` / `P0`
- **User goal:** اعتراضات مستقلة وتصحيح النتائج.
- **Primary action:** حسم الاستئناف.
- **Content / anatomy:** score history; reason; reviewer.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-031`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-032 — Contest Rewards & Certificates
- **Role / route / phase:** `ADMIN` / `/admin/rewards` / `P0`
- **User goal:** صرف الجوائز وإصدار شهادات.
- **Primary action:** إصدار.
- **Content / anatomy:** approval; badge; certificate; revocation.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-032`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-033 — CRM Pipeline
- **Role / route / phase:** `ADMIN` / `/admin/crm` / `P0`
- **User goal:** متابعة المسارات التسويقية.
- **Primary action:** متابعة lead.
- **Content / anatomy:** lead board; sources; paid conversion.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-033`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-034 — Campaign Analytics
- **Role / route / phase:** `ADMIN` / `/admin/marketing` / `P0`
- **User goal:** CAC وتجديد لكل cohort.
- **Primary action:** تصدير آمن.
- **Content / anatomy:** funnels; spend; cohorts; opt-outs.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-034`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-035 — Support Center
- **Role / route / phase:** `ADMIN` / `/admin/support` / `P0`
- **User goal:** تذاكر الدعم.
- **Primary action:** تعيين.
- **Content / anatomy:** triage; SLA; permission boundary.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-035`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-036 — Safeguarding Incident Queue
- **Role / route / phase:** `ADMIN` / `/admin/safety` / `P0`
- **User goal:** تدخل سريع في حالات السلامة.
- **Primary action:** تصعيد.
- **Content / anatomy:** severity; evidence handling; authorized only.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-036`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-037 — Recorded Content Library
- **Role / route / phase:** `ADMIN` / `/admin/library` / `P0`
- **User goal:** إدارة المحتوى والترخيص.
- **Primary action:** رفع درس.
- **Content / anatomy:** asset versions; privacy; rights.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-037`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-038 — Notification Center
- **Role / route / phase:** `ADMIN` / `/admin/notifications` / `P0`
- **User goal:** قوالب ورسائل متابعة.
- **Primary action:** إرسال مجدول.
- **Content / anatomy:** templates; unsubscribe; consent.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-038`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-039 — Reports and KPI Explorer
- **Role / route / phase:** `ADMIN` / `/admin/reports` / `P0`
- **User goal:** تقرير نمو وربحية وجودة.
- **Primary action:** إنشاء تقرير.
- **Content / anatomy:** filter; cohort; finance; quality.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-039`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-040 — Audit Trail
- **Role / route / phase:** `ADMIN` / `/admin/audit` / `P0`
- **User goal:** مراجعة تغييرات البيانات المالية والحساسة.
- **Primary action:** تصفية السجل.
- **Content / anatomy:** actor; action; reason; immutable event.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-040`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-ADMIN-041 — Settings & Feature Flags
- **Role / route / phase:** `ADMIN` / `/admin/settings` / `P0`
- **User goal:** إدارة الإصدارات والتكاملات والصلاحيات.
- **Primary action:** حفظ سياسة.
- **Content / anatomy:** flags; provider; AI quotas; locales.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-ADMIN-041`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Access by least privilege; destructive/financial changes require confirmation and auditable reason. Sensitive child/audio fields omitted unless specifically authorized.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-001 — Flutter Login
- **Role / route / phase:** `MOBILE` / `mobile://auth` / `P2`
- **User goal:** دخول موحد وحفظ رموز بأمان.
- **Primary action:** دخول.
- **Content / anatomy:** auth; OTP; biometric optional.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-001`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-002 — Flutter Today
- **Role / route / phase:** `MOBILE` / `mobile://home` / `P2`
- **User goal:** مهام اليوم وقرب الحصة.
- **Primary action:** ابدأ المراجعة.
- **Content / anatomy:** upcoming; revisions; notifications.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-002`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-003 — Flutter Classroom
- **Role / route / phase:** `MOBILE` / `mobile://classroom` / `P2`
- **User goal:** صوت وفيديو ومصحف بتخطيط شاشة صغيرة.
- **Primary action:** دخول.
- **Content / anatomy:** video overlay; Quran sheet; mic; reconnection.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-003`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** State model: prejoin/device-test → connecting → ready → muted/unmuted → reconnecting → ended/failed; external provider mode must show limitations and safe return action.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-004 — Flutter Schedule
- **Role / route / phase:** `MOBILE` / `mobile://schedule` / `P2`
- **User goal:** حجوزات واعتماد منطقة الزمن.
- **Primary action:** احجز.
- **Content / anatomy:** day list; teacher slots; reschedule.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-004`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-005 — Flutter Memory Map
- **Role / route / phase:** `MOBILE` / `mobile://memory` / `P2`
- **User goal:** نقاط الحفظ على الموبايل.
- **Primary action:** استكشف.
- **Content / anatomy:** compact surah matrix; evidence details.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-005`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-006 — Flutter AI Coach
- **Role / route / phase:** `MOBILE` / `mobile://coach` / `P2`
- **User goal:** توصيات من بيانات موثقة.
- **Primary action:** ابدأ تمرين.
- **Content / anatomy:** chat; suggestion; approved plan.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-006`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-007 — Flutter Exam
- **Role / route / phase:** `MOBILE` / `mobile://exam` / `P2`
- **User goal:** حل اختبار آمن حتى مع انقطاع.
- **Primary action:** تسليم.
- **Content / anatomy:** local draft; timer server; reconnect.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-007`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-008 — Flutter Competition
- **Role / route / phase:** `MOBILE` / `mobile://competition` / `P2`
- **User goal:** متابعة مسابقة ملائمة.
- **Primary action:** اشترك.
- **Content / anatomy:** details; rounds; scoreboard privacy.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-008`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Contest requires age/level eligibility, explicit rules, private leaderboard by default, reviewed scores and appeals; no cash/paid advantage without legal clearance.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-009 — Flutter Teacher Today
- **Role / route / phase:** `MOBILE` / `mobile://teacher` / `P2`
- **User goal:** جدول المعلم وتقاريره.
- **Primary action:** ابدأ الحصة.
- **Content / anatomy:** today; report quick compose.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-009`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-010 — Flutter Teacher Report
- **Role / route / phase:** `MOBILE` / `mobile://teacher/report` / `P2`
- **User goal:** تقييم معلم بواجهة قصيرة.
- **Primary action:** حفظ.
- **Content / anatomy:** rubric cards; partial offline draft.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-010`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.

## UX-MOBILE-011 — Flutter Account
- **Role / route / phase:** `MOBILE` / `mobile://settings` / `P2`
- **User goal:** خصوصية وإشعارات والأجهزة.
- **Primary action:** حفظ.
- **Content / anatomy:** consents; security; push prefs.
- **API contract:** map UI request to typed `/api/v1` endpoint; support pagination/validation; no direct vendor secret.
- **States:** default, loading skeleton, empty actionable, empty no access, submitted/success, invalid-input, server error with retry, offline/reconnecting, permission/consent blocked.
- **Behavior:** keep input drafts on recoverable failures, keyboard navigation, confirm high-impact action, meaningful server validation, unsaved-changes alert when editing.
- **Responsive:** 1440 two-column as appropriate, 768 condensed, 390 single-column, 360 minimum; touch controls >=44x44 CSS px design target.
- **Instrumentation:** `screen_viewed` with `UX-MOBILE-011`, `primary_action_clicked`, `form_error_shown`, `task_completed` where applicable; privacy-safe payload.
- **Extra:** Include safe area, native navigation/back, background/foreground media handling, 360/390 width and offline skeleton.
- **UAT:** role-specific visible data, forbidden data absent, action result and audit verified, AR/EN RTL/LTR, screen reader label, no dead end.
