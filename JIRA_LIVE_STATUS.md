# Jira live synchronization

Checked 2026-11-23: Atlassian resource `mykholy.atlassian.net` advertises read/write, but `listJiraProjects` returned `404 Site temporarily unavailable`; prior attempt at Jira JQL and boards also failed. **No Jira items or sprints created by this response.**

Use existing `jira/jira_sync.py` and `jira/sprint_and_links_sync.py` after the site is reachable; first run `--dry-run`, validate project, field mapping and issue counts, and only then write. Do not upload all sprint allocations as confirmed dates or launch 91 sprints simultaneously.
