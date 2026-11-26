# Screen specifications (169)

Each file in `screens/` is the implementation contract for one screen. Visual source: `01_design/canvas/<ID>.dc.html` (live) and `01_design/html/{ar,en}/<ID>.html` (static).

| ID | Screen | Role | Route | Phase | Module | Spec |
|---|---|---|---|---|---|---|
| `UX-PUBLIC-001` | Marketing Home | Guest (public) | `/` | P0 | GEO | [spec](screens/UX-PUBLIC-001.md) |
| `UX-PUBLIC-002` | Programs Directory | Guest (public) | `/programs` | P0 | CURR | [spec](screens/UX-PUBLIC-002.md) |
| `UX-PUBLIC-003` | Program Detail | Guest (public) | `/programs/:slug` | P0 | CURR | [spec](screens/UX-PUBLIC-003.md) |
| `UX-PUBLIC-004` | Pricing | Guest (public) | `/pricing` | P0 | PAY | [spec](screens/UX-PUBLIC-004.md) |
| `UX-PUBLIC-005` | Teacher Directory | Guest (public) | `/teachers` | P0 | TCHR | [spec](screens/UX-PUBLIC-005.md) |
| `UX-PUBLIC-006` | Teacher Public Profile | Guest (public) | `/teachers/:slug` | P0 | TCHR | [spec](screens/UX-PUBLIC-006.md) |
| `UX-PUBLIC-007` | How It Works | Guest (public) | `/how-it-works` | P0 | I18N | [spec](screens/UX-PUBLIC-007.md) |
| `UX-PUBLIC-008` | Competition Landing | Guest (public) | `/challenges` | P0 | CONTEST | [spec](screens/UX-PUBLIC-008.md) |
| `UX-PUBLIC-009` | Free Assessment Booking | Guest (public) | `/trial` | P0 | BOOK | [spec](screens/UX-PUBLIC-009.md) |
| `UX-PUBLIC-010` | About/Academic Standards | Guest (public) | `/about` | P0 | CURR | [spec](screens/UX-PUBLIC-010.md) |
| `UX-PUBLIC-011` | FAQ & Support | Guest (public) | `/help` | P0 | NOTIF | [spec](screens/UX-PUBLIC-011.md) |
| `UX-PUBLIC-012` | Legal & Consents | Guest (public) | `/legal/:slug` | P0 | I18N | [spec](screens/UX-PUBLIC-012.md) |
| `UX-AUTH-001` | Unified Signup | Guest / onboarding user | `/signup` | P0 | IAM | [spec](screens/UX-AUTH-001.md) |
| `UX-AUTH-002` | Guardian Consent Step | Guest / onboarding user | `/onboarding/guardian-consent` | P0 | IAM | [spec](screens/UX-AUTH-002.md) |
| `UX-AUTH-003` | Login | Guest / onboarding user | `/login` | P0 | IAM | [spec](screens/UX-AUTH-003.md) |
| `UX-AUTH-004` | Password Recovery | Guest / onboarding user | `/forgot-password` | P0 | IAM | [spec](screens/UX-AUTH-004.md) |
| `UX-AUTH-005` | Welcome Onboarding | Guest / onboarding user | `/onboarding` | P0 | PROF | [spec](screens/UX-AUTH-005.md) |
| `UX-LEARNER-001` | Learner Home | Learner | `/app` | P0 | PLAN | [spec](screens/UX-LEARNER-001.md) |
| `UX-LEARNER-002` | My Learning Profile | Learner | `/app/profile` | P0 | PROF | [spec](screens/UX-LEARNER-002.md) |
| `UX-LEARNER-003` | Programs Discover | Learner | `/app/programs` | P0 | CURR | [spec](screens/UX-LEARNER-003.md) |
| `UX-LEARNER-004` | Initial Assessment | Learner | `/app/assessment` | P0 | ASMT | [spec](screens/UX-LEARNER-004.md) |
| `UX-LEARNER-005` | Teachers Discover | Learner | `/app/teachers` | P0 | TCHR | [spec](screens/UX-LEARNER-005.md) |
| `UX-LEARNER-006` | Teacher Detail | Learner | `/app/teachers/:id` | P0 | TCHR | [spec](screens/UX-LEARNER-006.md) |
| `UX-LEARNER-007` | Calendar | Learner | `/app/calendar` | P0 | BOOK | [spec](screens/UX-LEARNER-007.md) |
| `UX-LEARNER-008` | Booking Wizard | Learner | `/app/book` | P0 | BOOK | [spec](screens/UX-LEARNER-008.md) |
| `UX-LEARNER-009` | Lesson Detail | Learner | `/app/lessons/:id` | P0 | BOOK | [spec](screens/UX-LEARNER-009.md) |
| `UX-LEARNER-010` | Classroom | Learner | `/app/lessons/:id/live` | P0 | VIDEO | [spec](screens/UX-LEARNER-010.md) |
| `UX-LEARNER-011` | Post-Lesson Report | Learner | `/app/lessons/:id/report` | P0 | ATT | [spec](screens/UX-LEARNER-011.md) |
| `UX-LEARNER-012` | Learning Plan | Learner | `/app/plan` | P0 | PLAN | [spec](screens/UX-LEARNER-012.md) |
| `UX-LEARNER-013` | Daily Study | Learner | `/app/study` | P0 | PLAN | [spec](screens/UX-LEARNER-013.md) |
| `UX-LEARNER-014` | Revision Queue | Learner | `/app/revision` | P0 | PLAN | [spec](screens/UX-LEARNER-014.md) |
| `UX-LEARNER-015` | Memory Map | Learner | `/app/memory-map` | P0 | PLAN | [spec](screens/UX-LEARNER-015.md) |
| `UX-LEARNER-016` | Practice Recording | Learner | `/app/practice` | P0 | MEDIA | [spec](screens/UX-LEARNER-016.md) |
| `UX-LEARNER-017` | Exam Catalog | Learner | `/app/exams` | P0 | ASMT | [spec](screens/UX-LEARNER-017.md) |
| `UX-LEARNER-018` | Exam Taking | Learner | `/app/exams/:id/take` | P0 | ASMT | [spec](screens/UX-LEARNER-018.md) |
| `UX-LEARNER-019` | Exam Results | Learner | `/app/exams/:id/result` | P0 | ASMT | [spec](screens/UX-LEARNER-019.md) |
| `UX-LEARNER-020` | Competitions Discover | Learner | `/app/competitions` | P0 | CONTEST | [spec](screens/UX-LEARNER-020.md) |
| `UX-LEARNER-021` | Competition Detail | Learner | `/app/competitions/:id` | P0 | CONTEST | [spec](screens/UX-LEARNER-021.md) |
| `UX-LEARNER-022` | Competition Preparation | Learner | `/app/competitions/:id/prepare` | P0 | CONTEST | [spec](screens/UX-LEARNER-022.md) |
| `UX-LEARNER-023` | Competition Round | Learner | `/app/competitions/:id/round/:roundId` | P0 | CONTEST | [spec](screens/UX-LEARNER-023.md) |
| `UX-LEARNER-024` | Competition Standings | Learner | `/app/competitions/:id/standings` | P0 | CONTEST | [spec](screens/UX-LEARNER-024.md) |
| `UX-LEARNER-025` | Competition Result & Appeal | Learner | `/app/competitions/:id/result` | P0 | CONTEST | [spec](screens/UX-LEARNER-025.md) |
| `UX-LEARNER-026` | Achievements | Learner | `/app/achievements` | P0 | CONTEST | [spec](screens/UX-LEARNER-026.md) |
| `UX-LEARNER-027` | AI Study Assistant | Learner | `/app/ai-coach` | P0 | AI | [spec](screens/UX-LEARNER-027.md) |
| `UX-LEARNER-028` | Course Library | Learner | `/app/library` | P0 | MEDIA | [spec](screens/UX-LEARNER-028.md) |
| `UX-LEARNER-029` | Subscription & Billing | Learner | `/app/billing` | P0 | PAY | [spec](screens/UX-LEARNER-029.md) |
| `UX-LEARNER-030` | Notifications | Learner | `/app/notifications` | P0 | NOTIF | [spec](screens/UX-LEARNER-030.md) |
| `UX-LEARNER-031` | Support and Reports | Learner | `/app/support` | P0 | NOTIF | [spec](screens/UX-LEARNER-031.md) |
| `UX-LEARNER-032` | Account Settings | Learner | `/app/settings` | P0 | IAM | [spec](screens/UX-LEARNER-032.md) |
| `UX-TEACHER-001` | Teacher Login & Onboarding | Guest / onboarding user | `/teach/start` | P0 | TCHR | [spec](screens/UX-TEACHER-001.md) |
| `UX-TEACHER-002` | Teacher Home | Teacher | `/teach` | P0 | TCHR | [spec](screens/UX-TEACHER-002.md) |
| `UX-TEACHER-003` | Availability | Teacher | `/teach/availability` | P0 | TCHR | [spec](screens/UX-TEACHER-003.md) |
| `UX-TEACHER-004` | Teaching Calendar | Teacher | `/teach/calendar` | P0 | TIME | [spec](screens/UX-TEACHER-004.md) |
| `UX-TEACHER-005` | Lesson Briefing | Teacher | `/teach/lessons/:id` | P0 | ATT | [spec](screens/UX-TEACHER-005.md) |
| `UX-TEACHER-006` | Teacher Classroom | Teacher | `/teach/lessons/:id/live` | P0 | VIDEO | [spec](screens/UX-TEACHER-006.md) |
| `UX-TEACHER-007` | Lesson Report Editor | Teacher | `/teach/lessons/:id/report` | P0 | ATT | [spec](screens/UX-TEACHER-007.md) |
| `UX-TEACHER-008` | My Assigned Learners | Teacher | `/teach/learners` | P0 | TCHR | [spec](screens/UX-TEACHER-008.md) |
| `UX-TEACHER-009` | Learner Academic Detail | Teacher | `/teach/learners/:id` | P0 | PROF | [spec](screens/UX-TEACHER-009.md) |
| `UX-TEACHER-010` | Assessment Workspace | Teacher | `/teach/assessments` | P0 | ASMT | [spec](screens/UX-TEACHER-010.md) |
| `UX-TEACHER-011` | Plan Review Queue | Teacher | `/teach/plans` | P0 | PLAN | [spec](screens/UX-TEACHER-011.md) |
| `UX-TEACHER-012` | Question Bank Review | Teacher | `/teach/questions` | P0 | CURR | [spec](screens/UX-TEACHER-012.md) |
| `UX-TEACHER-013` | Contests Assigned | Teacher | `/teach/competitions` | P0 | CONTEST | [spec](screens/UX-TEACHER-013.md) |
| `UX-TEACHER-014` | Contest Judging | Teacher | `/teach/competitions/:id/judge` | P0 | CONTEST | [spec](screens/UX-TEACHER-014.md) |
| `UX-TEACHER-015` | Appeals Academic Review | Teacher | `/teach/appeals` | P0 | CONTEST | [spec](screens/UX-TEACHER-015.md) |
| `UX-TEACHER-016` | Teacher Pay Statements | Teacher | `/teach/pay` | P0 | PAYROLL | [spec](screens/UX-TEACHER-016.md) |
| `UX-TEACHER-017` | Teacher Support | Teacher | `/teach/support` | P0 | NOTIF | [spec](screens/UX-TEACHER-017.md) |
| `UX-TEACHER-018` | Teacher Account & Consent | Teacher | `/teach/settings` | P0 | IAM | [spec](screens/UX-TEACHER-018.md) |
| `UX-ADMIN-001` | Executive Dashboard | Platform admin (scoped) | `/admin` | P0 | ADMIN | [spec](screens/UX-ADMIN-001.md) |
| `UX-ADMIN-002` | Learner Directory | Platform admin (scoped) | `/admin/learners` | P0 | IAM | [spec](screens/UX-ADMIN-002.md) |
| `UX-ADMIN-003` | Learner 360 | Platform admin (scoped) | `/admin/learners/:id` | P0 | PROF | [spec](screens/UX-ADMIN-003.md) |
| `UX-ADMIN-004` | Guardian Consent Queue | Platform admin (scoped) | `/admin/consents` | P0 | IAM | [spec](screens/UX-ADMIN-004.md) |
| `UX-ADMIN-005` | Staff & Permissions | Platform admin (scoped) | `/admin/staff` | P0 | ADMIN | [spec](screens/UX-ADMIN-005.md) |
| `UX-ADMIN-006` | Teacher Recruitment | Platform admin (scoped) | `/admin/teachers/applications` | P0 | TCHR | [spec](screens/UX-ADMIN-006.md) |
| `UX-ADMIN-007` | Teacher Management | Platform admin (scoped) | `/admin/teachers` | P0 | TCHR | [spec](screens/UX-ADMIN-007.md) |
| `UX-ADMIN-008` | Teacher Profile Admin | Platform admin (scoped) | `/admin/teachers/:id` | P0 | TCHR | [spec](screens/UX-ADMIN-008.md) |
| `UX-ADMIN-009` | Teacher Contract Builder | Platform admin (scoped) | `/admin/teachers/:id/compensation` | P0 | PAYROLL | [spec](screens/UX-ADMIN-009.md) |
| `UX-ADMIN-010` | Teacher Shift Planner | Platform admin (scoped) | `/admin/teachers/shifts` | P0 | TIME | [spec](screens/UX-ADMIN-010.md) |
| `UX-ADMIN-011` | Programs CMS | Platform admin (scoped) | `/admin/programs` | P0 | CURR | [spec](screens/UX-ADMIN-011.md) |
| `UX-ADMIN-012` | Quran Content Sources | Platform admin (scoped) | `/admin/quran-sources` | P0 | CURR | [spec](screens/UX-ADMIN-012.md) |
| `UX-ADMIN-013` | Question Bank Manager | Platform admin (scoped) | `/admin/question-bank` | P0 | CURR | [spec](screens/UX-ADMIN-013.md) |
| `UX-ADMIN-014` | Assessment Rubrics | Platform admin (scoped) | `/admin/rubrics` | P0 | ASMT | [spec](screens/UX-ADMIN-014.md) |
| `UX-ADMIN-015` | Bookings Operations | Platform admin (scoped) | `/admin/bookings` | P0 | BOOK | [spec](screens/UX-ADMIN-015.md) |
| `UX-ADMIN-016` | Live Lessons Monitor | Platform admin (scoped) | `/admin/live` | P0 | VIDEO | [spec](screens/UX-ADMIN-016.md) |
| `UX-ADMIN-017` | Conference Provider Registry | Platform admin (scoped) | `/admin/video-providers` | P0 | VIDEO | [spec](screens/UX-ADMIN-017.md) |
| `UX-ADMIN-018` | Attendance & Makeups | Platform admin (scoped) | `/admin/attendance` | P0 | ATT | [spec](screens/UX-ADMIN-018.md) |
| `UX-ADMIN-019` | Payments & Invoices | Platform admin (scoped) | `/admin/payments` | P0 | PAY | [spec](screens/UX-ADMIN-019.md) |
| `UX-ADMIN-020` | Packages & Promotions | Platform admin (scoped) | `/admin/packages` | P0 | PAY | [spec](screens/UX-ADMIN-020.md) |
| `UX-ADMIN-021` | Payroll Calculations | Platform admin (scoped) | `/admin/payroll` | P0 | PAYROLL | [spec](screens/UX-ADMIN-021.md) |
| `UX-ADMIN-022` | Payroll Approval | Platform admin (scoped) | `/admin/payroll/:id` | P0 | PAYROLL | [spec](screens/UX-ADMIN-022.md) |
| `UX-ADMIN-023` | AI Learning Control | Platform admin (scoped) | `/admin/ai-learning` | P0 | AI | [spec](screens/UX-ADMIN-023.md) |
| `UX-ADMIN-024` | Session Policy Review | Platform admin (scoped) | `/admin/session-reviews` | P0 | AI | [spec](screens/UX-ADMIN-024.md) |
| `UX-ADMIN-025` | Competition Templates | Platform admin (scoped) | `/admin/competition-templates` | P0 | CONTEST | [spec](screens/UX-ADMIN-025.md) |
| `UX-ADMIN-026` | Contest Builder Wizard | Platform admin (scoped) | `/admin/competitions/new` | P0 | CONTEST | [spec](screens/UX-ADMIN-026.md) |
| `UX-ADMIN-027` | Competitions List | Platform admin (scoped) | `/admin/competitions` | P0 | CONTEST | [spec](screens/UX-ADMIN-027.md) |
| `UX-ADMIN-028` | Competition Control Room | Platform admin (scoped) | `/admin/competitions/:id` | P0 | CONTEST | [spec](screens/UX-ADMIN-028.md) |
| `UX-ADMIN-029` | Judge Assignments | Platform admin (scoped) | `/admin/competitions/:id/judges` | P0 | CONTEST | [spec](screens/UX-ADMIN-029.md) |
| `UX-ADMIN-030` | Leaderboard & Publish | Platform admin (scoped) | `/admin/competitions/:id/results` | P0 | CONTEST | [spec](screens/UX-ADMIN-030.md) |
| `UX-ADMIN-031` | Contest Appeals | Platform admin (scoped) | `/admin/contest-appeals` | P0 | CONTEST | [spec](screens/UX-ADMIN-031.md) |
| `UX-ADMIN-032` | Contest Rewards & Certificates | Platform admin (scoped) | `/admin/rewards` | P0 | CONTEST | [spec](screens/UX-ADMIN-032.md) |
| `UX-ADMIN-033` | CRM Pipeline | Platform admin (scoped) | `/admin/crm` | P0 | CRM | [spec](screens/UX-ADMIN-033.md) |
| `UX-ADMIN-034` | Campaign Analytics | Platform admin (scoped) | `/admin/marketing` | P0 | CRM | [spec](screens/UX-ADMIN-034.md) |
| `UX-ADMIN-035` | Support Center | Platform admin (scoped) | `/admin/support` | P0 | SUP | [spec](screens/UX-ADMIN-035.md) |
| `UX-ADMIN-036` | Safeguarding Incident Queue | Platform admin (scoped) | `/admin/safety` | P0 | SUP | [spec](screens/UX-ADMIN-036.md) |
| `UX-ADMIN-037` | Recorded Content Library | Platform admin (scoped) | `/admin/library` | P0 | MEDIA | [spec](screens/UX-ADMIN-037.md) |
| `UX-ADMIN-038` | Notification Center | Platform admin (scoped) | `/admin/notifications` | P0 | NOTIF | [spec](screens/UX-ADMIN-038.md) |
| `UX-ADMIN-039` | Reports and KPI Explorer | Platform admin (scoped) | `/admin/reports` | P0 | ADMIN | [spec](screens/UX-ADMIN-039.md) |
| `UX-ADMIN-040` | Audit Trail | Platform admin (scoped) | `/admin/audit` | P0 | SEC | [spec](screens/UX-ADMIN-040.md) |
| `UX-ADMIN-041` | Settings & Feature Flags | Platform admin (scoped) | `/admin/settings` | P0 | ADMIN | [spec](screens/UX-ADMIN-041.md) |
| `UX-GLOB-001` | Country & Currency Selector | Guest (public) | `/choose-country` | P0 | GEO | [spec](screens/UX-GLOB-001.md) |
| `UX-GLOB-002` | Localized Pricing Comparison | Guest (public) | `/pricing` | P0 | GEO | [spec](screens/UX-GLOB-002.md) |
| `UX-GLOB-003` | Unavailable Country & Waitlist | Guest (public) | `/unavailable-market` | P1 | GEO | [spec](screens/UX-GLOB-003.md) |
| `UX-GLOB-004` | Language & Regional Preferences | Learner | `/me/preferences/region` | P0 | I18N | [spec](screens/UX-GLOB-004.md) |
| `UX-GLOB-005` | Timezone Preview & DST Warning | Learner | `/me/schedule/timezone-preview` | P0 | TIME | [spec](screens/UX-GLOB-005.md) |
| `UX-GLOB-006` | Regional Checkout Quote | Learner | `/checkout/:quoteId` | P0 | PAY | [spec](screens/UX-GLOB-006.md) |
| `UX-GLOB-007` | Renewal Price Change Notice | Learner | `/me/subscriptions/:id/renewal` | P1 | PAY | [spec](screens/UX-GLOB-007.md) |
| `UX-GLOB-008` | Timezone Availability Editor | Teacher | `/teacher/availability` | P0 | TIME | [spec](screens/UX-GLOB-008.md) |
| `UX-GLOB-009` | Cross Timezone Lesson Details | Teacher | `/teacher/lessons/:id` | P0 | TIME | [spec](screens/UX-GLOB-009.md) |
| `UX-GLOB-010` | Markets Overview | Platform admin (scoped) | `/admin/markets` | P0 | GEO | [spec](screens/UX-GLOB-010.md) |
| `UX-GLOB-011` | Market Launch Wizard | Platform admin (scoped) | `/admin/markets/new` | P0 | GEO | [spec](screens/UX-GLOB-011.md) |
| `UX-GLOB-012` | Country Pricing Matrix | Platform admin (scoped) | `/admin/pricing/matrix` | P0 | GEO | [spec](screens/UX-GLOB-012.md) |
| `UX-GLOB-013` | Price Approval & Version Diff | Platform admin (scoped) | `/admin/pricing/approvals/:id` | P0 | GEO | [spec](screens/UX-GLOB-013.md) |
| `UX-GLOB-014` | Merchant Profiles | Platform admin (scoped) | `/admin/payments/merchant-profiles` | P0 | GEO | [spec](screens/UX-GLOB-014.md) |
| `UX-GLOB-015` | FX Reporting & Settlement | Platform admin (scoped) | `/admin/finance/fx` | P1 | GEO | [spec](screens/UX-GLOB-015.md) |
| `UX-GLOB-016` | Regional Schedule Dashboard | Platform admin (scoped) | `/admin/operations/timezones` | P0 | TIME | [spec](screens/UX-GLOB-016.md) |
| `UX-GLOB-017` | Flutter Region & Language | Learner (Flutter) | `mobile://settings/region` | P2 | I18N | [spec](screens/UX-GLOB-017.md) |
| `UX-VPC-001` | Video Providers Overview | Platform admin (scoped) | `/admin/settings/video-providers` | P0 | VPC | [spec](screens/UX-VPC-001.md) |
| `UX-VPC-002` | Video Provider Credentials | Platform admin (scoped) | `/admin/settings/video-providers/:id/credentials` | P0 | VPC | [spec](screens/UX-VPC-002.md) |
| `UX-VPC-003` | Video Provider Capabilities | Platform admin (scoped) | `/admin/settings/video-providers/:id/capabilities` | P0 | VPC | [spec](screens/UX-VPC-003.md) |
| `UX-VPC-004` | Video Routing Rules | Platform admin (scoped) | `/admin/settings/video-routing` | P0 | VPC | [spec](screens/UX-VPC-004.md) |
| `UX-VPC-005` | Video Switch Impact & Dry-run | Platform admin (scoped) | `/admin/settings/video-routing/dry-run` | P0 | VPC | [spec](screens/UX-VPC-005.md) |
| `UX-VPC-006` | Video Routing Approval | Platform admin (scoped) | `/admin/settings/video-routing/approvals/:id` | P0 | VPC | [spec](screens/UX-VPC-006.md) |
| `UX-VPC-007` | Video Provider Monitoring | Platform admin (scoped) | `/admin/monitoring/video` | P1 | VPC | [spec](screens/UX-VPC-007.md) |
| `UX-VPC-008` | Video Failover Incident Console | Platform admin (scoped) | `/admin/operations/video-incidents/:id` | P0 | VPC | [spec](screens/UX-VPC-008.md) |
| `UX-VPC-009` | Embedded vs External Prejoin | Learner | `/lessons/:id/prejoin` | P0 | VPC | [spec](screens/UX-VPC-009.md) |
| `UX-VPC-010` | Teacher Provider Join Health | Teacher | `/teacher/lessons/:id/join` | P0 | VPC | [spec](screens/UX-VPC-010.md) |
| `UX-SUP-001` | Supervisor Home | Supervisor (scoped) | `/supervisor` | P0 | SUP | [spec](screens/UX-SUP-001.md) |
| `UX-SUP-002` | Academic Plans Approval | Supervisor (scoped) | `/supervisor/academic/plans` | P0 | SUP | [spec](screens/UX-SUP-002.md) |
| `UX-SUP-003` | Quality Observation Queue | Supervisor (scoped) | `/supervisor/quality/observations` | P1 | SUP | [spec](screens/UX-SUP-003.md) |
| `UX-SUP-004` | Safeguarding Case Console | Supervisor (scoped) | `/supervisor/safeguarding/cases` | P0 | SUP | [spec](screens/UX-SUP-004.md) |
| `UX-SUP-005` | Competition Moderation | Supervisor (scoped) | `/supervisor/competitions` | P1 | SUP | [spec](screens/UX-SUP-005.md) |
| `UX-SUP-006` | Operations Coverage Board | Supervisor (scoped) | `/supervisor/operations/schedule` | P0 | SUP | [spec](screens/UX-SUP-006.md) |
| `UX-SUP-007` | Regional KPI & Enrollment | Supervisor (scoped) | `/supervisor/regions` | P1 | SUP | [spec](screens/UX-SUP-007.md) |
| `UX-SUP-008` | Role Assignments & Scopes | Platform admin (scoped) | `/admin/security/supervisors` | P0 | SUP | [spec](screens/UX-SUP-008.md) |
| `UX-SUP-009` | Audit and Break-glass Review | Platform admin (scoped) | `/admin/security/access-audits` | P0 | SUP | [spec](screens/UX-SUP-009.md) |
| `UX-SUP-010` | Settings Registry | Platform admin (scoped) | `/admin/settings` | P0 | SUP | [spec](screens/UX-SUP-010.md) |
| `UX-SUP-011` | Localization Content Studio | Platform admin (scoped) | `/admin/content/translations` | P1 | I18N | [spec](screens/UX-SUP-011.md) |
| `UX-ENG-001` | Competition Localized Schedule | Learner | `/competitions/:id/schedule` | P1 | ENG | [spec](screens/UX-ENG-001.md) |
| `UX-ENG-002` | Adaptive Practice Brief | Learner | `/study/practice/recommended` | P1 | ENG | [spec](screens/UX-ENG-002.md) |
| `UX-ENG-003` | Gentle Progress & Streak Recovery | Learner | `/me/progress/weekly` | P1 | ENG | [spec](screens/UX-ENG-003.md) |
| `UX-MOBILE-000` | Flutter Splash (added) | Learner (Flutter) | `mobile://splash` | P2 | MOB | [spec](screens/UX-MOBILE-000.md) |
| `UX-MOBILE-001` | Flutter Login | Learner (Flutter) | `mobile://auth` | P2 | MOB | [spec](screens/UX-MOBILE-001.md) |
| `UX-MOBILE-002` | Flutter Today | Learner (Flutter) | `mobile://home` | P2 | MOB | [spec](screens/UX-MOBILE-002.md) |
| `UX-MOBILE-003` | Flutter Classroom | Learner (Flutter) | `mobile://classroom` | P2 | MOB | [spec](screens/UX-MOBILE-003.md) |
| `UX-MOBILE-004` | Flutter Schedule | Learner (Flutter) | `mobile://schedule` | P2 | MOB | [spec](screens/UX-MOBILE-004.md) |
| `UX-MOBILE-005` | Flutter Memory Map | Learner (Flutter) | `mobile://memory` | P2 | PLAN | [spec](screens/UX-MOBILE-005.md) |
| `UX-MOBILE-006` | Flutter AI Coach | Learner (Flutter) | `mobile://coach` | P2 | AI | [spec](screens/UX-MOBILE-006.md) |
| `UX-MOBILE-007` | Flutter Exam | Learner (Flutter) | `mobile://exam` | P2 | MOB | [spec](screens/UX-MOBILE-007.md) |
| `UX-MOBILE-008` | Flutter Competition | Learner (Flutter) | `mobile://competition` | P2 | CONTEST | [spec](screens/UX-MOBILE-008.md) |
| `UX-MOBILE-009` | Flutter Teacher Today | Teacher (Flutter) | `mobile://teacher` | P2 | MOB | [spec](screens/UX-MOBILE-009.md) |
| `UX-MOBILE-010` | Flutter Teacher Report | Teacher (Flutter) | `mobile://teacher/report` | P2 | ATT | [spec](screens/UX-MOBILE-010.md) |
| `UX-MOBILE-011` | Flutter Account | Learner (Flutter) | `mobile://settings` | P2 | MOB | [spec](screens/UX-MOBILE-011.md) |
| `UX-MOBILE-012` | App style chooser (added) | Learner (Flutter) | `mobile://settings/app-style` | P2 | MOB | [spec](screens/UX-MOBILE-012.md) |
| `UX-MOBILE-K02` | Kids · Today mission (added) | Learner (Flutter, Kids mode 6–12) | `mobile://kids/today` | P2 | MOB | [spec](screens/UX-MOBILE-K02.md) |
| `UX-MOBILE-K05` | Kids · My path (added) | Learner (Flutter, Kids mode 6–12) | `mobile://kids/path` | P2 | PLAN | [spec](screens/UX-MOBILE-K05.md) |
| `UX-MOBILE-K08` | Kids · My stars (added) | Learner (Flutter, Kids mode 6–12) | `mobile://kids/stars` | P2 | ENG | [spec](screens/UX-MOBILE-K08.md) |
| `UX-MOBILE-K11` | Kids · Me (added) | Learner (Flutter, Kids mode 6–12) | `mobile://kids/me` | P2 | IAM | [spec](screens/UX-MOBILE-K11.md) |
| `UX-MOBILE-S02` | Simple · Today (added) | Learner (Flutter, Simple mode 60+) | `mobile://simple/today` | P2 | MOB | [spec](screens/UX-MOBILE-S02.md) |
| `UX-MOBILE-S04` | Simple · My lessons (added) | Learner (Flutter, Simple mode 60+) | `mobile://simple/lessons` | P2 | MOB | [spec](screens/UX-MOBILE-S04.md) |
| `UX-MOBILE-S11` | Simple · Help (added) | Learner (Flutter, Simple mode 60+) | `mobile://simple/help` | P2 | MOB | [spec](screens/UX-MOBILE-S11.md) |
