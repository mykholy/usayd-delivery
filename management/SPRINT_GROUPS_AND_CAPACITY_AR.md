# تقسيم الـ91 Candidate Sprint إلى برامج تنفيذ

> الرقم 91 يعبّر عن جدولة تقديرية مبنية على تفاصيل تذاكر كثيرة لفريق شخصين، وليس التزامًا زمنيًا أو سبرنتات منشأة في Jira. الاحتفاظ بكل تذكرة ضروري للتتبع؛ عند التشغيل سيتم تجميع التسليم في Releases وRoadmap مرنة، وتأكيد S00 ثم S01 فقط.

## Sprint 0–2 — تأسيس

إعداد المستودعات الثلاثة، MySQL 8.4، Redis، Laravel، Next.js، Flutter، إدارة Secrets، CI، GitHub Rulesets، OpenAPI reconciliation، مراجعة قرارات المالك. لا مشاريع وهمية ولا CI أخضر دون تشغيل فعلي.

## Sprints التالية — حسب ترتيب Dependencies الفعلي

- Identity, guardian limitation, scoped roles and public accounts.
- Markets, programs, teachers, teacher verification, availability.
- DST-safe booking and holds, lesson video PoC and fallbacks.
- Attendance, teacher reports, academic plans and revision evidence.
- Assessments, exams, competitions, appeals and certificates.
- Pricing, quotes, billing, subscriptions, refunds, ledgers and payroll after approvals.
- AI/audio governance, Qur'an licensed content, privacy, anti-abuse and localization.
- Supervisor/admin consoles, CRM, support, analytics, provider console and market activation.
- Mobile integration, encrypted offline sync, Kids/Professional/Simple, release/store readiness.
- Security hardening, accessibility human testing, load testing, observability, disaster recovery and paid production gates.

## Planning protocol

Sprint length: 2 weeks. On day 1 team (Full Stack + Flutter) chooses ready tickets by merged dependencies. Reserve capacity for review/QA and production incidents. At review update throughput and forecast. Never drag all 91 candidate sprints into active Jira board. Each release has own GO / CONDITIONAL GO / NO-GO.
