# أكاديمية أُسَيْد — النسخة التخطيطية النهائية (المصدر READY فقط)

## ماذا تحتوي هذه الحزمة؟
- `source_original/usayd-academy-codex-package/`: ملفات المصدر READY حرفيًا (كل الملفات غير الخطوط، متحقق منها SHA256). لا تعديل على UI/UX أو OpenAPI المصدر.
- `planning/tasks/`: 707 ملف Markdown مستقل، فيها المواصفات والمراجع ومعايير التحقق والمراجعة.
- `planning/sprints/`: 91 sprint مرشحة قابلة لإعادة الجدولة وفق سرعة الفريق. **ليست التزامًا زمنيًا ولا Sprints موجودة بالفعل في Jira**.
- `jira/`: 33 Epic + 707 work items، CSV وPython idempotent import/sync scripts، Dependencies.
- `management/`: Architecture، Code Review، Release Gates، قرارات مالك المشروع.
- `repo_bootstrap/`: ملفات GitHub Actions وPR template وAgent guidance لكل مستودع مستقل، لا تتضمن مشروع Laravel/Next.js/Flutter منشأ فعليًا.
- `automation/`: AI reviewer وقواعد auto-merge مع إعدادات Secure Runner.
- `coverage/`: FR/Screen/Action/API/Journey traceability وSHA256 لكل المصدر.
- `USAYD_GEMINI_CODEX_AUTONOMOUS_MASTER_PROMPT.md`: البرومبت الرئيسي للتنفيذ.

## أول تشغيل
1. اقرأ `management/DECISIONS_AND_GATES.md` والقرارات المعلقة؛ لا تفعل وظائف مدفوعة أو تخص القاصرين بدون اعتماد.
2. أنشئ أو تحقّق من المستودعات الثلاثة: `usayd-api`, `usayd-web`, `usayd-flutter`. كل واحد repo مستقل.
3. جهّز قواعد حماية main وSecrets وCI وفق `automation/README.md`.
4. مشروع Jira الحالي موجود بالفعل؛ لا تعِد استيراد الحزمة أو تشغيل طوابير تاريخية. للتأسيس الأول فقط في مشروع جديد، نفّذ `python jira/jira_sync.py --plan-only` محليًا بلا Credentials (682 صفًا full-stack، واستبعاد 57 تاسك Flutter وEpic واحد)، ثم `--dry-run` للتحقق بالقراءة. يتطلب الإنشاء `--apply` صراحةً بعد مراجعة الخطة. لا ينشئ هذا المسار أي تاسك أو Epic خاص بـFlutter؛ مسؤول الموبايل يدير نطاقه منفصلًا. استخدم Jira الحي للتحقق والتزامن المعتاد.
5. ابدأ Sprint `planning/sprints/S00.md`، تذكرة واحدة لكل feature branch وPull Request، ثم مراجعة وحماية ودمج موثق.
6. تطبيق Flutter يبدأ UI + fixture-driven tests بالتوازي؛ الربط الفعلي يبدأ بعد جاهزية API وcontract.

## مهم
- هذه **حزمة تخطيط وتشغيل آلي قابلة للتهيئة**، ليست Backend ولا Frontend ولا تطبيقًا يعمل في Production.
- لا توجد Secrets أو Token أو اتصال دائم بالـGemini Runner داخل الحزمة. يجب تهيئة وتشغيل runner على حسابك.
- 91 Sprints فقط جدولة مرشحة لكامل النطاق؛ الفريق شخصان، فتوقع إعادة تقدير مستمرة.
- الـAI review لا يصح اعتباره موافقة بشرية. أكمل متطلبات Code Owners / branch rules للحالات الحساسة.
- ملفات الخطوط لا يعاد توزيعها؛ استخدم الأصل المرخص عند التنفيذ.

## الحالة الفعلية والمراجع الحية (26 نوفمبر 2026)
- [حالة GitHub وJira الموثقة](automation/LIVE_DELIVERY_STATE.json) — لا تستخدم التقارير التاريخية كحالة حية.
- [فهرس تصميم كل 169 شاشة](management/SCREEN_DESIGN_CATALOG.md) و[دليل التحويل من التصميم للكود](management/DESIGN_IMPLEMENTATION_GUIDE.md).
- [قرارات المالك المحدثة](management/OWNER_DECISION_REGISTER_2026-11-26.md)، [الخطوة التالية](automation/NEXT_ACTIONS.md).
- المصدر الأصلي immutable. قبل كل تاسك اقرأ الـspec وCanvas وAR/EN HTML والعقود والـFR والصلاحيات. بعد كل PR أو تعديل Jira حدث السجل الحي بأدلة فعلية. Flutter للقراءة فقط في مسار full-stack.

## تحديث 27 نوفمبر 2026
- [دليل التشغيل بين الفرق](architecture/CROSS_TEAM_OPERATIONS_RUNBOOK.md) و[دليل أدلة حماية المستودعات](architecture/REPOSITORY_GOVERNANCE_EVIDENCE.md).
- كل الأدوار التخصصية غير معينة بحسب تأكيد المالك؛ لا يعتبر ذلك اعتمادًا. لا تبدأ USYD-81 قبل إغلاق USYD-54. لا تطلب كلمات مرور أو مفاتيح API في المحادثة.
