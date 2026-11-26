# Jira Cloud — استيراد ومزامنة آمنة

**الحالة الحية:** اتصال Atlassian للمستخدم يعرض مورد `mykholy.atlassian.net` بصلاحية read-write، لكن listJiraProjects/listJiraBoards/JQL رجعت `404 Site temporarily unavailable` وقت التنفيذ. **لم تتم كتابة أي Epic/Sprint/Issue**. لا تصف هذه الحزمة بأنها مرفوعة على Jira.

## الإعداد
1. تأكد من وجود Jira Software Scrum Project مناسب، اسم `Usayd Academy`, Key مقترح `USAYD`، مع Board Scrum. لا تنشئ مشروعًا مكررًا إن كان موجودًا.
2. استخدم المسؤولية والإذن لإضافة `Epic`, `Story`, `Task`, وربط Parent، وإنشاء Sprint.
3. أنشئ الحقول `Repository` و`External Stable ID` اختياريًا، أو استخدم Labels المُعدّة.
4. **الطريقة الأكثر موثوقية:** شغّل `jira/jira_sync.py` في بيئة مؤهلة لها `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY` (و `JIRA_BOARD_ID` لإنشاء Sprints). المشروع يجب أن يكون موجودًا؛ السكربت يستخدم Jira REST API ويتأكد من كل نتيجة قبل المتابعة.
5. **بديل CSV:** `JIRA_IMPORT_EPICS.csv` ثم `JIRA_IMPORT_WORK_ITEMS.csv`. المابنج: Issue Type, Summary, Description, Labels, Priority. حقول External_ID وParent_External_ID وCandidate_Sprint بيانات مساعدة **وليست Jira standard fields**؛ لا تعينها إلى حقول غير موجودة. بعد الاستيراد استخدم `MASTER_BACKLOG.csv` لتعيين العلاقات يدويًا أو Sync script. أسماء Candidate Sprint ليست Jira IDs.
6. أنشئ Candidate Sprints فقط بعد مراجعة القدرة، ثم راجع Status وAssignee وBlocked Decisions مع الفريق. تجنب إنشاء عشرات السبرنتات النشطة دفعة واحدة.

## منع التكرار
Stable IDs مثل `USYD-T0001` في Summary وLabels. Query/search before create؛ حفظ نتيجة Jira key/issue id في `.jira_sync_state.json`. السكربت لا يعمل Merge ولا يغير statuses إلى Done تلقائيًا.
