# تقرير الاستيراد النهائي — أكاديمية أُسَيْد

**المشروع:** [Usayd Platform (USYD)](https://mykholy.atlassian.net/jira/software/projects/USYD/boards/1)  
**التاريخ:** 24 نوفمبر 2026  
**المرجع:** `USAYD_READY_JIRA_IMPORT_740.csv` المستخرج من حزمة READY النهائية.

## نتيجة الفحص من Jira الفعلي

| الفحص | نتيجة Jira |
|---|---:|
| جميع سجلات المشروع (مع سجلات التكرار) | 745 |
| العناصر المعتمدة ذات label `usayd-spec-handoff` | **740** |
| Epics المعتمدة | **33 / 33** |
| Task + Story المعتمدة | **707 / 707** |
| مهام Flutter المعتمدة | **57 / 57** |
| مهام Flutter المسندة لأحمد ممدوح | **57 / 57** |
| مهام Task/Story بلا Epic Parent | **0** |
| السجلات المكررة الموسومة `duplicate-ignore` بحالة Done | **5** |

**توزيع ملفات المصدر:** 435 Backend/API، 161 Next.js Web، 57 Flutter، 30 QA، 23 Docs/Product، 1 Ops، بالإضافة إلى 33 Epic.

### تعيين Flutter

تم التحقق من المستخدم `Ahmed Mamdouh El- Sayed` داخل Jira. حسابه الداخلي: `70121:24ce7639-fa05-4a15-b940-290557ac3fcd`.

[فلتر مهام Flutter](https://mykholy.atlassian.net/issues/?jql=project%20%3D%20USYD%20AND%20labels%20%3D%20flutter)

### معالجة التكرارات

هناك خمسة عناصر إضافية أُنشئت خلال إعادة محاولة الاستيراد؛ كل منها تم تعليمه كنسخة مكررة، وربطه بالأصل بعلاقة Duplicate، ونقله إلى Done، مع إزالة `usayd-spec-handoff` من النسخة الزائدة حتى لا يدخل ضمن Backlog العمل:

| الأصل المعتمد | النسخة المكررة المغلقة |
|---|---|
| USYD-540 | USYD-545 |
| USYD-541 | USYD-546 |
| USYD-542 | USYD-547 |
| USYD-543 | USYD-548 |
| USYD-544 | USYD-549 |

### حالة الـSprints

الـBoard الحالي `UP board` رقم `1` هو Team-managed Kanban **ولا يدعم Sprints فعلية**؛ أكدت Jira ذلك برسالة `The board does not support sprints`. كل تذكرة تحمل label من نوع `planned-s00` ... حسب خطة التوزيع، لكن لم يتم إنشاء 91 Sprint داخل Jira. يلزم إنشاء/تفعيل Scrum Board مناسب قبل تشغيل سبرنتات Jira الفعلية.

### حدود التحقق

تحققت فعليًا من **العدد، جميع المصادر المرجعية في ملف الـCSV، التغطية، وجود Epic Parent لكل مهمة، تصنيف Flutter وتعيينه، وإغلاق التكرارات الخمسة**. لم أختبر الكود أو كل Acceptance Criterion لكل تذكرة؛ هذه اختبارات تنفيذية تخص PRs والـCI لاحقًا. كما أن تقديرات Story Points في ملف التخطيط لم تُنقل تلقائيًا إلى حقول Jira المخصصة بعد؛ ظلت في الملف والمراجع. علاقات Dependencies مكتوبة داخل وصف المهمة لكنها لم تُحوّل كلها بعد إلى Jira issue links. لا نعد هذه الأشياء منجزة.

### استعلامات Jira المفيدة

- [Backlog المعتمد فقط](https://mykholy.atlassian.net/issues/?jql=project%20%3D%20USYD%20AND%20labels%20%3D%20usayd-spec-handoff)
- [Epics](https://mykholy.atlassian.net/issues/?jql=project%20%3D%20USYD%20AND%20issuetype%20%3D%20Epic)
- [Flutter](https://mykholy.atlassian.net/issues/?jql=project%20%3D%20USYD%20AND%20labels%20%3D%20flutter)
- [التكرارات المغلقة](https://mykholy.atlassian.net/issues/?jql=project%20%3D%20USYD%20AND%20labels%20%3D%20duplicate-ignore)

## ملفات التسليم

- `USAYD_JIRA_CANONICAL_TASK_MAPPING_2026-11-24.json`: مصدر مستقر قابل للقراءة بالآلة لتحويل `USYD-TXXXX` إلى رقم Jira الفعلي.
- `USAYD_JIRA_CANONICAL_TASK_MAPPING_2026-11-24.csv`: نفس الخريطة كجدول للمراجعة.

**هام:** لا تفترض أن `USYD-T0023` يعادل Issue Key في Jira؛ استخدم ملف الربط. مثال: `USYD-T0023` هو `USYD-56` في Jira.
