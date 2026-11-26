# Build the safe automation runner for Usayd Academy

You are Gemini operating in a connected engineering environment. Before executing a product ticket, implement or configure a **bounded, auditable external runner** for three GitHub repositories and Jira. A chat prompt alone cannot guarantee continuous background operation.

The runner must authenticate through a scoped GitHub App and supported Jira auth, store credentials in a secret manager, poll only READY tickets, respect `Depends On` and decisions, create one PR per task, monitor real CI status, and only merge when actual branch protection/reviewer approvals permit it. Expose dry-run, max tickets per run, max wall-clock, explicit stop on failure, and no access to production secrets for code-generation runs. Log issue key, source SHA, PR URL, CI URL and result to an audit trail.

Implement a test-only sandbox mode first, prove idempotency after partial failure, then request authorization to activate scheduling. Never claim the runner exists or the jobs are scheduled until those exact capabilities are verified by the host.
