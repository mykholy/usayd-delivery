# Screen inventory — public, learner, teacher, admin & mobile

**119 planned screens** with unique UX IDs. P0/P1/P2 release phases in this registry are defaults; feature gates supersede route labels: exam/AI/competition screens must not appear until their dependencies ship.

| ID | Persona | Screen | Route/frame | Business job | Primary CTA | Key components | Base phase |
|---|---|---|---|---|---|---|---|
| UX-PUBLIC-001 | PUBLIC | Marketing Home | / | بناء الثقة وإظهار البرامج والنتائج وآلية المتابعة | احجز تقييم مستوى | Hero; teacher proof; feature journey; pricing; real FAQ; CTA | P0 |
| UX-PUBLIC-002 | PUBLIC | Programs Directory | /programs | مقارنة برامج الحفظ/التجويد/المراجعة | استكشف البرنامج | program cards; outcomes; level/age tags; tabs | P0 |
| UX-PUBLIC-003 | PUBLIC | Program Detail | /programs/:slug | عرض مسار ومخرجات البرنامج | ابدأ تقييم المستوى | curriculum roadmap; eligibility; teachers; price | P0 |
| UX-PUBLIC-004 | PUBLIC | Pricing | /pricing | توضيح الباقات حسب البلد والعملات | اختر باقة | country currency; package duration; refund policy | P0 |
| UX-PUBLIC-005 | PUBLIC | Teacher Directory | /teachers | عرض المعلمين المؤهلين | تعرف على المعلم | teacher cards; filters; verified qualifications | P0 |
| UX-PUBLIC-006 | PUBLIC | Teacher Public Profile | /teachers/:slug | تعريف خبرة المعلم قبل الاشتراك | احجز تجربة | bio; certificates verified; languages; schedule | P0 |
| UX-PUBLIC-007 | PUBLIC | How It Works | /how-it-works | عرض رحلة التعلم بلا ادعاءات | احجز تجربة | steps; learning map demo; FAQ | P0 |
| UX-PUBLIC-008 | PUBLIC | Competition Landing | /challenges | شرح المسابقات العامة بدون بيانات حساسة | اكتشف التحديات | contest marketing cards; eligibility copy; examples | P0 |
| UX-PUBLIC-009 | PUBLIC | Free Assessment Booking | /trial | حجز تقييمي مباشر بحدود الاستغلال | احجز الموعد | contact; timezone; available slots; consent | P0 |
| UX-PUBLIC-010 | PUBLIC | About/Academic Standards | /about | عرض المعايير الأكاديمية والاعتمادات الحقيقية | شوف البرامج | team; method; teacher checks | P0 |
| UX-PUBLIC-011 | PUBLIC | FAQ & Support | /help | دعم العملاء والاسترداد والجدولة | ابدأ محادثة الدعم | FAQ; policies; contact support | P0 |
| UX-PUBLIC-012 | PUBLIC | Legal & Consents | /legal/:slug | عرض الشروط والخصوصية بمستويات فهم | اقرأ السياسة | policy archive; accessibility; language toggle | P0 |
| UX-AUTH-001 | AUTH | Unified Signup | /signup | تسجيل جميع الأعمار كمتعلم | إنشاء حساب | contact; name; age band; OTP; terms | P0 |
| UX-AUTH-002 | AUTH | Guardian Consent Step | /onboarding/guardian-consent | استيفاء تحقق ولي الأمر للقاصر | إرسال طلب الموافقة | guardian contact; proof; consent receipt; pending | P0 |
| UX-AUTH-003 | AUTH | Login | /login | تسجيل الدخول سريع وآمن | تسجيل الدخول | email/phone; password or code; recover | P0 |
| UX-AUTH-004 | AUTH | Password Recovery | /forgot-password | استرداد الحساب دون تسريب وجوده | استرداد | contact; OTP; neutral messages | P0 |
| UX-AUTH-005 | AUTH | Welcome Onboarding | /onboarding | هدف ووقت ورواية ومستوى | متابعة | goal; duration; timezone; preference | P0 |
| UX-LEARNER-001 | LEARNER | Learner Home | /app | إنجاز اليوم والحصة القادمة والتقدم | ابدأ مهمة اليوم | next lesson; daily card; due revision; alerts; contest | P0 |
| UX-LEARNER-002 | LEARNER | My Learning Profile | /app/profile | تعديل تفضيلات الدراسة | حفظ التغييرات | goals; schedule; locale; accessibility; security | P0 |
| UX-LEARNER-003 | LEARNER | Programs Discover | /app/programs | إضافة مسار تعلم | شوف البرنامج | tracks; level filter; teacher availability | P0 |
| UX-LEARNER-004 | LEARNER | Initial Assessment | /app/assessment | حجز/عرض تقييم أولي | حجز تقييم | rubric; assessment history; feedback | P0 |
| UX-LEARNER-005 | LEARNER | Teachers Discover | /app/teachers | اختيار معلم مناسب | اختيار موعد | verified filters; teacher card; availability | P0 |
| UX-LEARNER-006 | LEARNER | Teacher Detail | /app/teachers/:id | استعراض المؤهلات وأوقات المعلم | احجز مع المعلم | bio; level; languages; slots | P0 |
| UX-LEARNER-007 | LEARNER | Calendar | /app/calendar | استعراض جدول الحصص بالتوقيت المحلي | حجز أو تغيير | day/week; timezone label; upcoming | P0 |
| UX-LEARNER-008 | LEARNER | Booking Wizard | /app/book | اختيار البرنامج والمعلم والوقت والرصيد | تأكيد الحجز | stepper; conflict validation; credit preview | P0 |
| UX-LEARNER-009 | LEARNER | Lesson Detail | /app/lessons/:id | عرض التفاصيل وخطة الدرس وتذكير | دخول الحصة | teacher; join window; consent; provider mode | P0 |
| UX-LEARNER-010 | LEARNER | Classroom | /app/lessons/:id/live | تسميع ومصحف وواجب ووسائل اتصال | إنهاء الحصة | video; Quran; teacher annotations; mic/video; reconnect | P0 |
| UX-LEARNER-011 | LEARNER | Post-Lesson Report | /app/lessons/:id/report | عرض الحفظ والمراجعة والأخطاء | راجع الواجب | coverage; revision; approved notes; rating | P0 |
| UX-LEARNER-012 | LEARNER | Learning Plan | /app/plan | متابعة خطة أسبوعية وشهرية | ابدأ المهمة | timeline; teacher-approved versions; daily goals | P0 |
| UX-LEARNER-013 | LEARNER | Daily Study | /app/study | إنجاز ممارسة ذاتية | إنهاء التدريب | Quran; steps; timer optional; self-report | P0 |
| UX-LEARNER-014 | LEARNER | Revision Queue | /app/revision | المراجعات المستحقة حسب الضعف | راجع الآن | due groups; passage chips; estimated time | P0 |
| UX-LEARNER-015 | LEARNER | Memory Map | /app/memory-map | مخطط حفظ السور والآيات | افتح المقطع | surah grid; segment status; evidence dates | P0 |
| UX-LEARNER-016 | LEARNER | Practice Recording | /app/practice | تسميع اختياري مع ضوابط | إرسال للمعلم | mic; consent; duration; private replay | P0 |
| UX-LEARNER-017 | LEARNER | Exam Catalog | /app/exams | اختبارات متناسبة مع المستوى | ابدأ اختبار | difficulty tags; eligible exams; previous attempts | P0 |
| UX-LEARNER-018 | LEARNER | Exam Taking | /app/exams/:id/take | تقديم اختبار بأسئلة معتمدة | تسليم الاختبار | progress; question renderer; timer policy; draft save | P0 |
| UX-LEARNER-019 | LEARNER | Exam Results | /app/exams/:id/result | نقاط قوة وضعف وتوصيات مراجعة | عرض الخطة الجديدة | rubric breakdown; review buttons; appeal | P0 |
| UX-LEARNER-020 | LEARNER | Competitions Discover | /app/competitions | اكتشاف مسابقات مناسبة | عرض التفاصيل | level tabs; current/upcoming; private mode | P0 |
| UX-LEARNER-021 | LEARNER | Competition Detail | /app/competitions/:id | معرفة الأهلية والقواعد والجوائز | اشترك | rules; timeline; level band; prize; consent | P0 |
| UX-LEARNER-022 | LEARNER | Competition Preparation | /app/competitions/:id/prepare | دراسة خطة تحدي قبل التصفيات | ابدأ مهمة التحضير | due revisions; task list; round slots | P0 |
| UX-LEARNER-023 | LEARNER | Competition Round | /app/competitions/:id/round/:roundId | تنفيذ الاختبار أو التسميع | إرسال المشاركة | question/recitation; attempt; timeout; accessibility | P0 |
| UX-LEARNER-024 | LEARNER | Competition Standings | /app/competitions/:id/standings | نتائج عادلة وخاصة | عرض نتيجتي | level-specific ranking; opt-in pseudonyms | P0 |
| UX-LEARNER-025 | LEARNER | Competition Result & Appeal | /app/competitions/:id/result | تقرير المحكم والمراجعة والاعتراض | تقديم تظلم | criterion scores; review status; appeal window | P0 |
| UX-LEARNER-026 | LEARNER | Achievements | /app/achievements | الشهادات والشارات الداخلية | عرض الشهادة | badges; certificates; no external accreditation | P0 |
| UX-LEARNER-027 | LEARNER | AI Study Assistant | /app/ai-coach | أسئلة عن الخطة فقط وتوصيات موثقة | اسأل عن مراجعاتك | chat; cited tasks; safe fallback; usage budget | P0 |
| UX-LEARNER-028 | LEARNER | Course Library | /app/library | عرض مقاطع مرخصة قابلة للمشاهدة | شاهد الدرس | program chapters; progress; locked entitlements | P0 |
| UX-LEARNER-029 | LEARNER | Subscription & Billing | /app/billing | ترقية/تجديد وفواتير واضحة | تجديد الاشتراك | plans; credit count; payment status; receipts | P0 |
| UX-LEARNER-030 | LEARNER | Notifications | /app/notifications | تنبيهات قابلة للتحكم | ضبط الإشعارات | inbox; prefs; quiet hours | P0 |
| UX-LEARNER-031 | LEARNER | Support and Reports | /app/support | حل مشكلة حصة أو الإبلاغ عن سلامة | فتح تذكرة | ticket categories; status; priority; no oversharing | P0 |
| UX-LEARNER-032 | LEARNER | Account Settings | /app/settings | إدارة الأجهزة والخصوصية وطلب البيانات | حفظ | sessions; withdrawal; export; delete | P0 |
| UX-TEACHER-001 | TEACHER | Teacher Login & Onboarding | /teach/start | تأكيد الهوية والموافقة والعقد | استكمال البيانات | qualification checklist; contract; safeguarding | P0 |
| UX-TEACHER-002 | TEACHER | Teacher Home | /teach | الحصص القادمة والمهام والتقارير المستحقة | افتح الحصة | today timetable; overdue reports; alerts | P0 |
| UX-TEACHER-003 | TEACHER | Availability | /teach/availability | تعديل أوقات العمل والاستثناءات | حفظ التوافر | weekly slots; breaks; timezone | P0 |
| UX-TEACHER-004 | TEACHER | Teaching Calendar | /teach/calendar | تتبع الحصص والطلاب | عرض الحصة | week grid; student info minimal; status | P0 |
| UX-TEACHER-005 | TEACHER | Lesson Briefing | /teach/lessons/:id | عرض خطة الطالب قبل الحصة | ابدأ الحصة | last approved level; due revision; plan | P0 |
| UX-TEACHER-006 | TEACHER | Teacher Classroom | /teach/lessons/:id/live | تدريس وتحديد آيات ودرجات | إغلاق الحصة | video; Quran annotation; rubric; report quick | P0 |
| UX-TEACHER-007 | TEACHER | Lesson Report Editor | /teach/lessons/:id/report | تسجيل أدلة الحفظ والمراجعة | اعتماد التقرير | rubric; passages; homework; submit | P0 |
| UX-TEACHER-008 | TEACHER | My Assigned Learners | /teach/learners | متابعة الطلاب المخصصين فقط | افتح الملف | list; filter; no direct contact numbers | P0 |
| UX-TEACHER-009 | TEACHER | Learner Academic Detail | /teach/learners/:id | التاريخ والمراجعة والخطة | اقترح تعديل الخطة | memory map; prior reports; weak passages | P0 |
| UX-TEACHER-010 | TEACHER | Assessment Workspace | /teach/assessments | تقييم مستوى جديد | حفظ واعتماد | rubric; assessment evidence; supervisor queue | P0 |
| UX-TEACHER-011 | TEACHER | Plan Review Queue | /teach/plans | مراجعة AI plans وتعديلها | اعتماد أو رفض | side by side; evidence; version diff | P0 |
| UX-TEACHER-012 | TEACHER | Question Bank Review | /teach/questions | مراجعة أسئلة المناهج | إرسال للمشرف | source; rubric; edit history | P0 |
| UX-TEACHER-013 | TEACHER | Contests Assigned | /teach/competitions | المهام المكلف بها المعلم كحكم | فتح التحكيم | assigned rounds; conflict declaration | P0 |
| UX-TEACHER-014 | TEACHER | Contest Judging | /teach/competitions/:id/judge | التقييم المتزن للمشاركات | حفظ الدرجة | rubric; evidence; separate judge role | P0 |
| UX-TEACHER-015 | TEACHER | Appeals Academic Review | /teach/appeals | فحص الاعتراضات المكلف بها | حفظ القرار | history; independent reviewer | P0 |
| UX-TEACHER-016 | TEACHER | Teacher Pay Statements | /teach/pay | عرض المستحقات حسب العقد | عرض كشف الشهر | salary/lesson/hour/shift; adjustments | P0 |
| UX-TEACHER-017 | TEACHER | Teacher Support | /teach/support | التواصل مع الإدارة | فتح طلب | help; dispute pay; lesson incident | P0 |
| UX-TEACHER-018 | TEACHER | Teacher Account & Consent | /teach/settings | إدارة الأمان وتفضيلات الإعلام | حفظ | password/MFA; teacher bio approval | P0 |
| UX-ADMIN-001 | ADMIN | Executive Dashboard | /admin | فهم الإيراد والحضور والمشاكل | فتح التقرير | KPI segments; exceptions; alerts | P0 |
| UX-ADMIN-002 | ADMIN | Learner Directory | /admin/learners | البحث بحدود الصلاحيات | فتح متعلم | filters; safeguarding flags role-limited | P0 |
| UX-ADMIN-003 | ADMIN | Learner 360 | /admin/learners/:id | ملف تعلم وفواتير وتواصل وتاريخ | حل المشكلة | profile; consent flags; plan; billing; support | P0 |
| UX-ADMIN-004 | ADMIN | Guardian Consent Queue | /admin/consents | مراجعة إثبات الموافقات للقاصرين | اعتماد/رفض | consent document; verification; audit | P0 |
| UX-ADMIN-005 | ADMIN | Staff & Permissions | /admin/staff | إدارة صلاحيات الفريق | تغيير الدور | RBAC; MFA; access review | P0 |
| UX-ADMIN-006 | ADMIN | Teacher Recruitment | /admin/teachers/applications | قبول ومراجعة المعلمين | فتح الطلب | documents; checks; demo lesson | P0 |
| UX-ADMIN-007 | ADMIN | Teacher Management | /admin/teachers | القائمة وحالات الاعتماد | فتح المعلم | teacher capacity; active/suspended | P0 |
| UX-ADMIN-008 | ADMIN | Teacher Profile Admin | /admin/teachers/:id | معلومات المعلم ومؤهلاته | اعتماد | skills; credentials; policies; pay model | P0 |
| UX-ADMIN-009 | ADMIN | Teacher Contract Builder | /admin/teachers/:id/compensation | تحديد عقد الراتب أو الحصة أو الساعة | اعتماد العقد | rate rules; preview; effective date; audit | P0 |
| UX-ADMIN-010 | ADMIN | Teacher Shift Planner | /admin/teachers/shifts | تنظيم جداول المعلمين | حفظ الشيفت | shift blocks; breaks; capacity | P0 |
| UX-ADMIN-011 | ADMIN | Programs CMS | /admin/programs | إدارة البرامج والمناهج | برنامج جديد | curriculum versions; approval | P0 |
| UX-ADMIN-012 | ADMIN | Quran Content Sources | /admin/quran-sources | ضمان المصادر والروايات والتراخيص | اعتماد المصدر | edition registry; license, checksum | P0 |
| UX-ADMIN-013 | ADMIN | Question Bank Manager | /admin/question-bank | تجميع أسئلة اختبار معتمدة | إضافة سؤال | item versions; source; reviewers | P0 |
| UX-ADMIN-014 | ADMIN | Assessment Rubrics | /admin/rubrics | تعريف مقاييس تقييم | إصدار جديد | criterion weights; program/level/riwaya | P0 |
| UX-ADMIN-015 | ADMIN | Bookings Operations | /admin/bookings | حالة الحجوزات والتعارض والتعويض | حل تعارض | calendar; filters; conflict alerts | P0 |
| UX-ADMIN-016 | ADMIN | Live Lessons Monitor | /admin/live | حالة الجلسات وفق الصلاحيات | إعادة جدولة | provider health; join status; not raw surveillance | P0 |
| UX-ADMIN-017 | ADMIN | Conference Provider Registry | /admin/video-providers | تعيين المزود وقدراته دون تخزين أسرار بالواجهة | تحديث السياسات | provider availability; capabilities; failover | P0 |
| UX-ADMIN-018 | ADMIN | Attendance & Makeups | /admin/attendance | تسوية الحصص والغياب | اعتماد التعويض | events; reasons; disputes | P0 |
| UX-ADMIN-019 | ADMIN | Payments & Invoices | /admin/payments | المدفوعات والتسويات والاسترداد | استرداد منضبط | provider status; ledgers; receipts | P0 |
| UX-ADMIN-020 | ADMIN | Packages & Promotions | /admin/packages | تسعير حسب البلد والاشتراك | إنشاء باقة | pricing; currency; taxes; policy | P0 |
| UX-ADMIN-021 | ADMIN | Payroll Calculations | /admin/payroll | حساب مستحقات المعلمين | توليد دورة دفع | contract version; paid minutes; adjustments | P0 |
| UX-ADMIN-022 | ADMIN | Payroll Approval | /admin/payroll/:id | مراجعة وإقرار المستحقات | اعتماد الدفع | dual signoff; discrepancy flags | P0 |
| UX-ADMIN-023 | ADMIN | AI Learning Control | /admin/ai-learning | النماذج والتكلفة والاقتراحات | إيقاف النموذج | usage; model versions; false outputs | P0 |
| UX-ADMIN-024 | ADMIN | Session Policy Review | /admin/session-reviews | مراجعة أعلام المخالفات المصرح بها | حسم الحالة | evidence; consent; human disposition | P0 |
| UX-ADMIN-025 | ADMIN | Competition Templates | /admin/competition-templates | بناء قوالب المسابقات | قالب جديد | event types; level criteria; safe defaults | P0 |
| UX-ADMIN-026 | ADMIN | Contest Builder Wizard | /admin/competitions/new | إنشاء مسابقة من البداية حتى الاعتماد | إرسال للمراجعة | details; eligibility; round; rubric; prize | P0 |
| UX-ADMIN-027 | ADMIN | Competitions List | /admin/competitions | كل المسابقات وسير العمل | فتح مسابقة | state; registrations; compliance status | P0 |
| UX-ADMIN-028 | ADMIN | Competition Control Room | /admin/competitions/:id | إدارة المسابقة المباشرة | بدء جولة | roster; submissions; judge queue; moderation | P0 |
| UX-ADMIN-029 | ADMIN | Judge Assignments | /admin/competitions/:id/judges | تحديد المحكمين ومنع تضارب المصالح | تأكيد المحكمين | qualified judges; conflicts; double review | P0 |
| UX-ADMIN-030 | ADMIN | Leaderboard & Publish | /admin/competitions/:id/results | نتائج وفئات دون كشف أطفال | اعتماد النتائج | provisional; anonymization; audit | P0 |
| UX-ADMIN-031 | ADMIN | Contest Appeals | /admin/contest-appeals | اعتراضات مستقلة وتصحيح النتائج | حسم الاستئناف | score history; reason; reviewer | P0 |
| UX-ADMIN-032 | ADMIN | Contest Rewards & Certificates | /admin/rewards | صرف الجوائز وإصدار شهادات | إصدار | approval; badge; certificate; revocation | P0 |
| UX-ADMIN-033 | ADMIN | CRM Pipeline | /admin/crm | متابعة المسارات التسويقية | متابعة lead | lead board; sources; paid conversion | P0 |
| UX-ADMIN-034 | ADMIN | Campaign Analytics | /admin/marketing | CAC وتجديد لكل cohort | تصدير آمن | funnels; spend; cohorts; opt-outs | P0 |
| UX-ADMIN-035 | ADMIN | Support Center | /admin/support | تذاكر الدعم | تعيين | triage; SLA; permission boundary | P0 |
| UX-ADMIN-036 | ADMIN | Safeguarding Incident Queue | /admin/safety | تدخل سريع في حالات السلامة | تصعيد | severity; evidence handling; authorized only | P0 |
| UX-ADMIN-037 | ADMIN | Recorded Content Library | /admin/library | إدارة المحتوى والترخيص | رفع درس | asset versions; privacy; rights | P0 |
| UX-ADMIN-038 | ADMIN | Notification Center | /admin/notifications | قوالب ورسائل متابعة | إرسال مجدول | templates; unsubscribe; consent | P0 |
| UX-ADMIN-039 | ADMIN | Reports and KPI Explorer | /admin/reports | تقرير نمو وربحية وجودة | إنشاء تقرير | filter; cohort; finance; quality | P0 |
| UX-ADMIN-040 | ADMIN | Audit Trail | /admin/audit | مراجعة تغييرات البيانات المالية والحساسة | تصفية السجل | actor; action; reason; immutable event | P0 |
| UX-ADMIN-041 | ADMIN | Settings & Feature Flags | /admin/settings | إدارة الإصدارات والتكاملات والصلاحيات | حفظ سياسة | flags; provider; AI quotas; locales | P0 |
| UX-MOBILE-001 | MOBILE | Flutter Login | mobile://auth | دخول موحد وحفظ رموز بأمان | دخول | auth; OTP; biometric optional | P2 |
| UX-MOBILE-002 | MOBILE | Flutter Today | mobile://home | مهام اليوم وقرب الحصة | ابدأ المراجعة | upcoming; revisions; notifications | P2 |
| UX-MOBILE-003 | MOBILE | Flutter Classroom | mobile://classroom | صوت وفيديو ومصحف بتخطيط شاشة صغيرة | دخول | video overlay; Quran sheet; mic; reconnection | P2 |
| UX-MOBILE-004 | MOBILE | Flutter Schedule | mobile://schedule | حجوزات واعتماد منطقة الزمن | احجز | day list; teacher slots; reschedule | P2 |
| UX-MOBILE-005 | MOBILE | Flutter Memory Map | mobile://memory | نقاط الحفظ على الموبايل | استكشف | compact surah matrix; evidence details | P2 |
| UX-MOBILE-006 | MOBILE | Flutter AI Coach | mobile://coach | توصيات من بيانات موثقة | ابدأ تمرين | chat; suggestion; approved plan | P2 |
| UX-MOBILE-007 | MOBILE | Flutter Exam | mobile://exam | حل اختبار آمن حتى مع انقطاع | تسليم | local draft; timer server; reconnect | P2 |
| UX-MOBILE-008 | MOBILE | Flutter Competition | mobile://competition | متابعة مسابقة ملائمة | اشترك | details; rounds; scoreboard privacy | P2 |
| UX-MOBILE-009 | MOBILE | Flutter Teacher Today | mobile://teacher | جدول المعلم وتقاريره | ابدأ الحصة | today; report quick compose | P2 |
| UX-MOBILE-010 | MOBILE | Flutter Teacher Report | mobile://teacher/report | تقييم معلم بواجهة قصيرة | حفظ | rubric cards; partial offline draft | P2 |
| UX-MOBILE-011 | MOBILE | Flutter Account | mobile://settings | خصوصية وإشعارات والأجهزة | حفظ | consents; security; push prefs | P2 |
