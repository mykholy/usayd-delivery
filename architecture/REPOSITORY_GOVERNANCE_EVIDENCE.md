# Repository governance — verified evidence and remaining checklist

USYD-T0021 / [USYD-54](https://mykholy.atlassian.net/browse/USYD-54), 2026-11-27. Read-only verification via connected GitHub repository metadata, branch search and collaborator permission query; no settings mutations.

| Repository | Default branch | main exists | mykholy permission | Live rulesets / branch protection |
|---|---|---|---|---|
| mykholy/usayd-api | main | yes | admin | Not exposed by connector |
| mykholy/usayd-web | main | yes | admin | Not exposed by connector |
| mykholy/usayd-flutter | main | yes | admin | Not exposed by connector |
| mykholy/usayd-delivery | main | yes | admin | Not exposed by connector |

The repository metadata and collaborator permission do not prove protection or enforcement. The owner confirmed no independent technical/security approver has yet been appointed. Do not create fictional CODEOWNERS, weaken checks, change permissions, bypass required reviews or force-push. Flutter read-only.

## Owner verification checklist

1. In repository Settings → Rules → Rulesets (and Settings → Branches if classic protections exist), confirm the active policy targets main, including enforcement status and any bypass actors.
2. Verify required pull requests, independent review where required, dismissal of stale approvals or last-push review, conversation resolution, and required actual CI checks. API checks include API CI, Supply chain security and Independent PR Code Quality Review; Delivery requires Delivery validation. Web and Flutter required checks must reflect their actual workflows; do not invent check contexts.
3. Verify force-push and deletion prevention, default branch and relevant repository auto-delete policy; preserve docs and audit history. Check account plan supports enforcement on these repositories. Do not remove existing protection or use bypasses to make a PR merge.
4. Capture sanitized screenshots of rules and targets (no credentials). If using an authorized local GitHub CLI, read-only commands `gh api repos/mykholy/usayd-api/branches/main/protection` and `gh api repos/mykholy/usayd-api/rules/branches/main` may provide evidence; repeat for the other repositories as appropriate. Redact sensitive details. HTTP 403/404 is not proof that rules are absent.

[API rules](https://github.com/mykholy/usayd-api/settings/rules) · [Web rules](https://github.com/mykholy/usayd-web/settings/rules) · [Flutter rules](https://github.com/mykholy/usayd-flutter/settings/rules) · [Delivery rules](https://github.com/mykholy/usayd-delivery/settings/rules).

USYD-54 remains In Progress; USYD-81 has a hard prerequisite on USYD-T0021. No next-stage bootstrap merge or completion while this gate remains open. No new personal access token or production credential requested.

## Owner confirmation and direct evidence — 2026-11-27

All four repositories now public (GitHub metadata); owner explicitly accepts visibility and confirmed equivalent Protect main rulesets with repository-specific checks. Delivery Ruleset [28216946](https://github.com/mykholy/usayd-delivery/settings/rules/28216946) screenshot and authenticated page show Active, default main, empty bypass, restricted deletion, required PR/status checks, and blocked force pushes. Nested check names, strict-up-to-date and conversation resolution were collapsed; other repositories owner-attested, not directly inspected. No specialist reviewers appointed. USYD-54 advanced to In Review, not Done. No settings changed by agent. Delivery validation passed on 02e1714 (run 45911306404); independent review check not available. Web prerequisite remains open.
