# Headless ticket implementation kickoff (secure runner only)

> **Not an active automation:** requires installed Gemini CLI, repo access, Jira credentials, approved scope, required secrets and operator enablement.

1. Select one Ready ticket from live Jira; verify all hard prerequisites are merged.
2. Open its Markdown in `planning/tasks/`; resolve owning repository (api/web/flutter).
3. Clone latest protected main in isolated workspace using short-lived GitHub App credential.
4. Start with:

```
gemini --model gemini-3.8-flash --prompt "$(cat USAYD_GEMINI_CODEX_AUTONOMOUS_MASTER_PROMPT.md; cat planning/tasks/USYD-TXXXX.md)"
```

5. Review actual code/files; run repo-local test commands before pushing.
6. Open draft PR initially; run checks, independent review, revise. Don't self-approve.
7. Apply `safe-automerge` label ONLY to explicitly low-risk docs/test-fixtures after security triage; otherwise ask human reviewer. GitHub protects main and merges after checks/required approvals.
8. Observe real merge SHA and staging verification, then move Jira to Done. Next eligible ticket is processed by scheduler/external runner.

Gemini CLI supports headless `-p` or `--prompt` and `--model` (`-m`) in current Google docs. Verify CLI runtime and model availability before unattended usage.
