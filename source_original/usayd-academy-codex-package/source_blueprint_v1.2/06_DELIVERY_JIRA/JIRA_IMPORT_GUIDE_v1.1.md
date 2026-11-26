# Jira import 1.1 preflight

1. Use `Jira_Import.csv` ONLY (consolidated). Do not import preserved v1.0 simultaneously.
2. Create version labels P0/P1/P2 and Epic/Story/Task types. Every `Parent ID` must point to an existing issue of type Epic in same import.
3. Jira Cloud CSV field mappings vary; first import only sample Epic + Story + Task to a test project; validate parent links and UTF-8 Arabic.
4. After a clean test, import remaining; compare count, parent IDs and labels against `scripts/validate_blueprint.py` output.
5. Convert detailed QA `test_cases.csv`/Gherkin to Xray or Zephyr only if purchased/authorized; no fake execution results.
6. Store design frame, PR, coverage and decision evidence on each ticket. Escalate missing API or consent decision as Blocked, do not auto-Done.
