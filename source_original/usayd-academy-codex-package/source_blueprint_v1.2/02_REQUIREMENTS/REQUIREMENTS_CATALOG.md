# Functional requirement catalog

All requirements are specifications, **not implemented features**. Each requirement must map to Jira issue, endpoint/UI where applicable, tests and UAT evidence.

| ID | Module | Requirement | Detailed behavior | Persona | Phase | Priority |
|---|---|---|---|---|---|---|
| FR-IAM-001 | IAM | تسجيل متعلم موحد | بريد أو هاتف مع تحقق؛ لا يفرض حساب ولي أمر أو اختيار طفل/بالغ كنوع حساب؛ الحد من البيانات الأولية. | student,admin | P0 | Must |
| FR-IAM-002 | IAM | تحديد السن والبلد | سؤال السن/تاريخ الميلاد بالقدر اللازم للضوابط والمنطقة الزمنية والقوانين، ولا يسمح بتغيير سن محمي دون تحقق. | student,admin | P0 | Must |
| FR-IAM-003 | IAM | الدخول واستعادة الحساب | Rate limits، انتهاء رموز OTP، إبطال الجلسات القديمة، إثبات تغيير وسيلة التواصل. | student,admin | P0 | Must |
| FR-IAM-004 | IAM | RBAC/ABAC | learner, teacher, supervisor, support, finance, admin وguardian-link لاحق؛ التحقق من الدور والملكية على كل مورد. | student,admin | P0 | Must |
| FR-IAM-005 | IAM | MFA للموظفين | إلزام MFA للأدوار الإدارية والمالية والتقارير الحساسة؛ دعم Recovery Codes وإبطالها. | student,admin | P0 | Must |
| FR-IAM-006 | IAM | Consent ledger | حفظ نوع الموافقة ونسخة النص والتوقيت ومن أعطاها ومصدرها والسحب؛ فصل تشغيل الحصة عن تحليل الصوت والتسويق. | student,admin | P0 | Must |
| FR-IAM-007 | IAM | Guardian approval gate | للطلاب القُصّر، حفظ اتصال ولي الأمر والموافقة والتحقق قبل تشغيل التعلم المدفوع أو المعالجة المقيدة؛ واجهة ولي أمر كاملة لاحقًا. | student,admin | P0 | Must |
| FR-IAM-008 | IAM | قيود الجلسات والأجهزة | مراجعة الأجهزة وإبطال الرموز والحد المرن للأجهزة المتزامنة دون حظر تعسفي أثناء الحصة. | student,admin | P0 | Must |
| FR-IAM-009 | IAM | تصدير/حذف البيانات | طلبات الوصول والتصحيح والمحو وفق المدد والمتطلبات القانونية وحماية سجلات المحاسبة اللازمة. | student,admin | P0 | Must |
| FR-IAM-010 | IAM | إدارة اللغات | اختيار ar/en RTL/LTR مع ترجمة أخطاء التحقق والإشعارات ونسخة نصوص السياسات. | student,admin | P0 | Must |
| FR-PROF-001 | PROF | ملف متعلم مستقل | هدفه التعليمي ومستواه وتفضيلاته وجداول الوقت والرواية والمنهج دون ربط إلزامي بوالد. | student,admin | P0 | Must |
| FR-PROF-002 | PROF | أهداف تعلم متعددة | حفظ، مراجعة، تلاوة، تجويد، تأسيس قراءة مع هدف أساسي وقيود وقت. | student,admin | P0 | Must |
| FR-PROF-003 | PROF | المنطقة الزمنية | عرض جميع المواعيد بالتوقيت المحلي مع حفظ UTC وIANA zone ومعالجة DST. | student,admin | P0 | Must |
| FR-PROF-004 | PROF | تاريخ الطالب | عرض الاشتراكات والخطط والتقييمات وإجمالي التعلم والانتقالات بين المعلمين. | student,admin | P0 | Must |
| FR-PROF-005 | PROF | ملف الولاية المستقبلي | علاقة learner_guardian وموافقة مستقلة، قابلة للتفعيل لاحقًا دون تعديل هوية الطالب. | student,admin | P0 | Must |
| FR-PROF-006 | PROF | المفضلة والتفضيلات | جنس المعلم إذا طلبه المستخدم، لغة التدريس، وقت مناسب، وسهولة وصول دون إظهار بيانات حساسة. | student,admin | P0 | Must |
| FR-CURR-001 | CURR | كتالوج البرامج | مسارات وأهداف ومستويات ومتطلبات بدء ورسوم ومخرجات تعليم واضحة. | student,admin | P0 | Must |
| FR-CURR-002 | CURR | مناهج بنسخ | نسخ مناهج معتمدة وقابلة للأرشفة مع سجل إصدارات؛ لا يعدّل تاريخ تقييمات سابقة. | student,admin | P0 | Must |
| FR-CURR-003 | CURR | مصدر نص القرآن | عزل QuranTextProvider والتحقق من المصدر/الرواية وتراخيص الاستخدام؛ لا ينشئ AI نصًا قرآنيًا مرجعيًا. | student,admin | P0 | Must |
| FR-CURR-004 | CURR | ربط المقاطع | إسناد أهداف حفظ ومراجعة إلى آيات ومقاطع دقيقة بحدود سورة/آية/رواية. | student,admin | P0 | Must |
| FR-CURR-005 | CURR | دروس مسجلة | مواد مرخصة ومتصلة ببرنامج/مستوى، إتاحة مشروطة بالاشتراك مع وصلات مؤقتة. | student,admin | P0 | Must |
| FR-CURR-006 | CURR | إدارة الاختبارات التعليمية | Question bank من مؤلفين مؤهلين مع نسخ وتصنيفات ومستويات وحلول معتمدة. | student,admin | P0 | Must |
| FR-TCHR-001 | TCHR | تسجيل واستقدام المعلمين | طلب/وثائق/تحقق هوية ومؤهلات ومراجع واختبار تدريس ومراجعة حماية القاصرين. | teacher,admin | P0 | Must |
| FR-TCHR-002 | TCHR | ملف المعلم | مجالات تدريس، لغات، روايات معتمدة، جمهور مناسب، نبذة قابلة للعرض وموافقة نشر. | teacher,admin | P0 | Must |
| FR-TCHR-003 | TCHR | توافر متكرر | تقويم أسبوعي واستثناءات وإجازات وbuffers ومناطق زمنية. | teacher,admin | P0 | Must |
| FR-TCHR-004 | TCHR | مطابقة الطالب بالمعلم | قواعد مستوي/منهج/لغة/وقت/جودة والتوزيع اليدوي مع توضيح سبب الاختيار. | teacher,admin | P0 | Must |
| FR-TCHR-005 | TCHR | حالة التوظيف | candidate, approved, active, suspended, offboarded وإبطال الوصول الفوري عند الإيقاف. | teacher,admin | P0 | Must |
| FR-TCHR-006 | TCHR | تبديل المعلم | نقل الخطة والمهام والتقارير مع تنبيه الأطراف وحفظ تاريخ الملكية. | teacher,admin | P0 | Must |
| FR-TCHR-007 | TCHR | تقييمات الأداء | معدل حضور وتقارير مصدق عليها وشكاوى وجودة بدون ترتيب مجهول أو عقوبات آلية. | teacher,admin | P0 | Must |
| FR-BOOK-001 | BOOK | إنشاء حصة محجوزة | ربط الاشتراك والرصيد والمعلم والزمن والغرفة، والتحقق من التعارض بشكل transactional. | student,teacher,admin | P0 | Must |
| FR-BOOK-002 | BOOK | حجز تقييم مجاني | سقف حجز عادل وتأكيد قناة الاتصال وAnti-bot وقائمة انتظار. | student,teacher,admin | P0 | Must |
| FR-BOOK-003 | BOOK | حجز متكرر | 8/12/16 حصة أو خطة حسب الباقة مع منع ازدواج حجز المعلم. | student,teacher,admin | P0 | Must |
| FR-BOOK-004 | BOOK | تعديل الحصة | سياسة نافذة زمنية وموافقة المعلم وحفظ تاريخ التعديلات وإعادة تخصيص الرصيد. | student,teacher,admin | P0 | Must |
| FR-BOOK-005 | BOOK | غياب/تعويض | سياسات منفصلة لغياب المعلم والطالب والمشاكل التقنية وطوارئ وإثبات الحالات. | student,teacher,admin | P0 | Must |
| FR-BOOK-006 | BOOK | قائمة انتظار | عرض مواعيد جديدة حسب أسبقية واضحة دون كشف بيانات بقية المتعلمين. | student,teacher,admin | P0 | Must |
| FR-BOOK-007 | BOOK | مناطق زمنية وDST | جميع الحجوزات UTC، مع IANA IDs وحفظ وقت الحجز الأصلي وDST safe scheduling. | student,teacher,admin | P0 | Must |
| FR-BOOK-008 | BOOK | تعارض مقدمي الفيديو | تسجيل ارتباط كل حصة بمزود محدد والمواعيد دون ازدواج provider session. | student,teacher,admin | P0 | Must |
| FR-PAY-001 | PAY | كتالوج الباقات | مدة الحصة وعددها وسعر عملة/دولة وVAT إن انطبق وسياسة التجديد. | student,finance,admin | P0 | Must |
| FR-PAY-002 | PAY | إنشاء اشتراك | اختيار باقة مع تحديد entitlement/الحصص ومواعيد الاستحقاق دون تفعيل قبل تأكيد دفع. | student,finance,admin | P0 | Must |
| FR-PAY-003 | PAY | دفع دولي ومحلي | PaymentProvider abstraction للعملات وطرق الدفع والموافقات وإدارة التسوية. | student,finance,admin | P0 | Must |
| FR-PAY-004 | PAY | Webhooks الدفع | توقيع صحيح وidempotency ومعالجة retries/out of order دون تكرار تفعيل. | student,finance,admin | P0 | Must |
| FR-PAY-005 | PAY | استرداد واستقطاع | طلبات refund وحصص مستخدمة وكوبونات وسجلات سبب/موافقة وتقارير مالية. | student,finance,admin | P0 | Must |
| FR-PAY-006 | PAY | تجديد وتذكير | إشعارات متدرجة وتجنب التجديد التلقائي إلا بموافقة ومزوّد مدعوم. | student,finance,admin | P0 | Must |
| FR-PAY-007 | PAY | فوترة وتقارير | فاتورة وإيصال مرتبطان بكل دفع وإرجاع وخصم؛ معالجة الضرائب بحسب الكيان. | student,finance,admin | P0 | Must |
| FR-PAY-008 | PAY | محفظة الرصيد | حالة credited/reserved/consumed/returned/expired مع منع الرصيد السالب. | student,finance,admin | P0 | Must |
| FR-VIDEO-001 | VIDEO | Provider Registry | تعريف GoogleMeet/ZoomMeeting/ZoomVideoSDK/VideoSDK/LiveKit/Daily مع credentials وآلية الاختيار. | student,teacher,admin | P0 | Must |
| FR-VIDEO-002 | VIDEO | Capabilities | Matrix مخزنة لكل Provider: embed, raw_audio, attendance, recording, screen_share, breakout, transcripts, moderation, mobile. | student,teacher,admin | P0 | Must |
| FR-VIDEO-003 | VIDEO | اختيار المزود | تحديد لكل برنامج/حصة/منطقة مع fallback فقط قبل بدء الحصة أو بإجراء إعادة جدولة واضح. | student,teacher,admin | P0 | Must |
| FR-VIDEO-004 | VIDEO | الدخول الآمن | توليد token/meeting redirect مقيّد بالحصة والهوية والإذن وفق ما يدعمه المزود؛ لا تفترض أن الرابط وحده يمنع المشاركة. | student,teacher,admin | P0 | Must |
| FR-VIDEO-005 | VIDEO | أحداث الحضور | استقبال signed webhook والتوفيق مع client heartbeat؛ تعطيل استنتاج الحضور من صفحة frontend وحدها. | student,teacher,admin | P0 | Must |
| FR-VIDEO-006 | VIDEO | واجهة فصل متكاملة | مصحف مشترك/ملاحظات/تقييم داخل المنصة، حتى لو الفيديو في نافذة خارجية. | student,teacher,admin | P0 | Must |
| FR-VIDEO-007 | VIDEO | إنهاء وقطع الاتصال | حالات connecting/active/reconnecting/ended/failed، وتسجيل الأعطال وسياسة التعويض. | student,teacher,admin | P0 | Must |
| FR-VIDEO-008 | VIDEO | ضبط التسجيل | سياستها off by default، موافقات منفصلة، إشعارات داخل الحصة، مدة الاحتفاظ والأذونات. | student,teacher,admin | P0 | Must |
| FR-VIDEO-009 | VIDEO | تقييد دردشة الغرفة | عزل رسائل المستخدمين داخل المنصة حيث تدعمه SDKs وإظهار القيود بوضوح في Meet/Zoom. | student,teacher,admin | P0 | Must |
| FR-VIDEO-010 | VIDEO | فشل المزود | Fallback/incident playbook يمنع تفريغ بيانات أو فرض مزايا غير مدعومة. | student,teacher,admin | P0 | Must |
| FR-ATT-001 | ATT | حساب وقت الحضور | ضم join/leave/reconnect chunks من provider events وفق قواعد واضحة ومنع التكرار. | teacher,admin | P0 | Must |
| FR-ATT-002 | ATT | تأكيد إكمال الحصة | تحديد الحد الأدنى وزمن التأخير ونهاية الحصة وتأكيد نزاعات الحضور. | teacher,admin | P0 | Must |
| FR-ATT-003 | ATT | تحضير تقرير الحصة | لا يُقفل التقرير إلا بعد اختيار هدف/مراجعة/واجب ونتيجة أو توضيح سبب الغياب. | teacher,admin | P0 | Must |
| FR-ATT-004 | ATT | مراجعة جودة | سجلات تشغيل ومؤشرات دون تسجيل صوت تلقائي. | teacher,admin | P0 | Must |
| FR-ATT-005 | ATT | سجل التعويض | هل الحصة تعوض ولماذا ومن اعتمد، ومن يتحمل تكلفة المعلم. | teacher,admin | P0 | Must |
| FR-ASMT-001 | ASMT | تقييم دخول | نموذج rubric متغير حسب program/level يشمل قراءة/تلاوة/حفظ/مراجعة. | student,teacher,supervisor | P1 | Must |
| FR-ASMT-002 | ASMT | درجات بإثبات | المعلم يحفظ قياسات بنطاق 0–4 أو وصف؛ تأكيد البيانات وإحالة الشكوى. | student,teacher,supervisor | P1 | Must |
| FR-ASMT-003 | ASMT | اختبارات تكيفية | اختيار مقاطع وأسئلة من بنك معتمد مع مراعاة مواطن الضعف والتدرج. | student,teacher,supervisor | P1 | Must |
| FR-ASMT-004 | ASMT | اختبار شفهي مباشر | حجز اختبار live مع معلم ومخطط rubric ونتيجة بقرار المقيم. | student,teacher,supervisor | P1 | Must |
| FR-ASMT-005 | ASMT | اختبار كتابي وتفاعلي | أنماط اختيار/ترتيب/تحديد كلمات وفق الحقوق والنص المعتمد دون نشر أسئلة خاطئة. | student,teacher,supervisor | P1 | Must |
| FR-ASMT-006 | ASMT | إعادة اختبار | سياسات إعادة المحاولة ومنع تغيير النتائج المعتمدة وتحديد حالات التظلم. | student,teacher,supervisor | P1 | Must |
| FR-ASMT-007 | ASMT | اعتماد النتائج | حالات draft, pending_review, published, appealed, corrected، مع Audit. | student,teacher,supervisor | P1 | Must |
| FR-ASMT-008 | ASMT | لوحة نقاط الضعف | تجميع أخطاء مصنفة عبر اختبارات وحصص مع تجنب الاستنتاجات غير المؤكدة. | student,teacher,supervisor | P1 | Must |
| FR-PLAN-001 | PLAN | خطة أولية | بناء خطة من نتائج تقييم معتمد وأهداف الطالب ووقت الدراسة المتاح. | student,teacher,supervisor | P1 | Must |
| FR-PLAN-002 | PLAN | إصدارات الخطط | Draft → Teacher Review → Approved → Active → Superseded مع إمكان الرجوع. | student,teacher,supervisor | P1 | Must |
| FR-PLAN-003 | PLAN | خطة يومية | مهام قصيرة للحفظ والمراجعة والتمرين وتحديد وقت مناسب دون ضغط سلبي. | student,teacher,supervisor | P1 | Must |
| FR-PLAN-004 | PLAN | مراجعات متباعدة | حساب due dates حسب آخر إتقان ونتيجة اختبار وسجل النسيان، مع overrides. | student,teacher,supervisor | P1 | Must |
| FR-PLAN-005 | PLAN | تعديل وفق الضعف | اقتراح تخفيف حفظ أو زيادة مراجعة بعد اختبار انخفاض الأداء ثم اعتماد. | student,teacher,supervisor | P1 | Must |
| FR-PLAN-006 | PLAN | استرجاع بعد الانقطاع | Recovery plan يعيد تقييم مستوى الاسترجاع قبل فرض حمل سابق. | student,teacher,supervisor | P1 | Must |
| FR-PLAN-007 | PLAN | خريطة الحفظ | حالات لكل مقطع برواية/منهج، آخر اختبار وموعد مراجعة ونسبة مبنية على rubric. | student,teacher,supervisor | P1 | Must |
| FR-PLAN-008 | PLAN | تتبع عادات متوازن | متابعة المهام والإنجاز دون فرض عقوبات على الانقطاع أو تضخيم streak. | student,teacher,supervisor | P1 | Must |
| FR-CONTEST-001 | CONTEST | مُنشئ مسابقات | عنوان، هدف، نوع (حفظ/مراجعة/تجويد/اختبار معلومات)، نطاق، فترة، لغة، مستوى، أهلية. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-002 | CONTEST | أهلية حسب المستوى | الانضمام بعد ضوابط السن والمستوى والاشتراك والموافقات وقرارات الإدارة. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-003 | CONTEST | مسابقة فردية | تسميع مباشر أو مهمة تقييم مع rubric موحد وأداة اختيار محكم. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-004 | CONTEST | مسابقة جماعية | فرق اختيارية ومشاركات محكومة ومعايير واضحة تمنع التمييز غير العادل. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-005 | CONTEST | مسابقات دورية | أسبوعية/شهرية/رمضان أو دورة زمنية مع جدول إغلاق وتسجيل واعتماد. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-006 | CONTEST | بنك أسئلة المسابقات | أسئلة ذات مصادر معتمدة وإصدارات ومراجعة بشرية قبل النشر. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-007 | CONTEST | تقييم عادل | وزن صحة الحفظ والتجويد والمراجعة والالتزام حسب النوع، دون تحويل حجم النشاط لدرجة جودة. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-008 | CONTEST | تحكيم بشري | حالات submitted→evaluating→reviewed→final مع مراجعة ثانية للعروض النهائية. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-009 | CONTEST | Leaderboard منضبط | عرض opt-in أو أسماء مستعارة؛ لا قائمة عامة للقاصرين، ومرشحات مستويات منع ظلم المبتدئين. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-010 | CONTEST | جوائز وضوابط | جوائز تعليمية غير عشوائية غير مراهنات مع شروط معلنة ومراجعة قانونية للجوائز المادية. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-011 | CONTEST | التظلمات | نافذة اعتراض ورفع الأدلة وتعيين محكم مستقل وسجل إعادة التقييم. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-012 | CONTEST | مكافحة الغش | قواعد attempts وdevice patterns والنسخ وحالات flag دون اتهام تلقائي. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-013 | CONTEST | شارات الإنجاز | شارات داخلية توثق milestones، وليست شهادات اعتماد أو إجازة. | student,teacher,supervisor,admin | P1 | Must |
| FR-CONTEST-014 | CONTEST | مسابقات بلا دفع إضافي إلزامي | عدم ربط فرص الفوز بشراء محاولات إضافية أو رسوم ترفع فرص الفوز. | student,teacher,supervisor,admin | P1 | Must |
| FR-AI-001 | AI | AI Gateway | مزودات متعددة وميزانية tokens/minutes وtimeouts وfallback ومراقبة تكلفة. | student,teacher,admin | P1 | Must |
| FR-AI-002 | AI | منع توليد آيات مرجعية | الآيات من QuranTextProvider verified؛ AI يقتبس references فقط دون إعادة صياغة المصدر. | student,teacher,admin | P1 | Must |
| FR-AI-003 | AI | خطة مقترحة | Structured JSON مع evidence_ids من تقييم موثق؛ pending teacher approval. | student,teacher,admin | P1 | Must |
| FR-AI-004 | AI | تشخيص نقاط ضعف | ربط الاختبار/تقييم المعلم/مهمة مراجعة بنقطة ضعف مع مؤشر مصدر وحداثة. | student,teacher,admin | P1 | Must |
| FR-AI-005 | AI | اختيار أسئلة ذكية | AI يختار من بنك معتمد ولا ينشر سؤالًا مولدًا جديدًا بدون مراجعة. | student,teacher,admin | P1 | Must |
| FR-AI-006 | AI | ملخص حصة | اقتراح ملخص من بيانات منظمة أو نص مصرح به؛ اعتماد المعلم قبل النشر. | student,teacher,admin | P1 | Must |
| FR-AI-007 | AI | مساعد يومي | يجيب من بيانات الطالب المصرح بها بخطة مهام محددة ويقر بعدم المعرفة. | student,teacher,admin | P1 | Must |
| FR-AI-008 | AI | تحليل مخالفات محتملة | من تفريغ مصرح به؛ flags مع evidence snippets وhuman decision فقط. | student,teacher,admin | P1 | Must |
| FR-AI-009 | AI | Diarization وتلاوة | فصل المتحدثين وتمييز recitation/conversation قدر الإمكان مع وسم عدم اليقين. | student,teacher,admin | P1 | Must |
| FR-AI-010 | AI | مساعد معلم | ملخص سابق وrubric مقترح وأخطاء معتمدة دون تغييرات صامتة. | student,teacher,admin | P1 | Must |
| FR-AI-011 | AI | تسميع مستقل تجريبي | نماذج تخصصية بتقييم دقة على لهجات وفئات مختلفة؛ تظهر عبارة خطأ محتمل فقط. | student,teacher,admin | P1 | Must |
| FR-AI-012 | AI | حوكمة نماذج | Model registry، prompt versions، تقييمات offline، rollback، اعتراض وتصحيح وdelete. | student,teacher,admin | P1 | Must |
| FR-MEDIA-001 | MEDIA | مكتبة مسجلة | محاضرات وفيديوهات وتمارين وملفات تتبع الترخيص والمراجعة. | student,admin | P1 | Must |
| FR-MEDIA-002 | MEDIA | حماية المحتوى | Signed access وdomain restriction والحد من التوزيع؛ عدم ادعاء منع تسجيل الشاشة. | student,admin | P1 | Must |
| FR-MEDIA-003 | MEDIA | ملاحظات ومرفقات | رفع محدود وMalware scanning وsize limits ومنع تبادل بيانات شخصية غير لازمة. | student,admin | P1 | Must |
| FR-MEDIA-004 | MEDIA | حماية صوت الطالب | تسجيل ممارسة اختياري بموافقة وحذف تلقائي وقيود الوصول. | student,admin | P1 | Must |
| FR-MEDIA-005 | MEDIA | إتاحة تعلم منخفضة البيانات | تشغيل صوتي، جودة متكيّفة، استكمال، تنبيه لحجم استهلاك الشبكة. | student,admin | P1 | Must |
| FR-PAYROLL-001 | PAYROLL | عقد تعويض بنسخة | تعويض راتب/حصة/ساعة/شيفت/هجين مع تواريخ سريان واعتمادات لا تعيد حساب الماضي. | teacher,finance,admin | P0 | Must |
| FR-PAYROLL-002 | PAYROLL | حساب استحقاق حصة | completed / absent teacher / absent learner / technical failure مع rules محددة. | teacher,finance,admin | P0 | Must |
| FR-PAYROLL-003 | PAYROLL | احتساب الساعة | وقت حضور فعلي بحدود rounding وقواعد انتظار وسياسة ساعات الحد الأدنى. | teacher,finance,admin | P0 | Must |
| FR-PAYROLL-004 | PAYROLL | احتساب الشيفت | حجز block ساعات وفترات راحة وطاقة قصوى ومدفوعات حسب التعاقد. | teacher,finance,admin | P0 | Must |
| FR-PAYROLL-005 | PAYROLL | مرتب ثابت وحوافز | راتب دوري، overtime، حافز جودة، خصومات قانونية فقط، حوافز قابلة للتدقيق. | teacher,finance,admin | P0 | Must |
| FR-PAYROLL-006 | PAYROLL | Hybrid compensation | base + per completed lesson + caps + guaranteed minimum; settlement versioned. | teacher,finance,admin | P0 | Must |
| FR-PAYROLL-007 | PAYROLL | الحد الأدنى والامتثال | تحقق يدوي قانوني من أجور وتكاليف موظف/متعاقد حسب الولاية؛ منع تشغيل rule غير مُراجع. | teacher,finance,admin | P0 | Must |
| FR-PAYROLL-008 | PAYROLL | إقفال مستحقات | draft→reviewed→approved→paid→reconciled مع approver dual control. | teacher,finance,admin | P0 | Must |
| FR-PAYROLL-009 | PAYROLL | كشوف نزاعات | تظلم المعلم على حصة/تعويض وقرار موثق وسجل audit. | teacher,finance,admin | P0 | Must |
| FR-CRM-001 | CRM | Leads متعدد القنوات | source/medium/campaign/utm وdedup وconsent وowner/status. | sales,admin | P0 | Must |
| FR-CRM-002 | CRM | Trial pipeline | New→Contacted→Qualified→Scheduled→Attended→Paid/Lost مع أسباب وإجراءات متابعة. | sales,admin | P0 | Must |
| FR-CRM-003 | CRM | إحالات | Referral code وبونص بعد الدفع والتجديد وفق سقف منع إساءة استخدام. | sales,admin | P0 | Must |
| FR-CRM-004 | CRM | قمع التحويل | Lead→Trial→Attended→Paid→Renewed مع cohorts فصل مصر والخليج. | sales,admin | P0 | Must |
| FR-CRM-005 | CRM | اتصالات موافقة | فصل رسائل الخدمة عن التسويق وإدارة unsubscribe وموافقة WhatsApp. | sales,admin | P0 | Must |
| FR-CRM-006 | CRM | استرداد المنسحبين | Win-back حذر مع اختيار عدم التذكير وحماية الخصوصية. | sales,admin | P0 | Must |
| FR-NOTIF-001 | NOTIF | قوالب رسائل | email/SMS/WhatsApp/push حسب القناة ولغة الطالب ونوعه وموافقته. | student,admin | P0 | Must |
| FR-NOTIF-002 | NOTIF | تذكيرات الحصص | 24h/1h وقبل البداية مع timezone وdedupe. | student,admin | P0 | Must |
| FR-NOTIF-003 | NOTIF | إشعارات الخطة | مراجعة مستحقة وخطة معتمدة ونتيجة اختبار وتعويض حصة. | student,admin | P0 | Must |
| FR-NOTIF-004 | NOTIF | قناة سلامة طارئة | إشعار متدرج للفريق المخول منفصل عن قنوات التسويق. | student,admin | P0 | Must |
| FR-ADMIN-001 | ADMIN | مؤشرات تشغيل | عدد طلاب نشطين/حضور/إشغال/الإلغاءات/الإيراد/المستحقات/الحوادث. | admin,supervisor,support,finance | P0 | Must |
| FR-ADMIN-002 | ADMIN | صلاحيات متعددة | support وacademic وfinance وmoderation مع أقل صلاحيات. | admin,supervisor,support,finance | P0 | Must |
| FR-ADMIN-003 | ADMIN | تشغيل المسابقات | إنشاء ومراجعة ومحكمون ونتائج واعتراضات واستثناءات. | admin,supervisor,support,finance | P0 | Must |
| FR-ADMIN-004 | ADMIN | تغيير الإعدادات | Feature flags وrevision log وdual approval للأمور المالية الحساسة. | admin,supervisor,support,finance | P0 | Must |
| FR-ADMIN-005 | ADMIN | تصدير بيانات آمن | تصفية حسب الصلاحيات وwatermark وتسجيل من صدّر ومتى. | admin,supervisor,support,finance | P0 | Must |
| FR-ADMIN-006 | ADMIN | إدارة النزاعات | تذاكر دعم وفصل من اتخذ قرارًا عن صاحب الشكوى إذا تطلب الأمر. | admin,supervisor,support,finance | P0 | Must |
| FR-ADMIN-007 | ADMIN | مراجعة الجودة | مؤشرات وأخذ عينات مطابقة للموافقات ومراجعة أداء المعلمين. | admin,supervisor,support,finance | P0 | Must |
| FR-ADMIN-008 | ADMIN | لوحة AI | تكلفة/دقة/false positives/queue وقرار تشغيل أو إيقاف نموذج. | admin,supervisor,support,finance | P0 | Must |
| FR-ADMIN-009 | ADMIN | جداول الدول والعملات | أسعار حسب السوق، ميزانيات وسياسات محلية، بدون تسعير خفي مخالف. | admin,supervisor,support,finance | P0 | Must |
| FR-MOB-001 | MOB | واجهات Flutter | نفس API v1؛ navigation/auth/lesson/plan/contest يعمل على Android/iOS. | student,teacher | P2 | Must |
| FR-MOB-002 | MOB | العودة للحصة | handling background/foreground/audio interruptions/network and call state. | student,teacher | P2 | Must |
| FR-MOB-003 | MOB | إشعارات Push | push tokens per device وdeep links آمنة مع تعطيل عند تسجيل الخروج. | student,teacher | P2 | Must |
| FR-MOB-004 | MOB | Offline study cache | تخزين مهام غير حساسة ومصحف ضمن الرخص والتزامن دون تسريب تسجيلات. | student,teacher | P2 | Must |
| FR-MOB-005 | MOB | أحجام ومقاسات | mobile layout RTL/LTR وscreen readers واستجابات الأجهزة منخفضة الأداء. | student,teacher | P2 | Must |
| FR-SEC-001 | SEC | Tenant/ownership isolation | أي learner/teacher/lesson IDs تتحقق server-side من الملكية؛ اختبار BOLA. | engineer,admin | P0 | Must |
| FR-SEC-002 | SEC | Object storage policy | private buckets وsigned URL TTL وlogs وserver-side encryption. | engineer,admin | P0 | Must |
| FR-SEC-003 | SEC | Abuse/rate limits | محددات API وOTP وtrial وAI وcompetition attempts ومعدلات رفع الملف. | engineer,admin | P0 | Must |
| FR-SEC-004 | SEC | Audit logging | immutable events للتغييرات المالية/التحكيم/الموافقات/إصدار tokens. | engineer,admin | P0 | Must |
| FR-SEC-005 | SEC | Data retention | سياسة زمنية حسب نوع البيانات والمحضر القانوني مع purge jobs واختبارات حذف. | engineer,admin | P0 | Must |
| FR-SEC-006 | SEC | Secrets management | عدم وضع API/SDK secrets في الويب أو الموبايل والسرية الدورية. | engineer,admin | P0 | Must |
| FR-SEC-007 | SEC | Monitoring & incident | observability, alerts, on-call, backup restore drills and incident playbooks. | engineer,admin | P0 | Must |
| FR-SEC-008 | SEC | Threat model | Threats للنماذج الصوتية والـAI والمسابقة والبيانات والقُصّر واستجابة موثقة. | engineer,admin | P0 | Must |
