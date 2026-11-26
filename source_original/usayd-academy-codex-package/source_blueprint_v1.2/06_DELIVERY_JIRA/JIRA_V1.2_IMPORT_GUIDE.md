# Jira import guide v1.2

1. The authoritative CSV is `06_DELIVERY_JIRA/Jira_Import.csv`; do NOT import v1.0 and v1.1 copies in parallel.
2. File contains `Issue ID`, `Parent ID`, `Issue Type`, `Summary`, `Description`, `Priority`, `Fix Version`, `Labels`, `Component`, `Story Points`, `Requirement ID`. Fields are local link IDs, **not actual Jira issue keys**.
3. Jira Cloud projects/import modes vary. In a *sandbox Jira project*, import 1 Epic + 1 Story + 1 Task; map parent relationship using importer support for CSV issue ID/parent ID; confirm Arabic UTF-8, Description line breaks and parent type.
4. If importer cannot map parent links in one import, use staged Epics then stories/tasks with a deterministic local-id→Jira-key mapping file; avoid losing relationships silently.
5. Existing original stories 148 + v1.2 newly added 68 stories have Requirement IDs; v1.2 adds linked QA tasks and new domain Epics. Validate every requirement has one primary Story and two traceable tests.
6. Create Jira components/labels per domain GEO TIME I18N VPC SUP ENG. Do not auto-assign owner or sprint capacity without actual team bandwidth.
7. Add custom fields `FR_ID`, `UX_IDs`, `API_operationIds`, `Evidence_Link`, `Security_Reviewer`, `Academic_Reviewer`, `Legal_Reviewer` as available.
8. Fix versions and priority mapped to your actual Jira project vocabulary; import into test then verify counts and random Arabic stories.
9. Status initial = Backlog; no Story is Done merely because a spec document or design concept exists.
10. All release gates and 60 detailed E2E scenarios are in `14_RELEASE_QA/`. Test cases can be imported into Xray/Zephyr separately if licensed.
