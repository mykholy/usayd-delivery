# Automation integration and deployment checklist

This directory contains REAL templates and a non-deployed AI reviewer script. Merely unzipping it does **not** create GitHub repos, install Gemini CLI, configure GitHub Actions, sync Jira, or run a 24/7 agent. The owner must provision credentials and enable workflows.

## 1. Configure repositories

- `usayd-api`: Laravel 13/MySQL 8.4/Redis with migrations, queues and API contract CI.
- `usayd-web`: Next.js stable pinned in lockfile, typed API SDK, i18n, visual & Playwright test suite.
- `usayd-flutter`: Flutter stable pinned/tested, state management chosen via ADR, widget/golden/unit tests.

Copy corresponding contents of `repo_bootstrap/<repo>/.github/` and the `AGENTS.md`. Do not copy another repo's workflows. `repo_bootstrap` is NOT a functional application scaffold.

## 2. Permissions and required secrets

- `GEMINI_API_KEY` (external reviewer), repo variable `ALLOW_EXTERNAL_AI_REVIEW=yes` **only after approving data sharing**. All PR code fragments are submitted to the configured provider (limit 65K characters), so restrict sensitive PRs to local human review.
- `USAYD_AUTOMATION_ENABLED` must be explicitly `true` before any scheduled external runner may process tasks.
- Configure a short-lived GitHub App token for PR creation and cross-repo checkouts; no admin token or branch protection bypass to an agent.
- Jira: `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY`, `JIRA_BOARD_ID` (never commit to source). Import via scripts *after* Jira works.
- Branch rules: protect main; forbid force pushes and direct pushes; require unique real CI status checks + `independent-ai-review` check, no bypass by agent identity. Code owner + human review for sensitive paths.
- Auto-merge: enable in repo settings; only workflows with label `safe-automerge` and conservative allowlist can arm it automatically. All other tickets remain waiting for required approvals, then GitHub auto-merge may complete.

## 3. Execution operator (deployment not included)

1. On secure runner, check Jira and gate decisions and choose one actually READY ticket.
2. Use Gemini CLI headless `gemini -p "$(cat prompt.txt)" -m gemini-3.8-flash` or an equally authorized Codex invocation; **verify CLI syntax and supported model in your runtime before relying on this**.
3. Work in isolated clone and low-privilege credentials; never give model GitHub admin permissions. Enforce one active writer per repo.
4. Verify code and tests, open PR, run CI + independent review, iterate fixes, submit for review where necessary.
5. On confirmed merge + staging smoke, transition Jira to Done, release dependency, repeat within authorized runner execution. Unavailable Jira = no false Done.

## 4. Automated GitHub review

- Template `.github/workflows/ai-review.yml` executes `automation/pr_review.py` after owner enables external AI review. Copy script into each production repo under `automation/`.
- The script fails closed on missing approval/API key, overly large diffs, suspicious secrets, invalid AI output and P0/P1 findings.
- Any model-generated result is only an additional CI gate, not independent human approval and not proof of test execution.
- `safe-automerge.yml` never checks out untrusted PR code; it labels only docs/test-only changes as eligible and uses GitHub native merge protections.
- For features touching security/payments/guardian/recording/AI/Quran/payroll/production/migrations, require human review even if Gemini says PASS.

## 5. Suggested dry-run checks

```
python automation/preflight.py
python jira/jira_sync.py --dry-run  # requires Jira credentials + reachable site
```

## 6. Sources

- https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/automatically-merging-a-pull-request
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://google-gemini.github.io/gemini-cli/docs/cli/headless.html
