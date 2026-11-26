# Usayd Academy — Live Jira lookup for Gemini / Codex

Jira project: https://mykholy.atlassian.net/jira/software/projects/USYD/boards/1

The Jira migration was reconciled against the authoritative READY master backlog.

- 33 canonical Epics
- 707 canonical Tasks/Stories
- All 57 Flutter issues assigned to **Ahmed Mamdouh El- Sayed** (Jira accountId `70121:24ce7639-fa05-4a15-b940-290557ac3fcd`).
- All canonical tasks have Epic parents.
- 5 accidental duplicated import issues are Done, labeled `duplicate-ignore`, and linked to their canonical issues.

Use `USAYD_JIRA_CANONICAL_TASK_MAPPING_2026-11-24.json` or `.csv` to convert planning file IDs `USYD-TXXXX` to real Jira issue keys `USYD-###`. Do not assume these identifiers are interchangeable.

For example, canonical source task `USYD-T0023` maps to Jira issue `USYD-56`; planning file `delivery/planning/tasks/USYD-T0023.md` is still the detailed implementation specification. The Jira description references that path and carries acceptance guidance.

A candidate sprint is recorded as label `planned-s00`, `planned-s01`, etc. The current Jira board is **Kanban and does not support native Jira sprints**. Do not claim sprint creation or execution until a Scrum board is configured.

As of this sync, full cross-ticket Jira *blocks* links and site-specific story-point custom fields have **not** been populated from the planning CSV. Dependencies remain in each ticket's Description and the authoritative planning dependency matrix. Consult both before starting work.

Jira verified filters:

- Canonical backlog: `project = USYD AND labels = usayd-spec-handoff`
- Flutter assignments: `project = USYD AND labels = flutter AND assignee = "70121:24ce7639-fa05-4a15-b940-290557ac3fcd"`
- Ignore closed duplicates: `project = USYD AND labels = duplicate-ignore`

For each ticket, follow branch → implementation → tests → PR → independent review → merge where actual GitHub required checks/approvals are satisfied → verify result → Jira Done. Never report CI/PR status from assumptions.
