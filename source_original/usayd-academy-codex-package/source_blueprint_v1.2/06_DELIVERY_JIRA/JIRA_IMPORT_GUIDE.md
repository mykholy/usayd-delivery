# Jira import & team execution guide

## Contents

- `Jira_Import.csv` contains **311 issues**: **19 Epics**, **148 requirement Stories**, **119 UX/Flutter Tasks**, **25 implementation/research Tasks**.
- `requirements_traceability.csv` ties each functional requirement to a story and two test IDs.
- `dependency_map.csv` records epic dependencies; must be translated to Jira *blocks* issue links after import.
- `sprint_plan.csv` gives the suggested phase/sprint breakdown (NOT commitment).

## Import prerequisites

1. Create a clean Jira Software project and confirm that `Epic`, `Story`, `Task` and desired custom fields exist. Configure `P0/P1/P2` as versions/releases or map `Fix Version` values to a custom field.
2. `Issue ID` and `Parent ID` in CSV are **local import linkage IDs**, not existing Jira issue keys. Jira Cloud CSV importer support varies by UI and permissions; perform a 3-issue trial (Epic+Story+Task) before bulk import. Map `Parent ID` correctly or import Epics first and link stories via real Jira keys afterward.
3. Map `Summary`, `Issue Type`, `Description`, `Priority`, `Labels`, `Component`, `Story Points` (must exist/custom), and optional `Requirement ID`. If `Story Points` unsupported for Task, remove/map accordingly.
4. Review quoted multiline descriptions and UTF-8 BOM. If importer rejects hierarchy, drop Parent column and import with issue IDs, then bulk-link parent epics after import from `component/requirement ID` mapping.
5. Validate parent/child IDs and labels after import. This CSV is designed as a safe starting backlog, **not a claim of native Jira project creation**.

## Story refinement standard

Every story is expected to have: linked FR ID, UX screens, actual API typed contract, acceptance tests (happy/denied/invalid/timezone), required analytics and audit, owner, estimate and review requirements. Break 8+ point tasks into manageable implementation/test slices during sprint planning.

## Suggested team

Product Owner (1), Academic Lead (1), Tech Lead/Laravel (1), backend engineers (1–2), frontend engineer (1–2), UX/UI designer (1), QA automation (1), DevOps shared, Flutter developer (P2), AI engineer (P1), privacy/legal and finance part time. Velocity assumptions must be measured from real team, not guessed.

## Board configuration

Workflow: Backlog → Ready for Dev → In Progress → Code Review → QA → Stakeholder Review → Done, with Blocked state and bug-specific QA/Reopen transitions. Components map to modules/roles. Definition of Ready: requirements signed, dependencies resolved, contract and UX annotated. Definition of Done: code/QA/security/academic checks and release flags complete.
