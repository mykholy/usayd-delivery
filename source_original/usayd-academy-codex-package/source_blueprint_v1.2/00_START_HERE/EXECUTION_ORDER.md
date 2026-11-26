# Order of work for Claude, Codex and human reviewers

| Gate | Who | Input | Required output | Do not proceed until |
|---|---|---|---|---|
| G0 | Product/Academic/Legal/Finance | BRD, PRD, open decisions | signed pilot scope + DPA/legal/teacher policy decisions | required sign-offs documented |
| G1 | Claude/Figma | `CLAUDE.md`, UI screen specs, design tokens | editable components, 25 critical flows first, screen registry, prototype links, design review evidence | Product/Academic/A11y design review |
| G2 | Codex API | `AGENTS.md`, typed OpenAPI, SRS, data model | Laravel bootstrap, migrations, auth/consent, CI, API tests | API contract + security checks green |
| G3 | Codex academy | P0 booking/payments/teacher/timezone/provider specs | deterministic booking, ledger, teacher scheduling, embedded/external video adapter | paid learner E2E with webhook replay |
| G4 | Codex learning | academic rules + learner UX | assessments, approved plans, memory map, revision, exams | teacher approval, content checks green |
| G5 | Codex engagement | competitions & awards specs | contests, judging, result versioning, appeals, private leaderboard | fairness and minor privacy UAT |
| G6 | Codex AI | AI evaluation and consent policies | opt-in AI suggestions, human review, redaction, cost limits | accuracy/privacy/evaluation gates |
| G7 | Codex mobile | Flutter specs + stable API | Flutter app, secure session and video adapter | device/offline/a11y/store checks |
| G8 | QA/CTO/Ops | all prior gates | perf/rollback/DR/security QA and evidence | release owner GO decision |

**Conflict precedence:** legal safety & academic authenticity > signed ADR > SRS/FR/NFR > reviewed OpenAPI contract > reviewed UX > Jira description > AI-generated suggestions. Conflicts produce an ADR or issue, never a silent guess.

**Per-task rule:** plan → minimal change → unit tests → integration tests → E2E where meaningful → security review → traceability update → PR → evidence; never claim background work or production success.
