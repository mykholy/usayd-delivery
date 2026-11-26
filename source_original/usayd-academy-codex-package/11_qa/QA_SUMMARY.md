# QA summary — final cycle evidence

- Final audit: cycle 5. All cycles, issues and fixes are in `AUDIT_CYCLES.md` and `ISSUE_REGISTER.csv`. Raw JSON results are in `automated/`.
- The matrix covers all 178 boards (169 product screens + 9 journey boards) × AR/EN × light/dark × 9 widths (320–1920 px), plus 169 screens × 6 states × AR/EN × light/dark × 390/1440 px, plus a keyboard focus pass. Final cycle: `cycle12` (see `REGRESSION_REPORT.md`).
- Screen matrix: `SCREEN_VISUAL_QA_160.csv`, with `matrix_status` = PASS (automated) / FAIL / BLOCKED. Screen reader and human visual review are **NOT TESTED** for every screen.

## Status counts
- {k}: {v}
- {k}: {v}
- {k}: {v}
- {k}: {v}

`BLOCKED_BY_DECISION` = an owner decision or owner content is needed · `BLOCKED_BY_API` = the contract is missing from OpenAPI · `NEEDS_VISUAL_REVIEW` = density work is outstanding (OPEN-01) · `CHANGES_MADE` = remediated, automated checks pass, human sign-off pending.

## Before and after
`before_contact_sheets/` holds the auditor's mosaics. `after_contact_sheets/` holds this work.
