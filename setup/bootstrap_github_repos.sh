#!/usr/bin/env bash
# Idempotent opt-in GitHub repo creation; DRY RUN by default; requires gh auth.
set -euo pipefail
OWNER="${GH_OWNER:-mykholy}"
MODE="${1:---dry-run}"
[[ "$MODE" == "--dry-run" || "$MODE" == "--apply" ]] || { echo 'Usage: GH_OWNER=mykholy ./bootstrap_github_repos.sh [--dry-run|--apply]'; exit 2; }
command -v gh >/dev/null || { echo 'Install and authenticate GitHub CLI first'; exit 3; }
for repo in usayd-api usayd-web usayd-flutter; do
  if gh repo view "$OWNER/$repo" >/dev/null 2>&1; then
    echo "EXISTS $OWNER/$repo (will not alter it)"
  elif [[ "$MODE" == '--apply' ]]; then
    echo "CREATING private $OWNER/$repo"
    gh repo create "$OWNER/$repo" --private --description "Usayd Academy independent $repo application" --disable-issues=false
  else
    echo "WOULD CREATE private $OWNER/$repo"
  fi
done
printf '\nIMPORTANT: bootstrap templates are not application code. Initialize each repo with framework skeleton and required review rules before CI runs.\n'
