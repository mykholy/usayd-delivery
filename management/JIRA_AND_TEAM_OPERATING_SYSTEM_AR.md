# نظام إدارة الفريق وجيرا — أُسَيْد

- Scrum Project واحد `USAYD`، 3 Components/Labels `api`, `web`, `flutter` مع `product`, `qa`, `devops`.
- شخص 1 Full Stack (Laravel + MySQL + Next.js + PR/CI review); شخص 2 Flutter (Dart + integration + mobile releases). لا يوجد QA مستقل؛ يجب تخصيص وقت للاختبارات والمراجعة والقرارات.
- Sprint أسبوعين؛ Planning في البداية، stand-up يومي 10 دقائق، backlog refinement أسبوعيًا، Demo + Retro عند نهاية كل Sprint.
- لكل مهمة Stable ID من `planning/tasks`. سجل Pull Request، test evidence، screenshot أو migration، وحالة الحجب. لا تستخدم "Done" قبل merge+verification.
- يجب عمل Feature Flag لكل من O-01..O-10 و D-series غير المعتمدة حيث يؤثر على السلوك. المالك وحده يعتمد سياسة القاصرين، الحقوق، الأسعار والرواتب.
- Jira fields: Epic, Type, Priority, Labels, Components/Repository, Story Points (تقديرية)، Candidate Sprint (لا تكتب نصًا في حقل Sprint ID), Dependencies.
- في حال غياب project/board/capabilities في Jira لا تدعي الإنشاء؛ استخدم CSV أو `jira_sync.py` بعد تجهيز API token وتفعيل المشروع.
- إخفاق CI: أصلح في نفس Branch/PR وأعد التشغيل؛ لا تعمل Merge مشروط على أساس نتيجـة متوقعة.
