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
4. بعد عودة Jira، أنشئ مشروع Scrum واحدًا وادخل المهام عبر `jira/jira_sync.py` ثم اربط Sprints/Dependencies. إن لم تعد الخدمة، استخدم ملفات CSV محليًا مع حالة BLOCKED بدل الادعاء برفعها.
5. ابدأ Sprint `planning/sprints/S00.md`، تذكرة واحدة لكل feature branch وPull Request، ثم مراجعة وحماية ودمج موثق.
6. تطبيق Flutter يبدأ UI + fixture-driven tests بالتوازي؛ الربط الفعلي يبدأ بعد جاهزية API وcontract.

## مهم
- هذه **حزمة تخطيط وتشغيل آلي قابلة للتهيئة**، ليست Backend ولا Frontend ولا تطبيقًا يعمل في Production.
- لا توجد Secrets أو Token أو اتصال دائم بالـGemini Runner داخل الحزمة. يجب تهيئة وتشغيل runner على حسابك.
- 91 Sprints فقط جدولة مرشحة لكامل النطاق؛ الفريق شخصان، فتوقع إعادة تقدير مستمرة.
- الـAI review لا يصح اعتباره موافقة بشرية. أكمل متطلبات Code Owners / branch rules للحالات الحساسة.
- ملفات الخطوط لا يعاد توزيعها؛ استخدم الأصل المرخص عند التنفيذ.
